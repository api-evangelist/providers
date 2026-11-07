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
    agent_card: conformant
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
  score: 8.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for Dokimo, the cryptographic revenue platform offered by Augaster.
  name: Dokimo Service API
  slug: dokimo-service-api
artifact_total: 2
common:
- group: design
  href: https://artifacts.apis.io/augaster-com/conformance/augaster-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/augaster-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/augaster-com/a2a/augaster-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/augaster-com-a2a.yml
- group: other
  href: https://artifacts.apis.io/augaster-com/hosts/augaster-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/augaster-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/augaster-com/vendors/augaster-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/augaster-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/augaster-com/security/augaster-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/augaster-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://augaster.com/
- group: other
  title: ''
  type: Founder
  url: https://augaster.com/founder/
created: '2026-11-02'
description: Augaster provides enterprise transformation services focused on Oracle Cloud, ERP, and AI governance. They guide organizations through complex migrations, program leadership, and AI strategy, offering verifiable revenue infrastructure and AI job‑application assistance. Their offerings include Dokimo, a cryptographic revenue platform, and Rhapto, an AI‑driven recruitment tool, emphasizing transparency and compliance.
layout: provider
modified: '2026-11-02'
name: Augaster
nav: Providers
network: true
overview: Augaster is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Enterprise, Transformation, Oracle Cloud, AI Governance, and Consulting.
random_paper: 0
score:
  band: minimal
  composite: 6.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 62.5
    operational_transparency: 0.0
  previous_composite: 6.1
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Augaster Com Domain Security
  slug: augaster-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: augaster-com
tags:
- Enterprise
- Transformation
- Oracle Cloud
- AI Governance
- Consulting
website: https://augaster.com/
---
