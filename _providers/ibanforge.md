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
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-09-04'
api_count: 1
apis:
- baseURL: https://api.ibanforge.com
  baseurl_source: declared
  description: API key management — generate free keys and check usage
  name: IBANforge API Keys API
  slug: ibanforge-api-keys-api
- baseURL: https://api.ibanforge.com
  baseurl_source: declared
  description: BIC/SWIFT lookup endpoints (paid via x402)
  name: IBANforge BIC API
  slug: ibanforge-bic-api
- baseURL: https://api.ibanforge.com
  baseurl_source: declared
  description: Compliance check endpoint — IBAN validation + sanctions + SEPA + VoP + risk score (paid via x402)
  name: IBANforge Compliance API
  slug: ibanforge-compliance-api
- baseURL: https://api.ibanforge.com
  baseurl_source: declared
  description: Prepaid credit bundles — pay once in USDC (x402), get an API key with N credits; batch validation debits 1 credit per IBAN
  name: IBANforge Credits API
  slug: ibanforge-credits-api
- baseURL: https://api.ibanforge.com
  baseurl_source: declared
  description: Free endpoints — no payment required
  name: IBANforge Free API
  slug: ibanforge-free-api
- baseURL: https://api.ibanforge.com
  baseurl_source: declared
  description: IBAN validation endpoints (paid via x402)
  name: IBANforge IBAN API
  slug: ibanforge-iban-api
- baseURL: https://api.ibanforge.com
  baseurl_source: declared
  description: Model Context Protocol endpoint for AI agents (Streamable HTTP)
  name: IBANforge MCP API
  slug: ibanforge-mcp-api
- baseURL: https://api.ibanforge.com
  baseurl_source: declared
  description: Swiss BC-Nummer / IID clearing lookup (paid via x402)
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
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/ibanforge-capability-edges.yml
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
- description: IBANforge operates an official remote MCP server over Streamable HTTP, plus a stdio server published to npm as `ibanforge-mcp`. The HTTP transport answers a full handshake and tool calls with NO crede
  name: IBANforge MCP Server
  slug: ibanforge-mcp-server
modified: '2026-08-06'
name: IBANforge
nav: Providers
network: true
overview: 'IBANforge publishes 8 APIs on the [APIs.io](https://apis.io/) network, including API Keys API, BIC API, Compliance API, and 5 more. Tagged areas include Finance, Banking, Compliance, and MCP.


  IBANforge''s developer surface includes documentation, pricing, engineering blog, and 14 more developer resources.'
random_paper: 17
score:
  band: thin
  composite: 32.4
  coverage:
    artifact_dirs: 10
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 56.1
    developer_ergonomics: 11.9
    discoverability: 85.2
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 32.4
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
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
