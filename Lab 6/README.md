# Little Interactions Everywhere

**Collaborated with Anjali Vyas**

## Prep

1. Pull the new changes from the class interactive-lab-hub. (You should be familiar with this already!)
2. Install [MQTT Explorer](http://mqtt-explorer.com/) on your laptop. If you are using Mac, MQTT Explorer only works when installed from the [App Store](https://apps.apple.com/app/apple-store/id1455214828).
3. Readings before class:
   * [MQTT](#MQTT)
   * [The Presence Table](https://dl.acm.org/doi/10.1145/1935701.1935800) and [video](https://vimeo.com/15932020)


## Overview

The point of this lab is to introduce you to distributed interaction. We have included some Natural Language Processing (NLP) and Generation (NLG) but those are not really the emphasis. Feel free to dig into the examples and play around the code which you can integrate into your projects if wanted. However, we want to emphasize that the grading will focus on your ability to develop interesting uses for messaging across distributed devices. Here are the four sections of the lab activity:

A) [MQTT](#part-a)

B) [Send and Receive on your Pi](#part-b)

C) [Streaming a Sensor](#part-c)

D) [The One True ColorNet](#part-d)

E) [Make It Your Own](#part-)

## Part 1.

### Part A
### MQTT

MQTT is a lightweight messaging portal invented in 1999 for low bandwidth networks. It was later adopted as a defacto standard for a variety of [Internet of Things (IoT)](https://en.wikipedia.org/wiki/Internet_of_things) devices. 

#### The Bits

* **Broker** - The central server node that receives all messages and sends them out to the interested clients. Our broker is hosted on the far lab server (Thanks David!) at `farlab.infosci.cornell.edu/8883`. Imagine that the Broker is the messaging center!
* **Client** - A device that subscribes or publishes information to/on the network.
* **Topic** - The location data gets published to. These are *hierarchical with subtopics*. For example, If you were making a network of IoT smart bulbs this might look like `home/livingroom/sidelamp/light_status` and `home/livingroom/sidelamp/voltage`. With this setup, the info/updates of the sidelamp's `light_status` and `voltage` will be store in the subtopics. Because we use this broker for a variety of projects you have access to read, write and create subtopics of `IDD`. This means `IDD/ilan/is/a/goof` is a valid topic you can send data messages to.
*  **Subscribe** - This is a way of telling the client to pay attention to messages the broker sends out on the topic. You can subscribe to a specific topic or subtopics. You can also unsubscribe. Following the previouse example of home IoT smart bulbs, subscribing to `home/livingroom/sidelamp/#` would give you message updates to both the light_status and the voltage.
* **Publish** - This is a way of sending messages to a topic. Again, with the previouse example, you can set up your IoT smart bulbs to publish info/updates to the topic or subtopic. Also, note that you can publish to topics you do not subscribe to. 


**Important note:** With the broker we set up for the class, you are limited to subtopics of `IDD`. That is, to publish or subcribe, the topics will start with `IDD/`. Also, setting up a broker is not much work, but for the purposes of this class, you should all use the broker we have set up for you!


#### Useful Tooling

Debugging and visualizing what's happening on your MQTT broker can be helpful. We like [MQTT Explorer](http://mqtt-explorer.com/). You can connect by putting in the settings from the image below.


![input settings](imgs/mqtt_explorer.png?raw=true)


Once connected, you should be able to see all the messages under the IDD topic. , go to the **Publish** tab and try publish something! From the interface you can send and plot messages as well. Remember, you are limited to subtopics of `IDD`. That is, to publish or subcribe, the topics will start with `IDD/`.


<img width="1026" alt="Screen Shot 2022-10-30 at 10 40 32 AM" src="https://user-images.githubusercontent.com/24699361/198885090-356f4af0-4706-4fb1-870f-41c15e030aba.png">



### Part B
### Send and Receive on your Pi

[sender.py](./sender.py) and and [reader.py](./reader.py) show you the basics of using the mqtt in python. Let's spend a few minutes running these and seeing how messages are transferred and shown up. Before working on your Pi, keep the connection of `farlab.infosci.cornell.edu/8883` with MQTT Explorer running on your laptop.

**Running Examples on Pi**

* Install the packages from `requirements.txt` under a virtual environment, we will continue to use the `circuitpython` environment we setup earlier this semester:

  ```
  pi@raspberrypi:~/Interactive-Lab-Hub $ source circuitpython/bin/activate
  (circuitpython) pi@raspberrypi:~/Interactive-Lab-Hub $ cd Lab\ 6
  (circuitpython) pi@raspberrypi:~/Interactive-Lab-Hub/Lab 6 $ pip install -r requirements.txt
  ...
  ```
* Run `sender.py`, fill in a topic name (should start with `IDD/`), then start sending messages. You should be able to see them on MQTT Explorer.

  ```
  (circuitpython) pi@raspberrypi:~/Interactive-Lab-Hub/Lab 6 $ python sender.py
  >> topic: IDD/AlexandraTesting
  now writing to topic IDD/AlexandraTesting
  type new-topic to swich topics
  >> message: testtesttest
  ...

  ```
  
    <img width="1025" alt="image" src="https://user-images.githubusercontent.com/66789469/199729543-082e3192-6c50-4fc4-90ae-2d4bd0bfaa59.png">
    
    
* Run `reader.py`, and you should see any messages being published to `IDD/` subtopics. Type a message inside MQTT explorer and see if you can receive it with `reader.py`.

  ```
  (circuitpython) pi@raspberrypi:~ Interactive-Lab-Hub/Lab 6 $ python reader.py
  ...
  ```
  
<img width="253" alt="image" src="https://user-images.githubusercontent.com/66789469/200447948-a0459bb1-1432-4a06-92bd-5e71bce3d1b6.png">

**\*\*\*Consider how you might use this messaging system on interactive devices, and draw/write down 5 ideas here.\*\*\***

* Idea #1: Search and Rescue Robot Communication : When we are dealing with a swarm (or group) of robots in a search and rescue operation, each of these robots can use this messaging system to update the location of people they find in real time.
* Idea #2: Online Digital Painting Class: We can use the color sensor along with the pi to relay information through this messaging system about the color the teacher is using to all the students in a digital painting class.
* Idea #3: Enhance communication between people with disabilities:  By interfacing the pi with the gesture sensor we can enable easy communication through this messaging system between people with disabilities.
* Idea #4: Safety of Older Adults: To track when older adults are leaving their house, we can use a proximity sensor to detect when they are close to the door and relay this information to their family members in a remote location using this messaging system to ensure the safety of older adults with cognitive deficits.
* Idea #5: Musical Instrument: Use different pads on the Capacitive touch sensor to denote a certain pitch and sound. Transmit the information of the sound being produced (eg, pitch, etc) and play this sound on a speaker.

### Part C
### Streaming a Sensor

We have included an updated example from [lab 4](https://github.com/FAR-Lab/Interactive-Lab-Hub/tree/Fall2021/Lab%204) that streams the [capacitor sensor](https://learn.adafruit.com/adafruit-mpr121-gator) inputs over MQTT. We will also be running this example under `circuitpython` virtual environment.

Plug in the capacitive sensor board with the Qwiic connector. Use the alligator clips to connect a Twizzler (or any other things you used back in Lab 4) and run the example script:

<p float="left">
<img src="https://cdn-learn.adafruit.com/assets/assets/000/082/842/large1024/adafruit_products_4393_iso_ORIG_2019_10.jpg" height="150" />
<img src="https://cdn-shop.adafruit.com/970x728/4210-02.jpg" height="150">
<img src="https://cdn-learn.adafruit.com/guides/cropped_images/000/003/226/medium640/MPR121_top_angle.jpg?1609282424" height="150"/>
<img src="https://media.discordapp.net/attachments/679721816318803975/823299613812719666/PXL_20210321_205742253.jpg" height="150">
</p>

 ```
 (circuitpython) pi@raspberrypi:~ Interactive-Lab-Hub/Lab 6 $ python distributed_twizzlers_sender.py
 ...
 ```

**\*\*\*Include a picture of your setup here: what did you see on MQTT Explorer?\*\*\***

* I connected the capacitive touch sensor to my raspberry pi and touched twizzlers 6 and 10 on the sensor
* Setup:

<img width="1019" alt="image" src="https://user-images.githubusercontent.com/66789469/200454219-426b5434-9ea1-49b5-ad95-4d1fe8c194e9.png">

* MQTT Explorer: 

<img width="207" alt="image" src="https://user-images.githubusercontent.com/66789469/200449128-cf1e188f-5923-44fe-ad1f-675ec236d8c8.png">

<img width="222" alt="image" src="https://user-images.githubusercontent.com/66789469/200449161-0a730dc1-b0b0-45b1-9a32-185c59caf06a.png">

### Part D
### The One True ColorNet

It is with great fortitude and resilience that we shall worship at the altar of the *OneColor*. Through unity of the collective RGB, we too can find unity in our heart, minds and souls. With the help of machines, we can overthrow the bourgeoisie, get on the same wavelength (this was also a color pun) and establish [Fully Automated Luxury Communism](https://en.wikipedia.org/wiki/Fully_Automated_Luxury_Communism).

The first step on the path to *collective* enlightenment, plug the [APDS-9960 Proximity, Light, RGB, and Gesture Sensor](https://www.adafruit.com/product/3595) into the [MiniPiTFT Display](https://www.adafruit.com/product/4393). You are almost there!

<p float="left">
  <img src="https://cdn-learn.adafruit.com/assets/assets/000/082/842/large1024/adafruit_products_4393_iso_ORIG_2019_10.jpg" height="150" />
  <img src="https://cdn-shop.adafruit.com/970x728/4210-02.jpg" height="150">
  <img src="https://cdn-shop.adafruit.com/970x728/3595-03.jpg" height="150">
</p>


The second step to achieving our great enlightenment is to run `color.py`. We have talked about this sensor back in Lab 2 and Lab 4, this script is similar to what you have done before! Remember to activate the `circuitpython` virtual environment you have been using during this semester before running the script:

 ```
 (circuitpython) pi@raspberrypi:~ Interactive-Lab-Hub/Lab 6 $ python color.py
 ...
 ```

By running the script, wou will find the two squares on the display. Half is showing an approximation of the output from the color sensor. The other half is up to the collective. Press the top button to share your color with the class. Your color is now our color, our color is now your color. We are one.

(A message from the previous TA, Ilan: I was not super careful with handling the loop so you may need to press more than once if the timing isn't quite right. Also, I haven't load-tested it so things might just immediately break when everyone pushes the button at once.)

You may ask "but what if I missed class?" Am I not admitted into the collective enlightenment of the *OneColor*?

Of course not! You can go to [https://one-true-colornet.glitch.me/](https://one-true-colornet.glitch.me/) and become one with the ColorNet on the inter-webs. Glitch is a great tool for prototyping sites, interfaces and web-apps that's worth taking some time to get familiar with if you have a chance. Its not super pertinent for the class but good to know either way. 

**\*\*\*Can you set up the script that can read the color anyone else publish and display it on your screen?\*\*\***

<img width="586" alt="image" src="https://user-images.githubusercontent.com/66789469/200448938-52dd7a13-cc24-4add-b3a7-ec6a0c4786e1.png">

<img width="592" alt="image" src="https://user-images.githubusercontent.com/66789469/200449063-3d2232da-0c0e-4f4d-83ca-073607cb3cde.png">


### Part E
### Make it your own

Find at least one class (more are okay) partner, and design a distributed application together based on the exercise we asked you to do in this lab.

**\*\*\*1. Explain your design\*\*\*** For example, if you made a remote controlled banana piano, explain why anyone would want such a thing.

* We designed a replica of a Morse Code Translator using the capacitive touch sensor. 
* Morse code was one of the early communication methods which was used to send messages over long distances. 
* Morse Code has also been used as an alternative form of communication for people with disabilities or whom have their abilities to communicate imparied by stroke, heart attack, or paralysis. There have been several cases where individuals have been able to use their eyelids to communicate in Morse Code by using a series of long and quick blinks to represent that dots and dashes.
* Our design makes use of 5 pads on the capacitive touch sensor to transmit a message in Morse code from the sender's topic (IDD/Aashika).
* The Receiver(Anjali) subscribes to the sender's topic (IDD/Aashika) and waits till the entire message is received.
* Once the message is received, the receiver decrypts the message and plays it using the speaker.
* In our design we use two of the pads (pad #7 and #10) to create letters using dots and hyphens. The third pad (pad #5) is used as an asterisk to differentiate between letters. The fourth pad (pad #2) is used as a forward slash to differentiate between words. The fifth pad (pad #0) is used as an exclamation mark to indicate "End of Message". 
* In the modern day context, this morse code translator can be used by people with motor control disabilities.

<img width="609" alt="image" src="https://user-images.githubusercontent.com/66789469/200665032-8c07c4ae-0297-4811-94fa-7534d8842cd9.png">

**\*\*\*2. Diagram the architecture of the system.\*\*\*** Be clear to document where input, output and computation occur, and label all parts and connections. For example, where is the banana, who is the banana player, where does the sound get played, and who is listening to the banana music?

<img width="1146" alt="Screenshot 2022-11-07 at 5 00 33 PM" src="https://user-images.githubusercontent.com/66789469/200440752-20c8e00a-871d-467d-9338-4b02c3270d49.png">

**\*\*\*3. Build a working prototype of the system.\*\*\*** Do think about the user interface: if someone encountered these bananas somewhere in the wild, would they know how to interact with them? Should they know what to expect?

<img width="260" alt="image" src="https://user-images.githubusercontent.com/66789469/200445669-727b0352-8525-46df-8bb7-df5a14611c49.png">

* The user interface of the device is built on the capacitive touch sensor with conducting tape attached to each pad. 
* The end of each conducting tape has the corresponding symbol used for the morse code.
* The center of the capactive touch sensor has "morse code" written on it to indicate that this device can be used to send a message using morse code.
* The receiver looks at the subscribed topic(IDD/Aashika) on the MQTT Interface to see the message in Morse code being transmitted

* Code for morse code sender: https://github.com/aashiperun/Interactive-Lab-Hub-1/blob/Fall2022/Lab%206/sender.py
* Code for morse code receiver: https://github.com/aashiperun/Interactive-Lab-Hub-1/blob/Fall2022/Lab%206/morse_code_recvr.py

**\*\*\*4. Document the working prototype in use.\*\*\*** It may be helpful to record a Zoom session where you should the input in one location clearly causing response in another location.

https://drive.google.com/file/d/1ESvAuAMCE_ug-s1ZctOr9cSprVH_xaHu/view?usp=sharing

<!--**\*\*\*5. BONUS (Wendy didn't approve this so you should probably ignore it)\*\*\*** get the whole class to run your code and make your distributed system BIGGER.-->

