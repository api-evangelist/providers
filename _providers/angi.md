---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-03'
api_count: 2
apis:
- description: 'Not a self-serve public API - there is no published base URL, API reference, or API key signup. Once a pro or CRM partner is approved by an Angi Ads Client Success Manager, Angi Ads/Angi Leads pushes '
  name: Angi Leads Delivery (Webhook) API
  slug: angi-leads-delivery-api
- description: An OAuth-style "Sign in with Angi" account-linking flow used by a short, approved list of CRM and field-service management partners (ServiceTitan, Jobber) to connect a pro's Angi account and receive a
  name: Angi Pro Account Linking (Sign in with Angi)
  slug: angi-pro-account-linking
artifact_total: 5
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/angi-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/angi-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/angi
- group: company
  title: ''
  type: Website
  url: https://www.angi.com
- group: docs
  title: ''
  type: Documentation
  url: https://intercom.help/angi/en/collections/12900573-api-integrations
- group: commercial
  title: ''
  type: Plans
  url: plans/angi-plans-pricing.yml
created: '2026-07-03'
description: 'Angi (formerly Angie''s List, founded 1995) is a digital home services marketplace connecting homeowners with home service professionals for repair, maintenance, and improvement projects. Angie''s List merged with IAC''s HomeAdvisor in 2017 under parent ANGI Homeservices Inc.; in March 2021 the consumer brand and parent company were both renamed Angi, with HomeAdvisor continuing as the pro-facing "Angi Leads" lead-generation business. IAC fully spun off its stake in April 2025, making Angi Inc. (NASDAQ: ANGI) an independent public company. Angi does not operate a self-serve public developer portal or publish an API reference. It does offer a gated, partner-only lead-delivery mechanism: Angi Ads/Angi Leads pushes new homeowner leads as JSON to a webhook URL a pro''s CRM provides (authenticated with an X-API-KEY header), and an OAuth-style "Sign in with Angi" account-linking flow used by a short list of approved CRM/field-service partners (ServiceTitan, Jobber) to receive lead
  and booking data. Both require a direct arrangement with an Angi Ads Client Success Manager rather than self-serve API keys.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/angi.png
layout: provider
modified: '2026-07-03'
name: Angi
nav: Providers
network: true
overview: 'Angi publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Home Services, Marketplace, Leads, Angie''s List, and HomeAdvisor.


  Angi''s developer surface includes documentation and 5 more developer resources.'
plans:
- name: Angi Plans Pricing
  plan_count: 3
  slug: angi-plans-pricing
random_paper: 35
score:
  band: emerging
  composite: 14.9
  delta: 0.0
  facets:
    commercial_clarity: 31.6
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 14.9
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: domain-security
  name: Angi Domain Security
  slug: angi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Angi Vulnerability Disclosure
  slug: angi-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: angi
tags:
- Home Services
- Marketplace
- Leads
- Angie's List
- HomeAdvisor
- IAC
- Webhook
- No Public API
website: https://www.angi.com
---
