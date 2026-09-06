---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.2
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Bindbee Agentic Access
  operation_count: 7
  slug: bindbee-agentic-access
  summary_line: 7 operations
api_count: 1
apis:
- baseURL: https://api.bindbee.dev
  baseurl_source: declared
  description: Job candidates from connected ATS systems, normalized across Greenhouse, Lever, Workable, Ashby and every other connected ATS.
  name: Bindbee Candidates API
  slug: bindbee-candidates-api
- baseURL: https://api.bindbee.dev
  baseurl_source: declared
  description: Organizational departments from connected HRIS and ATS systems.
  name: Bindbee Departments API
  slug: bindbee-departments-api
- baseURL: https://api.bindbee.dev
  baseurl_source: declared
  description: Normalized employee records from connected HRIS systems, including employment, compensation, benefits, groups and reporting hierarchy.
  name: Bindbee Employees API
  slug: bindbee-employees-api
- baseURL: https://api.bindbee.dev
  baseurl_source: declared
  description: Job listings and requisitions from connected ATS systems.
  name: Bindbee Jobs API
  slug: bindbee-jobs-api
- baseURL: https://api.bindbee.dev
  baseurl_source: declared
  description: Employee time-off requests and accrued balances from connected HRIS systems.
  name: Bindbee Time Off API
  slug: bindbee-time-off-api
- baseURL: https://api.bindbee.dev
  baseurl_source: declared
  description: The complete Bindbee contract as the provider publishes it — 119 paths and 144 operations across the HRIS, ATS, LMS, Custom Fields, Embedded and platform namespaces, fetched verbatim from https://api.
  name: Bindbee Unified API
  slug: bindbee-unified-api
artifact_total: 65
asyncapis:
- description: ''
  name: Bindbee Webhooks
  slug: bindbee-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Bindbee Candidates API
  slug: open-bindbee-candidates-api
- collection_type: open
  name: Bindbee Candidates Departments API
  slug: open-bindbee-departments-api
- collection_type: open
  name: Bindbee Candidates Employees API
  slug: open-bindbee-employees-api
- collection_type: open
  name: Bindbee Candidates Jobs API
  slug: open-bindbee-jobs-api
- collection_type: open
  name: Bindbee Candidates Time Off API
  slug: open-bindbee-time-off-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.bindbee.dev/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bindbee-agentic-access.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/bindbee-a2a.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/bindbee-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/bindbee-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/bindbee-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bindbee-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/bindbee-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bindbee-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bindbee-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bindbee-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bindbee.dev/
- group: design
  title: ''
  type: Conformance
  url: conformance/bindbee-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/bindbee-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/bindbee-trust-center.yml
- group: build
  title: ''
  type: Packages
  url: packages/bindbee-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/bindbee-packages.yml
- group: design
  title: ''
  type: Components
  url: components/bindbee-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/bindbee-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/bindbee-webhooks.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/bindbee-unified-api-overlay.yaml
- group: commercial
  title: ''
  type: Plans
  url: plans/bindbee-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bindbee-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bindbee-llms.txt
- group: build
  title: ''
  type: Examples
  url: examples/bindbee-employees-response-example.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/bindbee-employees-response-schema.json
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.bindbee.dev/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.bindbee.dev/api-reference/basics/authentication
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.bindbee.dev/features/overview
- group: commercial
  title: ''
  type: Pricing
  url: https://bindbee.dev/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.bindbee.dev/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bindbee.dev/policies/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bindbee.dev/policies/privacy-policy
- group: operate
  title: ''
  type: Support
  url: mailto:support@bindbee.dev
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/unifyXX
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bindbee-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bindbee-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bindbee
- group: start
  title: ''
  type: Portal
  url: https://bindbee.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bindbee.dev/
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/bindbee/refs/heads/main/rules/bindbee-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/bindbee/refs/heads/main/vocabulary/bindbee-vocabulary.yaml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.bindbee.dev/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://bindbee.dev/blog/rss.xml
created: '2026-03-16'
description: Bindbee is a unified API for HRIS, Payroll, ATS and LMS integrations. One integration against Bindbee reaches 67+ third-party HR systems — BambooHR, Workday, ADP, Greenhouse, Lever, Personio, Hibob and the rest — through normalized employee, candidate, job, payroll, time-off and course models, so a B2B software company never builds a one-to-one connector again. Each of its customers' end users authorizes their own system through an embedded link flow and is addressed by a connector token; reads are served from Bindbee's synced copy of the upstream system, refreshed every 24 hours by default, with webhooks for sync and data-change events and a passthrough endpoint for anything the unified model does not cover.
examples:
- key_count: 2
  name: Bindbee Candidate Example
  slug: bindbee-candidate-example
- key_count: 2
  name: Bindbee Candidates Response Example
  slug: bindbee-candidates-response-example
- key_count: 2
  name: Bindbee Department Example
  slug: bindbee-department-example
- key_count: 2
  name: Bindbee Departments Response Example
  slug: bindbee-departments-response-example
- key_count: 2
  name: Bindbee Employee Example
  slug: bindbee-employee-example
- key_count: 2
  name: Bindbee Employees Response Example
  slug: bindbee-employees-response-example
- key_count: 2
  name: Bindbee Job Example
  slug: bindbee-job-example
- key_count: 2
  name: Bindbee Jobs Response Example
  slug: bindbee-jobs-response-example
- key_count: 2
  name: Bindbee Time Off Request Example
  slug: bindbee-time-off-request-example
- key_count: 2
  name: Bindbee Time Off Response Example
  slug: bindbee-time-off-response-example
