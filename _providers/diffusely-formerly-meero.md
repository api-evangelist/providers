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
    well_known_catalog: true
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/diffusely-formerly-meero/well-known/diffusely-formerly-meero-clarity-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/diffusely-formerly-meero-clarity-security.txt
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.carcutter.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.carcutter.com/privacy-policy/
- group: agent
  href: https://artifacts.apis.io/diffusely-formerly-meero/llms/diffusely-formerly-meero-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/diffusely-formerly-meero-llms.txt
- group: agent
  href: https://artifacts.apis.io/diffusely-formerly-meero/well-known/diffusely-formerly-meero-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/diffusely-formerly-meero-well-known.yml
- group: auth
  title: ''
  type: Security
  url: https://clarity.com/vdp
- group: other
  href: https://artifacts.apis.io/diffusely-formerly-meero/hosts/diffusely-formerly-meero-hosts.yml
  title: ''
  type: Hosts
  url: hosts/diffusely-formerly-meero-hosts.yml
- group: auth
  href: https://artifacts.apis.io/diffusely-formerly-meero/security/diffusely-formerly-meero-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/diffusely-formerly-meero-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/diffusely-formerly-meero/security/diffusely-formerly-meero-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/diffusely-formerly-meero-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.carcutter.com/
coverage:
  checked: '2026-10-23'
  detail: The provider's site https://diffusely.ai returns a JavaScript shell with no machine‑readable API documentation.
  evidence:
  - status: 200
    url: https://diffusely.ai
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-23'
description: Diffusely (formerly Meero) is an AI‑native media and content platform that enables creators and brands to generate, manage, and distribute visual assets at scale. Leveraging advanced generative AI, the company offers tools for image creation, video production, and asset management, positioning itself as a modern solution for media workflows. The firm emerged from Meero’s rebranding and continues to serve the digital content market with innovative AI capabilities.
layout: provider
modified: '2026-10-23'
name: Diffusely Formerly Meero
nav: Providers
network: true
overview: Diffusely Formerly Meero is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Media, Content, Generative AI, and Platform.
random_paper: 5
score:
  band: minimal
  composite: 10.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 4.6
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 51.8
    operational_transparency: 5.3
  previous_composite: 6.3
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 23.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/diffusely-formerly-meero/diffusely-formerly-meero-2026-11-03T130648.png
security:
- kind: domain-security
  name: Diffusely Formerly Meero Domain Security
  slug: diffusely-formerly-meero-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Diffusely Formerly Meero Vulnerability Disclosure
  slug: diffusely-formerly-meero-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: diffusely-formerly-meero
tags:
- Artificial Intelligence
- Media
- Content
- Generative AI
- Platform
- Company
website: https://www.carcutter.com/
---
