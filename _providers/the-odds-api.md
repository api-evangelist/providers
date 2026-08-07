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
- acting_count: 0
  human_in_the_loop: 0
  name: The Odds Api Agentic Access
  operation_count: 10
  slug: the-odds-api-agentic-access
  summary_line: 10 operations
api_count: 6
apis:
- description: Event listings without odds.
  name: The Odds API Events API
  slug: the-odds-api-events-api
- description: Historical odds and event snapshots.
  name: The Odds API Historical API
  slug: the-odds-api-historical-api
- description: Current odds from bookmakers.
  name: The Odds API Odds API
  slug: the-odds-api-odds-api
- description: Teams and players in a sport.
  name: The Odds API Participants API
  slug: the-odds-api-participants-api
- description: Live and recent game scores.
  name: The Odds API Scores API
  slug: the-odds-api-scores-api
- description: Available sports and their keys.
  name: The Odds API Sports API
  slug: the-odds-api-sports-api
artifact_total: 19
collections:
- collection_type: open
  name: The Odds API
  slug: open-the-odds-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/the-odds-api-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/the-odds-api-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/the-odds-api-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/the-odds-api
- group: company
  title: ''
  type: Website
  url: https://the-odds-api.com/
- group: docs
  title: ''
  type: Documentation
  url: https://the-odds-api.com/liveapi/guides/v4/
- group: start
  title: ''
  type: Signup
  url: https://the-odds-api.com/#get-access
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/the-odds-api
- group: operate
  title: ''
  type: StatusPage
  url: https://status.the-odds-api.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/the-odds-api-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/the-odds-api-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/the-odds-api-finops.yml
- group: design
  title: ''
  type: SpectralRuleset
  url: rules/the-odds-api-rules.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/the-odds-api-event-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/the-odds-api-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/the-odds-api-vocabulary.yml
created: '2025-02-08'
description: The Odds API provides sports betting odds from over 40 major bookmakers worldwide. Access current and historical odds for head-to-head, spreads, totals, and outrights markets across 100+ sports. Endpoints cover live scores, event listings, participants, and historical odds snapshots dating back to June 2020. Quota is consumed per request based on the number of regions and markets requested. All requests require an API key.
examples:
- key_count: 3
  name: The Odds Api Get Odds Example
  slug: the-odds-api-get-odds-example
finops:
- name: The Odds Api Finops
  service_category: API
  slug: the-odds-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/the-odds-api.png
json_schemas:
- name: The Odds API Event
  property_count: 7
  slug: the-odds-api-event
json_structures:
- name: The Odds Api Event Structure
  property_count: 0
  slug: the-odds-api-event-structure
jsonld:
- class_count: 24
  name: The Odds Api Context
  property_count: 5
  slug: the-odds-api-context
layout: provider
modified: '2026-05-25'
name: The Odds API
nav: Providers
network: true
overview: 'The Odds API publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Events API, Historical API, Odds API, and 3 more. Tagged areas include Betting, Odds, Sports, Scores, and Historical Data.


  The The Odds API catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  The Odds API''s developer surface includes authentication, documentation, signup flow, and 13 more developer resources.'
plans:
- name: The Odds Api Plans Pricing
  plan_count: 3
  slug: the-odds-api-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 5
  name: The Odds Api Rate Limits
  slug: the-odds-api-rate-limits
rules:
- name: The Odds API API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: the-odds-api-jsonschema-spectral-rules
- name: The Odds API API Rules
  rule_count: 10
  severity_counts:
    error: 3
    hint: 1
    info: 0
    warn: 6
  slug: the-odds-api-rules
score:
  band: developing
  composite: 51.2
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 67.4
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 51.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/the-odds-api/refs/heads/main/screenshots/the-odds-api-2026-06-20T195231.png
security:
- kind: authentication
  name: The Odds Api Authentication
  slug: the-odds-api-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: The Odds Api Domain Security
  slug: the-odds-api-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: the-odds-api
tags:
- Betting
- Odds
- Sports
- Scores
- Historical Data
website: https://the-odds-api.com/
---
