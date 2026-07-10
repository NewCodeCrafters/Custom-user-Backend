# Why Swagger Shows `401 Unauthorized`

This error:

```json
{
  "detail": "Authentication credentials were not provided."
}
```

does not mean your access token is missing from the login response. It means the protected endpoint did not receive the token in the format SimpleJWT expects.

## What Happened

Swagger was sending the header like this:

```http
Authorization: eyJhbGciOiJIUzI1Ni...
```

But Django REST Framework SimpleJWT expects this:

```http
Authorization: Bearer eyJhbGciOiJIUzI1Ni...
```

The word `Bearer` and the space after it are required.

## Is This a Code Problem?

Your user endpoints are not the main problem.

These protected views are correct when they use:

```python
permission_classes = [IsAuthenticated]
```

and your settings are correct when they use:

```python
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
}
```

The problem happened because Swagger's `apiKey` authorization sends exactly what you type into the Authorize box.

So if you type only the token, Swagger sends only the token.

## Correct Swagger Format

In Swagger, click **Authorize** and enter:

```text
Bearer your_access_token_here
```

Do not enter only:

```text
your_access_token_here
```

## Correct Postman Format

In Postman, choose:

```text
Authorization tab -> Type: Bearer Token
```

Then paste only the access token. Postman adds `Bearer` automatically.

## Summary

The 401 happened because Swagger sent:

```http
Authorization: <token>
```

instead of:

```http
Authorization: Bearer <token>
```

So this was a Swagger header-format issue, not a problem with your access token itself.
