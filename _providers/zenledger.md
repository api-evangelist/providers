---
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.1
  scored_at: '2026-09-05'
api_count: 2
apis:
- baseURL: https://api.zenledger.io
  baseurl_source: declared
  description: Digital-asset trade-monitoring and crypto tax-compliance REST API (v3) for financial institutions and enterprise compliance teams. Registers companies and their users, imports exchange accounts and wa
  name: ZenLedger Compliance Suite API
  slug: zenledger-compliance-suite-api
- baseURL: https://api.zenledger.io
  baseurl_source: declared
  description: Partner/aggregator REST API (v1) that creates an aggregated portfolio from a set of exchange and wallet accounts, returns the resulting tax calculation for that portfolio by aggregation code, and serv
  name: ZenLedger Aggregator Suite API
  slug: zenledger-aggregator-suite-api
artifact_total: 11
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
  title: ''
  type: Authentication
  url: authentication/zenledger-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/zenledger-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/zenledger-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/zenledger-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/zenledger-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/zenledger-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/zenledger-conformance.yml
- group: auth
  title: ''
  type: Security
  url: security/zenledger-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/zenledger-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/zenledger-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zenledger-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/zenledger-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/zenledger-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/zenledger-rate-limits.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/zenledger-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zenledger-llms.txt
created: '2026-09-05'
description: 'ZenLedger is a Seattle-founded crypto tax and digital-asset accounting company whose platform ingests transactions from 400+ exchanges, 100+ DeFi protocols and 10+ NFT marketplaces to calculate cost basis, capital gains and income, and generate US tax forms. Beyond the consumer product it operates two documented B2B REST APIs on api.zenledger.io: the Compliance Suite API (v3), a digital-asset trade-monitoring surface built with COMPLY for financial institutions and enterprise compliance teams that registers companies and users, imports wallets and exchange accounts, returns normalized transactions and holdings, and screens blockchain addresses against sanctions lists; and the Aggregator Suite API (v1), a partner surface that builds an aggregated portfolio from a set of accounts and returns the resulting tax calculation. Both authenticate with OAuth 2.0 client_credentials JWTs and are documented as versioned Postman collections at docs.zenledger.io.'
image: https://zenledger.io/wp-content/uploads/2023/07/ZenLedger-OpenGraph.png
layout: provider
modified: '2026-09-05'
name: ZenLedger
nav: Providers
network: true
overview: 'ZenLedger publishes 2 APIs on the [APIs.io](https://apis.io/) network: Compliance Suite API and Aggregator Suite API. Tagged areas include Crypto Tax, Digital Assets, Tax Compliance, Blockchain Analytics, and RegTech.


  The ZenLedger catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ZenLedger''s developer surface includes documentation, API reference, support, pricing, authentication, and 23 more developer resources.'
plans:
- name: Zenledger Plans Pricing
  plan_count: 7
  slug: zenledger-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Zenledger Rate Limits
  slug: zenledger-rate-limits
score:
  band: strong
  composite: 55.9
  coverage:
    artifact_dirs: 18
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 78.9
    commercial_clarity: 78.9
    contract_governance: 18.2
    contract_quality: 70.5
    developer_ergonomics: 39.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 36.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
  summary_line: disclosure policy published
- kind: trust-center
  name: Zenledger Trust Center
  slug: zenledger-trust-center
  summary_line: SOC 2 Type II, SOC 2 Framework alignment (Information Security Program)
slug: zenledger
tags:
- Crypto Tax
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
