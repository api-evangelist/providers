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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    idempotency: documented
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 60.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Bcb Group Agentic Access
  operation_count: 24
  slug: bcb-group-agentic-access
  summary_line: 24 operations · 12 acting
api_count: 8
apis:
- description: The Accounts API from BCB Group — 4 operation(s) for accounts.
  name: BCB Group Accounts API
  slug: bcb-group-accounts-api
- description: The Authentication API from BCB Group — 1 operation(s) for authentication.
  name: BCB Group Authentication API
  slug: bcb-group-authentication-api
- description: The Beneficiaries API from BCB Group — 2 operation(s) for beneficiaries.
  name: BCB Group Beneficiaries API
  slug: bcb-group-beneficiaries-api
- description: The BLINC API from BCB Group — 2 operation(s) for blinc.
  name: BCB Group BLINC API
  slug: bcb-group-blinc-api
- description: The Notifications API from BCB Group — 1 operation(s) for notifications.
  name: BCB Group Notifications API
  slug: bcb-group-notifications-api
- description: The Payments API from BCB Group — 7 operation(s) for payments.
  name: BCB Group Payments API
  slug: bcb-group-payments-api
- description: The Tools API from BCB Group — 1 operation(s) for tools.
  name: BCB Group Tools API
  slug: bcb-group-tools-api
- description: The Virtual Accounts API from BCB Group — 6 operation(s) for virtual accounts.
  name: BCB Group Virtual Accounts API
  slug: bcb-group-virtual-accounts-api
artifact_total: 14
asyncapis:
- description: ''
  name: Bcb Group Webhooks
  slug: bcb-group-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://bcbgroup.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.bcb.group/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bcb.group/docs
- group: docs
  title: ''
  type: APIReference
  url: https://docs.bcb.group/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.bcb.group/docs/introduction
- group: operate
  title: ''
  type: Support
  url: https://www.bcbgroup.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://www.bcbgroup.com/insights/
- group: start
  title: ''
  type: Login
  url: https://console.bcb.group/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bcbgroup.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bcbgroup.com/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://www.bcbgroup.com/about/our-licences-and-regulations/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.bcb.group/docs/changle-log
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bcb-group-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/bcb-group-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bcb-group-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/bcb-group-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bcb-group-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bcb-group-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/bcb-group-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bcb-group-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bcb-group-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/bcb-group-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/bcb-group-mcp.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bcb-group-agentic-access.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/bcb-group-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/bcb-group-security.txt
- group: auth
  title: ''
  type: Security
  url: https://bcbgroup.io/.well-known/security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bcb-group-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bcb-group-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/bcb-group-authenticate-and-check-balances.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/bcb-group-authorise-a-payment.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/bcb-group-manage-virtual-accounts.md
created: '2026-07-17'
description: BCB Group is a regulated, multi-jurisdictional payments infrastructure provider connecting traditional finance with digital assets for financial institutions across global fiat and crypto markets. Its products include multi-currency payment accounts, virtual IBANs, crypto and e-money accounts, trading, stablecoin earn, and the BLINC instant, fee-free 24/7 settlement network linking 100+ ecosystem members. BCB serves 250+ clients (including Bitstamp, Circle, Ripple, Fireblocks and Copper) and exposes a Bearer-token Payments API (OAuth 2.0 client credentials) covering accounts, balances, transactions, beneficiaries, payments, virtual accounts and webhooks. Surfaced as a portfolio company of Pantera Capital and enriched from its public developer documentation.
image: https://www.bcbgroup.com/wp-content/uploads/2026/03/bcb-icons.png
layout: provider
mcp_servers:
- description: ''
  name: bcb-group-mcp.yml
  slug: bcb-group-mcpyml
modified: '2026-07-18'
name: BCB Group
nav: Providers
network: true
overview: 'BCB Group publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Authentication API, Beneficiaries API, and 5 more. Tagged areas include Company, Crypto, Payments, Banking, and Digital Assets.


  The BCB Group catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  BCB Group''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, changelog, authentication, and 25 more developer resources.'
random_paper: 6
score:
  band: developing
  composite: 51.3
  delta: -6.2
  facets:
    commercial_clarity: 42.1
    contract_quality: 65.2
    developer_ergonomics: 62.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 34.2
  previous_composite: 57.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 45.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/bcb-group/refs/heads/main/screenshots/bcb-group-2026-07-25T202502.png
security:
- kind: authentication
  name: Bcb Group Authentication
  slug: bcb-group-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Bcb Group Domain Security
  slug: bcb-group-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Bcb Group Vulnerability Disclosure
  slug: bcb-group-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bcb-group
tags:
- Company
- Crypto
- Payments
- Banking
- Digital Assets
- Stablecoins
- Financial Services
- Fintech
website: https://bcbgroup.io/
---
