---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Monerium Agentic Access
  operation_count: 35
  slug: monerium-agentic-access
  summary_line: 35 operations · 17 acting
api_count: 2
apis:
- baseURL: https://api.monerium.app
  baseurl_source: declared
  description: API for developers to integrate Monerium payments, wallets, and user onboarding functionalities.
  name: Monerium API
  slug: monerium-api
artifact_total: 21
asyncapis:
- description: ''
  name: Monerium Webhooks
  slug: monerium-webhooks
common:
- group: operate
  href: https://artifacts.apis.io/monerium/changelog/monerium-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/monerium-changelog.yml
- group: start
  href: https://artifacts.apis.io/monerium/sandbox/monerium-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/monerium-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/monerium/authentication/monerium-authentication.yml
  title: ''
  type: Authentication
  url: authentication/monerium-authentication.yml
- group: design
  href: https://artifacts.apis.io/monerium/conformance/monerium-conformance.yml
  title: ''
  type: Conformance
  url: conformance/monerium-conformance.yml
- group: other
  href: https://artifacts.apis.io/monerium/hosts/monerium-hosts.yml
  title: ''
  type: Hosts
  url: hosts/monerium-hosts.yml
- group: other
  href: https://artifacts.apis.io/monerium/vendors/monerium-vendors.yml
  title: ''
  type: Vendors
  url: vendors/monerium-vendors.yml
- group: build
  href: https://artifacts.apis.io/monerium/packages/monerium-packages.yml
  title: ''
  type: Packages
  url: packages/monerium-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://help.monerium.com/
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@monerium/sdk
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://monerium.com/policies/privacy-notice/
- group: company
  title: ''
  type: Newsroom
  url: https://monerium.com/press/
- group: other
  title: ''
  type: Leadership
  url: https://monerium.com/team/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/monerium/
- group: auth
  href: https://artifacts.apis.io/monerium/security/monerium-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/monerium-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://monerium.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.monerium.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.monerium.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.monerium.com/api/
- group: company
  title: ''
  type: Blog
  url: https://monerium.com/blog/
created: '2026-10-27'
description: Monerium provides regulated digital money on blockchain, enabling businesses to issue e‑money, automate SEPA payments, and integrate fiat‑backed stablecoins into on‑chain applications. Their API lets developers create accounts, issue tokens, and manage transfers while complying with financial regulations.
image: https://monerium.com/images/monerium-social.jpg
json_schemas:
- name: CorporateDetails
  property_count: 13
  slug: monerium-corporate-details
- name: CorporateForm
  property_count: 7
  slug: monerium-corporate-form
- name: Order
  property_count: 12
  slug: monerium-order
- name: Payment
  property_count: 13
  slug: monerium-payment
- name: PersonalForm
  property_count: 14
  slug: monerium-personal-form
- name: SwapQuote
  property_count: 19
  slug: monerium-swap-quote
jsonld:
- class_count: 42
  name: Monerium Context
  property_count: 106
  slug: monerium-context
layout: provider
modified: '2026-10-27'
name: Monerium
nav: Providers
network: true
overview: 'Monerium publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Fintech, Payments, Blockchain, Digital Currency, and RegulatedMoney.


  The Monerium catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Monerium''s developer surface includes changelog, sandbox, authentication, support, documentation, API reference, engineering blog, and 12 more developer resources.'
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: Monerium API Rules
  rule_count: 17
  severity_counts:
    error: 10
    hint: 0
    info: 2
    warn: 5
  slug: monerium-rules
scopes:
- name: Monerium Scopes
  scope_count: 0
  slug: monerium-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 38.2
  coverage:
    artifact_dirs: 30
    catalog_earned: 52.5
    catalog_earned_first_party: 0.0
    catalog_gap: 62.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.1
  facets:
    access_clarity: 5.3
    contract_governance: 18.2
    contract_quality: 56.6
    developer_ergonomics: 42.9
    discoverability: 67.9
    operational_transparency: 18.4
  previous_composite: 43.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 25.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/monerium/monerium-2026-11-03T135827.png
security:
- kind: authentication
  name: Monerium Authentication
  slug: monerium-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Monerium Domain Security
  slug: monerium-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 7
skills:
- name: auth-token
  slug: monerium-auth-token
- name: auth
  slug: monerium-auth
- name: create-profile
  slug: monerium-create-profile
- name: create-subscription
  slug: monerium-create-subscription
- name: get-countries
  slug: monerium-get-countries
- name: list-subscriptions
  slug: monerium-list-subscriptions
- name: welcome
  slug: monerium-welcome
slug: monerium
tags:
- Fintech
- Payments
- Blockchain
- Digital Currency
- RegulatedMoney
website: https://monerium.com/
---
