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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.0
  scored_at: '2026-08-26'
api_count: 7
apis:
- description: The API Keys API from Qomplement — 2 operation(s) for api keys.
  name: Qomplement API Keys API
  slug: qomplement-api-keys-api
- description: The Extract API from Qomplement — 3 operation(s) for extract.
  name: Qomplement Extract API
  slug: qomplement-extract-api
- description: The Fill Excel API from Qomplement — 1 operation(s) for fill excel.
  name: Qomplement Fill Excel API
  slug: qomplement-fill-excel-api
- description: The Fill PDF API from Qomplement — 1 operation(s) for fill pdf.
  name: Qomplement Fill PDF API
  slug: qomplement-fill-pdf-api
- description: The Health API from Qomplement — 2 operation(s) for health.
  name: Qomplement Health API
  slug: qomplement-health-api
- description: The Jobs API from Qomplement — 3 operation(s) for jobs.
  name: Qomplement Jobs API
  slug: qomplement-jobs-api
- description: The Usage API from Qomplement — 1 operation(s) for usage.
  name: Qomplement Usage API
  slug: qomplement-usage-api
artifact_total: 20
asyncapis:
- description: ''
  name: Qomplement Webhooks
  slug: qomplement-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: StructDatafy API Keys API
  slug: open-qomplement-api-keys-api
- collection_type: open
  name: StructDatafy API Keys Extract API
  slug: open-qomplement-extract-api
- collection_type: open
  name: StructDatafy API Keys Fill Excel API
  slug: open-qomplement-fill-excel-api
- collection_type: open
  name: StructDatafy API Keys Fill PDF API
  slug: open-qomplement-fill-pdf-api
- collection_type: open
  name: StructDatafy API Keys Health API
  slug: open-qomplement-health-api
- collection_type: open
  name: StructDatafy API Keys Jobs API
  slug: open-qomplement-jobs-api
- collection_type: open
  name: StructDatafy API Keys Usage API
  slug: open-qomplement-usage-api
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.qomplement.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.qomplement.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.qomplement.com/api/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.qomplement.com/api/quickstart
- group: auth
  title: ''
  type: Authentication
  url: authentication/qomplement-authentication.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/qomplement-openapi-original.json
- group: build
  title: ''
  type: Packages
  url: packages/qomplement-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/qomplement-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/qomplement-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/qomplement-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/qomplement-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/qomplement-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/qomplement-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/qomplement-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/qomplement-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/qomplement-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/qomplement-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/qomplement-domain-security.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/qomplement-webhooks.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/qomplement-webhooks.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/qomplement-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Qomplement
- group: company
  title: ''
  type: Blog
  url: https://qomplement.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://developers.qomplement.com
- group: start
  title: ''
  type: Login
  url: https://kirbi.ai/auth
- group: commercial
  title: ''
  type: TermsOfService
  url: https://qomplement.com/legal-pages/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://qomplement.com/legal-pages/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://docs.qomplement.com
created: '2026-07-17'
description: Qomplement is a San Francisco-based Y Combinator (Spring 2026) company building an AI-native platform for supply chain and document-heavy back-office operations. Its publicly documented developer product is the Qomplement StructDatafy API, a REST API that extracts structured data from documents in 30+ formats, fills PDF forms, and populates Excel templates programmatically using AI OCR and structuring models. The API is asynchronous (job-based), authenticated with Bearer API keys issued from the developer portal, rate limited per minute and per month, and ships first-party Python and Node.js SDKs. This profile captures the published API surface, SDKs, authentication, conventions, error model, webhooks, and lifecycle.
image: https://qomplement.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Qomplement MCP Server
  slug: qomplement-mcp-server
modified: '2026-07-20'
name: Qomplement
nav: Providers
network: true
overview: 'Qomplement publishes 7 APIs on the [APIs.io](https://apis.io/) network, including API Keys API, Extract API, Fill Excel API, and 4 more. Tagged areas include Company, Document Extraction, OCR, Structured Data, and Artificial Intelligence.


  The Qomplement catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Qomplement''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, signup flow, support, and 22 more developer resources.'
random_paper: 19
rate_limits:
- limit_count: 2
  name: Qomplement Rate Limits
  slug: qomplement-rate-limits
score:
  band: developing
  composite: 48.6
  delta: 1.4
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 16.7
    contract_quality: 57.0
    developer_ergonomics: 66.1
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 31.6
  previous_composite: 47.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/qomplement/refs/heads/main/screenshots/qomplement-2026-08-17T081421.png
security:
- kind: authentication
  name: Qomplement Authentication
  slug: qomplement-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Qomplement Domain Security
  slug: qomplement-domain-security
  summary_line: TLSv1.3 · DMARC
slug: qomplement
tags:
- Company
- Document Extraction
- OCR
- Structured Data
- Artificial Intelligence
- Forms Automation
- PDF
- Supply Chain
- Developer API
- Y Combinator
website: https://developers.qomplement.com
---
