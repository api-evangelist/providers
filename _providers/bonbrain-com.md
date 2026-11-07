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
  score: 18.7
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/bonbrain-com/well-known/bonbrain-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bonbrain-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/bonbrain-com/hosts/bonbrain-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bonbrain-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/bonbrain-com/vendors/bonbrain-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bonbrain-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bonbrain.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bonbrain.com/privacy-policy
- group: auth
  href: https://artifacts.apis.io/bonbrain-com/security/bonbrain-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bonbrain-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bonbrain.com/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://mcp.bonbrain.com/mcp
  - status: 401
    url: https://mcp.bonbrain.com/api/graphql
  - status: 200
    url: https://bonbrain.com/
  reason: partner-login
  state: gated
created: '2026-11-02'
description: Bonbrain LLC builds AI‑powered mobile applications that transform everyday tasks into seamless digital experiences. Their product suite includes BonPic, an AI photo generator; Pantry Buddy, an AI grocery‑list manager; Proof Buddy, a timestamped photo service for insurance and verification; Decora AI, an interior‑design assistant; and Fast Cleanup, an AI duplicate‑photo remover. The company emphasizes robust engineering, scalable architecture, and a focus on delivering magical, reliable user experiences across its AI‑driven apps.
layout: provider
modified: '2026-11-02'
name: Bonbrain
nav: Providers
network: true
overview: Bonbrain is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Mobile, Photography, Grocery, and Interior Design.
random_paper: 7
score:
  band: minimal
  composite: 6.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
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
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bonbrain Com Domain Security
  slug: bonbrain-com-domain-security
  summary_line: TLSv1.3
slug: bonbrain-com
tags:
- Artificial Intelligence
- Mobile
- Photography
- Grocery
- Interior Design
website: https://bonbrain.com/
---
