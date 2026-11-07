---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://bettip.co.za/api/v1/
  baseurl_source: declared
  description: The Gosloto API from BetTip Draws API — 4 operation(s) for gosloto.
  name: BetTip Draws API Gosloto API
  slug: bettip-draws-api-gosloto-api
- baseURL: https://bettip.co.za/api/v1/
  baseurl_source: declared
  description: The Lotto API from BetTip Draws API — 5 operation(s) for lotto.
  name: BetTip Draws API Lotto API
  slug: bettip-draws-api-lotto-api
- baseURL: https://bettip.co.za/api/v1/
  baseurl_source: declared
  description: The Uk49s API from BetTip Draws API — 7 operation(s) for uk49s.
  name: BetTip Draws API Uk49s API
  slug: bettip-draws-api-uk49s-api
- baseURL: https://bettip.co.za/api/v1/
  baseurl_source: declared
  description: The World API from BetTip Draws API — 3 operation(s) for world.
  name: BetTip Draws API World API
  slug: bettip-draws-api-world-api
artifact_total: 11
common:
- group: operate
  href: https://artifacts.apis.io/bettip-draws-api/rate-limits/bettip-draws-api-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/bettip-draws-api-rate-limits.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://bettip.co.za/api/
- group: other
  href: https://artifacts.apis.io/bettip-draws-api/overlays/bettip-draws-api-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/bettip-draws-api-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://bettip.co.za/
- group: auth
  href: https://artifacts.apis.io/bettip-draws-api/security/bettip-draws-api-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bettip-draws-api-domain-security.yml
- group: build
  href: https://artifacts.apis.io/bettip-draws-api/packages/bettip-draws-api-packages.yml
  title: ''
  type: Packages
  url: packages/bettip-draws-api-packages.yml
- group: design
  href: https://artifacts.apis.io/bettip-draws-api/components/bettip-draws-api-components.yml
  title: ''
  type: Components
  url: components/bettip-draws-api-components.yml
- group: design
  href: https://artifacts.apis.io/bettip-draws-api/conventions/bettip-draws-api-conventions.yml
  title: ''
  type: Conventions
  url: conventions/bettip-draws-api-conventions.yml
- group: design
  href: https://artifacts.apis.io/bettip-draws-api/lifecycle/bettip-draws-api-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/bettip-draws-api-lifecycle.yml
- group: commercial
  href: https://artifacts.apis.io/bettip-draws-api/plans/bettip-draws-api-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bettip-draws-api-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/bettip-draws-api/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zaiqltd
created: '2026-09-08'
description: A free, keyless lottery-results data feed providing JSON and CSV results for UK49s, Russia Gosloto, the South African National Lottery, and a small set of world draws. Backed by a public OpenAPI 3.0.3 contract, open CORS, HTTPS, and no authentication. Operated by Easybet Group (Pty) Ltd under the BetTip brand; data is CC BY 4.0.
image: https://bettip.co.za/og.png
layout: provider
modified: '2026-09-09'
name: BetTip Draws API
nav: Providers
network: true
overview: 'BetTip Draws API publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Gosloto API, Lotto API, Uk49s API, and 1 more. Tagged areas include Lottery results, UK49s, Gosloto, SA National Lottery, and JSON.


  The BetTip Draws API catalog on APIs.io includes 1 Spectral governance ruleset.


  BetTip Draws API''s developer surface includes pricing and 11 more developer resources.'
plans:
- name: Bettip Draws Api Plans Pricing
  plan_count: 1
  slug: bettip-draws-api-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Bettip Draws Api Rate Limits
  slug: bettip-draws-api-rate-limits
rules:
- authorship: generated
  effective_rule_count: 82
  extends:
  - spectral:oas
  name: BetTip Draws API API Rules
  rule_count: 41
  severity_counts:
    error: 38
    hint: 0
    info: 2
    warn: 1
  slug: bettip-draws-api-rules
score:
  band: thin
  composite: 31.1
  coverage:
    artifact_dirs: 22
    catalog_earned: 49.5
    catalog_earned_first_party: 8.0
    catalog_gap: 65.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.1
  facets:
    access_clarity: 31.6
    contract_governance: 13.6
    contract_quality: 44.4
    developer_ergonomics: 23.2
    discoverability: 73.2
    operational_transparency: 2.6
  previous_composite: 30.0
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/bettip-draws-api/bettip-draws-api-2026-10-11T102029.png
security:
- kind: authentication
  name: Bettip Draws Api Authentication
  slug: bettip-draws-api-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Bettip Draws Api Domain Security
  slug: bettip-draws-api-domain-security
  summary_line: TLSv1.3
skill_count: 2
skills:
- name: bettip-draw-archive-analysis
  slug: bettip-draws-api-draw-archive
- name: bettip-latest-lottery-results
  slug: bettip-draws-api-latest-results
slug: bettip-draws-api
tags:
- Lottery results
- UK49s
- Gosloto
- SA National Lottery
- JSON
- CSV
- OpenAPI
- Sports/Betting data
- Reference Data
- Open Data
- Gambling & Betting
website: https://bettip.co.za/
---
