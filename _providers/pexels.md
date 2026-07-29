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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Pexels Agentic Access
  operation_count: 9
  slug: pexels-agentic-access
  summary_line: 9 operations
api_count: 3
apis:
- description: Browse featured and user-owned collections.
  name: Pexels Collections API
  slug: pexels-collections-api
- description: Search, browse, and retrieve photos.
  name: Pexels Photos API
  slug: pexels-photos-api
- description: Search, browse, and retrieve videos.
  name: Pexels Videos API
  slug: pexels-videos-api
artifact_total: 10
collections:
- collection_type: open
  name: Pexels API
  slug: open-pexels
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pexels-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pexels-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pexels-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pexels
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pexels
- group: start
  title: ''
  type: Portal
  url: https://www.pexels.com/api/
- group: docs
  title: ''
  type: Documentation
  url: https://www.pexels.com/api/documentation/
- group: start
  title: ''
  type: Signup
  url: https://www.pexels.com/api/
- group: company
  title: ''
  type: Website
  url: https://www.pexels.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pexels.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pexels.com/privacy-policy/
created: '2026-03-16'
description: Give your users access to the entire Pexels photo and video library without leaving your app or website. The Pexels API is free and seamlessly integrates with just a few lines of code.
finops:
- name: Pexels Finops
  service_category: API
  slug: pexels-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pexels.png
layout: provider
modified: '2026-05-19'
name: Pexels
nav: Providers
network: true
overview: 'Pexels publishes 3 APIs on the [APIs.io](https://apis.io/) network: Collections API, Photos API, and Videos API. Tagged areas include Photos, Stock Media, and Videos.


  Pexels'' developer surface includes authentication, developer portal, documentation, signup flow, and 7 more developer resources.'
plans:
- name: Pexels Plans Pricing
  plan_count: 3
  slug: pexels-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Pexels Rate Limits
  slug: pexels-rate-limits
score:
  band: developing
  composite: 42.7
  delta: -1.5
  facets:
    commercial_clarity: 60.5
    contract_quality: 58.5
    developer_ergonomics: 28.3
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 44.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pexels/refs/heads/main/screenshots/pexels-2026-06-20T191627.png
security:
- kind: authentication
  name: Pexels Authentication
  slug: pexels-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Pexels Domain Security
  slug: pexels-domain-security
  summary_line: TLSv1.3 · DMARC
slug: pexels
tags:
- Photos
- Stock Media
- Videos
website: https://www.pexels.com/
---
