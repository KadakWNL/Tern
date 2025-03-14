import logging

if __name__ == "__main__":
    # Disable all logging messages
    logging.disable(logging.ERROR,logging.WARNING,logging.WARNING)

    try:
        import work_GUI_PT2
    except Exception as e:
        pass