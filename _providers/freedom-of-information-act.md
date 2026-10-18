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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.9
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Freedom Of Information Act Agentic Access
  operation_count: 5
  slug: freedom-of-information-act-agentic-access
  summary_line: 5 operations · 1 acting
api_count: 1
apis:
- baseURL: https://api.foia.gov
  baseurl_source: declared
  description: Agencies and their FOIA components.
  name: Freedom of Information Act Agency Components API
  slug: freedom-of-information-act-agency-components-api
- baseURL: https://api.foia.gov
  baseurl_source: declared
  description: Portal-to-agency request submission API (implemented by participating agencies at foia-api.agency.gov).
  name: Freedom of Information Act Agency Submission API
  slug: freedom-of-information-act-agency-submission-api
- baseURL: https://api.foia.gov
  baseurl_source: declared
  description: Agency annual FOIA reports as XML.
  name: Freedom of Information Act Annual Reports API
  slug: freedom-of-information-act-annual-reports-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Freedom of Information Act (FOIA) Agency Components API
  slug: open-freedom-of-information-act-agency-components-api
- collection_type: open
  name: Freedom of Information Act (FOIA) Agency Components Agency Submission API
  slug: open-freedom-of-information-act-agency-submission-api
- collection_type: open
  name: Freedom of Information Act (FOIA) Agency Components Annual Reports API
  slug: open-freedom-of-information-act-annual-reports-api
- collection_type: open
  name: Freedom of Information Act (FOIA) API
  slug: open-freedom-of-information-act
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/freedom-of-information-act/refs/heads/main/plans/freedom-of-information-act-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/freedom-of-information-act-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/freedom-of-information-act/refs/heads/main/rate-limits/freedom-of-information-act-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/freedom-of-information-act-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/freedom-of-information-act/refs/heads/main/finops/freedom-of-information-act-finops.yml
  title: ''
  type: FinOps
  url: finops/freedom-of-information-act-finops.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/freedom-of-information-act/refs/heads/main/capabilities/freedom-of-information-act-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/freedom-of-information-act-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/freedom-of-information-act/refs/heads/main/agentic-access/freedom-of-information-act-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/freedom-of-information-act-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/freedom-of-information-act/refs/heads/main/security/freedom-of-information-act-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/freedom-of-information-act-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/freedom-of-information-act/refs/heads/main/authentication/freedom-of-information-act-authentication.yml
  title: ''
  type: Authentication
  url: authentication/freedom-of-information-act-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://www.foia.gov/developer/
- group: company
  title: ''
  type: Website
  url: https://www.foia.gov/
created: '2024-01-01'
description: The Freedom of Information Act (FOIA) API provides access to FOIA request data and related information from federal agencies.
finops:
- has_sources: false
  method: generated
  name: Freedom Of Information Act Finops
  primary_unit: ''
  service_category: API
  slug: freedom-of-information-act-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/freedom-of-information-act.png
layout: provider
modified: '2026-05-19'
name: Freedom of Information Act
nav: Providers
network: true
overview: 'Freedom of Information Act publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Agency Components API, Agency Submission API, and Annual Reports API. Tagged areas include Federal Government, FOIA, and Transparency.


  Freedom of Information Act''s developer surface includes authentication, developer portal, and 7 more developer resources.'
plans:
- name: Freedom Of Information Act Plans Pricing
  plan_count: 3
  slug: freedom-of-information-act-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Freedom Of Information Act Rate Limits
  slug: freedom-of-information-act-rate-limits
score:
  band: emerging
  composite: 24.8
  coverage:
    artifact_dirs: 11
    catalog_earned: 33.0
    catalog_earned_first_party: 0.0
    catalog_gap: 82.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.7
  facets:
    access_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 48.6
    developer_ergonomics: 31.0
    discoverability: 48.2
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 26.5
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
    regime: Government & Public Sector
    regime_id: government
    score: 11.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/freedom-of-information-act/refs/heads/main/screenshots/freedom-of-information-act-2026-06-20T181524.png
security:
- kind: authentication
  name: Freedom Of Information Act Authentication
  slug: freedom-of-information-act-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Freedom Of Information Act Domain Security
  slug: freedom-of-information-act-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: freedom-of-information-act
tags:
- Federal Government
- FOIA
- Transparency
website: https://www.foia.gov/
---
