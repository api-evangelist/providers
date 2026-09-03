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
    auth_clarity: negotiable
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
  score: 22.7
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Cmic Agentic Access
  operation_count: 11
  slug: cmic-agentic-access
  summary_line: 11 operations · 2 acting
api_count: 1
apis:
- description: CMiC's Power BI Connector allows users to connect Microsoft Power BI directly to CMiC ERP data through the CMiC API, enabling business intelligence dashboards and reports for construction project fina
  name: CMiC API Power BI Connector
  slug: cmic-power-bi-connector
- baseURL: https://api.cmic.ca
  baseurl_source: declared
  description: Job cost codes, budgets, and committed costs
  name: CMiC Cost Tracking API
  slug: cmic-cost-tracking-api
- baseURL: https://api.cmic.ca
  baseurl_source: declared
  description: Document management and approvals
  name: CMiC Documents API
  slug: cmic-documents-api
- baseURL: https://api.cmic.ca
  baseurl_source: declared
  description: Equipment tracking and usage
  name: CMiC Equipment API
  slug: cmic-equipment-api
- baseURL: https://api.cmic.ca
  baseurl_source: declared
  description: Job and cost code tracking
  name: CMiC Jobs API
  slug: cmic-jobs-api
- baseURL: https://api.cmic.ca
  baseurl_source: declared
  description: Construction project management
  name: CMiC Projects API
  slug: cmic-projects-api
- baseURL: https://api.cmic.ca
  baseurl_source: declared
  description: Subcontractor and vendor management
  name: CMiC Subcontractors API
  slug: cmic-subcontractors-api
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CMiC Construction ERP API
  slug: open-cmic-construction-erp
- collection_type: open
  name: CMiC Construction ERP Cost Tracking API
  slug: open-cmic-cost-tracking-api
- collection_type: open
  name: CMiC Construction ERP Cost Tracking Documents API
  slug: open-cmic-documents-api
- collection_type: open
  name: CMiC Construction ERP Cost Tracking Equipment API
  slug: open-cmic-equipment-api
- collection_type: open
  name: CMiC Construction ERP Cost Tracking Jobs API
  slug: open-cmic-jobs-api
- collection_type: open
  name: CMiC Construction ERP Cost Tracking Projects API
  slug: open-cmic-projects-api
- collection_type: open
  name: CMiC Construction ERP Cost Tracking Subcontractors API
  slug: open-cmic-subcontractors-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/cmic-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cmic-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cmic-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cmic-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cmic-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cmic
- group: company
  title: ''
  type: Website
  url: https://cmicglobal.com/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/cmic-construction-erp-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/cmic-project-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/cmic-context.jsonld
- group: design
  title: ''
  type: SpectralRuleset
  url: rules/cmic-rules.yml
- group: start
  title: ''
  type: Portal
  url: https://developers.cmicglobal.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cmicglobal.com/portal/Content/Home.htm
- group: auth
  title: ''
  type: Authentication
  url: https://developers.cmicglobal.com/v1/docs/authentication
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.cmicglobal.com/docs/developer-api-account
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cmicglobal.com/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://cmicglobal.com/resources/
created: '2026-03-18'
description: CMiC is a unified construction-industry ERP and project management platform used by general contractors, civil contractors, and heavy/highway builders. CMiC exposes an OAuth 2.0 secured REST API (api.cmic.ca) along with a Power BI connector for accessing project financials, job costing, subcontractor and vendor management, equipment tracking, and document management with application-level security applied across company, job, project, and employee scopes.
finops:
- name: Cmic Finops
  service_category: API
  slug: cmic-finops
json_schemas:
- name: CMiC Construction Project
  property_count: 14
  slug: cmic-project
jsonld:
- class_count: 9
  name: Cmic Context
  property_count: 21
  slug: cmic-context
layout: provider
modified: '2026-05-19'
name: CMiC
nav: Providers
network: true
overview: 'CMiC publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Cost Tracking API, Documents API, Equipment API, and 3 more. Tagged areas include Construction, ERP, Finance, and Project Management.


  The CMiC catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  CMiC''s developer surface includes authentication, developer portal, documentation, getting-started guide, engineering blog, and 12 more developer resources.'
plans:
- name: Cmic Plans Pricing
  plan_count: 3
  slug: cmic-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Cmic Rate Limits
  slug: cmic-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: CMiC API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: cmic-jsonschema-spectral-rules
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: CMiC API Rules
  rule_count: 9
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 5
  slug: cmic-rules
scopes:
- name: Cmic Scopes
  scope_count: 1
  slug: cmic-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: developing
  composite: 39.9
  coverage:
    artifact_dirs: 15
    catalog_gap: 54.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 13.6
    contract_quality: 63.8
    developer_ergonomics: 52.4
    discoverability: 55.6
    governance: 13.6
    operational_transparency: 7.9
  previous_composite: 39.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cmic/refs/heads/main/screenshots/cmic-2026-06-20T174629.png
security:
- kind: authentication
  name: Cmic Authentication
  slug: cmic-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Cmic Domain Security
  slug: cmic-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: cmic
tags:
- Construction
- ERP
- Finance
- Project Management
website: https://cmicglobal.com/
---
