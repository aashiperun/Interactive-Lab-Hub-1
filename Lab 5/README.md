# Observant Systems

**NAMES OF COLLABORATORS HERE**


For lab this week, we focus on creating interactive systems that can detect and respond to events or stimuli in the environment of the Pi, like the Boat Detector we mentioned in lecture. 
Your **observant device** could, for example, count items, find objects, recognize an event or continuously monitor a room.

This lab will help you think through the design of observant systems, particularly corner cases that the algorithms need to be aware of.

## Prep

1. Spend about 10 Minutes doing the Listening exercise as described in [ListeningExercise.md](https://github.com/FAR-Lab/Interactive-Lab-Hub/blob/Fall2022/Lab%205/ListeningExercise.md)
2.  Install VNC on your laptop if you have not yet done so. This lab will actually require you to run script on your Pi through VNC so that you can see the video stream. Please refer to the [prep for Lab 2](https://github.com/FAR-Lab/Interactive-Lab-Hub/blob/Fall2022/Lab%202/prep.md), we offered the instruction at the bottom.
3.  Read about [OpenCV](https://opencv.org/about/), [MediaPipe](https://mediapipe.dev/), and [TeachableMachines](https://teachablemachine.withgoogle.com/).
4.  Read Belloti, et al.'s [Making Sense of Sensing Systems: Five Questions for Designers and Researchers](https://www.cc.gatech.edu/~keith/pubs/chi2002-sensing.pdf).

### For the lab, you will need:
1. Pull the new Github Repo.(Please wait until thursday morning. There are still some incompatabilities to make the assignment work.)
1. Raspberry Pi
1. Webcam 

### Deliverables for this lab are:
1. Show pictures, videos of the "sense-making" algorithms you tried.
1. Show the filledout answers for the Contextual Interaction Design Tool.
1. Show a video of how you embed one of these algorithms into your observant system.
1. Test, characterize your interactive device. Show faults in the detection and how the system handled it.

## OverviewA
Building upon the paper-airplane metaphor (we're understanding the material of machine learning for design), here are the four sections of the lab activity:

A) [Play](#part-a)

B) [Fold](#part-b)

C) [Flight test](#part-c)

D) [Reflect](#part-d)

---

### Part A
### Play with different sense-making algorithms.

#### OpenCV
A more traditional method to extract information out of images is provided with OpenCV. The RPI image provided to you comes with an optimized installation that can be accessed through python. We included 4 standard OpenCV examples: contour(blob) detection, face detection with the ``Haarcascade``, flow detection (a type of keypoint tracking), and standard object detection with the [Yolo](https://pjreddie.com/darknet/yolo/) darknet.

Most examples can be run with a screen (e.g. VNC or ssh -X or with an HDMI monitor), or with just the terminal. The examples are separated out into different folders. Each folder contains a ```HowToUse.md``` file, which explains how to run the python example. 

The following command is a nicer way you can run and see the flow of the `openCV-examples` we have included in your Pi. Instead of `ls`, the command we will be using here is `tree`. [Tree](http://mama.indstate.edu/users/ice/tree/) is a recursive directory colored listing command that produces a depth indented listing of files. Install `tree` first and `cd` to the `openCV-examples` folder and run the command:

```shell
pi@ixe00:~ $ sudo apt install tree
...
pi@ixe00:~ $ cd openCV-examples
pi@ixe00:~/openCV-examples $ tree -l
.
├── contours-detection
│   ├── contours.py
│   └── HowToUse.md
├── data
│   ├── slow_traffic_small.mp4
│   └── test.jpg
├── face-detection
│   ├── face-detection.py
│   ├── faces_detected.jpg
│   ├── haarcascade_eye_tree_eyeglasses.xml
│   ├── haarcascade_eye.xml
│   ├── haarcascade_frontalface_alt.xml
│   ├── haarcascade_frontalface_default.xml
│   └── HowToUse.md
├── flow-detection
│   ├── flow.png
│   ├── HowToUse.md
│   └── optical_flow.py
└── object-detection
    ├── detected_out.jpg
    ├── detect.py
    ├── frozen_inference_graph.pb
    ├── HowToUse.md
    └── ssd_mobilenet_v2_coco_2018_03_29.pbtxt
```

The flow detection might seem random, but consider [this recent research](https://cseweb.ucsd.edu/~lriek/papers/taylor-icra-2021.pdf) that uses optical flow to determine busy-ness in hospital settings to facilitate robot navigation. Note the velocity parameter on page 3 and the mentions of optical flow.

Now, connect your webcam to your Pi and use **VNC to access to your Pi** and open the terminal. Use the following command lines to try each of the examples we provided:
(***it will not work if you use ssh from your laptop***)

```
pi@ixe00:~$ cd ~/openCV-examples/contours-detection
pi@ixe00:~/openCV-examples/contours-detection $ python contours.py
...
pi@ixe00:~$ cd ~/openCV-examples/face-detection
pi@ixe00:~/openCV-examples/face-detection $ python face-detection.py
...
pi@ixe00:~$ cd ~/openCV-examples/flow-detection
pi@ixe00:~/openCV-examples/flow-detection $ python optical_flow.py 0 window
...
pi@ixe00:~$ cd ~/openCV-examples/object-detection
pi@ixe00:~/openCV-examples/object-detection $ python detect.py
```

**\*\*\*Try each of the following four examples in the `openCV-examples`, include screenshots of your use and write about one design for each example that might work based on the individual benefits to each algorithm.\*\*\***

* Contour Detection

<img width="1014" alt="image" src="https://user-images.githubusercontent.com/66789469/196956474-0ea97693-20ec-47bd-a14a-2b50edb19e3f.png">

Design Idea: While trying contour detection, I observed that it detects shapes very clearly. I want to create a device which detects different shapes created by the user and associates these shapes with different moods. Based on the detetcted mood it would either play the user's favorite music if they are sad or call their long-distance loved one if they are missing them, etc.

* Face Detection

<img width="1012" alt="image" src="https://user-images.githubusercontent.com/66789469/196957095-f8384333-5686-4ced-9aba-71f1f228124f.png">

Design Idea: For a smart pill dispenser meant specifically for older adults with cognitive deficits, we need to be careful with who we dispense the medicine to. One of the checks can be to dispense the medicine only when one face is detected in front of the medicine dispenser. 

* Flow Detection

<img width="1015" alt="image" src="https://user-images.githubusercontent.com/66789469/196957656-be9a3b1c-fc42-425a-8771-849f7c99f376.png">

Design Idea: I want to create an Anxiety/ADHD detector. One of the most common signs of anxiety/ adhd is restlesness especially in their leg, commonly known as leg bouncing. To detect this, I will monitor a person's leg and detect the movement using the flow detection model and determine if the person is anxious or not. If the person is anxious, I will play calming sounds through the speaker.

* Object Detection

<img width="1016" alt="image" src="https://user-images.githubusercontent.com/66789469/196955758-25390b72-5112-4cad-9b8b-72ea241f9896.png">

Design Idea: Before entering an exam hall, I can use the object detector to check if students are carrying any objects that are not allowed into the exam hall.

#### Filtering, FFTs, and Time Series data. 
Additional filtering and analysis can be done on the sensors that were provided in the kit. For example, running a Fast Fourier Transform over the IMU or Microphone data stream could create a simple activity classifier between walking, running, and standing.

To get the microphone working we need to install two libraries. `PyAudio` to get the data from the microphone, `sciPy` to make data analysis easy, and the `numpy-ringbuffer` to keep track of the last ~1 second of audio. 
Pyaudio needs to be installed with the following comand:
``sudo apt install python3-pyaudio``
SciPy is installed with 
``sudo apt install python3-scipy`` 

Lastly we need numpy-ringbuffer, to make continues data anlysis easier.
``pip install numpy-ringbuffer``

Now try the audio processing example:
* Find what ID the micrpohone has with `python ListAvalibleAudioDevices.py`
    Look for a device name that includes `USB` in the name.
* Adjust the variable `DEVICE_INDEX` in the `ExampleAudioFFT.py` file.
    See if you are getting results printed out from the microphone. Try to understand how the code works.
    Then run the file by typing `python ExampleAudioFFT.py`



Using the microphone, try one of the following:

**1. Set up threshold detection** Can you identify when a signal goes above certain fixed values?

**2. Set up a running averaging** Can you set up a running average over one of the variables that are being calculated.[moving average](https://en.wikipedia.org/wiki/Moving_average)

**3. Set up peak detection** Can you identify when your signal reaches a peak and then goes down?

For technical references:

* Volume Calculation with [RootMeanSqare](https://en.wikipedia.org/wiki/Root_mean_square)
* [RingBuffer](https://en.wikipedia.org/wiki/Circular_buffer)
* [Frequency Analysis](https://en.wikipedia.org/wiki/Fast_Fourier_transform)


**\*\*\*Include links to your code here, and put the code for these in your repo--they will come in handy later.\*\*\***
* I created a device to detect if the person is speaking normally or too loudly
<img width="1019" alt="image" src="https://user-images.githubusercontent.com/66789469/199140231-bf97ec36-6a96-4a37-ba78-1f523d66f867.png">


### (Optional Reading) Introducing Additional Concepts
The following sections ([MediaPipe](#mediapipe) and [Teachable Machines](#teachable-machines)) are included for your own optional learning. **The associated scripts will not work on Fall 2022's Pi Image, so you can move onto part B.** However, you are welcome to try it on your personal computer. If this functionality is desirable for your lab or final project, we can help you get a different image running the last OS and version of python to make the following code work.

#### MediaPipe

A more recent open source and efficient method of extracting information from video streams comes out of Google's [MediaPipe](https://mediapipe.dev/), which offers state of the art face, face mesh, hand pose, and body pose detection.

![Alt Text](mp.gif)

To get started, create a new virtual environment with special indication this time:

```
pi@ixe00:~ $ virtualenv mpipe --system-site-packages
pi@ixe00:~ $ source mpipe/bin/activate
(mpipe) pi@ixe00:~ $ 
```

and install the following.

```
...
(mpipe) pi@ixe00:~ $ sudo apt install ffmpeg python3-opencv
(mpipe) pi@ixe00:~ $ sudo apt install libxcb-shm0 libcdio-paranoia-dev libsdl2-2.0-0 libxv1  libtheora0 libva-drm2 libva-x11-2 libvdpau1 libharfbuzz0b libbluray2 libatlas-base-dev libhdf5-103 libgtk-3-0 libdc1394-22 libopenexr25
(mpipe) pi@ixe00:~ $ pip3 install mediapipe-rpi3 pyalsaaudio
```

Each of the installs will take a while, please be patient. After successfully installing mediapipe, connect your webcam to your Pi and use **VNC to access to your Pi**, open the terminal, and go to Lab 5 folder and run the hand pose detection script we provide:
(***it will not work if you use ssh from your laptop***)


```
(mpipe) pi@ixe00:~ $ cd Interactive-Lab-Hub/Lab\ 5
(mpipe) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ python hand_pose.py
```

Try the two main features of this script: 1) pinching for percentage control, and 2) "[Quiet Coyote](https://www.youtube.com/watch?v=qsKlNVpY7zg)" for instant percentage setting. Notice how this example uses hardcoded positions and relates those positions with a desired set of events, in `hand_pose.py` lines 48-53. 

~~\*\*\*Consider how you might use this position based approach to create an interaction, and write how you might use it on either face, hand or body pose tracking.\*\*\*~~

(You might also consider how this notion of percentage control with hand tracking might be used in some of the physical UI you may have experimented with in the last lab, for instance in controlling a servo or rotary encoder.)



#### Teachable Machines
Google's [TeachableMachines](https://teachablemachine.withgoogle.com/train) might look very simple. However, its simplicity is very useful for experimenting with the capabilities of this technology.

![Alt Text](tm.gif)

To get started, create and activate a new virtual environment for this exercise with special indication:

```
pi@ixe00:~ $ virtualenv tmachine --system-site-packages
pi@ixe00:~ $ source tmachine/bin/activate
(tmachine) pi@ixe00:~ $ 
```

After activating the virtual environment, install the requisite TensorFlow libraries by running the following lines:
```
(tmachine) pi@ixe00:~ $ cd Interactive-Lab-Hub/Lab\ 5
(tmachine) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ sudo chmod +x ./teachable_machines.sh
(tmachine) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ ./teachable_machines.sh
``` 

This might take a while to get fully installed. After installation, connect your webcam to your Pi and use **VNC to access to your Pi**, open the terminal, and go to Lab 5 folder and run the example script:
(***it will not work if you use ssh from your laptop***)

```
(tmachine) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ python tm_ppe_detection.py
```


(**Optionally**: You can train your own model, too. First, visit [TeachableMachines](https://teachablemachine.withgoogle.com/train), select Image Project and Standard model. Second, use the webcam on your computer to train a model. For each class try to have over 50 samples, and consider adding a background class where you have nothing in view so the model is trained to know that this is the background. Then create classes based on what you want the model to classify. Lastly, preview and iterate, or export your model as a 'Tensorflow' model, and select 'Keras'. You will find an '.h5' file and a 'labels.txt' file. These are included in this labs 'teachable_machines' folder, to make the PPE model you used earlier. You can make your own folder or replace these to make your own classifier.)

~~**\*\*\*Whether you make your own model or not, include screenshots of your use of Teachable Machines, and write how you might use this to create your own classifier. Include what different affordances this method brings, compared to the OpenCV or MediaPipe options.\*\*\***~~


*Don't forget to run ```deactivate``` to end the Teachable Machines demo, and to reactivate with ```source tmachine/bin/activate``` when you want to use it again.*


### Part B
### Construct a simple interaction.

* Pick one of the models you have tried, and experiment with prototyping an interaction.
* This can be as simple as the boat detector showen in a previous lecture from Nikolas Matelaro.
* Try out different interaction outputs and inputs.
* Fill out the ``Contextual Interaction Design Tool`` sheet.[Found here.](ThinkingThroughContextandInteraction.png)

* Device: Anxiety Detector 
    * Model: Flow Detection
    * Description of the Device: I have created a device to determine if a person is being anxious based on the restlesness of their leg. I want to detect the if the user is bouncing their leg using the flow detection model. 
    * Contextual Interaction Design Tool for my Anxiety Detector.
    
    <img width="1132" alt="image" src="https://user-images.githubusercontent.com/66789469/199143489-5ed475fd-e29c-453c-a2bb-fbf72acab923.png">


**\*\*\*Describe and detail the interaction, as well as your experimentation here.\*\*\***

### Part C
### Test the interaction prototype

Now flight test your interactive prototype and **note down your observations**:
For example:
1. When does it do what it is supposed to do?
2. When does it fail?
3. When it fails, why does it fail?
4. Based on the behavior you have seen, what other scenarios could cause problems?

**\*\*\*Think about someone using the system. Describe how you think this will work.\*\*\***
1. Are they aware of the uncertainties in the system?
2. How bad would they be impacted by a miss classification?
3. How could change your interactive system to address this?
4. Are there optimizations you can try to do on your sense-making algorithm.

**\*\*\*ANXIETY DETECTOR TESTING\*\*\***
1. When does it do what it is supposed to do?
    * The anxiety detector device makes a noise to indicate to the user that they are being anxious when the user starts bouncing their leg.

2. When does it fail?
    * When there is movement in the background apart from the user's leg, the device creates a false alarm and fails.

3. When it fails why does it fail?
    * The camera detects a lot of points on the environment apart from the user's leg. 
    * So when something in the background moves it creates a false alarm to the user, telling them that they are anxious when they are actually not.

4. Based on the behavior you have seen, what other scenarios could cause problems?
    * When the user gets up from their chair to get something, it will detect the user's leg movement and think that the user is bouncing their leg, this scenario will also cause problems.
    
5. Are they aware of the uncertainties in the system?
    * The user may not be aware of the uncertainties in the system with regards to background movement as this is not in their control.
    
6. How bad would they be impacted by a miss classification?
    * Miss classification by our device would to create a false alert to the user telling them they have anxiety when they actually don't. This is a serious problem and will negatively impact a person who is already prone to being anxious. A false alert may lead them to becoming anxious, even if they previously weren't.
    
7. How could you change your interactive system to address this?
    * I could alter the model to detect only points on the user's knee and track only this point.
    * I could use a proximity sensor under the table to detect if the distance from the table to a person's leg is changing if they are bouncing their leg. This sensor data combined with the optical flow model could make more accurate predictions.
    
8. Are there optimizations you can try to do on your sense-making algorithm.
    * I could optimize the sense making algorithm to only detect points on the environment which are of interest to me and not detect all available points.
    
### Part D
### Characterize your own Observant system

Now that you have experimented with one or more of these sense-making systems **characterize their behavior**.
During the lecture, we mentioned questions to help characterize a material:
* What can you use X for?
* What is a good environment for X?
* What is a bad environment for X?
* When will X break?
* When it breaks how will X break?
* What are other properties/behaviors of X?
* How does X feel?

**\*\*\*Characterizing X: ANXIETY DETECTOR\*\*\***
*  What can you use the anxiety detector for? 
    * To detect when a person starts getting anxious
    * It can also be extended to other applications, such as detecting if a child has ADHD, etc.

* What is a good environment for the anxiety detector?
    * An good environment will be one with no background movement.

* What is a bad environment for the anxiety detector?
    * An environment with a lot of movement in the background.

**\*\*\*Include a short video demonstrating the answers to these questions.\*\*\***

https://drive.google.com/file/d/10ighPRZ-8H7DrQS4ytDmgPQ4kGHPdCcc/view?usp=sharing

### Part 2.

Following exploration and reflection from Part 1, finish building your interactive system, and demonstrate it in use with a video.

* Based on feedback and problems observed in part 1, this is the final design of my interactive system:
    * I have added a proximity sensor under the study table to detect the distance between my leg and the table.
    * This sensor distance is constantly monitored.
    * If the distance changes it means the leg if bouncing.
    * However if the flow detection model detects movement but the proximity sensor doesn't observe a change in the distance, then there is no alert provided by the device.
    * Only if the proximity sensor's distance changes AND the flow detection model detects movement, then an alert to the user is provided through the speaker which says: "You are starting to feel anxious, take a break"
    * This way my model reduces the number of false alerts provided by my anxiety detector to the user.

**\*\*\*Include a short video demonstrating the finished result.\*\*\***

* The following video shows two cases:
  * CASE 1. The user's leg is stationary, but there is movement in the background.
  * CASE 2. The user's leg is bouncing.

* Video

https://drive.google.com/file/d/1kfOF9tYcglvtBUOEVA4exBshBsdL3jJh/view?usp=sharing

