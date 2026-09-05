---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: National Agricultural Library Agentic Access
  operation_count: 9
  slug: national-agricultural-library-agentic-access
  summary_line: 9 operations · 3 acting
api_count: 1
apis:
- baseURL: https://api.nal.usda.gov/fdc/v1
  baseurl_source: declared
  description: endpoints to retrieve nutrient data
  name: National Agricultural Library FDC API
  slug: national-agricultural-library-fdc-api
artifact_total: 10
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Food Data Central FDC API
  slug: open-national-agricultural-library-fdc-api
- collection_type: open
  name: Food Data Central API
  slug: open-national-agricultural-library
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/national-agricultural-library-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/national-agricultural-library-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/national-agricultural-library-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/national-agricultural-library
- group: company
  title: ''
  type: Website
  url: https://www.nal.usda.gov/
- group: start
  title: ''
  type: Portal
  url: https://fdc.nal.usda.gov/
created: '2024-11-21'
description: The USDA National Agricultural Library houses one of the world's largest collections devoted to agriculture and its related sciences, and operates FoodData Central, an integrated data system providing nutrient profiles for foods.
finops:
- name: National Agricultural Library Finops
  service_category: API
  slug: national-agricultural-library-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/national-agricultural-library.png
layout: provider
modified: '2026-05-19'
name: National Agricultural Library
nav: Providers
network: true
overview: 'National Agricultural Library publishes 1 API on the [APIs.io](https://apis.io/) network: FDC API. Tagged areas include Agriculture, Federal-Government, Library, Food, and Nutrition.


  National Agricultural Library''s developer surface includes authentication, developer portal, and 4 more developer resources.'
plans:
- name: National Agricultural Library Plans Pricing
  plan_count: 3
  slug: national-agricultural-library-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: National Agricultural Library Rate Limits
  slug: national-agricultural-library-rate-limits
score:
  band: thin
  composite: 33.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 46.0
    catalog_earned_first_party: 0.0
    catalog_gap: 69.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 53.0
    developer_ergonomics: 31.0
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 33.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 22.2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/national-agricultural-library/refs/heads/main/screenshots/national-agricultural-library-2026-06-20T185959.png
security:
- kind: authentication
  name: National Agricultural Library Authentication
  slug: national-agricultural-library-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: National Agricultural Library Domain Security
  slug: national-agricultural-library-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: national-agricultural-library
tags:
- Agriculture
- Federal-Government
- Library
- Food
- Nutrition
website: https://www.nal.usda.gov/
---
