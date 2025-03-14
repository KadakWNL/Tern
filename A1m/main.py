import logging

if __name__ == "__main__":
    # Disable all logging messages
    logging.disable(logging.CRITICAL)

    try:
        import work_GUI
    except Exception as e:
        pass