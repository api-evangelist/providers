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
- description: REST API for programmatic management of cap table data including stakeholders, equity grants, option pools, convertible instruments, vesting schedules, and investor reporting. Used by integrations wit
  name: Pulley API
  slug: pulley-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/pulley-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pulley-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pulley.com/
- group: docs
  title: ''
  type: Documentation
  url: https://pulley.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/pulley
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pulley-cap-table
- group: company
  title: ''
  type: Blog
  url: https://pulley.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://pulley.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.pulley.com
- group: other
  title: ''
  type: X
  url: https://x.com/pulleyapp
- group: commercial
  title: ''
  type: Plans
  url: plans/pulley-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pulley-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/pulley-finops.yml
created: '2026-06-13'
description: Cap table management platform for startups and finance leaders, providing a REST API for managing equity, modeling dilution, issuing options and RSUs, tracking SAFEs and convertible instruments, and generating investor and compliance reports. Pulley supports both equity and token cap tables with integrations to leading HRIS platforms, custodians, and legal tools.
finops:
- name: Pulley Finops
  service_category: ''
  slug: pulley-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pulley.png
jsonld:
- class_count: 22
  name: Pulley Context
  property_count: 0
  slug: pulley-context
layout: provider
modified: '2026-06-13'
name: Pulley
nav: Providers
network: true
overview: 'Pulley publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cap Table, Equity Management, Startups, Options, and RSUs.


  The Pulley catalog on APIs.io includes 1 JSON-LD context.


  Pulley''s developer surface includes documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Pulley Plans Pricing
  plan_count: 6
  slug: pulley-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 3
  name: Pulley Rate Limits
  slug: pulley-rate-limits
score:
  band: thin
  composite: 29.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 72.0
    catalog_earned_first_party: 0.0
    catalog_gap: 43.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 0.0
    contract_quality: 10.7
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 44.7
  previous_composite: 29.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pulley/refs/heads/main/screenshots/pulley-2026-06-20T192253.png
security:
- kind: domain-security
  name: Pulley Domain Security
  slug: pulley-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Pulley Trust Center
  slug: pulley-trust-center
  summary_line: SOC 2, GDPR
slug: pulley
tags:
- Cap Table
- Equity Management
- Startups
- Options
- RSUs
- SAFEs
- 409A Valuations
- Token Cap Table
- Fintech
website: https://pulley.com/
---
