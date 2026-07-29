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
  band: agent-ready
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
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.3
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Aweber Agentic Access
  operation_count: 18
  slug: aweber-agentic-access
  summary_line: 18 operations · 5 acting
api_count: 9
apis:
- description: The Accounts API from AWeber — 2 operation(s) for accounts.
  name: AWeber Accounts API
  slug: aweber-accounts-api
- description: The Broadcasts API from AWeber — 2 operation(s) for broadcasts.
  name: AWeber Broadcasts API
  slug: aweber-broadcasts-api
- description: The Campaigns API from AWeber — 1 operation(s) for campaigns.
  name: AWeber Campaigns API
  slug: aweber-campaigns-api
- description: The Custom Fields API from AWeber — 1 operation(s) for custom fields.
  name: AWeber Custom Fields API
  slug: aweber-custom-fields-api
- description: The Landing Pages API from AWeber — 1 operation(s) for landing pages.
  name: AWeber Landing Pages API
  slug: aweber-landing-pages-api
- description: The Lists API from AWeber — 2 operation(s) for lists.
  name: AWeber Lists API
  slug: aweber-lists-api
- description: The Segments API from AWeber — 1 operation(s) for segments.
  name: AWeber Segments API
  slug: aweber-segments-api
- description: The Subscribers API from AWeber — 2 operation(s) for subscribers.
  name: AWeber Subscribers API
  slug: aweber-subscribers-api
- description: The Web Forms API from AWeber — 1 operation(s) for web forms.
  name: AWeber Web Forms API
  slug: aweber-web-forms-api
artifact_total: 16
collections:
- collection_type: open
  name: AWeber REST API
  slug: open-aweber
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/aweber-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/aweber-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aweber-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aweber-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/aweber-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.aweber.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.aweber.com/docs/v3
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.aweber.com
- group: start
  title: ''
  type: Signup
  url: https://www.aweber.com/signup.htm
- group: start
  title: ''
  type: Login
  url: https://auth.aweber.com/1.0/oauth2/authorize
- group: commercial
  title: ''
  type: Pricing
  url: https://www.aweber.com/pricing.htm
- group: operate
  title: ''
  type: Support
  url: https://help.aweber.com
- group: company
  title: ''
  type: Blog
  url: https://blog.aweber.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.aweber.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aweber.com/tos.htm
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aweber.com/privacy.htm
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aweber
- group: build
  title: ''
  type: Python SDK
  url: https://github.com/aweber/AWeber-API-Python-Library
- group: build
  title: ''
  type: PHP SDK
  url: https://github.com/aweber/AWeber-API-PHP-Library
- group: build
  title: ''
  type: Ruby SDK
  url: https://github.com/aweber/AWeber-API-Ruby-Library
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/aweber-api
- group: company
  title: ''
  type: X (Twitter)
  url: https://x.com/aweber
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/AWeber
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aweber
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/AWeber
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/aweber/aweber-mcp
created: '2026-05-11'
description: AWeber is an email marketing and automation platform for small businesses, creators, and entrepreneurs providing email broadcasts, drip campaigns, landing pages, sign-up forms, and subscriber management. The AWeber REST API at api.aweber.com offers full programmatic access to lists, subscribers, broadcasts, campaigns, custom fields, segments, and tags using OAuth 2.0 authentication.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aweber.png
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: AWeber
nav: Providers
network: true
overview: 'AWeber publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Broadcasts API, Campaigns API, and 6 more. Tagged areas include Email Marketing, Marketing Automation, Email, Newsletters, and Subscribers.


  AWeber''s developer surface includes authentication, documentation, signup flow, pricing, support, engineering blog, YouTube channel, and 19 more developer resources.'
random_paper: 14
scopes:
- name: Aweber Scopes
  scope_count: 9
  slug: aweber-scopes
  summary_line: 9 scopes · authorizationCode
score:
  band: developing
  composite: 46.6
  delta: -2.1
  facets:
    commercial_clarity: 52.6
    contract_quality: 53.4
    developer_ergonomics: 63.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 48.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aweber/refs/heads/main/screenshots/aweber-2026-06-20T172736.png
security:
- kind: authentication
  name: Aweber Authentication
  slug: aweber-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Aweber Domain Security
  slug: aweber-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Aweber Trust Center
  slug: aweber-trust-center
  summary_line: PCI DSS, GDPR
slug: aweber
tags:
- Email Marketing
- Marketing Automation
- Email
- Newsletters
- Subscribers
- Campaigns
- Landing Pages
website: https://www.aweber.com
---
