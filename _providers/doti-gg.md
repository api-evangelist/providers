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
    mcp_server: documented
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
  score: 21.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for D0T1 content creation platform (no public contract discovered)
  name: D0T1 API
  slug: d0t1-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/doti-gg/llms/doti-gg-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/doti-gg-llms.txt
- group: auth
  href: https://artifacts.apis.io/doti-gg/well-known/doti-gg-otto-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/doti-gg-otto-security.txt
- group: agent
  href: https://artifacts.apis.io/doti-gg/well-known/doti-gg-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/doti-gg-well-known.yml
- group: other
  href: https://artifacts.apis.io/doti-gg/hosts/doti-gg-hosts.yml
  title: ''
  type: Hosts
  url: hosts/doti-gg-hosts.yml
- group: other
  href: https://artifacts.apis.io/doti-gg/vendors/doti-gg-vendors.yml
  title: ''
  type: Vendors
  url: vendors/doti-gg-vendors.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.doti.gg/
- group: auth
  href: https://artifacts.apis.io/doti-gg/security/doti-gg-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/doti-gg-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://doti.gg/
created: '2026-11-05'
description: D0T1 (doti.gg) offers automated content creation services, providing research, creation, publishing, and conversion tools that run daily without human recording. The platform targets marketers and creators seeking AI‑driven content generation, with a focus on scalability and ease of use.
image: https://doti.gg/assets/hero-central-viral-v3.webp
layout: provider
modified: '2026-11-05'
name: D0T1
nav: Providers
network: true
overview: D0T1 is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Content Generation, Automation, and Marketing.
random_paper: 11
score:
  band: minimal
  composite: 8.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 57.1
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Doti Gg Domain Security
  slug: doti-gg-domain-security
  summary_line: TLSv1.3 · DMARC
slug: doti-gg
tags:
- Company
- Artificial Intelligence
- Content Generation
- Automation
- Marketing
website: https://doti.gg/
---
