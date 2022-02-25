# Django
## Maktab 64 | Task 20
### Logging

----
### A. Formatter
Provide the following formatters:  
1. **short: `{LEVEL_NAME} ({TIME}): "{MESSAGE}"`**    
**E.g.**  
    - INFO (2021-08-12 09:21:17,285) "Asqar"
    - DEBUG (2021-08-12 09:21:17,300) "Akbar"
  
2. **verbose: `{LEVEL_NAME} ({TIME}): "MESSAGE" at MODULE_NAME (process: {PROCESS}, thread: {Thread})`**  
**E.g.**  
    - ERROR (2021-08-12 10:49:49,978): "Error(40) msg" at views (process: 45355, thread: 139718495606528)
    - CRITICAL (2021-08-12 10:49:49,978): "Critical (50) msg" at views (process: 45355, thread: 139718495606528)

### B. Filter 
Use `CallbackFilter` or Implement a custom filter to   
_**Filter records with message length greater than 20.**_  
named `length_limit`

### C. Handler  
Provide the handlers below:
1. **console:** uses `short` formatter & `length_limit` filter. 
2. **file:** uses `verbose` formatter & level = 'ERROR'

### D. Root
Set root logger handlers -> console
Level -> DEBUG

### E. Custom logger
Provide custom loggers below:  
1. **project:** uses `file` handler, level = ERROR and propagate = True  
2. **project.developers:** uses `file` handler, level = DEBUG and propagate = False  

