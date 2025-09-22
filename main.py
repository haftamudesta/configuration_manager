def add_setting(settings, key_value_tuple):
    """
    Add a new setting to the settings dictionary.
    """
    key, value = key_value_tuple
    key = key.lower()
    value = value.lower()
    
    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        settings[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"
def update_setting(settings, key_value_tuple):
    """
    Update an existing setting in the settings dictionary.
    """
    key, value = key_value_tuple
    key = key.lower()
    value = value.lower()
    
    if key in settings:
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."
def delete_setting(settings, key):
    """
    Delete a setting from the settings dictionary.
    """
    key = key.lower()
    
    if key in settings:
        del settings[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"
def view_settings(settings):
    """
    View all current settings.
    """
    if len(settings) == 0:
        return "No settings available."
    else:
        result = "Current User Settings:\n"
        for key, value in settings.items():
            result += f"{key.capitalize()}: {value}\n"
        return result  
test_settings = {
    'theme': 'light',
    'language': 'english',
    'notifications': 'enabled'
}