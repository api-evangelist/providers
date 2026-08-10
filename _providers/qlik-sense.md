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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 21
  human_in_the_loop: 0
  name: Qlik Sense Agentic Access
  operation_count: 35
  slug: qlik-sense-agentic-access
  summary_line: 35 operations · 21 acting
api_count: 8
apis:
- description: WebSocket-based API for interacting with the Qlik Associative Engine, including data modeling, selections, and visualizations.
  name: Qlik Sense Engine API
  slug: qlik-sense-engine-api
- description: REST API for managing Qlik Sense repository objects including apps, streams, users, and security rules.
  name: Qlik Sense Repository API
  slug: qlik-sense-repository-api
- description: REST API for session management and authentication through the Qlik Sense Proxy Service.
  name: Qlik Sense Proxy API
  slug: qlik-sense-proxy-api
- description: REST API for managing data integration tasks, connections, and data pipelines.
  name: Qlik Data Integration API
  slug: qlik-data-integration-api
- description: JavaScript API for embedding Qlik Sense visualizations and mashups into web applications.
  name: Qlik Embedding API
  slug: qlik-embedding-api
- description: Manage Qlik Sense analytics applications including creating, copying, importing, exporting, publishing, and retrieving app metadata.
  name: Qlik Sense Apps API
  slug: qlik-sense-apps-api
- description: Trigger and manage data reloads for apps to refresh data from connected sources.
  name: Qlik Sense Reloads API
  slug: qlik-sense-reloads-api
- description: Manage spaces, which are logical containers within a tenant that control access for users and groups through role-based assignments.
  name: Qlik Sense Spaces API
  slug: qlik-sense-spaces-api
artifact_total: 44
collections:
- collection_type: postman
  name: Qlik Cloud REST Apps API
  slug: postman-qlik-sense-apps-api
- collection_type: postman
  name: Qlik Cloud REST Apps Reloads API
  slug: postman-qlik-sense-reloads-api
- collection_type: postman
  name: Qlik Cloud REST Apps Spaces API
  slug: postman-qlik-sense-spaces-api
- collection_type: open
  name: Qlik Cloud REST API
  slug: open-qlik-sense-cloud-rest-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/qlik-sense/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/qlik-sense-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/qlik-sense-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/qlik-sense-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/qlik
- group: start
  title: ''
  type: Portal
  url: https://qlik.dev
- group: company
  title: ''
  type: Website
  url: https://www.qlik.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.qlik.com/en-US/sense-developer/
- group: auth
  title: ''
  type: Authentication
  url: https://qlik.dev/authenticate
- group: start
  title: ''
  type: GettingStarted
  url: https://qlik.dev/get-started
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.qlik.com/us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.qlik.com/us/legal/privacy-and-cookie-notice
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/qlik-oss
- group: operate
  title: ''
  type: Support
  url: https://community.qlik.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.qlikcloud.com
- group: company
  title: ''
  type: Blog
  url: https://www.qlik.com/blog
- group: start
  title: ''
  type: Signup
  url: https://www.qlik.com/us/trial/qlik-cloud-analytics
- group: start
  title: ''
  type: Login
  url: https://myqlik.qlik.com
- group: build
  title: ''
  type: SDKs
  url: https://qlik.dev/toolkits/qlik-api
- group: operate
  title: ''
  type: ChangeLog
  url: https://qlik.dev/changelog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.qlik.com/us/pricing/data-integration-products-pricing
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/qlik-oss/qlik-mcp-registry
created: '2024-01-15'
description: APIs for Qlik Sense, a business intelligence and data analytics platform providing engine, repository, cloud, embedding, and data integration capabilities.
finops:
- name: Qlik Sense Finops
  service_category: Analytics
  slug: qlik-sense-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/qlik-sense.png
json_schemas:
- name: Qlik Sense App
  property_count: 23
  slug: qlik-sense-app
- name: AppAttributes
  property_count: 21
  slug: qlik-sense-appattributes
- name: AppCopy
  property_count: 3
  slug: qlik-sense-appcopy
- name: AppCreate
  property_count: 3
  slug: qlik-sense-appcreate
- name: AppDataLineage
  property_count: 2
  slug: qlik-sense-appdatalineage
- name: AppDataMetadata
  property_count: 3
  slug: qlik-sense-appdatametadata
- name: AppPublish
  property_count: 3
  slug: qlik-sense-apppublish
- name: AppScript
  property_count: 4
  slug: qlik-sense-appscript
- name: AppUpdate
  property_count: 2
  slug: qlik-sense-appupdate
- name: ErrorResponse
  property_count: 1
  slug: qlik-sense-errorresponse
- name: JsonPatch
  property_count: 3
  slug: qlik-sense-jsonpatch
- name: Reload
  property_count: 14
  slug: qlik-sense-reload
- name: ReloadCreate
  property_count: 3
  slug: qlik-sense-reloadcreate
- name: ReloadList
  property_count: 2
  slug: qlik-sense-reloadlist
- name: ReloadLog
  property_count: 4
  slug: qlik-sense-reloadlog
- name: Space
  property_count: 11
  slug: qlik-sense-space
- name: SpaceAssignment
  property_count: 9
  slug: qlik-sense-spaceassignment
- name: SpaceAssignmentCreate
  property_count: 3
  slug: qlik-sense-spaceassignmentcreate
- name: SpaceAssignmentList
  property_count: 1
  slug: qlik-sense-spaceassignmentlist
- name: SpaceCreate
  property_count: 3
  slug: qlik-sense-spacecreate
- name: SpaceList
  property_count: 2
  slug: qlik-sense-spacelist
- name: SpaceUpdate
  property_count: 3
  slug: qlik-sense-spaceupdate
json_structures:
- name: Qlik Sense Structure
  property_count: 0
  slug: qlik-sense-structure
jsonld:
- class_count: 0
  name: Qlik Sense Context
  property_count: 6
  slug: qlik-sense-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Qlik Sense
nav: Providers
network: true
overview: 'Qlik Sense publishes 3 APIs on the [APIs.io](https://apis.io/) network: Apps API, Reloads API, and Spaces API. Tagged areas include Analytics, Business Intelligence, Cloud, Data Integration, and Visualization.


  The Qlik Sense catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Qlik Sense''s developer surface includes authentication, developer portal, documentation, getting-started guide, support, engineering blog, signup flow, and 15 more developer resources.'
plans:
- name: Qlik Sense Plans Pricing
  plan_count: 1
  slug: qlik-sense-plans-pricing
random_paper: 92
rate_limits:
- limit_count: 1
  name: Qlik Sense Rate Limits
  slug: qlik-sense-rate-limits
rules:
- name: Qlik Sense API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: qlik-sense-jsonschema-spectral-rules
score:
  band: strong
  composite: 65.1
  delta: 0.0
  facets:
    commercial_clarity: 73.7
    contract_quality: 69.0
    developer_ergonomics: 65.2
    discoverability: 55.6
    governance: 58.3
    operational_transparency: 57.9
  previous_composite: 65.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/qlik-sense/refs/heads/main/screenshots/qlik-sense-2026-06-20T192340.png
security:
- kind: authentication
  name: Qlik Sense Authentication
  slug: qlik-sense-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Qlik Sense Domain Security
  slug: qlik-sense-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: qlik-sense
tags:
- Analytics
- Business Intelligence
- Cloud
- Data Integration
- Visualization
website: https://www.qlik.com
---
