## Inspiration
While A.I. has an undeserved stigma for being bad for humankind and culture, we want to prove that within the right hands and minds, machine learning can actually help greatly improve lives and be ethical. As students who seek to improve our social anxiety, we would use Moe to also improve our own social and emotional skills and understanding.

## What it does
Moe is a pocket-buddy for your shirt-pocket that records in real-time and alerts the user through sound feedback for any negative emotions that may be detected in your social interactions. Moe also works on selfie-mode. Negative emotions are saved in the database to later quiz users to help train and develop socio-emotional awareness according to tested and true developmental psychology therapy methods for people who suffer from Autism Spectrum Disorder.

## How we built it
Moe uses DeepFace-powered Machine Learning models and OpenCV HAAR Cascades incorporated onto a Raspberry Pi. Specifically, the program, developed by **Abdullah Mohammad**, incorporates Deepface Single-Shot Detector models and utilizes HAAR Cascades with openCV on an external camera in order to read real-time emotions on the faces of individuals the user interacts with. Emotions include anger, disgust, surprise, happiness, sadness, and fear. \
\
Moe also incorporates a quizzing feature designed by **Jacob Johnston** to allow individuals with ASD to practice identifying emotional cues and matching emotional states with recorded faces from people these individuals interact with on a daily basis. These images are saved to a local database only accessible to users of the device. If we were given more time, we would have utilized face-matching algorithms to create a whitelisting database to further enhance privacy and add consent to the recording. \
\
**Chahid Bagdouri** was our hardware lead, providing connections and support with an external WebCam and an Anker Bluetooth Speaker. As proof of concept, we used this external Bluetooth speaker to play audio. If we were to do this again, we would use a vibration motor to provide subtle signals to the user to alert them of certain social cues they may have missed throughout a live conversation or interaction.

## Challenges we ran into
While Moe reads facial emotion recognition onto the wearer's social interactions, Moe originally was going to ALSO support speech emotion recognition in the wearer themselves. We got it working through speech-to-text analysis AND live audio analysis, but the results were not accurate enough as we'd like. There were too many false-flags in our testing. While the OpenSmile library extracts accurate data, finding a consistently accurate pre-trained machine learning model was a little difficult. We tried different pre-trained models in Hugging Face. We also ran into the challenge of originally providing Moe to use a vibration sensor module. While a vibration is great, silent feedback that is hidden from everyone else as to not hinder the wearer's social interactions, it does not translate well for a demo and so we used a bluetooth speaker.

## Accomplishments that we're proud of
We're proud of the accuracy of Moe. We're proud of how Moe actually helped us learn something about ourselves which is explained right below!

## What we learned
We were surprised to find out that our very own self-awareness and understanding of the facial emotions we give off may not have been as accurate in our own heads as we thought. However, thanks to Moe, we were able to look at the moments where we showed those emotions. We also learned a lot about developmental psychology, therapy, and autism spectrum disorder. Lastly, we learned how hardware and software can result in a lot of troubleshooting and how much experience matters.

## What's next for Moe - An Emotional Wellness Robot
We're proud of potentially moving this project forward even more by training more speech emotion detection and to even support the ability to improve one's public speaking and interviewing experience and strategies! Lastly, Social Stories are another popular therapy method for children with A.S.D. and it involves many moving parts, contexts, plots, and actions. Stories are explained to engage children and to reward them for thinking of the socially appropiate action. These things are better off illustrated in a book or website than incorporated with real life camera modules, however, we're definitely keeping our eyes on how A.S.D., robotics, and machine-learning can be used to not only improve the emotional wellness of children with A.S.D., but even teenagers, adults, and people without A.S.D. who may just experience social anxiety and a lack of social experience.

## Authors
By Abdullah Mohammad, Jacob Johnston, and Chahid Bagdouri \
\
Link to devpost: https://devpost.com/software/moe-iuj39e

## Resources used
Deepface \
OpenCV \
https://orangefreesounds.com/womp-womp/ \
Roblox Oof Sound

##
![Moe](https://github.com/ChahidBagdouri/moe/assets/147211478/02419d81-2b93-4ed4-b2c0-32345d0facae)
