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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Trimble Agriculture Agentic Access
  operation_count: 31
  slug: trimble-agriculture-agentic-access
  summary_line: 31 operations · 13 acting
api_count: 1
apis:
- description: The Trimble Agriculture Telematics API provides access to real-time and historical equipment telematics data from connected Trimble displays and precision agriculture devices. Includes equipment locat
  name: Trimble Agriculture Telematics API
  slug: trimble-agriculture-telematics
- description: The Boundaries API from Trimble Agriculture — 1 operation(s) for boundaries.
  name: Trimble Agriculture Boundaries API
  slug: trimble-agriculture-boundaries-api
- description: The Crop Zones API from Trimble Agriculture — 2 operation(s) for crop zones.
  name: Trimble Agriculture Crop Zones API
  slug: trimble-agriculture-crop-zones-api
- description: The Equipment Activities API from Trimble Agriculture — 3 operation(s) for equipment activities.
  name: Trimble Agriculture Equipment Activities API
  slug: trimble-agriculture-equipment-activities-api
- description: The Farms API from Trimble Agriculture — 2 operation(s) for farms.
  name: Trimble Agriculture Farms API
  slug: trimble-agriculture-farms-api
- description: The Fields API from Trimble Agriculture — 2 operation(s) for fields.
  name: Trimble Agriculture Fields API
  slug: trimble-agriculture-fields-api
- description: The Imagery API from Trimble Agriculture — 1 operation(s) for imagery.
  name: Trimble Agriculture Imagery API
  slug: trimble-agriculture-imagery-api
- description: The Materials API from Trimble Agriculture — 1 operation(s) for materials.
  name: Trimble Agriculture Materials API
  slug: trimble-agriculture-materials-api
- description: The Organizations API from Trimble Agriculture — 2 operation(s) for organizations.
  name: Trimble Agriculture Organizations API
  slug: trimble-agriculture-organizations-api
- description: The Prescriptions API from Trimble Agriculture — 2 operation(s) for prescriptions.
  name: Trimble Agriculture Prescriptions API
  slug: trimble-agriculture-prescriptions-api
- description: The Work Orders API from Trimble Agriculture — 2 operation(s) for work orders.
  name: Trimble Agriculture Work Orders API
  slug: trimble-agriculture-work-orders-api
artifact_total: 39
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Trimble Agriculture Data Boundaries API
  slug: open-trimble-agriculture-boundaries-api
- collection_type: open
  name: Trimble Agriculture Data Boundaries Crop Zones API
  slug: open-trimble-agriculture-crop-zones-api
- collection_type: open
  name: Trimble Agriculture Data Boundaries Equipment Activities API
  slug: open-trimble-agriculture-equipment-activities-api
- collection_type: open
  name: Trimble Agriculture Data Boundaries Farms API
  slug: open-trimble-agriculture-farms-api
- collection_type: open
  name: Trimble Agriculture Data Boundaries Fields API
  slug: open-trimble-agriculture-fields-api
- collection_type: open
  name: Trimble Agriculture Data Boundaries Imagery API
  slug: open-trimble-agriculture-imagery-api
- collection_type: open
  name: Trimble Agriculture Data Boundaries Materials API
  slug: open-trimble-agriculture-materials-api
- collection_type: open
  name: Trimble Agriculture Data Boundaries Organizations API
  slug: open-trimble-agriculture-organizations-api
- collection_type: open
  name: Trimble Agriculture Data Boundaries Prescriptions API
  slug: open-trimble-agriculture-prescriptions-api
- collection_type: open
  name: Trimble Agriculture Data Boundaries Work Orders API
  slug: open-trimble-agriculture-work-orders-api
- collection_type: open
  name: Trimble Agriculture Data API
  slug: open-trimble-agriculture
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/trimble-agriculture-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/trimble-agriculture-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/trimble-agriculture-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trimble-agriculture-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/trimble-agriculture-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/trimble-ag
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/trimble-agriculture
- group: company
  title: ''
  type: Website
  url: https://agriculture.trimble.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://agdeveloper.trimble.com/
