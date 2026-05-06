---
aid: guidewire
url: https://raw.githubusercontent.com/api-evangelist/guidewire/refs/heads/main/apis.yml
apis:
  - aid: guidewire:guidewire-policycenter-api
    name: Guidewire PolicyCenter API
    tags:
      - Insurance
      - P&C
      - Policy
      - Underwriting
    image: https://raw.githubusercontent.com/api-evangelist/guidewire/refs/heads/main/image.png
    humanURL: https://docs.guidewire.com/
    baseURL: https://api.guidewire.com
    properties:
      - url: https://docs.guidewire.com/
        type: Documentation
      - url: https://www.guidewire.com/developers
        type: Getting Started
      - url: openapi/guidewire-policycenter-openapi.yml
        type: OpenAPI
    description: The Guidewire PolicyCenter API provides REST endpoints for policy lifecycle management, underwriting workflows, policy issuance, endorsements, renewals, and cancellations for property and casualty insurance carriers.
  - aid: guidewire:guidewire-claimcenter-api
    name: Guidewire ClaimCenter API
    tags:
      - Claims
      - Insurance
      - Loss Adjustment
      - P&C
    image: https://raw.githubusercontent.com/api-evangelist/guidewire/refs/heads/main/image.png
    humanURL: https://docs.guidewire.com/
    baseURL: https://api.guidewire.com
    properties:
      - url: https://docs.guidewire.com/
        type: Documentation
      - url: https://www.guidewire.com/developers
        type: Getting Started
      - url: openapi/guidewire-claimcenter-openapi.yml
        type: OpenAPI
    description: The Guidewire ClaimCenter API provides REST endpoints for claims intake, assignment, investigation, reserving, payment processing, and closure workflows for P&C insurance claim operations.
  - aid: guidewire:guidewire-billingcenter-api
    name: Guidewire BillingCenter API
    tags:
      - Billing
      - Insurance
      - P&C
      - Payments
    image: https://raw.githubusercontent.com/api-evangelist/guidewire/refs/heads/main/image.png
    humanURL: https://docs.guidewire.com/
    baseURL: https://api.guidewire.com
    properties:
      - url: https://docs.guidewire.com/
        type: Documentation
      - url: https://www.guidewire.com/developers
        type: Getting Started
    description: The Guidewire BillingCenter API provides REST endpoints for payment orchestration, invoice generation, payment plans, disbursements, and collections management for insurance billing operations.
  - aid: guidewire:guidewire-integration-gateway-api
    name: Guidewire Integration Gateway API
    tags:
      - Insurance
      - Integration
      - Middleware
      - P&C
    image: https://raw.githubusercontent.com/api-evangelist/guidewire/refs/heads/main/image.png
    humanURL: https://docs.guidewire.com/
    baseURL: https://api.guidewire.com
    properties:
      - url: https://docs.guidewire.com/
        type: Documentation
      - url: https://www.guidewire.com/developers
        type: Getting Started
      - url: asyncapi/guidewire-integration-gateway-asyncapi.yml
        type: AsyncAPI
    description: The Guidewire Integration Gateway provides a managed API layer for connecting Guidewire Cloud applications to third-party systems, enabling event-driven integrations and REST API extensions for the Guidewire insurance platform.
common:
  aid: guidewire
  name: Guidewire
  description: Guidewire provides the insurance industry's leading platform including PolicyCenter, ClaimCenter, and BillingCenter. REST APIs enable policy lifecycle management, claims processing, payment orchestration, and underwriting workflows for P&C insurance carriers on the Guidewire Cloud platform.
  image: https://raw.githubusercontent.com/api-evangelist/guidewire/refs/heads/main/image.png
  tags:
    - Insurance
    - Policy
    - Claims
    - Billing
    - P&C
  properties:
    - url: https://www.guidewire.com/developers
      type: Portal
    - url: https://docs.guidewire.com/
      type: Documentation
    - url: https://www.guidewire.com/developers
      type: Getting Started
    - url: https://status.guidewire.com/
      type: Status
    - url: https://community.guidewire.com/
      type: Support
    - url: https://www.guidewire.com/resources/blog
      type: Blog
    - url: https://www.guidewire.com/
      type: Website
    - url: https://marketplace.guidewire.com/
      type: Developer Tools
    - url: https://github.com/guidewire-oss
      type: GitHub Organization
    - url: openapi/guidewire-policycenter-openapi.yml
      type: OpenAPI
    - url: openapi/guidewire-claimcenter-openapi.yml
      type: OpenAPI
    - url: json-schema/guidewire-policy-schema.json
      type: JSONSchema
    - url: json-ld/guidewire-context.jsonld
      type: JSONLDContext
    - url: asyncapi/guidewire-integration-gateway-asyncapi.yml
      type: AsyncAPI
maintainer:
  name: Kin Lane
  email: kin@apievangelist.com
modified: '2026-04-28'
description: Guidewire Documentation.
---
