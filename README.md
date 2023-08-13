# EGL314-TeamA-ProjectSpace                 
# Bill Of Material (BOM)

 1. 1x Novation Launchpad Mk2
 2. 2x Raspberry Pi Raspi 4 Model B
 3. 1x Short Throw Projector Sony VPL-SW630
 4. 1x Media Server Lenovo ThinkStation P920
 5. 2x Ceiling Speakers Extron FF 220T
 6. 1x OEM Screen
 7. 1x Audio Amplifier Extron XPA 1002
 8. 1x Laptop HP Zbook 15 G5
 9. 1x HDMI Extender TX Kramer PT-571
 10. 1x HDMI Extender RX Kramer PT-572+
 11. 1x Wireless Router Netgear
 12. 1x LED Strips
 13. 1x Artnet/DMX Node 1 Eurolite
 14. 1x FTP3 RGB LED DMX Driver

 # Required Software and Licenses

 1. Christie Pandora Box
 2. Widget Designer
 3. Server Manager 
 4. Thonny Python IDE
 5. Dongles for Pandora license
 6. Toolbox
 7. VisionTools Pro-e
 8. SIMPL Windows

 # Network Settings

Login to router
</br>
username: admin
</br>
Login to router by going to a web browser and entering address 192.168.1.1 under URL section, then sign in with:\
username: admin\
password: password
![Alt text](<imgs/Router login.jpg>)
Name: TeamA
</br>
Password: mtswifipwd
![Alt text](<imgs/Router wireless setup.jpg>)
Router IP address set to 192.168.10.1
![Alt text](<imgs/Router LAN setup.jpg>)
 # How To Start
## Video Hardware Setup
![Alt Text](imgs/VideoHardSetup.jpg)
The video setup for our project consists of a ultra-short throw projector mounted onto a truss, then secured with a safety cable.
![Alt Text](imgs/ProjectorMount.jpg)
The projector is shooting to a OEM Screen, which is placed on the floor.
![Alt Text](imgs/OemScreen.jpg)
Video is sent to the projector via HDMI Extender, sending signal from a Media Server.
![Alt Text](imgs/MediaServer.jpg)
Hdmi Extenders
![Alt Text](imgs/Transmitter.jpg)

## Audio Hardware Setup
![Alt Text](imgs/CeilingSpk.jpg)
The audio setup for our project consists of an audio amplifier receiving input from a laptop via a 3.5mm cable sending to two ceiling speakers
![Alt Text](imgs/3.5mm.jpg)
Amplifier Receiving input from laptop
![Alt Text](imgs/Amplifier.jpg)
Speaker cable out from amplifier sending to ceiling speakers
![Alt Text](imgs/SpkToAmp.jpg)

## Video Software
For video we are sending content from Pandoras Box to a media server, connected via a LAN cable and controlled by Server Manager, while also being controlled with Widget designer.

