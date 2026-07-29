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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Drip Agentic Access
  operation_count: 22
  slug: drip-agentic-access
  summary_line: 22 operations · 11 acting
api_count: 11
apis:
- description: 'REST API for Drip exposing subscribers, tags, custom fields, broadcasts, email campaigns, events, conversions, workflows, shopper activity (orders, carts, products), purchases, and webhooks. Supports '
  name: Drip REST API
  slug: drip-api
- description: The Accounts API from Drip — 2 operation(s) for accounts.
  name: Drip Accounts API
  slug: drip-accounts-api
- description: The Broadcasts API from Drip — 2 operation(s) for broadcasts.
  name: Drip Broadcasts API
  slug: drip-broadcasts-api
- description: The Campaigns API from Drip — 5 operation(s) for campaigns.
  name: Drip Campaigns API
  slug: drip-campaigns-api
- description: The Conversions API from Drip — 1 operation(s) for conversions.
  name: Drip Conversions API
  slug: drip-conversions-api
- description: The Custom Fields API from Drip — 1 operation(s) for custom fields.
  name: Drip Custom Fields API
  slug: drip-custom-fields-api
- description: The Events API from Drip — 3 operation(s) for events.
  name: Drip Events API
  slug: drip-events-api
- description: The Forms API from Drip — 1 operation(s) for forms.
  name: Drip Forms API
  slug: drip-forms-api
- description: The Orders API from Drip — 1 operation(s) for orders.
  name: Drip Orders API
  slug: drip-orders-api
- description: The Shopper Activity API from Drip — 3 operation(s) for shopper activity.
  name: Drip Shopper Activity API
  slug: drip-shopper-activity-api
- description: The Subscribers API from Drip — 2 operation(s) for subscribers.
  name: Drip Subscribers API
  slug: drip-subscribers-api
artifact_total: 15
collections:
- collection_type: open
  name: Drip REST API
  slug: open-drip
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/drip-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/drip-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/drip-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/getdrip
- group: company
  title: ''
  type: Website
  url: https://www.drip.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.drip.com/
- group: start
  title: ''
  type: Signup
  url: https://www.drip.com/forms/79091116/submissions/new
- group: commercial
  title: ''
  type: Pricing
  url: https://www.drip.com/pricing
- group: start
  title: ''
  type: Login
  url: https://www.getdrip.com/login
- group: operate
  title: ''
  type: Support
  url: https://help.drip.com/
- group: company
  title: ''
  type: Blog
  url: https://www.drip.com/learn
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DripEmail
created: '2026-05-11'
description: Drip is an email marketing and marketing automation platform built for ecommerce brands that combines subscriber management, segmentation, email campaigns, automation workflows, and shopper activity tracking. The Drip REST API gives programmatic access to subscribers, campaigns, events, workflows, broadcasts, orders, carts, and webhooks using either API token Basic authentication or OAuth 2.0.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/drip.png
layout: provider
modified: '2026-05-11'
name: Drip
nav: Providers
network: true
overview: 'Drip publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Broadcasts API, Campaigns API, and 7 more. Tagged areas include Email Marketing, Marketing Automation, Ecommerce, Customer Engagement, and Campaigns.


  Drip''s developer surface includes authentication, documentation, signup flow, pricing, support, engineering blog, and 6 more developer resources.'
random_paper: 26
score:
  band: thin
  composite: 31.4
  delta: -2.1
  facets:
    commercial_clarity: 23.7
    contract_quality: 53.4
    developer_ergonomics: 26.1
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 33.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/drip/refs/heads/main/screenshots/drip-2026-06-20T180233.png
security:
- kind: authentication
  name: Drip Authentication
  slug: drip-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Drip Domain Security
  slug: drip-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: drip
tags:
- Email Marketing
- Marketing Automation
- Ecommerce
- Customer Engagement
- Campaigns
- Workflows
website: https://www.drip.com
---
