---
access_model:
  confidence: high
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Vespa Agentic Access
  operation_count: 6
  slug: vespa-agentic-access
  summary_line: 6 operations · 3 acting
api_count: 4
apis:
- description: The /document/v1 API supports GET, POST, PUT, and DELETE for documents, plus bulk visiting/iteration with continuation tokens, conditional writes (test-and-set using the document selector language), a
  name: Vespa Document API v1
  slug: vespa-document-api-v1
- description: The Vespa Search API accepts queries via YQL or structured query JSON over HTTP GET/POST. It powers full-text, vector, and hybrid retrieval with ranking expressions defined in the application package.
  name: Vespa Search API
  slug: vespa-search-api
- description: Single-document GET, POST, PUT, DELETE operations
  name: Vespa Documents API
  slug: vespa-documents-api
- description: Bulk visit (iteration) operations
  name: Vespa Visit API
  slug: vespa-visit-api
artifact_total: 12
collections:
- collection_type: open
  name: Vespa Document API
  slug: open-vespa
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/vespa-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/vespa-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vespa-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vespa-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vespa-ai
- group: company
  title: ''
  type: Website
  url: https://vespa.ai/
- group: start
  title: ''
  type: Portal
  url: https://docs.vespa.ai/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/vespa-engine/vespa
- group: other
  title: Vespa Cloud
  type: CommercialOffering
  url: https://cloud.vespa.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.vespa.ai/price-calculator.html
- group: commercial
  title: ''
  type: Plans
  url: plans/vespa-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/vespa-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/vespa-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.vespa.ai/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://blog.vespa.ai/feed.xml
created: '2026-05-08'
description: Vespa is an Apache 2.0 open-source serving engine for big-data, vector search, and recommendations. It exposes a Document API (write/read), a Search API (query), and several admin endpoints. Vespa Cloud is the commercial managed offering.
finops:
- name: Vespa Finops
  service_category: Vector Database
  slug: vespa-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vespa.png
layout: provider
modified: '2026-05-08'
name: Vespa
nav: Providers
network: true
overview: 'Vespa publishes 2 APIs on the [APIs.io](https://apis.io/) network: Documents API and Visit API. Tagged areas include Vector Database, Search, Open Source, Real-Time, and Recommendations.


  Vespa''s developer surface includes authentication, developer portal, pricing, engineering blog, and 11 more developer resources.'
plans:
- name: Vespa Plans Pricing
  plan_count: 1
  slug: vespa-plans-pricing
random_paper: 51
rate_limits:
- limit_count: 1
  name: Vespa Rate Limits
  slug: vespa-rate-limits
score:
  band: thin
  composite: 34.7
  delta: -3.1
  facets:
    commercial_clarity: 39.5
    contract_quality: 49.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 37.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vespa/refs/heads/main/screenshots/vespa-2026-06-20T200953.png
security:
- kind: authentication
  name: Vespa Authentication
  slug: vespa-authentication
  summary_line: mutualTLS · 1 scheme
- kind: domain-security
  name: Vespa Domain Security
  slug: vespa-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Vespa Vulnerability Disclosure
  slug: vespa-vulnerability-disclosure
  summary_line: Intigriti · security.txt · contact published
slug: vespa
tags:
- Vector Database
- Search
- Open Source
- Real-Time
- Recommendations
website: https://vespa.ai/
---
