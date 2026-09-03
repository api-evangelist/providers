---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
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
  score: 24.8
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Oracle Primavera Agentic Access
  operation_count: 13
  slug: oracle-primavera-agentic-access
  summary_line: 13 operations · 5 acting
api_count: 1
apis:
- description: Oracle Primavera Gateway provides integration APIs for connecting Primavera P6 with other Oracle and third-party applications. Enables bi-directional data exchange for projects, resources, cost accoun
  name: Oracle Primavera Gateway Integration API
  slug: oracle-primavera-gateway-integration-api
- description: Oracle Primavera Analytics provides reporting and business intelligence APIs for portfolio performance insights, project health dashboards, resource utilization analysis, and earned value management r
  name: Oracle Primavera Analytics API
  slug: oracle-primavera-analytics-api
- description: Oracle Primavera P6 provides project scheduling and portfolio management APIs for construction, engineering, and capital projects. REST and XML APIs enable access to WBS structures, activity schedules
  name: Oracle Primavera P6 Scheduling API
  slug: oracle-primavera-p6-scheduling-api
- baseURL: https://{host}/p6ws/rest/v1
  baseurl_source: declared
  description: Activity scheduling and management
  name: Oracle Primavera Activities API
  slug: oracle-primavera-activities-api
- baseURL: https://{host}/p6ws/rest/v1
  baseurl_source: declared
  description: Project baseline operations
  name: Oracle Primavera Baselines API
  slug: oracle-primavera-baselines-api
- baseURL: https://{host}/p6ws/rest/v1
  baseurl_source: declared
  description: Project management operations
  name: Oracle Primavera Projects API
  slug: oracle-primavera-projects-api
- baseURL: https://{host}/p6ws/rest/v1
  baseurl_source: declared
  description: Resource assignment operations
  name: Oracle Primavera ResourceAssignments API
  slug: oracle-primavera-resourceassignments-api
- baseURL: https://{host}/p6ws/rest/v1
  baseurl_source: declared
  description: Resource and role management
  name: Oracle Primavera Resources API
  slug: oracle-primavera-resources-api
- baseURL: https://{host}/p6ws/rest/v1
  baseurl_source: declared
  description: Work Breakdown Structure management
  name: Oracle Primavera WBS API
  slug: oracle-primavera-wbs-api
artifact_total: 34
collections:
- collection_type: postman
  name: Oracle Primavera P6 EPPM REST Activities API
  slug: postman-oracle-primavera-activities-api
- collection_type: postman
  name: Oracle Primavera P6 EPPM REST Activities Baselines API
  slug: postman-oracle-primavera-baselines-api
- collection_type: postman
  name: Oracle Primavera P6 EPPM REST Activities Projects API
  slug: postman-oracle-primavera-projects-api
- collection_type: postman
  name: Oracle Primavera P6 EPPM REST Activities ResourceAssignments API
  slug: postman-oracle-primavera-resourceassignments-api
- collection_type: postman
  name: Oracle Primavera P6 EPPM REST Activities Resources API
  slug: postman-oracle-primavera-resources-api
- collection_type: postman
  name: Oracle Primavera P6 EPPM REST Activities WBS API
  slug: postman-oracle-primavera-wbs-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Oracle Primavera P6 EPPM REST Activities API
  slug: open-oracle-primavera-activities-api
- collection_type: open
  name: Oracle Primavera P6 EPPM REST Activities Baselines API
  slug: open-oracle-primavera-baselines-api
- collection_type: open
  name: Oracle Primavera P6 EPPM REST API
  slug: open-oracle-primavera-p6-eppm
- collection_type: open
  name: Oracle Primavera P6 EPPM REST Activities Projects API
  slug: open-oracle-primavera-projects-api
- collection_type: open
  name: Oracle Primavera P6 EPPM REST Activities ResourceAssignments API
  slug: open-oracle-primavera-resourceassignments-api
