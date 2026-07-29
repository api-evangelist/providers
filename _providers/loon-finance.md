---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 28.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Loon Finance Agentic Access
  operation_count: 3
  slug: loon-finance-agentic-access
  summary_line: 3 operations
api_count: 3
apis:
- description: Independent monthly reserve attestation reports.
  name: Loon Finance Attestations API
  slug: loon-finance-attestations-api
- description: On-chain CADC mint events per chain.
  name: Loon Finance Issuances API
  slug: loon-finance-issuances-api
- description: Circulating and total CADC supply, overall and per chain.
  name: Loon Finance Supply API
  slug: loon-finance-supply-api
artifact_total: 7
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/loon-finance-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/loon-finance-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://loon.finance/.well-known/security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/loon-finance-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://loon.finance/
- group: docs
  title: ''
  type: Documentation
  url: https://loon.finance/cadc-partners
- group: company
  title: ''
  type: Blog
  url: https://loon.finance/blog
- group: operate
  title: ''
  type: Support
  url: https://loon.finance/support-centre
- group: commercial
  title: ''
  type: TermsOfService
  url: https://loon.finance/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://loon.finance/privacy-policy
- group: company
  title: ''
  type: Twitter
  url: https://x.com/LoonFinance
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/loonfinance/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/loon-finance-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/loon-finance-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/loon-finance-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/loon-finance-mcp.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/loon-finance-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/loon-finance-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/loon-finance-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://loon.finance/transparency
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Loon is a Calgary-based fintech and the issuer of CADC, a regulated, fiat-backed stablecoin pegged 1:1 to the Canadian dollar. Reserves are held in segregated cash deposits at ATB Financial and attested independently every month by HDCPA Professional Corporation, with FINTRAC compliance and a prospectus pre-filed with the Alberta Securities Commission. CADC is issued on Ethereum, Base, Polygon, Arbitrum, Linea, and Solana, and Loon acquired the token from Paytrie (launched 2021, $200M+ in cumulative volume). Loon publishes a small public, unauthenticated Transparency API exposing live circulating supply per chain, on-chain issuance (mint) events, and the monthly reserve-attestation history, backed by an llms.txt, a security.txt disclosure policy, and a public transparency dashboard.
image: https://loon.finance/apple-touch-icon.png
layout: provider
mcp_servers:
- description: ''
  name: loon-finance-mcp.yml
  slug: loon-finance-mcpyml
modified: '2026-07-20'
name: Loon Finance
nav: Providers
network: true
overview: 'Loon Finance publishes 3 APIs on the [APIs.io](https://apis.io/) network: Attestations API, Issuances API, and Supply API. Tagged areas include Company, Fintech, Stablecoin, Cryptocurrency, and Payments.


  Loon Finance''s developer surface includes documentation, engineering blog, support, and 18 more developer resources.'
random_paper: 9
score:
  band: thin
  composite: 37.7
  delta: -3.6
  facets:
    commercial_clarity: 28.9
    contract_quality: 53.7
    developer_ergonomics: 19.0
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 10.5
  previous_composite: 41.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 46.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/loon-finance/refs/heads/main/screenshots/loon-finance-2026-07-25T225523.png
security:
- kind: domain-security
  name: Loon Finance Domain Security
  slug: loon-finance-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Loon Finance Vulnerability Disclosure
  slug: loon-finance-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: loon-finance
tags:
- Company
- Fintech
- Stablecoin
- Cryptocurrency
- Payments
- Canada
- Digital Dollar
- Blockchain
- Transparency
website: https://loon.finance/
---
