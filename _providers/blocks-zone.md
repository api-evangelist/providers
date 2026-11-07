---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/blocks-zone/plans/blocks-zone-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/blocks-zone-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/blocks-zone/llms/blocks-zone-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/blocks-zone-llms.txt
- group: agent
  href: https://artifacts.apis.io/blocks-zone/well-known/blocks-zone-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/blocks-zone-well-known.yml
- group: other
  href: https://artifacts.apis.io/blocks-zone/hosts/blocks-zone-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blocks-zone-hosts.yml
- group: other
  href: https://artifacts.apis.io/blocks-zone/vendors/blocks-zone-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blocks-zone-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://blocks.zone/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://blocks.zone/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://blocks.zone/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://blocks.zone/guides/tp2intervals
- group: auth
  href: https://artifacts.apis.io/blocks-zone/security/blocks-zone-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blocks-zone-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://blocks.zone/
coverage:
  checked: '2026-11-02'
  detail: No machine‑readable API contract was found despite public documentation pages.
  evidence:
  - status: 200
    url: https://blocks.zone/guides/tp2intervals
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Blocks is an AI‑native training platform for endurance athletes. It lets you build and visualise structured intervals, sync every ride, and train with an assistant that reads your real data – cycling, running, swimming and strength. The service offers a free tier and premium plans, integrates with Strava and intervals.icu, and provides an MCP server for Claude and other AI agents.
image: https://blocks.zone/opengraph-image?bd6507f543e545a8
layout: provider
modified: '2026-11-02'
name: Blocks
nav: Providers
network: true
overview: 'Blocks is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Fitness, Training, Health Tech, and Endurance.


  Blocks'' developer surface includes pricing, documentation, and 9 more developer resources.'
plans:
- name: Blocks Zone Plans Pricing
  plan_count: 1
  slug: blocks-zone-plans-pricing
random_paper: 23
score:
  band: emerging
  composite: 13.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Blocks Zone Domain Security
  slug: blocks-zone-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: blocks-zone
tags:
- Artificial Intelligence
- Fitness
- Training
- Health Tech
- Endurance
website: https://blocks.zone/
---
