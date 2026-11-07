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
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/bottletech-net/security/bottletech-net-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/bottletech-net-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/bottletech-net/llms/bottletech-net-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bottletech-net-llms.txt
- group: auth
  href: https://artifacts.apis.io/bottletech-net/well-known/bottletech-net-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bottletech-net-security.txt
- group: agent
  href: https://artifacts.apis.io/bottletech-net/well-known/bottletech-net-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bottletech-net-well-known.yml
- group: other
  href: https://artifacts.apis.io/bottletech-net/hosts/bottletech-net-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bottletech-net-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://bottletech.net/press
- group: auth
  href: https://artifacts.apis.io/bottletech-net/security/bottletech-net-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bottletech-net-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/bottletech-net/security/bottletech-net-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bottletech-net-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bottletech.net/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bottletech.net/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bottletech.net/terms
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://bottletech.net/
  reason: no-developer-program
  state: none
created: '2026-11-02'
description: BottleTech is an Amman‑based technology company delivering AI‑driven automation, business systems and custom software solutions across Saudi Arabia, the UAE and Jordan. Their services span WhatsApp automation, CRM and POS integration, helping enterprises streamline operations and accelerate digital transformation.
image: https://bottletech.net/og.png
layout: provider
modified: '2026-11-02'
name: BottleTech
nav: Providers
network: true
overview: BottleTech is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Automation, Software, and Middle East.
random_paper: 2
score:
  band: minimal
  composite: 8.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 49.1
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bottletech Net Domain Security
  slug: bottletech-net-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Bottletech Net Vulnerability Disclosure
  slug: bottletech-net-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bottletech-net
tags:
- Company
- Artificial Intelligence
- Automation
- Software
- Middle East
website: https://bottletech.net/
---
