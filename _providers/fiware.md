---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.0
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 41
  human_in_the_loop: 0
  name: Fiware Agentic Access
  operation_count: 63
  slug: fiware-agentic-access
  summary_line: 63 operations · 41 acting
api_count: 15
apis:
- description: The API Entry Point API from FIWARE — 1 operation(s) for api entry point.
  name: FIWARE API Entry Point API
  slug: fiware-api-entry-point-api
- description: The Attribute Value API from FIWARE — 1 operation(s) for attribute value.
  name: FIWARE Attribute Value API
  slug: fiware-attribute-value-api
- description: The Attributes API from FIWARE — 1 operation(s) for attributes.
  name: FIWARE Attributes API
  slug: fiware-attributes-api
- description: The Batch Operations API from FIWARE — 7 operation(s) for batch operations.
  name: FIWARE Batch Operations API
  slug: fiware-batch-operations-api
- description: The Context Information API from FIWARE — 4 operation(s) for context information.
  name: FIWARE Context Information API
  slug: fiware-context-information-api
- description: The Context Sources API from FIWARE — 4 operation(s) for context sources.
  name: FIWARE Context Sources API
  slug: fiware-context-sources-api
- description: The Context Subscription API from FIWARE — 2 operation(s) for context subscription.
  name: FIWARE Context Subscription API
  slug: fiware-context-subscription-api
- description: The CSourceRegistrations API from FIWARE — 2 operation(s) for csourceregistrations.
  name: FIWARE CSourceRegistrations API
  slug: fiware-csourceregistrations-api
- description: The CSourceSubscriptions API from FIWARE — 2 operation(s) for csourcesubscriptions.
  name: FIWARE CSourceSubscriptions API
  slug: fiware-csourcesubscriptions-api
- description: The Entities API from FIWARE — 11 operation(s) for entities.
  name: FIWARE Entities API
  slug: fiware-entities-api
- description: The Registrations API from FIWARE — 2 operation(s) for registrations.
  name: FIWARE Registrations API
  slug: fiware-registrations-api
- description: The Subscriptions API from FIWARE — 4 operation(s) for subscriptions.
  name: FIWARE Subscriptions API
  slug: fiware-subscriptions-api
- description: The Temporal API from FIWARE — 5 operation(s) for temporal.
  name: FIWARE Temporal API
  slug: fiware-temporal-api
- description: The Temporal Evolution API from FIWARE — 5 operation(s) for temporal evolution.
  name: FIWARE Temporal Evolution API
  slug: fiware-temporal-evolution-api
- description: The Types API from FIWARE — 2 operation(s) for types.
  name: FIWARE Types API
  slug: fiware-types-api
artifact_total: 22
collections:
- collection_type: open
  name: ETSI ISG CIM / NGSI-LD API
  slug: open-fiware-ngsi-ld
- collection_type: open
  name: FIWARE-NGSI v2 Specification
  slug: open-fiware-ngsiv2
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fiware-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fiware-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fiware
- group: company
  title: ''
  type: Website
  url: https://www.fiware.org/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FIWARE
- group: docs
  title: ''
  type: Documentation
  url: https://fiware-orion.readthedocs.io/
- group: docs
  title: ''
  type: Specification
  url: https://github.com/FIWARE/specifications
- group: company
  title: ''
  type: Blog
  url: https://www.fiware.org/feed/
created: '2024-07-02'
description: FIWARE is an open-source framework that provides a curated set of standards and components for context information management. The cornerstone is the NGSI-LD API standardized by ETSI ISG CIM, which allows applications to provide, consume, and subscribe to context information in smart cities, smart industry, smart agriculture, and smart energy scenarios.
finops:
- name: Fiware Finops
  service_category: API
  slug: fiware-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fiware.png
layout: provider
modified: '2026-05-19'
name: FIWARE
nav: Providers
network: true
overview: 'FIWARE publishes 15 APIs on the [APIs.io](https://apis.io/) network, including API Entry Point API, Attribute Value API, Attributes API, and 12 more. Tagged areas include Context Information, Devices, Internet of Things, Linked Data, and NGSI.


  FIWARE''s developer surface includes documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Fiware Plans Pricing
  plan_count: 3
  slug: fiware-plans-pricing
random_paper: 68
rate_limits:
- limit_count: 5
  name: Fiware Rate Limits
  slug: fiware-rate-limits
score:
  band: thin
  composite: 33.6
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 49.2
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 33.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 15
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fiware/refs/heads/main/screenshots/fiware-2026-06-20T181304.png
security:
- kind: domain-security
  name: Fiware Domain Security
  slug: fiware-domain-security
  summary_line: TLSv1.3 · DMARC
slug: fiware
tags:
- Context Information
- Devices
- Internet of Things
- Linked Data
- NGSI
- Smart Cities
- Standards
website: https://www.fiware.org/
---
