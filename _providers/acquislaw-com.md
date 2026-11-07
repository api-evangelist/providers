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
    agent_skills: unknown
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
    mcp_server: false
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
  score: 21.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API providing access to verified EU law content for AI assistants.
  name: AcquisLaw API
  slug: acquislaw-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/acquislaw-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/acquislaw-com/well-known/acquislaw-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/acquislaw-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/acquislaw-com/hosts/acquislaw-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/acquislaw-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/acquislaw-com/security/acquislaw-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/acquislaw-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://acquislaw.com/
- group: docs
  title: ''
  type: Documentation
  url: https://acquislaw.com/docs
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://acquislaw.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://acquislaw.com/terms
coverage:
  checked: '2026-10-31'
  detail: Documentation exists but provides no machine‑readable API specification.
  evidence:
  - status: 200
    url: https://acquislaw.com/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: Acquis provides verified EU law content inside AI assistants, offering real-time answers to legal questions with citations to official EU regulations. The platform supports the AI Act, Cyber Resilience Act, GDPR and other regulations, delivering verbatim provisions, cryptographic verification, and plain‑language explanations. Users can trial the service for free, then choose Basic or Pro plans for ongoing access.
image: https://acquislaw.com/opengraph-image.png?e3a2047ceba065c0
layout: provider
modified: '2026-10-31'
name: Acquis
nav: Providers
network: true
overview: 'Acquis is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Legal Tech, EU Law, and Software-as-a-Service.


  Acquis'' developer surface includes documentation and 7 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 10.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.6
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.2
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 13.6
  provenance:
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Acquislaw Com Domain Security
  slug: acquislaw-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: acquislaw-com
tags:
- Company
- Artificial Intelligence
- Legal Tech
- EU Law
- Software-as-a-Service
website: https://acquislaw.com/
---
