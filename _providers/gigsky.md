---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
  score: 18.0
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: Programmatic access to GigSky's catalog of regional and global eSIM data plans by destination and price zone, used by partners and enterprises to browse and select connectivity. Endpoints, base URL, a
  name: GigSky Plans & Catalog API
  slug: gigsky-plans-catalog-api
- description: RESTful eSIM/SIM provisioning and lifecycle management through the GigSky Enterprise Manager (GEM) and IoT SIM Management portal - assigning and activating eSIM profiles, country-by-country connectivi
  name: GigSky eSIM Provisioning API
  slug: gigsky-esim-provisioning-api
- description: Order placement and fulfillment for eSIM plans and SIM deployments by partners and enterprises, tied to GigSky's pay-as-you-go and pooled-data billing models. Order endpoints, base URL, and authentica
  name: GigSky Orders API
  slug: gigsky-orders-api
- description: Reporting on data consumption and connectivity usage per SIM, user group, sub-account, or pooled plan, supporting GigSky's monthly statement and pay-as-you-go billing. Usage endpoints and authenticati
  name: GigSky Usage API
  slug: gigsky-usage-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: GigSky Enterprise & IoT API
  slug: open-gigsky
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gigsky-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gigsky-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gigsky
- group: company
  title: ''
  type: Website
  url: https://www.gigsky.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.gigsky.com/enterprise-solutions
- group: commercial
  title: ''
  type: Plans
  url: plans/gigsky-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/gigsky-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/gigsky-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.gigsky.com/blog
created: '2026-06-21'
description: GigSky is a global eSIM and mobile-data roaming platform offering travel and enterprise/IoT cellular connectivity across 190+ destinations. For business, enterprise, and IoT customers it provides the GigSky Enterprise Manager (GEM) and IoT SIM Management portal with RESTful APIs for eSIM provisioning, plan/catalog and connectivity management, orders, and usage controls. The partner/reseller and enterprise API surface is account-gated rather than publicly documented.
finops:
- name: Gigsky Finops
  service_category: Telecommunications and Connectivity
  slug: gigsky-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gigsky.png
layout: provider
modified: '2026-06-21'
name: GigSky
nav: Providers
network: true
overview: 'GigSky publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Plans & Catalog API, eSIM Provisioning API, Orders API, and 1 more. Tagged areas include eSIM, Mobile Data, Roaming, Connectivity, and IoT.


  GigSky''s developer surface includes authentication, documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Gigsky Plans Pricing
  plan_count: 3
  slug: gigsky-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 1
  name: Gigsky Rate Limits
  slug: gigsky-rate-limits
score:
  band: thin
  composite: 28.0
  coverage:
    artifact_dirs: 9
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 30.6
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 28.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 16.7
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gigsky/refs/heads/main/screenshots/gigsky-2026-07-25T215813.png
security:
- kind: authentication
  name: Gigsky Authentication
  slug: gigsky-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Gigsky Domain Security
  slug: gigsky-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: gigsky
tags:
- eSIM
- Mobile Data
- Roaming
- Connectivity
- IoT
- Telecom
website: https://www.gigsky.com/
---
