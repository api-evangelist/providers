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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.5
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: Catena's banking and governance API for AI agents - agent identity, custodial and non-custodial accounts, fiat and stablecoin payments, yield, and policy-enforced spending controls. Currently in Priva
  name: Catena API
  slug: catena-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/catena-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://catena.com/.well-known/security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/catena-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://catena.com/
- group: company
  title: ''
  type: About
  url: https://catena.com/about
- group: company
  title: ''
  type: Blog
  url: https://catena.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://app.catena.com
- group: start
  title: ''
  type: Login
  url: https://app.catena.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://catena.com/legal/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://catena.com/legal/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/catena-labs
- group: operate
  title: ''
  type: Support
  url: mailto:hello@catena.com
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/catena-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/catena-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/catena-security.txt
- group: build
  title: ''
  type: Packages
  url: packages/catena-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/catena-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/catena-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/catena-mcp.yml
created: '2026-07-17'
description: 'Catena (Catena Labs) is building a regulated banking and governance platform for AI agents. The platform gives agents verified identities, custodial and non-custodial accounts, fiat and stablecoin payment rails across ten chains, yield on idle assets, and policy-enforced spending controls. For the humans and businesses deploying those agents it is a control plane: set policy, cap spending, restrict counterparties, audit every movement, and halt activity when needed. Agents access the platform through an API, a CLI, an MCP server, and a Skills framework. Founded by Sean Neville (CEO) and Matt Venables (CTO) - both Circle co-founders and creators of USDC - Catena has filed for a National Trust Bank charter with the OCC and raised $48M total ($30M Series A co-led by a16z crypto and Acrew, with QED, Coinbase Ventures, General Catalyst, Breyer Capital, IDG Capital, Oak HC/FT, and Pillar).'
image: https://catena.com/images/og/pages/home.png
layout: provider
mcp_servers:
- description: ''
  name: Catena MCP Server
  slug: catena-mcp-server
modified: '2026-07-18'
name: Catena
nav: Providers
network: true
overview: 'Catena publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Banking, Agentic Finance, AI Agents, and Payments.


  Catena''s developer surface includes engineering blog, signup flow, support, CLI, and 15 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 16.9
  coverage:
    artifact_dirs: 8
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 16.9
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 25.3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/catena/refs/heads/main/screenshots/catena-2026-07-25T204808.png
security:
- kind: domain-security
  name: Catena Domain Security
  slug: catena-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Catena Vulnerability Disclosure
  slug: catena-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: catena
tags:
- Company
- Banking
- Agentic Finance
- AI Agents
- Payments
- Stablecoins
- Governance
- Fintech
website: https://catena.com/
---
