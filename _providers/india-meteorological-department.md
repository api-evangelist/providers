---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 7.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: JSON APIs under https://api.imd.gov.in/api/v1/ documented in IMD's HTML API reference, covering city weather forecasts (7 days), subdivision and state/district rainfall forecasts, current weather, dis
  name: IMD Weather API
  slug: imd-weather-api
artifact_total: 6
common:
- group: design
  href: https://artifacts.apis.io/india-meteorological-department/conventions/india-meteorological-department-conventions.yml
  title: ''
  type: Conventions
  url: conventions/india-meteorological-department-conventions.yml
- group: auth
  href: https://artifacts.apis.io/india-meteorological-department/authentication/india-meteorological-department-authentication.yml
  title: ''
  type: Authentication
  url: authentication/india-meteorological-department-authentication.yml
- group: design
  href: https://artifacts.apis.io/india-meteorological-department/lifecycle/india-meteorological-department-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/india-meteorological-department-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/india-meteorological-department/errors/india-meteorological-department-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/india-meteorological-department-problem-types.yml
- group: other
  href: https://artifacts.apis.io/india-meteorological-department/hosts/india-meteorological-department-hosts.yml
  title: ''
  type: Hosts
  url: hosts/india-meteorological-department-hosts.yml
- group: auth
  href: https://artifacts.apis.io/india-meteorological-department/security/india-meteorological-department-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/india-meteorological-department-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mausam.imd.gov.in/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.imd.gov.in/public/
- group: docs
  title: ''
  type: Documentation
  url: https://mausam.imd.gov.in/Forecast/marquee_data/API_doc.pdf
- group: docs
  title: ''
  type: APIReference
  url: https://api.imd.gov.in/public/api_reference.html
- group: operate
  title: ''
  type: Support
  url: https://api.imd.gov.in/public/contact.php
- group: operate
  title: ''
  type: Contact
  url: https://mausam.imd.gov.in/responsive/contact.php
- group: operate
  title: ''
  type: HelpCenter
  url: https://mausam.imd.gov.in/responsive/faq.php
- group: start
  title: ''
  type: SignUp
  url: https://api.imd.gov.in/public/register.php
created: '2026-10-28'
description: India Meteorological Department (IMD; Hindi भारत मौसम विज्ञान विभाग) is the national weather agency of India under the Ministry of Earth Sciences, Government of India, responsible for weather forecasting, climate monitoring and meteorological services. Through its IMD API Management portal (api.imd.gov.in), with self-service account registration, IMD offers developers JSON APIs for current weather observations, city-level forecasts, district nowcasts and warnings, rainfall data and marine bulletins, documented in an HTML API reference and a PDF API document.
image: https://mausam.imd.gov.in/responsive/img/logo/logo_emb.png
layout: provider
modified: '2026-10-28'
name: India Meteorological Department
nav: Providers
network: true
overview: 'India Meteorological Department is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Weather, Meteorology, India, and Public Data.


  India Meteorological Department''s developer surface includes authentication, documentation, API reference, support, signup flow, and 9 more developer resources.'
plans:
- name: India Meteorological Department Plans Pricing
  plan_count: 0
  slug: india-meteorological-department-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: India Meteorological Department Rate Limits
  slug: india-meteorological-department-rate-limits
scopes:
- name: India Meteorological Department Scopes
  scope_count: 0
  slug: india-meteorological-department-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 14.7
  coverage:
    artifact_dirs: 20
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.4
  facets:
    access_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 27.4
    discoverability: 66.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 19.1
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 21.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/india-meteorological-department/india-meteorological-department-2026-11-03T133735.png
security:
- kind: authentication
  name: India Meteorological Department Authentication
  slug: india-meteorological-department-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: India Meteorological Department Domain Security
  slug: india-meteorological-department-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: india-meteorological-department
tags:
- Company
- Weather
- Meteorology
- India
- Public Data
- Climate
- Government
website: https://mausam.imd.gov.in/
---
