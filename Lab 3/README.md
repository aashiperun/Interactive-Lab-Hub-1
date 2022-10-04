# Chatterboxes
**NAMES OF COLLABORATORS HERE**
[![Watch the video](https://user-images.githubusercontent.com/1128669/135009222-111fe522-e6ba-46ad-b6dc-d1633d21129c.png)](https://www.youtube.com/embed/Q8FWzLMobx0?start=19)

In this lab, we want you to design interaction with a speech-enabled device--something that listens and talks to you. This device can do anything *but* control lights (since we already did that in Lab 1).  First, we want you first to storyboard what you imagine the conversational interaction to be like. Then, you will use wizarding techniques to elicit examples of what people might say, ask, or respond.  We then want you to use the examples collected from at least two other people to inform the redesign of the device.

We will focus on **audio** as the main modality for interaction to start; these general techniques can be extended to **video**, **haptics** or other interactive mechanisms in the second part of the Lab.

## Prep for Part 1: Get the Latest Content and Pick up Additional Parts 

### Pick up Web Camera If You Don't Have One

Students who have not already received a web camera will receive their [IMISES web cameras](https://www.amazon.com/Microphone-Speaker-Balance-Conference-Streaming/dp/B0B7B7SYSY/ref=sr_1_3?keywords=webcam%2Bwith%2Bmicrophone%2Band%2Bspeaker&qid=1663090960&s=electronics&sprefix=webcam%2Bwith%2Bmicrophone%2Band%2Bsp%2Celectronics%2C123&sr=1-3&th=1) on Thursday at the beginning of lab. If you cannot make it to class on Thursday, please contact the TAs to ensure you get your web camera. 

### Get the Latest Content

As always, pull updates from the class Interactive-Lab-Hub to both your Pi and your own GitHub repo. There are 2 ways you can do so:

**\[recommended\]**Option 1: On the Pi, `cd` to your `Interactive-Lab-Hub`, pull the updates from upstream (class lab-hub) and push the updates back to your own GitHub repo. You will need the *personal access token* for this.

```
pi@ixe00:~$ cd Interactive-Lab-Hub
pi@ixe00:~/Interactive-Lab-Hub $ git pull upstream Fall2022
pi@ixe00:~/Interactive-Lab-Hub $ git add .
pi@ixe00:~/Interactive-Lab-Hub $ git commit -m "get lab3 updates"
pi@ixe00:~/Interactive-Lab-Hub $ git push
```

Option 2: On your your own GitHub repo, [create pull request](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2022Fall/readings/Submitting%20Labs.md) to get updates from the class Interactive-Lab-Hub. After you have latest updates online, go on your Pi, `cd` to your `Interactive-Lab-Hub` and use `git pull` to get updates from your own GitHub repo.

## Part 1.

### Text to Speech 

In this part of lab, we are going to start peeking into the world of audio on your Pi! 

We will be using the microphone and speaker on your webcamera. In the home directory of your Pi, there is a folder called `text2speech` containing several shell scripts. `cd` to the folder and list out all the files by `ls`:

```
pi@ixe00:~/text2speech $ ls
Download        festival_demo.sh  GoogleTTS_demo.sh  pico2text_demo.sh
espeak_demo.sh  flite_demo.sh     lookdave.wav
```

You can run these shell files by typing `./filename`, for example, typing `./espeak_demo.sh` and see what happens. Take some time to look at each script and see how it works. You can see a script by typing `cat filename`. For instance:

```
pi@ixe00:~/text2speech $ cat festival_demo.sh 
#from: https://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)#Festival_Text_to_Speech

echo "Just what do you think you're doing, Dave?" | festival --tts
```

Now, you might wonder what exactly is a `.sh` file? Typically, a `.sh` file is a shell script which you can execute in a terminal. The example files we offer here are for you to figure out the ways to play with audio on your Pi!

You can also play audio files directly with `aplay filename`. Try typing `aplay lookdave.wav`.

\*\***Write your own shell file to use your favorite of these TTS engines to have your Pi greet you by name.**\*\*
(This shell file should be saved to your own repo for this lab.)

https://drive.google.com/file/d/1trO9hNQ5i1o3hVTSqQbt29kTPout0ETd/view?usp=sharing

Bonus: If this topic is very exciting to you, you can try out this new TTS system we recently learned about: https://github.com/rhasspy/larynx

### Speech to Text

Now examine the `speech2text` folder. We are using a speech recognition engine, [Vosk](https://alphacephei.com/vosk/), which is made by researchers at Carnegie Mellon University. Vosk is amazing because it is an offline speech recognition engine; that is, all the processing for the speech recognition is happening onboard the Raspberry Pi. 

In particular, look at `test_words.py` and make sure you understand how the vocab is defined. 
Now, we need to find out where your webcam's audio device is connected to the Pi. Use `arecord -l` to get the card and device number:
```
pi@ixe00:~/speech2text $ arecord -l
**** List of CAPTURE Hardware Devices ****
card 1: Device [Usb Audio Device], device 0: USB Audio [USB Audio]
  Subdevices: 1/1
  Subdevice #0: subdevice #0
```
The example above shows a scenario where the audio device is at card 1, device 0. Now, use `nano vosk_demo_mic.sh` and change the `hw` parameter. In the case as shown above, change it to `hw:1,0`, which stands for card 1, device 0.  

Now, look at which camera you have. Do you have the cylinder camera (likely the case if you received it when we first handed out kits), change the `-r 16000` parameter to `-r 44100`. If you have the IMISES camera, check if your rate parameter says `-r 16000`. Save the file using Write Out and press enter.

Then try `./vosk_demo_mic.sh`

\*\***Write your own shell file that verbally asks for a numerical based input (such as a phone number, zipcode, number of pets, etc) and records the answer the respondent provides.**\*\*

My Shell file asks "How many siblings do you have?"

https://drive.google.com/file/d/1eQ7G0ayjXiPKJi3FttSlLUDQSo6ms0yV/view?usp=sharing

### Serving Pages

In Lab 1, we served a webpage with flask. In this lab, you may find it useful to serve a webpage for the controller on a remote device. Here is a simple example of a webserver.

```
pi@ixe00:~/Interactive-Lab-Hub/Lab 3 $ python server.py
 * Serving Flask app "server" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 162-573-883
```
From a remote browser on the same network, check to make sure your webserver is working by going to `http://<YourPiIPAddress>:5000`. You should be able to see "Hello World" on the webpage.

### Storyboard

\*\***Post your storyboard and diagram here.**\*\*
* Product: Wayfinding Walking Stick
* Purpose of Product: Older Adults with cognitive deficits like dementia often feel disoriented when they go out for a walk on their own. Using this device they dont need to use an additional device like a phone for navigation while holding their walking stick. This device would provide voice based guidance and is more interactive than a normal phone.

![Storyboarding (4)](https://user-images.githubusercontent.com/66789469/192393592-111ec376-79e4-407c-a62d-c5f762599ec2.jpg)


Write out what you imagine the dialogue to be. Use cards, post-its, or whatever method helps you develop alternatives or group responses. 

\*\***Please describe and document your process.**\*\*

![Storyboarding (5)](https://user-images.githubusercontent.com/66789469/192394718-607d9c29-bf31-4395-b37b-2eba32746010.jpg)

### Acting out the dialogue

Find a partner, and *without sharing the script with your partner* try out the dialogue you've designed, where you (as the device designer) act as the device you are designing.  Please record this interaction (for example, using Zoom's record feature).

\*\***Describe if the dialogue seemed different than what you imagined when it was acted out, and how.**\*\*

https://drive.google.com/file/d/1f4D7GZN7cd7ydhbeJDTHognUjlJj7FSQ/view?usp=sharing

* When acted out, I felt that the walking stick should provide more prompts to the user.

### Wizarding with the Pi (optional)
In the [demo directory](./demo), you will find an example Wizard of Oz project. In that project, you can see how audio and sensor data is streamed from the Pi to a wizard controller that runs in the browser.  You may use this demo code as a template. By running the `app.py` script, you can see how audio and sensor data (Adafruit MPU-6050 6-DoF Accel and Gyro Sensor) is streamed from the Pi to a wizard controller that runs in the browser `http://<YouPiIPAddress>:5000`. You can control what the system says from the controller as well!

\*\***Describe if the dialogue seemed different than what you imagined, or when acted out, when it was wizarded, and how.**\*\*

# Lab 3 Part 2

For Part 2, you will redesign the interaction with the speech-enabled device using the data collected, as well as feedback from part 1.

## Prep for Part 2

* Feedback from Part 1:
  * Anjali Vyas:
      * I really love this idea because it's like a smart assistant but geared towards a social good activity that I've never seen smart assistants being         used for before! Great job!
      * Some things I was wondering:
      * How would the device respond if an older adult says something incoherent (due to memory lapses) or something that the device is not programmed to         know the answer to. For example: why am I here, where's my daughter? - maybe the device can store emergency contact information of loved ones and         alert them in such cases.
      * I'm curious to know where exactly the speaker / microphone / device would be placed on the walking stick. In case the older adult doesn't use a           walking stick but could still benefit from the device how would you design it to make it available to them?
      
  * Neha Manjunath (TA)
      * Really cool idea! However, we would love to see your exploration of the idea and the different barriers that might arise wrt to human                     communication and list out workflows where the dialogue would fall apart and how you could accommodate those scenarios.
      
1. What are concrete things that could use improvement in the design of your device? For example: wording, timing, anticipation of misunderstandings...
   * From the feedback received, I understand that older people with cognitive deficits tend to have incoherent speech due to memory lapses. This is            factor I hadn't previously accounted for in my design.
   * My device could be improved to anticipate sentences older adults might say and reinforce/remind older adults why they are going to a specific place.
   * Where would the microphone be placed on the walking stick? 
   
2. What are other modes of interaction _beyond speech_ that you might also use to clarify how to interact?
   * Use a Pulse heart rate sensor to detect when the older adult is starting to feel anxious. Provide calming music/ voice recordings from family to calm      the older adult and reassure them that they are not lost.
   * Use a proximity sensor the detect obstacles or pavements to prevent older adults from falling.
   * Use Buttons to facilitate emergency calls.

3. Make a new storyboard, diagram and/or script based on these reflections.
   * Prototype of the walking stick based on the above reflections:
     ![image](https://user-images.githubusercontent.com/66789469/193737302-a2788396-2fe1-475c-b054-0d99d6acc2fa.png)
   * Dialogue: 
      ![Storyboarding (9)](https://user-images.githubusercontent.com/66789469/193877602-e8a121c3-1cf2-45f9-87cd-3a37eb4cdd83.jpg)


## Prototype your system

The system should:
* use the Raspberry Pi 
* use one or more sensors
* require participants to speak to it. 

*Document how the system works*

*Include videos or screencaptures of both the system and the controller.*

![Storyboarding (7)](https://user-images.githubusercontent.com/66789469/193825943-2b595672-5ea2-4ada-873e-ea8df85673a3.jpg)


## Test the system
Try to get at least two people to interact with your system. (Ideally, you would inform them that there is a wizard _after_ the interaction, but we recognize that can be hard.)

Answer the following:

### What worked well about the system and what didn't?
  * Worked Well: The system detected the obstacles using proximity sensor and promptly provided voice alerts using the pre-programmed speech2text.
  * Didn't Work Well: Inaccurate predictions by the model

### What worked well about the controller and what didn't?
  * Worked Well: The controller detected button presses and reacted quickly.
  * Didn't work well: It was difficult to place the controller on the makeshift walking stick with all the sensors connected because I had small wires that didn't reach to the end of the walking stick. 

### What lessons can you take away from the WoZ interactions for designing a more autonomous version of the system?
  * Key Takeaways from a WoZ interaction for designing a more autonomous version of the system:
      * The WoZ helped me realise that older people with cognitive deficits have frequent discontinuities in speech something I didn't realise while designing the system.
      * I would create more alternative responses / predict responses to discontinuous speech while designing a more autonomous version of the system.

### How could you use your system to create a dataset of interaction? What other sensing modalities would make sense to capture?
  * Capture data from Motion sensors/ GPS trackers to see if the older adult stops moving/following navigation.
  * Analyzing the sensor dataset could indicate either that the older adult has lost the walking stick/ the older adult doesn't know where to go next.
  * Using this information, we can ensure safety of older adults and detect an emergency situation faster.

