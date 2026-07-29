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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Cdisc Agentic Access
  operation_count: 13
  slug: cdisc-agentic-access
  summary_line: 13 operations
api_count: 7
apis:
- description: CDISC CORE (Checks and Rules Engine) is an open-source rules engine for validating clinical data against CDISC conformance rules. It enables automated validation of SDTM, ADaM, and other study data ar
  name: CDISC CORE (Checks and Rules Engine) API
  slug: cdisc-core-api
- description: Analysis Data Model standards
  name: cdisc ADaM API
  slug: cdisc-adam-api
- description: CDISC Biomedical Concepts (COSMOS)
  name: cdisc Biomedical Concepts API
  slug: cdisc-biomedical-concepts-api
- description: Clinical Data Acquisition Standards Harmonization
  name: cdisc CDASH API
  slug: cdisc-cdash-api
- description: CDISC standards product catalog
  name: cdisc Products API
  slug: cdisc-products-api
- description: Study Data Tabulation Model standards
  name: cdisc SDTM API
  slug: cdisc-sdtm-api
- description: CDISC controlled terminology
  name: cdisc Terminology API
  slug: cdisc-terminology-api
artifact_total: 17
collections:
- collection_type: open
  name: CDISC Library API
  slug: open-cdisc-library
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cdisc-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cdisc-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cdisc-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cdisc-org
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cdisc
- group: company
  title: ''
  type: Website
  url: https://www.cdisc.org/
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/cdisc/refs/heads/main/openapi/cdisc-library-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/cdisc/refs/heads/main/json-schema/cdisc-dataset-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/cdisc/refs/heads/main/json-ld/cdisc-context.jsonld
- group: start
  title: ''
  type: Portal
  url: https://www.cdisc.org/cdisc-library
- group: start
  title: ''
  type: GettingStarted
  url: https://www.cdisc.org/cdisc-library/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://www.cdisc.org/cdisc-library/api-documentation
- group: auth
  title: ''
  type: Authentication
  url: https://api.developer.library.cdisc.org/
- group: operate
  title: ''
  type: Support
  url: https://jira.cdisc.org/servicedesk/customer/portal/2
- group: operate
  title: ''
  type: ChangeLog
  url: https://wiki.cdisc.org/display/LIBSUPRT/Release+Notes
- group: start
  title: ''
  type: Signup
  url: https://www.cdisc.org/cdisc-library/api-account-request
- group: company
  title: ''
  type: Blog
  url: https://www.cdisc.org/news/whats-new
description: CDISC Library uses linked data and a REST API to deliver CDISC standards metadata to software applications that automate standards-based processes. CDISC Library provides access to new relationships between standards as well as a substantially increased number of versioned CDISC standards and controlled terminology packages.
finops:
- name: Cdisc Finops
  service_category: API
  slug: cdisc-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cdisc.png
json_schemas:
- name: CDISC Dataset (Domain)
  property_count: 9
  slug: cdisc-dataset
jsonld:
- class_count: 6
  name: Cdisc Context
  property_count: 16
  slug: cdisc-context
layout: provider
modified: '2026-05-19'
name: cdisc
nav: Providers
network: true
overview: 'cdisc publishes 6 APIs on the [APIs.io](https://apis.io/) network, including ADaM API, Biomedical Concepts API, CDASH API, and 3 more.


  The cdisc catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  cdisc''s developer surface includes authentication, developer portal, getting-started guide, documentation, support, changelog, signup flow, and 10 more developer resources.'
plans:
- name: Cdisc Plans Pricing
  plan_count: 3
  slug: cdisc-plans-pricing
random_paper: 44
rate_limits:
- limit_count: 5
  name: Cdisc Rate Limits
  slug: cdisc-rate-limits
rules:
- name: cdisc API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: cdisc-jsonschema-spectral-rules
score:
  band: developing
  composite: 54.7
  delta: -4.4
  facets:
    commercial_clarity: 39.5
    contract_quality: 69.5
    developer_ergonomics: 45.7
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 59.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cdisc/refs/heads/main/screenshots/cdisc-2026-06-20T174105.png
security:
- kind: authentication
  name: Cdisc Authentication
  slug: cdisc-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Cdisc Domain Security
  slug: cdisc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cdisc
website: https://www.cdisc.org/
---
