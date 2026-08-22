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
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: WalkMe Public APIs provide programmatic access to insights data, account/system metadata, content publishing, and integration with the WalkMe digital adoption platform.
  name: WalkMe Public API
  slug: walkme-public-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/walkme-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/walkme-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/WalkMe
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/walkme
- group: company
  title: ''
  type: Website
  url: https://www.walkme.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.walkme.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/walkme-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/walkme-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/walkme-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.walkme.com/blog/feed/
created: '2026-05-08'
description: WalkMe is a Digital Adoption Platform delivering in-app guidance, walkthroughs, and analytics that help users navigate and adopt enterprise applications.
finops:
- name: Walkme Finops
  service_category: Product
  slug: walkme-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/walkme.png
layout: provider
modified: '2026-05-08'
name: WalkMe
nav: Providers
network: true
overview: 'WalkMe publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Digital Adoption, In-App Guidance, Productivity, Analytics, and Onboarding.


  WalkMe''s developer surface includes documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Walkme Plans Pricing
  plan_count: 1
  slug: walkme-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 1
  name: Walkme Rate Limits
  slug: walkme-rate-limits
score:
  band: emerging
  composite: 12.6
  delta: -1.1
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 13.7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/walkme/refs/heads/main/screenshots/walkme-2026-06-20T201212.png
security:
- kind: domain-security
  name: Walkme Domain Security
  slug: walkme-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Walkme Trust Center
  slug: walkme-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, HIPAA, FedRAMP, GDPR, CSA STAR, FIPS 140
slug: walkme
tags:
- Digital Adoption
- In-App Guidance
- Productivity
- Analytics
- Onboarding
website: https://www.walkme.com/
---
