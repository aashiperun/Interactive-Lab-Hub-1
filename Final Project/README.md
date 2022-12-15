# Final Project Documentation 

### Project:

Smart Medicine Dispenser [ForMed] -> [ Requires no text input to function + Lets the user choose desired formulation for pills ]

### Team Members:
1) Aashika Perunkolam - ap966
2) Anjali Vyas - av379

### Big Idea:

Older adults with cognitive deficits often find it difficult to live independently as they require assistance with different tasks of daily living. To enable independent living we are going to focus on one of the most critical tasks of daily living for older adults which is to take their medications on time to prevent further cognitive decline. To ensure this, we built a prototype of a smart medicine dispenser with key differentiators that cater specifically to older adults.

### Project Proposal

https://github.com/aashiperun/Interactive-Lab-Hub-1/blob/Fall2022/Final%20Project/Project_Proposal.md

### Documentation of the Design Process

#### What was our motivation?
* Our idea for the smart pill dispenser was inspired by Aashika’s Product Studio How Might We challenge: “How might we help older people with cognitive deficits to live independently?.”
* Older adults often need to take a variety of different pills for severe health conditions. On average, a person over 65 needs to take and manage 14-16 prescriptions a year. Many with memory problems face tremendous difficulty in keeping track of which ones they should be taking and when they should take each one. 
* Currently, there are many different products on the market for managing this problem such as pill organizers that come in a lot of different shapes and forms as shown in the figure below.

<img width="634" alt="image" src="https://user-images.githubusercontent.com/66789469/207875517-74bac6bd-15ee-4173-95af-b9452733656d.png">

* However, these aren’t very useful if the older adult using them forgets to take any pills in the first place given that the pill organizer may not always be in sight. It also relies on someone accurately sorting the medication in the correct compartments every single time and assumes that older adults will not mistakenly take medications from the wrong compartment. To tackle such issues several smart pill dispensers have also been developed.

<img width="578" alt="image" src="https://user-images.githubusercontent.com/66789469/207875748-362d5881-fa31-4aea-88f5-3b6cbb336e84.png">

* While these can give older adults a lot more support when it comes to reminders and requiring less frequent input for accurate dispensing, they are also very expensive devices that may not even have an option for one time payment and require costly subscription fees ($24.99/month in the case of Hero Health shown in the top right above and $39.99/month for Medminder shown in the middle).
* We were very motivated to explore the possibility of developing a low cost prototype that can be accessible to a lot more older adults and provide this support for them. We also wanted to devise useful features beyond just dispensing and reminding for our device. 

#### How did we ideate and design the device?
We knew that we wanted to build upon what current smart pill dispensers offer so we tried to think of different features that could offer more value to older adults by solving additional challenges that they face when it comes to taking medications or just in their day to day lives in general.

Ideation

✅ Feature 1 Being able to choose the drug formulation that works best (whole, split or powdered)

Reading up online, we found that swallowing medication or supplement pills whole can be a burdensome task for older adults, especially those who may have swallowing difficulties. Research (https://www.aarp.org/health/drugs-supplements/info-2019/supplements-choking-risk.html)  has also found that choking is more common amongst older adults who take supplements. To alleviate this challenge, older adults often consume pills after splitting them in half. At the same time, more and more drugs (https://www.advacarepharma.com/en/pharmaceuticals/ibuprofen-powder-for-suspension) are being offered in a powdered formulation globally.

This gave us the idea of prototyping a smart pill dispenser that can offer medication in all 3 different formulations - whole, split and powdered. We decided to not actually build out the crushing or splitting functionality but instead wizard it and focus more on optimizing the interaction and understanding the value this idea could bring to people first. Since it is not safe to split or crush all pills, we planned to have a safety feature built in that will only allow safe formulations to be dispensed for any pill stored in the device (we were not able to implement this in our current version but given more time we would definitely tackle this). 

✅ Feature 2 Using Image to Text Convertors to provide input to the medicine dispenser

All the current smart dispensers in the market require the user to enter medicine name, and prescription schedule through an app for it to provide reminders and dispense the pills. However, our target audience are older adults with cognitive deficits who find it difficult to use technology. To reduce cognitive load on the user, we aimed to build a device that requires no text input from the user to function. To achieve this, we built an image to text converter using OpenCV. The older adult only needs to place the pill bottle in front of the camera. The camera will capture the image of the pill bottle and extract text from the label to identify the medicine name, dosage information, etc. This would be one of the key differentiators of our device.

❌ Feature 3 Being able to receive positive thoughts and messages from loved ones

Older adults in the United States are more likely to live alone than anywhere else in the world. One study (https://www.pewresearch.org/fact-tank/2020/03/10/older-people-are-more-likely-to-live-alone-in-the-u-s-than-elsewhere-in-the-world/)  found that 27% of people over the age of 60 live by themselves in the United States compared to 16% in around 160 countries and territories that were studied. Moreover,  the pandemic has made in-person visits to older adults from their loved ones more restricted and they also tend to face more difficulty in using digital communication tools.

This made us think of incorporating a small feature into the pill dispenser that would allow older adults to receive messages from their loved ones through a web interface very similar to the one that would allow clinicians to send prescriptions to the device. The messages would come with a cheery chime like sound and be read aloud by our device while also being shown on the display. We thought that this simple interface could potentially be much easier for older adults to interact with than some kind of messaging app and could also facilitate a way for loved ones to let the older adult know that they are thinking of them even when they might be busy. This idea stemmed from something that one of us had thought of during Lab 1 (https://github.com/anjvyas/Interactive-Lab-Hub/tree/Fall2022/Lab%201#the-miss-you-machine) - the miss you machine. Unfortunately, we were not able to incorporate this feature into our device within the timeframe but we think it could be a nice addition to it in the future.

❌ Feature 4 Being able to sharpen memory with memory games and puzzles

A lot of older adults face memory problems and this impairs a lot of their day to day living activities even outside of remembering to take important medicines. We thought that it could be useful if our pill dispenser could also double up as an interface through which older adults can sharpen their cognitive abilities by playing fun games or puzzles. It could also serve as a good source of entertainment for them.

Ultimately after giving this feature idea some thought we decided against it because it might make the device too complicated for the first version and deviate our efforts from making the pill dispensing and reminding functionality as great as it can be.

#### Design and planning

Before we started to actually build out our device, we wanted to sketch it out to help us solidify  what we wanted it to be able to do and what it should look like. We thought having a good, concrete vision will make our building easier.

First we tried to understand all the components that we would have to build out

Note: we first tried using MQTT but later changed it to using MongoDB instead, and we left out the face recognition aspect completely

<img width="468" alt="image" src="https://user-images.githubusercontent.com/66789469/207895475-4d427ac9-3101-419c-bd3b-346371274417.png">

Then we spent some time thinking about the different parts we would need and how they would all come together

<img width="468" alt="image" src="https://user-images.githubusercontent.com/66789469/207895672-69c19f25-2b35-4f2f-9141-14d2a26b2089.png">

Next, we came up with a potential user flow to make sure that using our device would be easy and we hadn’t missed anything

<img width="342" alt="image" src="https://user-images.githubusercontent.com/66789469/207895758-caa5255f-178b-4c05-9069-d73142a787f4.png">




