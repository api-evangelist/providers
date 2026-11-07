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
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/bridgeaibrasil-com-br/llms/bridgeaibrasil-com-br-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bridgeaibrasil-com-br-llms.txt
- group: other
  href: https://artifacts.apis.io/bridgeaibrasil-com-br/hosts/bridgeaibrasil-com-br-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bridgeaibrasil-com-br-hosts.yml
- group: other
  href: https://artifacts.apis.io/bridgeaibrasil-com-br/vendors/bridgeaibrasil-com-br-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bridgeaibrasil-com-br-vendors.yml
- group: auth
  href: https://artifacts.apis.io/bridgeaibrasil-com-br/security/bridgeaibrasil-com-br-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bridgeaibrasil-com-br-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bridgeaibrasil.com.br/
coverage:
  checked: '2026-11-03'
  detail: No machine‑readable API specification was discovered on any host.
  evidence:
  - status: 200
    url: https://painel.bridgeaibrasil.com.br/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: 'bridgeaibrasil-com-br is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
image: https://bridgeaibrasil.com.br/og.png?v=2026-09-22-21c82ed
layout: provider
modified: '2026-11-03'
name: bridgeaibrasil-com-br
nav: Providers
network: true
overview: bridgeaibrasil-com-br is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 17
score:
  band: minimal
  composite: 1.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 17.0
    catalog_earned_first_party: 0.0
    catalog_gap: 98.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 30.4
    operational_transparency: 0.0
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
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bridgeaibrasil Com Br Domain Security
  slug: bridgeaibrasil-com-br-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bridgeaibrasil-com-br
tags:
- Company
website: https://bridgeaibrasil.com.br/
---
