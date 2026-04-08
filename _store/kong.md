---
aid: kong
url: https://raw.githubusercontent.com/api-evangelist/kong/refs/heads/main/apis.yml
apis:
- aid: kong:kong
  name: Kong Gateway
  description: Kong Gateway is an open-source, lightweight API gateway optimized for microservices, delivering unparalleled latency performance and scalability through a rich plugin ecosystem.
  humanURL: https://konghq.com/products/kong-gateway
  tags:
  - API Gateway
  - Open Source
  properties:
  - type: Documentation
    url: https://developer.konghq.com/gateway/
  - type: Getting Started
    url: https://docs.konghq.com/gateway/latest/get-started/
  - type: Change Log
    url: https://developer.konghq.com/gateway/changelog/
  - type: GitHubRepository
    url: https://github.com/Kong/kong
- aid: kong:kong-admin-api
  name: Kong Gateway Admin API
  description: The Kong Gateway Admin API provides a RESTful interface for configuring and managing Kong Gateway instances, including services, routes, plugins, consumers, and certificates. It is used by operators to configure the gateway programmatically or via decK declarative configuration.
  humanURL: https://developer.konghq.com/admin-api/
  baseURL: https://konghq.com/
  tags:
  - Admin API
  - Configuration
  - Gateway
  - REST API
  properties:
  - type: Documentation
    url: https://developer.konghq.com/admin-api/
  - type: OpenAPI
    url: openapi/kong-gateway-admin-api.yml
  - type: JSONSchema
    url: json-schema/kong-service-schema.json
  - type: GitHubRepository
    url: https://github.com/Kong/kong
- aid: kong:kong-konnect-api
  name: Kong Konnect API
  description: The Kong Konnect API provides a programmatic interface for managing the Konnect cloud platform, including control planes, API products, teams, system accounts, and developer portal configuration. It is used to automate Konnect operations and integrate with CI/CD pipelines.
  humanURL: https://developer.konghq.com/konnect-api/
  baseURL: https://konghq.com/
  tags:
  - Cloud
  - Konnect
  - Management
  - REST API
  properties:
  - type: Documentation
    url: https://developer.konghq.com/konnect-api/
  - type: Reference
    url: https://developer.konghq.com/api/
  - type: Authentication
    url: https://developer.konghq.com/konnect-api/
  - type: GitHubRepository
    url: https://github.com/Kong/kong
- aid: kong:kong-mesh
  name: Kong Mesh
  description: Kong Mesh is an enterprise-grade service mesh built on top of Kuma and Envoy, providing universal service mesh capabilities across Kubernetes and virtual machine environments. It supports mTLS, traffic policies, service discovery, observability, and multi-zone deployments.
  humanURL: https://developer.konghq.com/mesh/
  baseURL: https://konghq.com/
  tags:
  - Envoy
  - Kubernetes
  - mTLS
  - Service Mesh
  properties:
  - type: Documentation
    url: https://developer.konghq.com/mesh/
  - type: Change Log
    url: https://developer.konghq.com/mesh/changelog/
  - type: Getting Started
    url: https://developer.konghq.com/mesh/
- aid: kong:kong-insomnia
  name: Kong Insomnia
  description: Kong Insomnia is an open-source API development platform for designing, debugging, and testing APIs. It supports REST, GraphQL, gRPC, and WebSocket protocols and provides collections, environments, mock servers, and OpenAPI spec editing for developers.
  humanURL: https://developer.konghq.com/insomnia/
  baseURL: https://konghq.com/
  tags:
  - API Client
  - Developer Tools
  - Open Source
  - Testing
  properties:
  - type: Documentation
    url: https://developer.konghq.com/insomnia/
  - type: GitHubRepository
    url: https://github.com/Kong/insomnia
name: Kong
tags:
- API Gateway
- Lua
- NGINX
- Open Source
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
- url: https://konghq.com/
  name: The API Platform Powering the API World | Kong Inc.
  type: Website
  description: 'null'
- url: https://konghq.com/customers
  name: Customer and Partner Success Stories | Kong Inc.
  type: Customers
  description: 'null'
- url: https://konghq.com/customers
  name: Customer and Partner Success Stories | Kong Inc.
  type: Customers
  description: 'null'
- url: https://konghq.com/blog
  name: Latest Blogs for API Insights and Ideas | Kong Inc.
  type: Blog
  description: 'null'
- url: https://konghq.com/resources/e-book
  name: 'eBooks: The Latest in API Trends | Kong Inc.'
  type: eBooks
  description: 'null'
- url: https://konghq.com/resources/case-study
  name: Case Studies | Kong Inc.
  type: CaseStudies
  description: 'null'
