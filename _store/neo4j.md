---
aid: neo4j
name: Neo4j
description: Neo4j is the leading graph database platform, enabling developers to build applications powered by connected data. Their developer platform provides HTTP, Query, and Aura cloud APIs alongside official drivers for Python, Java, and JavaScript, as well as a GraphQL library for rapid API development backed by the Neo4j graph database.
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Graph Database
  - Cypher
  - Cloud
  - GraphQL
  - Drivers
  - APIs
url: https://raw.githubusercontent.com/api-evangelist/neo4j/refs/heads/main/apis.yml
created: '2025-03-05'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: neo4j:http-api
    name: Neo4j HTTP API
    description: The Neo4j HTTP API allows developers to execute Cypher queries against a Neo4j database through HTTP requests. It supports both implicit transactions, where the API handles transaction management automatically, and explicit transactions, where developers control the full transaction lifecycle including open, commit, and rollback operations. By default the API uses port 7474 for HTTP and port 7473 for HTTPS on self-managed instances.
    humanURL: https://neo4j.com/docs/http-api/current/
    tags:
      - Graph Database
      - Cypher
      - HTTP
      - Transactions
      - Database
    properties:
      - type: Documentation
        url: https://neo4j.com/docs/http-api/current/
      - type: OpenAPI
        url: openapi/neo4j-http-api-openapi.yml
  - aid: neo4j:query-api
    name: Neo4j Query API
    description: The Neo4j Query API enables the execution of Cypher statements against a Neo4j server through HTTP requests. It provides a streamlined interface for running graph database queries, supporting both self-managed and cloud-hosted Neo4j instances. The Query API is designed for applications that need to interact with Neo4j programmatically and is particularly useful for languages where a dedicated Neo4j driver is not available.
    humanURL: https://neo4j.com/docs/query-api/current/
    tags:
      - Graph Database
      - Cypher
      - Query
      - HTTP
      - Database
    properties:
      - type: Documentation
        url: https://neo4j.com/docs/query-api/current/
      - type: OpenAPI
        url: openapi/neo4j-query-api-openapi.yml
  - aid: neo4j:aura-api
    name: Neo4j Aura API
    description: 'The Neo4j Aura API provides programmatic access to manage Neo4j AuraDB cloud database instances. It supports operations across three primary resources: instances, tenants, and snapshots. Developers authenticate using OAuth2 bearer tokens obtained through client credentials, and can automate the provisioning, configuration, and management of their cloud-hosted Neo4j graph databases. The API is accessible through the console.neo4j.io platform.'
    humanURL: https://neo4j.com/docs/aura/platform/api/specification/
    tags:
      - Cloud
      - Graph Database
      - Database Management
      - Instances
      - Snapshots
    properties:
      - type: Documentation
        url: https://neo4j.com/docs/aura/platform/api/specification/
      - type: OpenAPI
        url: openapi/neo4j-aura-api-openapi.yml
  - aid: neo4j:graphql-library
    name: Neo4j GraphQL Library
    description: The Neo4j GraphQL Library is an open source JavaScript library that enables rapid development of GraphQL APIs backed by a Neo4j graph database. It automatically generates a single optimized Cypher query for each GraphQL query or mutation, eliminating the N+1 problem common in GraphQL implementations. The library supports schema-first development and integrates with Neo4j AuraDB for cloud-hosted deployments, making it suitable for cross-platform and mobile applications.
    humanURL: https://neo4j.com/docs/graphql/current/
    tags:
      - GraphQL
      - Graph Database
      - JavaScript
      - Low-Code
      - API Development
    properties:
      - type: Documentation
        url: https://neo4j.com/docs/graphql/current/
  - aid: neo4j:bolt-protocol
    name: Neo4j Bolt Protocol
    description: The Neo4j Bolt Protocol is a binary application protocol designed for efficient execution of database queries using the Cypher query language. It operates over TCP or WebSocket connections on the default port 7687 and serves as the foundation for all official Neo4j drivers including Java, Python, JavaScript, .NET, and Go. The protocol supports both direct connections via the bolt:// scheme and routing connections via bolt+routing:// for clustered deployments.
    humanURL: https://neo4j.com/docs/bolt/current/bolt/
    tags:
      - Binary Protocol
      - Graph Database
      - Drivers
      - Connectivity
      - Networking
    properties:
      - type: Documentation
        url: https://neo4j.com/docs/bolt/current/bolt/
  - aid: neo4j:python-driver
    name: Neo4j Python Driver
    description: The Neo4j Python Driver is the official library for interacting with Neo4j graph databases from Python applications. It communicates using the Bolt protocol and supports both single instance and clustered database deployments. The driver is available on PyPI as the neo4j package and provides a comprehensive API for session management, transaction handling, and result processing.
    humanURL: https://neo4j.com/docs/python-manual/current/
    tags:
      - Python
      - SDK
      - Driver
      - Graph Database
      - Bolt
    properties:
      - type: Documentation
        url: https://neo4j.com/docs/python-manual/current/
      - type: Documentation
        url: https://neo4j.com/docs/api/python-driver/current/
  - aid: neo4j:java-driver
    name: Neo4j Java Driver
    description: The Neo4j Java Driver is the official library for connecting Java applications to Neo4j graph databases. Distributed via Maven, it uses the Bolt protocol for network communication and supports both single instance and clustered database configurations. The driver provides a full API for managing connections, sessions, transactions, and query results within Java applications.
    humanURL: https://neo4j.com/docs/java-manual/current/
    tags:
      - Java
      - SDK
      - Driver
      - Graph Database
      - Bolt
    properties:
      - type: Documentation
        url: https://neo4j.com/docs/java-manual/current/
      - type: Documentation
        url: https://neo4j.com/docs/api/java-driver/current/
  - aid: neo4j:javascript-driver
    name: Neo4j JavaScript Driver
    description: The Neo4j JavaScript Driver is the official library for interacting with Neo4j graph databases from JavaScript and Node.js applications. It uses the Bolt protocol for efficient communication and can be installed via npm. The driver supports both browser and server-side environments and provides APIs for session management, transaction control, and processing of query results from Neo4j databases.
    humanURL: https://neo4j.com/docs/javascript-manual/current/
    tags:
      - JavaScript
      - SDK
      - Driver
      - Graph Database
      - Bolt
      - Node.js
    properties:
      - type: Documentation
        url: https://neo4j.com/docs/javascript-manual/current/
      - type: Documentation
        url: https://neo4j.com/docs/api/javascript-driver/current/
common:
  - type: Portal
    url: https://neo4j.com/developer/
  - type: Documentation
    url: https://neo4j.com/docs/
  - type: Website
    url: https://neo4j.com
  - type: PrivacyPolicy
    url: https://neo4j.com/privacy-policy/
  - type: TermsOfService
    url: https://neo4j.com/terms/
  - type: Support
    url: https://support.neo4j.com/
  - type: Blog
    url: https://neo4j.com/blog/
  - type: Login
    url: https://console.neo4j.io/
maintainers:
  - FN: API Evangelist
    email: info@apievangelist.com
---
