---
access_model:
  confidence: high
  label: Paid (free tier) · Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: true
  source:
  - https://ibanforge.com/pricing
  - https://api.ibanforge.com/v1/demo
  - https://api.ibanforge.com/mcp
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 46.8
  scored_at: '2026-08-17'
api_count: 8
apis:
- description: API key management — generate free keys and check usage
  name: IBANforge API Keys API
  slug: ibanforge-api-keys-api
- description: BIC/SWIFT lookup endpoints (paid via x402)
  name: IBANforge BIC API
  slug: ibanforge-bic-api
- description: Compliance check endpoint — IBAN validation + sanctions + SEPA + VoP + risk score (paid via x402)
  name: IBANforge Compliance API
  slug: ibanforge-compliance-api
- description: Prepaid credit bundles — pay once in USDC (x402), get an API key with N credits; batch validation debits 1 credit per IBAN
  name: IBANforge Credits API
  slug: ibanforge-credits-api
- description: Free endpoints — no payment required
  name: IBANforge Free API
  slug: ibanforge-free-api
- description: IBAN validation endpoints (paid via x402)
  name: IBANforge IBAN API
  slug: ibanforge-iban-api
- description: Model Context Protocol endpoint for AI agents (Streamable HTTP)
  name: IBANforge MCP API
  slug: ibanforge-mcp-api
- description: Swiss BC-Nummer / IID clearing lookup (paid via x402)
  name: IBANforge Swiss Clearing API
  slug: ibanforge-swiss-clearing-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Ibanforge API Keys API
  slug: open-ibanforge-api-keys-api
- collection_type: open
  name: Ibanforge BIC API
  slug: open-ibanforge-bic-api
- collection_type: open
  name: Ibanforge Compliance API
  slug: open-ibanforge-compliance-api
- collection_type: open
  name: Ibanforge Credits API
  slug: open-ibanforge-credits-api
- collection_type: open
  name: Ibanforge Free API
  slug: open-ibanforge-free-api
- collection_type: open
  name: Ibanforge IBAN API
  slug: open-ibanforge-iban-api
- collection_type: open
  name: Ibanforge MCP API
  slug: open-ibanforge-mcp-api
- collection_type: open
  name: Ibanforge Swiss Clearing API
  slug: open-ibanforge-swiss-clearing-api
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ibanforge-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ibanforge-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ibanforge.com
- group: docs
  title: ''
  type: Documentation
  url: https://ibanforge.com/docs
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ibanforge-mcp.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/ibanforge-a2a.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/ibanforge-well-known.yml
- group: agent
  title: ''
  type: LlmsText
  url: llms/ibanforge-llms.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: https://api.ibanforge.com/.well-known/security.txt
- group: operate
  title: ''
  type: StatusPage
  url: https://ibanforge.com/status
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ibanforge.com/en/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ibanforge.com/en/legal/dpa
- group: commercial
  title: ''
  type: Pricing
  url: https://ibanforge.com/pricing
- group: other
  title: ''
  type: x402
  url: https://api.ibanforge.com/.well-known/x402
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: company
  title: ''
  type: Blog
  url: https://ibanforge.com/en/blog
created: '2026-05-28'
description: Pre-payout IBAN screening for developers and AI agents — validation, issuing-bank identification against national bank registers, Swiss clearing including QR-IID, bank-level sanctions, SEPA and VoP reachability, and risk scoring across 89 IBAN countries.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ibanforge.png
layout: provider
mcp_servers:
- description: ''
  name: ibanforge-mcp.yml
  slug: ibanforge-mcpyml
modified: '2026-08-06'
name: IBANforge
nav: Providers
network: true
overview: 'IBANforge publishes 8 APIs on the [APIs.io](https://apis.io/) network, including API Keys API, BIC API, Compliance API, and 5 more. Tagged areas include Finance, Banking, Compliance, and MCP.


  IBANforge''s developer surface includes documentation, pricing, engineering blog, and 13 more developer resources.'
random_paper: 47
score:
  band: thin
  composite: 35.0
  delta: 0.0
  facets:
    commercial_clarity: 31.6
    contract_quality: 61.6
    developer_ergonomics: 19.6
    discoverability: 90.7
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 35.0
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 25.3
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ibanforge/refs/heads/main/screenshots/ibanforge-2026-06-20T183111.png
security:
- kind: domain-security
  name: Ibanforge Domain Security
  slug: ibanforge-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Ibanforge Vulnerability Disclosure
  slug: ibanforge-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ibanforge
tags:
- Finance
- Banking
- Compliance
- MCP
website: https://ibanforge.com
---
