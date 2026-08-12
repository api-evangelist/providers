---
access_model:
  confidence: medium
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
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
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Whisky Hunter Agentic Access
  operation_count: 3
  slug: whisky-hunter-agentic-access
  summary_line: 3 operations
api_count: 2
apis:
- description: The Auctions API from Whisky Hunter — 1 operation(s) for auctions.
  name: Whisky Hunter Auctions API
  slug: whisky-hunter-auctions-api
- description: The Distilleries API from Whisky Hunter — 2 operation(s) for distilleries.
  name: Whisky Hunter Distilleries API
  slug: whisky-hunter-distilleries-api
artifact_total: 18
collections:
- collection_type: open
  name: Whisky Hunter API
  slug: open-whisky-hunter
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/whisky-hunter-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/whisky-hunter-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://whiskyhunter.net
- group: other
  title: ''
  type: API
  url: https://whiskyhunter.net/api/
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/whisky-hunter/refs/heads/main/openapi/whisky-hunter-openapi.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/whisky-hunter/refs/heads/main/vocabulary/whisky-hunter-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/whisky-hunter/refs/heads/main/json-ld/whisky-hunter-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/whisky-hunter/refs/heads/main/rules/whisky-hunter-rules.yml
- group: company
  title: ''
  type: Blog
  url: https://whiskyhunter.net/blog/
created: '2025-02-24'
description: Whisky Hunter is a market research and data platform for whisky collectors, investors, traders, and enthusiasts that aggregates historical auction data from 28 online whisky auction sites into a single database. It tracks trading volumes, winning bids, lot counts, and per-distillery statistics. All trading volumes and winning bids are stated in GBP (£). The Whisky Hunter API provides free, public access to this auction data with no authentication required.
examples:
- key_count: 2
  name: Whisky Hunter Get Auctions Data Example
  slug: whisky-hunter-get-auctions-data-example
- key_count: 2
  name: Whisky Hunter Get Distillery Data Example
  slug: whisky-hunter-get-distillery-data-example
- key_count: 2
  name: Whisky Hunter List Distilleries Example
  slug: whisky-hunter-list-distilleries-example
finops:
- name: Whisky Hunter Finops
  service_category: API
  slug: whisky-hunter-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/whisky-hunter.png
json_schemas:
- name: Whisky Hunter Auction Data Point
  property_count: 9
  slug: whisky-hunter-auction-data
- name: Whisky Hunter Distillery
  property_count: 3
  slug: whisky-hunter-distillery
json_structures:
- name: Whisky Hunter Auction Data Structure
  property_count: 0
  slug: whisky-hunter-auction-data-structure
- name: Whisky Hunter Distillery Structure
  property_count: 0
  slug: whisky-hunter-distillery-structure
jsonld:
- class_count: 40
  name: Whisky Hunter Context
  property_count: 0
  slug: whisky-hunter-context
layout: provider
modified: '2026-05-19'
name: Whisky Hunter
nav: Providers
network: true
overview: 'Whisky Hunter publishes 2 APIs on the [APIs.io](https://apis.io/) network: Auctions API and Distilleries API. Tagged areas include Whisky, Spirits, Auctions, Market Data, and Collectors.


  The Whisky Hunter catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Whisky Hunter''s developer surface includes engineering blog and 8 more developer resources.'
plans:
- name: Whisky Hunter Plans Pricing
  plan_count: 3
  slug: whisky-hunter-plans-pricing
random_paper: 102
rate_limits:
- limit_count: 5
  name: Whisky Hunter Rate Limits
  slug: whisky-hunter-rate-limits
rules:
- name: Whisky Hunter API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: whisky-hunter-jsonschema-spectral-rules
- name: Whisky Hunter API Rules
  rule_count: 9
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 7
  slug: whisky-hunter-rules
score:
  band: thin
  composite: 34.0
  delta: -7.2
  facets:
    commercial_clarity: 15.8
    contract_quality: 61.2
    developer_ergonomics: 2.2
    discoverability: 68.5
    governance: 68.8
    operational_transparency: 7.9
  previous_composite: 41.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 28.3
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/whisky-hunter/refs/heads/main/screenshots/whisky-hunter-2026-06-20T201439.png
security:
- kind: domain-security
  name: Whisky Hunter Domain Security
  slug: whisky-hunter-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: whisky-hunter
tags:
- Whisky
- Spirits
- Auctions
- Market Data
- Collectors
- Investors
website: https://whiskyhunter.net
---
