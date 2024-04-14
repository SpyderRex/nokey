from . nokey_apis import nokey_apis

def get_api_list():
    """
    Prints out the APIs in a visually pleasing format with headings for the categories 
    and the individual APIs under the respective headings.

    Args:
    - None
    
    Returns:
    - string: A list of the apis supported by the nokey package.
    """

    # ANSI escape codes for colors
    green_color = "\033[92m"  # Green
    blue_color = "\033[94m"   # Blue
    reset_color = "\033[0m"   # Reset color to default

    for category, apis in nokey_apis.items():
        print(f"{green_color}{category}{reset_color}")
        print("-" * (len(category) + 6))  # Line for aesthetics
        for api in apis:
            print(f"{blue_color}{api}{reset_color}")
        print()  # Empty line for better readability between categories
    return ""

