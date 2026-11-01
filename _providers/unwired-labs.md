---
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
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.6
  scored_at: '2026-10-31'
api_count: 3
apis:
- baseURL: https://us1.unwiredlabs.com/v2
  baseurl_source: declared
  description: The BALANCE API from Unwired Labs (incl. OpenCelliD) — 1 operation(s) for balance.
  name: Unwired Labs (incl. OpenCelliD) BALANCE API
  slug: unwired-labs-balance-api
- baseURL: https://us1.unwiredlabs.com/v2
  baseurl_source: declared
  description: The GEOLOCATION API from Unwired Labs (incl. OpenCelliD) — 1 operation(s) for geolocation.
  name: Unwired Labs (incl. OpenCelliD) GEOLOCATION API
  slug: unwired-labs-geolocation-api
- baseURL: https://us1.unwiredlabs.com/v2
  baseurl_source: declared
  description: The REVERSE API from Unwired Labs (incl. OpenCelliD) — 1 operation(s) for reverse.
  name: Unwired Labs (incl. OpenCelliD) REVERSE API
  slug: unwired-labs-reverse-api
- baseURL: https://us1.unwiredlabs.com/v2
  baseurl_source: declared
  description: The SEARCH API from Unwired Labs (incl. OpenCelliD) — 1 operation(s) for search.
  name: Unwired Labs (incl. OpenCelliD) SEARCH API
  slug: unwired-labs-search-api
- baseURL: https://us1.unwiredlabs.com/v2
  baseurl_source: declared
  description: The Timezone API from Unwired Labs (incl. OpenCelliD) — 1 operation(s) for timezone.
  name: Unwired Labs (incl. OpenCelliD) Timezone API
  slug: unwired-labs-timezone-api
artifact_total: 14
common:
- group: commercial
  href: https://artifacts.apis.io/unwired-labs/plans/unwired-labs-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/unwired-labs-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/unwired-labs/authentication/unwired-labs-authentication.yml
  title: ''
  type: Authentication
  url: authentication/unwired-labs-authentication.yml
- group: operate
  href: https://artifacts.apis.io/unwired-labs/lifecycle/unwired-labs-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/unwired-labs-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/unwired-labs/lifecycle/unwired-labs-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/unwired-labs-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/unwired-labs/conformance/unwired-labs-conformance.yml
  title: ''
  type: Conformance
  url: conformance/unwired-labs-conformance.yml
- group: agent
  href: https://artifacts.apis.io/unwired-labs/llms/unwired-labs-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/unwired-labs-llms.txt
- group: other
  href: https://artifacts.apis.io/unwired-labs/hosts/unwired-labs-hosts.yml
  title: ''
  type: Hosts
  url: hosts/unwired-labs-hosts.yml
- group: other
  href: https://artifacts.apis.io/unwired-labs/vendors/unwired-labs-vendors.yml
  title: ''
  type: Vendors
  url: vendors/unwired-labs-vendors.yml
- group: build
  href: https://artifacts.apis.io/unwired-labs/packages/unwired-labs-packages.yml
  title: ''
  type: SDKs
  url: packages/unwired-labs-packages.yml
- group: build
  href: https://artifacts.apis.io/unwired-labs/packages/unwired-labs-packages.yml
  title: ''
  type: Packages
  url: packages/unwired-labs-packages.yml
- group: other
  title: ''
  type: Leadership
  url: https://unwiredlabs.com/team
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/unwiredlabs
- group: auth
  href: https://artifacts.apis.io/unwired-labs/security/unwired-labs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/unwired-labs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://unwiredlabs.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://my.unwiredlabs.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.unwiredlabs.com
- group: docs
  title: ''
  type: APIReference
  url: https://unwiredlabs.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.unwiredlabs.com/docs/geolocation/getting-started
- group: operate
  title: ''
  type: Support
  url: https://unwiredlabs.com/contact
- group: company
  title: ''
  type: Blog
  url: https://unwiredlabs.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://unwiredlabs.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://my.unwiredlabs.com/trial
- group: commercial
  title: ''
  type: TermsOfService
  url: https://unwiredlabs.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://unwiredlabs.com/privacy
created: '2026-10-28'
description: Unwired Labs provides a Location API that offers geolocation, geocoding, and mapping services using Wi‑Fi positioning, cell tower data, and GPS‑free techniques. Their platform enables developers to locate IoT devices, vehicles, and mobile users worldwide, with additional APIs for reverse geocoding, static and dynamic map generation, and coverage information. The company also operates the OpenCelliD database, a crowdsourced cell tower repository, supporting global positioning services without relying on GPS.
json_schemas:
- name: Balance Response
  property_count: 3
  slug: unwired-labs-balance-response-schema
- name: error
  property_count: 2
  slug: unwired-labs-error-schema
- name: Geolocation
  property_count: 11
  slug: unwired-labs-geolocation-schema
- name: Reverse Geocoding Response
  property_count: 3
  slug: unwired-labs-reverse-response-schema
- name: Search Response
  property_count: 3
  slug: unwired-labs-search-response-schema
- name: timezone_response_schema
  property_count: 3
  slug: unwired-labs-timezone-response-schema
layout: provider
modified: '2026-10-28'
name: Unwired Labs (incl. OpenCelliD)
nav: Providers
network: true
overview: 'Unwired Labs (incl. OpenCelliD) publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including BALANCE API, GEOLOCATION API, REVERSE API, and 2 more. Tagged areas include Company, Location API, Geolocation, Mapping, and OpenCelliD.


  Unwired Labs (incl. OpenCelliD)''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 17 more developer resources.'
plans:
- name: Unwired Labs Plans Pricing
  plan_count: 1
  slug: unwired-labs-plans-pricing
random_paper: 5
score:
  band: developing
  composite: 49.6
  coverage:
    artifact_dirs: 14
    catalog_earned: 55.0
    catalog_earned_first_party: 8.0
    catalog_gap: 60.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 4.5
    contract_quality: 51.8
    developer_ergonomics: 64.3
    discoverability: 69.6
    operational_transparency: 13.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Unwired Labs Authentication
  slug: unwired-labs-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Unwired Labs Domain Security
  slug: unwired-labs-domain-security
  summary_line: TLSv1.3 · DMARC
slug: unwired-labs
tags:
- Company
- Location API
- Geolocation
- Mapping
- OpenCelliD
website: https://unwiredlabs.com/
---
