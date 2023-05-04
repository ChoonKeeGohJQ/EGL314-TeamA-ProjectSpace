# EGL314-TeamA-ProjectSpace
*Scrum link : https://docs.google.com/spreadsheets/d/1K91aIip-ZL4T0M8RgZgr2uuCa6e8iVZyCFgKndAOjxg/edit?usp=sharing*

*Slides link : https://docs.google.com/presentation/d/1gpmwZyzl72j914PGxcWpIQM8QkVoPqJsxVBmEhtlBfE/edit*
## Team composition and roles
Team Lead : Yi Shan
Asst Team Lead : Choon Kee
Video : Yi Mon
Programming : Thinesh & Aloysius
## Storyboard

## Floor Plan
![Floorplan](imgs\floorplan.jpg)

# System Diagrams 

## Video
```mermaid
graph LR
Laptop --> B[Media Server] --> C[HDMI Extender Tx]
C --> D[HDMI Extender Rx] --> Projector
```
## Audio

## Control

### Video
```mermaid
graph LR
Laptop --> B[Media Server]
B --> C[HDMI Extender TX]
C --> D[HDMI Extender RX]
D --> E[Projector]
```
### Audio

### Control

## Research 

## Codes
```
This is a sample code block

```
## Game Ideas
Reference links : 
- https://www.youtube.com/watch?v=3QKiK4rJIB0
- https://www.create-learn.us/blog/easy-games-to-code/

```mermaid
stateDiagram
    [*] --> Team_Lead
    Team_Lead --> [*]

    Team_Lead --> Team_Members
    Team_Members --> Team_Lead
    Team_Members --> Track_Own_Tasks
    Track_Own_Tasks --> [*]
```
