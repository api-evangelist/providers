---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.0
  scored_at: '2026-09-19'
api_count: 2
apis:
- baseURL: https://calendar-api.ma
  baseurl_source: declared
  description: National Open business days
  name: API Calendrier Marocain | Jours Fériés & Ouvrables REST + SDK Python Business Days API
  slug: calendar-api-ma-business-days-api
- baseURL: https://calendar-api.ma
  baseurl_source: declared
  description: National holidays of any year and Religious holidays of past years
  name: API Calendrier Marocain | Jours Fériés & Ouvrables REST + SDK Python Holidays API
  slug: calendar-api-ma-holidays-api
- baseURL: https://calendar-api.ma
  baseurl_source: declared
  description: Misc endpoints
  name: API Calendrier Marocain | Jours Fériés & Ouvrables REST + SDK Python Misc API
  slug: calendar-api-ma-misc-api
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://www.calendar-api.ma/
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/calendar-api-ma/refs/heads/main/overlays/calendar-api-ma-calendar-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/calendar-api-ma-calendar-api-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://calendar-api.ma
- group: docs
  title: ''
  type: Documentation
  url: https://docs.calendar-api.ma
- group: docs
  title: ''
  type: APIReference
  url: https://calendar-api.ma/api/v1/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://calendar-api.ma/holidays-api.html
- group: operate
  title: ''
  type: Support
  url: https://calendar-api.ma/contacts.html
- group: start
  title: ''
  type: SignUp
  url: https://calendar-api.ma/console/register
- group: start
  title: ''
  type: Login
  url: https://calendar-api.ma/console/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://calendar-api.ma/privacy.html
- group: build
  title: ''
  type: SourceCode
  url: https://gitlab.com/ud-labs/py-calendar-api
- group: build
  title: ''
  type: Postman
  url: https://documenter.getpostman.com/view/9897118/2sBYArSrTN
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/calendar-api-ma/refs/heads/main/packages/calendar-api-ma-packages.yml
  title: ''
  type: Packages
  url: packages/calendar-api-ma-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/calendar-api-ma/refs/heads/main/packages/calendar-api-ma-packages.yml
  title: ''
  type: SDKs
  url: packages/calendar-api-ma-packages.yml
- group: build
  title: ''
  type: Python SDK
  url: https://pypi.org/project/pycalendar-api/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/calendar-api-ma/refs/heads/main/authentication/calendar-api-ma-authentication.yml
  title: ''
  type: Authentication
  url: authentication/calendar-api-ma-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/calendar-api-ma/refs/heads/main/conventions/calendar-api-ma-conventions.yml
  title: ''
  type: Conventions
  url: conventions/calendar-api-ma-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/calendar-api-ma/refs/heads/main/errors/calendar-api-ma-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/calendar-api-ma-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/calendar-api-ma/refs/heads/main/lifecycle/calendar-api-ma-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/calendar-api-ma-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/calendar-api-ma/refs/heads/main/changelog/calendar-api-ma-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/calendar-api-ma-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/calendar-api-ma/refs/heads/main/conformance/calendar-api-ma-conformance.yml
  title: ''
  type: Conformance
  url: conformance/calendar-api-ma-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/calendar-api-ma/refs/heads/main/data-model/calendar-api-ma-data-model.yml
  title: ''
  type: DataModel
  url: data-model/calendar-api-ma-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/calendar-api-ma/refs/heads/main/examples/calendar-api-ma-examples.yml
  title: ''
  type: Examples
  url: examples/calendar-api-ma-examples.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/calendar-api-ma/refs/heads/main/rate-limits/calendar-api-ma-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/calendar-api-ma-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/calendar-api-ma/refs/heads/main/plans/calendar-api-ma-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/calendar-api-ma-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/calendar-api-ma/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/calendar-api-ma/refs/heads/main/llms/calendar-api-ma-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/calendar-api-ma-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/calendar-api-ma/refs/heads/main/security/calendar-api-ma-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/calendar-api-ma-domain-security.yml
created: '2026-08-18'
description: 'Calendar API is a REST service from Unravel Designs (Casablanca, Morocco) that turns the Moroccan economic calendar into a callable contract. It returns national, religious and exceptional public holidays with an explicit Estimated/Official status — religious feasts are dated astronomically and only become Official after moon sighting — and it calculates open business days: next and previous working day, counts and listings between two dates, and CalSpan, a chainable business-day [start_date, end_date] interval for a month, quarter, semester or year that drops straight into a SQL BETWEEN. Fourteen read-only GET operations are described by a published OpenAPI 3.1 document, authenticated with an X-API-KEY header, and wrapped by a typed first-party Python SDK (pycalendar-api). It is aimed at data engineers wiring Moroccan holiday logic into ETL pipelines and orchestrators such as Airflow and Dagster, and at regulated-market reporting where a hardcoded holiday table quietly goes
  stale every year.'
image: https://calendar-api.ma/assets/img/logos/cal-api-logo%20small.webp
layout: provider
modified: '2026-08-18'
name: API Calendrier Marocain | Jours Fériés & Ouvrables REST + SDK Python
nav: Providers
network: true
overview: 'API Calendrier Marocain | Jours Fériés & Ouvrables REST + SDK Python publishes 3 APIs on the [APIs.io](https://apis.io/) network: Business Days API, Holidays API, and Misc API. Tagged areas include Holidays, Morocco, Calendar, Business Days, and date-utilities.


  API Calendrier Marocain | Jours Fériés & Ouvrables REST + SDK Python''s developer surface includes documentation, API reference, getting-started guide, support, signup flow, authentication, changelog, and 21 more developer resources.'
plans:
- name: Calendar Api Ma Plans Pricing
  plan_count: 1
  slug: calendar-api-ma-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Calendar Api Ma Rate Limits
  slug: calendar-api-ma-rate-limits
score:
  band: developing
  composite: 47.6
  coverage:
    artifact_dirs: 20
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 54.0
    developer_ergonomics: 68.5
    discoverability: 68.5
    operational_transparency: 21.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - africa
  previous_composite: 47.6
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 28.4
  schema_version: 0.22.0
  scored_at: '2026-09-19'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://raw.githubusercontent.com/api-evangelist/calendar-api-ma/refs/heads/main/screenshots/calendar-api-ma-2026-09-02T145004.png
security:
- kind: authentication
  name: Calendar Api Ma Authentication
  slug: calendar-api-ma-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Calendar Api Ma Domain Security
  slug: calendar-api-ma-domain-security
  summary_line: TLSv1.3
slug: calendar-api-ma
tags:
- Holidays
- Morocco
- Calendar
- Business Days
- date-utilities
- Data Engineering
- ETL
- Python SDK
- Localization
- Reference Data
- Public Holidays
- Scheduling
website: https://www.calendar-api.ma/
---
