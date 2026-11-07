---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.5
  scored_at: '2026-11-06'
api_count: 2
apis:
- baseURL: https://api.zenledger.io
  baseurl_source: declared
  description: OAuth 2.0 client_credentials token issuance.
  name: ZenLedger Authentication API
  slug: zenledger-authentication-api
- baseURL: https://api.zenledger.io
  baseurl_source: declared
  description: Enterprise tenants registered under the Compliance Suite account.
  name: ZenLedger Companies API
  slug: zenledger-companies-api
- baseURL: https://api.zenledger.io
  baseurl_source: declared
  description: Per-source balances and import state for a user or company.
  name: ZenLedger Holdings API
  slug: zenledger-holdings-api
- baseURL: https://api.zenledger.io
  baseurl_source: declared
  description: Wallet and exchange-account import (signed and encrypted).
  name: ZenLedger Imports API
  slug: zenledger-imports-api
- baseURL: https://api.zenledger.io
  baseurl_source: declared
  description: Polymarket prediction-market positions.
  name: ZenLedger Polymarkets API
  slug: zenledger-polymarkets-api
- baseURL: https://api.zenledger.io
  baseurl_source: declared
  description: Create an aggregated portfolio from a set of accounts.
  name: ZenLedger Portfolios API
  slug: zenledger-portfolios-api
- baseURL: https://api.zenledger.io
  baseurl_source: declared
  description: Supported blockchain reference data.
  name: ZenLedger Supported Chains API
  slug: zenledger-supported-chains-api
- baseURL: https://api.zenledger.io
  baseurl_source: declared
  description: Currency reference data.
  name: ZenLedger Supported Currencies API
  slug: zenledger-supported-currencies-api
- baseURL: https://api.zenledger.io
  baseurl_source: declared
  description: Supported exchange/wallet source reference data.
  name: ZenLedger Supported Exchanges and Wallets API
  slug: zenledger-supported-exchanges-and-wallets-api
- baseURL: https://api.zenledger.io
  baseurl_source: declared
  description: Retrieve the tax calculation for an aggregated portfolio.
  name: ZenLedger Taxes API
  slug: zenledger-taxes-api
- baseURL: https://api.zenledger.io
  baseurl_source: declared
  description: Normalized crypto transactions for a user or across a company.
  name: ZenLedger Transactions API
  slug: zenledger-transactions-api
- baseURL: https://api.zenledger.io
  baseurl_source: declared
  description: End users tracked under a company.
  name: ZenLedger Users API
  slug: zenledger-users-api
- baseURL: https://api.zenledger.io
  baseurl_source: declared
  description: Sanctions and risk screening for a blockchain address.
  name: ZenLedger Wallet Screening API
  slug: zenledger-wallet-screening-api
artifact_total: 29
asyncapis:
- description: ''
  name: Zenledger Compliance Webhooks
  slug: zenledger-compliance-webhooks
collections:
- collection_type: postman
  name: 'Aggregator Suite: REST API Reference'
  slug: postman-zenledger-aggregators-v1
- collection_type: postman
  name: 'V3::Compliance Suite: REST API Reference'
  slug: postman-zenledger-compliance-v3
common:
- group: company
  title: ''
  type: Blog
  url: https://zenledger.io/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://zenledger.io/feed/
- group: other
  href: https://artifacts.apis.io/zenledger/capabilities/zenledger-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/zenledger-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/zenledger/overlays/zenledger-compliance-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zenledger-compliance-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zenledger/overlays/zenledger-aggregator-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zenledger-aggregator-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://zenledger.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.zenledger.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.zenledger.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.zenledger.io/compliance/v3/README.md
- group: build
  href: https://artifacts.apis.io/zenledger/postman/zenledger-compliance-v3.postman_collection.json
  title: ''
  type: Postman
  url: postman/zenledger-compliance-v3.postman_collection.json
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zenledger-io
- group: operate
  title: ''
  type: Support
  url: https://support.zenledger.io/en/
- group: commercial
  title: ''
  type: Pricing
  url: https://zenledger.io/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://zenledger.io/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://zenledger.io/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.zenledger.io/
- group: auth
  href: https://artifacts.apis.io/zenledger/authentication/zenledger-authentication.yml
  title: ''
  type: Authentication
  url: authentication/zenledger-authentication.yml
- group: design
  href: https://artifacts.apis.io/zenledger/conventions/zenledger-conventions.yml
  title: ''
  type: Conventions
  url: conventions/zenledger-conventions.yml
- group: design
  href: https://artifacts.apis.io/zenledger/errors/zenledger-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/zenledger-error-codes.yml
- group: design
  href: https://artifacts.apis.io/zenledger/lifecycle/zenledger-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/zenledger-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/zenledger/data-model/zenledger-data-model.yml
  title: ''
  type: DataModel
  url: data-model/zenledger-data-model.yml
