---
aid: symphony
url: https://raw.githubusercontent.com/api-evangelist/symphony/refs/heads/main/apis.yml
name: Symphony
description: Symphony is a secure collaboration platform designed for professional teams, particularly in financial services. It provides end-to-end encrypted messaging, voice, video, and workflows for regulated industries. Symphony's developer platform enables bot automation, workflow integrations, and extension apps through a suite of REST APIs including the Pod API, Agent API, Authenticator API, Login API, Profile Manager API, and Community Connect API.
image: https://symphony.com/favicon.ico
tags:
  - Collaboration
  - Communication
  - Financial Services
  - Messaging
  - Secure Communication
created: '2026-05-03'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: symphony:symphony-pod-api
    name: Symphony Pod API
    description: The Symphony Pod API provides core platform services including user management, stream (room) management, content export, connection management, security certificates, and presence. Used to build tools that manage and administer Symphony for an organization.
    humanURL: https://developers.symphony.com/
    baseURL: https://acme.symphony.com
    tags:
      - Certificates
      - Connections
      - Messaging
      - Presence
      - Rooms
      - Streams
      - User Management
      - Users
    properties:
      - type: Documentation
        url: https://docs.developers.symphony.com/bots/overview-of-rest-api
      - type: OpenAPI
        url: openapi/symphony-pod-api-openapi.yml
  - aid: symphony:symphony-agent-api
    name: Symphony Agent API
    description: The Symphony Agent API handles encryption and decryption of messages and content sent to and from bots. Provides message sending, datafeed (real-time event stream), signal management, DLP (Data Loss Prevention), and content sharing operations. Requires the on-premise Agent server to be deployed.
    humanURL: https://docs.developers.symphony.com/bots/overview-of-rest-api/agent-api
    baseURL: https://acme.symphony.com
    tags:
      - Attachment
      - Bots
      - Data Loss Prevention
      - Datafeed
      - Encryption
      - Messaging
      - Real-Time
      - Signals
      - Streams
    properties:
      - type: Documentation
        url: https://docs.developers.symphony.com/bots/overview-of-rest-api/agent-api
      - type: OpenAPI
        url: openapi/agent-openapi-original.yml
  - aid: symphony:symphony-authenticator-api
    name: Symphony Authenticator API
    description: The Symphony Authenticator API enables bots and on-premise processes to authenticate via mutual TLS certificate. Returns session tokens required for all subsequent API calls. Runs on both the Pod and the Key Manager, and both tokens are needed for full authentication.
    humanURL: https://docs.developers.symphony.com/bots/authentication
    baseURL: https://acme.symphony.com
    tags:
      - Authentication
      - Bots
      - Certificates
      - Session
      - TLS
    properties:
      - type: Documentation
        url: https://docs.developers.symphony.com/bots/authentication
      - type: OpenAPI
        url: openapi/authenticator-openapi-original.yml
  - aid: symphony:symphony-login-api
    name: Symphony Login API
    description: The Symphony Login API enables bots and applications to authenticate using RSA public/private key pairs, producing session tokens and OAuth2-compatible JWT access tokens. Supports bot authentication, extension app authentication, and delegated user context authentication.
    humanURL: https://docs.developers.symphony.com/bots/authentication/rsa-authentication
    baseURL: https://acme.symphony.com
    tags:
      - Authentication
      - Bots
      - JWT
      - OAuth2
      - Public Key
      - RSA
      - Session
    properties:
      - type: Documentation
        url: https://docs.developers.symphony.com/bots/authentication/rsa-authentication
      - type: OpenAPI
        url: openapi/login-openapi-original.yml
  - aid: symphony:symphony-profile-manager-api
    name: Symphony Profile Manager API
    description: Profile Manager is a microservice to manage user profiles and groups in Symphony. Supports group creation, membership management, and profile retrieval for enterprise directory use cases.
    humanURL: https://developers.symphony.com/
    baseURL: https://acme.symphony.com/profile-manager
    tags:
      - Directory
      - Groups
      - Profiles
      - User Management
      - Users
    properties:
      - type: Documentation
        url: https://developers.symphony.com/
      - type: OpenAPI
        url: openapi/profile-manager-openapi-original.yml
  - aid: symphony:symphony-community-connect-api
    name: Symphony Community Connect API
    description: The Symphony Community Connect API enables cross-company secure messaging and collaboration. Provides onboarding and tenant lookup for users joining Symphony Community Connect (formerly known as Channel Connect), enabling organizations to communicate with external partners over encrypted Symphony channels.
    humanURL: https://docs.developers.symphony.com/symphony-rest-api/connect-api
    baseURL: https://acme.symphony.com
    tags:
      - Collaboration
      - Community
      - Onboarding
      - Tenants
      - Users
    properties:
      - type: Documentation
        url: https://docs.developers.symphony.com/symphony-rest-api/connect-api
      - type: OpenAPI
        url: openapi/community-connect-openapi-original.yml
common:
  - type: Website
    url: https://symphony.com
  - type: Developer Documentation
    url: https://docs.developers.symphony.com
  - type: API Reference
    url: https://rest-api.symphony.com
  - type: Developer Center
    url: https://symphony.com/support/developers/
  - type: GitHub
    url: https://github.com/finos/symphony-api-spec
  - type: GitHub Organization
    url: https://github.com/SymphonyPlatformSolutions
  - type: Authentication
    url: https://docs.developers.symphony.com/bots/authentication
  - type: Sandbox
    url: https://developers.symphony.com/
  - type: Developer Certification
    url: https://developers.symphony.com/
  - type: SDK
    url: https://docs.developers.symphony.com/developer-tools/developer-tools/bdk-2.0
  - type: Changelog
    url: https://docs.developers.symphony.com/admin-guide/release-notes
maintainers:
  - FN: API Evangelist
    email: info@apievangelist.com
---
