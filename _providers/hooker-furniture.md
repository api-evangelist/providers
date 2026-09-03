---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - '{''url'': ''https://www.hookerfurniture.com'', ''status'': 301, ''note'': ''declared website redirects to https://hookerfurnishings.com/ — a different registrable domain (hookerfurniture.com -> hookerfurnishings.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
- description: The Hooker Furniture API provides access to platform services and data for enterprise integration and automation.
  name: Hooker Furniture API
  slug: hooker-furniture-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hooker-furniture-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hooker-furnishings-corporation
- group: company
  title: ''
  type: Website
  url: https://www.hookerfurniture.com
created: '2026-04-19'
description: Hooker Furniture is a major US corporation and Fortune 1000 company. The Hooker Furniture API provides programmatic access to its platform services, data, and integrations for enterprise customers and partners.
finops:
- name: Hooker Furniture Finops
  service_category: Furniture & Home Products
  slug: hooker-furniture-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hooker-furniture.png
layout: provider
modified: '2026-04-19'
name: Hooker Furniture
nav: Providers
network: true
overview: Hooker Furniture publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Furniture and Home Products.
plans:
- name: Hooker Furniture Plans Pricing
  plan_count: 1
  slug: hooker-furniture-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 1
  name: Hooker Furniture Rate Limits
  slug: hooker-furniture-rate-limits
score:
  band: emerging
  composite: 11.2
  coverage:
    artifact_dirs: 5
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 11.2
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hooker-furniture/refs/heads/main/screenshots/hooker-furniture-2026-06-20T182830.png
security:
- kind: domain-security
  name: Hooker Furniture Domain Security
  slug: hooker-furniture-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hooker-furniture
tags:
- Furniture
- Home Products
website: https://www.hookerfurniture.com
---
