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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
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
  score: 25.5
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Workday Integrations Agentic Access
  operation_count: 30
  slug: workday-integrations-agentic-access
  summary_line: 30 operations · 5 acting
api_count: 3
apis:
- description: Comprehensive SOAP-based web services for deep integration with Workday including Human Capital Management, Financial Management, and custom integrations.
  name: Workday SOAP Web Services
  slug: workday-soap-web-services
- baseURL: https://wd2-impl-services1.workday.com/ccx/api/v1/{tenant}
  baseurl_source: declared
  description: Access benefit plans and worker benefit enrollments
  name: Workday Integrations Benefits API
  slug: workday-integrations-benefits-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/api/v1/{tenant}
  baseurl_source: declared
  description: Interact with Workday business process workflows
  name: Workday Integrations Business Processes API
  slug: workday-integrations-business-processes-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/api/v1/{tenant}
  baseurl_source: declared
  description: Access compensation plans and worker compensation data
  name: Workday Integrations Compensation API
  slug: workday-integrations-compensation-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/api/v1/{tenant}
  baseurl_source: declared
  description: Discover available Workday and external data sources
  name: Workday Integrations Data Sources API
  slug: workday-integrations-data-sources-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/api/v1/{tenant}
  baseurl_source: declared
  description: Upload external data files into datasets
  name: Workday Integrations Data Upload API
  slug: workday-integrations-data-upload-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/api/v1/{tenant}
  baseurl_source: declared
  description: Manage Prism Analytics dataset definitions
  name: Workday Integrations Datasets API
  slug: workday-integrations-datasets-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/api/v1/{tenant}
  baseurl_source: declared
  description: Access job profile definitions and configurations
  name: Workday Integrations Job Profiles API
  slug: workday-integrations-job-profiles-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/api/v1/{tenant}
  baseurl_source: declared
  description: Retrieve and manage organizational structures and hierarchies
  name: Workday Integrations Organizations API
  slug: workday-integrations-organizations-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/api/v1/{tenant}
  baseurl_source: declared
  description: Access payroll data and pay group configurations
  name: Workday Integrations Payroll API
  slug: workday-integrations-payroll-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/api/v1/{tenant}
  baseurl_source: declared
  description: Manage position records and staffing
  name: Workday Integrations Positions API
  slug: workday-integrations-positions-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/api/v1/{tenant}
  baseurl_source: declared
  description: Manage job requisitions and candidate applications
  name: Workday Integrations Recruiting API
  slug: workday-integrations-recruiting-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/api/v1/{tenant}
  baseurl_source: declared
  description: Retrieve report field definitions and filter parameters
  name: Workday Integrations Report Metadata API
  slug: workday-integrations-report-metadata-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/api/v1/{tenant}
  baseurl_source: declared
  description: Access custom and standard Workday reports
  name: Workday Integrations Reports API
  slug: workday-integrations-reports-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/api/v1/{tenant}
  baseurl_source: declared
  description: Manage data tables derived from datasets
  name: Workday Integrations Tables API
  slug: workday-integrations-tables-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/api/v1/{tenant}
  baseurl_source: declared
  description: Manage time off requests and balances
  name: Workday Integrations Time Off API
  slug: workday-integrations-time-off-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/api/v1/{tenant}
  baseurl_source: declared
  description: Access and manage worker records including employees and contingent workers
  name: Workday Integrations Workers API
  slug: workday-integrations-workers-api
artifact_total: 55
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Workday Integrations Workday Prism Analytics Benefits API
  slug: open-workday-integrations-benefits-api
- collection_type: open
  name: Workday Integrations Workday Prism Analytics Benefits Business Processes API
  slug: open-workday-integrations-business-processes-api
- collection_type: open
  name: Workday Integrations Workday Prism Analytics Benefits Compensation API
  slug: open-workday-integrations-compensation-api
- collection_type: open
  name: Workday Integrations Workday Prism Analytics Benefits Data Sources API
  slug: open-workday-integrations-data-sources-api
- collection_type: open
  name: Workday Integrations Workday Prism Analytics Benefits Data Upload API
  slug: open-workday-integrations-data-upload-api
- collection_type: open
  name: Workday Integrations Workday Prism Analytics Benefits Datasets API
  slug: open-workday-integrations-datasets-api
- collection_type: open
  name: Workday Integrations Workday Prism Analytics Benefits Job Profiles API
  slug: open-workday-integrations-job-profiles-api
- collection_type: open
  name: Workday Integrations Workday Prism Analytics Benefits Organizations API
  slug: open-workday-integrations-organizations-api
- collection_type: open
  name: Workday Integrations Workday Prism Analytics Benefits Payroll API
  slug: open-workday-integrations-payroll-api
- collection_type: open
  name: Workday Integrations Workday Prism Analytics Benefits Positions API
  slug: open-workday-integrations-positions-api
- collection_type: open
  name: Workday Integrations Workday Prism Analytics API
  slug: open-workday-integrations-prism-analytics
- collection_type: open
  name: Workday Integrations Workday Report-as-a-Service (RaaS) API
  slug: open-workday-integrations-raas
- collection_type: open
  name: Workday Integrations Workday Prism Analytics Benefits Recruiting API
  slug: open-workday-integrations-recruiting-api
