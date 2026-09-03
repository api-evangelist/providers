---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
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
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: The PotlatchDeltic API provides access to platform services and data for enterprise integration and automation.
  name: PotlatchDeltic API
  slug: potlatch-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/potlatch-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/potlatchdeltic
- group: company
  title: ''
  type: Website
  url: https://www.potlatchdeltic.com
created: '2026-04-19'
description: PotlatchDeltic is a major US corporation and Fortune 1000 company. The PotlatchDeltic API provides programmatic access to its platform services, data, and integrations for enterprise customers and partners.
finops:
- name: Potlatch Finops
  service_category: Materials
  slug: potlatch-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/potlatch.png
layout: provider
modified: '2026-04-19'
name: PotlatchDeltic
nav: Providers
network: true
overview: PotlatchDeltic publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Timber, Real-Estate, and Wood Products.
plans:
- name: Potlatch Plans Pricing
  plan_count: 1
  slug: potlatch-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 1
  name: Potlatch Rate Limits
  slug: potlatch-rate-limits
score:
  band: emerging
  composite: 11.2
  coverage:
    artifact_dirs: 6
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
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/potlatch/refs/heads/main/screenshots/potlatch-2026-06-20T192021.png
security:
- kind: domain-security
  name: Potlatch Domain Security
  slug: potlatch-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: potlatch
tags:
- Timber
- Real-Estate
- Wood Products
website: https://www.potlatchdeltic.com
---
