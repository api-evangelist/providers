---
aid: lumos
name: Lumos
description: Lumos is the first Autonomous Identity Platform that helps organizations discover and manage access to all apps with enhanced security, increased productivity, and reduced cost. Lumos automates access requests, enforces least privilege, speeds up user access reviews, and eliminates extra SaaS app spending through 80+ connectors and an API.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Access Management
  - Access Reviews
  - Deprovisioning
  - Identity Governance
  - Identity Platform
  - Least Privilege
  - Provisioning
  - SaaS Management
  - Shadow IT
url: https://raw.githubusercontent.com/api-evangelist/lumos/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-03-27'
specificationVersion: '0.19'
apis:
  - aid: lumos:rest-api
    name: Lumos REST API
    description: The Lumos REST API enables programmatic access to the Lumos identity platform for automating tasks such as managing users, apps, access requests, and governance workflows. All requests require a bearer token (prefixed lsk_) in the Authorization header.
    humanURL: https://developers.lumos.com/docs/rest-api
    tags:
      - Access Management
      - Automation
      - Governance
      - Identity
    properties:
      - url: https://developers.lumos.com/reference/lumos-api
        type: Documentation
      - url: https://developers.lumos.com/docs/quick-start
        type: GettingStarted
      - url: https://developers.lumos.com/docs/rest-api
        type: Authentication
  - aid: lumos:connector-sdk
    name: Lumos Connector SDK
    description: The Lumos Connector SDK allows developers to build custom connectors that integrate third-party applications with the Lumos platform, enabling automated provisioning, deprovisioning, and access management for apps not yet supported natively.
    humanURL: https://developers.lumos.com/docs/connector-sdk
    tags:
      - Connectors
      - Integrations
      - SDK
    properties:
      - url: https://developers.lumos.com/docs/connector-sdk
        type: Documentation
      - url: https://developers.lumos.com/docs/building-a-lumos-connector-step-by-step-tutorial
        type: GettingStarted
common:
  - type: Website
    url: https://www.lumos.com/
  - type: Documentation
    url: https://developers.lumos.com/
  - type: Support
    url: https://support.lumos.com/
  - type: GettingStarted
    url: https://developers.lumos.com/docs/getting-started
  - type: Blog
    url: https://www.lumos.com/blog
  - type: Login
    url: https://app.lumosidentity.com/
  - type: SignUp
    url: https://www.lumos.com/demo
  - type: GitHub
    url: https://github.com/Lumos-Labs
  - type: LinkedIn
    url: https://www.linkedin.com/company/lumosidentity
  - type: CLI
    url: https://developers.lumos.com/docs/cli
  - type: ProductDocumentation
    url: https://docs.lumos.com/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
