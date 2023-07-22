from pytube import YouTube


def progress_function(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining

    percentage_of_completion = bytes_downloaded / total_size * 100
    print(f"\rDownloading... {percentage_of_completion:.2f}% complete", end='')


def download_video(url, save_path="."):
    yt = YouTube(url, on_progress_callback=progress_function)
    video = yt.streams.get_highest_resolution()
    video.download(output_path=save_path)
    print("\nDownload completed!")


if __name__ == "__main__":
    url = input("Enter the YouTube video URL: ")
    download_video(url)
