---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 42.6
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 64
  human_in_the_loop: 1
  name: Tzero Agentic Access
  operation_count: 135
  slug: tzero-agentic-access
  summary_line: 135 operations · 64 acting · 1 human-in-the-loop
api_count: 3
apis:
- baseURL: https://gateway-web-api.tzero.com/app
  baseurl_source: declared
  description: REST/JSON API for creating individual broker-dealer accounts, triggering and reviewing KYC on investors, browsing primary offerings and managing investments, linking bank accounts and moving funds, re
  name: tZERO Issuance & Secondary Markets API
  slug: issuance-secondary-markets
- baseURL: https://api.t0direct.com/api/v1
  baseurl_source: declared
  description: 'REST/JSON API giving institutional issuers and partners programmatic access to tZERO transfer-agent, tokenization and custody operations: investors and holdings, securities and cap tables, book-entry '
  name: tZERO Institutional API
  slug: institutional
- description: FIX 4.2 / 4.4 protocol surface for low-latency order entry, drop-copy execution reports, market data (snapshot and incremental refresh, trading session status, security status) and Indication of Inter
  name: tZERO FIX API
  slug: fix
artifact_total: 9
asyncapis:
- description: ''
  name: Tzero Institutional Webhooks
  slug: tzero-institutional-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tzero-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tzero-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tzero-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.tzero.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apidocs.tzero.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.tzero.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.tzero.com/docs/explorer
- group: start
  title: ''
  type: GettingStarted
  url: https://apidocs.tzero.com/docs
- group: operate
  title: ''
  type: Support
  url: https://www.tzero.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.tzero.com/content-hub
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tZERO-dev
- group: start
  title: ''
  type: SignUp
  url: https://platform.tzero.com/tzero/register
- group: start
  title: ''
  type: Login
  url: https://platform.tzero.com/tzero/auth
- group: commercial
  title: ''
  type: TermsOfService
  url: https://storage.googleapis.com/public-disclosures.tzero.com/tZERO_MasterTermsofUse.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://storage.googleapis.com/public-disclosures.tzero.com/Privacy-Policy-and-Privacy-Notices-(TDAS-and-tZERO-Securities).pdf
- group: commercial
  title: ''
  type: LegalHub
  url: https://www.tzero.com/legal
- group: other
  title: ''
  type: Company
  url: https://www.tzero.com/company
- group: company
  title: ''
  type: Careers
  url: https://www.tzero.com/careers
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tzero/
- group: other
  title: ''
  type: X
  url: https://x.com/tZERO
- group: design
  title: ''
  type: Conventions
  url: conventions/tzero-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/tzero-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tzero-problem-types.yml
- group: design
  title: ''
  type: ErrorCodes
  url: errors/tzero-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tzero-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/tzero-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tzero-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.tzero.com/legal
- group: design
  title: ''
  type: DataModel
  url: data-model/tzero-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/tzero-institutional-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tzero-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/tzero-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/tzero-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tzero-rate-limits.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/tzero-issuance-secondary-markets-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/tzero-institutional-overlay.yaml
created: '2026-09-01'
description: 'tZERO Technologies is a US financial-technology company building regulated infrastructure for tokenized real-world assets and digital securities. Through its SEC- and FINRA-regulated broker-dealer, Alternative Trading System (tZERO ATS, continuously operating since 2019), special purpose broker-dealer for digital custody, and SEC-registered transfer agent, tZERO covers the full lifecycle: capital formation and token issuance, secondary trading and market data, clearance and settlement, cap-table recordkeeping, corporate actions, dividends and proxy voting. Its developer surface — marketed as tZERO Connect — publishes two public OpenAPI 3.0.3 contracts (an Issuance & Secondary Markets REST API on gateway-web-api.tzero.com and an Institutional transfer-agent / tokenization / custody API on api.t0direct.com) alongside FIX 4.2 / 4.4 specifications for order entry, drop copy and market data.'
image: https://tzero.com/api/sanity-assets/images/jpd7ydtd/pre-prod/bcb9e8e2a5c5bf41d9938781a368d92635b0923a-595x156.svg?w=1200&h=627&fit=crop&auto=format
layout: provider
modified: '2026-09-01'
name: tZERO
nav: Providers
network: true
overview: 'tZERO publishes 2 APIs on the [APIs.io](https://apis.io/) network: Issuance & Secondary Markets API and Institutional API. Tagged areas include Company, Digital Securities, Tokenization, Capital Markets, and Trading.


  The tZERO catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  tZERO''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, signup flow, and 30 more developer resources.'
plans:
- name: Tzero Plans Pricing
  plan_count: 0
  slug: tzero-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Tzero Rate Limits
  slug: tzero-rate-limits
score:
  band: developing
  composite: 50.3
  coverage:
    artifact_dirs: 20
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 55.9
    developer_ergonomics: 58.9
    discoverability: 64.8
    governance: 18.2
    operational_transparency: 28.9
  previous_composite: 50.3
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 60.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tzero/refs/heads/main/screenshots/tzero-2026-09-02T164703.png
security:
- kind: authentication
  name: Tzero Authentication
  slug: tzero-authentication
  summary_line: apiKey/http/refreshToken · 4 schemes
- kind: domain-security
  name: Tzero Domain Security
  slug: tzero-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: tzero
tags:
- Company
- Digital Securities
- Tokenization
- Capital Markets
- Trading
- Alternative Trading System
- Transfer Agent
- Custody
- Blockchain
- Financial Services
- Securities
- Market Data
- FIX Protocol
website: https://www.tzero.com/
---
