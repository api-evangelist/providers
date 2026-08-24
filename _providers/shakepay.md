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
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.8
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://shakepay.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.shakepay.com
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.shakepay.com/en/
- group: commercial
  title: ''
  type: Pricing
  url: https://shakepay.com/fees
- group: start
  title: ''
  type: SignUp
  url: https://shakepay.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://legal.shakepay.com/master
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://legal.shakepay.com/master/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/shakepay
- group: operate
  title: ''
  type: StatusPage
  url: https://status.shakepay.com/
- group: auth
  title: ''
  type: Compliance
  url: https://shakepay.com/security
- group: auth
  title: ''
  type: Security
  url: https://legal.shakepay.com/v/master/bug-bounty-program
- group: agent
  title: ''
  type: MCPServer
  url: mcp/shakepay-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/shakepay-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/shakepay-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/shakepay-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/shakepay-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shakepay-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/shakepay-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/shakepay-lifecycle.yml
created: '2026-07-17'
description: Shakepay (Shake Labs Inc.) is a regulated Canadian cryptocurrency platform headquartered in Montreal, Quebec, serving 1,500,000+ Canadians with commission-free buying, selling, and on-chain movement of Bitcoin, Ethereum, and USDC via Interac e-Transfer. Beyond trading it offers a Visa prepaid card that earns up to 1.5% back in bitcoin (#shakepaid), recurring dollar-cost- averaging buys, interest paid weekly in bitcoin on CAD/USD balances, peer-to- peer transfers, bill pay, and the daily ShakingSats reward. Shakepay is a CIRO member, a registered Investment Dealer with the AMF, registered with securities regulators across all Canadian provinces/territories, and a FINTRAC money-services business. It does not currently publish a public developer API; it runs an experimental agent-access MCP surface (mcp.shakepay.com) alongside a public status page, security.txt bug-bounty program, and llms.txt reference.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/shakepay.png
layout: provider
mcp_servers:
- description: ''
  name: Shakepay MCP Server
  slug: shakepay-mcp-server
modified: '2026-07-21'
name: Shakepay
nav: Providers
network: true
overview: 'Shakepay is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Cryptocurrency, Bitcoin, and Financial-Services.


  Shakepay''s developer surface includes engineering blog, pricing, signup flow, and 16 more developer resources.'
random_paper: 14
score:
  band: thin
  composite: 26.9
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 28.9
  previous_composite: 26.9
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 46.9
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: domain-security
  name: Shakepay Domain Security
  slug: shakepay-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Shakepay Vulnerability Disclosure
  slug: shakepay-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: shakepay
tags:
- Company
- Payments
- Cryptocurrency
- Bitcoin
- Financial-Services
- Canada
- Fintech
website: https://shakepay.com/
---
