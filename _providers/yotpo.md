---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Yotpo Agentic Access
  operation_count: 14
  slug: yotpo-agentic-access
  summary_line: 14 operations · 8 acting
api_count: 1
apis:
- description: OAuth token exchange for app key + secret.
  name: Yotpo Authentication API
  slug: yotpo-authentication-api
- description: Loyalty and referrals customers, orders, and redemptions.
  name: Yotpo Loyalty API
  slug: yotpo-loyalty-api
- description: Reviews and user-generated content.
  name: Yotpo Reviews API
  slug: yotpo-reviews-api
- description: Core API store sync and webhook subscriptions.
  name: Yotpo Subscriptions API
  slug: yotpo-subscriptions-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Yotpo Authentication API
  slug: open-yotpo-authentication-api
- collection_type: open
  name: Yotpo Authentication Loyalty API
  slug: open-yotpo-loyalty-api
- collection_type: open
  name: Yotpo Authentication Subscriptions API
  slug: open-yotpo-subscriptions-api
- collection_type: open
  name: Yotpo API
  slug: open-yotpo
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/yotpo-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/yotpo-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/yotpo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/yotpo-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://www.yotpo.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/YotpoLtd
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/yotpo
- group: company
  title: ''
  type: Website
  url: https://www.yotpo.com
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.yotpo.com/reference
- group: commercial
  title: ''
  type: Plans
  url: plans/yotpo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/yotpo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/yotpo-finops.yml
created: '2026-06-25'
description: Yotpo is an eCommerce retention marketing platform offering Reviews & Ratings, Loyalty & Referrals, Subscriptions, and visual UGC. Each product exposes a documented REST API - the UGC/Reviews and Core APIs under api.yotpo.com (app key plus OAuth utoken) and the Loyalty & Referrals API under loyalty.yotpo.com (program GUID plus API key) - so merchants can sync orders, products, and customers and drive reviews, points, and redemptions programmatically. Yotpo's SMS & Email (SMSBump) products were discontinued on December 31, 2025.
finops:
- name: Yotpo Finops
  service_category: Marketing and Commerce
  slug: yotpo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/yotpo.png
layout: provider
modified: '2026-06-25'
name: Yotpo
nav: Providers
network: true
overview: 'Yotpo publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Loyalty API, Reviews API, and 1 more. Tagged areas include E-Commerce, Reviews, Loyalty, Retention Marketing, and UGC.


  Yotpo''s developer surface includes authentication, engineering blog, documentation, and 9 more developer resources.'
plans:
- name: Yotpo Plans Pricing
  plan_count: 4
  slug: yotpo-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 4
  name: Yotpo Rate Limits
  slug: yotpo-rate-limits
score:
  band: thin
  composite: 37.1
  coverage:
    artifact_dirs: 9
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 49.0
    developer_ergonomics: 20.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 37.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Yotpo Authentication
  slug: yotpo-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Yotpo Domain Security
  slug: yotpo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Yotpo Trust Center
  slug: yotpo-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, GDPR, CSA STAR
slug: yotpo
tags:
- E-Commerce
- Reviews
- Loyalty
- Retention Marketing
- UGC
website: https://www.yotpo.com
---
