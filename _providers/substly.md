---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: Substly is an uncomplicated and affordable SaaS management platform for SMBs, offering subscription tracking, spend optimization, user access management, and shadow IT detection. It integrates with Go
  name: Substly
  slug: substly
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/substly-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/substly
- group: company
  title: ''
  type: Website
  url: https://www.substly.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.substly.com/en/features/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.substly.com/en/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.substly.com/en/blog/
- group: company
  title: ''
  type: AboutUs
  url: https://www.substly.com/en/about-us/
- group: start
  title: ''
  type: Login
  url: https://app.substly.com
created: '2026-03-27'
description: Substly is a SaaS management platform designed for small and medium-sized businesses to track software subscriptions, optimize spend, manage user access, and detect shadow IT across cloud applications. It provides centralized oversight, automated renewal tracking, and integrations with Google Workspace and Microsoft Entra ID.
finops:
- name: Substly Finops
  service_category: API
  slug: substly-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/substly.png
jsonld:
- class_count: 14
  name: Substly Context
  property_count: 5
  slug: substly-context
layout: provider
modified: '2026-05-02'
name: Substly
nav: Providers
network: true
overview: 'Substly publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include SaaS Management, Subscription Management, Spend Management, IT Management, and Shadow IT.


  The Substly catalog on APIs.io includes 1 JSON-LD context.


  Substly''s developer surface includes documentation, pricing, engineering blog, and 5 more developer resources.'
plans:
- name: Substly Plans Pricing
  plan_count: 3
  slug: substly-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Substly Rate Limits
  slug: substly-rate-limits
score:
  band: emerging
  composite: 18.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 49.0
    catalog_earned_first_party: 0.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 32.9
    commercial_clarity: 32.9
    contract_governance: 0.0
    contract_quality: 10.7
    developer_ergonomics: 11.9
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 18.6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/substly/refs/heads/main/screenshots/substly-2026-06-20T194632.png
security:
- kind: domain-security
  name: Substly Domain Security
  slug: substly-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: substly
tags:
- SaaS Management
- Subscription Management
- Spend Management
- IT Management
- Shadow IT
website: https://www.substly.com
---
