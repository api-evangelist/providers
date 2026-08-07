---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Crunchbase Data Agentic Access
  operation_count: 6
  slug: crunchbase-data-agentic-access
  summary_line: 6 operations · 1 acting
api_count: 4
apis:
- description: Resolve a query string to matching entity identifiers.
  name: Crunchbase Autocomplete API
  slug: crunchbase-data-autocomplete-api
- description: Detect entities removed from the Crunchbase Graph (deltas).
  name: Crunchbase Deleted Entities API
  slug: crunchbase-data-deleted-entities-api
- description: Retrieve a single entity (and its related cards) by UUID or permalink.
  name: Crunchbase Entity Lookup API
  slug: crunchbase-data-entity-lookup-api
- description: Query a collection with field filters and keyset pagination.
  name: Crunchbase Search API
  slug: crunchbase-data-search-api
artifact_total: 11
collections:
- collection_type: open
  name: Crunchbase Data API v4
  slug: open-crunchbase-data
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/crunchbase-data-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/crunchbase-data-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/crunchbase-data-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/crunchbase
- group: company
  title: ''
  type: Website
  url: https://www.crunchbase.com
- group: docs
  title: ''
  type: Documentation
  url: https://data.crunchbase.com/docs
- group: start
  title: ''
  type: SignUp
  url: https://about.crunchbase.com/crunchbase-api-application-form/
- group: commercial
  title: ''
  type: Plans
  url: plans/crunchbase-data-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/crunchbase-data-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/crunchbase-data-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://about.crunchbase.com/blog/
created: '2026-07-11'
description: 'Crunchbase is a leading source of private and public company, funding, and investor data - firmographics, funding rounds, acquisitions, investors, people, and events across the global startup and business landscape. The Crunchbase Data API (REST v4, base https://api.crunchbase.com/v4/data) exposes this graph programmatically through four surfaces - Entity Lookup, Search, Autocomplete, and Deleted Entities (deltas) - for web intelligence, reference data, market research, sales and investment prospecting, and enrichment use cases. It is a read-only RESTful service authenticated with an API key (user_key query parameter or X-cb-user-key header). Access is subscription-gated: the full API requires a Crunchbase Enterprise or Applications license, with a reduced Basic API available to Crunchbase Basic plan holders.'
finops:
- name: Crunchbase Data Finops
  service_category: Data and Analytics
  slug: crunchbase-data-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/crunchbase-data.png
layout: provider
modified: '2026-07-11'
name: Crunchbase
nav: Providers
network: true
overview: 'Crunchbase publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Autocomplete API, Deleted Entities API, Entity Lookup API, and 1 more. Tagged areas include Company Data, Web Intelligence, Funding Data, Firmographics, and B2B Data.


  Crunchbase''s developer surface includes authentication, documentation, signup flow, engineering blog, and 7 more developer resources.'
plans:
- name: Crunchbase Data Plans Pricing
  plan_count: 3
  slug: crunchbase-data-plans-pricing
random_paper: 40
rate_limits:
- limit_count: 5
  name: Crunchbase Data Rate Limits
  slug: crunchbase-data-rate-limits
score:
  band: thin
  composite: 41.7
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 61.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 41.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/crunchbase-data/refs/heads/main/screenshots/crunchbase-data-2026-07-25T210816.png
security:
- kind: authentication
  name: Crunchbase Data Authentication
  slug: crunchbase-data-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Crunchbase Data Domain Security
  slug: crunchbase-data-domain-security
  summary_line: no transport/DNS hardening detected
slug: crunchbase-data
tags:
- Company Data
- Web Intelligence
- Funding Data
- Firmographics
- B2B Data
- Investor Data
- Reference Data
- Fortune 1000
website: https://www.crunchbase.com
---
