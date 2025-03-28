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
