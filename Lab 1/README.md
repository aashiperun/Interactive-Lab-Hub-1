

# Staging Interaction

In the original stage production of Peter Pan, Tinker Bell was represented by a darting light created by a small handheld mirror off-stage, reflecting a little circle of light from a powerful lamp. Tinkerbell communicates her presence through this light to the other characters. See more info [here](https://en.wikipedia.org/wiki/Tinker_Bell). 

There is no actor that plays Tinkerbell--her existence in the play comes from the interactions that the other characters have with her.

For lab this week, we draw on this and other inspirations from theatre to stage interactions with a device where the main mode of display/output for the interactive device you are designing is lighting. You will plot the interaction with a storyboard, and use your computer and a smartphone to experiment with what the interactions will look and feel like. 

## Part A. Plan 

\*\***Describe your setting, players, activity and goals here.**\*\*

The Interactive Device I am building is a Smart Toothbrush.

<img width="614" alt="image" src="https://user-images.githubusercontent.com/66789469/187313719-806dd0e2-6997-4658-bb7e-613fe86dd6f8.png">

\*\***Include a picture of your storyboard here**\*\*

![Untitled (3)](https://user-images.githubusercontent.com/66789469/187329394-eb5cf28b-f71e-4a68-93ea-68f77732358b.jpg)

\*\***Summarize feedback you got here.**\*\*

1) The user might find it frustrating while waiting for the light color to change. 
2) Can the light provide any other information other than just acting as a timer?

## Part B. Act out the Interaction

\*\***Are there things that seemed better on paper than acted out?**\*\*

* Looking at the same color for one minute felt like a dull process, since the light was telling me nothing other than the time duration I was brushing for.
* The anticipation of the light changing made me feel like it was longer than a minute.
* I would like to convey more information to the user through the light to keep the user engaged.

\*\***Are there new ideas that occur to you or your collaborators that come up from the acting?**\*\*

New Idea : 
* Breakdown the steps of Brushing into the following steps:

   * Step 1: Brush the Outer Surface of the Upper Teeth.
   * Step 2: Brush the Outer Surface of the Lower Teeth.
   * Step 3: Brush the Biting Surface of the Upper Teeth.
   * Step 4: Brush the Biting Surface of the Lower Teeth.
   * Step 5: Brush the Inner Surface of the Upper Teeth.
   * Step 6: Brush the Inner Surface of the Lower Teeth.

* Since there are six steps and the recommended duration for brushing your teeth is 2 minutes. I am diving all the steps into equal durations of time.
Each Step will be done for 20 seconds.

* I am going to allocate colors for each step. Everytime the toothbrush changes its color, the user will perform the step associated with it.

    <img width="257" alt="image" src="https://user-images.githubusercontent.com/66789469/187323964-ffdbfa2c-6fe7-4666-946f-b2eaaf2c6d30.png">

