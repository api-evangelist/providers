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
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.3
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Urbanfox Agentic Access
  operation_count: 14
  slug: urbanfox-agentic-access
  summary_line: 14 operations · 6 acting
api_count: 1
apis:
- baseURL: https://api.demo-retail.urbanfox.io
  baseurl_source: declared
  description: Fraud case retrieval and updates.
  name: UrbanFox Cases API
  slug: urbanfox-cases-api
- baseURL: https://api.demo-retail.urbanfox.io
  baseurl_source: declared
  description: End-user account retrieval, creation, updates, and deletion.
  name: UrbanFox End User Accounts API
  slug: urbanfox-end-user-accounts-api
- baseURL: https://api.demo-retail.urbanfox.io
  baseurl_source: declared
  description: Aggregated tenant metrics and time-series reporting.
  name: UrbanFox Metrics API
  slug: urbanfox-metrics-api
- baseURL: https://api.demo-retail.urbanfox.io
  baseurl_source: declared
  description: Tenant integration snippet retrieval.
  name: UrbanFox Snippet API
  slug: urbanfox-snippet-api
- baseURL: https://api.demo-retail.urbanfox.io
  baseurl_source: declared
  description: Tenant details and tenant authentication credentials.
  name: UrbanFox Tenants API
  slug: urbanfox-tenants-api
- baseURL: https://api.demo-retail.urbanfox.io
  baseurl_source: declared
  description: OAuth token generation for machine-to-machine authentication.
  name: UrbanFox O Auth API
  slug: urbanfox-oauth-api
artifact_total: 21
collections:
- collection_type: open
  name: UrbanFox Customer Cases API
  slug: open-urbanfox-cases-api
- collection_type: open
  name: UrbanFox Customer Cases End User Accounts API
  slug: open-urbanfox-end-user-accounts-api
- collection_type: open
  name: UrbanFox Customer Cases Metrics API
  slug: open-urbanfox-metrics-api
- collection_type: open
  name: UrbanFox Customer Cases OAuth API
  slug: open-urbanfox-oauth-api
- collection_type: open
  name: UrbanFox Customer Cases Snippet API
  slug: open-urbanfox-snippet-api
- collection_type: open
  name: UrbanFox Customer Cases Tenants API
  slug: open-urbanfox-tenants-api
common:
- group: commercial
  href: https://artifacts.apis.io/urbanfox/plans/urbanfox-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/urbanfox-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/urbanfox/overlays/urbanfox-customer-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/urbanfox-customer-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://urbanfox.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.urbanfox.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.urbanfox.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.urbanfox.io/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.urbanfox.io/tutorials/first-api-call
- group: operate
  title: ''
  type: Support
  url: https://docs.urbanfox.io/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.urbanfox.io/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.urbanfox.io/
- group: start
  title: ''
  type: SignUp
  url: https://2ffr2z.share-eu1.hsforms.com/2wcLUdqqOSWOmGkVadK7V0g
- group: agent
  href: https://artifacts.apis.io/urbanfox/llms/urbanfox-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/urbanfox-llms.txt
- group: auth
  href: https://artifacts.apis.io/urbanfox/authentication/urbanfox-authentication.yml
  title: ''
  type: Authentication
  url: authentication/urbanfox-authentication.yml
- group: auth
  href: https://artifacts.apis.io/urbanfox/scopes/urbanfox-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/urbanfox-scopes.yml
- group: auth
  href: https://artifacts.apis.io/urbanfox/security/urbanfox-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/urbanfox-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/urbanfox/agentic-access/urbanfox-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/urbanfox-agentic-access.yml
- group: agent
  href: https://artifacts.apis.io/urbanfox/mcp/urbanfox-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/urbanfox-mcp.yml
- group: design
  href: https://artifacts.apis.io/urbanfox/conformance/urbanfox-conformance.yml
  title: ''
  type: Conformance
  url: conformance/urbanfox-conformance.yml
- group: design
  href: https://artifacts.apis.io/urbanfox/errors/urbanfox-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/urbanfox-problem-types.yml
- group: design
  href: https://artifacts.apis.io/urbanfox/lifecycle/urbanfox-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/urbanfox-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/urbanfox/conventions/urbanfox-conventions.yml
  title: ''
  type: Conventions
  url: conventions/urbanfox-conventions.yml
- group: design
  href: https://artifacts.apis.io/urbanfox/components/urbanfox-components.yml
  title: ''
  type: Components
  url: components/urbanfox-components.yml
- group: design
  href: https://artifacts.apis.io/urbanfox/data-model/urbanfox-data-model.yml
  title: ''
  type: DataModel
  url: data-model/urbanfox-data-model.yml
- group: build
  href: https://artifacts.apis.io/urbanfox/packages/urbanfox-packages.yml
  title: ''
  type: Packages
  url: packages/urbanfox-packages.yml
- group: agent
  href: https://artifacts.apis.io/urbanfox/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: UrbanFox is an AI-powered online payment fraud detection and prevention platform that uses generative AI and behavioral intelligence - rather than static rule-sets - to detect payment fraud, account takeover, and bot traffic across transactions, sessions, and accounts. The Techstars-backed company ships a tenant-scoped Customer API (OAuth 2.0 client credentials) for fraud case management, end-user account management, activity metrics, credential rotation, and clickstream collector integration.
image: https://www.urbanfox.io/hubfs/Favicon.png
layout: provider
modified: '2026-07-21'
name: UrbanFox
nav: Providers
network: true
overview: 'UrbanFox publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Cases API, End User Accounts API, Metrics API, and 3 more. Tagged areas include Fraud Prevention, Payment Fraud, Account Takeover, Bot Detection, and Risk Management.


  UrbanFox''s developer surface includes documentation, API reference, getting-started guide, support, pricing, signup flow, authentication, and 18 more developer resources.'
plans:
- name: Urbanfox Plans Pricing
  plan_count: 0
  slug: urbanfox-plans-pricing
random_paper: 5
scopes:
- name: Urbanfox Scopes
  scope_count: 13
  slug: urbanfox-scopes
  summary_line: 13 scopes · clientCredentials
score:
  band: developing
  composite: 40.0
  coverage:
    artifact_dirs: 22
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 55.1
    developer_ergonomics: 56.5
    discoverability: 66.1
    operational_transparency: 0.0
  previous_composite: 40.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 25.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/urbanfox/urbanfox-2026-08-17T082646.png
security:
- kind: authentication
  name: Urbanfox Authentication
  slug: urbanfox-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Urbanfox Domain Security
  slug: urbanfox-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 4
skills:
- name: Authenticate and list fraud cases
  slug: urbanfox-authenticate-and-list-cases
- name: Investigate and close a fraud case
  slug: urbanfox-investigate-and-close-case
- name: Manage end-user accounts
  slug: urbanfox-manage-end-user-accounts
- name: Query tenant activity metrics
  slug: urbanfox-query-metrics
slug: urbanfox
tags:
- Fraud Prevention
- Payment Fraud
- Account Takeover
- Bot Detection
- Risk Management
- Security
- Artificial Intelligence
- E-Commerce
website: https://urbanfox.io/
---
