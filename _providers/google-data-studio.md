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
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
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
  score: 30.6
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 3
  human_in_the_loop: 1
  name: Google Data Studio Agentic Access
  operation_count: 7
  slug: google-data-studio-agentic-access
  summary_line: 7 operations · 3 acting · 1 human-in-the-loop
api_count: 2
apis:
- description: Community Connectors enable direct connections from Looker Studio to any internet-accessible data source using Google Apps Script. Developers implement getAuthType, getConfig, getSchema, and getData f
  name: Looker Studio Community Connectors
  slug: looker-studio-community-connectors
- description: 'Community Visualizations allow developers to build and share custom JavaScript visualizations in Looker Studio using the dscc helper library, extending the platform with custom chart types and visual '
  name: Looker Studio Community Visualizations
  slug: looker-studio-community-visualizations
- baseURL: https://datastudio.googleapis.com
  baseurl_source: declared
  description: Operations for searching and listing Looker Studio assets
  name: Google Data Studio Assets API
  slug: google-data-studio-assets-api
- baseURL: https://datastudio.googleapis.com
  baseurl_source: declared
  description: Operations for embedding pre-configured Looker Studio reports
  name: Google Data Studio Embedding API
  slug: google-data-studio-embedding-api
- baseURL: https://datastudio.googleapis.com
  baseurl_source: declared
  description: Operations for managing access controls on Looker Studio assets
  name: Google Data Studio Permissions API
  slug: google-data-studio-permissions-api
- baseURL: https://datastudio.googleapis.com
  baseurl_source: declared
  description: Operations for creating and configuring pre-built Looker Studio reports
  name: Google Data Studio Reports API
  slug: google-data-studio-reports-api
artifact_total: 32
collections:
- collection_type: postman
  name: Google Data Studio Assets API
  slug: postman-google-data-studio-assets-api
- collection_type: postman
  name: Google Data Studio Assets Embedding API
  slug: postman-google-data-studio-embedding-api
- collection_type: postman
  name: Google Data Studio Assets Permissions API
  slug: postman-google-data-studio-permissions-api
- collection_type: postman
  name: Google Data Studio Assets Reports API
  slug: postman-google-data-studio-reports-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Data Studio API
  slug: open-google-data-studio-api
- collection_type: open
  name: Google Data Studio Assets API
  slug: open-google-data-studio-assets-api
- collection_type: open
  name: Google Data Studio Assets Embedding API
  slug: open-google-data-studio-embedding-api
- collection_type: open
  name: Google Data Studio Looker Studio Linking API
  slug: open-google-data-studio-linking-api
- collection_type: open
  name: Google Data Studio Assets Permissions API
  slug: open-google-data-studio-permissions-api
- collection_type: open
  name: Google Data Studio Assets Reports API
  slug: open-google-data-studio-reports-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-data-studio/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-data-studio-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-data-studio-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-data-studio-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-data-studio-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-data-studio-scopes.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/google-data-studio-api-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/google-data-studio-linking-api-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/google-data-studio-asset-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/google-data-studio-permissions-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/google-data-studio-connector-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/google-data-studio-report-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/google-data-studio-datasource-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/google-data-studio-context.jsonld
- group: start
  title: ''
  type: Portal
  url: https://lookerstudio.google.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cloud.google.com/looker/docs/studio
- group: start
  title: ''
  type: GettingStarted
  url: https://support.google.com/looker-studio/answer/6283323
- group: auth
  title: ''
  type: Authentication
  url: https://developers.google.com/looker-studio/integrate/api
- group: company
  title: ''
  type: Blog
  url: https://cloud.google.com/blog/products/data-analytics
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.google.com/
- group: operate
  title: ''
  type: Support
  url: https://support.google.com/looker-studio
- group: commercial
  title: ''
  type: TermsOfService
  url: https://support.google.com/looker-studio/answer/7019158
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/looker-open-source
- group: operate
  title: ''
  type: Community
  url: https://www.googlecloudcommunity.com/gc/Looker-Studio/bd-p/looker-studio
- group: other
  title: ''
  type: Gallery
  url: https://lookerstudio.google.com/gallery
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.cloud.google.com/looker-studio/docs/release-notes
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/looker/pricing
- group: company
  title: ''
  type: Website
  url: https://cloud.google.com/looker-studio
- group: start
  title: ''
  type: Login
  url: https://lookerstudio.google.com/?requirelogin=1
- group: start
  title: ''
  type: Signup
  url: https://lookerstudio.google.com
created: '2024-01-01'
description: Google Data Studio, now rebranded as Looker Studio, is a free data visualization and business intelligence tool from Google that transforms data into customizable, shareable dashboards and reports. It connects to a wide range of data sources and supports community connectors and visualizations for extensibility.
finops:
- name: Google Data Studio Finops
  service_category: Business Intelligence / Analytics
  slug: google-data-studio-finops
image: https://www.gstatic.com/analytics-suite/header/suite/v2/ic_data_studio.svg
json_schemas:
- name: Looker Studio Asset
  property_count: 11
  slug: google-data-studio-asset
- name: Looker Studio Community Connector
  property_count: 4
  slug: google-data-studio-connector
- name: Looker Studio Data Source
  property_count: 10
  slug: google-data-studio-datasource
- name: Looker Studio Permissions
  property_count: 2
  slug: google-data-studio-permissions
- name: Looker Studio Report
  property_count: 11
  slug: google-data-studio-report
jsonld:
- class_count: 0
  name: Google Data Studio Context
  property_count: 10
  slug: google-data-studio-context
layout: provider
modified: '2026-05-19'
name: Google Data Studio
nav: Providers
network: true
overview: 'Google Data Studio publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Assets API, Embedding API, Permissions API, and 1 more. Tagged areas include Analytics, Business Intelligence, Dashboards, Data, and Reporting.


  The Google Data Studio catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Data Studio''s developer surface includes authentication, developer portal, documentation, getting-started guide, engineering blog, support, changelog, and 24 more developer resources.'
plans:
- name: Google Data Studio Plans Pricing
  plan_count: 6
  slug: google-data-studio-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 13
  name: Google Data Studio Rate Limits
  slug: google-data-studio-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Google Data Studio API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: google-data-studio-jsonschema-spectral-rules
scopes:
- name: Google Data Studio Scopes
  scope_count: 3
  slug: google-data-studio-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: developing
  composite: 48.6
  coverage:
    artifact_dirs: 15
    catalog_gap: 62.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 9.8
    contract_quality: 59.0
    developer_ergonomics: 59.5
    discoverability: 66.7
    governance: 9.8
    operational_transparency: 42.1
  previous_composite: 48.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-data-studio/refs/heads/main/screenshots/google-data-studio-2026-06-20T182153.png
security:
- kind: authentication
  name: Google Data Studio Authentication
  slug: google-data-studio-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Data Studio Domain Security
  slug: google-data-studio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Data Studio Vulnerability Disclosure
  slug: google-data-studio-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-data-studio
tags:
- Analytics
- Business Intelligence
- Dashboards
- Data
- Reporting
- Visualization
website: https://cloud.google.com/looker-studio
---
