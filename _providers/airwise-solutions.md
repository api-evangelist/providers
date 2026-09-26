---
agent_readiness:
  band: human-only
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
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.0
  scored_at: '2026-09-25'
api_count: 1
apis:
- description: 'API for UAS services including flight planning, real-time tracking, airspace restrictions and UTM coordination. Reference documentation requires a sign-in with an AirWise developer account; no public '
  name: airwiseOS API
  slug: airwiseos-api
artifact_total: 5
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/airwise-solutions/refs/heads/main/security/airwise-solutions-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/airwise-solutions-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://airwisesolutions.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.airwisesolutions.app/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/airwise-solutions/refs/heads/main/llms/airwise-solutions-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/airwise-solutions-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/airwise-solutions/refs/heads/main/well-known/airwise-solutions-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/airwise-solutions-well-known.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/airwise-solutions/refs/heads/main/conformance/airwise-solutions-conformance.yml
  title: ''
  type: Conformance
  url: conformance/airwise-solutions-conformance.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/airwise-solutions/refs/heads/main/packages/airwise-solutions-packages.yml
  title: ''
  type: Packages
  url: packages/airwise-solutions-packages.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/airwise-solutions/refs/heads/main/plans/airwise-solutions-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/airwise-solutions-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/airwise-solutions/refs/heads/main/rate-limits/airwise-solutions-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/airwise-solutions-rate-limits.yml
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://airwisesolutions.com/cancel-your-subscription-or-delete-your-account-and-data/
- group: company
  title: ''
  type: Blog
  url: https://airwisesolutions.com/insights/
- group: operate
  title: ''
  type: Support
  url: https://airwisesolutions.com/get-started/
- group: start
  title: ''
  type: Login
  url: https://flightmanager.airwisesolutions.app/index.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://airwisesolutions.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://airwisesolutions.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/airwise-solutions/
- group: other
  title: ''
  type: X
  url: https://x.com/AirwiseSolution
coverage:
  checked: '2026-09-20'
  detail: The airwiseOS API reference at developer.airwisesolutions.app sits behind a Cognito sign-in restricted to AirWise developer-account groups, and api.airwisesolutions.app answers 403 Forbidden to every anonymous path, so no contract was saved.
  evidence:
  - status: 200
    url: https://developer.airwisesolutions.app/
  - status: 403
    url: https://developer.airwisesolutions.app/openapi.json
  - status: 403
    url: https://api.airwisesolutions.app/openapi.json
  - status: 200
    url: https://airwisesolutions.com/
  reason: customer-only-docs
  state: gated
created: '2026-09-20'
description: 'AirWise Solutions is a Tulsa, Oklahoma drone operations software company founded in 2021. Its airwiseOS platform covers the full mission lifecycle for public safety and critical infrastructure teams: pre-flight planning and FAA authorizations including LAANC, real-time in-flight airspace awareness fusing ADS-B, Remote ID, RF, radar and weather data, and post-flight data, analytics and compliance. Products include Flight Manager, Nexus and UASidekick. The airwiseOS API exposes flight planning, real-time tracking, airspace restrictions and UTM coordination, and its documentation sits behind a developer-account sign-in.'
image: https://airwisesolutions.com/wp-content/uploads/2026/05/Built-for-managing-energy-and-utilities.jpg
layout: provider
modified: '2026-09-20'
name: AirWise Solutions
nav: Providers
network: true
overview: 'AirWise Solutions publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Drones, UAS, Aviation, and Airspace.


  AirWise Solutions'' developer surface includes engineering blog, support, and 15 more developer resources.'
plans:
- name: Airwise Solutions Plans Pricing
  plan_count: 0
  slug: airwise-solutions-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Airwise Solutions Rate Limits
  slug: airwise-solutions-rate-limits
score:
  band: emerging
  composite: 23.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.6
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 73.2
    operational_transparency: 0.0
  previous_composite: 22.1
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.4
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Airwise Solutions Authentication
  slug: airwise-solutions-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Airwise Solutions Domain Security
  slug: airwise-solutions-domain-security
  summary_line: TLSv1.3 · DMARC
slug: airwise-solutions
tags:
- Company
- Drones
- UAS
- Aviation
- Airspace
- UTM
- Public Safety
- Critical Infrastructure
- Geospatial
website: https://airwisesolutions.com/
---
