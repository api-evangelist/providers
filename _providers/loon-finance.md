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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.1
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Loon Finance Agentic Access
  operation_count: 3
  slug: loon-finance-agentic-access
  summary_line: 3 operations
api_count: 1
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
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Loon CADC Transparency Attestations API
  slug: open-loon-finance-attestations-api
- collection_type: open
  name: Loon CADC Transparency Attestations Issuances API
  slug: open-loon-finance-issuances-api
- collection_type: open
  name: Loon CADC Transparency Attestations Supply API
  slug: open-loon-finance-supply-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/loon-finance-transparency-overlay.yaml
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
  name: Loon Finance MCP Server
  slug: loon-finance-mcp-server
modified: '2026-07-20'
name: Loon Finance
nav: Providers
network: true
overview: 'Loon Finance publishes 3 APIs on the [APIs.io](https://apis.io/) network: Attestations API, Issuances API, and Supply API. Tagged areas include Company, Fintech, Stablecoins, Cryptocurrency, and Payments.


  Loon Finance''s developer surface includes documentation, engineering blog, support, and 19 more developer resources.'
random_paper: 12
score:
  band: developing
  composite: 44.7
  coverage:
    artifact_dirs: 14
    catalog_gap: 63.0
    catalog_max: 100.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 78.6
    commercial_clarity: 78.6
    contract_governance: 18.2
    contract_quality: 50.6
    developer_ergonomics: 18.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 5.3
  previous_composite: 44.7
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
  schema_version: 0.18.0
  scored_at: '2026-09-01'
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
- Stablecoins
- Cryptocurrency
- Payments
- Canada
- Digital Dollar
- Blockchain
- Transparency
website: https://loon.finance/
---
