---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
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
- acting_count: 8
  human_in_the_loop: 0
  name: Tray Io Agentic Access
  operation_count: 16
  slug: tray-io-agentic-access
  summary_line: 16 operations · 8 acting
api_count: 7
apis:
- description: The Tray.io Embedded API provides GraphQL-based APIs for embedding Tray's automation capabilities into your own products, enabling end users to configure and manage integrations directly.
  name: Tray.io Embedded API
  slug: tray-embedded-api
- description: Create, retrieve, and delete third-party service authentications required by connectors to access external services.
  name: Tray.io Authentications API
  slug: tray-io-authentications-api
- description: List available connectors and their operations, and call connector operations to interact with third-party services programmatically.
  name: Tray.io Connectors API
  slug: tray-io-connectors-api
- description: Manage projects and solutions for environment promotion, including creating, exporting, and importing project versions.
  name: Tray.io Projects API
  slug: tray-io-projects-api
- description: List available triggers and manage trigger subscriptions to receive real-time data from third-party services.
  name: Tray.io Triggers API
  slug: tray-io-triggers-api
- description: Manage users and roles within your Tray.io organization.
  name: Tray.io Users API
  slug: tray-io-users-api
- description: Manage workspaces and workspace users. Workspaces divide an organization into sub-categories such as departments or dev/prod environments.
  name: Tray.io Workspaces API
  slug: tray-io-workspaces-api
artifact_total: 51
collections:
- collection_type: open
  name: Tray.io Platform API
  slug: open-tray-io-platform-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tray-io-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/tray-io-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tray-io-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tray-io-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/trayio
- group: company
  title: ''
  type: Website
  url: https://tray.ai
- group: docs
  title: ''
  type: Documentation
  url: https://tray.ai/documentation
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.tray.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://tray.ai/pricing
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tray-io
- group: company
  title: ''
  type: X (Twitter)
  url: https://x.com/tray
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/tray-io-vocabulary.yml
- group: company
  title: ''
  type: Blog
  url: https://tray.ai/blog
created: '2026-03-26'
description: Tray.io (now also known as Tray.ai) is an AI-ready integration platform as a service (iPaaS) that enables businesses to integrate and automate workflows across cloud applications using a visual editor, pre-built connectors, and API-level access. The platform includes Merlin Agent Builder for building AI agents and a Universal Automation Cloud for connecting data and systems.
examples:
- key_count: 2
  name: Tray Io Call Connector Example
  slug: tray-io-call-connector-example
- key_count: 2
  name: Tray Io List Connectors Example
  slug: tray-io-list-connectors-example
features:
- 'Tray Advantage: foundational tier (custom)'
- 'Tray Advantage Plus: expanded services (custom)'
- Per-workspace + task pricing model
- Quarterly billing cycles
- Tasks = automated actions executed
- 650+ pre-built connectors
- Tray Embedded for SaaS vendors
- Merlin AI for workflow generation
- Visual workflow builder + JSONata data mapping
- Webhook triggers + scheduled triggers
- 'API requests: 600 req/min/workspace'
- 'Webhook trigger: 100 req/sec/workflow'
- Concurrent execution scales with tier
- Connector SDK for custom integrations
- SOC 2 Type 2 compliant
- HIPAA + GDPR-ready
finops:
- name: Tray Io Finops
  service_category: iPaaS
  slug: tray-io-finops
graphqls:
- description: The Tray.io Embedded API provides GraphQL-based APIs for embedding Tray's automation capabilities into your own products, enabling end users to configure and manage integrations directly.
  name: Tray.io GraphQL API
  slug: tray-io-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tray-io.png
json_schemas:
- name: Tray.io Authentication
  property_count: 5
  slug: tray-io-authentication
- name: CallConnectorRequest
  property_count: 3
  slug: tray-io-callconnectorrequest
- name: Tray.io Connector
  property_count: 5
  slug: tray-io-connector
- name: ConnectorVersion
  property_count: 4
  slug: tray-io-connectorversion
- name: CreateAuthenticationRequest
  property_count: 4
  slug: tray-io-createauthenticationrequest
- name: CreateSubscriptionRequest
  property_count: 5
  slug: tray-io-createsubscriptionrequest
- name: InviteUserRequest
  property_count: 3
  slug: tray-io-inviteuserrequest
- name: Operation
  property_count: 5
  slug: tray-io-operation
- name: Subscription
  property_count: 5
  slug: tray-io-subscription
- name: Trigger
  property_count: 5
  slug: tray-io-trigger
- name: User
  property_count: 5
  slug: tray-io-user
- name: Tray.io Workspace
  property_count: 4
  slug: tray-io-workspace
json_structures:
- name: Tray Io Connector Structure
  property_count: 0
  slug: tray-io-connector-structure
- name: Tray Io Structure
  property_count: 0
  slug: tray-io-structure
jsonld:
- class_count: 30
  name: Tray Io Context
  property_count: 0
  slug: tray-io-context
layout: provider
modified: '2026-05-19'
name: Tray.io
nav: Providers
network: true
overview: 'Tray.io publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Authentications API, Connectors API, Projects API, and 3 more. Tagged areas include AI Agents, API Aggregation, Automation, Connectors, and Integration.


  The Tray.io catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Tray.io''s developer surface includes authentication, documentation, pricing, engineering blog, and 9 more developer resources.'
plans:
- name: Tray Io Plans Pricing
  plan_count: 2
  slug: tray-io-plans-pricing
random_paper: 61
rate_limits:
- limit_count: 3
  name: Tray Io Rate Limits
  slug: tray-io-rate-limits
rules:
- name: Tray.io API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: tray-io-jsonschema-spectral-rules
- name: Tray.io API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 5
  slug: tray-io-rules
score:
  band: developing
  composite: 54.4
  delta: -4.1
  facets:
    commercial_clarity: 47.4
    contract_quality: 77.1
    developer_ergonomics: 30.4
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 58.5
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
screenshot: https://raw.githubusercontent.com/api-evangelist/tray-io/refs/heads/main/screenshots/tray-io-2026-06-20T195716.png
security:
- kind: authentication
  name: Tray Io Authentication
  slug: tray-io-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Tray Io Domain Security
  slug: tray-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Tray Io Trust Center
  slug: tray-io-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, HIPAA, FedRAMP, GDPR
slug: tray-io
tags:
- AI Agents
- API Aggregation
- Automation
- Connectors
- Integration
- iPaaS
- Workflow Automation
website: https://tray.ai
---
