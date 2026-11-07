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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/dotstell-app/hosts/dotstell-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dotstell-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/dotstell-app/vendors/dotstell-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dotstell-app-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://dotstell.app/auth/login
- group: auth
  href: https://artifacts.apis.io/dotstell-app/security/dotstell-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dotstell-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dotstell.app/
coverage:
  checked: '2026-11-06'
  detail: The provider's website does not offer any developer documentation or public API information.
  evidence:
  - status: 200
    url: https://dotstell.app/
  reason: no-developer-program
  state: none
created: '2026-11-05'
description: 'dotstell-app is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-11-05'
name: dotstell-app
nav: Providers
network: true
overview: dotstell-app is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Knowledge Graph, Personal Knowledge Management, Productivity, Note Taking, and AI Integration.
random_paper: 17
score:
  band: minimal
  composite: 4.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 35.7
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
  name: Dotstell App Domain Security
  slug: dotstell-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dotstell-app
tags:
- Knowledge Graph
- Personal Knowledge Management
- Productivity
- Note Taking
- AI Integration
website: https://dotstell.app/
---
