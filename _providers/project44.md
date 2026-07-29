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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: true
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
  score: 36.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 4
  human_in_the_loop: 1
  name: Project44 Agentic Access
  operation_count: 9
  slug: project44-agentic-access
  summary_line: 9 operations · 4 acting · 1 human-in-the-loop
api_count: 4
apis:
- description: Shipment tracking and management
  name: project44 Shipments API
  slug: project44-shipments-api
- description: Shipment status updates
  name: project44 Status API
  slug: project44-status-api
- description: Real-time position and event tracking
  name: project44 Tracking API
  slug: project44-tracking-api
- description: Webhook subscription management
  name: project44 Webhooks API
  slug: project44-webhooks-api
artifact_total: 33
asyncapis:
- description: project44 publishes real-time freight visibility events via webhooks. Events include shipment status updates, position changes, ETA revisions, and exception alerts across TL, LTL, ocean, air, and parc
  name: project44 Shipment Events API
  slug: project44-shipment-events-asyncapi
collections:
- collection_type: open
  name: project44 Tracking API
  slug: open-project44-tracking
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/project44-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/project44-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/project44-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/project44-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/project44-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/project44
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/project-44
- group: company
  title: ''
  type: Website
  url: https://www.project44.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.project44.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/project44-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/project44-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/project44-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.project44.com/feed/
created: '2026-05-08'
description: project44 is the supply chain visibility platform that connects, automates, and provides predictive analytics across multimodal shipments worldwide.
finops:
- name: Project44 Finops
  service_category: Logistics
  slug: project44-finops
graphqls:
- description: This conceptual GraphQL schema represents the domain model for the project44 supply chain visibility platform. project44 connects, automates, and provides predictive analytics across multimodal shipme
  name: project44 GraphQL Schema
  slug: project44-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/project44.png
json_schemas:
- name: Error
  property_count: 3
  slug: project44-error
- name: ETAWindow
  property_count: 5
  slug: project44-etawindow
- name: PageInfo
  property_count: 4
  slug: project44-pageinfo
- name: Position
  property_count: 6
  slug: project44-position
- name: project44 Shipment
  property_count: 16
  slug: project44-shipment
- name: ShipmentCreate
  property_count: 4
  slug: project44-shipmentcreate
- name: ShipmentDetail
  property_count: 0
  slug: project44-shipmentdetail
- name: ShipmentException
  property_count: 5
  slug: project44-shipmentexception
- name: ShipmentStop
  property_count: 13
  slug: project44-shipmentstop
- name: ShipmentStopInput
  property_count: 7
  slug: project44-shipmentstopinput
- name: StatusUpdate
  property_count: 10
  slug: project44-statusupdate
- name: TimeWindow
  property_count: 2
  slug: project44-timewindow
- name: WebhookSubscription
  property_count: 5
  slug: project44-webhooksubscription
- name: WebhookSubscriptionCreate
  property_count: 3
  slug: project44-webhooksubscriptioncreate
json_structures:
- name: Project44 Structure
  property_count: 0
  slug: project44-structure
jsonld:
- class_count: 0
  name: Project44 Context
  property_count: 28
  slug: project44-context
layout: provider
modified: '2026-05-19'
name: project44
nav: Providers
network: true
overview: 'project44 publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Shipments API, Status API, Tracking API, and 1 more. Tagged areas include Logistics, Supply Chain Visibility, Tracking, Freight, and Multi-modal.


  The project44 catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  project44''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Project44 Plans Pricing
  plan_count: 1
  slug: project44-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: Project44 Rate Limits
  slug: project44-rate-limits
rules:
- name: project44 API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 5
  slug: project44-asyncapi-spectral-rules
- name: project44 API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: project44-jsonschema-spectral-rules
scopes:
- name: Project44 Scopes
  scope_count: 3
  slug: project44-scopes
  summary_line: 3 scopes · clientCredentials
score:
  band: developing
  composite: 47.6
  delta: -2.8
  facets:
    commercial_clarity: 36.8
    contract_quality: 81.0
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 47.9
    operational_transparency: 26.3
  previous_composite: 50.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/project44/refs/heads/main/screenshots/project44-2026-06-20T192205.png
security:
- kind: authentication
  name: Project44 Authentication
  slug: project44-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Project44 Domain Security
  slug: project44-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Project44 Trust Center
  slug: project44-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, FedRAMP, GDPR
slug: project44
tags:
- Logistics
- Supply Chain Visibility
- Tracking
- Freight
- Multi-modal
website: https://www.project44.com/
---
