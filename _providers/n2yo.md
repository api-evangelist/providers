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
  score: 22.9
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: N2Yo Agentic Access
  operation_count: 5
  slug: n2yo-agentic-access
  summary_line: 5 operations
api_count: 1
apis:
- baseURL: https://api.n2yo.com/rest/v1/satellite
  baseurl_source: declared
  description: Satellites currently above an observer location.
  name: N2YO Above API
  slug: n2yo-above-api
- baseURL: https://api.n2yo.com/rest/v1/satellite
  baseurl_source: declared
  description: Future satellite positions over an observer location.
  name: N2YO Positions API
  slug: n2yo-positions-api
- baseURL: https://api.n2yo.com/rest/v1/satellite
  baseurl_source: declared
  description: Radio-communication satellite pass predictions.
  name: N2YO Radio Passes API
  slug: n2yo-radio-passes-api
- baseURL: https://api.n2yo.com/rest/v1/satellite
  baseurl_source: declared
  description: Two-Line Element data for satellites.
  name: N2YO TLE API
  slug: n2yo-tle-api
- baseURL: https://api.n2yo.com/rest/v1/satellite
  baseurl_source: declared
  description: Optically visible satellite pass predictions.
  name: N2YO Visual Passes API
  slug: n2yo-visual-passes-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: N2YO Satellite Tracking Above API
  slug: open-n2yo-above-api
- collection_type: open
  name: N2YO Satellite Tracking Above Positions API
  slug: open-n2yo-positions-api
- collection_type: open
  name: N2YO Satellite Tracking Above Radio Passes API
  slug: open-n2yo-radio-passes-api
- collection_type: open
  name: N2YO Satellite Tracking Above TLE API
  slug: open-n2yo-tle-api
- collection_type: open
  name: N2YO Satellite Tracking Above Visual Passes API
  slug: open-n2yo-visual-passes-api
- collection_type: open
  name: N2YO Satellite Tracking API
  slug: open-n2yo
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/n2yo-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/n2yo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/n2yo-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/n2yo
- group: company
  title: ''
  type: Website
  url: https://www.n2yo.com/
- group: start
  title: ''
  type: Signup
  url: https://www.n2yo.com/login/register/
- group: start
  title: ''
  type: Login
  url: https://www.n2yo.com/login/
- group: operate
  title: ''
  type: Contact
  url: https://www.n2yo.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.n2yo.com/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.n2yo.com/terms/
created: '2024-03-30'
description: N2YO.com is a website that provides real-time tracking and information about satellites and space stations using space surveillance data from Space Track, operated by the US Air Force Space Command.
finops:
- name: N2Yo Finops
  service_category: API
  slug: n2yo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/n2yo.png
layout: provider
modified: '2026-05-19'
name: N2YO
nav: Providers
network: true
overview: 'N2YO publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Above API, Positions API, Radio Passes API, and 2 more. Tagged areas include Satellites, Space, and Tracking.


  N2YO''s developer surface includes authentication, signup flow, and 8 more developer resources.'
plans:
- name: N2Yo Plans Pricing
  plan_count: 3
  slug: n2yo-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: N2Yo Rate Limits
  slug: n2yo-rate-limits
score:
  band: thin
  composite: 28.6
  coverage:
    artifact_dirs: 9
    catalog_earned: 36.0
    catalog_earned_first_party: 0.0
    catalog_gap: 79.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 22.4
    commercial_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 51.0
    developer_ergonomics: 21.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 28.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/n2yo/refs/heads/main/screenshots/n2yo-2026-06-20T185921.png
security:
- kind: authentication
  name: N2Yo Authentication
  slug: n2yo-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: N2Yo Domain Security
  slug: n2yo-domain-security
  summary_line: TLSv1.2 · DMARC
slug: n2yo
tags:
- Satellites
- Space
- Tracking
website: https://www.n2yo.com/
---