Start by Opening your network settings by right-clicking your wifi logo at the bottom right of your screen
<br>![Alt Text](imgs/Pandora%20Imgs/Open%20network%20settings.png)<br>
Then, go to Change adapter options
<br>![Alt Text](imgs/Pandora%20Imgs/Change%20Adapter%20Settings.png)<br>
Right click Ethernet and open up properties
<br>![Alt Text](imgs/Pandora%20Imgs/Ethernet.png)<br>
Then open Internet Protocol Version 4 (TCP/IPv4) properties and set your ip to 192.168.10.10, subnet mask to 255.255.255.0
<br>![Alt Text](imgs/Pandora%20Imgs/Ipv4.png)<br>
Now, Open pandora and start a new project
<br>![Alt Text](imgs/Pandora%20Imgs/NewfilePB.jpg)<br>
Name your project accordingly
<br>![Alt Text](imgs/Pandora%20Imgs/Rename.jpg)<br>
Then, right click your project folder at the left side of the app, and add a new folder. This will be the content folder
<br>![Alt Text](imgs/Pandora%20Imgs/AddFolder.png)<br>
To find content, use the navigation tool in the center of the screen, the directory for the downloads folder is (C:/Users/"username"/Downloads), bring in content by dragging content in from the navigation to the previously created content folder.
<br>![Alt Text](imgs/Pandora%20Imgs/FileDir.png)<br>
Next, we drag in content from our content to folder directly to our layers.
<br>![Alt Text](imgs/Pandora%20Imgs/Addimg2Layer.png)<br>
Then, we position our items in the property editor
<br>![Alt Text](imgs/Pandora%20Imgs/Positioning.png)<br>
Next, go to Configuration>Network and check your domain.
<br>![Alt Text](imgs/Pandora%20Imgs/CheckdomainPB.png)<br>
Open Server Manager and check if your Media server is connected, if it's not, check your connection between the laptop and the Media Server through your LAN cable. Else, Right click your server in the application and click connect VNC
<br>![Alt Text](imgs/Pandora%20Imgs/ConnectVNC.png)<br>
Next, Open Pandoras Box in the Media Server and make sure the domain number matches the one in Pandoras Box in your laptop,
<br>![Alt Text](imgs/Pandora%20Imgs/Open%20Pandora.png)<br>
Open Widget Designer and create a new file.
<br>![Alt Text](imgs/Pandora%20Imgs/FileNew.png)<br>
Add buttons by going to Widgets>Buttons and clicking CustomScript, this will set you in state where you can only add buttons
<br>![Alt Text](imgs/Pandora%20Imgs/Addbutton.png)<br>
Button adding state
<br>![Alt Text](imgs/Pandora%20Imgs/make%20button.png)<br>
To exit the button adding state, click the icon selected in the image at the top of the application
<br>![Alt Text](imgs/Pandora%20Imgs/Esc.jpg)<br>
At the end, you should have 40 buttons in total
<br>![Alt Text](imgs/Pandora%20Imgs/Final%20Layout.jpg)<br>
Double-click the button and change its type to toggle inside Settings and add in codes
<br>![Alt Text](imgs/Pandora%20Imgs/doubleclick.png)<br>

## The codes to use for buttons are:

### **To toggle the layer's opacity for Player 1**
Note that X means Device number and Y means layer number

onClick script:

(the portion after changing the opacity is for audio playback)
```
DeviceSetParam(X,Y,"Opacity",255)
DeviceSetParam(X,Y,"Playback Transport","Play")
WDWait
(0.5)DeviceSetParam(X,Y,"Playback Transport","Stop")
```

onRelease script:
```
DeviceSetParam(X,Y,"Opacity",0)
```
Master script to turn opacity down and release pressed state
```
DeviceSetParam(X,Y,"Opacity",0)
WDCustomScriptSetState(3,"Released")
```

Next, navigate to Connections>Remoting at the top of the application
<br>![Alt Text](imgs/Pandora%20Imgs/Remoting.jpg)<br>
Inside the Remote input control, set your TCP port to 5005 and Enable TCP connection.
<br>![Alt Text](imgs/Pandora%20Imgs/TCPSet.jpg)<br>


## Raspberry Pi
Download and install raspbian  

![Alt text](<imgs/Raspi Setup/Raspi Setup 1.jpg>)  

Choose the operating system as Raspberry Pi OS (32-bit)  

![Alt text](<imgs/Raspi Setup/Raspi Setup OS.jpg>)  

Choose the storage device, being the SD card that will be used to store data for the Raspberry Pi  

![Alt text](<imgs/Raspi Setup/Raspi Setup Storage.jpg>)  

Pick advanced options, enable hostname and SSH, then enter a hostname of your choosing, in this case, its TeamA2  

![Alt text](<imgs/Raspi Setup/Raspi Setup Advanced 1.jpg>)  

Enable set username and password then create a username and password, in this senario username being TeamA2, password being mtswifipwd  

![Alt text](<imgs/Raspi Setup/Raspi Setup Advanced 2.jpg>)  

Enable Configure wireless LAN and enter the SSID and password according to the SSID and password according what was configured in the netgear router  

