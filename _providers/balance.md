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
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Balance's v2 REST API for B2B payments, net-terms financing, invoicing, and accounts-receivable automation. Reference documentation is hosted on a password-gated ReadMe.io portal (access requested via
  name: Balance API v2
  slug: balance-api-v2
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://getbalance.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.getbalance.com/get-api
- group: docs
  title: ''
  type: Documentation
  url: https://docs.getbalance.com
- group: company
  title: ''
  type: Blog
  url: https://www.getbalance.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.getbalance.com/contact-us/
- group: start
  title: ''
  type: SignUp
  url: https://www.getbalance.com/get-api
- group: start
  title: ''
  type: Login
  url: https://dashboard.getbalance.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.getbalance.com/legal/balance-website-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.getbalance.com/legal/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.getbalance.com
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/balance-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/balance-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/balance-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/balance-mcp.yml
- group: auth
  title: ''
  type: Security
  url: https://www.getbalance.com/legal/security-policy
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/balance-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/balance-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/balance-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.getbalance.com/legal/security-policy
created: '2026-07-17'
description: Balance is a financial infrastructure platform for B2B commerce that lets merchants and marketplaces accept payments, offer net-terms financing (digital trade credit / B2B BNPL), and automate order-to-cash accounts-receivable operations. Its APIs power embedded, customizable buyer journeys, advanced and consolidated billing, split payments, and AI-powered credit-risk management, covering the full B2B flow from checkout through invoicing, financing, and reconciliation. Balance ships pre-built integrations for platforms including Shopify, BigCommerce, Magento, and Salesforce Commerce, plus marketplace solutions, and exposes a v2 REST API documented on a developer portal. The company was surfaced as a portfolio company of Forerunner Ventures, Lightspeed Venture Partners, Ribbit Capital, and Techstars, and is profiled in the API Evangelist network. Card processing runs through Stripe (PCI DSS Service Provider Level 1); Balance publishes a security policy, status page, monthly product-update
  changelog, and a beta Model Context Protocol server for agentic commerce.
image: https://files.readme.io/b57e38a-small-Frame_2_4.png
layout: provider
mcp_servers:
- description: Balance announced a Model Context Protocol (MCP) server for B2B agentic commerce, in closed beta at the time of capture. It lets LLMs and AI agents interact with Balance's APIs to get secure, conversa
  name: Balance MCP Server
  slug: balance-mcp-server
modified: '2026-07-18'
name: Balance
nav: Providers
network: true
overview: 'Balance publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Payments, B2B Payments, and Accounts Receivable.


  Balance''s developer surface includes documentation, engineering blog, support, signup flow, changelog, and 14 more developer resources.'
random_paper: 17
score:
  band: thin
  composite: 35.1
  coverage:
    artifact_dirs: 9
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 36.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 42.1
  previous_composite: 35.1
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 59.4
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/balance/refs/heads/main/screenshots/balance-2026-07-25T202259.png
security:
- kind: domain-security
  name: Balance Domain Security
  slug: balance-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Balance Vulnerability Disclosure
  slug: balance-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: balance
tags:
- Company
- Fintech
- Payments
- B2B Payments
- Accounts Receivable
- Net Terms
- Trade Credit
- BNPL
- Billing
- Embedded Finance
website: https://getbalance.com
---
