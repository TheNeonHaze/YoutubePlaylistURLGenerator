import re


def extract_video_id(url):
    match = re.search(r'(?:youtube\.com/watch\?v=|youtu.be/)([a-zA-Z0-9_-]+)', url)
    if match:
        return match.group(1)
    return None


def generate_playlist_url(video_ids):
    return f"https://www.youtube.com/watch_videos?video_ids={','.join(video_ids)}"


def main():
    input_file = 'input.txt'
    output_file = 'output.txt'
    video_ids = []

    with open(input_file, 'r') as f:
        lines = f.readlines()

    for line in lines:
        video_id = extract_video_id(line.strip())
        if video_id:
            video_ids.append(video_id)
        else:
            print("Invalid YouTube URL format... skipping")

    if video_ids:
        playlist_url = generate_playlist_url(video_ids)
        with open(output_file, 'w') as f:
            f.write(playlist_url)
            print(f"Playlist URL saved to {output_file}: {playlist_url}")
    else:
        print("No valid video IDs found in the input file.")


if __name__ == "__main__":
    main()