![Alt text](<imgs/Raspi Setup/Raspi Setup configure wireless LAN.jpg>)  

Select write  

![Alt text](<imgs/Raspi Setup/Raspi Setup 2.jpg>)  

Note that the SD card will be formatted and everything in it will be erased, do not use a SD card will has data in it  

![Alt text](<imgs/Raspi Setup/Raspi Setup Write Confirmation.jpg>)  

Wait for raspbian to fishing writing  

![Alt text](<imgs/Raspi Setup/Raspi Setup Writing.jpg>)  

Now you can remove the SD card from your laptop and insert it into the raspberry pi  

![Alt text](<imgs/Raspi Setup/Raspi Setup Finished writing.jpg>)  

After the Raspberry Pi finishes starting up, go the command terminal, and type the command "ifconfig" and look for the the ip address of the raspberry pi, in this case being 192.168.10.4  

Use the command sudo raspi-config and enable VNC  

![Alt text](<imgs/Raspi Setup/Raspi ifconfig.jpg>)  

Download and install VNC viewer, enter the ip address of the raspberry pi  

![Alt text](<imgs/Raspi Setup/VNC 1.jpg>)  

Login to raspberry pi  

![Alt text](<imgs/Raspi Setup/VNC 2.jpg>)



## Installing neccesary Libraries.

### 1. Library to use.
- mido  
- rtmidi

### 2. Open Terminal in Raspberry Pi  
![Alt text](imgs/Raspi/OpenTer.jpg)  

### 3. Enter command line to install library
replace pip with whichever version of python you are using.
if you are using python verion 3 then use 'pip3' instead of 'pip'
- install mido library
'pip install mido'
- install python-rtmidi
'pip install python-rtmidi'

### 4. if installing the library happens to fail, try the following steps.
 - Open Raspberry Pi Configuration
 ![Alt text](imgs/Raspi/OpenRaspiConfig.jpg)
 - go to Localisation
 - Set Timezone and Wireless LAN Country to your country.
 ![Alt text](imgs/Raspi/RaspiConfigLocalisation.jpg)

## TicTacToe with TCP(MK2)
### 1. Open Thonny in Rapberry Pi

### 2. Using the code  
- Either import the the program file for
[Tic-Tac-Toe](<Game codes/TicTacToeWTCP>), or the program file for [BattleShip](<Game codes/BattleShip/game.py>) and open in Thonny
![Alt text](imgs/Raspi/ThonnyFileOpen.jpg)

- Or insert the code below into a new file in Thonny and save.
![Alt text](imgs/Raspi/ThonnyPage.jpg)

## Lighting Set Up (Hardware)

Our set up for lighting consist of LED Strips, Artnet/DMX Node, DMX Driver and laptop. This is how the set up look like:

![Alt Text](imgs/lighting%20set%20up/setup.jpg)

The laptop is connected to the Artnet via LAN cable. 


The Artnet is then connected to the DMX driver via DMX to Terminal Block cable as a DMX output, making the driver as DMX Input. 

On the Artnet, the output is set as DMX

![Alt Text](imgs/lighting%20set%20up/artnet.jpg)

The IP Address on the Artnet is set to 2.0.0.3 and the subnet is 255.0.0.0 as the Artnet only supports Class A IP Address. The universe is set to 1.

![Alt Text](imgs/lighting%20set%20up/ip0.jpg)
![Alt Text](imgs/lighting%20set%20up/ip1.jpg)
![Alt Text](imgs/lighting%20set%20up/ip2.jpg)
![Alt Text](imgs/lighting%20set%20up/ip3.jpg)
![Alt Text](imgs/lighting%20set%20up/sw0.jpg)
![Alt Text](imgs/lighting%20set%20up/sw1.jpg)
![Alt Text](imgs/lighting%20set%20up/sw2.jpg)
![Alt Text](imgs/lighting%20set%20up/sw3.jpg)
![Alt Text](imgs/lighting%20set%20up/universe.jpg)

