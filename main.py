from moviepy.editor import VideoFileClip

def cut_video(input_file, output_prefix, num_parts):
    video = VideoFileClip(input_file)
    duration = video.duration
    part_duration = 60  # Set the desired duration of each cut video part to 60 seconds

    for i in range(num_parts):
        start_time = i * part_duration
        end_time = start_time + part_duration

        part = video.subclip(start_time, end_time)
        output_file = f"{output_prefix}_{i+1}.mp4"
        part.write_videofile(output_file)

    video.close()

# Example usage
input_file = "C:\\Users\\lenov\Desktop\\Python\\Video Chopper\\input.mp4"
output_prefix = "output"
num_parts = 10

cut_video(input_file, output_prefix, num_parts)
