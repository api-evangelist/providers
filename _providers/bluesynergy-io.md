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
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/bluesynergy-io/well-known/bluesynergy-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bluesynergy-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/bluesynergy-io/hosts/bluesynergy-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bluesynergy-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/bluesynergy-io/vendors/bluesynergy-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bluesynergy-io-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bluesynergy.io/terms.html
- group: auth
  href: https://artifacts.apis.io/bluesynergy-io/security/bluesynergy-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bluesynergy-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bluesynergy.io/
coverage:
  checked: '2026-11-02'
  detail: Bluesynergy.io provides no public developer documentation or API specifications.
  evidence:
  - status: 200
    url: https://bluesynergy.io/
  reason: no-developer-program
  state: none
created: '2026-11-02'
description: Blue Synergy provides advanced AI enterprise solutions, bridging deterministic software architecture, regulated laboratory rigor, and enterprise AI orchestration. Their platform enables zero‑tolerance environments with robust, scalable services for regulated industries, offering customizable integrations and secure data pipelines.
image: https://www.bluesynergy.io/og-image.webp
layout: provider
modified: '2026-11-02'
name: Blue Synergy
nav: Providers
network: true
overview: Blue Synergy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Enterprise AI, AI Integration, Workflow Orchestration, Private RAG, and MedTech AI.
random_paper: 6
score:
  band: minimal
  composite: 4.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bluesynergy Io Domain Security
  slug: bluesynergy-io-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bluesynergy-io
tags:
- Enterprise AI
- AI Integration
- Workflow Orchestration
- Private RAG
- MedTech AI
- SaaS Platform
website: https://bluesynergy.io/
---
