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
  href: https://artifacts.apis.io/cargovox-com/llms/cargovox-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cargovox-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/cargovox-com/well-known/cargovox-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cargovox-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/cargovox-com/hosts/cargovox-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cargovox-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/cargovox-com/vendors/cargovox-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cargovox-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/cargovox-com/security/cargovox-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cargovox-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cargovox.com/
coverage:
  checked: '2026-11-03'
  detail: No public API documentation or machine-readable contract was found on the provider's hosts.
  evidence:
  - status: 0
    url: https://api.cargovox.com/
  reason: no-developer-program
  state: none
created: '2026-11-03'
description: Coservices OU offers CargoVox, an AI phone agent for transport, logistics, and moving companies. It provides 24/7 call answering, automatic language detection, price calculation, lead capture, and integrates via webhooks or CRM. The service aims to reduce missed calls and dispatcher costs while delivering instant quotes and multilingual support across Europe.
layout: provider
modified: '2026-11-03'
name: Coservices OU
nav: Providers
network: true
overview: Coservices OU is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include AI Phone Agent, Transport, Logistics, Moving Services, and CRM Integration.
random_paper: 13
score:
  band: minimal
  composite: 3.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: derived
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
  name: Cargovox Com Domain Security
  slug: cargovox-com-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: cargovox-com
tags:
- AI Phone Agent
- Transport
- Logistics
- Moving Services
- CRM Integration
- Lead Capture
website: https://cargovox.com/
---
