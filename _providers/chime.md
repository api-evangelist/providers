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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Chime Agentic Access
  operation_count: 7
  slug: chime-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 5
apis:
- description: Legacy partner authentication
  name: Chime Authentication API
  slug: chime-authentication-api
- description: OAuth 2.0 authorization and token management
  name: Chime OAuth API
  slug: chime-oauth-api
- description: Access account statements
  name: Chime Statements API
  slug: chime-statements-api
- description: Access transaction history
  name: Chime Transactions API
  slug: chime-transactions-api
- description: Access user account information
  name: Chime Users API
  slug: chime-users-api
artifact_total: 21
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/chime-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/chime-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chime-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/chime-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.chime.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.chime.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/chimehq
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/chime-card
- group: company
  title: ''
  type: Blog
  url: https://medium.com/life-at-chime
- group: commercial
  title: ''
  type: Pricing
  url: https://chime.me/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.chime.com/
- group: other
  title: ''
  type: X
  url: https://x.com/chime
- group: commercial
  title: ''
  type: Plans
  url: plans/chime-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/chime-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/chime-finops.yml
created: '2026-06-13'
description: Chime is a neobank and fintech platform offering fee-free checking and savings accounts, early paycheck access, credit building, and peer-to-peer payment features for consumer banking. The Chime Partner API enables developers to access user account information, transaction details, account balances, statements, and payment initiation through OAuth 2.0 authentication.
examples:
- key_count: 4
  name: Get Transactions Response
  slug: get-transactions-response
- key_count: 3
  name: Get User Response
  slug: get-user-response
- key_count: 6
  name: Oauth Token Request
  slug: oauth-token-request
- key_count: 5
  name: Oauth Token Response
  slug: oauth-token-response
finops:
- name: Chime Finops
  service_category: ''
  slug: chime-finops
graphqls:
- description: Chime is a neobank and fintech platform offering fee-free checking and savings accounts, early direct deposit access, credit building, and peer-to-peer payment features for consumer banking. The Chime
  name: Chime Financial GraphQL Schema
  slug: chime-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chime.png
json_schemas:
- name: ChimeAccount
  property_count: 7
  slug: chime-account
- name: ChimeTransaction
  property_count: 9
  slug: chime-transaction
jsonld:
- class_count: 25
  name: Chime Context
  property_count: 7
  slug: chime-context
layout: provider
modified: '2026-06-13'
name: Chime
nav: Providers
network: true
overview: 'Chime publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, OAuth API, Statements API, and 2 more. Tagged areas include Fintech, Neobank, Banking, Checking Accounts, and Savings Accounts.


  The Chime catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Chime''s developer surface includes authentication, documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Chime Plans Pricing
  plan_count: 4
  slug: chime-plans-pricing
random_paper: 42
rate_limits:
- limit_count: 0
  name: Chime Rate Limits
  slug: chime-rate-limits
rules:
- name: Chime API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: chime-jsonschema-spectral-rules
score:
  band: developing
  composite: 52.2
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 66.7
    developer_ergonomics: 21.7
    discoverability: 100.0
    governance: 73.7
    operational_transparency: 21.1
  previous_composite: 52.2
  regulatory:
    applies: true
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 50.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/chime/refs/heads/main/screenshots/chime-2026-06-20T174317.png
security:
- kind: authentication
  name: Chime Authentication
  slug: chime-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Chime Domain Security
  slug: chime-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Chime Vulnerability Disclosure
  slug: chime-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: chime
tags:
- Fintech
- Neobank
- Banking
- Checking Accounts
- Savings Accounts
- Early Paycheck Access
- Credit Building
- Peer-to-Peer Payments
- Consumer Banking
website: https://www.chime.com/
---
