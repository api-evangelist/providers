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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: 'Web services API for CosmoLex legal practice management. Enables programmatic access to matters, time entries, billing, trust accounting, documents, and client data. Access is subject to a maximum of '
  name: CosmoLex API
  slug: cosmolex-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cosmolex-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/cosmolex/refs/heads/main/plans/cosmolex-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/cosmolex/refs/heads/main/rate-limits/cosmolex-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/cosmolex/refs/heads/main/finops/cosmolex-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.cosmolex.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cosmolex.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.cosmolex.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://support.cosmolex.com/
- group: start
  title: ''
  type: Login
  url: https://law.cosmolex.com/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cosmolex.com/subscription-agreement/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cosmolex.com/privacy-policy/
created: '2026-06-13'
description: CosmoLex is a cloud-based legal practice management platform that combines matter management, time tracking, billing, trust accounting, and client engagement in a single system. It provides a web services API for integrating matters, time entries, billing, trust accounting, and compliance workflows, subject to a per-user-license monthly call quota. CosmoLex serves solo practitioners and law firms up to 100 users and is designed to satisfy state bar trust accounting compliance requirements.
finops:
- name: Cosmolex Finops
  service_category: ''
  slug: cosmolex-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cosmolex.png
jsonld:
- class_count: 11
  name: Cosmolex Context
  property_count: 25
  slug: cosmolex-context
layout: provider
modified: '2026-06-13'
name: CosmoLex
nav: Providers
network: true
overview: 'CosmoLex publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Legal, Law Practice Management, Matter Management, Billing, and Trust Accounting.


  The CosmoLex catalog on APIs.io includes 1 JSON-LD context.


  CosmoLex''s developer surface includes pricing, engineering blog, support, and 8 more developer resources.'
plans:
- name: Cosmolex Plans Pricing
  plan_count: 3
  slug: cosmolex-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 3
  name: Cosmolex Rate Limits
  slug: cosmolex-rate-limits
score:
  band: thin
  composite: 33.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 75.0
    catalog_earned_first_party: 0.0
    catalog_gap: 40.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 77.6
    commercial_clarity: 77.6
    contract_governance: 0.0
    contract_quality: 14.7
    developer_ergonomics: 16.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 33.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cosmolex/refs/heads/main/screenshots/cosmolex-2026-06-20T175047.png
security:
- kind: domain-security
  name: Cosmolex Domain Security
  slug: cosmolex-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cosmolex
tags:
- Legal
- Law Practice Management
- Matter Management
- Billing
- Trust Accounting
- Time Tracking
- Legal Compliance
- Legal Software
website: https://www.cosmolex.com/
---
