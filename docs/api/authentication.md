# API Authentication

CherryBomb provides secure authentication mechanisms to protect your data and ensure that only authorized users can access the API.

## Authentication Methods

CherryBomb supports multiple authentication methods:

1. **JWT (JSON Web Token)** - Primary authentication method
2. **API Keys** - For programmatic access
3. **OAuth 2.0** - For third-party integrations

## JWT Authentication

### Obtaining a JWT Token

```text
POST /api/auth/login
```

**Request Body:**

```json
{
  "email": "user@example.com",
  "password": "yourSecurePassword"
}
```

**Response:**

```json
{
  "success": true,
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refreshToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "expiresIn": 3600,
  "user": {
    "id": "usr_123456789",
    "email": "user@example.com",
    "username": "username",
    "role": "user"
  }
}
```

### Using JWT Authentication

Include the token in the `Authorization` header of your requests:

```text
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

### Refreshing a Token

```text
POST /api/auth/refresh
```

**Request Body:**

```json
{
  "refreshToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

**Response:**

```json
{
  "success": true,
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refreshToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "expiresIn": 3600
}
```

## API Key Authentication

### Creating an API Key

```text
POST /api/auth/api-keys
```

**Request Headers:**

```text
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Request Body:**

```json
{
  "name": "My Application",
  "permissions": ["read:datasets", "read:insights"],
  "expiry": "2026-05-15T00:00:00Z"  // Optional
}
```

**Response:**

```json
{
  "success": true,
  "apiKey": {
    "id": "key_123456789",
    "key": "cb_sk_123456789abcdefghijklmnopqrstuvwxyz",
    "name": "My Application",
    "permissions": ["read:datasets", "read:insights"],
    "createdAt": "2025-05-15T10:30:00Z",
    "expiresAt": "2026-05-15T00:00:00Z"
  }
}
```

### Using API Key Authentication

Include the API key in the `X-API-Key` header of your requests:

```text
X-API-Key: cb_sk_123456789abcdefghijklmnopqrstuvwxyz
```

### Listing API Keys

```text
GET /api/auth/api-keys
```

**Request Headers:**

```text
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Response:**

```json
{
  "success": true,
  "apiKeys": [
    {
      "id": "key_123456789",
      "name": "My Application",
      "permissions": ["read:datasets", "read:insights"],
      "createdAt": "2025-05-15T10:30:00Z",
      "expiresAt": "2026-05-15T00:00:00Z",
      "lastUsed": "2025-05-15T10:45:00Z"
    }
  ]
}
```

### Revoking an API Key

```text
DELETE /api/auth/api-keys/{key_id}
```

**Request Headers:**

```text
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Response:**

```json
{
  "success": true,
  "message": "API key revoked successfully"
}
```

## OAuth 2.0 Integration

### Initiating OAuth Flow

```text
GET /api/auth/oauth/{provider}
```

Where `{provider}` can be:

- `google`
- `facebook`
- `twitter`

**Query Parameters:**

```text
redirect_uri=https://your-app.com/callback
state=randomStateString
```

### OAuth Callback Handler

```text
GET /api/auth/oauth/{provider}/callback
```

**Query Parameters:**

```text
code=authorizationCode
state=randomStateString
```

**Response:**

```json
{
  "success": true,
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refreshToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "expiresIn": 3600,
  "user": {
    "id": "usr_123456789",
    "email": "user@example.com",
    "username": "username",
    "role": "user"
  }
}
```

## Error Responses

### Authentication Errors

**Invalid Credentials:**

```json
{
  "success": false,
  "error": {
    "code": "auth/invalid-credentials",
    "message": "Invalid email or password"
  }
}
```

**Expired Token:**

```json
{
  "success": false,
  "error": {
    "code": "auth/token-expired",
    "message": "Token has expired"
  }
}
```

**Invalid Token:**

```json
{
  "success": false,
  "error": {
    "code": "auth/invalid-token",
    "message": "Token is invalid"
  }
}
```

**Insufficient Permissions:**

```json
{
  "success": false,
  "error": {
    "code": "auth/insufficient-permissions",
    "message": "You do not have permission to access this resource"
  }
}
```

## Best Practices

1. **Store Tokens Securely**: Never store tokens in local storage or cookies without proper security measures
2. **Set Short Expiry Times**: Use short-lived access tokens with refresh tokens
3. **Use HTTPS**: Always use HTTPS when transmitting authentication details
4. **Implement Rate Limiting**: Protect against brute force attacks by implementing rate limiting
5. **Limit API Key Permissions**: Only grant the minimum permissions needed for your use case
