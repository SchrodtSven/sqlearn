# Foo
- https://mermaid.js.org/syntax/entityRelationshipDiagram.html

```mermaid
---
    config:
        layout: elk
---
erDiagram

    CAL_USR ||--o{ EVENT_APPLICATION : places
    CAL_USR {
        int usr_id
        Person P_DATA
        
    }
    EVENT_APPLICATION ||--|{ EVENT : contains
    EVENT_APPLICATION {
        int appl_id
        int usr_id
        Status  status_id
    }
    EVENT {
        
        int usr_id
        int loc_id
        int cat_id
        datetime e_start
        datetime e_end
        string title
        string description
    }

 ```
```mermaid 
graph LR
      A["$$x^2$$"] -->|"$$\sqrt{x+3}$$"| B("$$\frac{1}{2}$$")
      A -->|"$$\overbrace{a+b+c}^{\text{note}}$$"| C("$$\pi r^2$$")
      B --> D("$$x = \begin{cases} a &\text{if } b \\ c &\text{if } d \end{cases}$$")
      C --> E("$$x(t)=c_1\begin{bmatrix}-\cos{t}+\sin{t}\\ 2\cos{t} \end{bmatrix}e^{2t}$$")
```