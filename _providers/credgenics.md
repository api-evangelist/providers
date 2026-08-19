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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.7
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Credgenics Agentic Access
  operation_count: 7
  slug: credgenics-agentic-access
  summary_line: 7 operations · 5 acting
api_count: 3
apis:
- description: Client-credentials access-token exchange.
  name: Credgenics Authentication API
  slug: credgenics-authentication-api
- description: Customer and transaction ingestion for credit-line products.
  name: Credgenics Credit Line API
  slug: credgenics-credit-line-api
- description: Loan and payment ingestion and retrieval.
  name: Credgenics Lending API
  slug: credgenics-lending-api
artifact_total: 13
asyncapis:
- description: ''
  name: Credgenics Webhooks
  slug: credgenics-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Credgenics Recovery Authentication API
  slug: open-credgenics-authentication-api
- collection_type: open
  name: Credgenics Recovery Authentication Credit Line API
  slug: open-credgenics-credit-line-api
- collection_type: open
  name: Credgenics Recovery Authentication Lending API
  slug: open-credgenics-lending-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.credgenics.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.credgenics.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.credgenics.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.credgenics.com/#getting-started
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.credgenics.com/#getting-started
- group: company
  title: ''
  type: Blog
  url: https://blog.credgenics.com/
- group: start
  title: ''
  type: Login
  url: https://app.credgenics.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.credgenics.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.credgenics.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/credgenics
- group: auth
  title: ''
  type: Compliance
  url: https://www.credgenics.com/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/credgenics-trust-center.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/credgenics-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/credgenics-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/credgenics-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/credgenics-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/credgenics-problem-types.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/credgenics-well-known.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/credgenics-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/credgenics-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/credgenics-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/credgenics-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/credgenics-llms.txt
- group: design
  title: ''
  type: DataModel
  url: data-model/credgenics-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/credgenics-recovery-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Credgenics is an AI-powered debt collection and loan recovery SaaS platform used by banks, NBFCs, housing-finance companies, microfinance institutions, fintechs and asset-reconstruction companies (primarily in India). Its REST Recovery API lets lenders push loan, customer, payment and transaction data into the platform and read collections status, DPD and penalties back, alongside digital communications, a GenAI voicebot (Swara), predictive dialing (DialNext), field collections (CG Collect), litigation management, online dispute resolution and the Billzy loan-repayment payments product. Authentication is a client-credentials exchange returning a short-lived `authenticationtoken`; every request carries the tenant `company_id`.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/credgenics.png
layout: provider
mcp_servers:
- description: ''
  name: credgenics-mcp.yml
  slug: credgenics-mcpyml
modified: '2026-07-18'
name: Credgenics
nav: Providers
network: true
overview: 'Credgenics publishes 3 APIs on the [APIs.io](https://apis.io/) network: Authentication API, Credit Line API, and Lending API. Tagged areas include Company, Enterprise, Financial Services, Debt Collection, and Loan Recovery.


  The Credgenics catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Credgenics'' developer surface includes documentation, API reference, getting-started guide, engineering blog, authentication, and 21 more developer resources.'
random_paper: 4
score:
  band: thin
  composite: 30.8
  delta: -8.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 30.3
    contract_quality: 23.1
    developer_ergonomics: 16.1
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 10.5
  previous_composite: 38.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/credgenics/refs/heads/main/screenshots/credgenics-2026-07-25T210716.png
security:
- kind: authentication
  name: Credgenics Authentication
  slug: credgenics-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Credgenics Domain Security
  slug: credgenics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Credgenics Trust Center
  slug: credgenics-trust-center
  summary_line: PCI DSS, ISO (certificate displayed; specific ISO standard not named on the page)
slug: credgenics
tags:
- Company
- Enterprise
- Financial Services
- Debt Collection
- Loan Recovery
- Lending
- Collections
- Fintech
- India
website: https://www.credgenics.com/
---
