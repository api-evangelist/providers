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
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Programmatic access to JWST images and observations sourced from the MAST archive. Filter and query by program, observation type, and other attributes. Requires an API key obtained via signup at jwsta
  name: James Webb Space Telescope API
  slug: james-webb-space-telescope-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/james-webb-space-telescope-api-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://jwstapi.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://creativecommons.org/licenses/by/4.0/
created: '2024-11-07'
description: A free, third-party API for accessing James Webb Space Telescope data sourced from the Mikulski Archive for Space Telescopes (MAST). The API provides access to JWST images, observations, and data filterable by program, type, and other parameters. It is built by an independent engineer (not an official NASA, ESA, or CSA service) and data is available under CC-BY 4.0. Authentication is via API key obtained at signup.
finops:
- name: James Webb Space Telescope Api Finops
  service_category: API
  slug: james-webb-space-telescope-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/james-webb-space-telescope-api.png
layout: provider
modified: '2026-04-28'
name: James Webb Space Telescope API
nav: Providers
network: true
overview: James Webb Space Telescope API publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Astronomy, JWST, NASA, Science, and Space.
plans:
- name: James Webb Space Telescope Api Plans Pricing
  plan_count: 3
  slug: james-webb-space-telescope-api-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: James Webb Space Telescope Api Rate Limits
  slug: james-webb-space-telescope-api-rate-limits
score:
  band: emerging
  composite: 17.7
  coverage:
    artifact_dirs: 5
    catalog_gap: 69.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 17.7
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/james-webb-space-telescope-api/refs/heads/main/screenshots/james-webb-space-telescope-api-2026-06-20T183655.png
security:
- kind: domain-security
  name: James Webb Space Telescope Api Domain Security
  slug: james-webb-space-telescope-api-domain-security
  summary_line: TLSv1.3
slug: james-webb-space-telescope-api
tags:
- Astronomy
- JWST
- NASA
- Science
- Space
website: https://jwstapi.com
---
