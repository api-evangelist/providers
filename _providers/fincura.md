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
    event_surface_described: derived
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.4
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 29
  human_in_the_loop: 0
  name: Fincura Agentic Access
  operation_count: 67
  slug: fincura-agentic-access
  summary_line: 67 operations · 29 acting
api_count: 20
apis:
- description: The Api-Key API from Fincura — 1 operation(s) for api-key.
  name: Fincura Api-Key API
  slug: fincura-api-key-api
- description: A record in our system to link financials and analyses to.
  name: Fincura Borrowers API
  slug: fincura-borrowers-api
- description: The CustomAttributes API from Fincura — 2 operation(s) for customattributes.
  name: Fincura CustomAttributes API
  slug: fincura-customattributes-api
- description: The DataViews API from Fincura — 7 operation(s) for dataviews.
  name: Fincura DataViews API
  slug: fincura-dataviews-api
- description: The DscrAnalysis API from Fincura — 4 operation(s) for dscranalysis.
  name: Fincura DscrAnalysis API
  slug: fincura-dscranalysis-api
- description: DSCR Templates
  name: Fincura DscrTemplate API
  slug: fincura-dscrtemplate-api
- description: Embedded Document Workflows enable a 3rd party user to use the Fincura UI to complete a portion of our document parsing pipeline and then return to the 3rd parties website.
  name: Fincura EmbeddedDocument API
  slug: fincura-embeddeddocument-api
- description: Embedded DSCR Analysis allows an API user to authenticate and embedded previously created DSCR analysis into a 3rd party workflow.
  name: Fincura EmbeddedDscrAnalysis API
  slug: fincura-embeddeddscranalysis-api
- description: Embedded Financials allows an API user to authenticate and embedded borrower financials into a 3rd party workflow.
  name: Fincura EmbeddedFinancials API
  slug: fincura-embeddedfinancials-api
- description: Embedded Global Cashflow Analysis allows an API user to authenticate and embed previously created Global Cashflow analyses into a 3rd party applications.
  name: Fincura EmbeddedGlobalCashflowAnalysis API
  slug: fincura-embeddedglobalcashflowanalysis-api
- description: Files serve as the source input data for our insights engine. They are represented by a `DocumentFile` record.
  name: Fincura Files API
  slug: fincura-files-api
- description: The FinancialStatementSubmission API from Fincura — 1 operation(s) for financialstatementsubmission.
  name: Fincura FinancialStatementSubmission API
  slug: fincura-financialstatementsubmission-api
- description: The GlobalCashflowAnalysis API from Fincura — 5 operation(s) for globalcashflowanalysis.
  name: Fincura GlobalCashflowAnalysis API
  slug: fincura-globalcashflowanalysis-api
- description: The GlobalCashflowTemplate API from Fincura — 1 operation(s) for globalcashflowtemplate.
  name: Fincura GlobalCashflowTemplate API
  slug: fincura-globalcashflowtemplate-api
- description: A Borrower loan record in our system.
  name: Fincura Loans API
  slug: fincura-loans-api
- description: Portfolios allow for grouping Borrowers.
  name: Fincura Portfolios API
  slug: fincura-portfolios-api
- description: Set rules/covenants for your borrowers
  name: Fincura Requirements API
  slug: fincura-requirements-api
- description: Spreading Templates
  name: Fincura SpreadingTemplate API
  slug: fincura-spreadingtemplate-api
- description: The TenantSettings API from Fincura — 1 operation(s) for tenantsettings.
  name: Fincura TenantSettings API
  slug: fincura-tenantsettings-api
- description: '## Supported Events The following are events you can listen to via webhooks. | Event&nbsp;Type&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Description | | --------------------------------------------- | ---------'
  name: Fincura Webhooks API
  slug: fincura-webhooks-api
arazzos:
- description: Creates a borrower, uploads a financial document for automated spreading, retrieves the normalized data view, then runs a DSCR analysis and downloads it.
  name: Spread a borrower financial statement and run DSCR analysis
  slug: fincura-spread-and-analyze
artifact_total: 47
asyncapis:
- description: ''
  name: Fincura Webhooks
  slug: fincura-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Automated Spreading and Analysis Api-Key API
  slug: open-fincura-api-key-api
- collection_type: open
  name: Automated Spreading and Analysis Api-Key Borrowers API
  slug: open-fincura-borrowers-api
- collection_type: open
  name: Automated Spreading and Analysis Api-Key CustomAttributes API
  slug: open-fincura-customattributes-api
- collection_type: open
  name: Automated Spreading and Analysis Api-Key DataViews API
  slug: open-fincura-dataviews-api
- collection_type: open
  name: Automated Spreading and Analysis Api-Key DscrAnalysis API
  slug: open-fincura-dscranalysis-api
