---
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
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.5
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/aechelon-technology/llms/aechelon-technology-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aechelon-technology-llms.txt
- group: agent
  href: https://artifacts.apis.io/aechelon-technology/well-known/aechelon-technology-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aechelon-technology-well-known.yml
- group: other
  href: https://artifacts.apis.io/aechelon-technology/hosts/aechelon-technology-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aechelon-technology-hosts.yml
- group: other
  href: https://artifacts.apis.io/aechelon-technology/vendors/aechelon-technology-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aechelon-technology-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.shield.ai/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://shield.ai/privacy/
- group: company
  title: ''
  type: Newsroom
  url: https://shield.ai/newsroom/
- group: auth
  href: https://artifacts.apis.io/aechelon-technology/security/aechelon-technology-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aechelon-technology-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.aechelon.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: http://www.aechelon.com
  reason: no-developer-program
  state: none
created: '2026-10-26'
description: Aechelon Technology provides high-fidelity visual and sensor simulation platforms that prepare pilots, operators, and autonomous systems for real-world missions across every domain. Their solutions enable synthetic reality, flight simulation training, geo-specific visualization, and AI/ML machine training, delivering immersive training environments for defense and commercial aviation.
image: https://shield.ai/wp-content/uploads/2025/03/ogp.jpg
layout: provider
modified: '2026-10-26'
name: Aechelon Technology
nav: Providers
network: true
overview: Aechelon Technology is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Simulation, AI, Aviation, Defense, and Visualization.
random_paper: 16
score:
  band: minimal
  composite: 9.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 18.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aechelon Technology Domain Security
  slug: aechelon-technology-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aechelon-technology
tags:
- Simulation
- AI
- Aviation
- Defense
- Visualization
website: http://www.aechelon.com
---
