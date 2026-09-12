---
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
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.1
  scored_at: '2026-09-12'
api_count: 1
apis:
- baseURL: https://bettip.co.za/api/v1/
  baseurl_source: declared
  description: Keyless, CORS-open REST API serving lottery draw results as JSON and CSV across UK49s, Gosloto, SA National Lottery, and world draws. Documented by a public OpenAPI 3.0.3 spec and an llms.txt agent-na
  name: BetTip Draws API
  slug: bettip-draws-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://bettip.co.za/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bettip-draws-api-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/bettip-draws-api-packages.yml
- group: design
  title: ''
  type: Components
  url: components/bettip-draws-api-components.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bettip-draws-api-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bettip-draws-api-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/bettip-draws-api-plans-pricing.yml
- group: agent
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
overview: 'BetTip Draws API publishes 1 API on the [APIs.io](https://apis.io/) network: BetTip Draws API. Tagged areas include Lottery results, UK49s, Gosloto, SA National Lottery, and JSON.'
plans:
- name: Bettip Draws Api Plans Pricing
  plan_count: 1
  slug: bettip-draws-api-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Bettip Draws Api Rate Limits
  slug: bettip-draws-api-rate-limits
score:
  band: thin
  composite: 26.3
  coverage:
    artifact_dirs: 16
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 37.7
    developer_ergonomics: 23.2
    discoverability: 75.9
    operational_transparency: 2.6
  previous_composite: 26.3
  provenance:
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 22.2
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: authentication
  name: Bettip Draws Api Authentication
  slug: bettip-draws-api-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Bettip Draws Api Domain Security
  slug: bettip-draws-api-domain-security
  summary_line: TLSv1.3
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
- Reference data
- Open data
- Gambling & Betting
website: https://bettip.co.za/
---
