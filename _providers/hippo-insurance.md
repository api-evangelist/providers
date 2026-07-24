---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
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
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-23'
api_count: 4
apis:
- description: Direct-to-consumer homeowners quote, bind, and policy management. Quotes delivered in under 60 seconds. No public API; carrier partnerships are managed via First Connect.
  name: Hippo Consumer Quote & Bind
  slug: hippo-consumer
- description: Hippo Home is the consumer smart-home companion app for iOS and Android. Provides DIY maintenance checklists, seasonal guidance, and a home health score. No public API; integrations are sales-led.
  name: Hippo Home App
  slug: hippo-home
- description: First Connect, a Hippo subsidiary, is an API-first digital platform giving independent agents one-stop access to 100+ home, auto, cyber, small business, life, and specialty carriers and MGAs. The port
  name: First Connect (Independent Agent Platform)
  slug: first-connect
- description: Spinnaker is Hippo's affiliated specialty admitted carrier providing paper for MGAs and program administrators. Integrations are sales-led.
  name: Spinnaker Insurance (MGA Carrier Paper)
  slug: spinnaker
artifact_total: 9
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/hippo-insurance-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hippo-insurance-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hippo-insurance
- group: company
  title: ''
  type: Website
  url: https://www.hippo.com/
- group: company
  title: ''
  type: Blog
  url: https://www.hippo.com/blog
- group: learn
  title: ''
  type: LearnCenter
  url: https://www.hippo.com/learn-center
- group: operate
  title: ''
  type: FAQ
  url: https://faq.hippo.com/en/
- group: other
  title: ''
  type: FirstConnect
  url: https://www.firstconnectinsurance.com/
- group: other
  title: ''
  type: Spinnaker
  url: https://spinnakerins.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/hippo-insurance-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hippo-insurance-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/hippo-insurance-finops.yml
created: '2026-05-23'
description: Hippo is a modern homeowners insurance carrier that also offers landlord, fire, flood, pet, and auto add-ons, backed by 70+ carrier partners. Hippo's smart-home angle is the Hippo Home app, which delivers DIY maintenance checklists, seasonal guidance, and a home health score. Hippo's B2B distribution runs through First Connect, an API-driven independent-agent platform with 100+ carriers and MGAs, and Spinnaker for MGA carrier paper.
finops:
- name: Hippo Insurance Finops
  service_category: API
  slug: hippo-insurance-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hippo-insurance.png
layout: provider
modified: '2026-05-23'
name: Hippo Insurance
nav: Providers
network: true
overview: 'Hippo Insurance publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Homeowners, Insurtech, Smart Home, and Agents.


  Hippo Insurance''s developer surface includes engineering blog, FAQ, and 10 more developer resources.'
plans:
- name: Hippo Insurance Plans Pricing
  plan_count: 1
  slug: hippo-insurance-plans-pricing
random_paper: 27
rate_limits:
- limit_count: 2
  name: Hippo Insurance Rate Limits
  slug: hippo-insurance-rate-limits
score:
  band: emerging
  composite: 21.0
  delta: 0.5
  facets:
    commercial_clarity: 36.8
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 20.5
  regulatory:
    applies: true
    regime: Insurance
    regime_id: insurance
    score: 23.9
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hippo-insurance/refs/heads/main/screenshots/hippo-insurance-2026-06-20T182750.png
security:
- kind: domain-security
  name: Hippo Insurance Domain Security
  slug: hippo-insurance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Hippo Insurance Trust Center
  slug: hippo-insurance-trust-center
  summary_line: SOC 2, CSA STAR
slug: hippo-insurance
tags:
- Insurance
- Homeowners
- Insurtech
- Smart Home
- Agents
- MGA
- Embedded Insurance
- Carrier
website: https://www.hippo.com/
---
