---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 36.5
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: 1Token Agentic Access
  operation_count: 1
  slug: 1token-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- baseURL: https://1ndex.1token.tech/api/v1
  baseurl_source: declared
  description: Anonymous, read-only REST API returning the aggregate 1ndex strategy overview — current platform statistics (investors, strategies, trading teams), per-strategy-type summaries (accumulated NAV and PnL
  name: 1Token 1ndex Public Strategy Overview API
  slug: 1token-1ndex-public-strategy-overview-api
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://1token.tech/
- group: docs
  title: ''
  type: Documentation
  url: https://1token.tech/api/1ndex/v1/README.md
- group: docs
  title: ''
  type: APIReference
  url: https://1token.tech/api/1ndex/v1/README.md
- group: company
  title: ''
  type: Blog
  url: https://blog.1token.tech/
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.1token.tech/rss/
- group: operate
  title: ''
  type: ChangeLog
  url: https://1token.tech/insights/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/1token-changelog.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://1token.tech/trust-center
- group: auth
  title: ''
  type: Compliance
  url: https://1token.tech/trust-center
- group: auth
  title: ''
  type: Security
  url: security/1token-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/1token-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/1token-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/1token-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: https://1token.tech/.well-known/api-catalog
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/1token-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/1token-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/1token-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/1token-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/1token-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/1token-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/1token-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/1token-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/1token-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/1token-packages.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/1token-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/1token-agentic-access.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/1token-1ndex-overlay.yaml
- group: build
  title: ''
  type: SDKs
  url: packages/1token-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://t.me/Crypto1Token
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/1token-tech
- group: start
  title: ''
  type: Login
  url: https://1ndex.1token.tech/login
created: '2026-09-05'
description: 1Token builds institutional digital asset infrastructure for crypto funds, fund-of-funds, prime brokers, lenders, fund platforms, fund administrators and auditors. Its main platform, 1Token CAM, covers post-trade portfolio management, real-time risk (PnL, exposure, Greeks, collateral, alerts, stress testing, VaR), exchange/custody/wallet data collection and trade reconciliation, performance intelligence and verification, and investor-ready analysis and reporting across 84 CeFi venues, 164 DeFi chains and 4,290 DeFi protocols. A sister platform, 1Token 1ndex, is an institutional crypto strategy discovery service for allocators and trading teams. 1Token publishes exactly one supported public API — an anonymous, read-only 1ndex strategy overview endpoint described by an OpenAPI 3.1.1 document and discoverable through an RFC 9727 API Catalog at the domain root; the CAM product interfaces are documented behind a customer login.
image: https://1token.tech/images/og/1token-og.png
layout: provider
modified: '2026-09-05'
name: 1Token
nav: Providers
network: true
overview: '1Token publishes 1 API on the [APIs.io](https://apis.io/) network: 1ndex Public Strategy Overview API. Tagged areas include Digital Assets, Crypto, Portfolio Management, Risk Management, and Fund Administration.


  1Token''s developer surface includes documentation, API reference, engineering blog, changelog, authentication, support, and 26 more developer resources.'
plans:
- name: 1Token Plans Pricing
  plan_count: 0
  slug: 1token-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: 1Token Rate Limits
  slug: 1token-rate-limits
score:
  band: developing
  composite: 42.2
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 22.4
    commercial_clarity: 22.4
    contract_governance: 18.2
    contract_quality: 51.7
    developer_ergonomics: 44.6
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 13.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 56.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: authentication
  name: 1Token Authentication
  slug: 1token-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: 1Token Domain Security
  slug: 1token-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: 1Token Vulnerability Disclosure
  slug: 1token-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: 1Token Trust Center
  slug: 1token-trust-center
  summary_line: SOC 2 Type II
slug: 1token
tags:
- Digital Assets
- Crypto
- Portfolio Management
- Risk Management
- Fund Administration
- Reconciliation
- Fund Accounting
- Institutional Finance
- DeFi
- Market Data
- Company
website: https://1token.tech/
---
