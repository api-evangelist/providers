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
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.6
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Elliptic Agentic Access
  operation_count: 40
  slug: elliptic-agentic-access
  summary_line: 40 operations · 16 acting
api_count: 6
apis:
- baseURL: https://aml-api.elliptic.co
  baseurl_source: declared
  description: The Assets API from Elliptic — 1 operation(s) for assets.
  name: Elliptic Assets API
  slug: elliptic-assets-api
- baseURL: https://aml-api.elliptic.co
  baseurl_source: declared
  description: The Count Analyses API from Elliptic — 1 operation(s) for count analyses.
  name: Elliptic Count Analyses API
  slug: elliptic-count-analyses-api
- baseURL: https://aml-api.elliptic.co
  baseurl_source: declared
  description: Retrieve all criteria related to triggering risk rules
  name: Elliptic Criteria API
  slug: elliptic-criteria-api
- baseURL: https://aml-api.elliptic.co
  baseurl_source: declared
  description: 'The customers endpoints are used to manage customers which you have associated analysis with, via the `customer_reference` analysis subject attribute. Currently, the customers endpoints only refer to '
  name: Elliptic Customers API
  slug: elliptic-customers-api
- baseURL: https://aml-api.elliptic.co
  baseurl_source: declared
  description: Health check endpoints
  name: Elliptic Health API
  slug: elliptic-health-api
- baseURL: https://aml-api.elliptic.co
  baseurl_source: declared
  description: Manage risk rules. Currently the same risk rules are used for Navigator and Lens
  name: Elliptic Risk Rules API
  slug: elliptic-risk-rules-api
- baseURL: https://aml-api.elliptic.co
  baseurl_source: declared
  description: The Sanctions API from Elliptic — 1 operation(s) for sanctions.
  name: Elliptic Sanctions API
  slug: elliptic-sanctions-api
- baseURL: https://aml-api.elliptic.co
  baseurl_source: declared
  description: Wallet and transaction screening endpoints
  name: Elliptic Screenings API
  slug: elliptic-screenings-api
- baseURL: https://aml-api.elliptic.co
  baseurl_source: declared
  description: Run blockchain analysis against one or more transactions. Get and update previously run analyses.
  name: Elliptic Transaction Analyses API
  slug: elliptic-transaction-analyses-api
- baseURL: https://aml-api.elliptic.co
  baseurl_source: declared
  description: The Transaction Workflow API from Elliptic — 3 operation(s) for transaction workflow.
  name: Elliptic Transaction Workflow API
  slug: elliptic-transaction-workflow-api
- baseURL: https://aml-api.elliptic.co
  baseurl_source: declared
  description: Tron blockchain data lookup operations
  name: Elliptic Tron NodeIntelligence API
  slug: elliptic-tron-nodeintelligence-api
- baseURL: https://aml-api.elliptic.co
  baseurl_source: declared
  description: Manage users
  name: Elliptic Users API
  slug: elliptic-users-api
- baseURL: https://aml-api.elliptic.co
  baseurl_source: declared
  description: Run blockchain analysis against one or more wallets. Get and update previously run analyses.
  name: Elliptic Wallet Analyses API
  slug: elliptic-wallet-analyses-api
- baseURL: https://aml-api.elliptic.co
  baseurl_source: declared
  description: The Wallet Analyses Count API from Elliptic — 1 operation(s) for wallet analyses count.
  name: Elliptic Wallet Analyses Count API
  slug: elliptic-wallet-analyses-count-api
- baseURL: https://aml-api.elliptic.co
  baseurl_source: declared
  description: The Wallet API from Elliptic — 1 operation(s) for wallet.
  name: Elliptic Wallet API
  slug: elliptic-wallet-api
- baseURL: https://aml-api.elliptic.co
  baseurl_source: declared
  description: The Wallet Workflow API from Elliptic — 2 operation(s) for wallet workflow.
  name: Elliptic Wallet Workflow API
  slug: elliptic-wallet-workflow-api
artifact_total: 40
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: AML API OAuth Assets API
  slug: open-elliptic-assets-api
- collection_type: open
  name: AML API OAuth Assets Count Analyses API
  slug: open-elliptic-count-analyses-api
- collection_type: open
  name: AML API OAuth Assets Criteria API
  slug: open-elliptic-criteria-api
- collection_type: open
  name: AML API OAuth Assets Customers API
  slug: open-elliptic-customers-api
- collection_type: open
  name: AML API OAuth Assets Health API
  slug: open-elliptic-health-api
- collection_type: open
  name: AML API OAuth Assets Risk Rules API
  slug: open-elliptic-risk-rules-api
- collection_type: open
  name: AML API OAuth Assets Sanctions API
  slug: open-elliptic-sanctions-api
- collection_type: open
  name: AML API OAuth Assets Screenings API
  slug: open-elliptic-screenings-api
- collection_type: open
  name: AML API OAuth Assets Transaction Analyses API
  slug: open-elliptic-transaction-analyses-api
- collection_type: open
  name: AML API OAuth Assets Transaction Workflow API
  slug: open-elliptic-transaction-workflow-api
- collection_type: open
  name: AML API OAuth Assets Tron NodeIntelligence API
  slug: open-elliptic-tron-nodeintelligence-api
- collection_type: open
  name: AML API OAuth Assets Users API
  slug: open-elliptic-users-api
- collection_type: open
  name: AML API OAuth Assets Wallet Analyses API
  slug: open-elliptic-wallet-analyses-api
- collection_type: open
  name: AML API OAuth Assets Wallet Analyses Count API
  slug: open-elliptic-wallet-analyses-count-api
- collection_type: open
  name: AML API OAuth Assets Wallet Workflow API
  slug: open-elliptic-wallet-workflow-api
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
random_paper: 14
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
  band: developing
  composite: 39.4
  coverage:
    artifact_dirs: 12
    catalog_earned: 56.0
    catalog_earned_first_party: 0.0
    catalog_gap: 59.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 59.3
    developer_ergonomics: 34.5
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 39.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 48.4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
