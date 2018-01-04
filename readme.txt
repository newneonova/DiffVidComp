OK so the idea I want to try out is as follows.

Take a video. Extract all its frames into a set of images.

For each image, get the Diff amount with every other image by:

Image as binary:

ImA Diff ImB by ImA bit add ImB -> count the number of 1 bits in the result = difference score.

Create a solid compressed block where:

part 1: an array where the posiiton is frame in the block and the value is actual position of the frame in the video.
part 2: the first frame of the video (whatever frame we pick for this)
rest: the next back of code is the difference between frame 2 and frame 1, then diff between frame 3 and frame 2..etc

To reconstruct:
Frame 1, Frame 2 = Frame 1 + diff 2, frame 3 = frame 2 + diff 3, etc.  Then reorder frame by part 1 information.

To make the block:
Get pairwise difference scores.
Group by most similar.
Try to make a 1-D array of frames such that adjacant frames have minimal differences.

The theory I'm working on is that this will lead to long long stretches of 0s in the resulting saw binary string, which will deflate very effectively.

TEST 1: jellyfish-25-mbps-hd-hevc.mp4
32 MB
Used ffmpeg to extract it to bmp images in JellyOut  ~~ 5GB