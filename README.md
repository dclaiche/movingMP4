Step 1: Install the Advanced Scene Switcher Plugin
Download the Advanced Scene Switcher plugin from [here.](https://obsproject.com/forum/resources/advanced-scene-switcher.395/)
Install the plugin following the instructions provided on the page.

Step 2: Configure the Scene Switcher to Trigger on Stream Stop
Open OBS Studio.
Go to Tools > Advanced Scene Switcher.
In the Advanced Scene Switcher window, go to the "Macro" tab.
Click Add to create a new macro.

Step 3: Set Up the Macro to Run Your Python Script
Name your macro (e.g., "Run Python Script to Organize on Stream Stop").

Add Condition:

Click Add under Conditions.
Select Streaming > Streaming State and set it to Stopped.
This condition tells OBS to trigger the macro only when streaming stops.

Add Action:

Click Add under Actions.
Choose Run program.
In the program path, point to your Python executable (e.g., C:\path\to\python.exe).
**NOTE** **You have to have python downloaded**
In the Arguments field, specify the path to your script (e.g., C:\path\to\your_script.py).
Download my "sortmp4.py" file and copy the path to it.

Save the macro configuration, and close the Advanced Scene Switcher settings.




This is how it works once stream is closed
![Screenshot 2024-10-29 112319](https://github.com/user-attachments/assets/5fe60714-8deb-41b8-b518-d98ae3ee7c1a)

Copy folder path to mp4 files
![Screenshot 2024-10-29 112358](https://github.com/user-attachments/assets/1b7376bd-126e-4cce-89ca-31f560070d13)

Enter program with the following python + scriptfilename + source_folder_of_mp4_files + destination_folder + anystring
Make sure to put spaces between everything. I used the same source and destination folder in the example.
![Screenshot 2024-10-29 112421](https://github.com/user-attachments/assets/7a701a2a-d1da-46cc-b9ff-3dc42e817c82)

Output
![Screenshot 2024-10-29 112429](https://github.com/user-attachments/assets/ef782e79-ae24-41e3-930c-05c20667c264)

Output
![Screenshot 2024-10-29 112637](https://github.com/user-attachments/assets/e59d94d5-e99d-4391-87b1-7be752b973fd)
