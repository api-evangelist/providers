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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.9
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 17
  human_in_the_loop: 3
  name: Ledger Investing Agentic Access
  operation_count: 32
  slug: ledger-investing-agentic-access
  summary_line: 32 operations · 17 acting · 3 human-in-the-loop
api_count: 6
apis:
- description: Cashflow models composed from a fitted development model and tail model.
  name: Ledger Investing Cashflow Models API
  slug: ledger-investing-cashflow-models-api
- description: Bayesian loss development models (ChainLadder, TraditionalChainLadder, ManualATA, MeyersCRC, GMCL).
  name: Ledger Investing Development Models API
  slug: ledger-investing-development-models-api
- description: Forecasting models (AR1, SSM, TraditionalGCC).
  name: Ledger Investing Forecast Models API
  slug: ledger-investing-forecast-models-api
- description: Tail development models (GeneralizedBondy, Sherman, ClassicalPowerTransformTail).
  name: Ledger Investing Tail Models API
  slug: ledger-investing-tail-models-api
- description: Poll the status of asynchronous fit and predict tasks.
  name: Ledger Investing Tasks API
  slug: ledger-investing-tasks-api
- description: Upload, list, retrieve and delete insurance loss triangles.
  name: Ledger Investing Triangles API
  slug: ledger-investing-triangles-api
artifact_total: 12
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/ledger-investing-analytics-overlay.yaml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/LedgerInvesting/ledger-analytics/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/LedgerInvesting/ledger-analytics/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/LedgerInvesting/ledger-analytics/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ledger-investing-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://www.ledgerinvesting.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://ledger-investing-ledger-analytics.readthedocs-hosted.com/en/stable/index.html
- group: docs
  title: ''
  type: Documentation
  url: https://ledger-investing-ledger-analytics.readthedocs-hosted.com/en/stable/index.html
- group: docs
  title: ''
  type: APIReference
  url: https://ledger-investing-ledger-analytics.readthedocs-hosted.com/en/stable/api/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://ledger-investing-ledger-analytics.readthedocs-hosted.com/en/stable/quickstart.html
- group: commercial
  title: ''
  type: Pricing
  url: https://ledger-investing-ledger-analytics.readthedocs-hosted.com/en/stable/pricing.html
- group: start
  title: ''
  type: SignUp
  url: https://ledger-investing-ledger-analytics.readthedocs-hosted.com/en/stable/apikeys.html
- group: operate
  title: ''
  type: Support
  url: https://www.ledgerinvesting.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.ledgerinvesting.com/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LedgerInvesting
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/LedgerInvesting/ledger-analytics
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ledgerinvesting.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ledgerinvesting.com/privacy
- group: auth
  title: ''
  type: Compliance
  url: https://trust.korra.com
- group: auth
  title: ''
  type: Security
  url: https://trust.korra.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ledger-investing
- group: company
  title: ''
  type: Twitter
  url: https://x.com/LedgerInvesting
- group: build
  title: ''
  type: Packages
  url: packages/ledger-investing-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/ledger-investing-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ledger-investing-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ledger-investing-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ledger-investing-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ledger-investing-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ledger-investing-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ledger-investing-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ledger-investing-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ledger-investing-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/ledger-investing-trust-center.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ledger-investing-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ledger-investing-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/ledger-investing-changelog.yml
created: '2026-07-17'
description: Ledger Investing is a New York-based specialist broking and advisory firm for casualty insurance-linked securities (ILS), connecting insurers, reinsurers and fronting carriers to institutional capital markets investors. The firm originates casualty risk, structures off-balance-sheet solutions, brokes and distributes the resulting securities, and supports secondary trading, having securitized more than $2.5 billion of casualty premium across 170+ transactions since graduating Y Combinator in 2017. Its wholly owned SaaS subsidiary Korra Tech, LLC operates the Korra open data and analytics platform for the reinsurance and ILS market, whose Ledger Analytics API gives actuaries programmatic remote-compute access to Bayesian loss development, tail and forecasting models over insurance loss triangles, alongside the open-source Bermuda (loss triangle manipulation) and BayesBlend (Bayesian model stacking) Python libraries. Other subsidiaries include Ledger Capital Markets, LLC (SEC-registered
  broker-dealer, FINRA/SIPC member) and Ledger Risk Markets, LLC (licensed reinsurance intermediary).
image: https://www.ledgerinvesting.com/apple-touch-icon.png
layout: provider
mcp_servers:
- description: ''
  name: ledger-investing-mcp.yml
  slug: ledger-investing-mcpyml
modified: '2026-07-19'
name: Ledger Investing
nav: Providers
network: true
overview: 'Ledger Investing publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Cashflow Models API, Development Models API, Forecast Models API, and 3 more. Tagged areas include Company, Insurance Tech, Insurance, Reinsurance, and Insurance-Linked Securities.


  Ledger Investing''s developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, support, engineering blog, and 30 more developer resources.'
random_paper: 95
score:
  band: developing
  composite: 54.0
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 58.0
    developer_ergonomics: 62.5
    discoverability: 81.5
    governance: 20.8
    operational_transparency: 31.6
  previous_composite: 54.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 54.5
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ledger-investing/refs/heads/main/screenshots/ledger-investing-2026-07-25T224810.png
security:
- kind: authentication
  name: Ledger Investing Authentication
  slug: ledger-investing-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Ledger Investing Domain Security
  slug: ledger-investing-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ledger Investing Vulnerability Disclosure
  slug: ledger-investing-vulnerability-disclosure
  summary_line: security.txt
- kind: trust-center
  name: Ledger Investing Trust Center
  slug: ledger-investing-trust-center
  summary_line: SOC 2 Type 1, SOC 2 Type 2
slug: ledger-investing
tags:
- Company
- Insurance Tech
- Insurance
- Reinsurance
- Insurance-Linked Securities
- Actuarial
- Analytics
- Capital Markets
- Data Science
- Financial Services
website: https://www.ledgerinvesting.com/
---
