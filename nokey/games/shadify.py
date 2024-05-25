import requests_cache
from .. helperFuncs import make_request as mr

class Shadify:
    """
    A class for interacting with the Shadify API.
    
    Attributes:
    - base_url: The base URL of the API.
    - about: A short description of the API.
    """
    def __init__(self, use_caching=False, cache_name="shadify_cache", backend="sqlite", expire_after=3600):
        self.base_url = "https://shadify.dev/api/"
        self.about = "Shadify is a powerful REST API service provides a collection of different puzzle types, like crosswords, Sudoku, word search and so on. The API allows users to generate data for puzzles, check the correctness of solutions, and configure various parameters to change the difficulty of the puzzles."
        
        if use_caching:
            requests_cache.install_cache(cache_name, backend=backend, expire_after=expire_after)
            
    def get_docs_url(self):
        """
        Returns the URL for the Shadify API documentation.
        
        Args:
        - None
        
        Returns:
        - string: The URL for the API docs.
        """
        return "https://shadify.dev/introduction.html"
        
    # SUDOKU
    def about_sudoku(self):
        """
        Returns a short description of the game.
        
        Args:
        - None
        
        Returns:
        - string: A short description of the game.
        """
        return "Sudoku is a popular number puzzle game. The essence of the game is to fill free cells with numbers from 1 to 9 so that in each row, each column and each small 3×3 square each digit occurs only once."
    
    def generate_random_sudoku(self, fill=30):
        """
        Returns a random sudoku puzzle, both the finished ("grid") and the unfinished ("task") versions.
        
        Args:
        - fill (int): A number from 0 to 50 that corresponds to the field fill level (as a percentage). Default is 30.
        
        Returns:
        - dict: A dictionary containing two grids: the unfinished and finished versions of the puzzle.
        """
        if fill > 50:
            print("Fill value cannot exceed 50.")
            exit()
        endpoint = f"sudoku/generator?fill={fill}"
        return mr.make_request(self.base_url+endpoint)
        
    def check_sudoku(self, puzzle_grid):
        """
        Returns whether or not the provided sudoku grid is correct or not.
        
        Args:
        - puzzle_grid (array): A two-dimensional grid (list of lists), where each list is a row in the sudoku grid.
        
        Returns:
        - dict: A dictionary containing whether or not the given puzzle is correctly solved, as well as which row contains incorrect values.
        """
        payload = {
                    "task": puzzle_grid
        }
        endpoint = "sudoku/verifier"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=payload)
        
    # TAKUZU
    def about_takuzu(self):
        """
        Returns a short description of the game.
        
        Args:
        - None
        
        Returns:
        - string: A short description of the game.
        """
        return "Takuzu (a.k.a. Binairo) is an entertaining puzzle game with simple rules. All you have to do is to fill a square field of a certain size with two digits (or colors) while following three simple rules: 1) Each column and each row must be unique. 2) Each row and each column must have an equal number of tiles of each digit. 3) No more than two tiles with the same digit in a row (110001 is wrong, 110010 is right)."
        
    def generate_random_takuzu(self, size=8, fill=33):
        """
        Returns a random takuzu puzzle, both the finished ("field") and the unfinished ("task") versions.
        
        Args:
        - size (int): An even number from 4 to 12, which specifies the size of the field. Default is 8.
        - fill (int): A number from 0 to 100 that corresponds to the field fill level (as a percentage). Default is 33.
        
        Returns:
        - dict: A dictionary containing two grids: the unfinished and finished versions of the puzzle, as well as the size of the grid.
        """
        if (size > 12 or size < 4 or size % 2 != 0) and fill > 100:
            print("Size must be an even number between 4 and 12, inclusive; and fill cannot exceed 100.")
            exit()
        if size > 12 or size < 4 or size % 2 != 0:
            print("Size must be an even number between 4 and 12, inclusive.")
            exit()
        if fill > 100:
            print("Fill value cannot exceed 100.")
            exit()
        endpoint = f"takuzu/generator?size={size}&fill={fill}"
        return mr.make_request(self.base_url+endpoint)
        
    def check_takuzu(self, puzzle_grid):
        """
        Returns whether or not the provided takuzu grid is correct or not.
        
        Args:
        - puzzle_grid (array): A two-dimensional grid (list of lists), where each list is a row in the takuzu grid.
        
        Returns:
        - dict: A dictionary containing whether or not the given puzzle is correctly solved, as well as which row contains incorrect values.
        """
        payload = {
                    "task": puzzle_grid
        }
        endpoint = "takuzu/verifier"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=payload)
        
    # SET (I know nothing about this game or how to make it work, so read the documentation or Wikipedia to learn how it works.)
    def about_set(self):
        """
        Returns a short description of the game.
        
        Args:
        - None
        
        Returns:
        - string: A short description of the game.
        """
        return "Set (card game) – a fascinating card game. The game deck consists of 81 cards, each with one, two, or three of the same symbol (rhombus, oval, or wave) of the same color (red, green, or purple) and texture (shaded, shaded, or outline only). The essence of the game is to find a set - a set of three cards that meets certain conditions."
        
    def get_all_set_cards(self, possible_sets=True):
        """
        Always returns the same array of 81 objects. Each object corresponds to one of the cards.
        
        Args:
        - possible_sets (bool): A true/false string that enables/disables the search for possible sets in the current layout. The list of possible sets is not necessary for the game and acts only as a hint and evidence that sets exist in the current layout.
        
        Returns:
        - dict: A dictionary containing 
        """
        endpoint = f"set/start?possible-sets={possible_sets}"
        return mr.make_request(self.base_url+endpoint)
        
    def load_set_state(self, state, possible_sets=True, action=None, cards=None):
        """
        Always returns the same array of 81 objects. Each object corresponds to one of the cards.
        
        Args:
        - A string of hyphenated, no spaced numbers representing the state of the cards.
        - possible_sets (bool): A true/false string that enables/disables the search for possible sets in the current layout. The list of possible sets is not necessary for the game and acts only as a hint and evidence that sets exist in the current layout.
        - action (str): Optional. The add/remove string, which allows you to perform the appropriate action with the current game state. The add string adds 3 random cards from the current freeCards array to the current layout (available only if the layout size does not exceed 20 cards). The remove string removes the specified combination of three cards from the current layout. To do this you must use the cards parameter. Default is None.
        - cards (str): Required if action=remove. A string of the form 1-2-3, where each number corresponds to the unique identifier of one of the cards that make up the set. Default is None.
        
        Returns:
        - dict: A dictionary containing 
        """
        if action == "remove" and cards is not None:
            endpoint = f"set/{state}?possible-sets={possible_sets}&action={action}&cards={cards}"
        if action == "remove" and cards is None:
            print("If value of action is 'removed,' cards cannot be None.")
            exit()
        if action == "add":
            endpoint = f"set/{state}?possible-sets={possible_sets}&action={action}"   
        if action is None:
            endpoint = f"set/{state}?possible-sets={possible_sets}" 
        return mr.make_request(self.base_url+endpoint)
        
    # MATH
    def about_math(self):
        """
        Returns a short description of the game.
        
        Args:
        - None
        
        Returns:
        - string: A short description of the game.
        """
        return "A module for generating random mathematical expressions. Great for creating various simulators, where you'll have to wiggle your brain."
        
    def generate_addition(self, min_first=1, max_first=99, min_second=1, max_second=99):
        """
        Returns a generated addition expression.
        
        Args:
        - min_first (int): Optional. Minimum value of the first number in the expression. Default is 1.
        - max_first (int): Optional. Maximum value of the first number in the expression. Default is 99.
        - min_second (int): Optional. Minimum value of the second number in the expression. Default is 1.
        - max_second (int): Optional. Maximum value of the second number in the expression. Default is 99.   
        
        Returns:
        - dict: A dictionary containing the generated expression.
        """
        endpoint = f"math/add?min-first={min_first}&max-first={max_first}&min-second={min_second}&max-second={max_second}"
        return mr.make_request(self.base_url+endpoint)
        
    def generate_subtraction(self, min_first=1, max_first=99, min_second=1, max_second=99, negative=0):
        """
        Returns a generated subtraction expression.
        
        Args:
        - min_first (int): Optional. Minimum value of the first number in the expression. Default is 1.
        - max_first (int): Optional. Maximum value of the first number in the expression. Default is 99.
        - min_second (int): Optional. Minimum value of the second number in the expression. Default is 1.
        - max_second (int): Optional. Maximum value of the second number in the expression. Default is 99.
        - negative (int): Optional. The number 0/1 which enables/disables the possibility of generating a result with a negative value for expressions with subtraction. Initially, when generating an expression with subtraction, the first number is always greater than the second number. To change this behavior, use this parameter. Default is 0.   
        
        Returns:
        - dict: A dictionary containing the generated expression.
        """
        endpoint = f"math/sub?min-first={min_first}&max-first={max_first}&min-second={min_second}&max-second={max_second}&negative={negative}"
        return mr.make_request(self.base_url+endpoint)
        
    def generate_multiplication(self, min_first=1, max_first=99, min_second=1, max_second=99):
        """
        Returns a generated multiplication expression.
        
        Args:
        - min_first (int): Optional. Minimum value of the first number in the expression. Default is 1.
        - max_first (int): Optional. Maximum value of the first number in the expression. Default is 99.
        - min_second (int): Optional. Minimum value of the second number in the expression. Default is 1.
        - max_second (int): Optional. Maximum value of the second number in the expression. Default is 99.
        
        Returns:
        - dict: A dictionary containing the generated expression.
        """
        endpoint = f"math/mul?min-first={min_first}&max-first={max_first}&min-second={min_second}&max-second={max_second}"
        return mr.make_request(self.base_url+endpoint)
        
    def generate_division(self, min_first=1, max_first=99):
        """
        Returns a generated division expression.
        
        Args:
        - min_first (int): Optional. Minimum value of the first number in the expression. Default is 1.
        - max_first (int): Optional. Maximum value of the first number in the expression. Default is 99. 
        
        Returns:
        - dict: A dictionary containing the generated expression.
        """
        endpoint = f"math/div?min-first={min_first}&max-first={max_first}"
        return mr.make_request(self.base_url+endpoint)
        
    def generate_quadratic_equation(self, min_a=1, max_a=20, min_b=1, max_b=40, min_c=1, max_c=20):
        """
        Returns a generated quadratic equation.
        
        Args:
        - min_a (int): Minimum value of coefficient a. Default is 1.
        - max_a (int): Maximum value of coefficient a. Default is 20.
        - min_b (int): Minimum value of coefficient b. Default is 1.
        - max_b (int): Maximum value of coefficient b. Default is 40.
        - min_c (int): Minimum value of coefficient c. Default is 1.
        - max_c (int): Maximum value of coefficient c. Default is 20.
       
        Returns:
        - dict: A dictionary containing the generated equation.
        """
        endpoint = f"math/quad?min-a={min_a}&max-a={max_a}&min-b={min_b}&max-b={max_b}&min-c={min_c}&max-c={max_c}"
        return mr.make_request(self.base_url+endpoint)
        
    
    # SCHULTE TABLES
    def about_schulte(self):
        """
        Returns a short description of the game.
        
        Args:
        - None
        
        Returns:
        - string: A short description of the game.
        """
        return "Schulte Tables – tables with randomly arranged objects (usually numbers or letters) used to test and develop quickness of finding these objects in a certain order (usually in ascending order for numbers and alphabetical order for letters). Exercises with tables can improve peripheral visual perception, which will have a positive impact on the skill of speed reading."
        
    def generate_random_schulte_table(self, size=5, mode="number"):
        """
        Returns a random schulte table.
        
        Args:
        - size (int): The size of the generated table. The available range is from 1 to 15. Default is 5.
        - mode (str) The number / alphabet string, which defines the generated values for the table: numbers or letters. If alphabet is selected, the size parameter will always be 5. Default is number
        
        Returns:
        - dict: A dictionary containing a grid representing the schulte table.
        """
        if size < 1 or size > 15:
            print("Size must be between 1 and 15, inclusive.")
            exit()
        endpoint = f"schulte/generator?size={size}&mode={mode}"
        return mr.make_request(self.base_url+endpoint)  
        
    # MINESWEEPER
    def about_minesweeper(self):
        """
        Returns a short description of the game.
        
        Args:
        - None
        
        Returns:
        - string: A short description of the game.
        """
        return "Minesweeper – a computer puzzle game in which the playing field is divided into adjacent cells, some of which are mined. The number of mined cells is known. The goal of the game is to open all the cells that do not contain mines. This game has become quite popular among Windows users, since it was pre-installed by default on older versions of that OS."

    def generate_random_minesweeper_field(self, start, width=9, height=9, mines=12):
        """
        Returns a randomly generated minesweeper grid.
        
        Args:
        - start (str): A string of the form 1-2, which sets the starting position of the player. There will never be mines in and around this position. The first number is the X coordinate (from 1 to the value of the widht parameter), the second number is the Y coordinate (from 1 to the value of the height parameter).
        - width (int): The number that sets the width of the generated field. The total number of cells in the field must not exceed 1000. Default is 9.
        - height (int): The number that sets the height of the generated field. The total number of cells in the field must not exceed 1000. Default is 9.
        - mines (int): The number that sets the number of mines on the field. The number of mines must not exceed 25% of the total number of cells on the field. Default is 12.
        
        Returns:
        - dict: A dictionary containing the minesweeper board grid and other data.
        """
        if width * height > 1000:
            print(f"The width and height given would result in {width*height} cells, but total cells must not exceed 1000. Adjust dimensions accordingly.")
            exit()
        if mines > .25 * width * height:
            print(f"Number of mines given would be {mines/(width*height)} of total cells, but number of mines may not exceed .25 of total cells. Adjust number of mines accordingly.")
            exit()
        endpoint = f"minesweeper/generator?start={start}&width={width}&height={height}&mines={mines}"
        return mr.make_request(self.base_url+endpoint)
        
    # WORDSEARCH
    def about_wordsearch(self):
        """
        Returns a short description of the game.
        
        Args:
        - None
        
        Returns:
        - string: A short description of the game.
        """
        return "Word search is a puzzle consisting of letters of words placed in a square or rectangular grid. The aim of the puzzle is to find and mark all the words hidden in the grid. The words can be placed horizontally, vertically or diagonally."
        
    def generate_random_wordsearch_grid(self, width=9, height=9):
        """
        Returns a randomly generated wordsearch grid.
        
        Args:
        - width (int): A number from 5 to 20 that specifies the width of the grid. The total number of cells in the field must not exceed 256. Default is 9.
        - height (int): A number from 5 to 20 that specifies the width of the grid. The total number of cells in the field must not exceed 256. Default is 9.
        
        Returns:
        - dict: Returns a dictionary containing the wordsearch grid and the key.
        """
        if width < 5 or width > 20:
            print("Value of width must be between 5 and 20, inclusive.")
            exit()
        if height < 5 or height > 20:
            print("Value of height must be between 5 and 20, inclusive.")
            exit()
        if width * height > 256:
            print(f"Width and height given would result in {width*height} cells, but cells must not exceed 256. Adjust dimensions accordingly.")
            exit()
        endpoint = f"wordsearch/generator?width={width}&height={height}"
        return mr.make_request(self.base_url+endpoint)
        
    # ANAGRAMS
    def about_anagram(self):
        """
        Returns a short description of the game.
        
        Args:
        - None
        
        Returns:
        - string: A short description of the game.
        """
        return "Anagrams is a whole type of puzzles associated with composing all possible words from a given set of letters. This module implements the simplest variation of anagrams: a random word is given, the letters of which should be used to compose as many other words as possible."
        
    def generate_random_anagram(self):
        """
        Returns a word as the task and the possible words that can be composed from the word.
        
        Args:
        - None
        
        Returns:
        - dict: A dictionary containing a task word and a list of words that can be composed from this word.
        """
        endpoint = "anagram/generator"
        return mr.make_request(self.base_url+endpoint)
        
    # COUNTRIES
    def about_countries(self):
        """
        Returns a short description of the game.
        
        Args:
        - None
        
        Returns:
        - string: A short description of the game.
        """
        return "Countries module allows you to generate quizes such as guess the capital or guess the country from an image of the flag. It is a simple and useful module for creating applications to test and practice knowledge of all countries."
        
    def generate_capital_quiz(self, variants=4, amount=1):
        """
        Returns a country capital quiz and answer the the quiz.
        
        Args:
        - variants (int): Optional. A number from 2 to 6 corresponding to the number of different options from which you have to choose the correct capital of the given country. Default is 4.
        - amount (int): Optional. A number from 1 to 20 which is responsible for the number of quizzes returned. The use of this parameter ensures that among all quizzes received, all will be unique. Default is 1.
        
        Returns:
        - dict: A dictionary containing a country name, a link to its flag, possible answers for its capital, and correct answer.
        """
        if variants < 2 or variants > 6:
            print("Value of variants must be between 2 and 6, inclusive. Please adjust value accordingly.")
            exit()
        if amount < 1 or amount > 20:
            print("Value of amount must be between 1 and 20, inclusive. Please adjust value accordingly.")
            exit()
        endpoint = f"countries/capital-quiz?variants={variants}&amount={amount}"
        return mr.make_request(self.base_url+endpoint)
        
    def generate_country_quiz(self, variants=4, amount=1):
        """
        Returns a country capital quiz and answer the the quiz.
        
        Args:
        - variants (int): Optional. A number from 2 to 6 corresponding to the number of different options from which you have to choose the the correct country of the given flag image. Default is 4.
        - amount (int): Optional. A number from 1 to 20 which is responsible for the number of quizzes returned. The use of this parameter ensures that among all quizzes received, all will be unique. Default is 1.
        
        Returns:
        - dict: A dictionary containing a link to a country's flag, possible answers for the country, and correct answer.
        """
        if variants < 2 or variants > 6:
            print("Value of variants must be between 2 and 6, inclusive. Please adjust value accordingly.")
            exit()
        if amount < 1 or amount > 20:
            print("Value of amount must be between 1 and 20, inclusive. Please adjust value accordingly.")
            exit()
        endpoint = f"countries/country-quiz?variants={variants}&amount={amount}"
        return mr.make_request(self.base_url+endpoint)
        
    # CAMP
    def about_camp(self):
        """
        Returns a short description of the game.
        
        Args:
        - None
        
        Returns:
        - string: A short description of the game.
        """
        return "Camp (aka Tents and trees, Tents) is a logic puzzle with simple rules and challenging solutions. The rules of Camp are simple: 1) Pair each tree with a tent adjacent horizontally or vertically. This should be a 1 to 1 relation. 2) Tents never touch each other even diagonally. 3) The clues outside the grid indicate the number of tents on that row/column."
    
    def generate_random_camp_task(self, width=7, height=7, solution=True):
        """
        Returns a camp game grid and the solution.
        
        Args:
        - width (int): Optional. A number from 5 to 15 which corresponds to the width of the generated field. Default is 7.
        - height (int): Optional. A number from 5 to 15 which corresponds to the height of the generated field. Default is 7.
        - solution (bool): Optional. The true/false value that specifies whether the solution should be sent with the task or not. Default is True.
        
        Returns:
        - dict: A dictionary containing the camp grid task and the solution if solution is True.
        """
        if width < 5 or width > 15:
            print("Value of width must be between 5 and 15, inclusive. Please adjust value accordingly.")
            exit()
        if height < 5 or height > 15:
            print("Value of height must be between 5 and 15, inclusive. Please adjust value accordingly.")
            exit()
        endpoint = f"camp/generator?width={width}&height={height}&solution={solution}"
        return mr.make_request(self.base_url+endpoint)
        
    def check_camp_task(self, row_tents, column_tents, solution):
        """
        Checks the given camp task grid and returns whether or not it is correct.
        
        Args:
        - row_tents (list): A list containing the row tents values.
        - column_tents (list). A list containing the column tents values.
        - solution (array): A two dimensional array containing the solution grid.
        
        Returns:
        - dict: A dictionary containing whether or not the solution is valid, where the error occurs if it is not, and a message.
        """
        payload = {
                "rowTents": row_tents,
                "columnTents": column_tents,
                "solution": solution
        }
        endpoint = "camp/verifier/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=payload)
        
    # KUROMASU
    def about_kuromasu(self):
        """
        Returns a short description of the game.
        
        Args:
        - None
        
        Returns:
        - string: A short description of the game.
        """
        return "Kuromasu is a puzzle played on a rectangular grid. Some of these cells have numbers in them. Each cell may be either black or white. The object is to determine what type each cell is. The following rules determine which cells are which: 1) Each number on the board represents the number of white cells that can be seen from that cell, including itself. A cell can be seen from another cell if both cells are within the same row or column, and there are no black cells between them in that row or column. 2) Numbered cells must not be black. 3) No two black cells must be horizontally or vertically adjacent. 4) All the white cells must be connected horizontally or vertically."
    
    def generate_random_kuromasu_task(self, width=5, height=5, fill=30):
        """
        Returns a kuromasu task grid and the solution.
        
        Args:
        - width (int): Optional. A number from 4 to 15 which corresponds to the width of the generated field. Default is 5.
        - height (int): Optional. A number from 4 to 15 which corresponds to the height of the generated field. Default is 5.
        - fill (int): Optional. A number from 10 to 50 which corresponds to the % level of filling the task with ready cells.
        
        Returns:
        - dict: A dictionary containing the kuromasu grid task and the solution.
        """
        if width < 4 or width > 15:
            print("Value of width must be between 4 and 15, inclusive. Please adjust value accordingly.")
            exit()
        if height < 4 or height > 15:
            print("Value of height must be between 4 and 15, inclusive. Please adjust value accordingly.")
            exit()
        if fill < 10 or fill > 50:
            print("Value of fill must be between 10 and 50, inclusive.")
        endpoint = f"kuromasu/generator?width={width}&height={height}&fill={fill}"
        return mr.make_request(self.base_url+endpoint)
        
    def check_kuromasu_task(self, solution):
        """
        Checks the given kuromasu task grid and returns whether or not it is correct.
        
        Args:
        - solution (array): A two dimensional array containing the solution grid.
        
        Returns:
        - dict: A dictionary containing whether or not the solution is valid, where the error occurs if it is not.
        """
        payload = {
                "solution": solution
        }
        endpoint = "kuromasu/verifier/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=payload)
        
    # MEMORY
    def about_memory(self):
        """
        Returns a short description of the game.
        
        Args:
        - None
        
        Returns:
        - string: A short description of the game.
        """
        return "Memory is a puzzle that's great for practicing memorization. You are given a field with a random set of elements, and each element in the field occur several times (usually 2 or 3). You have some time to remember the position of all the elements on the field, and then all of them are hidden and your task is to open pairs of identical elements one by one trying to make as few mistakes as possible."
  
    def generate_random_memory_grid(self, width=6, height=4, pair_size=3, show_positions=True):
        """
        Returns a memory grid and pair positions.
        
        Args:
        - width (int). Optional. A number corresponding to the width of the generated grid. The total number of cells in the grid must not exceed 52 multiplied by the pair-size. Default is 6.
        - height (int): Optional. A number corresponding to the height of the generated grid. The total number of cells in the grid must not exceed 52 multiplied by the pair-size. Default is 4.
        - pair_size (int): Optional. A number corresponding to the size of a pair of identical elements. The value must be a multiple of the total number of cells in the grid. Available values: 2, 3, 4. Default is 3.
        - show_positions (bool): Optional. A true/false value that determines whether to send position information for each pair of elements. Default is True.
        
        Returns:
        - dict: A dictionary containing a memory grid and pair positions.
        """
        if width * height > 52 * pair_size:
            print(f"The total number of cells in the grid are {width*height}, but total cells must not exceed 52 times the pair_size. Please adjust dimensions accordingly.")
            exit()
        endpoint = f"memory/generator?width={width}&height={height}&pair-size={pair_size}&show-positions={show_positions}"
        return mr.make_request(self.base_url+endpoint)
        
        
            
    
    
    
        
    
        
  
   
        
    
    
        