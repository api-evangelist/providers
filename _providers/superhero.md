---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Superhero Agentic Access
  operation_count: 8
  slug: superhero-agentic-access
  summary_line: 8 operations
api_count: 2
apis:
- description: Retrieve full or partial character data by numeric ID.
  name: Superhero API Characters API
  slug: superhero-characters-api
- description: Search for characters by name.
  name: Superhero API Search API
  slug: superhero-search-api
artifact_total: 13
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/superhero-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/superhero-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.superheroapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.superheroapi.com/api.html
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/topics/superheroapi
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/
- group: company
  title: ''
  type: Blog
  url: https://www.superheroapi.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.superheroapi.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://www.superheroapi.com/
- group: other
  title: ''
  type: X
  url: https://x.com/
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/superhero/refs/heads/main/plans/superhero-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/superhero/refs/heads/main/rate-limits/superhero-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/superhero/refs/heads/main/finops/superhero-finops.yml
created: '2026-06-13'
description: The Superhero API is a quantified and programmatically accessible data source of superheroes and villains from across comic book universes. It provides comprehensive character data for 731 heroes and villains including power stats, biography, appearance, work, connections, and image data from Marvel, DC, and other publishers. Developers authenticate via an API access token obtained through GitHub login and query characters by ID or name.
examples:
- key_count: 9
  name: Batman
  slug: batman
- key_count: 3
  name: Search Results
  slug: search-results
- key_count: 9
  name: Spider Man
  slug: spider-man
finops:
- name: Superhero Finops
  service_category: API
  slug: superhero-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/superhero.png
json_schemas:
- name: Character
  property_count: 9
  slug: character
jsonld:
- class_count: 18
  name: context Context
  property_count: 16
  slug: context
layout: provider
modified: '2026-06-13'
name: Superhero API
nav: Providers
network: true
overview: 'Superhero API publishes 2 APIs on the [APIs.io](https://apis.io/) network: Characters API and Search API. Tagged areas include Superheroes, Comics, Characters, Marvel, and DC Comics.


  The Superhero API catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Superhero API''s developer surface includes documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Superhero Plans Pricing
  plan_count: 1
  slug: superhero-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 2
  name: Superhero Rate Limits
  slug: superhero-rate-limits
rules:
- name: Superhero API API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: superhero-jsonschema-spectral-rules
score:
  band: developing
  composite: 42.3
  delta: -4.5
  facets:
    commercial_clarity: 39.5
    contract_quality: 67.2
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 42.1
  previous_composite: 46.8
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
    regime: Government & Public Sector
    regime_id: government
    score: 20.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/superhero/refs/heads/main/screenshots/superhero-2026-06-20T194712.png
security:
- kind: domain-security
  name: Superhero Domain Security
  slug: superhero-domain-security
  summary_line: TLSv1.3 · DMARC
slug: superhero
tags:
- Superheroes
- Comics
- Characters
- Marvel
- DC Comics
- Entertainment
- Open Data
website: https://www.superheroapi.com/
---
