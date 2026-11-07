---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: AutoIsto shromažďuje inzeráty aut z českých autobazarů na jedno místo. AI ti najde přesně to auto, které hledáš.
  name: AutoIsto API
  slug: autoisto-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/autoisto-cz/llms/autoisto-cz-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/autoisto-cz-llms.txt
- group: other
  href: https://artifacts.apis.io/autoisto-cz/hosts/autoisto-cz-hosts.yml
  title: ''
  type: Hosts
  url: hosts/autoisto-cz-hosts.yml
- group: other
  href: https://artifacts.apis.io/autoisto-cz/vendors/autoisto-cz-vendors.yml
  title: ''
  type: Vendors
  url: vendors/autoisto-cz-vendors.yml
- group: auth
  href: https://artifacts.apis.io/autoisto-cz/security/autoisto-cz-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/autoisto-cz-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.autoisto.cz/
coverage:
  checked: '2026-11-02'
  detail: Main site renders with JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://www.autoisto.cz/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-02'
description: AutoIsto shromažďuje inzeráty aut z českých autobazarů na jedno místo. AI ti najde přesně to auto, které hledáš. Vyhledávač ojetých aut z českých autobazarů na jednom místě, s hodnocením ceny oproti srovnatelným autům. Poskytuje detailní informace, fotky a historii vozidel, usnadňuje výběr a nákup.
image: https://www.autoisto.cz/_next/image?url=%2Flogo.png&w=3840&q=75
layout: provider
modified: '2026-11-02'
name: AutoIsto
nav: Providers
network: true
overview: AutoIsto is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Automotive, Marketplace, Search, and Czech.
random_paper: 2
score:
  band: minimal
  composite: 4.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 4.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Autoisto Cz Domain Security
  slug: autoisto-cz-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: autoisto-cz
tags:
- Company
- Automotive
- Marketplace
- Search
- Czech
website: https://www.autoisto.cz/
---
