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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.1
  scored_at: '2026-08-19'
api_count: 2
apis:
- description: The Liquidity Providers API from Stablesea — 2 operation(s) for liquidity providers.
  name: Stablesea Liquidity Providers API
  slug: stablesea-liquidity-providers-api
- description: The Organizations API from Stablesea — 11 operation(s) for organizations.
  name: Stablesea Organizations API
  slug: stablesea-organizations-api
artifact_total: 8
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Stable Sea Terminal Liquidity Providers API
  slug: open-stablesea-liquidity-providers-api
- collection_type: open
  name: Stable Sea Terminal Liquidity Providers Organizations API
  slug: open-stablesea-organizations-api
common:
- group: agent
  title: ''
  type: AgentSkill
  url: skills/stablesea-place-payout-order.md
- group: agent
  title: ''
  type: MCPServer
  url: mcp/stablesea-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/stablesea-terminal-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stablesea-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.stablesea.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.stablesea.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://docs.stablesea.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.stablesea.com/api-reference
- group: start
  title: ''
  type: SignUp
  url: https://app.stablesea.com/signup
- group: operate
  title: ''
  type: Support
  url: https://www.stablesea.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.stablesea.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.stablesea.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.stablesea.com/privacy
- group: company
  title: ''
  type: Careers
  url: https://careers.stablesea.com/
created: '2026-07-17'
description: Stable Sea is a financial technology platform providing global cash management and liquidity for companies building in stablecoins. The Stable Sea Terminal lets businesses consolidate on-chain and off-chain accounts, settle money across 40+ countries, run fiat-to-stablecoin on/off-ramps for transactions up to $50M, earn yield through tokenized money-market funds, and hold Bitcoin in insured custody. The Stable Sea Terminal API is a bearer-authenticated REST API (OpenAPI 3.1) for managing organizations, liquidity providers and exchange rates, external payment instruments, offerings, quotes, and payout orders — with idempotent writes on all create operations. Surfaced as a Kindred Ventures portfolio company and enriched into the API Evangelist network.
image: https://framerusercontent.com/images/Z7eNpaGMVcjn2gmGRb3QxFnqnE.png
layout: provider
mcp_servers:
- description: ''
  name: stablesea-mcp.yml
  slug: stablesea-mcpyml
modified: '2026-07-21'
name: Stablesea
nav: Providers
network: true
overview: 'Stablesea publishes 2 APIs on the [APIs.io](https://apis.io/) network: Liquidity Providers API and Organizations API. Tagged areas include Company, Stablecoins, Payments, Cash Management, and Treasury.


  Stablesea''s developer surface includes documentation, API reference, signup flow, support, engineering blog, and 9 more developer resources.'
random_paper: 3
score:
  band: thin
  composite: 32.4
  delta: -1.6
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 16.7
    contract_quality: 52.5
    developer_ergonomics: 35.1
    discoverability: 75.9
    governance: 16.7
    operational_transparency: 0.0
  previous_composite: 34.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 21.9
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Stablesea Authentication
  slug: stablesea-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Stablesea Domain Security
  slug: stablesea-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: stablesea
tags:
- Company
- Stablecoins
- Payments
- Cash Management
- Treasury
- Cross-Border Payments
- Liquidity
- Fintech
- On-Off Ramp
- Cryptocurrency
website: https://www.stablesea.com/
---
