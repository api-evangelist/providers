---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 6
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/aftership-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/aftership-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aftership-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AfterShip
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aftership
- group: company
  title: ''
  type: Website
  url: https://www.aftership.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/aftership-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/aftership-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/aftership-finops.yml
created: '2026-05-08'
description: AfterShip is an e-commerce shipment tracking and post-purchase platform. APIs cover trackings, couriers, notifications, returns, and email.
finops:
- name: Aftership Finops
  service_category: Shipping
  slug: aftership-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aftership.png
layout: provider
modified: '2026-05-08'
name: AfterShip
nav: Providers
network: true
overview: AfterShip is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Shipping, Tracking, E-Commerce, Post-Purchase, and Notification.
plans:
- name: Aftership Plans Pricing
  plan_count: 1
  slug: aftership-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 1
  name: Aftership Rate Limits
  slug: aftership-rate-limits
score:
  band: minimal
  composite: 9.3
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 40.7
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 9.3
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aftership/refs/heads/main/screenshots/aftership-2026-06-20T165736.png
security:
- kind: domain-security
  name: Aftership Domain Security
  slug: aftership-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aftership Vulnerability Disclosure
  slug: aftership-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Aftership Trust Center
  slug: aftership-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: aftership
tags:
- Shipping
- Tracking
- E-Commerce
- Post-Purchase
- Notification
website: https://www.aftership.com/
---