The LED Strips are connected to the driver's output accroding to the RGB colours. The power is connected to DC Input via terminal block. 

On the DMX Driver, the start address is set to 1. 

Since we are using DMX output, the seetings are set accroding to the settings shown on the driver for the DMX Mode.

![Alt Text](imgs/lighting%20set%20up/dmxdriver.jpg)

The LED Strips are hang around the table where players sit at to play games.

![Alt Text](imgs/lighting%20set%20up/light.jpg)

## Lighting Up LED (Software)

We used Pandora Box and Widget Designer to control the lights.
We need to check that the LAN cable IP address is in Class A IP to match with the IP Adrress on the Artnet. 

To do that, right click on the Wifi Logo and go to Open Network & Internet Settings

![Alt Text](imgs/Pandora%20Imgs/Open%20network%20settings.png)

Go to Change Adapter Options

![Alt Text](imgs/Pandora%20Imgs/Change%20Adapter%20Settings.png)

Right click on Ethernet 3 and go to properties

![Alt Text](imgs/Pandora%20Imgs/ethernet3.png)

The Ethernet 3 properties page will appear. 

Click on Internet Protocol Version 4 (TCP/IPv4) and go to properties

![Alt Text](imgs/Pandora%20Imgs/ethernetproperties.png)

The properties page will appear and make sure the ip address is in Class A with the correct subnet, make changes if needed.

![Alt Text](imgs/Pandora%20Imgs/ipsettings.png)

On Pandora, we add in a device for LED Strips and patching the lights.

To add in a device:

Under Tabs, go to Device Types

![Alt Text](imgs/Pandora%20Imgs/devicetype2.png)

This device window will appear. Afterwards go to DMX Fixtures

![Alt Text](imgs/Pandora%20Imgs/devicetype.png)

Under the DMX Fixture, go to the _GENERIC file. Under the _GENERIC file, select _GENERIC@RGB 3ch.clib

![Alt Text](imgs/Pandora%20Imgs/dmxfixture.png)

Drag the file to the device tab

![Alt Text](imgs/Pandora%20Imgs/devicetab.png)

For patching:

Right click on the layer _GENERIC@RGB 3ch and go to Patch and click on Reveal in Patch Tab

![Alt Text](imgs/Pandora%20Imgs/revealpatchtab.png)

The patch window will appear.

![Alt Text](imgs/Pandora%20Imgs/patchwindow.png)

If it doesn't show any text box for DMX and universe in the patch window, right click on the layer _GENERIC@RGB 3ch and go to Patch and click on Set Patch Start Values

![Alt Text](imgs/Pandora%20Imgs/setpatch.png)

It will show the page for the start address and universe

![Alt Text](imgs/Pandora%20Imgs/autopatch.png)

Another way to do this is to go to Tabs and click on Patch

![Alt Text](imgs/Pandora%20Imgs/patchtab.png)

It will also show the same page as this

![Alt Text](imgs/Pandora%20Imgs/patchwindow.png)

In the patch window, tick the check box under patch. The channel will state 3 as there are 3 channels. Since we set our start address and universe 1 on the DMX driver and Artnet respectively, it is stated as 1 in Pandora. 

![Alt Text](imgs/Pandora%20Imgs/patchdetails.png)

Afterwards, we have to activiate ARTNET on PB Manager.

To do this:

Go to the configuration tab, then go to Remote Control Protocols.

Make sure to put the correct Network Adapter under Preferred Network Adapter. 

Afterwards click on Acitivate Output under Art-Net to activate the Artnet Output.

![Alt Text](imgs/Pandora%20Imgs/PBConfiguration.png)

Afterwards, pull the fader up to turn on the lights

![Alt Text](imgs/Pandora%20Imgs/fader.png)

Cues are created on the timeline to have different effects for when players play the tic tac toe game.

In the timeline:

Cue 1 is added to turn on red light when it is Player 1's turn.

Cue 2 is added to turn on blue light when it is Player 2's turn.