* Storyboard for New Idea:

    ![Untitled (4)](https://user-images.githubusercontent.com/66789469/187329303-52d8a817-432d-44bf-a6ab-f242253f4703.jpg)

## Part C. Prototype the device

You will be using your smartphone as a stand-in for the device you are prototyping. You will use the browser of your smart phone to act as a “light” and use a remote control interface to remotely change the light on that device. 

Code for the "Tinkerbelle" tool, and instructions for setting up the server and your phone are [here](https://github.com/FAR-Lab/tinkerbelle).

We invented this tool for this lab! 

If you run into technical issues with this tool, you can also use a light switch, dimmer, etc. that you can can manually or remotely control.

\*\***Give us feedback on Tinkerbelle.**\*\*

  * I did face an issue while trying to install the requirements.txt
  * Fix: Changed Gevent version to v21.12.0 and greenlet to >= 1.1.0 in the requirements.txt file.

## Part D. Wizard the device

\*\***Include your first attempts at recording the set-up video here.**\*\*

https://drive.google.com/file/d/1nMv6Hhr5GmIExjmIS7vnezWTVvrR-sSS/view?usp=sharing

Now, hange the goal within the same setting, and update the interaction with the paper prototype. 

\*\***Show the follow-up work here.**\*\*

* While trying the set-up for the first time, I had to constantly look down at the phone screen to see the color, which was inconvinient. 
* To make the device more user-friendly, I am adding the color indicating light on the toothbrush as shown below.
    * <img width="217" alt="Screen Shot 2022-08-30 at 12 56 56 AM" src="https://user-images.githubusercontent.com/66789469/187352643-b957e54b-0bcc-4e32-a6fb-67a31bbbc7c4.png">

## Part E. Costume the device

\*\***Include sketches of what your device might look like here.**\*\*

<img width="1065" alt="Screen Shot 2022-08-30 at 1 38 13 AM" src="https://user-images.githubusercontent.com/66789469/187358142-0d7b7e62-abe3-4cbd-8e17-5d9eb38e746d.png">


\*\***What concerns or opportunitities are influencing the way you've designed the device to look?**\*\*

* I've added the Color changing LED to the upper part of the toothbrush, so that the user can still see the LED while holding the toothbrush.
* Concern: The LED on the toothbrush might be too small to capture the user's attention.

## Part F. Record

\*\***Take a video of your prototyped interaction.**\*\*

https://drive.google.com/file/d/1nUVVzPG4UXP5E_6qMvV0WUXcOatT7RGS/view?usp=sharing

\*\***Please indicate anyone you collaborated with on this Lab.**\*\*

N/A

# Staging Interaction, Part 2 

This describes the second week's work for this lab activity.


## Prep (to be done before Lab on Wednesday)

\*\***Summarize feedback from your partners here.**\*\*

Elyse Toder: When a person is holding the toothbrush they may not be able to see the color changing unless they stand in front of mirror. You could add another indicator to catch the user's attention.

Ravi Niteesh Voleti: You can use a vibration every 20 seconds to alert the user to brush a different portion of their teeth.

Sarang Pramode: Add a voice alert/message every time the light changes or even just a "ding" sound. For example: "Brush biting surface of Upper Teeth now". 20 seconds later: "Brush inner surface of Upper Teeth now".

Feedback from TA:
Nice and clearly documentation, Aashika! The storyboards are very clear and also the sketches are easy to understand. One thing I would suggest is to explore the novelty of this idea, since this kind of device has already been implemented in a lot of smart toothbrushes. The video is clear in delivering the message as well! Overall good work!

## Make it your own

Do last week’s assignment again, but this time: 
1) It doesn’t have to (just) use light, 
2) You can use any modality (e.g., vibration, sound) to prototype the behaviors! Again, be creative!
3) We will be grading with an emphasis on creativity. 

\*\***Document everything here. (Particularly, we would like to see the storyboard and video, although photos of the prototype are also great.)**\*\*

Based on the feedback received, I want to focus on the following parameters while improving my product:
1) Novelty
  * I looked at the existing Smart Toothbrushes. Some of the existing products that are similar to my proposed idea were:
    * Philips Sonicare 9900 Prestige 
    * Oral-B Genius Pro 8000
  * Both of these brushes interfaced with an app which showed the user which portion of the teeth they should brush and used light as an indicator.
  * Both of them used pressure/vibration to alert the user.
  * None of them used sound as a modality to alert the user.
      
2) Using sound as additional indicator to catch the User's Attention
  * Instead of just using a "ding" or "voice alert" I want to use music as my sound alert to catch the user's attention.
  * Listening to music in the morning is recommended because it improves brain functionality and is good for a person's mental well-being.

Concept for new idea:

![Untitled (7)](https://user-images.githubusercontent.com/66789469/188531893-f61b1276-8561-4e91-bf0c-7dcafbd40e05.jpg)

Storyboard:

![Untitled (9)](https://user-images.githubusercontent.com/66789469/188534904-d555e96c-9130-465f-bd05-0114f77a2a1c.jpg)

Prototype:
https://drive.google.com/file/d/1p10-aJ3w0Jsf5Vbs2gTKKeMSBCHGt4bE/view?usp=sharing
