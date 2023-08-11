from pytube import YouTube
import time

previous_bytes = 0
time_marker = time.time()


def progress_function(stream, chunk, bytes_remaining):
    global previous_bytes, time_marker

    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining

    # Calculate download speed
    elapsed_time = time.time() - time_marker
    bytes_per_second = (bytes_downloaded - previous_bytes) / elapsed_time
    speed = f"{bytes_per_second / (1024 ** 2):.2f} MB/s"  # Convert to MB/s for display

    percentage_of_completion = bytes_downloaded / total_size * 100

    bar_length = 50
    filled_bar = int(percentage_of_completion * bar_length / 100)
    bar = '=' * filled_bar + ' ' * (bar_length - filled_bar)

    print(f"\r[{bar}] Downloading... {percentage_of_completion:.2f}% complete at {speed}", end='')

    # Reset for next interval
    previous_bytes = bytes_downloaded
    time_marker = time.time()


def download_video(url, save_path="."):
    yt = YouTube(url, on_progress_callback=progress_function)
    video = yt.streams.get_highest_resolution()
    video.download(output_path=save_path)
    print("\nDownload completed!")


if __name__ == "__main__":
    url = input("Enter the YouTube video URL: ")
    download_video(url)
