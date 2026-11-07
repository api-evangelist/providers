---
access_model:
  confidence: low
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
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 25.4
  scored_at: '2026-11-06'
api_count: 6
apis:
- description: Kryptos provides a Crypto Tax, Portfolio Tracker & Finance API that connects to over 5,000 integrations across exchanges, wallets, and blockchains.
  name: Kryptos API
  slug: kryptos-api
- baseURL: https://api-v2.kryptos.io
  baseurl_source: declared
  description: 'kryptos-io api API as documented publicly: 49 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: kryptos-io api API
  slug: api-api
- baseURL: https://api-v2.kryptos.io
  baseurl_source: declared
  description: 'kryptos-io authentication API as documented publicly: 4 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: kryptos-io authentication API
  slug: authentication-api
- baseURL: https://api-v2.kryptos.io
  baseurl_source: declared
  description: 'kryptos-io core API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: kryptos-io core API
  slug: core-api
- baseURL: https://api-v2.kryptos.io
  baseurl_source: declared
  description: 'kryptos-io kryptos connect API as documented publicly: 7 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: kryptos-io kryptos connect API
  slug: kryptos-connect-api
- baseURL: https://api-v2.kryptos.io
  baseurl_source: declared
  description: 'kryptos-io reference API as documented publicly: 5 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: kryptos-io reference API
  slug: reference-api
artifact_total: 30
common:
- group: design
  href: https://artifacts.apis.io/kryptos-io/rules/kryptos-io-rules.yml
  title: ''
  type: Spectral
  url: rules/kryptos-io-rules.yml
- group: design
  href: https://artifacts.apis.io/kryptos-io/json-ld/kryptos-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/kryptos-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/kryptos-io/vocabulary/kryptos-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/kryptos-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/kryptos-io/data-model/kryptos-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/kryptos-io-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://kryptos.io/
- group: auth
  href: https://artifacts.apis.io/kryptos-io/authentication/kryptos-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/kryptos-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/kryptos-io/errors/kryptos-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/kryptos-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/kryptos-io/conformance/kryptos-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/kryptos-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/kryptos-io/llms/kryptos-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/kryptos-io-llms.txt
- group: auth
  href: https://artifacts.apis.io/kryptos-io/well-known/kryptos-io-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/kryptos-io-help-security.txt
- group: agent
  href: https://artifacts.apis.io/kryptos-io/well-known/kryptos-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/kryptos-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/kryptos-io/hosts/kryptos-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kryptos-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/kryptos-io/vendors/kryptos-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/kryptos-io-vendors.yml
- group: build
  href: https://artifacts.apis.io/kryptos-io/packages/kryptos-io-packages.yml
  title: ''
  type: SDKs
  url: packages/kryptos-io-packages.yml
- group: build
  href: https://artifacts.apis.io/kryptos-io/packages/kryptos-io-packages.yml
  title: ''
  type: Packages
  url: packages/kryptos-io-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://kryptos.io/terms-of-services
- group: operate
  title: ''
  type: Support
  url: https://help.kryptos.io/en/
- group: start
  title: ''
  type: SignUp
  url: https://app.kryptos.io/signup
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kryptos.io/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://kryptos.io/blog-categories/press
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.kryptos.io/docs/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://kryptos.io/guides/carf-self-certification-tin-validation-onboarding
- group: auth
  href: https://artifacts.apis.io/kryptos-io/security/kryptos-io-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/kryptos-io-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/kryptos-io/security/kryptos-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kryptos-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kryptos.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.kryptos.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dashboard.kryptos.io/
- group: company
  title: ''
  type: Blog
  url: https://kryptos.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Kryptoskatt
- group: commercial
  title: ''
  type: Pricing
  url: https://kryptos.io/pricing
- group: docs
  title: ''
  type: APIReference
  url: https://docs.kryptos.io/docs/api/overview
