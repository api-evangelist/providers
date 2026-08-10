---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 53.8
  scored_at: '2026-08-10'
api_count: 7
apis:
- description: Aidbox's HL7 FHIR REST API for creating, reading, updating, deleting, and searching clinical and administrative resources. Supports FHIR R4 (4.0.1), R5, and R6, with standard FHIR interactions, transa
  name: Aidbox FHIR API
  slug: aidbox-fhir-api
- description: Aidbox-native REST and search API offering CRUD over resources plus SQL-based search implementations for performance optimization and complex custom queries beyond standard FHIR search parameters.
  name: Aidbox REST & Search API
  slug: aidbox-rest-search-api
- description: SQL-on-FHIR support that lets clients run SQL queries directly against FHIR data, treating FHIR resources as relational tables for analytics and reporting.
  name: Aidbox SQL-on-FHIR API
  slug: aidbox-sql-on-fhir-api
- description: A GraphQL API over FHIR data that lets clients request exactly the data they need across related resources in a single call.
  name: Aidbox GraphQL API
  slug: aidbox-graphql-api
- description: FHIR Bulk Data API for large-scale export and import of FHIR resources, including $export, FHIR import/load, and dump utilities for moving datasets in and out of Aidbox.
  name: Aidbox Bulk Data API
  slug: aidbox-bulk-data-api
- description: FHIR topic-based Subscriptions that deliver notifications on changes to FHIR resources through multiple channels for event-driven healthcare integrations.
  name: Aidbox Topic-Based Subscriptions API
  slug: aidbox-subscriptions-api
- description: Terminology services for working with FHIR CodeSystems, ValueSets, and ConceptMaps, including validation and lookup against clinical terminologies.
  name: Aidbox Terminology API
  slug: aidbox-terminology-api
artifact_total: 12
asyncapis:
- description: ''
  name: Aidbox Subscriptions Webhooks
  slug: aidbox-subscriptions-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aidbox-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.health-samurai.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.health-samurai.io/docs/aidbox
- group: docs
  title: ''
  type: Documentation
  url: https://www.health-samurai.io/docs/aidbox
- group: docs
  title: ''
  type: APIReference
  url: https://www.health-samurai.io/docs/aidbox/api-1/api
- group: start
  title: ''
  type: GettingStarted
  url: https://www.health-samurai.io/docs/aidbox/getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://www.health-samurai.io/docs/aidbox/getting-started/editions-and-pricing
- group: company
  title: ''
  type: Blog
  url: https://www.health-samurai.io/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.aidbox.app/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Aidbox
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/health-samurai/
- group: auth
  title: ''
  type: Security
  url: https://www.health-samurai.io/docs/aidbox/modules/security-and-access-control
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.health-samurai.io/legal/privacy-policy
- group: other
  title: ''
  type: SMARTConfiguration
  url: fhir/aidbox-smart-configuration.json
- group: other
  title: ''
  type: OpenIDConfiguration
  url: fhir/aidbox-openid-configuration.json
- group: other
  title: ''
  type: CapabilityStatement
  url: fhir/aidbox-capabilitystatement.json
- group: operate
  title: ''
  type: Support
  url: https://www.health-samurai.io/contacts
- group: start
  title: ''
  type: SignUp
  url: https://aidbox.app/
- group: auth
  title: ''
  type: Compliance
  url: https://www.health-samurai.io/fhir-server
- group: auth
  title: ''
  type: Authentication
  url: authentication/aidbox-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/aidbox-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/aidbox-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/aidbox-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/aidbox-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/aidbox-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/aidbox-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://www.health-samurai.io/docs/aidbox/overview/release-notes
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/aidbox-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/aidbox-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/aidbox-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/aidbox-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/aidbox-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/aidbox-subscriptions-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/aidbox-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/aidbox-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/aidbox-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aidbox-llms.txt
created: '2026-07-24'
description: Aidbox is a production-ready FHIR platform and clinical data backend from Health Samurai, used by digital health startups, providers, payers, and life-sciences teams to build interoperable healthcare products in the United States and globally. Built on PostgreSQL, Aidbox exposes a full HL7 FHIR REST API (R4, R5, and R6) plus Aidbox-native SQL search, SQL-on-FHIR, a GraphQL API, Bulk Data export/import, topic-based Subscriptions, and terminology services. It is self-hosted or Aidbox-hosted software rather than a single public multi-tenant endpoint, so each deployment serves its own FHIR base and its own CapabilityStatement; a public sandbox (sandbox.aidbox.app) exposes a live FHIR R4 CapabilityStatement and a SMART-on-FHIR / OpenID .well-known configuration. Authentication is OAuth 2.0 with SMART-on-FHIR support (patient/user/system scopes, EHR and standalone launch, client-confidential and client-public flows). Aidbox aligns with US interoperability needs (US Core, SMART App
  Launch, Bulk Data) and is HIPAA-oriented, HITRUST and SOC 2 focused. This profile catalogs the documented, real API surface only.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: aidbox-mcp.yml
  slug: aidbox-mcpyml
modified: '2026-07-24'
name: Aidbox
nav: Providers
network: true
overview: 'Aidbox publishes 7 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, United States, FHIR, HL7, and Interoperability.


  The Aidbox catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Aidbox''s developer surface includes documentation, API reference, getting-started guide, pricing, engineering blog, support, signup flow, and 31 more developer resources.'
random_paper: 51
scopes:
- name: Aidbox Scopes
  scope_count: 12
  slug: aidbox-scopes
  summary_line: 12 scopes · authorizationCode/clientCredentials/implicit/password
score:
  band: strong
  composite: 58.5
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 55.0
    developer_ergonomics: 75.5
    discoverability: 92.6
    governance: 12.5
    operational_transparency: 63.2
  previous_composite: 58.5
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 71.3
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aidbox/refs/heads/main/screenshots/aidbox-2026-07-25T195346.png
security:
- kind: authentication
  name: Aidbox Authentication
  slug: aidbox-authentication
  summary_line: oauth2/openIdConnect/http · 3 schemes
- kind: domain-security
  name: Aidbox Domain Security
  slug: aidbox-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: aidbox
tags:
- Healthcare
- United States
- FHIR
- HL7
- Interoperability
- SMART on FHIR
- EHR
- Health Data
- FHIR Server
- Bulk Data
- Terminology
- Digital Health
website: https://www.health-samurai.io/
---
