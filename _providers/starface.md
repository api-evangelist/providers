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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/starface/llms/starface-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/starface-llms.txt
- group: agent
  href: https://artifacts.apis.io/starface/well-known/starface-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/starface-well-known.yml
- group: other
  href: https://artifacts.apis.io/starface/hosts/starface-hosts.yml
  title: ''
  type: Hosts
  url: hosts/starface-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://starface.com/en/terms-conditions/
- group: start
  title: ''
  type: Login
  url: https://starface.com/login/
- group: company
  title: ''
  type: Blog
  url: https://starface.com/blog/
- group: auth
  href: https://artifacts.apis.io/starface/security/starface-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/starface-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://starface.com/
coverage:
  checked: '2026-10-26'
  detail: Developer documentation at https://starface.com/developer/ is heavily JavaScript‑rendered and provides no machine‑readable spec.
  evidence:
  - status: 200
    url: https://starface.com/developer/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-26'
description: STARFACE provides unified communication solutions, offering a comprehensive IP‑based phone system that integrates voice, video, chat, and collaboration tools for businesses of all sizes. Their platform supports on‑premises, cloud, and hybrid deployments, featuring advanced call routing, voicemail, conferencing, and integration with CRM and ERP systems. STARFACE focuses on security, scalability, and ease of management, delivering a modern unified communications experience.
layout: provider
modified: '2026-10-26'
name: STARFACE
nav: Providers
network: true
overview: 'STARFACE is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Communications, Unified Communications, and VoIP.


  STARFACE''s developer surface includes engineering blog and 7 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 6.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.8
  facets:
    access_clarity: 11.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 42.9
    operational_transparency: 0.0
  previous_composite: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/starface/starface-2026-11-03T143739.png
security:
- kind: domain-security
  name: Starface Domain Security
  slug: starface-domain-security
  summary_line: TLSv1.3 · DMARC
slug: starface
tags:
- Company
- Communications
- Unified Communications
- VoIP
website: https://starface.com/
---
