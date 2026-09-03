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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: API for managing and accessing operation support equipment data, inventory, maintenance records, and deployment information for operational logistics and equipment lifecycle management.
  name: Operation Support Equipment API
  slug: operation-support-equipment
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/operation-support-equipment-domain-security.yml
created: '2024-01-15'
description: API for managing and accessing operation support equipment data, inventory, maintenance records, and deployment information for operational logistics and equipment lifecycle management.
finops:
- name: Operation Support Equipment Finops
  service_category: API
  slug: operation-support-equipment-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/operation-support-equipment.png
layout: provider
modified: '2026-04-28'
name: Operation Support Equipment
nav: Providers
network: true
overview: Operation Support Equipment publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Deployment, Equipment Management, Inventory, Logistics, and Maintenance.
plans:
- name: Operation Support Equipment Plans Pricing
  plan_count: 3
  slug: operation-support-equipment-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Operation Support Equipment Rate Limits
  slug: operation-support-equipment-rate-limits
score:
  band: emerging
  composite: 11.1
  coverage:
    artifact_dirs: 5
    catalog_gap: 79.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 11.1
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/operation-support-equipment/refs/heads/main/screenshots/operation-support-equipment-2026-06-20T191100.png
security:
- kind: domain-security
  name: Operation Support Equipment Domain Security
  slug: operation-support-equipment-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: operation-support-equipment
tags:
- Deployment
- Equipment Management
- Inventory
- Logistics
- Maintenance
- Operation Support
---
