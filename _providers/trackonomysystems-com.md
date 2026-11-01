---
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
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://artifacts.apis.io/trackonomysystems-com/security/trackonomysystems-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/trackonomysystems-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://trackonomy.ai
- group: docs
  title: ''
  type: Documentation
  url: https://trackonomy.ai/platform/
- group: start
  title: ''
  type: GettingStarted
  url: https://trackonomy.ai/request-demo/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://trackonomy.ai/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://trackonomy.ai/terms-of-use/
coverage:
  checked: '2026-10-25'
  detail: Platform page requires reCAPTCHA, preventing automated spec discovery.
  evidence:
  - status: 200
    url: https://trackonomy.ai/platform/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-25'
description: Trackonomy provides smart label technology for supply chain visibility, enabling real‑time tracking, predictive maintenance, and workflow optimization across industries. Their platform connects devices, sensors, and data streams to deliver actionable insights, improve asset protection, and streamline logistics operations. Backed by 8vc, Trackonomy serves enterprises seeking to digitize and secure their supply chain.
layout: provider
modified: '2026-10-25'
name: Trackonomy
nav: Providers
network: true
overview: 'Trackonomy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Supply-Chain, IoT, Smart-Labels, and Real-Time-Tracking.


  Trackonomy''s developer surface includes documentation, getting-started guide, and 4 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 12.8
  coverage:
    artifact_dirs: 4
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Trackonomysystems Com Domain Security
  slug: trackonomysystems-com-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: trackonomysystems-com
tags:
- Company
- Supply-Chain
- IoT
- Smart-Labels
- Real-Time-Tracking
- Predictive-Maintenance
website: https://trackonomy.ai
---
