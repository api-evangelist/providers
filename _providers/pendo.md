---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
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
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Pendo Agentic Access
  operation_count: 13
  slug: pendo-agentic-access
  summary_line: 13 operations · 3 acting
api_count: 8
apis:
- description: The Pendo Engage API provides programmatic access to product analytics data and in-app guide management — visitors, accounts, features, pages, guides, reports, metadata, and aggregations. Used to push
  name: Pendo Engage API
  slug: engage-api
- description: The Accounts API from Pendo — 1 operation(s) for accounts.
  name: Pendo Accounts API
  slug: pendo-accounts-api
- description: The Features API from Pendo — 2 operation(s) for features.
  name: Pendo Features API
  slug: pendo-features-api
- description: The Guides API from Pendo — 2 operation(s) for guides.
  name: Pendo Guides API
  slug: pendo-guides-api
- description: The Metadata API from Pendo — 2 operation(s) for metadata.
  name: Pendo Metadata API
  slug: pendo-metadata-api
- description: The Pages API from Pendo — 2 operation(s) for pages.
  name: Pendo Pages API
  slug: pendo-pages-api
- description: The Reports API from Pendo — 3 operation(s) for reports.
  name: Pendo Reports API
  slug: pendo-reports-api
- description: The Visitors API from Pendo — 1 operation(s) for visitors.
  name: Pendo Visitors API
  slug: pendo-visitors-api
artifact_total: 16
collections:
- collection_type: open
  name: Pendo Engage API
  slug: open-pendo
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pendo-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/pendo-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pendo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pendo-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pendo-io
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pendo-io
- group: company
  title: ''
  type: Website
  url: https://www.pendo.io/
- group: other
  title: ''
  type: Developers
  url: https://www.pendo.io/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://engageapi.pendo.io/
- group: commercial
  title: ''
  type: Plans
  url: plans/pendo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pendo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/pendo-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://app.pendo.io/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.pendo.io/blog/
created: '2026-05-08'
description: Pendo is a product analytics, in-app guidance, and feedback platform. Captures product usage, surfaces NPS, and delivers in-app messages, walkthroughs, and resource centers.
finops:
- name: Pendo Finops
  service_category: Product
  slug: pendo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pendo.png
layout: provider
modified: '2026-05-08'
name: Pendo
nav: Providers
network: true
overview: 'Pendo publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Features API, Guides API, and 4 more. Tagged areas include Product, Analytics, In-App Guidance, Customer Success, and NPS.


  Pendo''s developer surface includes authentication, documentation, engineering blog, and 11 more developer resources.'
plans:
- name: Pendo Plans Pricing
  plan_count: 1
  slug: pendo-plans-pricing
random_paper: 59
rate_limits:
- limit_count: 1
  name: Pendo Rate Limits
  slug: pendo-rate-limits
score:
  band: thin
  composite: 35.9
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 57.4
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 35.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pendo/refs/heads/main/screenshots/pendo-2026-06-20T191536.png
security:
- kind: authentication
  name: Pendo Authentication
  slug: pendo-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Pendo Domain Security
  slug: pendo-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Pendo Trust Center
  slug: pendo-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: pendo
tags:
- Product
- Analytics
- In-App Guidance
- Customer Success
- NPS
website: https://www.pendo.io/
---
