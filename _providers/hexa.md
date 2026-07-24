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
- acting_count: 26
  human_in_the_loop: 0
  name: Hexa Agentic Access
  operation_count: 44
  slug: hexa-agentic-access
  summary_line: 44 operations · 26 acting
api_count: 9
apis:
- description: The Cells API from Hex — 3 operation(s) for cells.
  name: Hex Cells API
  slug: hexa-cells-api
- description: The Collections API from Hex — 2 operation(s) for collections.
  name: Hex Collections API
  slug: hexa-collections-api
- description: The Data Connections API from Hex — 3 operation(s) for data connections.
  name: Hex Data Connections API
  slug: hexa-data-connections-api
- description: The Embedding API from Hex — 1 operation(s) for embedding.
  name: Hex Embedding API
  slug: hexa-embedding-api
- description: The Groups API from Hex — 2 operation(s) for groups.
  name: Hex Groups API
  slug: hexa-groups-api
- description: The Guides API from Hex — 4 operation(s) for guides.
  name: Hex Guides API
  slug: hexa-guides-api
- description: The Projects API from Hex — 10 operation(s) for projects.
  name: Hex Projects API
  slug: hexa-projects-api
- description: The Semantic (projects|models) API from Hex — 2 operation(s) for semantic (projects|models).
  name: Hex Semantic (projects|models) API
  slug: hexa-semantic-projects-models-api
- description: The Users API from Hex — 3 operation(s) for users.
  name: Hex Users API
  slug: hexa-users-api
artifact_total: 18
collections:
- collection_type: open
  name: Hex API
  slug: open-hexa
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hexa-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/hexa-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/hexa-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hexa-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hexa-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hex-technologies
- group: company
  title: ''
  type: Website
  url: https://hex.tech/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.hex.tech/
- group: commercial
  title: ''
  type: Pricing
  url: https://hex.tech/pricing/
- group: start
  title: ''
  type: Signup
  url: https://app.hex.tech/signup
- group: start
  title: ''
  type: Login
  url: https://app.hex.tech/login
- group: company
  title: ''
  type: Blog
  url: https://hex.tech/blog/
- group: agent
  title: ''
  type: LlmsText
  url: https://app.hex.tech/llms.txt
created: '2025-01-01'
description: Hex is an AI analytics platform that enables teams to explore, analyze, and share data insights together. It provides agentic notebooks, conversational self-serve analytics, data apps, dashboards, and a Context Studio for semantic modeling and data governance, integrating with major data warehouses such as Snowflake, BigQuery, Databricks, and Redshift.
finops:
- name: Hexa Finops
  service_category: API
  slug: hexa-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hexa.png
layout: provider
modified: '2026-05-19'
name: Hex
nav: Providers
network: true
overview: 'Hex publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Cells API, Collections API, Data Connections API, and 6 more. Tagged areas include Analytics, Collaboration, Data, and Notebooks.


  Hex''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, and 8 more developer resources.'
plans:
- name: Hexa Plans Pricing
  plan_count: 3
  slug: hexa-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Hexa Rate Limits
  slug: hexa-rate-limits
score:
  band: thin
  composite: 39.9
  delta: 0.0
  facets:
    commercial_clarity: 71.1
    contract_quality: 47.0
    developer_ergonomics: 21.7
    discoverability: 55.0
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 39.9
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hexa/refs/heads/main/screenshots/hexa-2026-06-20T182713.png
security:
- kind: authentication
  name: Hexa Authentication
  slug: hexa-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Hexa Domain Security
  slug: hexa-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Hexa Vulnerability Disclosure
  slug: hexa-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Hexa Trust Center
  slug: hexa-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, FedRAMP, GDPR, CSA STAR
slug: hexa
tags:
- Analytics
- Collaboration
- Data
- Notebooks
website: https://hex.tech/
---
