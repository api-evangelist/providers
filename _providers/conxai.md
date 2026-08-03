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
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.7
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 63
  human_in_the_loop: 2
  name: Conxai Agentic Access
  operation_count: 114
  slug: conxai-agentic-access
  summary_line: 114 operations · 63 acting · 2 human-in-the-loop
api_count: 17
apis:
- description: The annotations API from Conxai — 1 operation(s) for annotations.
  name: Conxai annotations API
  slug: conxai-annotations-api
- description: The camera API from Conxai — 4 operation(s) for camera.
  name: Conxai camera API
  slug: conxai-camera-api
- description: The document-types API from Conxai — 4 operation(s) for document-types.
  name: Conxai document-types API
  slug: conxai-document-types-api
- description: The documents API from Conxai — 26 operation(s) for documents.
  name: Conxai documents API
  slug: conxai-documents-api
- description: The exports API from Conxai — 2 operation(s) for exports.
  name: Conxai exports API
  slug: conxai-exports-api
- description: The Images API from Conxai — 2 operation(s) for images.
  name: Conxai Images API
  slug: conxai-images-api
- description: The integrations API from Conxai — 5 operation(s) for integrations.
  name: Conxai integrations API
  slug: conxai-integrations-api
- description: The production_tracking API from Conxai — 4 operation(s) for production_tracking.
  name: Conxai production_tracking API
  slug: conxai-production-tracking-api
- description: The project API from Conxai — 5 operation(s) for project.
  name: Conxai project API
  slug: conxai-project-api
- description: The projects API from Conxai — 2 operation(s) for projects.
  name: Conxai projects API
  slug: conxai-projects-api
- description: The samples API from Conxai — 16 operation(s) for samples.
  name: Conxai samples API
  slug: conxai-samples-api
- description: The schema API from Conxai — 1 operation(s) for schema.
  name: Conxai schema API
  slug: conxai-schema-api
- description: The summary-table API from Conxai — 12 operation(s) for summary-table.
  name: Conxai summary-table API
  slug: conxai-summary-table-api
- description: The use-cases API from Conxai — 6 operation(s) for use-cases.
  name: Conxai use-cases API
  slug: conxai-use-cases-api
- description: The users API from Conxai — 3 operation(s) for users.
  name: Conxai users API
  slug: conxai-users-api
- description: The workflow API from Conxai — 3 operation(s) for workflow.
  name: Conxai workflow API
  slug: conxai-workflow-api
- description: The workflow-table API from Conxai — 3 operation(s) for workflow-table.
  name: Conxai workflow-table API
  slug: conxai-workflow-table-api
artifact_total: 22
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/conxai-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/conxai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/conxai-authentication.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://conxai.readme.io/
- group: docs
  title: ''
  type: Documentation
  url: https://conxai.readme.io/reference/sitelens-integration-steps
- group: docs
  title: ''
  type: APIReference
  url: https://conxai.readme.io/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://conxai.readme.io/reference/sitelens-integration-steps
- group: company
  title: ''
  type: Website
  url: https://www.conxai.com/
- group: company
  title: ''
  type: Blog
  url: https://www.conxai.com/company/news
- group: operate
  title: ''
  type: Support
  url: https://www.conxai.com/company/contact-us
- group: start
  title: ''
  type: SignUp
  url: https://lens.conxai.ai/
- group: start
  title: ''
  type: Login
  url: https://lens.conxai.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.conxai.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.conxai.com/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: https://conxai.eu.trust.site/
- group: auth
  title: ''
  type: Compliance
  url: https://conxai.eu.trust.site/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/conxai-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/conxai-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/conxai-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/conxai-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/conxai-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/conxai-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/conxai-conformance.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/conxai
created: '2026-07-17'
description: 'Conxai (CONXAI Technologies GmbH) is a Munich, Germany-based startup building a no-code, agentic AI platform purpose-built for the construction and AEC (architecture, engineering, construction) industry. The modular platform contextualizes fragmented project-lifecycle data — site photos and video, documents, CAD drawings and tender submissions — and turns it into actionable knowledge across three areas: transparency, automation, and knowledge management. Marquee products include SiteLens (real-time construction-site camera analysis, progress tracking and firestop detection) and DocNostic (document extraction, classification and workflow automation). Conxai exposes several REST APIs — a Customer/SiteLens API, a Docnostic document API, a Firestop API and a Production Tracking API — documented on ReadMe and secured with an X-Api-Key header (Docnostic also accepts a JWT bearer token). The company is backed by Earlybird, Pi Labs, Cemex Ventures, Zacua Ventures, Capricorn Partners
  and BayBG Venture Capital.'
image: https://cdn.prod.website-files.com/6768048a3496e563be715576/676ffd7357fd1eda32f52ca3_OG.png
layout: provider
mcp_servers:
- description: ''
  name: conxai-mcp.yml
  slug: conxai-mcpyml
modified: '2026-07-18'
name: Conxai
nav: Providers
network: true
overview: 'Conxai publishes 17 APIs on the [APIs.io](https://apis.io/) network, including annotations API, camera API, document-types API, and 14 more. Tagged areas include Company, Construction, AEC, Artificial Intelligence, and Document Processing.


  Conxai''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, support, signup flow, and 18 more developer resources.'
random_paper: 72
score:
  band: developing
  composite: 46.8
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 60.0
    developer_ergonomics: 56.0
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 46.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: derived
    skills: derived
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/conxai/refs/heads/main/screenshots/conxai-2026-07-25T210354.png
security:
- kind: authentication
  name: Conxai Authentication
  slug: conxai-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Conxai Domain Security
  slug: conxai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Conxai Trust Center
  slug: conxai-trust-center
  summary_line: SOC 2, ISO 27001:2022
slug: conxai
tags:
- Company
- Construction
- AEC
- Artificial Intelligence
- Document Processing
- Computer Vision
- Agentic AI
- Machine Learning
website: https://www.conxai.com/
---
