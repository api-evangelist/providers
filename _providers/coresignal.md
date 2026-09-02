---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.5
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Coresignal Agentic Access
  operation_count: 11
  slug: coresignal-agentic-access
  summary_line: 11 operations · 8 acting
api_count: 3
apis:
- description: 'The Agentic Search API enables natural language search across Coresignal''s company, employee, and jobs datasets, returning relevant records based on conversational queries. Designed for AI agents and '
  name: Coresignal Agentic Search API
  slug: agentic-search-api
- description: 'The Company Enrichment API takes a company domain or name and returns a fully-enriched company record. Designed for sales and marketing systems that need to enrich CRM records or web form submissions '
  name: Coresignal Company Enrichment API
  slug: company-enrichment-api
- description: Retrieve full company records by ID.
  name: Coresignal Collect API
  slug: coresignal-collect-api
- description: Search and filter company records.
  name: Coresignal Search API
  slug: coresignal-search-api
arazzos:
- description: Run an Elasticsearch DSL company query, then bulk collect the full records for every matching ID.
  name: Coresignal Company Elasticsearch Search and Bulk Collect
  slug: coresignal-company-esdsl-bulk-collect-workflow
- description: Filter companies and branch between single-record collect and multi-record bulk collect based on how many matched.
  name: Coresignal Company Search with Branching Collect
  slug: coresignal-company-search-branch-collect-workflow
- description: Search the Multi-source Company API by filters, then collect the full top-matching company record.
  name: Coresignal Company Search and Collect
  slug: coresignal-company-search-collect-workflow
- description: Find a company, then find and collect a key employee currently working at that company.
  name: Coresignal Company to Employees Enrichment
  slug: coresignal-company-to-employees-workflow
- description: Find a company, then find and collect an active job posting published by that company.
  name: Coresignal Company to Job Postings Enrichment
  slug: coresignal-company-to-jobs-workflow
- description: Run an Elasticsearch DSL employee query, then bulk collect the full profiles for every matching ID.
  name: Coresignal Employee Elasticsearch Search and Bulk Collect
  slug: coresignal-employee-esdsl-bulk-collect-workflow
- description: Search the Multi-source Employee API by filters, then collect the full top-matching employee profile.
  name: Coresignal Employee Search and Collect
  slug: coresignal-employee-search-collect-workflow
- description: Run an Elasticsearch DSL job query, then collect the full record for the first matching posting.
  name: Coresignal Job Elasticsearch Search and Collect
  slug: coresignal-job-esdsl-search-collect-workflow
- description: Search the Multi-source Jobs API by filters, then collect the full top-matching job posting.
  name: Coresignal Job Search and Collect
  slug: coresignal-job-search-collect-workflow
artifact_total: 43
asyncapis:
- description: ''
  name: Coresignal Webhooks
  slug: coresignal-webhooks
collections:
- collection_type: postman
  name: Coresignal Multi-source Company API
  slug: postman-coresignal-multi-source-company-api
- collection_type: postman
  name: Coresignal Multi-source Employee API
  slug: postman-coresignal-multi-source-employee-api
- collection_type: postman
  name: Coresignal Multi-source Jobs API
  slug: postman-coresignal-multi-source-jobs-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Coresignal Multi-source Company Collect API
  slug: open-coresignal-collect-api
- collection_type: open
  name: Coresignal Multi-source Company API
  slug: open-coresignal-multi-source-company-api
- collection_type: open
  name: Coresignal Multi-source Employee API
  slug: open-coresignal-multi-source-employee-api
- collection_type: open
  name: Coresignal Multi-source Jobs API
  slug: open-coresignal-multi-source-jobs-api
- collection_type: open
  name: Coresignal Multi-source Company Collect Search API
  slug: open-coresignal-search-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/coresignal-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/coresignal-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/coresignal-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/coresignal/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/coresignal-company-esdsl-bulk-collect-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/coresignal-company-search-branch-collect-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/coresignal-company-search-collect-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/coresignal-company-to-employees-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/coresignal-company-to-jobs-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/coresignal-employee-esdsl-bulk-collect-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/coresignal-employee-search-collect-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/coresignal-job-esdsl-search-collect-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/coresignal-job-search-collect-workflow.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Coresignal-com
- group: company
  title: ''
  type: Website
  url: https://coresignal.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.coresignal.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.coresignal.com/
- group: other
  title: ''
  type: APIsOverview
  url: https://docs.coresignal.com/api-introduction/apis-overview
- group: auth
  title: ''
  type: Authorization
  url: https://docs.coresignal.com/api-introduction/authorization
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.coresignal.com/api-introduction/getting-started
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.coresignal.com/api-introduction/rate-limits
- group: build
  title: ''
  type: ResponseCodes
  url: https://docs.coresignal.com/api-introduction/response-codes
- group: other
  title: ''
  type: Credits
  url: https://docs.coresignal.com/api-introduction/credits
- group: design
  title: ''
  type: Webhooks
  url: https://docs.coresignal.com/api-introduction/webhooks
- group: other
  title: ''
  type: Dashboard
  url: https://dashboard.coresignal.com/sign-in
- group: start
  title: ''
  type: Signup
  url: https://dashboard.coresignal.com/sign-up
