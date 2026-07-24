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
    agent_skills: true
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 46.2
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Snackmagic Agentic Access
  operation_count: 15
  slug: snackmagic-agentic-access
  summary_line: 15 operations · 8 acting
api_count: 5
apis:
- description: 'Stadium uses JWT (as Bearer token) for authentication. API provides 4 different methods to generate the token: 1. Client Credentials 2. Authorization Code (OAuth2) 3. Authorization Code using PKCE 4. '
  name: SnackMagic Authentication API
  slug: snackmagic-authentication-api
- description: Automation related API endpoints
  name: SnackMagic Automation management API
  slug: snackmagic-automation-management-api
- description: Order related API endpoints
  name: SnackMagic Order management API
  slug: snackmagic-order-management-api
- description: Store related API endpoints
  name: SnackMagic Store management API
  slug: snackmagic-store-management-api
- description: User related API endpoints
  name: SnackMagic User management API
  slug: snackmagic-user-management-api
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://snackmagic.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.bystadium.com/api-integrations
- group: docs
  title: ''
  type: Documentation
  url: https://api.bystadium.com/api/v2/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.bystadium.com/api/v2/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.bystadium.com/api-integrations
- group: auth
  title: ''
  type: Authentication
  url: authentication/snackmagic-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/snackmagic-agentic-access.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/snackmagic-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/snackmagic-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.bystadium.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bystadium.com
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bystadium.com/go/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.bystadium.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bystadium.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bystadium.com/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.bystadium.com/blog
- group: operate
  title: ''
  type: Support
  url: https://help.bystadium.com/hc
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/snackmagic
- group: other
  title: ''
  type: Wallet
  url: https://www.bystadium.com/wallet
created: '2026-07-17'
description: SnackMagic is a 100% customizable snack-box gifting service, now part of Stadium, that lets recipients build their own box from 500+ snacks and beverages or receive curated gifts, delivered worldwide. Companies use it for employee, client, prospect, and event gifting. SnackMagic is exposed to developers through the Stadium API (api.bystadium.com), a JSON REST API for embedding a global gift, rewards, and branded-swag catalog, placing orders funded by a pre-purchased Wallet balance, sending Stadium Shop points via treat links, and triggering webhook-automation gift orders. This profile was enriched from the provider's public OpenAPI and developer surface.
image: https://fecdn.snackmagic.com/static/media/snackmagic-logo.b9e03ebf.svg
layout: provider
modified: '2026-07-21'
name: SnackMagic
nav: Providers
network: true
overview: 'SnackMagic publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Automation management API, Order management API, and 2 more. Tagged areas include Company, Consumer, Gifting, Rewards, and Swag.


  SnackMagic''s developer surface includes documentation, API reference, getting-started guide, authentication, pricing, signup flow, engineering blog, and 13 more developer resources.'
random_paper: 21
score:
  band: developing
  composite: 50.6
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 62.5
    developer_ergonomics: 58.7
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 50.6
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Snackmagic Authentication
  slug: snackmagic-authentication
  summary_line: http/apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Snackmagic Domain Security
  slug: snackmagic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Snackmagic Trust Center
  slug: snackmagic-trust-center
  summary_line: trust center published
slug: snackmagic
tags:
- Company
- Consumer
- Gifting
- Rewards
- Swag
- Snacks
- E-Commerce
- Fulfillment
website: https://snackmagic.com
---
