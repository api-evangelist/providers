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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 0.0
  scored_at: '2026-07-27'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/parkhub-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/parkhub-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/parkhub-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/parkhub
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/parkhub-com
- group: company
  title: ''
  type: Website
  url: https://www.justpark.com/business/
- group: company
  title: ''
  type: Blog
  url: https://www.justpark.com/uk/business/blog
created: '2026-03-16'
description: Parkhub provided parking management and payment processing APIs for parking operators and venues. Parkhub has been acquired and the parkhub.com domain now redirects to JustPark Business. Public API documentation is no longer available.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/parkhub.png
layout: provider
modified: '2026-04-28'
name: Parkhub
nav: Providers
network: true
overview: 'Parkhub is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Parking, Payments, and Acquired.


  Parkhub''s developer surface includes engineering blog and 6 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 12.5
  delta: 0.0
  facets:
    commercial_clarity: 7.9
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 55.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 12.5
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 37.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/parkhub/refs/heads/main/screenshots/parkhub-2026-06-20T191416.png
security:
- kind: domain-security
  name: Parkhub Domain Security
  slug: parkhub-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Parkhub Vulnerability Disclosure
  slug: parkhub-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Parkhub Trust Center
  slug: parkhub-trust-center
  summary_line: SOC 2, PCI DSS
slug: parkhub
tags:
- Parking
- Payments
- Acquired
website: https://www.justpark.com/business/
---
