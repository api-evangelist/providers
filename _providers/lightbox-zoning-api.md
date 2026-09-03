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
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Lightbox Zoning Api Agentic Access
  operation_count: 3
  slug: lightbox-zoning-api-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 1
apis:
- baseURL: https://api.lightboxre.com/v1
  baseurl_source: declared
  description: Zoning lookups by parcel, address, or geometry
  name: LightBox Zoning API Zoning API
  slug: lightbox-zoning-api-zoning-api
artifact_total: 10
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: LightBox Zoning API
  slug: open-lightbox-zoning-api-zoning-api
- collection_type: open
  name: LightBox Zoning API
  slug: open-lightbox-zoning-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lightbox-zoning-api-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lightbox-zoning-api-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lightbox-zoning-api-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lightbox-re
created: '2025-01-07'
description: Zoning data is a critical piece of decision making for the CRE and builder/developer markets, giving insights into what a property is zoned for, zoning districts, setback requirements, floor area ratio (FAR), building height limits, allowed uses, and more. Part of the LightBox property and location intelligence platform.
finops:
- name: Lightbox Zoning Api Finops
  service_category: API
  slug: lightbox-zoning-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lightbox-zoning-api.png
layout: provider
modified: '2026-05-19'
name: LightBox Zoning API
nav: Providers
network: true
overview: 'LightBox Zoning API publishes 1 API on the [APIs.io](https://apis.io/) network: Zoning API. Tagged areas include Zoning, Real-Estate, CRE, Property, and Parcels.


  LightBox Zoning API''s developer surface includes authentication and 3 more developer resources.'
plans:
- name: Lightbox Zoning Api Plans Pricing
  plan_count: 3
  slug: lightbox-zoning-api-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Lightbox Zoning Api Rate Limits
  slug: lightbox-zoning-api-rate-limits
score:
  band: thin
  composite: 27.6
  coverage:
    artifact_dirs: 10
    catalog_gap: 69.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 49.0
    developer_ergonomics: 21.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 27.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lightbox-zoning-api/refs/heads/main/screenshots/lightbox-zoning-api-2026-06-20T184514.png
security:
- kind: authentication
  name: Lightbox Zoning Api Authentication
  slug: lightbox-zoning-api-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Lightbox Zoning Api Domain Security
  slug: lightbox-zoning-api-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lightbox-zoning-api
tags:
- Zoning
- Real-Estate
- CRE
- Property
- Parcels
- Geospatial
- Land Use
---
