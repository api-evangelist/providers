---
aid: synapse
name: Synapse
description: Synapse is the reference Matrix homeserver implementation maintained by Element (formerly by the Matrix.org Foundation). Written in Python and Rust, it implements the Matrix open standard for secure, decentralized real-time communication. Synapse powers thousands of deployments worldwide and provides Client-Server, Server-Server (federation), Application Service, Identity Service, and Admin APIs. Since version 1.99, maintained by Element under AGPL-3.0.
image: https://matrix.org/images/matrix-logo.svg
url: https://raw.githubusercontent.com/api-evangelist/synapse/refs/heads/main/apis.yml
created: '2026-05-03'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: synapse:synapse-client-server-api
    name: Synapse Client-Server API
    description: RESTful API for Matrix client applications to interact with the homeserver, enabling real-time messaging, room management, user authentication, event synchronization, and media uploads. Follows the Matrix Client-Server specification.
    image: https://matrix.org/images/matrix-logo.svg
    humanURL: https://spec.matrix.org/latest/client-server-api/
    baseURL: https://matrix.example.com/_matrix/client
    tags:
      - Chat
      - Client
      - Collaboration
      - Matrix
      - Messaging
      - Real-Time
      - Rooms
    properties:
      - type: Documentation
        url: https://spec.matrix.org/latest/client-server-api/
      - type: OpenAPI
        url: https://github.com/matrix-org/matrix-spec/tree/main/data/api/client-server
  - aid: synapse:synapse-server-server-api
    name: Synapse Server-Server API
    description: Federation API enabling different Matrix homeservers to communicate with each other, supporting decentralized messaging, event exchange, and room state synchronization across server boundaries.
    image: https://matrix.org/images/matrix-logo.svg
    humanURL: https://spec.matrix.org/latest/server-server-api/
    baseURL: https://matrix.example.com/_matrix/federation
    tags:
      - Decentralized
      - Federation
      - Matrix
      - Server-To-Server
    properties:
      - type: Documentation
        url: https://spec.matrix.org/latest/server-server-api/
      - type: OpenAPI
        url: https://github.com/matrix-org/matrix-spec/tree/main/data/api/server-server
  - aid: synapse:synapse-admin-api
    name: Synapse Admin API
    description: Administrative REST API for managing the Synapse homeserver. Provides server administrators with endpoints for user management, room administration, media management, federation control, registration tokens, background updates, event reports, and server statistics.
    image: https://matrix.org/images/matrix-logo.svg
    humanURL: https://matrix-org.github.io/synapse/latest/usage/administration/admin_api/
    baseURL: https://matrix.example.com/_synapse/admin
    tags:
      - Administration
      - Management
      - Matrix
      - Monitoring
      - Users
    properties:
      - type: Documentation
        url: https://matrix-org.github.io/synapse/latest/usage/administration/admin_api/
      - type: OpenAPI
        url: openapi/synapse-admin-api-openapi.yml
      - type: GitHub
        url: https://github.com/matrix-org/synapse/tree/develop/docs/admin_api
  - aid: synapse:synapse-application-service-api
    name: Synapse Application Service API
    description: API for integrating application services (bridges and bots) with the Matrix homeserver. Allows third-party applications to handle namespaced user IDs and room aliases, enabling Matrix bridges for IRC, Slack, Telegram, and other platforms.
    image: https://matrix.org/images/matrix-logo.svg
    humanURL: https://spec.matrix.org/latest/application-service-api/
    baseURL: https://matrix.example.com/_matrix/app
    tags:
      - Application-Services
      - Bots
      - Bridges
      - Integration
      - Matrix
    properties:
      - type: Documentation
        url: https://spec.matrix.org/latest/application-service-api/
common:
  - type: GitHub
    url: https://github.com/matrix-org/synapse
  - type: GitHub
    url: https://github.com/element-hq/synapse
  - type: Documentation
    url: https://matrix-org.github.io/synapse/latest/
  - type: Getting Started
    url: https://matrix-org.github.io/synapse/latest/setup/installation.html
  - type: Authentication
    url: https://matrix-org.github.io/synapse/latest/usage/configuration/config_documentation.html#authentication
  - type: Rate Limits
    url: https://matrix-org.github.io/synapse/latest/usage/configuration/config_documentation.html#ratelimiting
  - type: Changelog
    url: https://github.com/matrix-org/synapse/blob/develop/CHANGES.md
  - type: License
    url: https://github.com/matrix-org/synapse/blob/develop/LICENSE
  - type: Docker
    url: https://hub.docker.com/r/matrixdotorg/synapse
  - type: PyPI
    url: https://pypi.org/project/matrix-synapse/
  - type: Matrix Spec
    url: https://spec.matrix.org/latest/
maintainers:
  - FN: API Evangelist
    email: info@apievangelist.com
tags:
  - Chat
  - Collaboration
  - Decentralized
  - Federation
  - Matrix
  - Messaging
  - Open-Source
  - Real-Time
---