- group: docs
  title: ''
  type: Documentation
  url: https://agdeveloper.trimble.com/api-docs
- group: start
  title: ''
  type: Signup
  url: https://agdeveloper.trimble.com/
- group: operate
  title: ''
  type: Contact
  url: mailto:ag_api@trimble.com
created: '2025-02-06'
description: The Trimble Agriculture Cloud is an independent, brand-agnostic platform that connects infield devices and operational workflows to more efficiently execute crop production plans and collect robust agricultural datasets. The Trimble Agriculture API (now operating as PTxAg FarmENGAGE) provides REST APIs for farm setup, field boundaries, task records, work orders, prescriptions, equipment activities, crop zones, materials, and telematics. It enables third-party integrators to exchange as-applied data, send prescriptions to Trimble displays, and align field resources across precision agriculture systems. The platform serves over 180 million customer acres globally.
examples:
- key_count: 2
  name: Trimble Agriculture Create Work Order Example
  slug: trimble-agriculture-create-work-order-example
- key_count: 2
  name: Trimble Agriculture List Equipment Activities Example
  slug: trimble-agriculture-list-equipment-activities-example
- key_count: 2
  name: Trimble Agriculture List Farms Example
  slug: trimble-agriculture-list-farms-example
finops:
- name: Trimble Agriculture Finops
  service_category: API
  slug: trimble-agriculture-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/trimble-agriculture.png
json_schemas:
- name: Trimble Agriculture Equipment Activity
  property_count: 10
  slug: trimble-agriculture-activity
- name: Trimble Agriculture Crop Zone
  property_count: 8
  slug: trimble-agriculture-cropzone
json_structures:
- name: Trimble Agriculture Cropzone Structure
  property_count: 0
  slug: trimble-agriculture-cropzone-structure
jsonld:
- class_count: 9
  name: Trimble Agriculture Context
  property_count: 28
  slug: trimble-agriculture-context
layout: provider
modified: '2026-05-19'
name: Trimble Agriculture
nav: Providers
network: true
overview: 'Trimble Agriculture publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Boundaries API, Crop Zones API, Equipment Activities API, and 7 more. Tagged areas include Agriculture, Farming, IoT, Precision Agriculture, and Field Management.


  The Trimble Agriculture catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Trimble Agriculture''s developer surface includes authentication, documentation, signup flow, and 9 more developer resources.'
plans:
- name: Trimble Agriculture Plans Pricing
  plan_count: 3
  slug: trimble-agriculture-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Trimble Agriculture Rate Limits
  slug: trimble-agriculture-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Trimble Agriculture API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: trimble-agriculture-jsonschema-spectral-rules
- effective_rule_count: 52
  extends:
  - spectral:oas
  name: Trimble Agriculture API Rules
  rule_count: 11
  severity_counts:
    error: 5
    hint: 2
    info: 0
    warn: 4
  slug: trimble-agriculture-rules
score:
  band: thin
  composite: 35.8
  coverage:
    artifact_dirs: 16
    catalog_gap: 58.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 13.6
    contract_quality: 60.8
    developer_ergonomics: 21.4
    discoverability: 59.3
    governance: 13.6
    operational_transparency: 10.5
  previous_composite: 35.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/trimble-agriculture/refs/heads/main/screenshots/trimble-agriculture-2026-06-20T195713.png
security:
- kind: authentication
  name: Trimble Agriculture Authentication
  slug: trimble-agriculture-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Trimble Agriculture Domain Security
  slug: trimble-agriculture-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Trimble Agriculture Trust Center
  slug: trimble-agriculture-trust-center
  summary_line: SOC 2, ISO 27001
slug: trimble-agriculture
tags:
- Agriculture
- Farming
- IoT
- Precision Agriculture
- Field Management
- Prescriptions
- Telematics
website: https://agriculture.trimble.com/
---
