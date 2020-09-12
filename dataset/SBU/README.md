# SBU-Kinect-Interaction dataset v2.0


We choose eight types of two-person interactions, including: 

- approaching
- departing
- pushing
- kicking
- punching
- exchanging objects
- hugging
- shaking hands

The frame rate is 15 frames per second (FPS). 

Note that in most interactions, one person is acting and the other person is reacting.

Skeleton data consists of 15 joints per person. Each row follows the following format:

	Frame#, PA(1), PA(2), ..., PA(15), PB(1), PB(2),...,PB(15)

PA(i)   => position of ith joint (x,y,z) for the subject A located at left  
PB(i)   => position of ith joint (x,y,z) for the subject B located at right  
x and y are normalized as [0,1] while z is normalized as [0,7.8125]

Joint number|Joint name
-|-
1 | HEAD
2 | NECK
3 | TORSO
4 | LEFT_SHOULDER
5 | LEFT_ELBOW
6 | LEFT_HAND
7 | RIGHT_SHOULDER
8 | RIGHT_ELBOW
9 | RIGHT_HAND
10 | LEFT_HIP
11 | LEFT_KNEE
12 | LEFT_FOOT
13 | RIGHT_HIP
14 | RIGHT_KNEE
15 | RIGHT_FOOT

The skeleton data was normalized. In order to extract the original position of the joints, the following equations are needed:
	
	original_X = 1280 - (normalized_X .* 2560);
	original_Y = 960 - (normalized_Y .* 1920);
	original_Z = normalized_Z .* 10000 ./ 7.8125;
				