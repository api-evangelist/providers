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
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.4
  scored_at: '2026-09-19'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Workday Advanced Compensation Agentic Access
  operation_count: 11
  slug: workday-advanced-compensation-agentic-access
  summary_line: 11 operations · 1 acting
api_count: 3
apis:
- baseURL: https://<tenantHostname>/compensation/v3
  baseurl_source: declared
  description: Workday's first-party Compensation REST service, published as OpenAPI 3.0.1 on developer.workday.com. Fourteen operations over compensation scorecards, scorecard results and scores, workers, and one-t
  name: Workday Compensation REST API v3
  slug: workday-compensation-rest-v3
- description: Workday Web Services for compensation, published as WSDL 1.1 on community.workday.com under the urn:com.workday/bsvc/Compensation namespace. The Compensation service carries 68 operations — compensati
  name: Workday Compensation SOAP Web Services (WWS v47.0)
  slug: workday-compensation-soap-wws
- baseURL_template: https://{tenant}.workday.com/api/compensation/v1
  baseurl_source: spec_template
  description: Manage bonus and incentive plans
  name: Workday Advanced Compensation Bonus Plans API
  slug: workday-advanced-compensation-bonus-plans-api
- baseURL_template: https://{tenant}.workday.com/api/compensation/v1
  baseurl_source: spec_template
  description: Manage compensation budgets and allocations
  name: Workday Advanced Compensation Budgets API
  slug: workday-advanced-compensation-compensation-budgets-api
- baseURL_template: https://{tenant}.workday.com/api/compensation/v1
  baseurl_source: spec_template
  description: Manage compensation grade profiles and pay ranges
  name: Workday Advanced Compensation Grades API
  slug: workday-advanced-compensation-compensation-grades-api
- baseURL_template: https://{tenant}.workday.com/api/compensation/v1
  baseurl_source: spec_template
  description: Manage compensation plans and eligibility rules
  name: Workday Advanced Compensation Plans API
  slug: workday-advanced-compensation-compensation-plans-api
- baseURL_template: https://{tenant}.workday.com/api/compensation/v1
  baseurl_source: spec_template
  description: Manage compensation review processes and cycles
  name: Workday Advanced Compensation Reviews API
  slug: workday-advanced-compensation-compensation-reviews-api
- baseURL_template: https://{tenant}.workday.com/api/compensation/v1
  baseurl_source: spec_template
  description: Manage individual employee compensation packages
  name: Workday Advanced Compensation Employee Compensation API
  slug: workday-advanced-compensation-employee-compensation-api
- baseURL_template: https://{tenant}.workday.com/api/compensation/v1
  baseurl_source: spec_template
  description: Manage merit increase plans and cycles
  name: Workday Advanced Compensation Merit Plans API
  slug: workday-advanced-compensation-merit-plans-api
- baseURL_template: https://{tenant}.workday.com/api/compensation/v1
  baseurl_source: spec_template
  description: Manage equity and stock compensation plans
  name: Workday Advanced Compensation Stock Plans API
  slug: workday-advanced-compensation-stock-plans-api
artifact_total: 58
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Workday Advanced Compensation Bonus Plans API
  slug: open-workday-advanced-compensation-bonus-plans-api
- collection_type: open
  name: Workday Advanced Compensation Bonus Plans Compensation Budgets API
  slug: open-workday-advanced-compensation-compensation-budgets-api
- collection_type: open
  name: Workday Advanced Compensation Bonus Plans Compensation Grades API
  slug: open-workday-advanced-compensation-compensation-grades-api
- collection_type: open
  name: Workday Advanced Compensation Bonus Plans Compensation Plans API
  slug: open-workday-advanced-compensation-compensation-plans-api
- collection_type: open
  name: Workday Advanced Compensation Bonus Plans Employee Compensation API
  slug: open-workday-advanced-compensation-employee-compensation-api
- collection_type: open
  name: Workday Advanced Compensation Bonus Plans Merit Plans API
  slug: open-workday-advanced-compensation-merit-plans-api
