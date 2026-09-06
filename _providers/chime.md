---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.5
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Chime Agentic Access
  operation_count: 7
  slug: chime-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 1
apis:
- baseURL: https://api.chimebank.com/chime/v1
  baseurl_source: declared
  description: Legacy partner authentication
  name: Chime Authentication API
  slug: chime-authentication-api
- baseURL: https://api.chimebank.com/chime/v1
  baseurl_source: declared
  description: OAuth 2.0 authorization and token management
  name: Chime OAuth API
  slug: chime-oauth-api
- baseURL: https://api.chimebank.com/chime/v1
  baseurl_source: declared
  description: Access account statements
  name: Chime Statements API
  slug: chime-statements-api
- baseURL: https://api.chimebank.com/chime/v1
  baseurl_source: declared
  description: Access transaction history
  name: Chime Transactions API
  slug: chime-transactions-api
- baseURL: https://api.chimebank.com/chime/v1
  baseurl_source: declared
  description: Access user account information
  name: Chime Users API
  slug: chime-users-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Chime Partner Authentication API
  slug: open-chime-authentication-api
- collection_type: open
  name: Chime Partner Authentication OAuth API
  slug: open-chime-oauth-api
- collection_type: open
  name: Chime Partner Authentication Statements API
  slug: open-chime-statements-api
- collection_type: open
  name: Chime Partner Authentication Transactions API
  slug: open-chime-transactions-api
- collection_type: open
  name: Chime Partner Authentication Users API
  slug: open-chime-users-api
common:
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.chime.com/changelog
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


  Chime''s developer surface includes changelog, authentication, documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Chime Plans Pricing
  plan_count: 4
  slug: chime-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Chime Rate Limits
  slug: chime-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Chime API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: chime-jsonschema-spectral-rules
score:
  band: developing
  composite: 44.6
  coverage:
    artifact_dirs: 16
    catalog_earned: 63.3
    catalog_earned_first_party: 0.0
    catalog_gap: 51.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 9.8
    contract_quality: 65.4
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 36.8
  previous_composite: 44.6
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
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 29.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
