---
access_model:
  confidence: medium
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Open Brewery Db Agentic Access
  operation_count: 6
  slug: open-brewery-db-agentic-access
  summary_line: 6 operations
api_count: 1
apis:
- description: Brewery listing, retrieval, search, autocomplete, and metadata operations.
  name: Open Brewery DB Breweries API
  slug: open-brewery-db-breweries-api
artifact_total: 14
collections:
- collection_type: open
  name: Open Brewery DB
  slug: open-open-brewery-db
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/open-brewery-db-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/open-brewery-db-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.openbrewerydb.org/
- group: docs
  title: ''
  type: Documentation
  url: https://www.openbrewerydb.org/documentation
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/openbrewerydb
- group: company
  title: ''
  type: Blog
  url: https://www.openbrewerydb.org/news
- group: commercial
  title: ''
  type: Pricing
  url: https://www.openbrewerydb.org/
- group: other
  title: ''
  type: X
  url: https://bsky.app/profile/openbrewerydb.org
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/open-brewery-db/refs/heads/main/plans/open-brewery-db-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/open-brewery-db/refs/heads/main/rate-limits/open-brewery-db-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/open-brewery-db/refs/heads/main/finops/open-brewery-db-finops.yml
created: '2024-11-13'
description: Open Brewery DB is a free and open-source REST API providing public information on breweries, cideries, brewpubs, and bottleshops worldwide. The database contains 11,000+ entries across 23+ countries and 212+ states and regions. No API key, authentication, or registration is required. Data includes brewery name, type, address, city, state, country, coordinates, phone, and website. The API processes over 720,000 requests per week and bulk dataset downloads are available in CSV, JSON, and SQL formats.
examples:
- key_count: 6
  name: Brewery Meta
  slug: brewery-meta
- key_count: 16
  name: Brewery Single
  slug: brewery-single
finops:
- name: Open Brewery Db Finops
  service_category: API
  slug: open-brewery-db-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/open-brewery-db.png
json_schemas:
- name: BreweryMeta
  property_count: 6
  slug: brewery-meta
- name: Brewery
  property_count: 16
  slug: brewery
jsonld:
- class_count: 3
  name: Brewery Context
  property_count: 14
  slug: brewery-context
- class_count: 0
  name: Brewery Example Context
  property_count: 0
  slug: brewery-example
layout: provider
modified: '2026-06-13'
name: Open Brewery DB
nav: Providers
network: true
overview: 'Open Brewery DB publishes 1 API on the [APIs.io](https://apis.io/) network: Breweries API. Tagged areas include Beer, Bottle Shops, Brew Pubs, Breweries, and Cider.


  The Open Brewery DB catalog on APIs.io includes 2 JSON-LD contexts and 1 Spectral governance ruleset.


  Open Brewery DB''s developer surface includes documentation, engineering blog, pricing, and 8 more developer resources.'
plans:
- name: Open Brewery Db Plans Pricing
  plan_count: 1
  slug: open-brewery-db-plans-pricing
random_paper: 65
rate_limits:
- limit_count: 0
  name: Open Brewery Db Rate Limits
  slug: open-brewery-db-rate-limits
rules:
- name: Open Brewery DB API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: open-brewery-db-jsonschema-spectral-rules
score:
  band: thin
  composite: 40.2
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 65.9
    developer_ergonomics: 10.9
    discoverability: 59.3
    governance: 58.3
    operational_transparency: 5.3
  previous_composite: 40.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/open-brewery-db/refs/heads/main/screenshots/open-brewery-db-2026-06-20T190730.png
security:
- kind: domain-security
  name: Open Brewery Db Domain Security
  slug: open-brewery-db-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: open-brewery-db
tags:
- Beer
- Bottle Shops
- Brew Pubs
- Breweries
- Cider
website: https://www.openbrewerydb.org/
---
