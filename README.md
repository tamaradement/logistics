    Shopify: Backend Developer Intern Challenge Question
    Intern candidate: Tamara deMent

    Inventory tracking web application 
        Data structure:
            Objects:
                - Warehouse
                - Item
            Properties:
                - Warehouse
                    - name
                    - city 
                    - state
                - Item:
                    - type
                    - brand
                    - unit_Count
                    - unit_weight
                    - location (Warehouse, foreign key)
            Relationship: 
                - Warehouse/Item: One to many
                    - A warehouse can have many items (>=0)
                    - An item belongs to one warehouse (=1)
            Deletion:
                - When a warehouse is deleted, items stored at that location(warehouse) are also deleted.

    App requirements:
        [X] Create inventory items
        [X] Edit Them
        [X] Delete Them
        [X] View a list of them

    Additional features:
        [ ] When deleting, allow deletion comments and undeletion.
        [X] Ability to create warehouses/locations and assign inventory to specific locations.
        [ ] Ability to create “shipments” and assign inventory to the shipment, and adjust inventory appropriately

    Demo link:
        https://www.loom.com/share/26653479039b4240b9f38325a6cb5876

    Ideas for new features:
        [ ] Make inventory list items filterable by warehouse.
        [ ] When a warehouse is deleted, have option to move inventory stored at that location elsewhere.
