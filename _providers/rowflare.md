---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Read and write records in a Rowflare instance via the self‑hosted or cloud‑hosted service.
  name: Rowflare REST API
  slug: rowflare-rest-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/rowflare/plans/rowflare-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/rowflare-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/rowflare/vocabulary/rowflare-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/rowflare-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/rowflare/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/rowflare/conformance/rowflare-conformance.yml
  title: ''
  type: Conformance
  url: conformance/rowflare-conformance.yml
- group: agent
  href: https://artifacts.apis.io/rowflare/llms/rowflare-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/rowflare-llms.txt
- group: other
  href: https://artifacts.apis.io/rowflare/hosts/rowflare-hosts.yml
  title: ''
  type: Hosts
  url: hosts/rowflare-hosts.yml
- group: other
  href: https://artifacts.apis.io/rowflare/vendors/rowflare-vendors.yml
  title: ''
  type: Vendors
  url: vendors/rowflare-vendors.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://rowflare.com/pricing/
- group: docs
  title: ''
  type: Documentation
  url: https://rowflare.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://rowflare.com/docs/api/
- group: auth
  href: https://artifacts.apis.io/rowflare/security/rowflare-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rowflare-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://rowflare.com
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://rowflare.com/openapi.json
  - status: 401
    url: https://app.rowflare.com/mcp
  - status: 200
    url: https://rowflare.com
  reason: partner-login
  state: gated
created: '2026-10-22'
description: Rowflare provides an open-source, self‑hosted Airtable‑like platform built on Cloudflare Workers. It offers a collaborative spreadsheet database with a modern UI, API access, and flexible pricing at $5 per month for a team, positioning itself as a cost‑effective alternative to Airtable for developers and organizations seeking on‑premise control.
image: https://rowflare.com/og.png
layout: provider
modified: '2026-10-22'
name: Rowflare
nav: Providers
network: true
overview: 'Rowflare is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Airtable, Open Source, Cloudflare, and Collaboration.


  Rowflare''s developer surface includes pricing, documentation, API reference, and 9 more developer resources.'
plans:
- name: Rowflare Plans Pricing
  plan_count: 2
  slug: rowflare-plans-pricing
random_paper: 2
score:
  band: emerging
  composite: 15.9
  coverage:
    artifact_dirs: 15
    catalog_earned: 46.3
    catalog_earned_first_party: 8.0
    catalog_gap: 68.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.7
  facets:
    access_clarity: 26.3
    contract_governance: 8.3
    contract_quality: 0.0
    developer_ergonomics: 14.8
    discoverability: 73.2
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 18.6
  provenance:
    conformance: derived
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/rowflare/rowflare-2026-11-03T142439.png
security:
- kind: domain-security
  name: Rowflare Domain Security
  slug: rowflare-domain-security
  summary_line: TLSv1.3 · DMARC
slug: rowflare
tags:
- Company
- Airtable
- Open Source
- Cloudflare
- Collaboration
website: https://rowflare.com
---
