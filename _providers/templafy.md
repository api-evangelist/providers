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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.3
  scored_at: '2026-07-28'
api_count: 17
apis:
- description: The DataSourceFields API from Templafy — 2 operation(s) for datasourcefields.
  name: Templafy DataSourceFields API
  slug: templafy-datasourcefields-api
- description: The DataSourceItemFields API from Templafy — 1 operation(s) for datasourceitemfields.
  name: Templafy DataSourceItemFields API
  slug: templafy-datasourceitemfields-api
- description: The DataSourceItems API from Templafy — 2 operation(s) for datasourceitems.
  name: Templafy DataSourceItems API
  slug: templafy-datasourceitems-api
- description: The DataSources API from Templafy — 2 operation(s) for datasources.
  name: Templafy DataSources API
  slug: templafy-datasources-api
- description: The Documents API from Templafy — 3 operation(s) for documents.
  name: Templafy Documents API
  slug: templafy-documents-api
- description: The EmailElements API from Templafy — 2 operation(s) for emailelements.
  name: Templafy EmailElements API
  slug: templafy-emailelements-api
- description: The Folders API from Templafy — 3 operation(s) for folders.
  name: Templafy Folders API
  slug: templafy-folders-api
- description: The Images API from Templafy — 2 operation(s) for images.
  name: Templafy Images API
  slug: templafy-images-api
- description: The Libraries API from Templafy — 2 operation(s) for libraries.
  name: Templafy Libraries API
  slug: templafy-libraries-api
- description: The Links API from Templafy — 2 operation(s) for links.
  name: Templafy Links API
  slug: templafy-links-api
- description: The Pdfs API from Templafy — 2 operation(s) for pdfs.
  name: Templafy Pdfs API
  slug: templafy-pdfs-api
- description: The Presentations API from Templafy — 3 operation(s) for presentations.
  name: Templafy Presentations API
  slug: templafy-presentations-api
- description: The SlideElements API from Templafy — 2 operation(s) for slideelements.
  name: Templafy SlideElements API
  slug: templafy-slideelements-api
- description: The Slides API from Templafy — 2 operation(s) for slides.
  name: Templafy Slides API
  slug: templafy-slides-api
- description: The Spaces API from Templafy — 1 operation(s) for spaces.
  name: Templafy Spaces API
  slug: templafy-spaces-api
- description: The Spreadsheets API from Templafy — 3 operation(s) for spreadsheets.
  name: Templafy Spreadsheets API
  slug: templafy-spreadsheets-api
- description: The TextElements API from Templafy — 3 operation(s) for textelements.
  name: Templafy TextElements API
  slug: templafy-textelements-api
artifact_total: 21
common:
- group: company
  title: ''
  type: Website
  url: https://www.templafy.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.templafy.com/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://support.templafy.com/hc/en-us/sections/360003936298-Templafy-API
- group: docs
  title: ''
  type: APIReference
  url: https://api.templafy.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://support.templafy.com/hc/en-us/articles/9982927949341-Templafy-Public-API
- group: operate
  title: ''
  type: Support
  url: https://support.templafy.com/
- group: company
  title: ''
  type: Blog
  url: https://www.templafy.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/templafy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.templafy.com/home/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.templafy.com/home/legal/templafy-saas-agreement/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.templafy.com/home/platform/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.templafy.com/
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/templafy-lifecycle.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.templafy.com/home/platform/security/
- group: auth
  title: ''
  type: TrustCenter
  url: security/templafy-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/templafy-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/templafy-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/templafy-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/templafy-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/templafy-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/templafy-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/templafy-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/templafy-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/templafy-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/templafy-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/templafy-llms.txt
created: '2026-07-17'
description: Templafy is an enterprise document-generation and content-enablement platform that helps large organizations keep every document, presentation, email, and spreadsheet on-brand and compliant. Its REST Public API automates template and digital-asset management across spaces, libraries, and folders, maintains structured data sources, and generates documents, presentations, spreadsheets, and text elements from templates. Authentication uses a scoped API key sent as an HTTP bearer token created in the Templafy Admin Center; the API is versioned in the URI path (v1-v4 plus an unstable channel) with per-version stability levels, returns RFC 7807/9457 Problem Details errors, and paginates lists with pageNumber/pageSize.
image: https://www.templafy.com/wp-content/uploads/2024/06/Logo_black.png
layout: provider
mcp_servers:
- description: ''
  name: templafy-mcp.yml
  slug: templafy-mcpyml
modified: '2026-07-21'
name: Templafy
nav: Providers
network: true
overview: 'Templafy publishes 17 APIs on the [APIs.io](https://apis.io/) network, including DataSourceFields API, DataSourceItemFields API, DataSourceItems API, and 14 more. Tagged areas include Company, Document Generation, Templates, Content Management, and Digital Asset Management.


  Templafy''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, authentication, and 19 more developer resources.'
random_paper: 66
score:
  band: developing
  composite: 49.4
  delta: -1.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 53.4
    developer_ergonomics: 60.9
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 28.9
  previous_composite: 50.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Templafy Authentication
  slug: templafy-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Templafy Domain Security
  slug: templafy-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Templafy Trust Center
  slug: templafy-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, GDPR
slug: templafy
tags:
- Company
- Document Generation
- Templates
- Content Management
- Digital Asset Management
- Document Automation
- Productivity
- Enterprise
- SaaS
website: https://www.templafy.com/
---