Cue 3 is added to flash red lights when Player 1 wins.

Cue 5 is added to flash blue lights when Player 2 wins.

![Alt Text](imgs/Pandora%20Imgs/lightingcues.png)

On the widget designer, buttons are created to control the different lighting effects programmed on the Pandora Box Timeline.

![Alt Text](imgs/Pandora%20Imgs/widget.png)

When players are playing, the lights will light up either red or blue accroding to the player's turn. 

In this case if it is Player 1's turn, the lights will turn on red. If it is Player 2's turn, the lights will turn on blue.

For the winning statement, the lights will either flash red or blue lights depending on which player wins. 

In this case if Player 1 wins, the lights will flash red lights. If Player 2 wins, the lights will flash blue lights.

## Control Setup

To Program a control interface with Cretron, 3 softwares are required.

</br>

The first software being Toolbox 
</br>

![Alt text](<imgs/Crestron Config/Crestron Config 01.jpg>)

Ensure that a connection is established with the processor, be it wired or wireless.
</br>

![Alt text](<imgs/Crestron Config/Crestron Config 02.jpg>)

In Crestron Toolbox, click on the address book icon
</br>

![Alt text](<imgs/Crestron Config/Crestron Config 05.jpg>)

If it is the first time connecting to the processor, use a USB connection to find out the IP address on the processor.
</br>

![Alt text](<imgs/Crestron Config/Crestron Config 03.jpg>)

After connection is established, ethernet settings to change the default IP address to one with the same subnet as your station, in our case, it's 10.

![Alt text](<imgs/Crestron Config/Crestron Config 07.jpg>)

![Alt text](<imgs/Crestron Config/Crestron Config 08.jpg>)

A TCP connection can be substituted for the USB connection.
</br>

![Alt text](<imgs/Crestron Config/Crestron Config 04.jpg>)

Ensure that it shows that you are connected.

![Alt text](<imgs/Crestron Config/Crestron Config 06.jpg>)

You can follow up with opening the VisionTools Pro e application.
</br>

![Alt text](<imgs/Crestron Config/Crestron Config 19.jpg>)

Create a new project file and follow up by designing the GUI.
</br>

![Alt text](<imgs/Crestron Config/Crestron Config 10.jpg>)

![Alt text](<imgs/Crestron Config/Crestron Config 11.jpg>)

After designing the GUI and setting the visibility digital join in VisionTools Pro e and compile the project, you can start programming the connection on SIMPL windows.
</br>

![Alt text](<imgs/Crestron Config/Crestron Config 20.jpg>)

In SIMPL Windows, create a new module and enter all program header infomation. 
</br>

![Alt text](<imgs/Crestron Config/Crestron Config 12.jpg>)

![Alt text](<imgs/Crestron Config/Crestron Config 13.jpg>)

In the configure page, search for the processor module under control systems, X panel windows under Touchpanel and TCP/IP client under Ethernet Control Modules in Device directories
</br>

![Alt text](<imgs/Crestron Config/Crestron Config 14.jpg>)

![Alt text](<imgs/Crestron Config/Crestron Config 22.jpg>)

![Alt text](<imgs/Crestron Config/Crestron Config 23.jpg>)

In the program page, program the connection between touchpanel and the devices using drivers.
</br>

![Alt text](<imgs/Crestron Config/Crestron Config 15.jpg>)

If the drivers for the devices are not available in the symbol libary, it can be aquired from the Crestron application market.
</br>

![Alt text](<imgs/Crestron Config/Crestron Config 17.jpg>)

Once you finish programming all the connections, you can compile and send the program to your touchpanel.
</br>

![Alt text](<imgs/Crestron Config/Crestron Config 16.jpg>)

Return to VisionTools pro e to open your xpanel with the play button.
</br>

![Alt text](<imgs/Crestron Config/Crestron Config 18.jpg>)

Xpanel will appear and can be used as the control your devices.

![Alt text](<imgs/Crestron Config/Crestron Config 21.jpg>)