features:
- description: Access employee data from BambooHR, Workday, ADP, and 50+ HRIS systems through one API.
  name: Unified HRIS API
- description: Access job listings and candidates from Greenhouse, Lever, Workable, and other ATS systems.
  name: Unified ATS API
- description: Consistent normalized schema across all connected HR systems.
  name: Data Normalization
- description: Efficient cursor-based pagination for large employee datasets.
  name: Cursor Pagination
- description: Secure per-integration connector tokens for multi-tenant HR data access.
  name: Connector Tokens
- description: Webhooks and polling for real-time HR data synchronization.
  name: Real-Time Sync
finops:
- name: Bindbee Finops
  service_category: API
  slug: bindbee-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bindbee.png
json_schemas:
- name: AtsCandidate
  property_count: 22
  slug: bindbee-candidate
- name: PaginatedResponse[AtsCandidate]
  property_count: 3
  slug: bindbee-candidates-response
- name: AtsDepartment
  property_count: 6
  slug: bindbee-department
- name: PaginatedResponse[AtsDepartment]
  property_count: 3
  slug: bindbee-departments-response
- name: HrisEmployeeResponse
  property_count: 40
  slug: bindbee-employee
- name: PaginatedResponse[HrisEmployeeResponse]
  property_count: 3
  slug: bindbee-employees-response
- name: AtsJob
  property_count: 17
  slug: bindbee-job
- name: PaginatedResponse[AtsJob]
  property_count: 3
  slug: bindbee-jobs-response
- name: HrisTimeOff
  property_count: 14
  slug: bindbee-time-off-request
- name: PaginatedResponse[HrisTimeOff]
  property_count: 3
  slug: bindbee-time-off-response
json_structures:
- name: Bindbee Candidate Structure
  property_count: 7
  slug: bindbee-candidate-structure
- name: Bindbee Candidates Response Structure
  property_count: 1
  slug: bindbee-candidates-response-structure
- name: Bindbee Department Structure
  property_count: 3
  slug: bindbee-department-structure
- name: Bindbee Departments Response Structure
  property_count: 1
  slug: bindbee-departments-response-structure
- name: Bindbee Employee Structure
  property_count: 8
  slug: bindbee-employee-structure
- name: Bindbee Employees Response Structure
  property_count: 3
  slug: bindbee-employees-response-structure
- name: Bindbee Job Structure
  property_count: 6
  slug: bindbee-job-structure
- name: Bindbee Jobs Response Structure
  property_count: 1
  slug: bindbee-jobs-response-structure
- name: Bindbee Time Off Request Structure
  property_count: 6
  slug: bindbee-time-off-request-structure
- name: Bindbee Time Off Response Structure
  property_count: 1
  slug: bindbee-time-off-response-structure
jsonld:
- class_count: 10
  name: Bindbee Context
  property_count: 12
  slug: bindbee-context
layout: provider
mcp_servers:
- description: Bindbee serves a remote MCP server on its own documentation host. It was probed anonymously with a JSON-RPC tools/list call on 2026-09-04 and returned three tools with full inputSchemas. It is a DOCUM
  name: Bindbee Docs
  slug: bindbee-docs
modified: '2026-09-04'
name: Bindbee
nav: Providers
network: true
overview: 'Bindbee publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Candidates API, Departments API, Employees API, and 3 more. Tagged areas include ATS, HR Integration, HRIS, Workforce, and Unified API.


  The Bindbee catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Bindbee''s developer surface includes sandbox, code examples, API reference, getting-started guide, pricing, signup flow, support, and 38 more developer resources.'
plans:
- name: Bindbee Plans Pricing
  plan_count: 3
  slug: bindbee-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 2
  name: Bindbee Rate Limits
  slug: bindbee-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Bindbee API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: bindbee-jsonschema-spectral-rules
- effective_rule_count: 71
  extends:
  - spectral:oas
  name: Bindbee API Rules
  rule_count: 30
  severity_counts:
    error: 8
    hint: 0
    info: 0
    warn: 22
  slug: bindbee-spectral-rules
score:
  band: exemplar
  composite: 67.7
  coverage:
    artifact_dirs: 31
    catalog_earned: 80.5
    catalog_earned_first_party: 20.0
    catalog_gap: 34.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.1
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 47.0
    contract_quality: 33.4
    developer_ergonomics: 78.6
    discoverability: 75.9
    governance: 47.0
    operational_transparency: 47.4
  previous_composite: 67.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 11
      marker_coverage: 100.0
      total: 11
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 55.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bindbee/refs/heads/main/screenshots/bindbee-2026-06-20T173245.png
security:
- kind: authentication
  name: Bindbee Authentication
  slug: bindbee-authentication
  summary_line: http/apiKey · 2 schemes
- kind: domain-security
  name: Bindbee Domain Security
  slug: bindbee-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Bindbee Trust Center
  slug: bindbee-trust-center
  summary_line: SOC 2 Type II, ISO 27001, HIPAA, GDPR
slug: bindbee
tags:
- ATS
- HR Integration
- HRIS
- Workforce
- Unified API
- Payroll
- LMS
- Employee Data
- Integrations
use_cases:
- description: Sync employee records from any HRIS into internal apps and directories.
  name: Employee Directory Integration
- description: Trigger onboarding workflows when new employees are added in the HRIS.
  name: Onboarding Automation
- description: Track candidates across ATS stages in unified dashboards.
  name: Recruiting Pipeline Visibility
- description: Move between HRIS providers without rewriting integrations.
  name: HRIS Migration
- description: Aggregate people data from multiple HR systems for workforce analytics.
  name: HR Analytics
website: https://www.bindbee.dev/
---
