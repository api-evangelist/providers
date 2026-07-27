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
- acting_count: 63
  human_in_the_loop: 2
  name: Polytomic Agentic Access
  operation_count: 128
  slug: polytomic-agentic-access
  summary_line: 128 operations · 63 acting · 2 human-in-the-loop
api_count: 21
apis:
- description: The subpackage_bulkSync API from Polytomic — 8 operation(s) for subpackage_bulksync.
  name: Polytomic subpackage_bulkSync API
  slug: polytomic-subpackage-bulksync-api
- description: The subpackage_bulkSync.subpackage_bulkSync/executions API from Polytomic — 8 operation(s) for subpackage_bulksync.subpackage_bulksync/executions.
  name: Polytomic subpackage_bulkSync.subpackage_bulkSync/executions API
  slug: polytomic-subpackage-bulksync-subpackage-bulksync-executions-api
- description: The subpackage_bulkSync.subpackage_bulkSync/schedules API from Polytomic — 2 operation(s) for subpackage_bulksync.subpackage_bulksync/schedules.
  name: Polytomic subpackage_bulkSync.subpackage_bulkSync/schedules API
  slug: polytomic-subpackage-bulksync-subpackage-bulksync-schedules-api
- description: The subpackage_bulkSync.subpackage_bulkSync/schemas API from Polytomic — 3 operation(s) for subpackage_bulksync.subpackage_bulksync/schemas.
  name: Polytomic subpackage_bulkSync.subpackage_bulkSync/schemas API
  slug: polytomic-subpackage-bulksync-subpackage-bulksync-schemas-api
- description: The subpackage_connections API from Polytomic — 12 operation(s) for subpackage_connections.
  name: Polytomic subpackage_connections API
  slug: polytomic-subpackage-connections-api
- description: The subpackage_entities API from Polytomic — 2 operation(s) for subpackage_entities.
  name: Polytomic subpackage_entities API
  slug: polytomic-subpackage-entities-api
- description: The subpackage_events API from Polytomic — 2 operation(s) for subpackage_events.
  name: Polytomic subpackage_events API
  slug: polytomic-subpackage-events-api
- description: The subpackage_identity API from Polytomic — 1 operation(s) for subpackage_identity.
  name: Polytomic subpackage_identity API
  slug: polytomic-subpackage-identity-api
- description: The subpackage_jobs API from Polytomic — 1 operation(s) for subpackage_jobs.
  name: Polytomic subpackage_jobs API
  slug: polytomic-subpackage-jobs-api
- description: The subpackage_models API from Polytomic — 6 operation(s) for subpackage_models.
  name: Polytomic subpackage_models API
  slug: polytomic-subpackage-models-api
- description: The subpackage_modelSync API from Polytomic — 9 operation(s) for subpackage_modelsync.
  name: Polytomic subpackage_modelSync API
  slug: polytomic-subpackage-modelsync-api
- description: The subpackage_modelSync.subpackage_modelSync/executions API from Polytomic — 6 operation(s) for subpackage_modelsync.subpackage_modelsync/executions.
  name: Polytomic subpackage_modelSync.subpackage_modelSync/executions API
  slug: polytomic-subpackage-modelsync-subpackage-modelsync-executions-api
- description: The subpackage_modelSync.subpackage_modelSync/targets API from Polytomic — 3 operation(s) for subpackage_modelsync.subpackage_modelsync/targets.
  name: Polytomic subpackage_modelSync.subpackage_modelSync/targets API
  slug: polytomic-subpackage-modelsync-subpackage-modelsync-targets-api
- description: The subpackage_notifications API from Polytomic — 1 operation(s) for subpackage_notifications.
  name: Polytomic subpackage_notifications API
  slug: polytomic-subpackage-notifications-api
- description: The subpackage_organization API from Polytomic — 3 operation(s) for subpackage_organization.
  name: Polytomic subpackage_organization API
  slug: polytomic-subpackage-organization-api
- description: The subpackage_permissions.subpackage_permissions/policies API from Polytomic — 2 operation(s) for subpackage_permissions.subpackage_permissions/policies.
  name: Polytomic subpackage_permissions.subpackage_permissions/policies API
  slug: polytomic-subpackage-permissions-subpackage-permissions-policies-api
- description: The subpackage_permissions.subpackage_permissions/roles API from Polytomic — 2 operation(s) for subpackage_permissions.subpackage_permissions/roles.
  name: Polytomic subpackage_permissions.subpackage_permissions/roles API
  slug: polytomic-subpackage-permissions-subpackage-permissions-roles-api
- description: The subpackage_queryRunner API from Polytomic — 2 operation(s) for subpackage_queryrunner.
  name: Polytomic subpackage_queryRunner API
  slug: polytomic-subpackage-queryrunner-api
- description: The subpackage_schemas API from Polytomic — 7 operation(s) for subpackage_schemas.
  name: Polytomic subpackage_schemas API
  slug: polytomic-subpackage-schemas-api
- description: The subpackage_users API from Polytomic — 5 operation(s) for subpackage_users.
  name: Polytomic subpackage_users API
  slug: polytomic-subpackage-users-api
- description: The subpackage_webhooks API from Polytomic — 4 operation(s) for subpackage_webhooks.
  name: Polytomic subpackage_webhooks API
  slug: polytomic-subpackage-webhooks-api
artifact_total: 30
collections:
- collection_type: open
  name: API Reference
  slug: open-polytomic
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/polytomic-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/polytomic-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/polytomic-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/polytomic-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/polytomic-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/polytomic
- group: company
  title: ''
  type: Website
  url: https://www.polytomic.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.polytomic.com/
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.polytomic.com/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/polytomic
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.polytomic.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://polytomic.com/blog
created: '2026-03-27'
description: Polytomic is a data integration platform providing no-code data syncing between databases, data warehouses, and SaaS applications. The Polytomic REST API exposes connections, syncs, models, bulk syncs, identity, schemas, and webhooks for programmatic management of data movement.
finops:
- name: Polytomic Finops
  service_category: API
  slug: polytomic-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/polytomic.png
layout: provider
modified: '2026-05-19'
name: Polytomic
nav: Providers
network: true
overview: 'Polytomic publishes 21 APIs on the [APIs.io](https://apis.io/) network, including subpackage_bulkSync API, subpackage_bulkSync.subpackage_bulkSync/executions API, subpackage_bulkSync.subpackage_bulkSync/schedules API, and 18 more. Tagged areas include Data Integration, Reverse ETL, Unified API, ELT, and Data Sync.


  Polytomic''s developer surface includes authentication, documentation, API reference, GitHub presence, engineering blog, and 7 more developer resources.'
plans:
- name: Polytomic Plans Pricing
  plan_count: 3
  slug: polytomic-plans-pricing
random_paper: 40
rate_limits:
- limit_count: 5
  name: Polytomic Rate Limits
  slug: polytomic-rate-limits
score:
  band: thin
  composite: 43.5
  delta: 3.2
  facets:
    commercial_clarity: 47.4
    contract_quality: 54.4
    developer_ergonomics: 28.3
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 40.3
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/polytomic/refs/heads/main/screenshots/polytomic-2026-06-20T191910.png
security:
- kind: authentication
  name: Polytomic Authentication
  slug: polytomic-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Polytomic Domain Security
  slug: polytomic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Polytomic Vulnerability Disclosure
  slug: polytomic-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Polytomic Trust Center
  slug: polytomic-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: polytomic
tags:
- Data Integration
- Reverse ETL
- Unified API
- ELT
- Data Sync
website: https://www.polytomic.com/
---
