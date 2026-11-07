---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 14
  human_in_the_loop: 2
  name: Singlestore Agentic Access
  operation_count: 29
  slug: singlestore-agentic-access
  summary_line: 29 operations · 14 acting · 2 human-in-the-loop
api_count: 2
apis:
- baseURL: https://{workspaceHost}
  baseurl_source: declared
  description: Upload, download, list, and delete files in the personal, shared, or models space within SingleStore Helios Spaces (stage storage).
  name: SingleStore Files API
  slug: singlestore-files-api
- baseURL: https://{workspaceHost}
  baseurl_source: declared
  description: Health check operations for verifying connectivity to the Data API endpoint without requiring authentication credentials.
  name: SingleStore Health API
  slug: singlestore-health-api
- baseURL: https://{workspaceHost}
  baseurl_source: declared
  description: Create, retrieve, list, and delete scheduled notebook jobs within SingleStore Helios. Jobs enable automated execution of notebooks on configurable schedules.
  name: SingleStore Jobs API
  slug: singlestore-jobs-api
- baseURL: https://{workspaceHost}
  baseurl_source: declared
  description: Retrieve information about the current user's organization within SingleStore Helios.
  name: SingleStore Organizations API
  slug: singlestore-organizations-api
- baseURL: https://{workspaceHost}
  baseurl_source: declared
  description: Execute SQL statements against a SingleStore Helios workspace over HTTP. Supports DDL, DML, and SELECT statements returning results as JSON.
  name: SingleStore Queries API
  slug: singlestore-queries-api
- baseURL: https://{workspaceHost}
  baseurl_source: declared
  description: List available cloud provider regions that support workspace group creation, including shared tier regions.
  name: SingleStore Regions API
  slug: singlestore-regions-api
- baseURL: https://{workspaceHost}
  baseurl_source: declared
  description: Manage organization-level secrets that can be referenced securely in notebooks and jobs without exposing plaintext credentials.
  name: SingleStore Secrets API
  slug: singlestore-secrets-api
- baseURL: https://{workspaceHost}
  baseurl_source: declared
  description: Create, list, retrieve, update, suspend, resume, and delete workspaces within a workspace group. Workspaces are the compute resources that connect to a SingleStore database.
  name: SingleStore Workspaces API
  slug: singlestore-workspaces-api
- baseURL: https://{workspaceHost}
  baseurl_source: declared
  description: Create, list, retrieve, update, and delete workspace groups within a SingleStore Helios organization. Workspace groups are logical containers that group workspaces by region and network configuration.
  name: SingleStore Workspace Groups API
  slug: singlestore-workspace-groups-api
artifact_total: 62
collections:
- collection_type: postman
  name: SingleStore Data Files API
  slug: postman-singlestore-files-api
- collection_type: postman
  name: SingleStore Data Files Health API
  slug: postman-singlestore-health-api
- collection_type: postman
  name: SingleStore Data Files Jobs API
  slug: postman-singlestore-jobs-api
- collection_type: postman
  name: SingleStore Data Files Organizations API
  slug: postman-singlestore-organizations-api
- collection_type: postman
  name: SingleStore Data Files Queries API
  slug: postman-singlestore-queries-api
- collection_type: postman
  name: SingleStore Data Files Regions API
  slug: postman-singlestore-regions-api
- collection_type: postman
  name: SingleStore Data Files Secrets API
  slug: postman-singlestore-secrets-api
- collection_type: postman
  name: SingleStore Data Files WorkspaceGroups API
  slug: postman-singlestore-workspacegroups-api
- collection_type: postman
  name: SingleStore Data Files Workspaces API
  slug: postman-singlestore-workspaces-api
- collection_type: open
  name: SingleStore Data API
  slug: open-singlestore-data-api
- collection_type: open
  name: SingleStore Data Files API
  slug: open-singlestore-files-api
- collection_type: open
  name: SingleStore Data Files Health API
  slug: open-singlestore-health-api
- collection_type: open
  name: SingleStore Data Files Jobs API
  slug: open-singlestore-jobs-api
- collection_type: open
  name: SingleStore Management API
  slug: open-singlestore-management-api
- collection_type: open
  name: SingleStore Data Files Organizations API
  slug: open-singlestore-organizations-api
- collection_type: open
  name: SingleStore Data Files Queries API
  slug: open-singlestore-queries-api
- collection_type: open
  name: SingleStore Data Files Regions API
  slug: open-singlestore-regions-api
- collection_type: open
  name: SingleStore Data Files Secrets API
  slug: open-singlestore-secrets-api
- collection_type: open
  name: SingleStore Data Files WorkspaceGroups API
  slug: open-singlestore-workspacegroups-api
- collection_type: open
  name: SingleStore Data Files Workspaces API
  slug: open-singlestore-workspaces-api
common:
- group: commercial
  href: https://artifacts.apis.io/singlestore/plans/singlestore-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/singlestore-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/singlestore/rate-limits/singlestore-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/singlestore-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/singlestore/finops/singlestore-finops.yml
  title: ''
  type: FinOps
  url: finops/singlestore-finops.yml
