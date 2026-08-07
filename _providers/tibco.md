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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.0
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 38
  human_in_the_loop: 1
  name: Tibco Agentic Access
  operation_count: 85
  slug: tibco-agentic-access
  summary_line: 85 operations · 38 acting · 1 human-in-the-loop
api_count: 26
apis:
- description: Enterprise messaging API supporting EMS (Enterprise Message Service) and FTL (Fast Transport Layer).
  name: TIBCO Messaging API
  slug: tibco-messaging-api
- description: Manage inference agents
  name: TIBCO Agents API
  slug: tibco-agents-api
- description: Manage Spotfire analysis files
  name: TIBCO Analyses API
  slug: tibco-analyses-api
- description: Manage developer applications
  name: TIBCO Applications API
  slug: tibco-applications-api
- description: Manage integration applications
  name: TIBCO Apps API
  slug: tibco-apps-api
- description: Manage event channels and destinations
  name: TIBCO Channels API
  slug: tibco-channels-api
- description: Manage connector connections
  name: TIBCO Connections API
  slug: tibco-connections-api
- description: Manage data source connections
  name: TIBCO Data Sources API
  slug: tibco-data-sources-api
- description: Manage decision tables for rule evaluation
  name: TIBCO Decision Tables API
  slug: tibco-decision-tables-api
- description: Deploy and manage running app instances
  name: TIBCO Deployments API
  slug: tibco-deployments-api
- description: Manage API endpoints within services
  name: TIBCO Endpoints API
  slug: tibco-endpoints-api
- description: Manage deployment environments
  name: TIBCO Environments API
  slug: tibco-environments-api
- description: Submit and query complex events
  name: TIBCO Events API
  slug: tibco-events-api
- description: Manage Flogo flows and activities
  name: TIBCO Flows API
  slug: tibco-flows-api
- description: Manage user groups
  name: TIBCO Groups API
  slug: tibco-groups-api
- description: Manage Spotfire library items and folders
  name: TIBCO Library API
  slug: tibco-library-api
- description: Manage developer portal members
  name: TIBCO Members API
  slug: tibco-members-api
- description: Manage Spotfire Server nodes and services
  name: TIBCO Nodes API
  slug: tibco-nodes-api
- description: Manage API packages for bundling services
  name: TIBCO Packages API
  slug: tibco-packages-api
- description: Manage subscription plans within packages
  name: TIBCO Plans API
  slug: tibco-plans-api
- description: API usage reporting and analytics
  name: TIBCO Reports API
  slug: tibco-reports-api
- description: The Rest API from TIBCO — 2 operation(s) for rest.
  name: TIBCO Rest API
  slug: tibco-rest-api
- description: Manage business rules and rule sets
  name: TIBCO Rules API
  slug: tibco-rules-api
- description: Manage scheduled analysis updates
  name: TIBCO Scheduled Updates API
  slug: tibco-scheduled-updates-api
- description: Manage metric scorecards and dashboards
  name: TIBCO Scorecards API
  slug: tibco-scorecards-api
- description: Manage Spotfire users
  name: TIBCO Users API
  slug: tibco-users-api
artifact_total: 48
asyncapis:
- description: Enterprise messaging API supporting TIBCO Enterprise Message Service (EMS) and FTL (TIBCO FTL) for reliable, high-performance messaging. Supports JMS-compatible publish-subscribe and point-to-point me
  name: TIBCO Messaging API
  slug: tibco-messaging-asyncapi
collections:
- collection_type: open
  name: TIBCO BusinessEvents API
  slug: open-tibco-businessevents
- collection_type: open
  name: TIBCO Cloud Integration API
  slug: open-tibco-cloud-integration
- collection_type: open
  name: TIBCO Mashery API Management
  slug: open-tibco-mashery
- collection_type: open
  name: TIBCO Spotfire Analytics API
  slug: open-tibco-spotfire
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tibco-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tibco-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tibco-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/tibco-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.tibco.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tibco.com
- group: operate
  title: ''
  type: Support
  url: https://support.tibco.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tibco.com
- group: company
  title: ''
  type: Blog
  url: https://www.tibco.com/blog
- group: build
  title: ''
  type: GitHub
  url: https://github.com/tibco
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tibco
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/tibco
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tibco.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tibco.com/legal/privacy
- group: design
  title: ''
  type: JSONLD
  url: json-ld/tibco-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/tibco-integration-app-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/tibco-api-service-schema.json
- group: design
  title: ''
  type: Spectral
  url: rules/tibco-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/tibco-vocabulary.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.tibco.com/llms.txt
created: '2024'
description: APIs and services provided by TIBCO Software Inc., a global leader in integration, API management, and analytics software.
examples:
- key_count: 2
  name: Tibco Cloud Integration List Apps Example
  slug: tibco-cloud-integration-list-apps-example
- key_count: 2
  name: Tibco Mashery List Api Services Example
  slug: tibco-mashery-list-api-services-example
- key_count: 2
  name: Tibco Spotfire List Library Items Example
  slug: tibco-spotfire-list-library-items-example
finops:
- name: Tibco Finops
  service_category: Integration & Analytics
  slug: tibco-finops
image: https://www.tibco.com/sites/tibco/files/media_entity/2021-04/TIBCO-logo.svg
json_schemas:
- name: TIBCO Mashery API Service
  property_count: 10
  slug: tibco-api-service
- name: TIBCO Cloud Integration App
  property_count: 11
  slug: tibco-integration-app
json_structures:
- name: Tibco Integration App Structure
  property_count: 0
  slug: tibco-integration-app-structure
jsonld:
- class_count: 0
  name: Tibco Context
  property_count: 13
  slug: tibco-context
layout: provider
modified: '2026-05-19'
name: TIBCO
nav: Providers
network: true
overview: 'TIBCO publishes 26 APIs on the [APIs.io](https://apis.io/) network, including Messaging API, Agents API, Analyses API, and 23 more. Tagged areas include Analytics, API Management, Cloud, Enterprise Software, and Integration.


  The TIBCO catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  TIBCO''s developer surface includes authentication, developer portal, documentation, support, engineering blog, GitHub presence, and 14 more developer resources.'
plans:
- name: Tibco Plans Pricing
  plan_count: 1
  slug: tibco-plans-pricing
random_paper: 77
rate_limits:
- limit_count: 1
  name: Tibco Rate Limits
  slug: tibco-rate-limits
rules:
- name: TIBCO API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 7
  slug: tibco-asyncapi-spectral-rules
- name: TIBCO API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: tibco-jsonschema-spectral-rules
- name: TIBCO API Rules
  rule_count: 13
  severity_counts:
    error: 4
    hint: 0
    info: 4
    warn: 5
  slug: tibco-rules
scopes:
- name: Tibco Scopes
  scope_count: 0
  slug: tibco-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 56.6
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 78.4
    developer_ergonomics: 34.8
    discoverability: 72.2
    governance: 58.3
    operational_transparency: 42.1
  previous_composite: 56.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 25
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 58.3
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tibco/refs/heads/main/screenshots/tibco-2026-06-20T195332.png
security:
- kind: authentication
  name: Tibco Authentication
  slug: tibco-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Tibco Domain Security
  slug: tibco-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tibco
tags:
- Analytics
- API Management
- Cloud
- Enterprise Software
- Integration
- Messaging
- Real-Time Data
website: https://developer.tibco.com
---
