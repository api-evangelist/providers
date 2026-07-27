---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Africastalking Agentic Access
  operation_count: 14
  slug: africastalking-agentic-access
  summary_line: 14 operations · 12 acting
api_count: 6
apis:
- description: Distribute mobile airtime to recipients.
  name: Africa's Talking Airtime API
  slug: africastalking-airtime-api
- description: Disburse mobile data bundles to recipients.
  name: Africa's Talking Mobile Data API
  slug: africastalking-mobile-data-api
- description: Mobile C2B checkout, B2C, and B2B mobile money transfers.
  name: Africa's Talking Payments API
  slug: africastalking-payments-api
- description: Premium SMS subscriptions and checkout tokens.
  name: Africa's Talking Premium SMS API
  slug: africastalking-premium-sms-api
- description: Send single and bulk SMS and fetch inbox messages.
  name: Africa's Talking SMS API
  slug: africastalking-sms-api
- description: Outbound calls, transfers, queue status, and media upload.
  name: Africa's Talking Voice API
  slug: africastalking-voice-api
artifact_total: 13
collections:
- collection_type: open
  name: Africa's Talking API
  slug: open-africastalking
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/africastalking-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/africastalking-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/africastalking-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AfricasTalkingLtd
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/africa-s-talking
- group: company
  title: ''
  type: Website
  url: https://africastalking.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.africastalking.com
- group: commercial
  title: ''
  type: Plans
  url: plans/africastalking-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/africastalking-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/africastalking-finops.yml
created: '2026-06-20'
description: Africa's Talking is a pan-African communications platform that exposes a unified set of REST APIs for SMS, USSD, Voice, Airtime, Mobile Data, and Payments. Developers authenticate with an apiKey and username and reach mobile subscribers across Kenya, Nigeria, Uganda, Tanzania, Rwanda, and other African markets through carrier integrations.
finops:
- name: Africastalking Finops
  service_category: Communications
  slug: africastalking-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/africastalking.png
layout: provider
modified: '2026-06-20'
name: Africa's Talking
nav: Providers
network: true
overview: 'Africa''s Talking publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Airtime API, Mobile Data API, Payments API, and 3 more. Tagged areas include Communications, SMS, USSD, Voice, and Airtime.


  Africa''s Talking''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Africastalking Plans Pricing
  plan_count: 2
  slug: africastalking-plans-pricing
random_paper: 47
rate_limits:
- limit_count: 5
  name: Africastalking Rate Limits
  slug: africastalking-rate-limits
score:
  band: thin
  composite: 37.1
  delta: 2.8
  facets:
    commercial_clarity: 28.9
    contract_quality: 58.1
    developer_ergonomics: 19.6
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 34.3
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 26.1
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/africastalking/refs/heads/main/screenshots/africastalking-2026-06-20T165713.png
security:
- kind: authentication
  name: Africastalking Authentication
  slug: africastalking-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Africastalking Domain Security
  slug: africastalking-domain-security
  summary_line: TLSv1.3 · DMARC
slug: africastalking
tags:
- Communications
- SMS
- USSD
- Voice
- Airtime
- Mobile Data
- Payments
- Africa
website: https://africastalking.com
---
