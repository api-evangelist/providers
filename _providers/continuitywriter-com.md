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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.7
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/continuitywriter-com/llms/continuitywriter-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/continuitywriter-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/continuitywriter-com/well-known/continuitywriter-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/continuitywriter-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/continuitywriter-com/hosts/continuitywriter-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/continuitywriter-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/continuitywriter-com/vendors/continuitywriter-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/continuitywriter-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://continuitywriter.com/terms
- group: operate
  title: ''
  type: Support
  url: https://continuitywriter.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://continuitywriter.com/privacy
- group: auth
  href: https://artifacts.apis.io/continuitywriter-com/security/continuitywriter-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/continuitywriter-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://continuitywriter.com/
coverage:
  checked: '2026-11-04'
  detail: Continuitywriter.com provides a story bible platform without a public API contract.
  evidence:
  - status: 200
    url: https://continuitywriter.com/
  reason: not-a-software-company
  state: none
created: '2026-11-04'
description: Continuity by Ouroboros Apps offers a story bible platform for AI assistants like ChatGPT, Claude, Gemini, and others. It lets writers maintain private canon for characters, worlds, and narratives, ensuring consistency across sessions. Users can connect their AI assistants to the service, manage subscriptions via Stripe, and access tools hosted on Vercel and Supabase. The platform emphasizes privacy, with detailed policies and support resources.
image: https://continuitywriter.com/logo.jpg
layout: provider
modified: '2026-11-04'
name: Continuity by Ouroboros Apps
nav: Providers
network: true
overview: 'Continuity by Ouroboros Apps is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Storytelling, Writing, Software-as-a-Service, and Continuity.


  Continuity by Ouroboros Apps'' developer surface includes support and 8 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 9.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Continuitywriter Com Domain Security
  slug: continuitywriter-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: continuitywriter-com
tags:
- Artificial Intelligence
- Storytelling
- Writing
- Software-as-a-Service
- Continuity
- Platform
website: https://continuitywriter.com/
---