created: '2026-10-30'
description: Kryptos provides a Crypto Tax, Portfolio Tracker and Finance API that connects to over 5,000 integrations across exchanges, wallets, and blockchains. It enables developers to pull holdings, transactions, DeFi, NFT and tax data through a unified endpoint, serving individuals, enterprises, and developers.
image: https://cdn.sanity.io/images/69b8yewa/production/be302a2ed72e23acfcedc055c2b46c37ff2d79b8-1200x630.png?auto=format
json_schemas:
- name: GetHealthResponse
  property_count: 1
  slug: kryptos-io-get-health-response
- name: GetOidcUserinfoResponse
  property_count: 6
  slug: kryptos-io-get-oidc-userinfo-response
- name: GetTokenGrantsResponse
  property_count: 2
  slug: kryptos-io-get-token-grants-response
- name: GetV1DefiResponse
  property_count: 6
  slug: kryptos-io-get-v1-defi-response
- name: GetV1IntegrationsResponse
  property_count: 26
  slug: kryptos-io-get-v1-integrations-response
- name: GetV1LedgersResponse
  property_count: 2
  slug: kryptos-io-get-v1-ledgers-response
- name: GetV1ProvidersResponse
  property_count: 19
  slug: kryptos-io-get-v1-providers-response
- name: GetV1SyncSyncidResponse
  property_count: 3
  slug: kryptos-io-get-v1-sync-syncid-response
- name: GetV1TransactionsIdResponse
  property_count: 30
  slug: kryptos-io-get-v1-transactions-id-response
- name: GetV1TransactionsResponse
  property_count: 24
  slug: kryptos-io-get-v1-transactions-response
- name: PostDeveloperIntegrationsWalletidResyncRequest
  property_count: 2
  slug: kryptos-io-post-developer-integrations-walletid-resync-request
- name: PostDeveloperIntegrationsWalletidResyncResponse
  property_count: 6
  slug: kryptos-io-post-developer-integrations-walletid-resync-response
- name: PostLinkTokenRequest
  property_count: 2
  slug: kryptos-io-post-link-token-request
- name: PostLinkTokenResponse
  property_count: 5
  slug: kryptos-io-post-link-token-response
- name: PostMcpResponse
  property_count: 4
  slug: kryptos-io-post-mcp-response
- name: PostOidcTokenResponse
  property_count: 6
  slug: kryptos-io-post-oidc-token-response
- name: PostOidcTokenRevocationResponse
  property_count: 6
  slug: kryptos-io-post-oidc-token-revocation-response
- name: PostTokenExchangeResponse
  property_count: 6
  slug: kryptos-io-post-token-exchange-response
jsonld:
- class_count: 54
  name: Kryptos Io Context
  property_count: 154
  slug: kryptos-io-context
layout: provider
modified: '2026-10-30'
name: kryptos-io
nav: Providers
network: true
overview: 'kryptos-io is listed with 6 APIs on the [APIs.io](https://apis.io/) network, including api API, authentication API, core API, and 3 more. Tagged areas include Cryptocurrency, Finance, Portfolio, and Tax.


  The kryptos-io catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  kryptos-io''s developer surface includes authentication, support, signup flow, changelog, getting-started guide, documentation, engineering blog, and 24 more developer resources.'
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: kryptos-io API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: kryptos-io-rules
scopes:
- name: Kryptos Io Scopes
  scope_count: 0
  slug: kryptos-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 35.0
  coverage:
    artifact_dirs: 27
    catalog_earned: 55.8
    catalog_earned_first_party: 0.0
    catalog_gap: 59.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -13.1
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 25.5
    developer_ergonomics: 41.7
    discoverability: 54.5
    operational_transparency: 21.1
  previous_composite: 48.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/kryptos-io/kryptos-io-2026-11-03T134538.png
security:
- kind: authentication
  name: Kryptos Io Authentication
  slug: kryptos-io-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Kryptos Io Domain Security
  slug: kryptos-io-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Kryptos Io Trust Center
  slug: kryptos-io-trust-center
  summary_line: SOC 2, ISO 27001
slug: kryptos-io
tags:
- Cryptocurrency
- Finance
- Portfolio
- Tax
website: https://kryptos.io/
---
