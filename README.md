# Microapps2datautils
Data utils for handling files and content extraction / transformation

In progress:
Todo:

    
    A) Brand - Models:
        1. extract B&M from brand and model fields (EqAlloc)
        2. extract B&M from brand and model fields (Equipment(description))
        3. extract matched B&M by description
        *** bonus: brand origin / country
        Result: B&M + modification data & id "tokens"
    B) Types/Categories: 
        [x]1. extract labeled category by equipment type(EqAlloc) *** partial match of types.
        [x]2. extract keyword category by description field (kw extract)
        [x]3. if exist: extract weight and measuring units && normalize it.
        [x]4. extract similarities based on VIN and mark/model
        Result:
        [best case: B1 & A1 steps results combined with 3rd block are final ] 
        Fail-safe: 1st step results into Category, buildup with 4th block results.   
    
    C) Fuels-Propulsion (FP)
        1. extract and map by EquipAlloc field /if exists
        2. match with Brand & Model(A) - only EV -> to result. 
        3. extract by Equipment field(description)
        4. extract by VIN
        [fail-safe] by 4.
        Result: fuel/propulsion 
    D) Emission 
        1. By EquipAlloc emission field
        2. By A), B) and C)
        3. By Q2 rep.
        *** bonus - by previous data 
        
        Check missmatch.
        Result:...obvious. 
    
    E) Labels update, UUID
    F) GUI with FreeSimpleGui

    *** bonus:
        - DB log
        - TWG metrics
        - TWG APC file generator
        - TC file generator
        - DB-check - field per field log with previous data
        - EAA DB implementation - additional layer in A to D, after data cleaning.

    ****
