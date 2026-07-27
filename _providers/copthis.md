---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: true
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 51.0
  scored_at: '2026-07-27'
api_count: 2
apis:
- description: Order previews, creation, tracking, address updates, and cancellation.
  name: CopThis Orders API
  slug: copthis-orders-api
- description: Partner stores (typically one per artist) and their merchandise.
  name: CopThis Stores API
  slug: copthis-stores-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/copthis-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://merchbar.com
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/CopThis/partner-api/blob/master/partner_api.md
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/CopThis/partner-api/blob/master/partner_api.md#api-endpoints
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CopThis
- group: auth
  title: ''
  type: Authentication
  url: authentication/copthis-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/copthis-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/copthis-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/copthis-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/copthis-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/copthis-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/copthis-conformance.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/copthis-partner-api-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/copthis-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/copthis-llms.txt
created: '2026-07-17'
description: CopThis is the company behind Merchbar, the official online merchandise retailer for musicians and artists, selling authenticated band and artist merch (vinyl, apparel, accessories) across thousands of artist stores. CopThis operates the Merchbar Partner API — a REST contract that merchandise and fulfillment partners implement so Merchbar can list a partner's stores and merchandise and place, track, update, and cancel orders on behalf of Merchbar customers. The API uses HTTP Basic authentication over HTTPS, a JSON envelope with a top-level data key and pagination for collections, URI-path versioning (v1), and an error envelope for 4xx/5xx responses. CopThis is a portfolio company of 500 Global.
image: https://merchbar.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: copthis-mcp.yml
  slug: copthis-mcpyml
modified: '2026-07-18'
name: CopThis
nav: Providers
network: true
overview: 'CopThis publishes 2 APIs on the [APIs.io](https://apis.io/) network: Orders API and Stores API. Tagged areas include Company, Music, Merchandise, E-Commerce, and Retail.


  CopThis'' developer surface includes documentation, API reference, authentication, and 13 more developer resources.'
random_paper: 14
score:
  band: thin
  composite: 35.2
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 63.7
    developer_ergonomics: 41.3
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 35.2
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/copthis/refs/heads/main/screenshots/copthis-2026-07-25T210411.png
security:
- kind: authentication
  name: Copthis Authentication
  slug: copthis-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Copthis Domain Security
  slug: copthis-domain-security
  summary_line: TLSv1.3 · DMARC
slug: copthis
tags:
- Company
- Music
- Merchandise
- E-Commerce
- Retail
- Orders
- Fulfillment
- Partner API
- Marketplace
website: https://merchbar.com
---
