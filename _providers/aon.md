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
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: Aon Insights publishes research, reports, and the "On Aon" podcast across Trade, Technology, Weather, and Workforce themes, framed by "From navigating climate change to workforce resilience, today's l
  name: Aon Insights
  slug: insights
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/aon-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aon-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aon.com
- group: company
  title: ''
  type: About
  url: https://www.aon.com/en/about
- group: company
  title: ''
  type: InvestorRelations
  url: https://ir.aon.com
- group: company
  title: ''
  type: Newsroom
  url: https://www.aon.com/en/about/newsroom
- group: other
  title: ''
  type: Insights
  url: https://www.aon.com/en/insights
- group: company
  title: ''
  type: Careers
  url: https://www.aon.com/en/about/careers
- group: operate
  title: ''
  type: Contact
  url: https://www.aon.com/en/contact
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aon
- group: other
  title: ''
  type: X
  url: https://twitter.com/Aon_plc
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/Aonplc
- group: operate
  title: ''
  type: Contact
  url: https://www.aon.com/en/capabilities/reinsurance
- group: operate
  title: ''
  type: Contact
  url: https://www.aon.com/en/capabilities/risk-analytics
- group: operate
  title: ''
  type: Contact
  url: https://www.aon.com/en/capabilities/health-and-benefits
- group: company
  title: ''
  type: Careers
  url: https://www.aon.com/en/capabilities/talent-and-rewards
- group: company
  title: ''
  type: About
  url: https://www.nfp.com
created: '2026-05-22'
description: Aon plc is a London-headquartered global professional services firm delivering integrated risk and human capital advisory through two reporting pillars — Risk Capital (broking, reinsurance, risk analytics) and Human Capital (health, wealth, talent, rewards). The firm operates in over 120 countries, lists on the NYSE under the ticker AON, and grew its US middle-market footprint with the April 2024 acquisition of NFP for roughly $13B. Aon publishes named analytics platforms (Risk Analyzer suite, ReMetrica, CyQu, Spectrum, Impact Forecasting catastrophe models, Radford McLagan Compensation Database, SkillsGraph, Gauge, Revenue GPS) but those tools are delivered through gated client portals — no developer portal, OpenAPI catalog, SDK org, or public API reference is published on aon.com.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aon.png
layout: provider
modified: '2026-07-25'
name: Aon
nav: Providers
network: true
overview: 'Aon publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Risk, Reinsurance, Insurance, Health, and Retirement.


  Aon''s developer surface includes YouTube channel and 16 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 6.5
  coverage:
    artifact_dirs: 2
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 18.2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aon/refs/heads/main/screenshots/aon-2026-06-20T172037.png
security:
- kind: domain-security
  name: Aon Domain Security
  slug: aon-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aon Vulnerability Disclosure
  slug: aon-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: aon
tags:
- Risk
- Reinsurance
- Insurance
- Health
- Retirement
- Talent
- Analytics
- Professional Services
website: https://www.aon.com
---
