# Overview
This project is our way of getting a look into how you work as a developer. Asking whiteboard/pseudocode questions can be helpful, but we are also interested in how you work in an environment closer to what the job will entail. You will have much more time to work on this than it should take to complete, we estimate It to take around four hours. We ask that you try to ration your time to a similar window and roughly track your time.

> Before you is a (hopefully) bug free starting project that a coworker created right before leaving on vacation. Some priorities have shifted and we need to add a couple of key features before the end of the week; luckily as our powerhouse developer we know you can handle the short notice. The requested features can be found below.

### Style and Implementation
As a test of your general skill as a developer, we would like you to treat this like adding a feature to a real service. For example, follow the code style and formatting from existing files, try to use existing packages instead of importing similar alternatives, and keep consistent with commenting strategies. If you require additional packages not defined in the poetry dependencies please add them.

### Testing
For each feature you add to the project, we would like one or more test case(s) added to the pytest suite. You can separate these out into new files or just add them to the existing `test_paste.py` file. You can follow the examples given to test your new features, and expect these tests to provide validation of your code.

# Features
- A major project at the company relies on a hard-coded paste ID for their service and cannot change that value for the sake of national security. We need to be able to change the value for a given ID, design an endpoint that allows the user to update the value a desired paste.
- Some developers have accidentally stored company secrets in paste and need to remove their entries. Create an endpoint which can delete pastes. 
- Opening up every paste to every user could prove to be problematic. Add a feature so that a paste can only be accessed when provided with the correct secret.
- A team wants to share some data using paste, but only for a couple of hours. Add a feature for timed pastes, so that they can only be accessed for a given amount of time defined at creation.
- Sometimes people forget the ID for their paste entry, but they somehow remember the value they entered. Create an endpoint that will return a set of paste ID's that contain the submitted content string.
- Our product is opening up to the global market, and we need some of our paste values to be translated based on region. Create an endpoint that takes in a paste entry ID and a language, and returns the text result of a google translate transformation. We do not care if the result is well translated or makes any sense whatsoever, just return whatever google translate decides. 
