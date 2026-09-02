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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 16
  human_in_the_loop: 2
  name: Singlestore Agentic Access
  operation_count: 29
  slug: singlestore-agentic-access
  summary_line: 29 operations · 16 acting · 2 human-in-the-loop
api_count: 2
apis:
- description: Upload, download, list, and delete files in the personal, shared, or models space within SingleStore Helios Spaces (stage storage).
  name: SingleStore Files API
  slug: singlestore-files-api
- description: Health check operations for verifying connectivity to the Data API endpoint without requiring authentication credentials.
  name: SingleStore Health API
  slug: singlestore-health-api
- description: Create, retrieve, list, and delete scheduled notebook jobs within SingleStore Helios. Jobs enable automated execution of notebooks on configurable schedules.
  name: SingleStore Jobs API
  slug: singlestore-jobs-api
- description: Retrieve information about the current user's organization within SingleStore Helios.
  name: SingleStore Organizations API
  slug: singlestore-organizations-api
- description: Execute SQL statements against a SingleStore Helios workspace over HTTP. Supports DDL, DML, and SELECT statements returning results as JSON.
  name: SingleStore Queries API
  slug: singlestore-queries-api
- description: List available cloud provider regions that support workspace group creation, including shared tier regions.
  name: SingleStore Regions API
  slug: singlestore-regions-api
- description: Manage organization-level secrets that can be referenced securely in notebooks and jobs without exposing plaintext credentials.
  name: SingleStore Secrets API
  slug: singlestore-secrets-api
- description: Create, list, retrieve, update, and delete workspace groups within a SingleStore Helios organization. Workspace groups are logical containers that group workspaces by region and network configuration.
  name: SingleStore WorkspaceGroups API
  slug: singlestore-workspacegroups-api
- description: Create, list, retrieve, update, suspend, resume, and delete workspaces within a workspace group. Workspaces are the compute resources that connect to a SingleStore database.
  name: SingleStore Workspaces API
  slug: singlestore-workspaces-api
artifact_total: 45
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
  name: API Collection
  slug: open-.refine-report
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
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/singlestore/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/singlestore-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/singlestore-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/singlestore-domain-security.yml
- group: auth
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
- name: Singlestore Finops
  service_category: API
  slug: singlestore-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/singlestore.png
json_schemas:
- name: SingleStore Data API Query
  property_count: 3
  slug: singlestore-query
- name: SingleStore Workspace
  property_count: 10
  slug: singlestore-workspace
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
overview: 'SingleStore publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Files API, Health API, Jobs API, and 6 more. Tagged areas include Database, SQL, Analytics, Cloud, and Distributed SQL.


  The SingleStore catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  SingleStore''s developer surface includes authentication, documentation, pricing, engineering blog, signup flow, support, and 11 more developer resources.'
plans:
- name: Singlestore Plans Pricing
  plan_count: 3
  slug: singlestore-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Singlestore Rate Limits
  slug: singlestore-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: SingleStore API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: singlestore-jsonschema-spectral-rules
- effective_rule_count: 8
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
  composite: 45.0
  coverage:
    artifact_dirs: 18
    catalog_gap: 60.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.7
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 9.8
    contract_quality: 63.8
    developer_ergonomics: 42.9
    discoverability: 75.9
    governance: 9.8
    operational_transparency: 13.2
  previous_composite: 44.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 77.8
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/singlestore/refs/heads/main/screenshots/singlestore-2026-06-20T193949.png
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
  summary_line: disclosure policy published
slug: singlestore
tags:
- Database
- SQL
- Analytics
- Cloud
- Distributed SQL
website: https://www.singlestore.com/
---
