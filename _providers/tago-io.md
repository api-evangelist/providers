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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 65
  human_in_the_loop: 0
  name: Tago Io Agentic Access
  operation_count: 107
  slug: tago-io-agentic-access
  summary_line: 107 operations · 65 acting
api_count: 22
apis:
- description: Roles, permissions, and sharing (Profile Token).
  name: TagoIO Access Management API
  slug: tago-io-access-management-api
- description: Account-level operations (Profile Token).
  name: TagoIO Account API
  slug: tago-io-account-api
- description: The Backup API from TagoIO — 3 operation(s) for backup.
  name: TagoIO Backup API
  slug: tago-io-backup-api
- description: The Configuration Param API from TagoIO — 2 operation(s) for configuration param.
  name: TagoIO Configuration Param API
  slug: tago-io-configuration-param-api
- description: Manage dashboards (Profile Token).
  name: TagoIO Dashboards API
  slug: tago-io-dashboards-api
- description: Endpoints that act as a device using a Device Token (device-level permissions).
  name: TagoIO Device Data API
  slug: tago-io-device-data-api
- description: Manage device tokens (Profile Token).
  name: TagoIO Device Tokens API
  slug: tago-io-device-tokens-api
- description: Manage devices using a Profile Token (admin-level).
  name: TagoIO Devices API
  slug: tago-io-devices-api
- description: Manage Dictionary Slugs and Keys for TagoRUN (Profile Token).
  name: TagoIO Dictionary API
  slug: tago-io-dictionary-api
- description: Manage entities (Profile Token).
  name: TagoIO Entity API
  slug: tago-io-entity-api
- description: Operations specific to managing entitie stored data (Profile Token)
  name: TagoIO Entity Data API
  slug: tago-io-entity-data-api
- description: File storage operations (Profile Token).
  name: TagoIO Files API
  slug: tago-io-files-api
- description: Operations specific to immutable device type (Profile Token).
  name: TagoIO Immutable Device API
  slug: tago-io-immutable-device-api
- description: Import/Export Operations for devices (Profile Token).
  name: TagoIO Import/Export API
  slug: tago-io-import-export-api
- description: Endpoints that act as a network using a Network Token (network-level permissions).
  name: TagoIO Network Ingest API
  slug: tago-io-network-ingest-api
- description: Manage notifications (Profile Token).
  name: TagoIO Notifications API
  slug: tago-io-notifications-api
- description: Manage your own profile settings (Profile Token).
  name: TagoIO Profile API
  slug: tago-io-profile-api
- description: Usage statistics and billing (Profile Token).
  name: TagoIO Statistics / Billing API
  slug: tago-io-statistics-billing-api
- description: The Tago RUN API from TagoIO — 2 operation(s) for tago run.
  name: TagoIO Tago RUN API
  slug: tago-io-tago-run-api
- description: The Upload API from TagoIO — 1 operation(s) for upload.
  name: TagoIO Upload API
  slug: tago-io-upload-api
- description: Manage TagoRUN users (Profile Token).
  name: TagoIO Users API
  slug: tago-io-users-api
- description: Manage widgets (Profile Token).
  name: TagoIO Widgets API
  slug: tago-io-widgets-api
artifact_total: 57
collections:
- collection_type: postman
  name: TagoIO Access Management API
  slug: postman-tago-io-access-management-api
- collection_type: postman
  name: TagoIO Access Management Account API
  slug: postman-tago-io-account-api
- collection_type: postman
  name: TagoIO Access Management Backup API
  slug: postman-tago-io-backup-api
- collection_type: postman
  name: TagoIO Access Management Configuration Param API
  slug: postman-tago-io-configuration-param-api
- collection_type: postman
  name: TagoIO Access Management Dashboards API
  slug: postman-tago-io-dashboards-api
- collection_type: postman
  name: TagoIO Access Management Device Data API
  slug: postman-tago-io-device-data-api
- collection_type: postman
  name: TagoIO Access Management Device Tokens API
  slug: postman-tago-io-device-tokens-api
- collection_type: postman
  name: TagoIO Access Management Devices API
  slug: postman-tago-io-devices-api
- collection_type: postman
  name: TagoIO Access Management Dictionary API
  slug: postman-tago-io-dictionary-api
- collection_type: postman
  name: TagoIO Access Management Entity API
  slug: postman-tago-io-entity-api
- collection_type: postman
  name: TagoIO Access Management Entity Data API
  slug: postman-tago-io-entity-data-api
- collection_type: postman
  name: TagoIO Access Management Files API
  slug: postman-tago-io-files-api
- collection_type: postman
  name: TagoIO Access Management Immutable Device API
  slug: postman-tago-io-immutable-device-api
- collection_type: postman
  name: TagoIO Access Management Import/Export API
  slug: postman-tago-io-import-export-api
