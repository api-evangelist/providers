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
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/bloki-si/llms/bloki-si-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bloki-si-llms.txt
- group: other
  href: https://artifacts.apis.io/bloki-si/hosts/bloki-si-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bloki-si-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bloki.si/en/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bloki.si/en/privacy/
- group: company
  title: ''
  type: Blog
  url: https://bloki.si/blog/
- group: auth
  href: https://artifacts.apis.io/bloki-si/security/bloki-si-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bloki-si-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bloki.si/
coverage:
  checked: '2026-11-02'
  detail: The provider’s site is a JavaScript‑rendered UI with no machine‑readable API specification.
  evidence:
  - status: 200
    url: https://bloki.si/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-02'
description: Bloki.si provides an MCP server that aggregates Slovenian public registers such as GURS, ETN, OPN, AJPES, and OSM. It offers data on buildings, parcels, real‑estate prices, surroundings, and spatial plans, enabling AI assistants like Claude to query these datasets. The service is free, open‑source, and targets developers building AI‑driven applications for Slovenian geographic and cadastral information.
image: https://bloki.si/og/sl/home.png
layout: provider
modified: '2026-11-02'
name: Bloki.si
nav: Providers
network: true
overview: 'Bloki.si is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data, Public Registers, Slovenia, and MCP.


  Bloki.si''s developer surface includes engineering blog and 6 more developer resources.'
random_paper: 2
score:
  band: minimal
  composite: 6.4
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
    developer_ergonomics: 1.2
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bloki Si Domain Security
  slug: bloki-si-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bloki-si
tags:
- Company
- Data
- Public Registers
- Slovenia
- MCP
- Open Source
website: https://bloki.si/
---