- collection_type: open
  name: Workday Advanced Compensation Bonus Plans Stock Plans API
  slug: open-workday-advanced-compensation-stock-plans-api
- collection_type: open
  name: Workday Advanced Compensation API
  slug: open-workday-advanced-compensation
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/workday-advanced-compensation/refs/heads/main/security/workday-advanced-compensation-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/workday-advanced-compensation-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/workday-advanced-compensation/refs/heads/main/security/workday-advanced-compensation-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/workday-advanced-compensation-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.workday.com/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/workday-advanced-compensation/refs/heads/main/agentic-access/workday-advanced-compensation-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/workday-advanced-compensation-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/workday-advanced-compensation/refs/heads/main/authentication/workday-advanced-compensation-authentication.yml
  title: ''
  type: Authentication
  url: authentication/workday-advanced-compensation-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/workday-advanced-compensation/refs/heads/main/scopes/workday-advanced-compensation-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/workday-advanced-compensation-scopes.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.workday.com/
- group: operate
  title: ''
  type: API Status
  url: https://status.workday.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.workday.com/en-us/legal.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.workday.com/en-us/privacy.html
- group: auth
  title: ''
  type: Security
  url: https://www.workday.com/en-us/why-workday/trust/overview.html
- group: operate
  title: ''
  type: RateLimits
  url: https://developer.workday.com/doc/dan1370797408285.md
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/workday-advanced-compensation/refs/heads/main/sandbox/workday-advanced-compensation-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/workday-advanced-compensation-sandbox.yml
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Workday
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/workday-advanced-compensation/refs/heads/main/json-ld/workday-advanced-compensation-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/workday-advanced-compensation-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/workday-advanced-compensation/refs/heads/main/rules/workday-advanced-compensation-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/workday-advanced-compensation-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/workday-advanced-compensation/refs/heads/main/vocabulary/workday-advanced-compensation-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/workday-advanced-compensation-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/workday-advanced-compensation/refs/heads/main/llms/workday-advanced-compensation-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/workday-advanced-compensation-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://developer.workday.com/llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/workday-advanced-compensation/refs/heads/main/conventions/workday-advanced-compensation-conventions.yml
  title: ''
  type: Conventions
  url: conventions/workday-advanced-compensation-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/workday-advanced-compensation/refs/heads/main/errors/workday-advanced-compensation-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/workday-advanced-compensation-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/workday-advanced-compensation/refs/heads/main/lifecycle/workday-advanced-compensation-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/workday-advanced-compensation-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.workday.com/bundles/rest-directory-ui/public/static/services_oas3.json
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/workday-advanced-compensation/refs/heads/main/changelog/workday-advanced-compensation-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/workday-advanced-compensation-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/workday-advanced-compensation/refs/heads/main/conformance/workday-advanced-compensation-conformance.yml
  title: ''
  type: Conformance
  url: conformance/workday-advanced-compensation-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.workday.com/en-us/why-workday/trust/compliance.html
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/workday-advanced-compensation/refs/heads/main/data-model/workday-advanced-compensation-data-model.yml
  title: ''
  type: DataModel
  url: data-model/workday-advanced-compensation-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/workday-advanced-compensation/refs/heads/main/packages/workday-advanced-compensation-packages.yml
  title: ''
  type: Packages
  url: packages/workday-advanced-compensation-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/workday-advanced-compensation/refs/heads/main/components/workday-advanced-compensation-components.yml
  title: ''
  type: Components
  url: components/workday-advanced-compensation-components.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/workday-advanced-compensation/refs/heads/main/mcp/workday-advanced-compensation-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/workday-advanced-compensation-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/workday-advanced-compensation/refs/heads/main/mcp/workday-advanced-compensation-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/workday-advanced-compensation-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/workday-advanced-compensation/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: GraphQL
  url: https://developer.workday.com/bundles/graphql-changelog/public/static/schema/schema.txt
- group: docs
  title: ''
  type: Documentation
  url: https://developer.workday.com/
- group: docs
  title: ''
  type: APIReference
  url: https://community.workday.com/sites/default/files/file-hosting/restapi/index.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Workday
