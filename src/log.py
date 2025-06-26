import time
import random


def generate_logs(log_file: str = "access.log", num_logs: int | None = None) -> None:
    """
    Generate logs to a file.

    :param log_file: The file to which logs will be written.
    :param num_logs: The number of logs to produce. If None, logs will be produced indefinitely.
    :raises ValueError: If num_logs is a negative integer.
    :raises FileNotFoundError: If the log file cannot be opened.
    :raises KeyboardInterrupt: If the user interrupts the log production.
    :return: None
    """
    if num_logs is not None and num_logs < 0:
        raise ValueError(
            "num_logs must be a non-negative integer or None for indefinite logging."
        )

    count = 0
    methods = ["GET", "POST", "PUT", "DELETE"]
    paths = ["/home", "/about", "/contact", "/products", "/services"]
    statuses = [200, 404, 500, 301, 403]

    try:
        with open(log_file, "a") as f:
            while num_logs is None or count < num_logs:
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                method = random.choice(methods)
                path = random.choice(paths)
                status = random.choice(statuses)
                log_entry = f"{timestamp} - {method} {path} - Status: {status}\n"

                print(log_entry.strip())

                f.write(log_entry)
                f.flush()

                count += 1
                time.sleep(random.uniform(0.1, 1))
    except FileNotFoundError:
        print(f"Log file not found: {log_file}")
    except KeyboardInterrupt:
        print("Log production stopped by user.")
    finally:
        if count == 0:
            print("No logs were produced.")
        else:
            print(f"Produced {count} logs to {log_file}.")


if __name__ == "__main__":
    generate_logs(log_file="logs/nginx.log", num_logs=100)
