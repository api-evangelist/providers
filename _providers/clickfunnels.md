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
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Clickfunnels Agentic Access
  operation_count: 9
  slug: clickfunnels-agentic-access
  summary_line: 9 operations · 6 acting
api_count: 5
apis:
- description: The Contacts API from ClickFunnels — 1 operation(s) for contacts.
  name: ClickFunnels Contacts API
  slug: clickfunnels-contacts-api
- description: The Fulfillments API from ClickFunnels — 2 operation(s) for fulfillments.
  name: ClickFunnels Fulfillments API
  slug: clickfunnels-fulfillments-api
- description: The Products API from ClickFunnels — 4 operation(s) for products.
  name: ClickFunnels Products API
  slug: clickfunnels-products-api
- description: The Teams API from ClickFunnels — 1 operation(s) for teams.
  name: ClickFunnels Teams API
  slug: clickfunnels-teams-api
- description: The Workspaces API from ClickFunnels — 1 operation(s) for workspaces.
  name: ClickFunnels Workspaces API
  slug: clickfunnels-workspaces-api
artifact_total: 10
collections:
- collection_type: open
  name: ClickFunnels 2.0 API
  slug: open-clickfunnels
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/clickfunnels-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/clickfunnels-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clickfunnels-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/clickfunnels-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/clickfunnels2
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/clickfunnels
- group: company
  title: ''
  type: Website
  url: https://www.clickfunnels.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.myclickfunnels.com
- group: docs
  title: ''
  type: APIReference
  url: https://developers.myclickfunnels.com/docs/intro
- group: commercial
  title: ''
  type: Pricing
  url: https://www.clickfunnels.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://signup.clickfunnels.com
- group: start
  title: ''
  type: Login
  url: https://app.myclickfunnels.com/sign_in
- group: auth
  title: ''
  type: Authentication
  url: https://support.myclickfunnels.com/support/solutions/articles/150000156745-accessing-the-clickfunnels-api
- group: operate
  title: ''
  type: Support
  url: https://support.myclickfunnels.com
- group: other
  title: ''
  type: Classic API
  url: https://apidocs.clickfunnels.com/
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.myclickfunnels.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.clickfunnels.com/blog/feed
created: '2026-05-11'
description: ClickFunnels is a sales funnel and online business platform that lets entrepreneurs build landing pages, sales funnels, checkout flows, courses, membership sites, and email marketing campaigns without code. The ClickFunnels 2.0 REST API gives developers programmatic access to workspaces, funnels, pages, products, contacts, orders, and subscriptions, authenticated with Bearer tokens or OAuth 2.0.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/clickfunnels.png
layout: provider
modified: '2026-05-11'
name: ClickFunnels
nav: Providers
network: true
overview: 'ClickFunnels publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Contacts API, Fulfillments API, Products API, and 2 more. Tagged areas include Sales Funnels, Landing Pages, E-commerce, Marketing, and Checkout.


  ClickFunnels'' developer surface includes authentication, documentation, API reference, pricing, signup flow, support, engineering blog, and 10 more developer resources.'
random_paper: 5
score:
  band: thin
  composite: 33.2
  delta: 0.1
  facets:
    commercial_clarity: 23.7
    contract_quality: 56.1
    developer_ergonomics: 32.6
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 33.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 28.1
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/clickfunnels/refs/heads/main/screenshots/clickfunnels-2026-06-20T174514.png
security:
- kind: authentication
  name: Clickfunnels Authentication
  slug: clickfunnels-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Clickfunnels Domain Security
  slug: clickfunnels-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Clickfunnels Vulnerability Disclosure
  slug: clickfunnels-vulnerability-disclosure
  summary_line: disclosure policy published
slug: clickfunnels
tags:
- Sales Funnels
- Landing Pages
- E-commerce
- Marketing
- Checkout
- CRM
website: https://www.clickfunnels.com
---