- group: company
  title: ''
  type: Blog
  url: https://blog.workday.com/
- group: operate
  title: ''
  type: Support
  url: https://www.workday.com/en-us/company/about-workday/contact-us.html
- group: auth
  title: ''
  type: TrustCenter
  url: https://security.workday.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.workday.com/doc/GUID-1293c9bb-ea02-48cd-a523-254b5060b3a6-enHYPHENus.md
- group: operate
  title: ''
  type: Roadmap
  url: https://developer.workday.com/doc/GUID-7ac8632c-1c99-44cd-b939-44c675ea6198.md
created: '2024-01-15'
description: 'Workday Advanced Compensation is the Workday HCM module for total-rewards administration — compensation plans and grades, merit and bonus cycles, stock and equity awards, compensation scorecards, budget pools and compensation review processes. Workday exposes it through three first-party machine-readable contracts published anonymously on its own hosts: a REST service (compensation v1-v3, OpenAPI 3.0.1) whose operation descriptions name the Advanced Compensation scope directly, the Compensation and Compensation_Review Workday Web Services SOAP contracts (89 operations across two WSDLs, v47.0), and a Compensation namespace inside Workday''s published GraphQL schema. The capability surface is overwhelmingly SOAP: 89 SOAP operations against 14 REST operations. Every surface runs against a customer''s own Workday tenant under OAuth 2.0 with Workday security domains; there is no public sandbox, no published pricing and no idempotency contract on any compensation write.'
examples:
- key_count: 8
  name: Workday Advanced Compensation Bonus Plan Example
  slug: workday-advanced-compensation-bonus-plan-example
- key_count: 9
  name: Workday Advanced Compensation Compensation Budget Example
  slug: workday-advanced-compensation-compensation-budget-example
- key_count: 8
  name: Workday Advanced Compensation Compensation Change Request Example
  slug: workday-advanced-compensation-compensation-change-request-example
- key_count: 9
  name: Workday Advanced Compensation Compensation Grade Example
  slug: workday-advanced-compensation-compensation-grade-example
- key_count: 8
  name: Workday Advanced Compensation Compensation Plan Example
  slug: workday-advanced-compensation-compensation-plan-example
- key_count: 8
  name: Workday Advanced Compensation Compensation Review Example
  slug: workday-advanced-compensation-compensation-review-example
- key_count: 9
  name: Workday Advanced Compensation Employee Compensation Example
  slug: workday-advanced-compensation-employee-compensation-example
- key_count: 8
  name: Workday Advanced Compensation Merit Plan Example
  slug: workday-advanced-compensation-merit-plan-example
- key_count: 8
  name: Workday Advanced Compensation Stock Plan Example
  slug: workday-advanced-compensation-stock-plan-example
finops:
- name: Workday Advanced Compensation Finops
  service_category: API
  slug: workday-advanced-compensation-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/workday-advanced-compensation.png
json_schemas:
- name: Bonus Plan
  property_count: 8
  slug: workday-advanced-compensation-bonus-plan
- name: Compensation Budget
  property_count: 9
  slug: workday-advanced-compensation-compensation-budget
- name: Compensation Change Request
  property_count: 8
  slug: workday-advanced-compensation-compensation-change-request
- name: Compensation Grade
  property_count: 9
  slug: workday-advanced-compensation-compensation-grade
- name: Compensation Plan
  property_count: 8
  slug: workday-advanced-compensation-compensation-plan
- name: Compensation Review
  property_count: 8
  slug: workday-advanced-compensation-compensation-review
- name: Employee Compensation
  property_count: 9
  slug: workday-advanced-compensation-employee-compensation
- name: Merit Plan
  property_count: 8
  slug: workday-advanced-compensation-merit-plan
- name: Stock Plan
  property_count: 8
  slug: workday-advanced-compensation-stock-plan
json_structures:
- name: Workday Advanced Compensation Bonus Plan Structure
  property_count: 8
  slug: workday-advanced-compensation-bonus-plan-structure
