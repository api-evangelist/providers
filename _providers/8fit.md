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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 6.3
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/8fit-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/8fit-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/8fit-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/8fit-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/8fit-security.txt
- group: company
  title: ''
  type: Website
  url: https://8fit.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://8fit.zendesk.com/hc/en-us
- group: operate
  title: ''
  type: Support
  url: https://8fit.zendesk.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://8fit.com/articles/
- group: start
  title: ''
  type: SignUp
  url: https://8fit.com/signup/
- group: start
  title: ''
  type: Login
  url: https://8fit.com/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://8fit.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://8fit.com/privacy/
created: '2026-07-17'
description: 8fit is a consumer health and fitness application offering personalized home workout programs (HIIT, boxing, Pilates, yoga, and meditation), custom healthy meal and nutrition plans, and holistic wellness guidance built around sustainable habit-building rather than quick fixes. Founded in Berlin and surfaced in the API Evangelist network as a portfolio company of Creandum, 8fit reached more than 40 million downloads before being acquired by Withings (a Gilde Healthcare portfolio company) in February 2022. Withings announced the discontinuation of the standalone 8fit app effective June 26, 2026, folding its nutrition and activity content into the Withings app and Withings+ service. 8fit is a mobile/web consumer app and does not publish a public developer API; this profile captures its public web, security, and identity surface.
image: https://images.ctfassets.net/90pc6zknij8o/QKISIkVdSR3h8d2wmF2tc/62dc9226c81562cffdd0a4418fe69904/web_link_image.png
layout: provider
modified: '2026-07-17'
name: 8fit
nav: Providers
network: true
overview: '8fit is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Fitness, Health, and Wellness.


  8fit''s developer surface includes support, engineering blog, signup flow, and 10 more developer resources.'
random_paper: 51
score:
  band: emerging
  composite: 17.0
  delta: -3.3
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 61.1
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 20.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 25.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/8fit/refs/heads/main/screenshots/8fit-2026-07-25T181241.png
security:
- kind: domain-security
  name: 8Fit Domain Security
  slug: 8fit-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: 8Fit Vulnerability Disclosure
  slug: 8fit-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: 8fit
tags:
- Company
- Consumer
- Fitness
- Health
- Wellness
- Nutrition
- Mobile App
website: https://8fit.com/
---
