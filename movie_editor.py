import moviepy.editor

clip_1 = moviepy.editor.VideoFileClip("clip1.mp4")
clip_1 = clip_1.subclip(0, 3)
clip_2 = moviepy.editor.VideoFileClip("clip2.mp4")
clip_2 = clip_2.subclip(0, 3)
clip_3 = moviepy.editor.VideoFileClip("clip3.mp4")
clip_3 = clip_3.subclip(0, 3)

final_output = moviepy.editor.concatenate_videoclips([clip_1, clip_2, clip_3])

final_output.write_videofile("final.mp4", codec='libx264')