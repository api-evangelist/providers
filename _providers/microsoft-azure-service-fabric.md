---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Microsoft Azure Service Fabric Agentic Access
  operation_count: 7
  slug: microsoft-azure-service-fabric-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 2
apis:
- description: Clusters operations
  name: Azure Service Fabric Clusters API
  slug: microsoft-azure-service-fabric-clusters-api
- description: Operations operations
  name: Azure Service Fabric Operations API
  slug: microsoft-azure-service-fabric-operations-api
artifact_total: 10
collections:
- collection_type: open
  name: Azure Service Fabric REST API
  slug: open-microsoft-azure-service-fabric
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-service-fabric-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-service-fabric-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-service-fabric-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-azure-service-fabric-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoft
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/details/service-fabric/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/service-fabric/
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/azure/service-fabric/service-fabric-quickstart-containers
- group: operate
  title: ''
  type: StatusPage
  url: https://azure.status.microsoft/en-us/status
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/
- group: company
  title: ''
  type: Blog
  url: https://azure.microsoft.com/en-us/blog/product/service-fabric/
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/azure-service-fabric
- group: agent
  title: ''
  type: LlmsText
  url: https://portal.azure.com/llms.txt
created: '2026-03-13'
description: Azure Service Fabric REST API provides management of microservices clusters, applications, and services. It supports creating and scaling clusters, deploying applications, managing partitions and replicas, and monitoring cluster health for distributed systems.
finops:
- name: Microsoft Azure Service Fabric Finops
  service_category: API
  slug: microsoft-azure-service-fabric-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-azure-service-fabric.png
layout: provider
modified: '2026-05-19'
name: Azure Service Fabric
nav: Providers
network: true
overview: 'Azure Service Fabric publishes 2 APIs on the [APIs.io](https://apis.io/) network: Clusters API and Operations API. Tagged areas include Microservices, Distributed Systems, Containers, and Orchestration.


  Azure Service Fabric''s developer surface includes authentication, developer portal, pricing, documentation, getting-started guide, support, engineering blog, and 9 more developer resources.'
plans:
- name: Microsoft Azure Service Fabric Plans Pricing
  plan_count: 3
  slug: microsoft-azure-service-fabric-plans-pricing
random_paper: 27
rate_limits:
- limit_count: 5
  name: Microsoft Azure Service Fabric Rate Limits
  slug: microsoft-azure-service-fabric-rate-limits
scopes:
- name: Microsoft Azure Service Fabric Scopes
  scope_count: 1
  slug: microsoft-azure-service-fabric-scopes
  summary_line: 1 scope · implicit
score:
  band: developing
  composite: 48.2
  delta: 0.0
  facets:
    commercial_clarity: 71.1
    contract_quality: 53.1
    developer_ergonomics: 45.7
    discoverability: 47.5
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 48.2
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-service-fabric/refs/heads/main/screenshots/microsoft-azure-service-fabric-2026-06-20T185437.png
security:
- kind: authentication
  name: Microsoft Azure Service Fabric Authentication
  slug: microsoft-azure-service-fabric-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Azure Service Fabric Domain Security
  slug: microsoft-azure-service-fabric-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-azure-service-fabric
tags:
- Microservices
- Distributed Systems
- Containers
- Orchestration
website: https://portal.azure.com/
---
