---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
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
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Singularity Energy Agentic Access
  operation_count: 9
  slug: singularity-energy-agentic-access
  summary_line: 9 operations · 3 acting
api_count: 1
apis:
- baseURL: https://api.singularity.energy
  baseurl_source: declared
  description: The Emissions API from Singularity — 3 operation(s) for emissions.
  name: Singularity Emissions API
  slug: singularity-energy-emissions-api
- baseURL: https://api.singularity.energy
  baseurl_source: declared
  description: The Events API from Singularity — 4 operation(s) for events.
  name: Singularity Events API
  slug: singularity-energy-events-api
- baseURL: https://api.singularity.energy
  baseurl_source: declared
  description: The Interchange API from Singularity — 2 operation(s) for interchange.
  name: Singularity Interchange API
  slug: singularity-energy-interchange-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Singularity Grid Carbon Emissions API
  slug: open-singularity-energy-emissions-api
- collection_type: open
  name: Singularity Grid Carbon Emissions Events API
  slug: open-singularity-energy-events-api
- collection_type: open
  name: Singularity Grid Carbon Emissions Interchange API
  slug: open-singularity-energy-interchange-api
- collection_type: open
  name: Singularity Grid Carbon API
  slug: open-singularity-energy
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/singularity-energy-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/singularity-energy-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/singularity-energy-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://medium.com/feed/singularity-energy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/singularity-energy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/singularity-energy
- group: company
  title: ''
  type: Website
  url: https://www.singularity.energy
- group: docs
  title: ''
  type: Documentation
  url: https://docs.singularity.energy
- group: commercial
  title: ''
  type: Plans
  url: plans/singularity-energy-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/singularity-energy-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/singularity-energy-finops.yml
created: '2026-06-21'
description: Singularity Energy is a Boston-based grid decarbonization data company. Its Grid Carbon API delivers hourly, location-specific electricity emissions intelligence - generated, consumed, and marginal carbon intensity, fuel mix, generation events, interchange, and 48-hour emissions forecasts across ISOs and balancing authorities in the U.S. and Canada.
finops:
- name: Singularity Energy Finops
  service_category: Analytics
  slug: singularity-energy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/singularity-energy.png
layout: provider
modified: '2026-06-21'
name: Singularity
nav: Providers
network: true
overview: 'Singularity publishes 3 APIs on the [APIs.io](https://apis.io/) network: Emissions API, Events API, and Interchange API. Tagged areas include Energy, Carbon Emissions, Grid, Sustainability, and Carbon Intensity.


  Singularity''s developer surface includes authentication, engineering blog, documentation, and 8 more developer resources.'
plans:
- name: Singularity Energy Plans Pricing
  plan_count: 3
  slug: singularity-energy-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 3
  name: Singularity Energy Rate Limits
  slug: singularity-energy-rate-limits
score:
  band: thin
  composite: 38.4
  coverage:
    artifact_dirs: 10
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 50.3
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 38.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 16.2
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/singularity-energy/refs/heads/main/screenshots/singularity-energy-2026-09-02T155609.png
security:
- kind: authentication
  name: Singularity Energy Authentication
  slug: singularity-energy-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Singularity Energy Domain Security
  slug: singularity-energy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: singularity-energy
tags:
- Energy
- Carbon Emissions
- Grid
- Sustainability
- Carbon Intensity
website: https://www.singularity.energy
---
