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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.8
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Modernfi Agentic Access
  operation_count: 37
  slug: modernfi-agentic-access
  summary_line: 37 operations · 19 acting
api_count: 7
apis:
- description: The Accounts API from ModernFi — 5 operation(s) for accounts.
  name: ModernFi Accounts API
  slug: modernfi-accounts-api
- description: The auth API from ModernFi — 1 operation(s) for auth.
  name: ModernFi auth API
  slug: modernfi-auth-api
- description: The customBenchmarks API from ModernFi — 2 operation(s) for custombenchmarks.
  name: ModernFi customBenchmarks API
  slug: modernfi-custombenchmarks-api
- description: The Depositors API from ModernFi — 3 operation(s) for depositors.
  name: ModernFi Depositors API
  slug: modernfi-depositors-api
- description: The files API from ModernFi — 4 operation(s) for files.
  name: ModernFi files API
  slug: modernfi-files-api
- description: The pricingGroups API from ModernFi — 4 operation(s) for pricinggroups.
  name: ModernFi pricingGroups API
  slug: modernfi-pricinggroups-api
- description: The Transactions API from ModernFi — 2 operation(s) for transactions.
  name: ModernFi Transactions API
  slug: modernfi-transactions-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: API Reference Accounts API
  slug: open-modernfi-accounts-api
- collection_type: open
  name: API Reference Accounts auth API
  slug: open-modernfi-auth-api
- collection_type: open
  name: API Reference Accounts customBenchmarks API
  slug: open-modernfi-custombenchmarks-api
- collection_type: open
  name: API Reference Accounts Depositors API
  slug: open-modernfi-depositors-api
- collection_type: open
  name: API Reference Accounts files API
  slug: open-modernfi-files-api
- collection_type: open
  name: API Reference Accounts pricingGroups API
  slug: open-modernfi-pricinggroups-api
- collection_type: open
  name: API Reference Accounts Transactions API
  slug: open-modernfi-transactions-api
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.modernfi.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.modernfi.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.modernfi.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.modernfi.com/modernfi-developer-hub/getting-started
- group: operate
  title: ''
  type: Support
  url: https://modernfi.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://modernfi.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/modernfi
- group: operate
  title: ''
  type: StatusPage
  url: https://status.modernfi.com
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.modernfi.com/topics/versioning
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/modernfi-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/modernfi-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/modernfi-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/modernfi-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/modernfi-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/modernfi-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/modernfi-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/modernfi-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/modernfi-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/modernfi-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/modernfi-well-known.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/modernfi-digital-banking-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/modernfi-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/modernfi-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/modernfi-domain-security.yml
created: '2026-07-17'
description: ModernFi operates institution-owned deposit networks for U.S. banks and credit unions, giving them infrastructure to grow deposits, extend reciprocal deposit insurance beyond standard FDIC/NCUA limits, optimize funding, and deepen depositor relationships. Its Digital Banking API (v1) lets member institutions programmatically manage deposit accounts, depositors, transaction records and sweeps, monthly statements and files, custom rate benchmarks, and pricing groups — authenticated with OAuth 2.0 client credentials and pulled into treasury, ALCO, risk, and reporting systems. ModernFi is backed by a16z.
image: https://modernfi.com/favicon.ico
layout: provider
mcp_servers:
- description: Official ModernFi documentation MCP server (Fern-hosted). Provides AI-powered search over the ModernFi developer documentation at docs.modernfi.com. This is a docs-search server, not a full API-operat
  name: ModernFi MCP Server
  slug: modernfi-mcp-server
modified: '2026-07-20'
name: ModernFi
nav: Providers
network: true
overview: 'ModernFi publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, auth API, customBenchmarks API, and 4 more. Tagged areas include Company, Banking, Deposits, Fintech, and Credit Unions.


  ModernFi''s developer surface includes documentation, API reference, getting-started guide, support, changelog, authentication, sandbox, and 18 more developer resources.'
random_paper: 12
score:
  band: developing
  composite: 46.0
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 16.7
    contract_quality: 54.2
    developer_ergonomics: 63.7
    discoverability: 92.6
    governance: 16.7
    operational_transparency: 42.1
  previous_composite: 46.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 36.7
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/modernfi/refs/heads/main/screenshots/modernfi-2026-08-07T184015.png
security:
- kind: authentication
  name: Modernfi Authentication
  slug: modernfi-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Modernfi Domain Security
  slug: modernfi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: modernfi
tags:
- Company
- Banking
- Deposits
- Fintech
- Credit Unions
- Financial-Services
- Deposit Network
- Treasury
website: https://docs.modernfi.com
---