- collection_type: postman
  name: TagoIO Access Management Network Ingest API
  slug: postman-tago-io-network-ingest-api
- collection_type: postman
  name: TagoIO Access Management Notifications API
  slug: postman-tago-io-notifications-api
- collection_type: postman
  name: TagoIO Access Management Profile API
  slug: postman-tago-io-profile-api
- collection_type: postman
  name: TagoIO Access Management Statistics / Billing API
  slug: postman-tago-io-statistics-billing-api
- collection_type: postman
  name: TagoIO Access Management Tago RUN API
  slug: postman-tago-io-tago-run-api
- collection_type: postman
  name: TagoIO Access Management Upload API
  slug: postman-tago-io-upload-api
- collection_type: postman
  name: TagoIO Access Management Users API
  slug: postman-tago-io-users-api
- collection_type: postman
  name: TagoIO Access Management Widgets API
  slug: postman-tago-io-widgets-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/tagoio/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tago-io-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/tago-io-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tago-io-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tago-io-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://tago.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tago.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tago-io
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tago.io
- group: company
  title: ''
  type: Blog
  url: https://tago.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://tago.io/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tago.io/
- group: operate
  title: ''
  type: ChangeLog
  url: https://changelog.tago.io/
- group: other
  title: ''
  type: X
  url: https://x.com/tagoio
- group: other
  title: ''
  type: Developers
  url: https://tago.io/developers
- group: build
  title: ''
  type: SDKJavaScript
  url: https://github.com/tago-io/sdk-js
- group: build
  title: ''
  type: SDKPython
  url: https://github.com/tago-io/sdk-python
- group: build
  title: ''
  type: CLI
  url: https://github.com/tago-io/tagoio-cli
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/tago-io/refs/heads/main/plans/tago-io-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/tago-io/refs/heads/main/rate-limits/tago-io-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/tago-io/refs/heads/main/finops/tago-io-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/tago-io/refs/heads/main/vocabulary/tago-io-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/tago-io/refs/heads/main/json-ld/tago-io-context.jsonld
created: '2026-06-12'
description: TagoIO is an IoT cloud application development platform that enables businesses to build, deploy, and manage IoT applications with a comprehensive REST API. The platform provides full programmatic control over devices, dashboards, data storage, analysis scripts, alerts, and user management. TagoIO exposes regional REST API endpoints covering device data ingestion, entity management, access control policies, and file storage, all secured with token-based authentication. Plans range from a free tier supporting five devices up to an enterprise-grade TagoDeploy option supporting millions of devices with dedicated cloud instances and customizable rate limits.
examples:
- key_count: 4
  name: Tago Io List Devices Example
  slug: tago-io-list-devices-example
- key_count: 4
  name: Tago Io Send Device Data Example
  slug: tago-io-send-device-data-example
finops:
- name: Tago Io Finops
  service_category: ''
  slug: tago-io-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tago-io.png
json_schemas:
- name: TagoIO Device Data Item
  property_count: 10
  slug: tago-io-device-data-item
- name: TagoIO Device
  property_count: 14
  slug: tago-io-device
jsonld:
- class_count: 34
  name: Tago Io Context
  property_count: 11
  slug: tago-io-context
layout: provider
modified: '2026-06-12'
name: TagoIO
nav: Providers
network: true
overview: 'TagoIO publishes 22 APIs on the [APIs.io](https://apis.io/) network, including Access Management API, Account API, Backup API, and 19 more. Tagged areas include IoT, Internet of Things, Devices, Data Storage, and Dashboards.


  The TagoIO catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  TagoIO''s developer surface includes authentication, documentation, engineering blog, pricing, changelog, CLI, and 17 more developer resources.'
plans:
- name: Tago Io Plans Pricing
  plan_count: 4
  slug: tago-io-plans-pricing
random_paper: 32
rate_limits:
- limit_count: 7
  name: Tago Io Rate Limits
  slug: tago-io-rate-limits
rules:
- name: TagoIO API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: tago-io-jsonschema-spectral-rules
score:
  band: strong
  composite: 61.5
  delta: -3.7
  facets:
    commercial_clarity: 57.9
    contract_quality: 75.5
    developer_ergonomics: 32.6
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 68.4
  previous_composite: 65.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 22
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tago-io/refs/heads/main/screenshots/tago-io-2026-06-20T194853.png
security:
- kind: authentication
  name: Tago Io Authentication
  slug: tago-io-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Tago Io Domain Security
  slug: tago-io-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: trust-center
  name: Tago Io Trust Center
  slug: tago-io-trust-center
  summary_line: ISO 27001, PCI DSS, GDPR
slug: tago-io
tags:
- IoT
- Internet of Things
- Devices
- Data Storage
- Dashboards
- Analysis
- Alerts
- MQTT
- Telemetry
website: https://tago.io/
---