- url: https://konghq.com/resources/videos#
  name: 'Video Library: Level Up Your API Knowledge | Kong Inc.'
  type: Videos
  description: 'null'
- url: https://konghq.com/events/webinars
  name: 'On-Demand Webinars: Gateway to API News and Learning | Kong Inc.'
  type: Webinars
  description: 'null'
- url: https://konghq.com/events/workshops
  name: Workshops | Kong Inc.
  type: Workshops
  description: 'null'
- url: https://konghq.com/pricing/plans
  name: API Gateway Pricing for Konnect | Kong Inc.
  type: Pricing
  description: 'null'
- url: https://konghq.com/legal/terms-of-use
  name: Website Terms of Use | Kong Inc.
  type: TermsOfService
  description: 'null'
- url: https://konghq.com/legal/privacy-policy
  name: Privacy Policy | Kong Inc.
  type: PrivacyPolicy
  description: 'null'
- url: https://konghq.com/compliance
  name: Trust and Compliance at Kong | Kong Inc.
  type: Trust
  description: 'null'
- url: https://konghq.com/compliance
  name: Trust and Compliance at Kong | Kong Inc.
  type: Compliance
  description: 'null'
- url: https://konghq.com/compliance
  name: Trust and Compliance at Kong | Kong Inc.
  type: Compliance
  description: 'null'
- url: https://signin.cloud.konghq.com/u/login?state=hKFo2SBwMlNVbGpWc1RCamFRQkNTNVpqUkRRWjBacE9OdldleqFur3VuaXZlcnNhbC1sb2dpbqN0aWTZIFBOMzZGWVhickxPS3dUV2UyazlhS3hNTXlKbENCWEhto2NpZNkgVWVjOTVoa3VRTmR0eDE4UzZvS0dsS0dJaElGNVQ0cHg
  name: Login | Konnect
  type: Login
  description: 'null'
- url: https://konghq.com/products/kong-konnect/register
  name: Kong Inc.
  type: SignUp
  description: 'null'
- url: https://konghq.com/
  name: The API Platform Powering the API World | Kong Inc.
  type: Website
  description: 'null'
- data:
  - name: API Gateway for Istio
  - name: Build on Kubernetes
  - name: Decentralized Load Balancing
  - name: Monolith to Microservices
  - name: Observability
  - name: Power OpenAI Applications
  - name: Service Mesh Connectivity
  - name: Zero Trust Security
  name: Use Cases
  type: UseCases
- data:
  - name: Advanced Analytics
  - name: API Analytics and Observability
  - name: API Developer Portal
  - name: API Discovery
  - name: API Gateway Transaction Volume
  - name: API Requests per Month Included
  - name: Audit Logging
  - name: Cost per Additional API Developer Portal
  - name: Cost per Additional Published API
  - name: Cost per Dcgw Control Plane
  - name: Dcgw Bandwidth Cost
  - name: Dcgw Control Plane Limits
  - name: Dcgws in Your AWS, Gcp, And/or Azure Region of Choice
  - name: Dedicated Cloud Gateways (Dcgw)
  - name: Dedicated Customer Success Manager
  - name: Email Only
  - name: Email Support During Your Trial
  - name: Email, Zendesk, Slack, and Other Channels Available
  - name: Hybrid API Gateway Control Plane Costs
  - name: Hybrid API Gateway Control Plane Limits
  - name: Hybrid API Gateways
  - name: Integration With Third-Party Monitoring and Observability Solutions
  - name: Limited to One Region per Control Plane
  - name: Maximum Number of API Developer Portals
  - name: Maximum Number of Published Apisservice Catalog
  - name: Number of Included API Developer Portals
  - name: Number of Included Governed Services
  - name: Number of Included Published APIs
  - name: Number of Regions
  - name: Observability
  - name: Opentelemetry Support
  - name: Professional Services Available
  - name: RBAC
  - name: Security and Governance
  - name: Self-Managed API Gateway
  - name: Serverless API Gateway Contol Plane Costs
  - name: Serverless API Gateway Control Plane Limits
  - name: Serverless API Gateways
  - name: SLA
  - name: SSO
  - name: Support Channels
  - name: Technical Support and Customer Success
  - name: Training and Support
  - name: User Management, Access Control, and Governance
  name: Features
  type: Features
created: '2025-01-08T00:00:00.000Z'
modified: '2026-04-07'
position: Consuming
description: Kong Gateway is the world's most popular open-source API gateway, built on NGINX and Lua, offering a plugin ecosystem for authentication, rate limiting, observability, and traffic management at any scale.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

