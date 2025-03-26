### OIDC is used for authentication or authorization?

OpenID Connect (OIDC) is primarily used for authentication. It allows applications to verify the identity of a user based on the authentication performed by an identity provider (like Google). OIDC provides user profile information (like name and email) through tokens, such as ID tokens, to establish "who" the user is.
While OIDC focuses on authentication, it can also work alongside OAuth 2.0 for authorization. OAuth 2.0 is used to grant applications permission to access specific resources on behalf of the user (like accessing Google Drive files).

In short:
OIDC: Authentication (Who the user is).
OAuth 2.0: Authorization (What the user is allowed to do).