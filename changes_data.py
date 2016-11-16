def changes_data(f):
    def wrapper(*args, **kwargs):
        res = f(*args, **kwargs)
        args[0].dataChanged.emit()
        return res
    return wrapper
