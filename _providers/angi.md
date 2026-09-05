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
random_paper: 16
score:
  band: emerging
  composite: 16.5
  coverage:
    artifact_dirs: 3
    catalog_earned: 49.0
    catalog_earned_first_party: 0.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 16.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/angi/refs/heads/main/screenshots/angi-2026-08-07T161409.png
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
- IaC
- Webhook
- No Public API
website: https://www.angi.com
---
