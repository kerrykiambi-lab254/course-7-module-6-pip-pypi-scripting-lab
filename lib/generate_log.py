from datetime import datetime

def generate_log(data):
    if not isinstance(data, list):
        raise ValueError("Input must be a list")

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    with open(filename, "w") as file:
        file.write("\n".join(data))

    print(f"Log written to {filename}")

    return filename
