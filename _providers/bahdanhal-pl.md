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
    mcp_server: false
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
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Security
  url: https://bahdanhal.pl/services
- group: agent
  href: https://artifacts.apis.io/bahdanhal-pl/llms/bahdanhal-pl-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bahdanhal-pl-llms.txt
- group: auth
  href: https://artifacts.apis.io/bahdanhal-pl/well-known/bahdanhal-pl-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bahdanhal-pl-security.txt
- group: agent
  href: https://artifacts.apis.io/bahdanhal-pl/well-known/bahdanhal-pl-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bahdanhal-pl-well-known.yml
- group: other
  href: https://artifacts.apis.io/bahdanhal-pl/hosts/bahdanhal-pl-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bahdanhal-pl-hosts.yml
- group: other
  href: https://artifacts.apis.io/bahdanhal-pl/vendors/bahdanhal-pl-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bahdanhal-pl-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bahdanhal
- group: auth
  href: https://artifacts.apis.io/bahdanhal-pl/security/bahdanhal-pl-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bahdanhal-pl-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/bahdanhal-pl/security/bahdanhal-pl-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bahdanhal-pl-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bahdanhal.pl/
coverage:
  checked: '2026-11-02'
  detail: The provider is an individual engineer with no software product offering an API.
  evidence:
  - status: 200
    url: https://bahdanhal.pl/
  reason: not-a-software-company
  state: none
created: '2026-11-02'
description: Bahdan Hal is a senior backend engineer based in Gdańsk, Poland, specializing in Symfony, Laravel, Linux, and AI integrations. He shares his personal story, professional experience, and ecosystem products, having worked on telecommunications backends and educational platforms at Freedom Mobile, GWO, and Manao-dev. He owns product vision, software architecture, infrastructure, and day‑to‑day operations for live production platforms.
image: https://bahdanhal.pl/og-image.jpg
layout: provider
modified: '2026-11-02'
name: Bahdan Hal
nav: Providers
network: true
overview: Bahdan Hal is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Backend, Engineer, Symfony, Laravel, and Artificial Intelligence.
random_paper: 4
score:
  band: minimal
  composite: 5.2
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - poland
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - cee
    - europe
  previous_composite: 6.2
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bahdanhal Pl Domain Security
  slug: bahdanhal-pl-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Bahdanhal Pl Vulnerability Disclosure
  slug: bahdanhal-pl-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bahdanhal-pl
tags:
- Backend
- Engineer
- Symfony
- Laravel
- Artificial Intelligence
- Poland
website: https://bahdanhal.pl/
---