- group: design
  href: https://artifacts.apis.io/zenledger/conformance/zenledger-conformance.yml
  title: ''
  type: Conformance
  url: conformance/zenledger-conformance.yml
- group: auth
  href: https://artifacts.apis.io/zenledger/conformance/zenledger-conformance.yml
  title: ''
  type: Compliance
  url: conformance/zenledger-conformance.yml
- group: auth
  href: https://artifacts.apis.io/zenledger/security/zenledger-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/zenledger-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/zenledger/security/zenledger-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/zenledger-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/zenledger/security/zenledger-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/zenledger-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/zenledger/security/zenledger-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zenledger-domain-security.yml
- group: build
  href: https://artifacts.apis.io/zenledger/packages/zenledger-packages.yml
  title: ''
  type: Packages
  url: packages/zenledger-packages.yml
- group: commercial
  href: https://artifacts.apis.io/zenledger/plans/zenledger-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/zenledger-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/zenledger/rate-limits/zenledger-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/zenledger-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/zenledger/mcp/zenledger-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/zenledger-mcp.yml
- group: agent
  href: https://artifacts.apis.io/zenledger/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/zenledger/llms/zenledger-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/zenledger-llms.txt
created: '2026-09-05'
description: 'ZenLedger is a Seattle-founded crypto tax and digital-asset accounting company whose platform ingests transactions from 400+ exchanges, 100+ DeFi protocols and 10+ NFT marketplaces to calculate cost basis, capital gains and income, and generate US tax forms. Beyond the consumer product it operates two documented B2B REST APIs on api.zenledger.io: the Compliance Suite API (v3), a digital-asset trade-monitoring surface built with COMPLY for financial institutions and enterprise compliance teams that registers companies and users, imports wallets and exchange accounts, returns normalized transactions and holdings, and screens blockchain addresses against sanctions lists; and the Aggregator Suite API (v1), a partner surface that builds an aggregated portfolio from a set of accounts and returns the resulting tax calculation. Both authenticate with OAuth 2.0 client_credentials JWTs and are documented as versioned Postman collections at docs.zenledger.io.'
finops:
- has_sources: true
  method: derived
  name: Zenledger Finops
  primary_unit: subscription
  service_category: ''
  slug: zenledger-finops
  template: false
image: https://zenledger.io/wp-content/uploads/2023/07/ZenLedger-OpenGraph.png
layout: provider
modified: '2026-10-06'
name: ZenLedger
nav: Providers
network: true
overview: 'ZenLedger publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authentication API, Companies API, Holdings API, and 10 more. Tagged areas include crypto-tax, Digital Assets, Tax Compliance, Blockchain Analytics, and RegTech.


  The ZenLedger catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  ZenLedger''s developer surface includes engineering blog, documentation, API reference, support, pricing, authentication, and 27 more developer resources.'
plans:
- name: Zenledger Plans Pricing
  plan_count: 7
  slug: zenledger-plans-pricing
- name: Zenledger Price Estimates
  plan_count: 0
  slug: zenledger-price-estimates
random_paper: 0
rate_limits:
- limit_count: 0
  name: Zenledger Rate Limits
  slug: zenledger-rate-limits
rules:
- authorship: generated
  effective_rule_count: 108
  extends:
  - spectral:oas
  name: ZenLedger API Rules
  rule_count: 67
  severity_counts:
    error: 55
    hint: 0
    info: 1
    warn: 11
  slug: zenledger-rules
score:
  band: strong
  composite: 60.0
  coverage:
    artifact_dirs: 27
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 86.8
    contract_governance: 31.8
    contract_quality: 64.0
    developer_ergonomics: 41.8
    discoverability: 73.2
    operational_transparency: 36.8
  previous_composite: 60.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/zenledger/zenledger-2026-10-11T195112.png
security:
- kind: authentication
  name: Zenledger Authentication
  slug: zenledger-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Zenledger Domain Security
  slug: zenledger-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Zenledger Vulnerability Disclosure
  slug: zenledger-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Zenledger Trust Center
  slug: zenledger-trust-center
  summary_line: SOC 2 Type II, SOC 2 Framework alignment (Information Security Program)
skill_count: 4
skills:
- name: zenledger-aggregate-portfolio-taxes
  slug: zenledger-aggregate-portfolio-taxes
- name: zenledger-onboard-compliance-user
  slug: zenledger-onboard-compliance-user
- name: zenledger-pull-transactions-and-holdings
  slug: zenledger-pull-transactions-and-holdings
- name: zenledger-screen-wallet-address
  slug: zenledger-screen-wallet-address
slug: zenledger
tags:
- crypto-tax
- Digital Assets
- Tax Compliance
- Blockchain Analytics
- RegTech
- Accounting
- Sanctions Screening
- Financial Services
- Portfolio Aggregation
- Cryptocurrency
website: https://zenledger.io/
---
