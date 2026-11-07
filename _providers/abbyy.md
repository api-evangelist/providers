---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
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
    mcp_tool_quality: full
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 45.9
  scored_at: '2026-11-06'
api_count: 3
apis:
- description: REST API for ABBYY FlexiCapture Cloud for Invoices. Uploads files, runs invoice capture tasks, downloads results, and maintains business-unit and vendor master-data sets plus model training. HTTP Basi
  name: ABBYY FlexiCapture Cloud for Invoices API
  slug: abbyy-flexicapture-invoices
- description: Hosted, unauthenticated Model Context Protocol server over the public ABBYY documentation corpus. Exposes semantic search, a read-only virtual documentation filesystem, and a feedback tool, plus an MC
  name: ABBYY Documentation MCP Server
  slug: abbyy-docs-mcp
- baseURL: https://vantage-us.abbyy.com
  baseurl_source: declared
  description: The CatalogRecords API from ABBYY — 3 operation(s) for catalogrecords.
  name: ABBYY Catalog Records API
  slug: abbyy-catalogrecords-api
- baseURL: https://vantage-us.abbyy.com
  baseurl_source: declared
  description: The Catalogs API from ABBYY — 5 operation(s) for catalogs.
  name: ABBYY Catalogs API
  slug: abbyy-catalogs-api
- baseURL: https://vantage-us.abbyy.com
  baseurl_source: declared
  description: The Invites API from ABBYY — 1 operation(s) for invites.
  name: ABBYY Invites API
  slug: abbyy-invites-api
- baseURL: https://vantage-us.abbyy.com
  baseurl_source: declared
  description: The Report API from ABBYY — 5 operation(s) for report.
  name: ABBYY Report API
  slug: abbyy-report-api
- baseURL: https://vantage-us.abbyy.com
  baseurl_source: declared
  description: The Report v1 API from ABBYY — 3 operation(s) for report v1.
  name: ABBYY Report v1 API
  slug: abbyy-report-v1-api
- baseURL: https://vantage-us.abbyy.com
  baseurl_source: declared
  description: The Skills API from ABBYY — 2 operation(s) for skills.
  name: ABBYY Skills API
  slug: abbyy-skills-api
- baseURL: https://vantage-us.abbyy.com
  baseurl_source: declared
  description: The Transactions API from ABBYY — 11 operation(s) for transactions.
  name: ABBYY Transactions API
  slug: abbyy-transactions-api
- baseURL: https://api-us.flexicapture.com
  baseurl_source: declared
  description: The Transaction Documents API from ABBYY — 4 operation(s) for transaction documents.
  name: ABBYY Transaction Documents API
  slug: abbyy-transaction-documents-api
artifact_total: 20
common:
- group: commercial
  href: https://artifacts.apis.io/abbyy/finops/abbyy-finops.yml
  title: ''
  type: FinOps
  url: finops/abbyy-finops.yml
- group: other
  href: https://artifacts.apis.io/abbyy/overlays/abbyy-vantage-processing-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/abbyy-vantage-processing-overlay.yaml
- group: other
  href: https://artifacts.apis.io/abbyy/overlays/abbyy-vantage-reporting-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/abbyy-vantage-reporting-overlay.yaml
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
  href: https://artifacts.apis.io/abbyy/llms/abbyy-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/abbyy-llms.txt
- group: other
  href: https://artifacts.apis.io/abbyy/a2a/abbyy-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/abbyy-a2a.yml
- group: agent
  href: https://artifacts.apis.io/abbyy/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/abbyy/mcp/abbyy-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/abbyy-mcp.yml
- group: build
  href: https://artifacts.apis.io/abbyy/mcp/abbyy-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/abbyy-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/abbyy/well-known/abbyy-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/abbyy-well-known.yml
- group: build
  href: https://artifacts.apis.io/abbyy/packages/abbyy-packages.yml
  title: ''
  type: Packages
  url: packages/abbyy-packages.yml
- group: build
  href: https://artifacts.apis.io/abbyy/packages/abbyy-packages.yml
  title: ''
  type: SDKs
  url: packages/abbyy-packages.yml
- group: auth
  href: https://artifacts.apis.io/abbyy/authentication/abbyy-authentication.yml
  title: ''
  type: Authentication
  url: authentication/abbyy-authentication.yml
- group: auth
  href: https://artifacts.apis.io/abbyy/scopes/abbyy-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/abbyy-scopes.yml
