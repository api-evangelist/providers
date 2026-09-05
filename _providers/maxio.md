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
    auth_clarity: bearer
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
  score: 2.5
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: 'REST API for managing the full subscription lifecycle in Maxio Advanced Billing (formerly Chargify): customers, products, components, subscriptions, invoices, transactions, coupons, and webhooks. Auth'
  name: Maxio Advanced Billing API
  slug: advanced-billing-api
artifact_total: 3
common:
- group: start
  title: ''
  type: Sandbox
  url: https://www.maxio.com/sandbox
- group: auth
  title: ''
  type: Security
  url: https://www.maxio.com/security
- group: operate
  title: ''
  type: StatusPage
  url: https://maxio.statuspage.io/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.maxio.com/privacy-policy
- group: other
  title: ''
  type: OpenIDConnect
  url: https://www.maxio.com/.well-known/oauth-authorization-server
- group: auth
  title: ''
  type: TrustCenter
  url: security/maxio-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/maxio-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wearemaxio
- group: company
  title: ''
  type: Website
  url: https://www.maxio.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.maxio.com/
- group: operate
  title: ''
  type: Help Center
  url: https://docs.maxio.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/maxio-com
- group: start
  title: ''
  type: Signup
  url: https://www.maxio.com/get-started
- group: commercial
  title: ''
  type: Pricing
  url: https://www.maxio.com/pricing
- group: agent
  title: ''
  type: LlmsText
  url: https://maxio.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.maxio.com/blog
created: '2026-05-11'
description: Maxio is a SaaS billing and financial operations platform formed from the merger of Chargify and SaaSOptics, providing subscription management, recurring billing, revenue recognition, and SaaS metrics for B2B software companies. Maxio Advanced Billing (formerly Chargify) exposes a REST API for managing customers, subscriptions, products, components, invoices, and events. Authentication uses HTTP Basic auth with a per-site API key as the username.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/maxio.png
layout: provider
modified: '2026-05-11'
name: Maxio
nav: Providers
network: true
overview: 'Maxio publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Billing, Subscription, Recurring Billing, Revenue Recognition, and SaaS Metrics.


  Maxio''s developer surface includes sandbox, documentation, signup flow, pricing, engineering blog, and 11 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 25.1
  coverage:
    artifact_dirs: 5
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 25.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 32.8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/maxio/refs/heads/main/screenshots/maxio-2026-06-20T185049.png
security:
- kind: domain-security
  name: Maxio Domain Security
  slug: maxio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Maxio Trust Center
  slug: maxio-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, GDPR
slug: maxio
tags:
- Billing
- Subscription
- Recurring Billing
- Revenue Recognition
- SaaS Metrics
- Payments
website: https://www.maxio.com
---