- group: other
  href: https://artifacts.apis.io/singlestore/capabilities/singlestore-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/singlestore-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/singlestore/overview
- group: agent
  href: https://artifacts.apis.io/singlestore/agentic-access/singlestore-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/singlestore-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/singlestore/security/singlestore-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/singlestore-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/singlestore/security/singlestore-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/singlestore-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/singlestore/authentication/singlestore-authentication.yml
  title: ''
  type: Authentication
  url: authentication/singlestore-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/singlestore
- group: company
  title: ''
  type: Website
  url: https://www.singlestore.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.singlestore.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.singlestore.com/cloud/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.singlestore.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.singlestore.com/blog/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/singlestore-labs
- group: start
  title: ''
  type: Signup
  url: https://www.singlestore.com/cloud-trial/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.singlestore.com/cloud-terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.singlestore.com/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://support.singlestore.com
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.singlestore.com/llms.txt
created: '2025-01-01'
description: SingleStore is a cloud-native distributed SQL database designed for real-time analytics and mixed workloads. It offers a management API for provisioning and managing cloud workspaces, and a data API for executing SQL statements over HTTP without requiring native database drivers. SingleStore Helios is the fully managed cloud service providing serverless database capabilities with elastic scaling.
examples:
- key_count: 4
  name: Singlestore Execute Sql Example
  slug: singlestore-execute-sql-example
- key_count: 4
  name: Singlestore Query Rows Example
  slug: singlestore-query-rows-example
finops:
- has_sources: true
  method: derived
  name: Singlestore Finops
  primary_unit: hour
  service_category: ''
  slug: singlestore-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/singlestore.png
json_schemas:
- name: ExecRequest
  property_count: 3
  slug: singlestore-exec-request
- name: ExecResponse
  property_count: 1
  slug: singlestore-exec-response
- name: JobCreate
  property_count: 6
  slug: singlestore-job-create
- name: JobExecution
  property_count: 8
  slug: singlestore-job-execution
- name: Job
  property_count: 10
  slug: singlestore-job
- name: Organization
  property_count: 3
  slug: singlestore-organization
- name: QueryRequest
  property_count: 3
  slug: singlestore-query-request
- name: QueryRowsResponse
  property_count: 1
  slug: singlestore-query-rows-response
- name: SingleStore Data API Query
  property_count: 3
  slug: singlestore-query
- name: QueryTuplesResponse
  property_count: 1
  slug: singlestore-query-tuples-response
- name: Region
  property_count: 4
  slug: singlestore-region
- name: Secret
  property_count: 6
  slug: singlestore-secret
- name: WorkspaceCreate
  property_count: 6
  slug: singlestore-workspace-create
- name: WorkspaceDeleteResponse
  property_count: 1
  slug: singlestore-workspace-delete-response
- name: WorkspaceGroupCreate
  property_count: 6
  slug: singlestore-workspace-group-create
- name: WorkspaceGroupDeleteResponse
  property_count: 1
  slug: singlestore-workspace-group-delete-response
- name: WorkspaceGroup
  property_count: 8
  slug: singlestore-workspace-group
- name: WorkspaceGroupUpdate
  property_count: 4
  slug: singlestore-workspace-group-update
- name: SingleStore Workspace
  property_count: 10
  slug: singlestore-workspace
- name: WorkspaceUpdate
  property_count: 3
  slug: singlestore-workspace-update
json_structures:
- name: Singlestore Workspace Structure
  property_count: 0
  slug: singlestore-workspace-structure
jsonld:
- class_count: 0
  name: Singlestore Context
  property_count: 9
  slug: singlestore-context
layout: provider
modified: '2026-05-19'
name: SingleStore
nav: Providers
network: true
overview: 'SingleStore publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Files API, Health API, Jobs API, and 6 more. Tagged areas include Database, SQL, Analytics, Cloud, and Distributed SQL.


  The SingleStore catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  SingleStore''s developer surface includes authentication, documentation, pricing, engineering blog, signup flow, support, and 15 more developer resources.'
plans:
- name: Singlestore Plans Pricing
  plan_count: 4
  slug: singlestore-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 5
  name: Singlestore Rate Limits
  slug: singlestore-rate-limits
rules:
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: SingleStore — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: singlestore-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 8
  extends: []
  name: SingleStore API Rules
  rule_count: 8
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 4
  slug: singlestore-rules
score:
  band: developing
  composite: 52.1
  coverage:
    artifact_dirs: 32
    catalog_earned: 63.3
    catalog_earned_first_party: 12.0
    catalog_gap: 51.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 73.7
    contract_governance: 28.0
    contract_quality: 58.8
    developer_ergonomics: 39.3
    discoverability: 73.2
    operational_transparency: 23.7
  previous_composite: 52.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/singlestore/singlestore-2026-06-20T193949.png
security:
- kind: authentication
  name: Singlestore Authentication
  slug: singlestore-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Singlestore Domain Security
  slug: singlestore-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Singlestore Vulnerability Disclosure
  slug: singlestore-vulnerability-disclosure
  summary_line: no policy recorded
slug: singlestore
tags:
- Database
- SQL
- Analytics
- Cloud
- Distributed SQL
website: https://www.singlestore.com/
---
