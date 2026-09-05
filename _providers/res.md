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
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/res-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.getresq.com
- group: company
  title: ''
  type: Blog
  url: https://www.getresq.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.getresq.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://support.getresq.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.getresq.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.getresq.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.getresq.com/privacy-policy
created: '2026-07-17'
description: Res (ResQ) is an AI-powered operations platform for the service economy, connecting restaurants, hospitality groups, and facilities-management teams with vetted trades vendors to manage repair-and-maintenance work orders end to end. The platform covers work-order intake and dispatch, vendor sourcing and communication, invoicing and payments, and reporting across trades such as HVAC, plumbing, refrigeration, and electrical. Backed by Homebrew and surfaced through the API Evangelist network, ResQ operates a web and mobile SaaS product; it publishes no public developer API, OpenAPI definitions, SDKs, or webhook surface at this time, so this profile captures company identity, website properties, and probed domain-security posture.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/res.png
layout: provider
modified: '2026-07-20'
name: Res
nav: Providers
network: true
overview: 'Res is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Facilities Management, Field Service, and Work Orders.


  Res'' developer surface includes engineering blog, pricing, support, and 5 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 12.7
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 12.7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/res/refs/heads/main/screenshots/res-2026-09-02T153525.png
security:
- kind: domain-security
  name: Res Domain Security
  slug: res-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: res
tags:
- Company
- Consumer
- Facilities Management
- Field Service
- Work Orders
- Trades
- Maintenance
- Hospitality
- Restaurant
- Software-as-a-Service
- Vendor Management
website: https://www.getresq.com
---
