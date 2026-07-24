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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 0.0
  scored_at: '2026-07-23'
api_count: 8
apis:
- description: Aon's Commercial Risk practice places property, casualty, financial, cyber, and specialty insurance for corporations and institutions through its global broking platform, paired with claims management
  name: Aon Risk Capital — Commercial Risk Broking
  slug: risk-capital-broking
- description: Aon's Reinsurance practice advises insurers on treaty and facultative placement, capital optimization, and analytics, marketing itself with "Delivering value for insurance industry clients with more r
  name: Aon Reinsurance Solutions
  slug: risk-capital-reinsurance
- description: Aon's Risk Analytics offering bundles named tools — Risk Analyzer suite, ReMetrica, Aon's Risk Financing Analytics, CyQu, and Spectrum — to help clients "Unlock the full potential of your risk data an
  name: Aon Risk Analytics
  slug: risk-analytics
- description: Aon's Health and Benefits practice advises employers on medical, pharmacy, wellbeing, and global benefits strategy, supported by Aon's Global Medical Trend Rates research. Delivery is consultative and
  name: Aon Human Capital — Health and Benefits
  slug: human-capital-health
- description: Aon's Wealth Solutions covers pension and retirement plan advisory, investment consulting, and delegated/OCIO investment management for plan sponsors. Engagement is consultative; no public investment-
  name: Aon Human Capital — Wealth Solutions
  slug: human-capital-wealth
- description: Aon's Talent and Rewards practice runs compensation, job architecture, pay equity, and talent assessment programs, anchored by named data products — the Radford McLagan Compensation Database, SkillsGr
  name: Aon Human Capital — Talent and Rewards
  slug: human-capital-talent
- description: NFP, acquired by Aon in April 2024 for approximately $13B, operates as an independent middle-market brokerage business inside Aon serving property and casualty, benefits, wealth, and retirement client
  name: NFP — an Aon Company
  slug: nfp
- description: Aon Insights publishes research, reports, and the "On Aon" podcast across Trade, Technology, Weather, and Workforce themes, framed by "From navigating climate change to workforce resilience, today's l
  name: Aon Insights
  slug: insights
artifact_total: 10
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
created: '2026-05-22'
description: Aon plc is a London-headquartered global professional services firm delivering integrated risk and human capital advisory through two reporting pillars — Risk Capital (broking, reinsurance, risk analytics) and Human Capital (health, wealth, talent, rewards). The firm operates in over 120 countries, lists on the NYSE under the ticker AON, and grew its US middle-market footprint with the April 2024 acquisition of NFP for roughly $13B. Aon publishes named analytics platforms (Risk Analyzer suite, ReMetrica, CyQu, Spectrum, Impact Forecasting catastrophe models, Radford McLagan Compensation Database, SkillsGraph, Gauge, Revenue GPS) but those tools are delivered through gated client portals — no developer portal, OpenAPI catalog, SDK org, or public API reference is published on aon.com.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aon.png
layout: provider
modified: '2026-05-23'
name: Aon
nav: Providers
network: true
overview: 'Aon publishes 8 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Risk, Reinsurance, Insurance, Health, and Retirement.


  Aon''s developer surface includes YouTube channel and 11 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 11.4
  delta: 2.6
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 87.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.8
  regulatory:
    applies: true
    regime: Health
    regime_id: health
    score: 26.1
  schema_version: 0.5
  scored_at: '2026-07-23'
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
