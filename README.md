# EGL314-TeamA-ProjectSpace

```mermaid
stateDiagram
    [*] --> Team_Lead
    Team_Lead --> [*]

    Team_Lead [Add_Members] --> Team_Members
    Team_Members --> Team_Lead
    Team_Members [Self_Monitor] --> Track_Own_Tasks
    Track_Own_Tasks --> [*]
```
