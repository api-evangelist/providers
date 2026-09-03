---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 24
  human_in_the_loop: 0
  name: Fipto Agentic Access
  operation_count: 52
  slug: fipto-agentic-access
  summary_line: 52 operations · 24 acting
api_count: 2
apis:
- baseURL: https://api.fipto.app
  baseurl_source: declared
  description: Endpoints for AISP/PISP.
  name: Fipto AISP/PISP API
  slug: fipto-aisp-pisp-api
- baseURL: https://api.fipto.app
  baseurl_source: declared
  description: Retrieve information about assets supported by Fipto.
  name: Fipto Assets API
  slug: fipto-assets-api
- baseURL: https://api.fipto.app
  baseurl_source: declared
  description: The Automations API from Fipto — 2 operation(s) for automations.
  name: Fipto Automations API
  slug: fipto-automations-api
- baseURL: https://api.fipto.app
  baseurl_source: declared
  description: Manage your beneficiaries to whitelist addresses for payout.
  name: Fipto Beneficiaries API
  slug: fipto-beneficiaries-api
- baseURL: https://api.fipto.app
  baseurl_source: declared
  description: Manage information and settings of a company.
  name: Fipto Companies API
  slug: fipto-companies-api
- baseURL: https://api.fipto.app
  baseurl_source: declared
  description: Manage conversions.
  name: Fipto Conversions API
  slug: fipto-conversions-api
- baseURL: https://api.fipto.app
  baseurl_source: declared
  description: The Internal Transfers API from Fipto — 1 operation(s) for internal transfers.
  name: Fipto Internal Transfers API
  slug: fipto-internal-transfers-api
- baseURL: https://api.fipto.app
  baseurl_source: declared
  description: The Payin Simulation API from Fipto — 1 operation(s) for payin simulation.
  name: Fipto Payin Simulation API
  slug: fipto-payin-simulation-api
- baseURL: https://api.fipto.app
  baseurl_source: declared
  description: Manage payment links.
  name: Fipto Payment links API
  slug: fipto-payment-links-api
- baseURL: https://api.fipto.app
  baseurl_source: declared
  description: Initiate payout and retrieve information about ongoing and completed transactions.
  name: Fipto Transactions API
  slug: fipto-transactions-api
- baseURL: https://api.fipto.app
  baseurl_source: declared
  description: The Travel Rule API from Fipto — 1 operation(s) for travel rule.
  name: Fipto Travel Rule API
  slug: fipto-travel-rule-api
- baseURL: https://api.fipto.app
  baseurl_source: declared
  description: Manage wallets and their related wallet details.
  name: Fipto Wallets API
  slug: fipto-wallets-api
artifact_total: 20
asyncapis:
- description: ''
  name: Fipto Webhooks
  slug: fipto-webhooks
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/fipto-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fipto-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://fipto.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.fipto.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.fipto.com/docs/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.fipto.com/reference/getting-started
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.fipto.com/docs/introduction
- group: auth
  title: ''
  type: Authentication
  url: authentication/fipto-authentication.yml
- group: operate
  title: ''
  type: Support
  url: https://www.fipto.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.fipto.com/company/blog
- group: start
  title: ''
  type: SignUp
  url: https://www.fipto.com/demo
- group: start
  title: ''
  type: Login
  url: https://fipto.app/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fipto.com/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fipto.com/legal/privacy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/galactic-meadow-917828/workspace/fipto-api-demo-environment/collection/24959087-42b9da95-ca00-4b9a-89cc-52d84d432d5f
- group: operate
  title: ''
  type: StatusPage
  url: https://status.fipto.com/
- group: auth
  title: ''
  type: Compliance
  url: https://www.fipto.com/company/compliance
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fipto-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/fipto-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/fipto-packages.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/fipto-customer-api-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/fipto-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/fipto-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fipto-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fipto-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/fipto-trust-center.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/fipto-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/fipto-conventions.yml
- group: design
  title: ''
  type: Components
  url: components/fipto-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/fipto-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/fipto-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/fipto-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fipto-rate-limits.yml
created: '2026-08-17'
description: Fipto is a Paris-based enterprise stablecoin payments and multi-currency accounts platform that lets businesses send and receive both fiat and stablecoin payments, hold multi-asset wallets with EUR and USD named accounts, convert between fiat and digital currencies, and automate treasury and reconciliation. It is licensed as a Payment Institution by France's ACPR (code 17908) and as a Crypto-Asset Service Provider by the AMF under MiCA (authorization A2026-009), and is ISO/IEC 27001:2022 certified. Fipto publishes a REST API (OpenAPI 3.0.3) covering wallets, beneficiaries, payouts, transactions, conversions, payment links, automation rules and an AISP/PISP access surface, plus signed webhooks and an open-source Model Context Protocol server for AI agents.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: Fipto MCP Server
  slug: fipto-mcp-server
modified: '2026-08-17'
name: Fipto
nav: Providers
network: true
overview: 'Fipto publishes 12 APIs on the [APIs.io](https://apis.io/) network, including AISP/PISP API, Assets API, Automations API, and 9 more. Tagged areas include Company, Blockchain, Payments, Stablecoins, and Banking.


  The Fipto catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Fipto''s developer surface includes documentation, API reference, getting-started guide, authentication, support, engineering blog, signup flow, and 27 more developer resources.'
plans:
- name: Fipto Plans Pricing
  plan_count: 0
  slug: fipto-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Fipto Rate Limits
  slug: fipto-rate-limits
score:
  band: developing
  composite: 51.9
  coverage:
    artifact_dirs: 23
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 57.5
    developer_ergonomics: 56.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 7.9
  previous_composite: 51.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: EU
      standard: psd2
    - jurisdiction: EU
      standard: psd2-sca
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 68.8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fipto/refs/heads/main/screenshots/fipto-2026-09-02T145515.png
security:
- kind: authentication
  name: Fipto Authentication
  slug: fipto-authentication
  summary_line: httpSignature · 1 scheme
- kind: domain-security
  name: Fipto Domain Security
  slug: fipto-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Fipto Trust Center
  slug: fipto-trust-center
  summary_line: ISO/IEC 27001:2022
slug: fipto
tags:
- Company
- Blockchain
- Payments
- Stablecoins
- Banking
- Treasury
- Cross-Border Payments
- Digital Currency
- Fintech
- Wallets
website: https://fipto.com
---
