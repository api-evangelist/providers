---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
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
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Elliptic Agentic Access
  operation_count: 40
  slug: elliptic-agentic-access
  summary_line: 40 operations · 16 acting
api_count: 16
apis:
- description: The Assets API from Elliptic — 1 operation(s) for assets.
  name: Elliptic Assets API
  slug: elliptic-assets-api
- description: The Count Analyses API from Elliptic — 1 operation(s) for count analyses.
  name: Elliptic Count Analyses API
  slug: elliptic-count-analyses-api
- description: Retrieve all criteria related to triggering risk rules
  name: Elliptic Criteria API
  slug: elliptic-criteria-api
- description: 'The customers endpoints are used to manage customers which you have associated analysis with, via the `customer_reference` analysis subject attribute. Currently, the customers endpoints only refer to '
  name: Elliptic Customers API
  slug: elliptic-customers-api
- description: Health check endpoints
  name: Elliptic Health API
  slug: elliptic-health-api
- description: Manage risk rules. Currently the same risk rules are used for Navigator and Lens
  name: Elliptic Risk Rules API
  slug: elliptic-risk-rules-api
- description: The Sanctions API from Elliptic — 1 operation(s) for sanctions.
  name: Elliptic Sanctions API
  slug: elliptic-sanctions-api
- description: Wallet and transaction screening endpoints
  name: Elliptic Screenings API
  slug: elliptic-screenings-api
- description: Run blockchain analysis against one or more transactions. Get and update previously run analyses.
  name: Elliptic Transaction Analyses API
  slug: elliptic-transaction-analyses-api
- description: The Transaction Workflow API from Elliptic — 3 operation(s) for transaction workflow.
  name: Elliptic Transaction Workflow API
  slug: elliptic-transaction-workflow-api
- description: Tron blockchain data lookup operations
  name: Elliptic Tron NodeIntelligence API
  slug: elliptic-tron-nodeintelligence-api
- description: Manage users
  name: Elliptic Users API
  slug: elliptic-users-api
- description: Run blockchain analysis against one or more wallets. Get and update previously run analyses.
  name: Elliptic Wallet Analyses API
  slug: elliptic-wallet-analyses-api
- description: The Wallet Analyses Count API from Elliptic — 1 operation(s) for wallet analyses count.
  name: Elliptic Wallet Analyses Count API
  slug: elliptic-wallet-analyses-count-api
- description: The Wallet API from Elliptic — 1 operation(s) for wallet.
  name: Elliptic Wallet API
  slug: elliptic-wallet-api
- description: The Wallet Workflow API from Elliptic — 2 operation(s) for wallet workflow.
  name: Elliptic Wallet Workflow API
  slug: elliptic-wallet-workflow-api
artifact_total: 24
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/elliptic-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/elliptic-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/elliptic-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/elliptic-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://developers.elliptic.co/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.elliptic.co/docs
- group: auth
  title: ''
  type: Authentication
  url: https://developers.elliptic.co/docs/authentication-1
- group: build
  title: ''
  type: SDKs
  url: https://developers.elliptic.co/docs/quick-start-sdks
- group: operate
  title: ''
  type: Status
  url: https://status.elliptic.co/
- group: company
  title: ''
  type: Blog
  url: https://www.elliptic.co/blog
- group: operate
  title: ''
  type: Support
  url: https://help.elliptic.co/
- group: other
  title: ''
  type: Dashboard
  url: https://app.elliptic.co
- group: company
  title: ''
  type: Partners
  url: https://www.elliptic.co/partner-program
- group: operate
  title: ''
  type: Contact
  url: https://www.elliptic.co/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.elliptic.co/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.elliptic.co/terms-of-service
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/elliptic/refs/heads/main/json-ld/elliptic.jsonld
created: '2026-06-14'
description: Elliptic is a blockchain analytics and crypto compliance platform providing REST APIs for transaction screening, wallet risk scoring, entity identification, and AML compliance. Their APIs enable financial institutions, exchanges, and DeFi platforms to automate crypto risk screening across 60+ blockchains, reduce investigation time by up to 90%, and meet AML regulatory requirements with sub-second response times.
finops:
- name: Elliptic Finops
  service_category: ''
  slug: elliptic-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/elliptic.png
jsonld:
- class_count: 0
  name: Elliptic Context
  property_count: 0
  slug: elliptic
layout: provider
modified: '2026-06-14'
name: Elliptic
nav: Providers
network: true
overview: 'Elliptic publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Assets API, Count Analyses API, Criteria API, and 13 more. Tagged areas include Blockchain, Crypto, Compliance, AML, and Transaction Screening.


  The Elliptic catalog on APIs.io includes 1 JSON-LD context.


  Elliptic''s developer surface includes authentication, developer portal, documentation, status page, engineering blog, support, and 11 more developer resources.'
plans:
- name: Elliptic Plans
  plan_count: 1
  slug: elliptic-plans
random_paper: 54
rate_limits:
- limit_count: 0
  name: Aml Api
  slug: aml-api
scopes:
- name: Elliptic Scopes
  scope_count: 2
  slug: elliptic-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: thin
  composite: 40.4
  delta: -2.5
  facets:
    commercial_clarity: 50.0
    contract_quality: 59.1
    developer_ergonomics: 41.3
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 42.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/elliptic/refs/heads/main/screenshots/elliptic-2026-06-20T180613.png
security:
- kind: authentication
  name: Elliptic Authentication
  slug: elliptic-authentication
  summary_line: apiKey/http/oauth2 · 5 schemes
- kind: domain-security
  name: Elliptic Domain Security
  slug: elliptic-domain-security
  summary_line: TLSv1.3 · DMARC
slug: elliptic
tags:
- Blockchain
- Crypto
- Compliance
- AML
- Transaction Screening
- Wallet Screening
- Risk Scoring
- Analytics
website: https://developers.elliptic.co/
---
