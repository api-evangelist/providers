---
aid: ocelot
name: Ocelot
description: Ocelot is an open-source API Gateway built with .NET for microservices architectures. It provides routing, authentication, rate limiting, load balancing, and service discovery features for managing and securing APIs in .NET ecosystems.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - .NET
  - API Gateway
  - Microservices
  - Open Source
url: https://raw.githubusercontent.com/api-evangelist/ocelot/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: ocelot:ocelot-gateway
    name: Ocelot API Gateway
    description: Ocelot is an open-source .NET API Gateway that provides routing, authentication, authorization, rate limiting, load balancing, caching, and service discovery for microservices architectures. It is configured via JSON files and integrates with ASP.NET Core middleware pipelines.
    humanURL: https://ocelot.readthedocs.io/en/latest/
    baseURL: https://ocelot.readthedocs.io/
    tags:
      - .NET
      - API Gateway
      - Microservices
      - Routing
    properties:
      - type: Documentation
        url: https://ocelot.readthedocs.io/en/latest/
      - type: Getting Started
        url: https://ocelot.readthedocs.io/en/latest/introduction/gettingstarted.html
      - type: Reference
        url: https://ocelot.readthedocs.io/en/latest/features/configuration.html
      - type: Authentication
        url: https://ocelot.readthedocs.io/en/latest/features/authentication.html
      - type: GitHubRepository
        url: https://github.com/ThreeMammals/Ocelot
  - aid: ocelot:ocelot-administration-api
    name: Ocelot Administration API
    description: The Ocelot Administration API allows runtime changes to gateway configuration via an authenticated HTTP API. It supports updating routes and clearing cache regions without restarting the gateway, and is authenticated using Bearer tokens issued by Ocelot's built-in IdentityServer or an external identity provider.
    humanURL: https://ocelot.readthedocs.io/en/latest/features/administration.html
    baseURL: https://ocelot.readthedocs.io/
    tags:
      - .NET
      - Administration
      - Configuration
      - Management
    properties:
      - type: Documentation
        url: https://ocelot.readthedocs.io/en/latest/features/administration.html
      - type: Authentication
        url: https://ocelot.readthedocs.io/en/latest/features/authentication.html
      - type: GitHubRepository
        url: https://github.com/ThreeMammals/Ocelot
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/ocelot/refs/heads/main/openapi/ocelot-administration-openapi.yml
common:
  - type: Website
    url: https://ocelot.readthedocs.io/
  - type: Documentation
    url: https://ocelot.readthedocs.io/en/latest/
  - type: Getting Started
    url: https://ocelot.readthedocs.io/en/latest/introduction/gettingstarted.html
  - type: Change Log
    url: https://github.com/ThreeMammals/Ocelot/releases
  - type: GitHub Organization
    url: https://github.com/ThreeMammals/Ocelot
  - type: GitHubRepository
    url: https://github.com/ThreeMammals/Ocelot
  - type: Community
    url: https://github.com/ThreeMammals/Ocelot/discussions
  - type: Issue Tracker
    url: https://github.com/ThreeMammals/Ocelot/issues
  - type: SDKs
    url: https://www.nuget.org/packages/Ocelot
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
