---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
    error_semantics: false
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
  score: 28.7
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Uspto Agentic Access
  operation_count: 8
  slug: uspto-agentic-access
  summary_line: 8 operations
api_count: 1
apis:
- description: The USPTO Patent Assignment Search API retrieves patent assignment information including ownership transfers, recorded assignments, and assignment history for individual patents and patent portfolios.
  name: USPTO Patent Assignment Search API
  slug: assignment-search-api
- baseURL: https://data.uspto.gov/api/v1
  baseurl_source: declared
  description: Patent assignment records
  name: USPTO Assignments API
  slug: uspto-assignments-api
- baseURL: https://data.uspto.gov/api/v1
  baseurl_source: declared
  description: Patent search and retrieval
  name: USPTO Patents API
  slug: uspto-patents-api
- baseURL: https://data.uspto.gov/api/v1
  baseurl_source: declared
  description: Patent Trial and Appeal Board proceedings
  name: USPTO PTAB API
  slug: uspto-ptab-api
- baseURL: https://data.uspto.gov/api/v1
  baseurl_source: declared
  description: Trademark status and documents
  name: USPTO Trademarks API
  slug: uspto-trademarks-api
artifact_total: 42
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: USPTO Patent & Trademark Assignments API
  slug: open-uspto-assignments-api
- collection_type: open
  name: USPTO Patent & Trademark API
  slug: open-uspto-patent-api
- collection_type: open
  name: USPTO Patent & Trademark Assignments Patents API
  slug: open-uspto-patents-api
- collection_type: open
  name: USPTO Patent & Trademark Assignments PTAB API
  slug: open-uspto-ptab-api
- collection_type: open
  name: USPTO Patent & Trademark Assignments Trademarks API
  slug: open-uspto-trademarks-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/uspto-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/uspto-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/uspto-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/uspto-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/USPTO
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/uspto
- group: start
  title: ''
  type: Portal
  url: https://developer.uspto.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.uspto.gov/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.uspto.gov/api-catalog
- group: build
  title: ''
  type: DeveloperTools
  url: https://data.uspto.gov/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.uspto.gov/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://www.uspto.gov/
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/uspto-patent-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/uspto-context.jsonld
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/uspto-patent-structure.json
- group: design
  title: ''
  type: SpectralRules
  url: rules/uspto-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/uspto-vocabulary.yml
- group: company
  title: ''
  type: Blog
  url: https://www.uspto.gov/rss.xml
created: '2025-01-01'
description: The United States Patent and Trademark Office (USPTO) is the federal agency responsible for granting U.S. patents and registering trademarks. USPTO provides a suite of developer APIs through the Open Data Portal (developer.uspto.gov) and data.uspto.gov for programmatic access to patent applications, granted patents, PTAB trial proceedings, trademark status, patent assignments, office actions, and citation data. All USPTO APIs are open government data and return JSON and XML responses. An ODP API key is required for most endpoints.
examples:
- key_count: 2
  name: Uspto Gettrademarkstatus Example
  slug: uspto-getTrademarkStatus-example
- key_count: 2
  name: Uspto Searchptabtrials Example
  slug: uspto-searchPTABTrials-example
- key_count: 2
  name: Uspto Searchpatentapplications Example
  slug: uspto-searchPatentApplications-example
- key_count: 2
  name: Uspto Searchpatentassignments Example
  slug: uspto-searchPatentAssignments-example
finops:
- name: Uspto Finops
  service_category: Government Open Data
  slug: uspto-finops
image: https://www.uspto.gov/sites/default/files/USPTO_Logo.png
json_schemas:
- name: Assignee
  property_count: 5
  slug: uspto-assignee
- name: Assignment
  property_count: 7
  slug: uspto-assignment
- name: AssignmentSearchResponse
  property_count: 2
  slug: uspto-assignmentsearchresponse
- name: Classification
  property_count: 3
  slug: uspto-classification
- name: GrantedPatent
  property_count: 0
  slug: uspto-grantedpatent
- name: Inventor
  property_count: 5
  slug: uspto-inventor
- name: USPTO Patent
  property_count: 16
  slug: uspto-patent
- name: PatentApplication
  property_count: 12
  slug: uspto-patentapplication
- name: PatentSearchResponse
  property_count: 4
  slug: uspto-patentsearchresponse
- name: PatentSummary
  property_count: 10
  slug: uspto-patentsummary
- name: ProsecutionEvent
  property_count: 4
  slug: uspto-prosecutionevent
- name: PTABDecisionSearchResponse
  property_count: 2
  slug: uspto-ptabdecisionsearchresponse
- name: PTABTrial
  property_count: 0
  slug: uspto-ptabtrial
- name: PTABTrialSearchResponse
  property_count: 3
  slug: uspto-ptabtrialsearchresponse
- name: PTABTrialSummary
  property_count: 9
  slug: uspto-ptabtrialsummary
- name: TrademarkStatus
  property_count: 13
  slug: uspto-trademarkstatus
json_structures:
- name: Uspto Patent Structure
  property_count: 0
  slug: uspto-patent-structure
- name: Uspto Structure
  property_count: 0
  slug: uspto-structure
jsonld:
- class_count: 24
  name: Uspto Context
  property_count: 7
  slug: uspto-context
layout: provider
modified: '2026-05-19'
name: USPTO
nav: Providers
network: true
overview: 'USPTO publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Assignments API, Patents API, PTAB API, and 1 more. Tagged areas include Government, Intellectual Property, Open Data, Patents, and Regulatory.


  The USPTO catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  USPTO''s developer surface includes authentication, developer portal, documentation, getting-started guide, engineering blog, and 13 more developer resources.'
plans:
- name: Uspto Plans Pricing
  plan_count: 1
  slug: uspto-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 1
  name: Uspto Rate Limits
  slug: uspto-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: USPTO API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: uspto-jsonschema-spectral-rules
- effective_rule_count: 61
  extends:
  - spectral:oas
  name: USPTO API Rules
  rule_count: 20
  severity_counts:
    error: 8
    hint: 0
    info: 3
    warn: 9
  slug: uspto-rules
score:
  band: developing
  composite: 42.9
  coverage:
    artifact_dirs: 17
    catalog_gap: 52.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 28.8
    contract_quality: 67.4
    developer_ergonomics: 41.7
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 7.9
  previous_composite: 42.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 38.9
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/uspto/refs/heads/main/screenshots/uspto-2026-08-17T083343.png
security:
- kind: authentication
  name: Uspto Authentication
  slug: uspto-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Uspto Domain Security
  slug: uspto-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: uspto
tags:
- Government
- Intellectual Property
- Open Data
- Patents
- Regulatory
- Trademarks
- USPTO
website: https://www.uspto.gov/
---
