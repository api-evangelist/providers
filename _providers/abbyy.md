---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.3
  scored_at: '2026-09-05'
api_count: 3
apis:
- baseURL: https://vantage-us.abbyy.com
  baseurl_source: declared
  description: Public REST API for ABBYY Vantage intelligent document processing. Create transactions, upload and order files, launch AI skills for classification, extraction and OCR, poll transaction status, downlo
  name: ABBYY Vantage Processing REST API
  slug: abbyy-vantage-processing
- baseURL: https://vantage-us.abbyy.com
  baseurl_source: declared
  description: Reporting REST API for ABBYY Vantage. Downloads CSV extracts from the Business Processing Reporting Warehouse (transaction-level step timings, skill versions, reviewer detail) and the Analytics Report
  name: ABBYY Vantage Reporting API
  slug: abbyy-vantage-reporting
- description: REST API for ABBYY FlexiCapture Cloud for Invoices. Uploads files, runs invoice capture tasks, downloads results, and maintains business-unit and vendor master-data sets plus model training. HTTP Basi
  name: ABBYY FlexiCapture Cloud for Invoices API
  slug: abbyy-flexicapture-invoices
- description: Hosted, unauthenticated Model Context Protocol server over the public ABBYY documentation corpus. Exposes semantic search, a read-only virtual documentation filesystem, and a feedback tool, plus an MC
  name: ABBYY Documentation MCP Server
  slug: abbyy-docs-mcp
artifact_total: 12
common:
- group: company
  title: ''
  type: Website
  url: https://www.abbyy.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.abbyy.com/ai-document-processing/api/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.abbyy.com/vantage/developer/api-introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.abbyy.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.abbyy.com/vantage/getting-started/overview
- group: company
  title: ''
  type: Blog
  url: https://www.abbyy.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/abbyy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/abbyy
- group: build
  title: ''
  type: Postman
  url: https://www.abbyy.com/marketplace/assets/host/abbyy/connector/postman---abbyy-vantage-api-collection/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.abbyy.com/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.abbyy.com/legal/subscription-terms/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.abbyy.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/abbyy-llms.txt
- group: other
  title: ''
  type: AgentCard
  url: a2a/abbyy-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/abbyy-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/abbyy-tool-crosswalk.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/abbyy-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/abbyy-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/abbyy-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/abbyy-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/abbyy-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/abbyy-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/abbyy-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/abbyy-trust-center.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/abbyy-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/abbyy-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/abbyy-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/abbyy-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/abbyy-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/abbyy-components.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/abbyy-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/abbyy-rate-limits.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/abbyy-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/abbyy-domain-security.yml
created: '2026-03-27'
description: ABBYY is an intelligent document processing (IDP) and process intelligence company whose platform classifies documents, extracts structured data with confidence scores, and orchestrates human-in-the-loop review. ABBYY Vantage exposes two public REST APIs — a Processing API for transactions, documents, skills and data catalogs, and a Reporting API for business and analytics warehouse exports — both authenticated with OAuth 2.0 and served from regional US, EU and AU hosts. ABBYY also ships FlexiCapture Cloud for Invoices as a separate Basic-auth REST API, mobile capture SDKs, RPA connectors for UiPath, Power Automate, Pega, Blue Prism and Automation Anywhere, a hosted documentation MCP server, and a published A2A agent card.
finops:
- name: Abbyy Finops
  service_category: API
  slug: abbyy-finops
image: /assets/icons/abbyy.png
layout: provider
mcp_servers:
- description: ''
  name: ABBYY Documentation MCP Server
  slug: abbyy-documentation-mcp-server
modified: '2026-08-29'
name: ABBYY
nav: Providers
network: true
overview: 'ABBYY publishes 2 APIs on the [APIs.io](https://apis.io/) network: Vantage Processing REST API and Vantage Reporting API. Tagged areas include AI Automation, Document Processing, OCR, Intelligent Document Processing, and Data Extraction.


  ABBYY''s developer surface includes documentation, API reference, getting-started guide, engineering blog, authentication, changelog, and 29 more developer resources.'
plans:
- name: Abbyy Plans Pricing
  plan_count: 0
  slug: abbyy-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Abbyy Rate Limits
  slug: abbyy-rate-limits
scopes:
- name: Abbyy Scopes
  scope_count: 3
  slug: abbyy-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: developing
  composite: 51.0
  coverage:
    artifact_dirs: 23
    catalog_earned: 43.0
    catalog_earned_first_party: 0.0
    catalog_gap: 72.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 54.6
    developer_ergonomics: 71.4
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 42.1
  previous_composite: 51.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/abbyy/refs/heads/main/screenshots/abbyy-2026-07-25T181335.png
security:
- kind: authentication
  name: Abbyy Authentication
  slug: abbyy-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Abbyy Domain Security
  slug: abbyy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Abbyy Trust Center
  slug: abbyy-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: abbyy
tags:
- AI Automation
- Document Processing
- OCR
- Intelligent Document Processing
- Data Extraction
- Process Intelligence
- MCP
- Agent Skills
- RPA
- Enterprise Automation
website: https://www.abbyy.com
---