- collection_type: open
  name: Automated Spreading and Analysis Api-Key DscrTemplate API
  slug: open-fincura-dscrtemplate-api
- collection_type: open
  name: Automated Spreading and Analysis Api-Key EmbeddedDocument API
  slug: open-fincura-embeddeddocument-api
- collection_type: open
  name: Automated Spreading and Analysis Api-Key EmbeddedDscrAnalysis API
  slug: open-fincura-embeddeddscranalysis-api
- collection_type: open
  name: Automated Spreading and Analysis Api-Key EmbeddedFinancials API
  slug: open-fincura-embeddedfinancials-api
- collection_type: open
  name: Automated Spreading and Analysis Api-Key EmbeddedGlobalCashflowAnalysis API
  slug: open-fincura-embeddedglobalcashflowanalysis-api
- collection_type: open
  name: Automated Spreading and Analysis Api-Key Files API
  slug: open-fincura-files-api
- collection_type: open
  name: Automated Spreading and Analysis Api-Key FinancialStatementSubmission API
  slug: open-fincura-financialstatementsubmission-api
- collection_type: open
  name: Automated Spreading and Analysis Api-Key GlobalCashflowAnalysis API
  slug: open-fincura-globalcashflowanalysis-api
- collection_type: open
  name: Automated Spreading and Analysis Api-Key GlobalCashflowTemplate API
  slug: open-fincura-globalcashflowtemplate-api
- collection_type: open
  name: Automated Spreading and Analysis Api-Key Loans API
  slug: open-fincura-loans-api
- collection_type: open
  name: Automated Spreading and Analysis Api-Key Portfolios API
  slug: open-fincura-portfolios-api
- collection_type: open
  name: Automated Spreading and Analysis Api-Key Requirements API
  slug: open-fincura-requirements-api
- collection_type: open
  name: Automated Spreading and Analysis Api-Key SpreadingTemplate API
  slug: open-fincura-spreadingtemplate-api
- collection_type: open
  name: Automated Spreading and Analysis Api-Key TenantSettings API
  slug: open-fincura-tenantsettings-api
- collection_type: open
  name: Automated Spreading and Analysis Api-Key Webhooks API
  slug: open-fincura-webhooks-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/fincura-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fincura-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fincura-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fincura-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/fincura-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/fincura-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/fincura-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fincura-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/fincura-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/fincura-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fincura-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/fincura-conventions.yml
- group: design
  title: ''
  type: Components
  url: components/fincura-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/fincura-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/fincura-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/fincura-spread-and-analyze.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fincura
- group: start
  title: ''
  type: Login
  url: https://app.fincura.com/
- group: company
  title: ''
  type: Website
  url: https://www.abrigo.com/
created: '2026-07-17'
description: Fincura (now part of Abrigo) provides automated financial statement spreading and credit analysis for banks, credit unions, and other lenders. Its Automated Spreading and Analysis API ingests borrower financial documents (PDF, Excel, and images), spreads them into normalized data views, and runs debt-service-coverage-ratio (DSCR) and global cashflow analyses. The REST API (v1) covers borrowers, loans, portfolios, document files, data views, spreading/DSCR/global-cashflow templates, financial requirements, custom attributes, embeddable workflow UIs, and HMAC-signed webhooks. Authentication is a bearer JWT API key issued per Fincura user account. Originally a Techstars-backed startup, Fincura was acquired by Abrigo.
image: https://avatars.githubusercontent.com/u/71975225?v=4
layout: provider
mcp_servers:
- description: ''
  name: fincura-mcp.yml
  slug: fincura-mcpyml
modified: '2026-07-19'
name: Fincura
nav: Providers
network: true
overview: 'Fincura publishes 20 APIs on the [APIs.io](https://apis.io/) network, including Api-Key API, Borrowers API, CustomAttributes API, and 17 more. Tagged areas include Financial Services, Lending, Credit Analysis, Financial Spreading, and Banking.


  The Fincura catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Fincura''s developer surface includes authentication and 19 more developer resources.'
random_paper: 148
score:
  band: thin
  composite: 31.9
  delta: 0.0
  facets:
    commercial_clarity: 13.2
    contract_quality: 59.4
    developer_ergonomics: 21.2
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 13.2
  previous_composite: 31.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 20
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 25.8
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fincura/refs/heads/main/screenshots/fincura-2026-07-25T214509.png
security:
- kind: authentication
  name: Fincura Authentication
  slug: fincura-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Fincura Domain Security
  slug: fincura-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: fincura
tags:
- Financial Services
- Lending
- Credit Analysis
- Financial Spreading
- Banking
- Fintech
- Underwriting
- Company
website: https://www.abrigo.com/
---
