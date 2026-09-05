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
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 30.2
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: OAuth2-secured wealth-data API covering the Connect flow (connectors, sessions, SCA resolution), Credentials, Entities, Aggregation, and Letters, returning standardized portfolios, investments, accoun
  name: Flanks API
  slug: flanks-api
artifact_total: 6
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.flanks.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.flanks.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.flanks.io/pages/flanks-apis/connect-api/v2/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.flanks.io/pages/integration-example/
- group: auth
  title: ''
  type: Authentication
  url: authentication/flanks-authentication.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/flanks-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/flanks-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/flanks-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/flanks-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.flanks.io/responsible-disclosure
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.flanks.io/security-and-privacy
- group: auth
  title: ''
  type: Compliance
  url: https://www.flanks.io/security-and-privacy
- group: design
  title: ''
  type: Conformance
  url: conformance/flanks-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/flanks-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/flanks-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/flanks-changelog.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/flanks-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/flanks-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/flanks-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/flanks-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/flanks-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/flanks-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/flanks-llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.flanks.io/blog
- group: operate
  title: ''
  type: Support
  url: https://www.flanks.io/customer-service
- group: start
  title: ''
  type: Login
  url: https://platform.flanks.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.flanks.io/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.flanks.io/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/flanksio
created: '2026-07-17'
description: Flanks is an AI-powered wealth data platform, headquartered in Barcelona with offices in Madrid, Paris, and London, that aggregates and standardizes investment and banking data from 700+ financial institutions into a single unified model. It serves financial advisors, banks, family offices, and asset managers through its Aggregate and Lume modules, processing millions of portfolios monthly across the EU. The Flanks API exposes an OAuth2-secured Connect flow (link accounts, resolve MFA/SCA challenges), plus Credentials, Entities, Aggregation, and Letters APIs that return portfolios, investments, accounts, liabilities, cards, and their transactions. A hosted Model Context Protocol (MCP) server gives AI assistants direct, OAuth-secured access to the same multi-bank investment data.
image: https://cdn.prod.website-files.com/66d71d258c24eef64e16030e/66e002e85abba93409df5c36_flanks-opengrapfh.png
layout: provider
mcp_servers:
- description: Model Context Protocol server giving AI assistants direct access to multi-bank investment data through Flanks. Covers the Connect flow, credential management, and portfolio/investment data retrieval.
  name: Flanks MCP Server
  slug: flanks-mcp-server
modified: '2026-07-19'
name: Flanks
nav: Providers
network: true
overview: 'Flanks publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Wealth Management, Financial Data, Data Aggregation, and Fintech.


  Flanks'' developer surface includes documentation, API reference, getting-started guide, authentication, changelog, sandbox, engineering blog, and 22 more developer resources.'
random_paper: 9
score:
  band: thin
  composite: 29.7
  coverage:
    artifact_dirs: 14
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 29.7
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: EU
      standard: psd2-sca
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 45.6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/flanks/refs/heads/main/screenshots/flanks-2026-07-25T214706.png
security:
- kind: authentication
  name: Flanks Authentication
  slug: flanks-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Flanks Domain Security
  slug: flanks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Flanks Vulnerability Disclosure
  slug: flanks-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Flanks Trust Center
  slug: flanks-trust-center
  summary_line: SOC 2 Type II, SOC 3, GDPR
slug: flanks
tags:
- Company
- Wealth Management
- Financial Data
- Data Aggregation
- Fintech
- Investments
- Open Banking
website: https://docs.flanks.io/
---
