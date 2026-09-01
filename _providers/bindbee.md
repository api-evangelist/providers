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
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.4
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Bindbee Agentic Access
  operation_count: 7
  slug: bindbee-agentic-access
  summary_line: 7 operations
api_count: 5
apis:
- description: Job candidates from connected ATS systems
  name: Bindbee Candidates API
  slug: bindbee-candidates-api
- description: Organizational departments
  name: Bindbee Departments API
  slug: bindbee-departments-api
- description: Employee records from connected HRIS systems
  name: Bindbee Employees API
  slug: bindbee-employees-api
- description: Job listings from connected ATS systems
  name: Bindbee Jobs API
  slug: bindbee-jobs-api
- description: Employee time-off requests and balances
  name: Bindbee Time Off API
  slug: bindbee-time-off-api
artifact_total: 61
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
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bindbee-agentic-access.yml
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
description: Bindbee provides a unified HRIS and ATS integration API that allows companies to connect with multiple HR systems through a single integration, simplifying workforce data access and HR automation.
examples:
- key_count: 7
  name: Bindbee Candidate Example
  slug: bindbee-candidate-example
- key_count: 1
  name: Bindbee Candidates Response Example
  slug: bindbee-candidates-response-example
- key_count: 3
  name: Bindbee Department Example
  slug: bindbee-department-example
- key_count: 1
  name: Bindbee Departments Response Example
  slug: bindbee-departments-response-example
- key_count: 8
  name: Bindbee Employee Example
  slug: bindbee-employee-example
- key_count: 3
  name: Bindbee Employees Response Example
  slug: bindbee-employees-response-example
- key_count: 6
  name: Bindbee Job Example
  slug: bindbee-job-example
- key_count: 1
  name: Bindbee Jobs Response Example
  slug: bindbee-jobs-response-example
- key_count: 6
  name: Bindbee Time Off Request Example
  slug: bindbee-time-off-request-example
- key_count: 1
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
- name: Candidate
  property_count: 7
  slug: bindbee-candidate
- name: CandidatesResponse
  property_count: 1
  slug: bindbee-candidates-response
- name: Department
  property_count: 3
  slug: bindbee-department
- name: DepartmentsResponse
  property_count: 1
  slug: bindbee-departments-response
- name: Employee
  property_count: 8
  slug: bindbee-employee
- name: EmployeesResponse
  property_count: 3
  slug: bindbee-employees-response
- name: Job
  property_count: 6
  slug: bindbee-job
- name: JobsResponse
  property_count: 1
  slug: bindbee-jobs-response
- name: TimeOffRequest
  property_count: 6
  slug: bindbee-time-off-request
- name: TimeOffResponse
  property_count: 1
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
modified: '2026-04-21'
name: Bindbee
nav: Providers
network: true
overview: 'Bindbee publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Candidates API, Departments API, Employees API, and 2 more. Tagged areas include ATS, HR Integration, HRIS, and Workforce.


  The Bindbee catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Bindbee''s developer surface includes authentication, developer portal, documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Bindbee Plans Pricing
  plan_count: 3
  slug: bindbee-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
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
  band: emerging
  composite: 25.2
  coverage:
    artifact_dirs: 17
    catalog_gap: 60.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 28.8
    contract_quality: 22.0
    developer_ergonomics: 33.3
    discoverability: 53.7
    governance: 28.8
    operational_transparency: 7.9
  previous_composite: 25.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bindbee/refs/heads/main/screenshots/bindbee-2026-06-20T173245.png
security:
- kind: authentication
  name: Bindbee Authentication
  slug: bindbee-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Bindbee Domain Security
  slug: bindbee-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bindbee
tags:
- ATS
- HR Integration
- HRIS
- Workforce
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
website: https://bindbee.dev/
---
