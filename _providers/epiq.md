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
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-10'
api_count: 3
apis:
- description: The AACER API enables real-time bankruptcy case information to be electronically transmitted system-to-system, integrating with the industry's largest servicing applications and proprietary systems. S
  name: Epiq AACER Bankruptcy API
  slug: epiq-aacer-bankruptcy-api
- description: Epiq Discover provides an open API and third-party integration support for eDiscovery workflows, enabling seamless adoption within client tech stacks. Supports preserving, processing, analyzing, revie
  name: Epiq eDiscovery API
  slug: epiq-ediscovery-api
- description: EpiqPay is Epiq's proprietary platform facilitating digital settlement payments. Provides APIs for disbursing class action and settlement funds to claimants via diverse payment networks including PayP
  name: EpiqPay Payment API
  slug: epiqpay-payment-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/epiq-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://access.epiqglobal.com/
- group: company
  title: ''
  type: Website
  url: https://www.epiqglobal.com/
- group: commercial
  title: ''
  type: ServiceLevelAgreement
  url: https://www.epiqglobal.com/en-us/service-level-agreement
- group: operate
  title: ''
  type: Contact
  url: https://www.epiqglobal.com/en-us/contact-us
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/epiq/refs/heads/main/plans/epiq-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/epiq/refs/heads/main/rate-limits/epiq-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/epiq/refs/heads/main/finops/epiq-finops.yml
- group: company
  title: ''
  type: Investors
  url: https://www.epiqglobal.com/en-us/technologies/class-action-and-mass-tort-technologies/epiqfiling
created: '2026-06-13'
description: Epiq is a global legal operations and technology company providing REST APIs for case management, eDiscovery, settlement administration, bankruptcy services, and class action claims processing. Their API suite includes AACER for real-time bankruptcy case data retrieval and monitoring, EpiqFiling for securities claims management, and EpiqPay for settlement payment disbursement.
finops:
- name: Epiq Finops
  service_category: ''
  slug: epiq-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/epiq.png
jsonld:
- class_count: 6
  name: Epiq Context
  property_count: 38
  slug: epiq-context
layout: provider
modified: '2026-07-25'
name: Epiq
nav: Providers
network: true
overview: 'Epiq publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Legal, eDiscovery, Bankruptcy, Class Action, and Settlement Administration.


  The Epiq catalog on APIs.io includes 1 JSON-LD context.


  Epiq''s developer surface includes developer portal and 8 more developer resources.'
plans:
- name: Epiq Plans Pricing
  plan_count: 3
  slug: epiq-plans-pricing
random_paper: 83
rate_limits:
- limit_count: 0
  name: Epiq Rate Limits
  slug: epiq-rate-limits
score:
  band: emerging
  composite: 21.5
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 17.7
    developer_ergonomics: 8.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 21.5
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/epiq/refs/heads/main/screenshots/epiq-2026-06-20T180757.png
security:
- kind: domain-security
  name: Epiq Domain Security
  slug: epiq-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: epiq
tags:
- Legal
- eDiscovery
- Bankruptcy
- Class Action
- Settlement Administration
- Legal Technology
- Case Management
- Document Review
website: https://www.epiqglobal.com/
---