- group: commercial
  title: ''
  type: Pricing
  url: https://coresignal.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://coresignal.com/blog/
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/coresignal-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/coresignal-context.jsonld
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://coresignal.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://coresignal.com/terms-and-conditions/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.coresignal.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/coresignal
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/coresignal
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.coresignal.com/llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/coresignal-llms.txt
- group: docs
  title: ''
  type: APIReference
  url: https://docs.coresignal.com/api-introduction/apis-overview
- group: operate
  title: ''
  type: Support
  url: https://coresignal.com/contact-us/
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.coresignal.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://dashboard.coresignal.com/sign-in
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.coresignal.com/release-notes/release-notes
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/coresignal-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://coresignal.com/data-transparency
- group: agent
  title: ''
  type: MCPServer
  url: mcp/coresignal-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/coresignal-tool-crosswalk.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/coresignal-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/coresignal-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/coresignal-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/coresignal-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/coresignal-lifecycle.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/coresignal-scopes.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/coresignal-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/coresignal-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/coresignal-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/coresignal-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/coresignal-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/coresignal-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/coresignal-finops.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/coresignal-search-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/coresignal-collect-api-overlay.yaml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/coresignal-company-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/coresignal-companyfilter-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/coresignal-employee-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/coresignal-employeefilter-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/coresignal-job-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/coresignal-jobfilter-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/coresignal-structure.json
created: '2025-02-12'
description: Coresignal is a data-as-a-service company providing access to public web data on companies, employees, and jobs through a suite of REST APIs. The platform aggregates and refines more than 4.5 billion data records covering 75M+ companies (with 500+ data fields), 865M+ employee profiles (300+ fields), and 461M+ job postings (85+ fields). Coresignal offers Multi-source, Clean, and Base data tiers across Company, Employee, and Jobs APIs, plus specialized real-time, employee posts, agentic search, and company enrichment endpoints. Authentication uses a single apikey HTTP header.
finops:
- name: Coresignal Finops
  service_category: B2B Data API
  slug: coresignal-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/coresignal.png
json_schemas:
- name: Company
  property_count: 24
  slug: coresignal-company
- name: CompanyFilter
  property_count: 10
  slug: coresignal-companyfilter
- name: Employee
  property_count: 18
  slug: coresignal-employee
- name: EmployeeFilter
  property_count: 8
  slug: coresignal-employeefilter
- name: Job
  property_count: 18
  slug: coresignal-job
- name: JobFilter
  property_count: 9
  slug: coresignal-jobfilter
json_structures:
- name: Coresignal Structure
  property_count: 0
  slug: coresignal-structure
jsonld:
- class_count: 42
  name: Coresignal Context
  property_count: 0
  slug: coresignal-context
layout: provider
mcp_servers:
- description: ''
  name: Coresignal MCP Server
  slug: coresignal-mcp-server
modified: '2026-08-13'
name: Coresignal
nav: Providers
network: true
overview: 'Coresignal publishes 2 APIs on the [APIs.io](https://apis.io/) network: Collect API and Search API. Tagged areas include Agentic Search, B2B Data, Companies, Company Data, and Data as a Service.


  The Coresignal catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 4 Spectral governance rulesets.


  Coresignal''s developer surface includes authentication, documentation, getting-started guide, signup flow, pricing, engineering blog, API reference, and 62 more developer resources.'
plans:
- name: Coresignal Plans Pricing
  plan_count: 8
  slug: coresignal-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 9
  name: Coresignal Rate Limits
  slug: coresignal-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Coresignal API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: coresignal-jsonschema-spectral-rules
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: Coresignal API Rules
  rule_count: 9
  severity_counts:
    error: 6
    hint: 0
    info: 0
    warn: 3
  slug: coresignal-multi-source-company-api-rules
- effective_rule_count: 48
  extends:
  - spectral:oas
  name: Coresignal API Rules
  rule_count: 7
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 1
  slug: coresignal-multi-source-employee-api-rules
- effective_rule_count: 48
  extends:
  - spectral:oas
  name: Coresignal API Rules
  rule_count: 7
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 2
  slug: coresignal-multi-source-jobs-api-rules
scopes:
- name: Coresignal Scopes
  scope_count: 4
  slug: coresignal-scopes
  summary_line: 4 scopes · authorizationCode/clientCredentials/refreshToken
score:
  band: exemplar
  composite: 68.6
  coverage:
    artifact_dirs: 33
    catalog_gap: 30.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.3
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 47.0
    contract_quality: 68.5
    developer_ergonomics: 58.9
    discoverability: 81.5
    governance: 47.0
    operational_transparency: 57.9
  previous_composite: 68.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/coresignal/refs/heads/main/screenshots/coresignal-2026-06-20T175026.png
security:
- kind: authentication
  name: Coresignal Authentication
  slug: coresignal-authentication
  summary_line: apiKey/oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Coresignal Domain Security
  slug: coresignal-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: coresignal
tags:
- Agentic Search
- B2B Data
- Companies
- Company Data
- Data as a Service
- Elasticsearch
- Employee Data
- Employees
- Enrichment
- Firmographics
- Job Postings
- Job
- Lead Generation
- People Data
- Sales Intelligence
- Talent Intelligence
- Web Data
website: https://coresignal.com
---
