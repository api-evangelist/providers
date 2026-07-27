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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Medidata Agentic Access
  operation_count: 9
  slug: medidata-agentic-access
  summary_line: 9 operations · 2 acting
api_count: 6
apis:
- description: Audit trail access for 21 CFR Part 11 compliance
  name: medidata Audit API
  slug: medidata-audit-api
- description: CRF data entry and retrieval
  name: medidata Clinical Data API
  slug: medidata-clinical-data-api
- description: Data query management
  name: medidata Queries API
  slug: medidata-queries-api
- description: Investigator site management
  name: medidata Sites API
  slug: medidata-sites-api
- description: Clinical study management
  name: medidata Studies API
  slug: medidata-studies-api
- description: Trial subject enrollment and management
  name: medidata Subjects API
  slug: medidata-subjects-api
artifact_total: 18
collections:
- collection_type: open
  name: Medidata Rave EDC REST API
  slug: open-medidata-rave
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/medidata-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/medidata-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/medidata-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/medidata-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mdsol
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/medidata-solutions
- group: start
  title: ''
  type: Portal
  url: https://www.medidata.com/
- group: company
  title: ''
  type: Website
  url: https://www.medidata.com/
- group: company
  title: ''
  type: Blog
  url: https://www.medidata.com/en/life-science-resources/medidata-blog/
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/medidata/refs/heads/main/openapi/medidata-rave-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/medidata/refs/heads/main/json-schema/medidata-subject-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/medidata/refs/heads/main/json-ld/medidata-context.jsonld
description: Medidata powers smarter clinical trials with unified data, AI-driven insights, and patient-centric technology to accelerate research.
finops:
- name: Medidata Finops
  service_category: API
  slug: medidata-finops
graphqls:
- description: Medidata provides cloud solutions for clinical trials. The API covers study design, patient data management, EDC data collection, site management, safety events, biomarkers, and clinical analytics for
  name: Medidata Solutions GraphQL API
  slug: medidata-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/medidata.png
json_schemas:
- name: Medidata Rave Clinical Trial Subject
  property_count: 9
  slug: medidata-subject
jsonld:
- class_count: 20
  name: Medidata Context
  property_count: 10
  slug: medidata-context
layout: provider
modified: '2026-05-19'
name: medidata
nav: Providers
network: true
overview: 'medidata publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Audit API, Clinical Data API, Queries API, and 3 more.


  The medidata catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  medidata''s developer surface includes authentication, developer portal, engineering blog, and 9 more developer resources.'
plans:
- name: Medidata Plans Pricing
  plan_count: 3
  slug: medidata-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: Medidata Rate Limits
  slug: medidata-rate-limits
rules:
- name: medidata API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: medidata-jsonschema-spectral-rules
scopes:
- name: Medidata Scopes
  scope_count: 2
  slug: medidata-scopes
  summary_line: 2 scopes · clientCredentials
score:
  band: developing
  composite: 50.8
  delta: 3.8
  facets:
    commercial_clarity: 39.5
    contract_quality: 72.9
    developer_ergonomics: 21.7
    discoverability: 67.5
    governance: 73.7
    operational_transparency: 36.8
  previous_composite: 47.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/medidata/refs/heads/main/screenshots/medidata-2026-06-20T185127.png
security:
- kind: authentication
  name: Medidata Authentication
  slug: medidata-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Medidata Domain Security
  slug: medidata-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: medidata
website: https://www.medidata.com/
---
