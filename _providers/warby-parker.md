---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.warbyparker.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/WarbyParker
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/warby-parker-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/warby-parker-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/warby-parker-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/warby-parker-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.warbyparker.com/.well-known/security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/warby-parker-domain-security.yml
created: '2026-07-17'
description: 'Warby Parker (NYSE: WRBY) is a direct-to-consumer eyewear and vision care company founded in 2010, selling prescription eyeglasses, sunglasses, contact lenses, and eye exams online and across 900+ retail stores. It operates a headless, modular commerce architecture and a proprietary point-of-sale system (Point of Everything), plus consumer-facing tools like Virtual Vision Test and PD measurement. Warby Parker does not publish a public developer API or developer portal; its API surface (api.warbyparker.com) is internal. The company does publish a public llms.txt for AI agents and an RFC 9116 security.txt with a bug-bounty contact. This API Evangelist profile captures that agent-facing and security posture; there is no OpenAPI/AsyncAPI or SDK surface to harvest.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/warby-parker.png
layout: provider
modified: '2026-07-21'
name: Warby Parker
nav: Providers
network: true
overview: Warby Parker is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Eyewear, Retail, and E-Commerce.
random_paper: 0
score:
  band: minimal
  composite: 7.5
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 7.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/warby-parker/refs/heads/main/screenshots/warby-parker-2026-09-02T170438.png
security:
- kind: domain-security
  name: Warby Parker Domain Security
  slug: warby-parker-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Warby Parker Vulnerability Disclosure
  slug: warby-parker-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: warby-parker
tags:
- Company
- Consumer
- Eyewear
- Retail
- E-Commerce
- Vision Care
- Optical
- Direct to Consumer
website: https://www.warbyparker.com
---
