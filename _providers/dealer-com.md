---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Lead generation and management capability - pre-qualification, messaging, and customer-engagement tools that capture website leads and route them into dealer CRM and Cox Automotive systems (Dealertrac
  name: Dealer.com Leads API
  slug: dealer-com-leads-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/dealer-com-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dealer-com-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dealer-com
- group: company
  title: ''
  type: Website
  url: https://www.dealer.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.dealer.com/products/integrated-partner-program
- group: docs
  title: ''
  type: Documentation
  url: https://developer.coxautoinc.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/dealer-com-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dealer-com-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dealer-com-finops.yml
- group: other
  title: ''
  type: ProductPage
  url: https://www.dealer.com/integrations/
- group: company
  title: ''
  type: News
  url: https://www.dealer.com/company-news/data-integration-unlocks-website-personalization-press-release/
created: '2026-07-10'
description: 'Dealer.com, a Cox Automotive brand, builds automotive dealership websites, digital advertising, and digital marketing technology used by thousands of franchise and independent dealers across North America. Its integration surface is partner-gated: third parties embed experiences on dealer sites through the Dealer.com Website Integration API and the Integrated Partner Program, while inventory, leads, deal, and digital-retail data flow through the broader Cox Automotive Integration Platform (developer.coxautoinc.com), which uses OAuth (Okta) and requires an approved partner agreement. Dealer.com does not publish an open, self-serve public API; the endpoints modeled here are logical groupings of the partner capabilities, not a documented public surface.'
finops:
- name: Dealer Com Finops
  service_category: Automotive Digital Marketing and Websites
  slug: dealer-com-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dealer-com.png
layout: provider
modified: '2026-07-25'
name: Dealer.com
nav: Providers
network: true
overview: 'Dealer.com publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Automotive, Dealership, Digital Marketing, Website Platform, and Inventory.


  Dealer.com''s developer surface includes documentation, product news, and 9 more developer resources.'
plans:
- name: Dealer Com Plans Pricing
  plan_count: 2
  slug: dealer-com-plans-pricing
random_paper: 61
rate_limits:
- limit_count: 3
  name: Dealer Com Rate Limits
  slug: dealer-com-rate-limits
score:
  band: emerging
  composite: 17.6
  delta: -2.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 19.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dealer-com/refs/heads/main/screenshots/dealer-com-2026-07-25T211507.png
security:
- kind: domain-security
  name: Dealer Com Domain Security
  slug: dealer-com-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Dealer Com Vulnerability Disclosure
  slug: dealer-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: dealer-com
tags:
- Automotive
- Dealership
- Digital Marketing
- Website Platform
- Inventory
- Leads
- Digital Advertising
- Cox Automotive
- Partner Program
website: https://www.dealer.com
---
