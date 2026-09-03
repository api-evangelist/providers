---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.8
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: Managed Cloud REST surface covering OAuth auth, a Proxy API to a Core instance, Data API, Filters API, Alerts API, and the MCP endpoint. Auth via API keys or OAuth.
  name: Blnk Cloud API
  slug: blnk-cloud-api
- description: Rule-based transaction monitoring API (transaction evaluation, instruction management, Git-backed rule sync). Beta.
  name: Blnk Watch API
  slug: blnk-watch-api
- baseURL: http://localhost:5001
  baseurl_source: declared
  description: The Accounts API from Blnk Finance — 2 operation(s) for accounts.
  name: Blnk Finance Accounts API
  slug: blnkfinance-accounts-api
- baseURL: http://localhost:5001
  baseurl_source: declared
  description: The Backup API from Blnk Finance — 2 operation(s) for backup.
  name: Blnk Finance Backup API
  slug: blnkfinance-backup-api
- baseURL: http://localhost:5001
  baseurl_source: declared
  description: The Balance Monitors API from Blnk Finance — 2 operation(s) for balance monitors.
  name: Blnk Finance Balance Monitors API
  slug: blnkfinance-balance-monitors-api
- baseURL: http://localhost:5001
  baseurl_source: declared
  description: The Balances API from Blnk Finance — 2 operation(s) for balances.
  name: Blnk Finance Balances API
  slug: blnkfinance-balances-api
- baseURL: http://localhost:5001
  baseurl_source: declared
  description: The Identities API from Blnk Finance — 2 operation(s) for identities.
  name: Blnk Finance Identities API
  slug: blnkfinance-identities-api
- baseURL: http://localhost:5001
  baseurl_source: declared
  description: The Ledgers API from Blnk Finance — 2 operation(s) for ledgers.
  name: Blnk Finance Ledgers API
  slug: blnkfinance-ledgers-api
- baseURL: http://localhost:5001
  baseurl_source: declared
  description: The Refund Transaction API from Blnk Finance — 1 operation(s) for refund transaction.
  name: Blnk Finance Refund Transaction API
  slug: blnkfinance-refund-transaction-api
- baseURL: http://localhost:5001
  baseurl_source: declared
  description: The Transactions API from Blnk Finance — 2 operation(s) for transactions.
  name: Blnk Finance Transactions API
  slug: blnkfinance-transactions-api
artifact_total: 20
asyncapis:
- description: ''
  name: Blnkfinance Webhooks
  slug: blnkfinance-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/blnkfinance-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/blnkfinance-authentication.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.blnkfinance.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.blnkfinance.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.blnkfinance.com/reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.blnkfinance.com/home/install
- group: operate
  title: ''
  type: Support
  url: https://blnkfinance.com/contact/us
- group: company
  title: ''
  type: Blog
  url: https://blnkfinance.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/blnkfinance
- group: commercial
  title: ''
  type: Pricing
  url: https://blnkfinance.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://cloud.blnkfinance.com/auth/sign-up
- group: commercial
  title: ''
  type: TermsOfService
  url: https://blnkfinance.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://blnkfinance.com/legal/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.blnkfinance.com/
- group: build
  title: ''
  type: Packages
  url: packages/blnkfinance-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/blnkfinance-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/blnkfinance-cli.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/blnkfinance-well-known.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/blnkfinance-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/blnkfinance-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/blnkfinance-core-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/blnkfinance-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/blnkfinance-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/blnkfinance-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/blnkfinance-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/blnkfinance-lifecycle.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/blnkfinance-scopes.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/blnkfinance-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/blnkfinance-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/blnkfinance-trust-center.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/blnkfinance-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/blnkfinance-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/blnkfinance-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/blnkfinance-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/blnkfinance-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/blnkfinance-webhooks.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/blnkfinance-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/blnkfinance-rate-limits.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/blnkfinance-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/blnkfinance-tool-crosswalk.yml
created: '2026-08-26'
description: Open-source double-entry ledger for financial products (wallets, loans, payouts, escrow, cards). Available as self-hosted Blnk Core (OSS engine) and Blnk Cloud (managed), plus Blnk Watch for transaction monitoring. Exposes REST APIs with a public OpenAPI spec, hosted MCP servers, llms.txt, and installable agent skills.
image: https://blnkfinance.com/_astro/og-default.4FpZOtzr.png
layout: provider
mcp_servers:
- description: 'Open, no-auth Mintlify DOCUMENTATION-SEARCH MCP on a first-party host. Probed live 2026-08-27: initialize + tools/list returned 200, serverInfo "Blnk Finance", protocolVersion 2025-11-25, 3 tools. It '
  name: Blnk Finance MCP Server
  slug: blnk-finance-mcp-server
- description: 'Cloud ledger MCP: https://api.cloud.blnkfinance.com/mcp/{instance_id}, 33 tools, Bearer + mcp:read/mcp:write.'
  name: Blnk Finance MCP Server
  slug: blnk-finance-mcp-server-2
modified: '2026-08-27'
name: Blnk Finance
nav: Providers
network: true
overview: 'Blnk Finance publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Backup API, Balance Monitors API, and 5 more. Tagged areas include Fintech, Financial-Services, Ledger, double-entry-accounting, and Payments.


  The Blnk Finance catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Blnk Finance''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 34 more developer resources.'
plans:
- name: Blnkfinance Plans Pricing
  plan_count: 4
  slug: blnkfinance-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 2
  name: Blnkfinance Rate Limits
  slug: blnkfinance-rate-limits
scopes:
- name: Blnkfinance Scopes
  scope_count: 24
  slug: blnkfinance-scopes
  summary_line: 24 scopes
score:
  band: exemplar
  composite: 71.5
  coverage:
    artifact_dirs: 24
    catalog_gap: 63.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 50.5
    developer_ergonomics: 85.7
    discoverability: 66.7
    governance: 18.2
    operational_transparency: 65.8
  previous_composite: 71.5
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 71.9
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/blnkfinance/refs/heads/main/screenshots/blnkfinance-2026-09-02T144933.png
security:
- kind: authentication
  name: Blnkfinance Authentication
  slug: blnkfinance-authentication
  summary_line: apiKey/http/oauth2 · 0 schemes
- kind: domain-security
  name: Blnkfinance Domain Security
  slug: blnkfinance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Blnkfinance Vulnerability Disclosure
  slug: blnkfinance-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Blnkfinance Trust Center
  slug: blnkfinance-trust-center
  summary_line: ISO/IEC 27001, GDPR, SOC 2, PCI DSS, HIPAA
slug: blnkfinance
tags:
- Fintech
- Financial-Services
- Ledger
- double-entry-accounting
- Payments
- Wallets
- Lending
- Banking Infrastructure
- Open-Source
- MCP
- AI Agents
- Developer Tools
website: https://docs.blnkfinance.com/
---
