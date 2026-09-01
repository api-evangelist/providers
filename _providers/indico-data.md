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
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.2
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Exchange an API token for a short-lived JWT access token
  name: Indico Data Authentication API
  slug: indico-data-authentication-api
- description: Datasets that back workflows and models
  name: Indico Data Datasets API
  slug: indico-data-datasets-api
- description: Objects stored on the Indico platform
  name: Indico Data Storage API
  slug: indico-data-storage-api
- description: Documents submitted to a workflow and their results
  name: Indico Data Submissions API
  slug: indico-data-submissions-api
- description: Document processing workflows
  name: Indico Data Workflows API
  slug: indico-data-workflows-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Indico REST Authentication API
  slug: open-indico-data-authentication-api
- collection_type: open
  name: Indico REST Authentication Datasets API
  slug: open-indico-data-datasets-api
- collection_type: open
  name: Indico REST Authentication Storage API
  slug: open-indico-data-storage-api
- collection_type: open
  name: Indico REST Authentication Submissions API
  slug: open-indico-data-submissions-api
- collection_type: open
  name: Indico REST Authentication Workflows API
  slug: open-indico-data-workflows-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/indico-data-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://indicodata.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.indicodata.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.indicodata.ai/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://developer.indicodata.ai/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.indicodata.ai/docs/getting-started
- group: operate
  title: ''
  type: HelpCenter
  url: https://docs.indicodata.ai/
- group: company
  title: ''
  type: Blog
  url: https://indicodata.ai/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/IndicoDataSolutions
- group: start
  title: ''
  type: Login
  url: https://app.indico.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://indicodata.ai/eula
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://indicodata.ai/privacypolicy
- group: auth
  title: ''
  type: TrustCenter
  url: https://app.carbidesecure.com/trust/indico
- group: auth
  title: ''
  type: Compliance
  url: https://app.carbidesecure.com/trust/indico
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/indico-data-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/indico-data-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/indico-data-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/indico-data-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/indico-data-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/indico-data-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/indico-data-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/indico-data-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/indico-data-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/indico-data-domain-security.yml
created: '2026-07-17'
description: Indico Data is an enterprise intelligent document processing (IDP) and intelligent process automation (IPA) company that turns unstructured content — documents, emails, images, and free text — into structured, usable data. Its Agents & Workflows platform lets teams build extraction and classification models from as few as ~200 sample documents (no rules or templates) and deploy them as document-processing pipelines. Developers integrate via a REST API and a companion GraphQL API, authenticating with an API token exchanged for a short-lived JWT, and via first-party Python, C#, and Java client libraries. The platform is commonly deployed on a dedicated per-customer cluster and is used to automate high-volume unstructured-data workflows across insurance, financial services, and other document-heavy industries.
image: https://indicodata.ai/wp-content/uploads/2023/01/indico-data-logo.png
layout: provider
mcp_servers:
- description: ''
  name: Indico Data MCP Server
  slug: indico-data-mcp-server
modified: '2026-07-19'
name: Indico Data
nav: Providers
network: true
overview: 'Indico Data publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Datasets API, Storage API, and 2 more. Tagged areas include Company, Intelligent Document Processing, Intelligent Process Automation, Document AI, and Machine-Learning.


  Indico Data''s developer surface includes documentation, API reference, getting-started guide, engineering blog, changelog, authentication, and 19 more developer resources.'
random_paper: 14
score:
  band: thin
  composite: 34.5
  coverage:
    artifact_dirs: 18
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 4.5
    contract_quality: 16.2
    developer_ergonomics: 42.3
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 34.5
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 5
      marker_coverage: 100.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 45.5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/indico-data/refs/heads/main/screenshots/indico-data-2026-07-25T222311.png
security:
- kind: authentication
  name: Indico Data Authentication
  slug: indico-data-authentication
  summary_line: http-basic/http-bearer · 2 schemes
- kind: domain-security
  name: Indico Data Domain Security
  slug: indico-data-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Indico Data Trust Center
  slug: indico-data-trust-center
  summary_line: SOC 2 Type II
slug: indico-data
tags:
- Company
- Intelligent Document Processing
- Intelligent Process Automation
- Document AI
- Machine-Learning
- Unstructured Data
- Data Extraction
- Insurance
website: https://indicodata.ai/
---
