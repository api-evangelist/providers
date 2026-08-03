---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Ontraport Agentic Access
  operation_count: 11
  slug: ontraport-agentic-access
  summary_line: 11 operations · 5 acting
api_count: 3
apis:
- description: RESTful API providing CRUD access to contacts, transactions, tags, sequences, forms, landing pages, and ecommerce objects. Authentication uses two headers, Api-Key and Api-Appid, on every request, wit
  name: Ontraport REST API
  slug: rest-api
- description: Object metadata and field information.
  name: Ontraport Metadata API
  slug: ontraport-metadata-api
- description: Generic CRUD operations across Ontraport object types.
  name: Ontraport Objects API
  slug: ontraport-objects-api
artifact_total: 7
collections:
- collection_type: open
  name: Ontraport REST API
  slug: open-ontraport
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ontraport-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ontraport-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ontraport-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ontraport
- group: company
  title: ''
  type: Website
  url: https://ontraport.com
- group: docs
  title: ''
  type: Documentation
  url: https://api.ontraport.com/doc/
- group: commercial
  title: ''
  type: Pricing
  url: https://ontraport.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://ontraport.com/freetrial
- group: operate
  title: ''
  type: Support
  url: https://support.ontraport.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Ontraport
- group: company
  title: ''
  type: Blog
  url: https://ontraport.com/blog/feed/
created: '2026-05-11'
description: Ontraport is a business automation platform combining CRM, marketing automation, email marketing, landing pages, ecommerce, and membership site capabilities for small businesses and entrepreneurs. The platform unifies contact management, sales pipelines, payment processing, and visual automation campaigns in a single workspace. Ontraport's REST API exposes contacts, transactions, tags, sequences, forms, landing pages, and ecommerce objects using API-Key and Api-Appid header authentication.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ontraport.png
layout: provider
modified: '2026-05-11'
name: Ontraport
nav: Providers
network: true
overview: 'Ontraport publishes 2 APIs on the [APIs.io](https://apis.io/) network: Metadata API and Objects API. Tagged areas include CRM, Marketing Automation, Email Marketing, Ecommerce, and Landing Pages.


  Ontraport''s developer surface includes authentication, documentation, pricing, signup flow, support, engineering blog, and 5 more developer resources.'
random_paper: 51
score:
  band: thin
  composite: 29.0
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 54.3
    developer_ergonomics: 26.1
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 29.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ontraport/refs/heads/main/screenshots/ontraport-2026-06-20T190730.png
security:
- kind: authentication
  name: Ontraport Authentication
  slug: ontraport-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Ontraport Domain Security
  slug: ontraport-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ontraport
tags:
- CRM
- Marketing Automation
- Email Marketing
- Ecommerce
- Landing Pages
- Membership Sites
website: https://ontraport.com
---