- name: Workday Advanced Compensation Compensation Budget Structure
  property_count: 9
  slug: workday-advanced-compensation-compensation-budget-structure
- name: Workday Advanced Compensation Compensation Change Request Structure
  property_count: 8
  slug: workday-advanced-compensation-compensation-change-request-structure
- name: Workday Advanced Compensation Compensation Grade Structure
  property_count: 9
  slug: workday-advanced-compensation-compensation-grade-structure
- name: Workday Advanced Compensation Compensation Plan Structure
  property_count: 8
  slug: workday-advanced-compensation-compensation-plan-structure
- name: Workday Advanced Compensation Compensation Review Structure
  property_count: 8
  slug: workday-advanced-compensation-compensation-review-structure
- name: Workday Advanced Compensation Employee Compensation Structure
  property_count: 9
  slug: workday-advanced-compensation-employee-compensation-structure
- name: Workday Advanced Compensation Merit Plan Structure
  property_count: 8
  slug: workday-advanced-compensation-merit-plan-structure
- name: Workday Advanced Compensation Stock Plan Structure
  property_count: 8
  slug: workday-advanced-compensation-stock-plan-structure
jsonld:
- class_count: 31
  name: Workday Advanced Compensation Context
  property_count: 17
  slug: workday-advanced-compensation-context
layout: provider
mcp_servers:
- description: ''
  name: Workday Advanced Compensation MCP Server
  slug: workday-advanced-compensation-mcp-server
modified: '2026-09-17'
name: Workday Advanced Compensation
nav: Providers
network: true
overview: 'Workday Advanced Compensation publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Workday Compensation REST API v3, Bonus Plans API, Budgets API, and 6 more. Tagged areas include Compensation, Human Resources, Payroll, HCM, and Enterprise Software.


  The Workday Advanced Compensation catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Workday Advanced Compensation''s developer surface includes authentication, sandbox, changelog, documentation, API reference, engineering blog, support, and 34 more developer resources.'
plans:
- name: Workday Advanced Compensation Plans Pricing
  plan_count: 0
  slug: workday-advanced-compensation-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Workday Advanced Compensation Rate Limits
  slug: workday-advanced-compensation-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Workday Advanced Compensation API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: workday-advanced-compensation-jsonschema-spectral-rules
- effective_rule_count: 84
  extends:
  - spectral:oas
  name: Workday Advanced Compensation API Rules
  rule_count: 43
  severity_counts:
    error: 7
    hint: 0
    info: 11
    warn: 25
  slug: workday-advanced-compensation-spectral-rules
scopes:
- name: Workday Advanced Compensation Scopes
  scope_count: 3
  slug: workday-advanced-compensation-scopes
  summary_line: 3 scopes · implicit
score:
  band: developing
  composite: 47.7
  coverage:
    artifact_dirs: 33
    catalog_earned: 68.5
    catalog_earned_first_party: 0.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.4
  facets:
    access_clarity: 44.7
    contract_governance: 47.0
    contract_quality: 32.3
    developer_ergonomics: 63.7
    discoverability: 72.2
    operational_transparency: 44.7
  previous_composite: 46.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 90.0
      derived: 9
      marker_coverage: 90.0
      total: 10
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-19'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/workday-advanced-compensation/refs/heads/main/screenshots/workday-advanced-compensation-2026-06-20T201555.png
security:
- kind: authentication
  name: Workday Advanced Compensation Authentication
  slug: workday-advanced-compensation-authentication
  summary_line: oauth2 · 4 schemes
- kind: domain-security
  name: Workday Advanced Compensation Domain Security
  slug: workday-advanced-compensation-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Workday Advanced Compensation Trust Center
  slug: workday-advanced-compensation-trust-center
  summary_line: SOC 2, ISO 27001, FedRAMP, GDPR
slug: workday-advanced-compensation
tags:
- Compensation
- Human Resources
- Payroll
- HCM
- Enterprise Software
- Total Rewards
- Bonus
- Merit
- Stock Compensation
- SOAP
- Software-as-a-Service
website: https://www.workday.com/
---
