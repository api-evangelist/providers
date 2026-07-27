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
api_count: 3
apis:
- description: Retrieve individual and company wealth-intelligence dossiers.
  name: Wealth-X Dossiers API
  slug: wealth-x-dossiers-api
- description: Reference / lookup data used to build searches.
  name: Wealth-X Reference API
  slug: wealth-x-reference-api
- description: Advanced search across the Wealth-X database.
  name: Wealth-X Search API
  slug: wealth-x-search-api
artifact_total: 6
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.wealthx.com/api/main.html
- group: docs
  title: ''
  type: Documentation
  url: https://developers.wealthx.com/docs/api/index.html
- group: docs
  title: ''
  type: APIReference
  url: https://developers.wealthx.com/docs/api/index.html
- group: start
  title: ''
  type: Portal
  url: https://wealthx.com/products/api
- group: operate
  title: ''
  type: Support
  url: https://wealthx.com/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://wealthx.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://wealthx.com/terms-of-use
- group: build
  title: ''
  type: Postman
  url: https://developers.wealthx.com/api/Wealth-X%20API%20Samples.postman_collection.json
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wealth-x-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wealth-x-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/wealth-x-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/wealth-x-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/wealth-x-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/wealth-x-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/wealth-x-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/wealth-x-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wealth-x-llms.txt
created: '2026-07-17'
description: Wealth-X, an Altrata company founded in 2010, provides curated wealth intelligence on ultra-high-net-worth (UHNW) and very-high-net-worth (VHNW) individuals and their privately held companies. Its Connect API delivers Wealth-X dossiers — net worth, careers, interests, philanthropy and relationship networks — plus advanced prospect search and bulk/incremental sync directly into a subscriber's CRM or data platform. Wealth-X serves financial services, luxury, nonprofit and education clients for prospect qualification, relationship intelligence and compliance.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wealth-x.png
layout: provider
mcp_servers:
- description: ''
  name: wealth-x-mcp.yml
  slug: wealth-x-mcpyml
modified: '2026-07-21'
name: Wealth-X
nav: Providers
network: true
overview: 'Wealth-X publishes 3 APIs on the [APIs.io](https://apis.io/) network: Dossiers API, Reference API, and Search API. Tagged areas include Company, Wealth Intelligence, Data, UHNW, and Prospecting.


  Wealth-X''s developer surface includes documentation, API reference, developer portal, support, authentication, and 13 more developer resources.'
random_paper: 62
score:
  band: thin
  composite: 40.6
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 58.4
    developer_ergonomics: 58.7
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 40.6
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Wealth X Authentication
  slug: wealth-x-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Wealth X Domain Security
  slug: wealth-x-domain-security
  summary_line: TLSv1.3 · DMARC
slug: wealth-x
tags:
- Company
- Wealth Intelligence
- Data
- UHNW
- Prospecting
- Financial Services
- CRM
- People Data
website: https://developers.wealthx.com/api/main.html
---
