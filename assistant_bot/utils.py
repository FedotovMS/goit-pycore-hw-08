def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return f"Error: {e}"
        except KeyError:
            return "Error: Contact not found."
        except IndexError:
            return "Error: Invalid input."
    return wrapper


def parse_input(user_input):
    parts = user_input.split()
    return parts[0], parts[1:]