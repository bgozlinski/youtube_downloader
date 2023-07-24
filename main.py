from pytube import YouTube


def progress_function(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100

    bar_length = 50
    filled_bar = int(percentage_of_completion * bar_length / 100)
    bar = '=' * filled_bar + ' ' * (bar_length - filled_bar)

    print(f"\r[{bar}] Downloading... {percentage_of_completion:.2f}% complete", end='')


def download_video(url, save_path="."):
    yt = YouTube(url, on_progress_callback=progress_function)
    video = yt.streams.get_highest_resolution()
    video.download(output_path=save_path)
    print("\nDownload completed!")


if __name__ == "__main__":
    url = input("Enter the YouTube video URL: ")
    download_video(url)
