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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/papa-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/papa-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.papa.com/blog
- group: company
  title: ''
  type: Website
  url: https://www.papa.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/papainc
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/joinpapa
- group: start
  title: ''
  type: SignUp
  url: https://www.papa.com/health-plans
created: '2026-07-03'
description: Papa is a companion care company that pairs older adults and families with vetted, trained companions called Papa Pals for social support, errands, transportation, technology help, check-ins, and everyday assistance. Papa sells to Medicare Advantage, Medicaid, Special Needs, and commercial health plans and to employers as a tech-enabled social care benefit, serving millions of members across roughly 70-100 health plan and employer partners. Members are enrolled by phone or, for employer members, online, and use the Papa Care app to request and schedule visits; Papa Pals use the Papa Pal app to accept and complete visits. Papa does not publish a public or self-serve developer API. Health plan integration is handled through business agreements - eligibility file exchange to identify and onboard eligible members, and recurring reporting dashboards covering utilization, gaps, referrals, satisfaction, and outcomes - rather than through a documented public REST API, developer portal,
  or API keys.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/papa.png
layout: provider
modified: '2026-07-03'
name: Papa
nav: Providers
network: true
overview: 'Papa is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Social Care, Companion Care, Older Adults, and Medicare Advantage.


  Papa''s developer surface includes engineering blog, signup flow, and 5 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 10.9
  delta: -3.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 13.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 13.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Papa Domain Security
  slug: papa-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Papa Trust Center
  slug: papa-trust-center
  summary_line: SOC 2, HIPAA
slug: papa
tags:
- Healthcare
- Social Care
- Companion Care
- Older Adults
- Medicare Advantage
- Medicaid
- Health Plans
- Aging
- No Public API
website: https://www.papa.com
---
