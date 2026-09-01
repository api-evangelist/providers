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
- acting_count: 13
  human_in_the_loop: 2
  name: Software Ag Agentic Access
  operation_count: 19
  slug: software-ag-agentic-access
  summary_line: 19 operations · 13 acting · 2 human-in-the-loop
api_count: 1
apis:
- description: The webMethods Developer Portal provides a marketplace for publishing and discovering REST, SOAP, and OData APIs for third-party developers and partners. It enables developer onboarding, API subscript
  name: webMethods Developer Portal
  slug: webmethods-developer-portal
- description: The webMethods Integration Server is a comprehensive integration platform that enables connectivity between enterprise applications, databases, legacy systems, and cloud services. It provides flow ser
  name: webMethods Integration Server
  slug: webmethods-integration-server
- description: API lifecycle management operations
  name: Software AG APIs API
  slug: software-ag-apis-api
- description: Application and consumer management
  name: Software AG Applications API
  slug: software-ag-applications-api
- description: Policy and scope management
  name: Software AG Policies API
  slug: software-ag-policies-api
- description: API portal publishing operations
  name: Software AG Publishing API
  slug: software-ag-publishing-api
artifact_total: 25
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: webMethods API Gateway Service Management APIs API
  slug: open-software-ag-apis-api
- collection_type: open
  name: webMethods API Gateway Service Management APIs Applications API
  slug: open-software-ag-applications-api
- collection_type: open
  name: webMethods API Gateway Service Management APIs Policies API
  slug: open-software-ag-policies-api
- collection_type: open
  name: webMethods API Gateway Service Management APIs Publishing API
  slug: open-software-ag-publishing-api
- collection_type: open
  name: webMethods API Gateway Service Management API
  slug: open-webmethods-api-gateway
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/SoftwareAG/webmethods-developer-portal/issues
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/ibm/
- group: commercial
  title: ''
  type: License
  url: https://github.com/SoftwareAG/webmethods-developer-portal/blob/main/LICENSE
- group: operate
  title: ''
  type: Support
  url: https://www.softwareag.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.softwareag.com/en/privacy/
- group: start
  title: ''
  type: Signup
  url: https://www.softwareag.com/free-trials/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/software-ag-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/software-ag-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/software-ag-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.softwareag.com/
- group: company
  title: ''
  type: Website
  url: https://www.softwareag.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SoftwareAG
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.softwareag.com/
- group: company
  title: ''
  type: Blog
  url: https://techcommunity.softwareag.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/software-ag
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/SoftwareAG
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/software-ag/refs/heads/main/json-ld/software-ag-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/software-ag/refs/heads/main/vocabulary/software-ag-vocabulary.yml
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/web-methods/
created: '2026-03-16'
description: Software AG provides enterprise integration and API management through webMethods, a platform for connecting applications, processes, and people across hybrid cloud and on-premises environments. The webMethods platform includes API Gateway, Developer Portal, Integration Server, and cloud-native integration services. Software AG was acquired by IBM in 2024.
examples:
- key_count: 4
  name: Webmethods Create Api Example
  slug: webmethods-create-api-example
- key_count: 4
  name: Webmethods List Apis Example
  slug: webmethods-list-apis-example
finops:
- name: Software Ag Finops
  service_category: Enterprise Integration
  slug: software-ag-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/software-ag.png
json_schemas:
- name: webMethods API
  property_count: 12
  slug: webmethods-api
json_structures:
- name: Webmethods Api Structure
  property_count: 0
  slug: webmethods-api-structure
jsonld:
- class_count: 0
  name: Software Ag Context
  property_count: 18
  slug: software-ag-context
layout: provider
modified: '2026-08-21'
name: Software AG
nav: Providers
network: true
overview: 'Software AG publishes 4 APIs on the [APIs.io](https://apis.io/) network, including APIs API, Applications API, Policies API, and 1 more. Tagged areas include API Management, Enterprise Integration, iPaaS, webMethods, and Integration Platform.


  The Software AG catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Software AG''s developer surface includes support, signup flow, authentication, developer portal, documentation, engineering blog, and 13 more developer resources.'
plans:
- name: Software Ag Plans Pricing
  plan_count: 1
  slug: software-ag-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 1
  name: Software Ag Rate Limits
  slug: software-ag-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Software AG API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: software-ag-jsonschema-spectral-rules
- effective_rule_count: 12
  extends: []
  name: Software AG API Rules
  rule_count: 12
  severity_counts:
    error: 4
    hint: 0
    info: 2
    warn: 6
  slug: webmethods-api-gateway-rules
score:
  band: thin
  composite: 34.7
  coverage:
    artifact_dirs: 17
    catalog_gap: 53.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 25.0
    contract_quality: 63.8
    developer_ergonomics: 33.3
    discoverability: 66.7
    governance: 25.0
    operational_transparency: 7.9
  open_source:
    applies: true
    score: 0.0
  previous_composite: 34.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/software-ag/refs/heads/main/screenshots/software-ag-2026-06-20T194136.png
security:
- kind: authentication
  name: Software Ag Authentication
  slug: software-ag-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Software Ag Domain Security
  slug: software-ag-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: software-ag
tags:
- API Management
- Enterprise Integration
- iPaaS
- webMethods
- Integration Platform
- API Gateway
website: https://www.softwareag.com/
---
