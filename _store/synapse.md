---
aid: synapse
url: https://raw.githubusercontent.com/api-evangelist/synapse/refs/heads/main/apis.yml
apis:
- name: Synapse Client-Server API
  description: RESTful API for client applications to interact with the Matrix homeserver, enabling messaging, room management, user authentication, and real-time events.
  image: https://matrix.org/images/matrix-logo.svg
  humanURL: https://spec.matrix.org/latest/client-server-api/
  baseURL: https://matrix.example.com/_matrix/client
  tags:
  - Chat
  - Collaboration
  - Messaging
  - Real-Time
  properties:
  - type: Documentation
    url: https://spec.matrix.org/latest/client-server-api/
  - type: OpenAPI
    url: https://github.com/matrix-org/matrix-spec/tree/main/data/api/client-server
  contact:
  - FN: Matrix.org Team
    email: support@matrix.org
    url: https://matrix.org/support/
- name: Synapse Server-Server API
  description: Federation API allowing different Matrix homeservers to communicate with each other, enabling decentralized messaging across servers.
  image: https://matrix.org/images/matrix-logo.svg
  humanURL: https://spec.matrix.org/latest/server-server-api/
  baseURL: https://matrix.example.com/_matrix/federation
  tags:
  - Decentralized
  - Federation
  - Server-To-Server
  properties:
  - type: Documentation
    url: https://spec.matrix.org/latest/server-server-api/
  - type: OpenAPI
    url: https://github.com/matrix-org/matrix-spec/tree/main/data/api/server-server
- name: Synapse Admin API
  description: Administrative API for managing the Synapse homeserver, including user management, room administration, server configuration, and monitoring.
  image: https://matrix.org/images/matrix-logo.svg
  humanURL: https://matrix-org.github.io/synapse/latest/usage/administration/admin_api/
  baseURL: https://matrix.example.com/_synapse/admin
  tags:
  - Administration
  - Management
  - Monitoring
  properties:
  - type: Documentation
    url: https://matrix-org.github.io/synapse/latest/usage/administration/admin_api/
  - type: GitHub
    url: https://github.com/matrix-org/synapse/tree/develop/docs/admin_api
- name: Synapse Application Service API
  description: API for integrating application services (bridges and bots) with the Matrix homeserver.
  image: https://matrix.org/images/matrix-logo.svg
  humanURL: https://spec.matrix.org/latest/application-service-api/
  baseURL: https://matrix.example.com/_matrix/app
  tags:
  - Application-Services
  - Bots
  - Bridges
  - Integration
  properties:
  - type: Documentation
    url: https://spec.matrix.org/latest/application-service-api/
name: Synapse
tags:
- Chat
- Collaboration
- Decentralized
- Federation
- Matrix
- Messaging
- Open-Source
- Real-Time
type: Contract
image: https://matrix.org/images/matrix-logo.svg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: An open-source Matrix homeserver implementation that provides decentralized, secure communication services including real-time messaging, voice/video calls, and collaboration features.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

