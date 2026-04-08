---
aid: ocelot
url: https://raw.githubusercontent.com/api-evangelist/ocelot/refs/heads/main/apis.yml
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
name: Ocelot
tags:
- .NET
- API Gateway
- Microservices
- Open Source
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Ocelot is an open-source API Gateway built with .NET for microservices architectures. It provides routing, authentication, rate limiting, load balancing, and service discovery features for managing and securing APIs in .NET ecosystems.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

