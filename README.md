# PedoController API Documentation

This document provides a comprehensive listing of all API endpoints in the PedoController system, along with their required parameters and return values.

## Table of Contents
- [Subject Profiles](#subject-profiles)
- [Decoy Profiles](#decoy-profiles)
- [Conversation Management](#conversation-management)
- [Messaging System](#messaging-system)
- [Platform Integration](#platform-integration)
- [Authentication](#authentication)
- [System Status](#system-status)
- [Analytics](#analytics)

## Subject Profiles

### POST `/pedocontroller/pedophiles/create`
Creates a new subject profile in the database.

**Parameters:**
- `nickname` (str): Pseudonym of the subject
- `socialNetwork` (int): ID of the associated social network
- `score` (int, optional): Risk assessment score
- `user_socialNetwork_id` (str, optional): User ID on the social network

**Returns:** Created profile object with status 201, or errors with status 400

### PUT `/pedocontroller/pedophiles/update`
Updates an existing subject profile.

**Parameters:**
- `id` (int): Unique identifier of the profile
- `nickname` (str): Pseudonym of the subject
- `socialNetwork` (int): ID of the associated social network
- `score` (int): Risk assessment score
- `user_socialNetwork_id` (str, optional): User ID on the social network

**Returns:** Updated profile object, or error 404 if not found

### DELETE `/pedocontroller/pedophiles/delete`
Deletes a subject profile.

**Parameters:**
- `id` (int): Unique identifier of the profile (query parameter)

**Returns:** Status code 204 if successful, 404 if not found

### GET `/pedocontroller/pedophiles/findOne`
Retrieves a specific subject profile.

**Parameters:**
- `id` (int): Unique identifier of the profile (query parameter)

**Returns:** Profile object, or error 404 if not found

### GET `/pedocontroller/pedophiles/findAll`
Retrieves all subject profiles.

**Parameters:** None

**Returns:** List of all profile objects

### POST `/pedocontroller/pedophiles/findBy`
Searches for subject profiles based on criteria.

**Parameters (all optional):**
- `id` (int): Unique identifier
- `nickname` (str): Pseudonym
- `score` (int): Exact score
- `score_min` (int): Minimum score
- `score_max` (int): Maximum score
- `score_range` (str): Score range in format "min,max"
- `socialNetwork` (int): ID of the social network

**Returns:** List of matching profile objects

### POST `/pedocontroller/pedophiles/get`
Pagination of subject profile results.

**Parameters:**
- `id` (int): Unique identifier
- `nickname` (str): Pseudonym
- `score` (int): Exact score
- `score_min` (int): Minimum score
- `score_max` (int): Maximum score
- `score_range` (str): Score range in format "min,max"
- `socialNetwork` (int): ID of the social network
- `numberPage` (int): Page number
- `numberResults` (int): Number of results per page
- `numberResults` (int): Number of results per page

**Returns:** Paginated list of profile objects

## Decoy Profiles

### POST `/pedocontroller/baiters/create`
Creates a new decoy profile.

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
- `context` (str, optional): Decoy context

**Returns:** Created decoy object with status 201, or errors with status 400

### PUT `/pedocontroller/baiters/update`
Updates an existing decoy profile.

**Parameters:**
- `id` (int): Unique identifier of the decoy
- `socialNetwork` (int): ID of the associated social network
- `username` (str): Username
- `fullName` (str): Full name
- `email` (str): Email
- `password` (str): Password
- `bio` (str): Biography
- `location` (str): Location
- `gender` (str): Gender ('boy' or 'girl')
- `birthDate` (datetime): Date of birth
- `context` (str, optional): Decoy context

**Returns:** Updated decoy object, or error 404 if not found

### DELETE `/pedocontroller/baiters/delete`
Deletes a decoy profile.

**Parameters:**
- `id` (int): Unique identifier of the decoy (query parameter)

**Returns:** Status code 204 if successful, 404 if not found

### GET `/pedocontroller/baiters/findOne`
Retrieves a specific decoy profile.

**Parameters:**
- `id` (int): Unique identifier of the decoy (query parameter)

**Returns:** Decoy object, or error 404 if not found

### GET `/pedocontroller/baiters/findAll`
Retrieves all decoy profiles.

**Parameters:** None

**Returns:** List of all decoy objects

### POST `/pedocontroller/baiters/findBy`
Searches for decoy profiles based on criteria.

**Parameters (all optional):**
- `id` (int): Unique identifier
- `username` (str): Username
- `email` (str): Email
- `location` (str): Location
- `gender` (str): Gender

**Returns:** List of matching decoy objects

## Conversation Management

### POST `/pedocontroller/conversations/create`
Creates a new conversation.

**Parameters:**
- `baiter` (int): ID of the associated decoy
- `pedophile` (int): ID of the associated subject
- `socialNetwork` (int): ID of the social network

**Returns:** Created conversation object with status 201, or errors with status 400

### PUT `/pedocontroller/conversations/update`
Updates an existing conversation.

**Parameters:**
- `id` (int): Unique identifier of the conversation
- `baiter` (int): ID of the associated decoy
- `pedophile` (int): ID of the associated subject
- `socialNetwork` (int): ID of the social network

**Returns:** Updated conversation object, or error 404 if not found

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

**Returns:** List of all conversation objects

### POST `/pedocontroller/conversations/findBy`
Searches for conversations based on criteria.

**Parameters (all optional):**
- `id` (int): Unique identifier
- `baiter` (int): ID of the decoy
- `pedophile` (int): ID of the subject

**Returns:** List of matching conversation objects

## Messaging System

### POST `/pedocontroller/messages/create`
Creates a new message.

**Parameters:**
- `conversation` (int): ID of the associated conversation
- `message` (str): Content of the message
- `date` (datetime): Date of the message
- `sender_type` (str): Type of sender ('assistant', 'user', 'system')

**Returns:** Created message object with status 201, or errors with status 400

### POST `/pedocontroller/messages/create/ai`
Creates a message from the decoy (AI).

**Parameters:**
- `conversation` (int): ID of the associated conversation
- `message` (str): Content of the message
- `date` (datetime): Date of the message

**Returns:** Created message object and sends the message via pedo-connector

### POST `/pedocontroller/messages/create/pedophile`
Creates a message from the subject.

**Parameters:**
- `conversation` (int): ID of the associated conversation
- `message` (str): Content of the message
- `date` (datetime): Date of the message

**Returns:** Created message object and forwards to pedo-hunter-api for analysis

### PUT `/pedocontroller/messages/update`
Updates an existing message.

**Parameters:**
- `id` (int): Unique identifier of the message
- `conversation` (int): ID of the associated conversation
- `message` (str): Content of the message
- `date` (datetime): Date of the message

**Returns:** Updated message object, or error 404 if not found

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

**Returns:** List of all message objects

### POST `/pedocontroller/messages/findBy`
Searches for messages based on criteria.

**Parameters (all optional):**
- `id` (int): Unique identifier
- `conversation` (int): ID of the conversation
- `date` (datetime): Date of the message
- `order_by` (str): Field to sort by

**Returns:** List of matching message objects

### POST `/pedocontroller/messages/initFirstMessage`
Initializes the first message in a conversation.

**Parameters:**
- `idConversation` (int): ID of the conversation
- `idBaiter` (int): ID of the decoy

**Returns:** Created system message object with decoy context

## Platform Integration

### POST `/pedocontroller/socialnetworks/create`
Creates a new social network.

**Parameters:**
- `name` (str): Name of the social network
- `token` (str): Access token for the social network

**Returns:** Created social network object with status 201, or errors with status 400

### PUT `/pedocontroller/socialnetworks/update`
Updates an existing social network.

**Parameters:**
- `id` (int): Unique identifier of the social network
- `name` (str): Name of the social network
- `token` (str): Access token for the social network

**Returns:** Updated social network object, or error 404 if not found

### DELETE `/pedocontroller/socialnetworks/delete`
Deletes a social network.

**Parameters:**
- `id` (int): Unique identifier of the social network (query parameter)

**Returns:** Status code 204 if successful, 404 if not found

### GET `/pedocontroller/socialnetworks/findOne`
Retrieves a specific social network.

**Parameters:**
- `id` (int): Unique identifier of the social network (query parameter)

**Returns:** Social network object, or error 404 if not found

### GET `/pedocontroller/socialnetworks/findAll`
Retrieves all social networks.

**Parameters:** None

**Returns:** List of all social network objects

### POST `/pedocontroller/socialnetworks/findBy`
Searches for social networks based on criteria.

**Parameters (all optional):**
- `id` (int): Unique identifier
- `name` (str): Name of the social network

**Returns:** List of matching social network objects

## Authentication

### POST `/pedocontroller/auth/login`
Authenticates a user and provides an access token.

**Parameters:**
- `username` (str): Username
- `password` (str): Password

**Returns:** JWT token and user information with status 200, or error with status 401

### POST `/pedocontroller/auth/refresh`
Refreshes an existing authentication token.

**Parameters:**
- `refresh_token` (str): Refresh token from previous login

**Returns:** New JWT token with status 200, or error with status 401

### POST `/pedocontroller/auth/logout`
Invalidates the current authentication token.

**Parameters:**
- Authorization header with token

**Returns:** Success message with status 200

## System Status

### GET `/pedocontroller/status`
Checks the overall system status.

**Parameters:** None

**Returns:** System health information with component statuses

### GET `/pedocontroller/status/db`
Checks the database connection status.

**Parameters:** None

**Returns:** Database connection information and status

### GET `/pedocontroller/status/ai`
Checks the AI system status.

**Parameters:** None

**Returns:** AI system status and available models

## Analytics

### GET `/pedocontroller/analytics/conversations`
Retrieves analytics about conversations.

**Parameters (all optional):**
- `start_date` (datetime): Start date for the analysis
- `end_date` (datetime): End date for the analysis
- `socialNetwork` (int): ID of the social network

**Returns:** Conversation metrics and statistics

### GET `/pedocontroller/analytics/subjects`
Retrieves analytics about subject profiles.

**Parameters (all optional):**
- `start_date` (datetime): Start date for the analysis
- `end_date` (datetime): End date for the analysis

**Returns:** Subject profile metrics and risk distribution

### GET `/pedocontroller/analytics/messages`
Retrieves analytics about message content and patterns.

**Parameters (all optional):**
- `start_date` (datetime): Start date for the analysis
- `end_date` (datetime): End date for the analysis
- `conversation` (int): ID of a specific conversation

**Returns:** Message frequency, patterns, and content analysis