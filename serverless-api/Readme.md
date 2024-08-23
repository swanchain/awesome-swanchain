## Get Started 

If you want to run a "serverless api" docker project, please follow the steps below

## Build  Image


###
```shell
cd serverless-api
docker build -t serverless-api .
```
## Start a instance

```shell
 docker run serverless-api
```

Open the web page at http://0.0.0.0:7860, if success you can the following response 

```json
{
    "ping": "pong"
}
```

### API Endpoints

1. **GET /**
   - **Description**: Basic health check endpoint that returns a simple `ping` response.
   - **Response**:
     ```json
     {
       "ping": "pong"
     }
     ```

2. **POST /items/**
   - **Description**: Create a new item and add it to the in-memory database.
   - **Request Body**: JSON object representing the item to be added.
     ```json
     {
       "id": 1,
       "name": "Item Name",
       "description": "Item Description",
       "price": 100.0,
       "tax": 5.0
     }
     ```
   - **Response**: The created item.
     ```json
     {
       "id": 1,
       "name": "Item Name",
       "description": "Item Description",
       "price": 100.0,
       "tax": 5.0
     }
     ```

3. **GET /items/**
   - **Description**: Retrieve a list of all items in the in-memory database.
   - **Response**: A JSON array of items.
     ```json
     [
       {
         "id": 1,
         "name": "Item Name",
         "description": "Item Description",
         "price": 100.0,
         "tax": 5.0
       },
       {
         "id": 2,
         "name": "Another Item",
         "description": "Another Description",
         "price": 150.0,
         "tax": 7.5
       }
     ]
     ```

4. **GET /items/{item_id}**
   - **Description**: Retrieve a specific item by its ID.
   - **Path Parameter**: `item_id` (integer) - The ID of the item to retrieve.
   - **Response**:
     - **Success**: The item with the specified ID.
       ```json
       {
         "id": 1,
         "name": "Item Name",
         "description": "Item Description",
         "price": 100.0,
         "tax": 5.0
       }
       ```
     - **Error**: If the item is not found.
       ```json
       {
         "error": "Item not found"
       }
       ```