- group: design
  href: https://artifacts.apis.io/abbyy/conventions/abbyy-conventions.yml
  title: ''
  type: Conventions
  url: conventions/abbyy-conventions.yml
- group: design
  href: https://artifacts.apis.io/abbyy/conformance/abbyy-conformance.yml
  title: ''
  type: Conformance
  url: conformance/abbyy-conformance.yml
- group: auth
  href: https://artifacts.apis.io/abbyy/security/abbyy-trust-center.yml
  title: ''
  type: Compliance
  url: security/abbyy-trust-center.yml
- group: design
  href: https://artifacts.apis.io/abbyy/errors/abbyy-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/abbyy-problem-types.yml
- group: design
  href: https://artifacts.apis.io/abbyy/lifecycle/abbyy-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/abbyy-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/abbyy/lifecycle/abbyy-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/abbyy-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/abbyy/changelog/abbyy-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/abbyy-changelog.yml
- group: design
  href: https://artifacts.apis.io/abbyy/data-model/abbyy-data-model.yml
  title: ''
  type: DataModel
  url: data-model/abbyy-data-model.yml
- group: design
  href: https://artifacts.apis.io/abbyy/components/abbyy-components.yml
  title: ''
  type: Components
  url: components/abbyy-components.yml
- group: commercial
  href: https://artifacts.apis.io/abbyy/plans/abbyy-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/abbyy-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/abbyy/rate-limits/abbyy-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/abbyy-rate-limits.yml
- group: auth
  href: https://artifacts.apis.io/abbyy/security/abbyy-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/abbyy-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/abbyy/security/abbyy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/abbyy-domain-security.yml
created: '2026-03-27'
description: ABBYY is an intelligent document processing (IDP) and process intelligence company whose platform classifies documents, extracts structured data with confidence scores, and orchestrates human-in-the-loop review. ABBYY Vantage exposes two public REST APIs — a Processing API for transactions, documents, skills and data catalogs, and a Reporting API for business and analytics warehouse exports — both authenticated with OAuth 2.0 and served from regional US, EU and AU hosts. ABBYY also ships FlexiCapture Cloud for Invoices as a separate Basic-auth REST API, mobile capture SDKs, RPA connectors for UiPath, Power Automate, Pega, Blue Prism and Automation Anywhere, a hosted documentation MCP server, and a published A2A agent card.
finops:
- has_sources: true
  method: derived
  name: Abbyy Finops
  primary_unit: ''
  service_category: ''
  slug: abbyy-finops
  template: true
image: /assets/icons/abbyy.png
layout: provider
mcp_servers:
- description: Remote MCP server at docs.abbyy.com over streamable HTTP; 3 tools listed.
  name: ABBYY Documentation MCP Server
  slug: abbyy-documentation-mcp-server
modified: '2026-08-29'
name: ABBYY
nav: Providers
network: true
overview: 'ABBYY publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Catalog Records API, Catalogs API, Invites API, and 7 more. Tagged areas include AI Automation, Document Processing, OCR, Intelligent Document Processing, and Data Extraction.


  The ABBYY catalog on APIs.io includes 1 Spectral governance ruleset.


  ABBYY''s developer surface includes documentation, API reference, getting-started guide, engineering blog, authentication, changelog, and 32 more developer resources.'
plans:
- name: Abbyy Plans Pricing
  plan_count: 0
  slug: abbyy-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Abbyy Rate Limits
  slug: abbyy-rate-limits
rules:
- authorship: generated
  effective_rule_count: 98
  extends:
  - spectral:oas
  name: ABBYY API Rules
  rule_count: 57
  severity_counts:
    error: 47
    hint: 0
    info: 2
    warn: 8
  slug: abbyy-rules
scopes:
- name: Abbyy Scopes
  scope_count: 3
  slug: abbyy-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: developing
  composite: 53.8
  coverage:
    artifact_dirs: 28
    catalog_earned: 44.5
    catalog_earned_first_party: 0.0
    catalog_gap: 70.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.4
  facets:
    access_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 54.3
    developer_ergonomics: 71.4
    discoverability: 80.0
    operational_transparency: 42.1
  previous_composite: 52.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 8
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 39.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/abbyy/abbyy-2026-07-25T181335.png
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
skill_count: 1
skills:
- name: Abbyy
  slug: abbyy-vantage
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
- A2A
website: https://www.abbyy.com
---