- collection_type: open
  name: Workday Integrations Workday Prism Analytics Benefits Report Metadata API
  slug: open-workday-integrations-report-metadata-api
- collection_type: open
  name: Workday Integrations Workday Prism Analytics Benefits Reports API
  slug: open-workday-integrations-reports-api
- collection_type: open
  name: Workday Integrations Workday REST API
  slug: open-workday-integrations-rest-api
- collection_type: open
  name: Workday Integrations Workday Prism Analytics Benefits Tables API
  slug: open-workday-integrations-tables-api
- collection_type: open
  name: Workday Integrations Workday Prism Analytics Benefits Time Off API
  slug: open-workday-integrations-time-off-api
- collection_type: open
  name: Workday Integrations Workday Prism Analytics Benefits Workers API
  slug: open-workday-integrations-workers-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/workday-integrations-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/workday-integrations-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/workday-integrations-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/workday-integrations-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://newsroom.workday.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://community.workday.com/developer
- group: docs
  title: ''
  type: Authentication Guide
  url: https://doc.workday.com/admin-guide/en-us/integration/integration-security/authentication-overview.html
- group: build
  title: ''
  type: Integration Cloud Platform
  url: https://www.workday.com/en-us/products/platform-product-extensions/workday-integration-cloud.html
- group: other
  title: ''
  type: Studio
  url: https://doc.workday.com/admin-guide/en-us/integration/workday-studio/workday-studio-overview.html
- group: operate
  title: ''
  type: Community
  url: https://community.workday.com/
- group: operate
  title: ''
  type: Support
  url: https://www.workday.com/en-us/customer-experience/support.html
- group: operate
  title: ''
  type: StatusPage
  url: https://status.workday.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.workday.com/en-us/legal.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.workday.com/en-us/privacy.html
- group: design
  title: ''
  type: JSONLD
  url: json-ld/workday-integrations-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/workday-integrations-worker-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/workday-integrations-organization-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/workday-integrations-position-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/workday-integrations-compensation-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/workday-integrations-dataset-schema.json
- group: design
  title: ''
  type: SpectralRules
  url: rules/workday-integrations-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/workday-integrations-vocabulary.yml
created: '2025-03-15'
description: Workday provides cloud-based enterprise software for finance, HR, and planning. This APIs.json file describes the integration capabilities and APIs available for connecting Workday with other systems.
examples:
- key_count: 2
  name: Workday Integrations List Workers Example
  slug: workday-integrations-list-workers-example
- key_count: 2
  name: Workday Integrations Upload Dataset Example
  slug: workday-integrations-upload-dataset-example
finops:
- name: Workday Integrations Finops
  service_category: Integration / iPaaS
  slug: workday-integrations-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/workday-integrations.png
json_schemas:
- name: Workday Compensation Detail
  property_count: 7
  slug: workday-integrations-compensation
- name: Workday Prism Analytics Dataset
  property_count: 9
  slug: workday-integrations-dataset
- name: Workday Organization
  property_count: 8
  slug: workday-integrations-organization
- name: Workday Position
  property_count: 9
  slug: workday-integrations-position
- name: Workday Worker
  property_count: 6
  slug: workday-integrations-worker
json_structures:
- name: Workday Integrations Worker Structure
  property_count: 0
  slug: workday-integrations-worker-structure
jsonld:
- class_count: 0
  name: Workday Integrations Context
  property_count: 11
  slug: workday-integrations-context
layout: provider
modified: '2026-05-19'
name: Workday Integrations
nav: Providers
network: true
overview: 'Workday Integrations publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Benefits API, Business Processes API, Compensation API, and 13 more. Tagged areas include Cloud, Enterprise Software, ERP, Finance, and HCM.


  The Workday Integrations catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Workday Integrations'' developer surface includes authentication, engineering blog, support, and 19 more developer resources.'
plans:
- name: Workday Integrations Plans Pricing
  plan_count: 1
  slug: workday-integrations-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 2
  name: Workday Integrations Rate Limits
  slug: workday-integrations-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Workday Integrations API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: workday-integrations-jsonschema-spectral-rules
- effective_rule_count: 52
  extends:
  - spectral:oas
  name: Workday Integrations API Rules
  rule_count: 11
  severity_counts:
    error: 4
    hint: 1
    info: 0
    warn: 6
  slug: workday-integrations-rules
score:
  band: developing
  composite: 43.6
  coverage:
    artifact_dirs: 16
    catalog_gap: 50.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 28.8
    contract_quality: 66.1
    developer_ergonomics: 35.7
    discoverability: 74.1
    governance: 28.8
    operational_transparency: 5.3
  previous_composite: 43.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/workday-integrations/refs/heads/main/screenshots/workday-integrations-2026-06-20T201603.png
security:
- kind: authentication
  name: Workday Integrations Authentication
  slug: workday-integrations-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Workday Integrations Domain Security
  slug: workday-integrations-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Workday Integrations Trust Center
  slug: workday-integrations-trust-center
  summary_line: SOC 2, ISO 27001, FedRAMP, GDPR
slug: workday-integrations
tags:
- Cloud
- Enterprise Software
- ERP
- Finance
- HCM
- HR
- Integration
website: https://community.workday.com/developer
---
