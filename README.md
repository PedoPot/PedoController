# PedoController API Documentation

This document provides a comprehensive listing of all API endpoints in the PedoController system, along with their required parameters and return values.

## Table of Contents
- [Pedophile Endpoints](#pedophile-endpoints)
- [Baiter Endpoints](#baiter-endpoints)
- [Conversation Endpoints](#conversation-endpoints)
- [Message Endpoints](#message-endpoints)
- [Social Network Endpoints](#social-network-endpoints)

## Pedophile Endpoints

### POST `/pedocontroller/pedophiles/create`
Creates a new pedophile in the database.

**Parameters:**
- `nickname` (str): Pseudonym of the pedophile
- `socialNetwork` (int): ID of the associated social network
- `score` (int, optional): Pedophilia score
- `user_socialNetwork_id` (str, optional): User ID on the social network

**Returns:** Created Pedophile object with status 201, or errors with status 400

### PUT `/pedocontroller/pedophiles/update`
Updates an existing pedophile.

**Parameters:**
- `id` (int): Unique identifier of the pedophile
- `nickname` (str): Pseudonym of the pedophile
- `socialNetwork` (int): ID of the associated social network
- `score` (int): Pedophilia score
- `user_socialNetwork_id` (str, optional): User ID on the social network

**Returns:** Updated Pedophile object, or error 404 if not found

### DELETE `/pedocontroller/pedophiles/delete`
Deletes a pedophile.

**Parameters:**
- `id` (int): Unique identifier of the pedophile (query parameter)

**Returns:** Status code 204 if successful, 404 if not found

### GET `/pedocontroller/pedophiles/findOne`
Retrieves a specific pedophile.

**Parameters:**
- `id` (int): Unique identifier of the pedophile (query parameter)

**Returns:** Pedophile object, or error 404 if not found

### GET `/pedocontroller/pedophiles/findAll`
Retrieves all pedophiles.

**Parameters:** None

**Returns:** List of all Pedophile objects

### POST `/pedocontroller/pedophiles/findBy`
Searches for pedophiles based on criteria.

**Parameters (all optional):**
- `id` (int): Unique identifier
- `nickname` (str): Pseudonym
- `score` (int): Exact score
- `score_min` (int): Minimum score
- `score_max` (int): Maximum score
- `score_range` (str): Score range in format "min,max"
- `socialNetwork` (int): ID of the social network

**Returns:** List of matching Pedophile objects

### POST `/pedocontroller/pedophiles/get`
Pagination of pedophile results.

**Parameters:**
- Same parameters as `findBy`
- `numberPage` (int): Page number
- `numberResults` (int): Number of results per page

**Returns:** Paginated list of Pedophile objects

### POST `/pedocontroller/pedophiles/getScore`
Retrieves and computes the risk assessment score for a pedophile.

**Parameters:**
- `id` (int): Unique identifier of the pedophile

**Returns:** Pedophile ID and computed score, or error 404 if not found

## Baiter Endpoints

### POST `/pedocontroller/baiters/create`
Creates a new baiter (decoy).

**Parameters:**
- `socialNetwork` (int): ID of the associated social network
- `username` (str): Username
- `fullName` (str): Full name
- `email` (str): Email
- `password` (str): Password
- `bio` (str): Biography
- `location` (str): Location
- `gender` (str): Gender ('boy' or 'girl')
- `birthDate` (datetime): Date of birth
- `context` (str, optional): Baiter context

**Returns:** Created Baiter object with status 201, or errors with status 400

### PUT `/pedocontroller/baiters/update`
Updates an existing baiter.

**Parameters:**
- `id` (int): Unique identifier of the baiter
- Same parameters as for creation

**Returns:** Updated Baiter object, or error 404 if not found

### DELETE `/pedocontroller/baiters/delete`
Deletes a baiter.

**Parameters:**
- `id` (int): Unique identifier of the baiter (query parameter)

**Returns:** Status code 204 if successful, 404 if not found

### GET `/pedocontroller/baiters/findOne`
Retrieves a specific baiter.

**Parameters:**
- `id` (int): Unique identifier of the baiter (query parameter)

**Returns:** Baiter object, or error 404 if not found

### GET `/pedocontroller/baiters/findAll`
Retrieves all baiters.

**Parameters:** None

**Returns:** List of all Baiter objects

### POST `/pedocontroller/baiters/findBy`
Searches for baiters based on criteria.

**Parameters (all optional):**
- `id` (int): Unique identifier
- `username` (str): Username
- `email` (str): Email
- `location` (str): Location
- `gender` (str): Gender

**Returns:** List of matching Baiter objects

## Conversation Endpoints

### POST `/pedocontroller/conversations/create`
Creates a new conversation and initializes the first message.

**Parameters:**
- `baiter` (int): ID of the associated baiter
- `pedophile` (int): ID of the associated pedophile
- `socialNetwork` (int): ID of the social network

**Returns:** Created Conversation object with status 201, or errors with status 400

### PUT `/pedocontroller/conversations/update`
Updates an existing conversation.

**Parameters:**
- `id` (int): Unique identifier of the conversation
- `baiter` (int): ID of the associated baiter
- `pedophile` (int): ID of the associated pedophile
- `socialNetwork` (int): ID of the social network

**Returns:** Updated Conversation object, or error 404 if not found

### DELETE `/pedocontroller/conversations/delete`
Deletes a conversation.

**Parameters:**
- `id` (int): Unique identifier of the conversation (query parameter)

**Returns:** Status code 204 if successful, 404 if not found

### GET `/pedocontroller/conversations/findOne`
Retrieves a specific conversation.

**Parameters:**
- `id` (int): Unique identifier of the conversation (query parameter)

**Returns:** Conversation object, or error 404 if not found

### GET `/pedocontroller/conversations/findAll`
Retrieves all conversations.

**Parameters:** None

**Returns:** List of all Conversation objects

### POST `/pedocontroller/conversations/findBy`
Searches for conversations based on criteria.

**Parameters (all optional):**
- `id` (int): Unique identifier
- `baiter` (int): ID of the baiter
- `pedophile` (int): ID of the pedophile

**Returns:** List of matching Conversation objects

### POST `/pedocontroller/conversations/get`
Pagination of conversation results with filtering.

**Parameters:**
- Same parameters as `findBy`
- `numberPage` (int): Page number
- `numberResults` (int): Number of results per page

**Returns:** Paginated list of Conversation objects

## Message Endpoints

### POST `/pedocontroller/messages/create`
Creates a new message.

**Parameters:**
- `conversation` (int): ID of the associated conversation
- `message` (str): Content of the message
- `date` (datetime): Date of the message
- `sender_type` (str): Type of sender ('assistant', 'user', 'system')

**Returns:** Created Message object with status 201, or errors with status 400

### POST `/pedocontroller/messages/initFirstMessage`
Initializes the first system message in a conversation with baiter context.

**Parameters:**
- `idConversation` (int): ID of the conversation
- `idBaiter` (int): ID of the baiter

**Returns:** Created system Message object with baiter context

### POST `/pedocontroller/messages/create/ai`
Creates a message from the baiter (AI) and sends it via pedo-connector.

**Parameters:**
- `conversation` (int): ID of the associated conversation
- `message` (str): Content of the message
- `date` (datetime): Date of the message

**Returns:** Created Message object and sends the message via pedo-connector service

### POST `/pedocontroller/messages/create/pedophile`
Creates a message from the pedophile and forwards it to pedo-hunter-api for analysis.

**Parameters:**
- `conversation` (int): ID of the associated conversation
- `message` (str): Content of the message
- `date` (datetime): Date of the message

**Returns:** Created Message object and forwards to pedo-hunter-api for analysis

### PUT `/pedocontroller/messages/update`
Updates an existing message.

**Parameters:**
- `id` (int): Unique identifier of the message
- `conversation` (int): ID of the associated conversation
- `message` (str): Content of the message
- `date` (datetime): Date of the message

**Returns:** Updated Message object, or error 404 if not found

### DELETE `/pedocontroller/messages/delete`
Deletes a message.

**Parameters:**
- `id` (int): Unique identifier of the message (query parameter)

**Returns:** Status code 204 if successful, 404 if not found

### GET `/pedocontroller/messages/findOne`
Retrieves a specific message.

**Parameters:**
- `id` (int): Unique identifier of the message (query parameter)

**Returns:** Message object, or error 404 if not found

### GET `/pedocontroller/messages/findAll`
Retrieves all messages.

**Parameters:** None

**Returns:** List of all Message objects

### POST `/pedocontroller/messages/findBy`
Searches for messages based on criteria with optional ordering.

**Parameters (all optional):**
- `id` (int): Unique identifier
- `conversation` (int): ID of the conversation
- `date` (datetime): Date of the message
- `order_by` (str): Field to sort by (e.g., 'date')

**Returns:** List of matching Message objects (ordered if specified)

## Social Network Endpoints

### POST `/pedocontroller/socialnetworks/create`
Creates a new social network.

**Parameters:**
- `name` (str): Name of the social network
- `token` (str): Access token for the social network

**Returns:** Created SocialNetwork object with status 201, or errors with status 400

### PUT `/pedocontroller/socialnetworks/update`
Updates an existing social network.

**Parameters:**
- `id` (int): Unique identifier of the social network
- `name` (str): Name of the social network
- `token` (str): Access token for the social network

**Returns:** Updated SocialNetwork object, or error 404 if not found

### DELETE `/pedocontroller/socialnetworks/delete`
Deletes a social network.

**Parameters:**
- `id` (int): Unique identifier of the social network (query parameter)

**Returns:** Status code 204 if successful, 404 if not found

### GET `/pedocontroller/socialnetworks/findOne`
Retrieves a specific social network.

**Parameters:**
- `id` (int): Unique identifier of the social network (query parameter)

**Returns:** SocialNetwork object, or error 404 if not found

### GET `/pedocontroller/socialnetworks/findAll`
Retrieves all social networks.

**Parameters:** None

**Returns:** List of all SocialNetwork objects

### POST `/pedocontroller/socialnetworks/findBy`
Searches for social networks based on criteria.

**Parameters (all optional):**
- `id` (int): Unique identifier
- `name` (str): Name of the social network

**Returns:** List of matching SocialNetwork objects

## Database Configuration

The application uses PostgreSQL with the following configuration:
- **Database Name**: PedoStocker
- **Host**: 127.0.0.1
- **Port**: 5432
- **User**: user
- **Password**: password

## Allowed Hosts

The application accepts requests from the following hosts:
- pedo-stocker
- pedo-connector
- pedo-observer
- pedo-hunter-api
- pedo-meter-api
- pedo-controller
- localhost
- 127.0.0.1

## Notes

- All endpoints require appropriate HTTP methods as specified
- Date parameters should be in ISO format (e.g., '2023-06-10T12:00:00Z')
- The system automatically initializes conversations with a context message from the baiter
- AI messages are automatically forwarded to the pedo-connector service
- Pedophile messages trigger analysis via the pedo-hunter-api service
- All API responses follow REST conventions with appropriate HTTP status codes