- collection_type: open
  name: Oracle Primavera P6 EPPM REST Activities Resources API
  slug: open-oracle-primavera-resources-api
- collection_type: open
  name: Oracle Primavera P6 EPPM REST Activities WBS API
  slug: open-oracle-primavera-wbs-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/oracle-primavera-capability-edges.yml
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/oracle/
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/oracle-primavera/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/oracle-primavera-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/oracle-primavera-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/oracle-primavera-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/oracle-primavera-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/oracle
- group: start
  title: ''
  type: Portal
  url: https://docs.oracle.com/en/industries/construction-engineering/primavera/
- group: company
  title: ''
  type: Website
  url: https://www.oracle.com/construction-engineering/primavera/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.oracle.com/en/industries/construction-engineering/primavera-p6-project/index.html
- group: docs
  title: ''
  type: Reference
  url: https://docs.oracle.com/cd/G48897_01/index.htm
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.oracle.com/cd/E64687_01/EPPM/EPPM_CFO.html
- group: start
  title: ''
  type: GettingStarted
  url: https://mylearn.oracle.com/construction
- group: operate
  title: ''
  type: Support
  url: https://www.oracle.com/support/
- group: operate
  title: ''
  type: StatusPage
  url: https://ocistatus.oraclecloud.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.oracle.com/legal/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.oracle.com/legal/terms.html
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/oracle-primavera-p6-eppm-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/oracle-primavera-project-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/oracle-primavera-activity-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/oracle-primavera-context.jsonld
created: '2024-01-01'
description: Oracle Primavera is a portfolio of project portfolio management (PPM) applications for construction, engineering, and capital project industries. Primavera APIs provide programmatic access to enterprise project portfolio management data including WBS structures, activity schedules, resource assignments, critical path analysis, and portfolio dashboards across cloud and on-premises deployments.
finops:
- name: Oracle Primavera Finops
  service_category: Project Management
  slug: oracle-primavera-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/oracle-primavera.png
json_schemas:
- name: Oracle Primavera P6 Activity
  property_count: 24
  slug: oracle-primavera-activity
- name: Oracle Primavera P6 Project
  property_count: 21
  slug: oracle-primavera-project
jsonld:
- class_count: 0
  name: Oracle Primavera Context
  property_count: 26
  slug: oracle-primavera-context
layout: provider
modified: '2026-08-21'
name: Oracle Primavera
nav: Providers
network: true
overview: 'Oracle Primavera publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Activities API, Baselines API, Projects API, and 3 more. Tagged areas include Construction, Engineering, Project Management, Scheduling, and Portfolio-Management.


  The Oracle Primavera catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Oracle Primavera''s developer surface includes authentication, developer portal, documentation, changelog, getting-started guide, support, and 16 more developer resources.'
plans:
- name: Oracle Primavera Plans Pricing
  plan_count: 3
  slug: oracle-primavera-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 3
  name: Oracle Primavera Rate Limits
  slug: oracle-primavera-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Oracle Primavera API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: oracle-primavera-jsonschema-spectral-rules
scopes:
- name: Oracle Primavera Scopes
  scope_count: 2
  slug: oracle-primavera-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: developing
  composite: 45.1
  coverage:
    artifact_dirs: 15
    catalog_gap: 62.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 9.8
    contract_quality: 62.6
    developer_ergonomics: 47.6
    discoverability: 59.3
    governance: 9.8
    operational_transparency: 42.1
  previous_composite: 45.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/oracle-primavera/refs/heads/main/screenshots/oracle-primavera-2026-06-20T191153.png
security:
- kind: authentication
  name: Oracle Primavera Authentication
  slug: oracle-primavera-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Oracle Primavera Domain Security
  slug: oracle-primavera-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: oracle-primavera
tags:
- Construction
- Engineering
- Project Management
- Scheduling
- Portfolio-Management
- Oracle
website: https://www.oracle.com/construction-engineering/primavera/
---
