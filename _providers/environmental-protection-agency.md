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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.0
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Environmental Protection Agency Agentic Access
  operation_count: 6
  slug: environmental-protection-agency-agentic-access
  summary_line: 6 operations
api_count: 1
apis:
- description: Envirofacts provides a single point of access to U.S. EPA environmental data contained in U.S. EPA databases. The RESTful Data Service API returns output in JSON, CSV, Excel, HTML, JSONP, Parquet, PDF
  name: EPA Envirofacts Data Service API
  slug: envirofacts
- description: The EPA Air Quality System (AQS) API provides programmatic access to ambient air pollution data collected by the EPA, state, local, and tribal air pollution control agencies, including hourly sample d
  name: EPA Air Quality System API
  slug: aqs
- description: The EPA UV Index API provides hourly and daily ultraviolet radiation forecasts by ZIP code or city/state. Output is available in XML, JSON, Excel, and CSV formats.
  name: EPA UV Index API
  slug: uv-index
- description: Enforcement and Compliance History Online (ECHO) provides public access to compliance and enforcement information for EPA-regulated facilities nationwide. The ECHO web services API supports facility s
  name: EPA ECHO Compliance and Enforcement API
  slug: echo
- baseURL: https://data.epa.gov/efservice/
  baseurl_source: declared
  description: The Envirofacts API from Environmental Protection Agency — 2 operation(s) for envirofacts.
  name: Environmental Protection Agency Envirofacts API
  slug: environmental-protection-agency-envirofacts-api
- baseURL: https://data.epa.gov/efservice/
  baseurl_source: declared
  description: The UVIndex API from Environmental Protection Agency — 4 operation(s) for uvindex.
  name: Environmental Protection Agency UVIndex API
  slug: environmental-protection-agency-uvindex-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: EPA Data Service Envirofacts API
  slug: open-environmental-protection-agency-envirofacts-api
- collection_type: open
  name: EPA Data Service Envirofacts UVIndex API
  slug: open-environmental-protection-agency-uvindex-api
- collection_type: open
  name: EPA Envirofacts Data Service API
  slug: open-environmental-protection-agency
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/environmental-protection-agency-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/environmental-protection-agency-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/usepa
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/us-epa
- group: company
  title: ''
  type: Website
  url: https://www.epa.gov/
- group: other
  title: ''
  type: Developer Central
  url: https://www.epa.gov/developers
- group: other
  title: ''
  type: Web Services
  url: https://www.epa.gov/enviro/web-services
- group: other
  title: ''
  type: Open Data
  url: https://www.data.gov/
created: '2024-12-03'
description: The U.S. Environmental Protection Agency (EPA) provides multiple public data APIs covering environmental records, air quality monitoring, UV forecasts, and internal data holdings. These services enable State and local governments, federal agencies, researchers, and the public to access environmental data about air, water, and land.
finops:
- name: Environmental Protection Agency Finops
  service_category: API
  slug: environmental-protection-agency-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/environmental-protection-agency.png
layout: provider
modified: '2026-04-28'
name: Environmental Protection Agency
nav: Providers
network: true
overview: 'Environmental Protection Agency publishes 2 APIs on the [APIs.io](https://apis.io/) network: Envirofacts API and UVIndex API. Tagged areas include Environment, Federal-Government, Air Quality, and Open Data.'
plans:
- name: Environmental Protection Agency Plans Pricing
  plan_count: 3
  slug: environmental-protection-agency-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Environmental Protection Agency Rate Limits
  slug: environmental-protection-agency-rate-limits
score:
  band: emerging
  composite: 24.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 45.6
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 24.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/environmental-protection-agency/refs/heads/main/screenshots/environmental-protection-agency-2026-06-20T180737.png
security:
- kind: domain-security
  name: Environmental Protection Agency Domain Security
  slug: environmental-protection-agency-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: environmental-protection-agency
tags:
- Environment
- Federal-Government
- Air Quality
- Open Data
website: https://www.epa.gov/
---
