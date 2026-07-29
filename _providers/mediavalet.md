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
- acting_count: 8
  human_in_the_loop: 0
  name: Mediavalet Agentic Access
  operation_count: 33
  slug: mediavalet-agentic-access
  summary_line: 33 operations · 8 acting
api_count: 6
apis:
- description: Core digital asset objects and their derivatives.
  name: MediaValet Assets API
  slug: mediavalet-assets-api
- description: Custom metadata fields and their values on assets.
  name: MediaValet Attributes API
  slug: mediavalet-attributes-api
- description: Hierarchical folders that organize assets.
  name: MediaValet Categories API
  slug: mediavalet-categories-api
- description: Keyword vocabulary and per-asset tagging.
  name: MediaValet Keywords API
  slug: mediavalet-keywords-api
- description: Chunked ingest of new files into a library.
  name: MediaValet Uploads API
  slug: mediavalet-uploads-api
- description: Users, groups, and permissions.
  name: MediaValet Users API
  slug: mediavalet-users-api
artifact_total: 15
collections:
- collection_type: open
  name: MediaValet Open API
  slug: open-mediavalet
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mediavalet-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/mediavalet-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mediavalet-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mediavalet-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/mediavalet-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mediavalet
- group: company
  title: ''
  type: Website
  url: https://www.mediavalet.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mediavalet.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.mediavalet.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/mediavalet-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mediavalet-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/mediavalet-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.mediavalet.com/blog
created: '2026-07-05'
description: MediaValet is a cloud-native digital asset management (DAM) platform, built on Microsoft Azure, for storing, organizing, sharing, and distributing an organization's images, videos, documents, and other brand and marketing assets. Its Open API is a RESTful, JSON, hypermedia-driven service (base https://api.mediavalet.com) secured with OAuth 2.0 plus a per-account subscription key, letting teams automate uploading, cataloging, searching, and governing assets, categories, attributes, keywords, and users.
finops:
- name: Mediavalet Finops
  service_category: Digital Asset Management
  slug: mediavalet-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mediavalet.png
layout: provider
modified: '2026-07-05'
name: MediaValet
nav: Providers
network: true
overview: 'MediaValet publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Assets API, Attributes API, Categories API, and 3 more. Tagged areas include Digital Asset Management, DAM, Media, Assets, and Content.


  MediaValet''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Mediavalet Plans Pricing
  plan_count: 2
  slug: mediavalet-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 3
  name: Mediavalet Rate Limits
  slug: mediavalet-rate-limits
scopes:
- name: Mediavalet Scopes
  scope_count: 3
  slug: mediavalet-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: thin
  composite: 40.0
  delta: -2.1
  facets:
    commercial_clarity: 36.8
    contract_quality: 60.2
    developer_ergonomics: 30.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 42.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Mediavalet Authentication
  slug: mediavalet-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Mediavalet Domain Security
  slug: mediavalet-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Mediavalet Trust Center
  slug: mediavalet-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: mediavalet
tags:
- Digital Asset Management
- DAM
- Media
- Assets
- Content
- Marketing
- Cloud Storage
website: https://www.mediavalet.com
---
