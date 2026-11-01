---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 36.7
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Airthings Agentic Access
  operation_count: 39
  slug: airthings-agentic-access
  summary_line: 39 operations · 8 acting
api_count: 2
apis:
- baseURL: https://ext-api.airthings.com
  baseurl_source: declared
  description: The Accounts API from Airthings — 1 operation(s) for accounts.
  name: Airthings Accounts API
  slug: airthings-accounts-api
- baseURL: https://ext-api.airthings.com
  baseurl_source: declared
  description: The Device API from Airthings — 1 operation(s) for device.
  name: Airthings Device API
  slug: airthings-device-api
- baseURL: https://ext-api.airthings.com
  baseurl_source: declared
  description: The Devices API from Airthings — 13 operation(s) for devices.
  name: Airthings Devices API
  slug: airthings-devices-api
- baseURL: https://ext-api.airthings.com
  baseurl_source: declared
  description: The Health API from Airthings — 1 operation(s) for health.
  name: Airthings Health API
  slug: airthings-health-api
- baseURL: https://ext-api.airthings.com
  baseurl_source: declared
  description: The Locations API from Airthings — 4 operation(s) for locations.
  name: Airthings Locations API
  slug: airthings-locations-api
- baseURL: https://ext-api.airthings.com
  baseurl_source: declared
  description: The Organizations API from Airthings — 1 operation(s) for organizations.
  name: Airthings Organizations API
  slug: airthings-organizations-api
- baseURL: https://ext-api.airthings.com
  baseurl_source: declared
  description: The Segments API from Airthings — 8 operation(s) for segments.
  name: Airthings Segments API
  slug: airthings-segments-api
- baseURL: https://ext-api.airthings.com
  baseurl_source: declared
  description: The Sensor API from Airthings — 1 operation(s) for sensor.
  name: Airthings Sensor API
  slug: airthings-sensor-api
- baseURL: https://ext-api.airthings.com
  baseurl_source: declared
  description: The Spaces API from Airthings — 1 operation(s) for spaces.
  name: Airthings Spaces API
  slug: airthings-spaces-api
- baseURL: https://ext-api.airthings.com
  baseurl_source: declared
  description: The Thresholds API from Airthings — 1 operation(s) for thresholds.
  name: Airthings Thresholds API
  slug: airthings-thresholds-api
- baseURL: https://ext-api.airthings.com
  baseurl_source: declared
  description: The Webhooks API from Airthings — 2 operation(s) for webhooks.
  name: Airthings Webhooks API
  slug: airthings-webhooks-api
artifact_total: 22
common:
- group: auth
  href: https://artifacts.apis.io/airthings/well-known/airthings-airthings-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/airthings-airthings-security.txt
- group: agent
  href: https://artifacts.apis.io/airthings/agentic-access/airthings-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/airthings-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/airthings/plans/airthings-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/airthings-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/airthings/rules/airthings-rules.yml
  title: ''
  type: Spectral
  url: rules/airthings-rules.yml
- group: design
  href: https://artifacts.apis.io/airthings/json-ld/airthings-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/airthings-context.jsonld
- group: design
  href: https://artifacts.apis.io/airthings/vocabulary/airthings-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/airthings-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/airthings/data-model/airthings-data-model.yml
  title: ''
  type: DataModel
  url: data-model/airthings-data-model.yml
- group: auth
  title: ''
  type: Security
  url: https://magento.com/security
- group: design
  href: https://artifacts.apis.io/airthings/errors/airthings-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/airthings-problem-types.yml
- group: design
  href: https://artifacts.apis.io/airthings/conformance/airthings-conformance.yml
  title: ''
  type: Conformance
  url: conformance/airthings-conformance.yml
- group: agent
  href: https://artifacts.apis.io/airthings/llms/airthings-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/airthings-llms.txt
- group: auth
  href: https://artifacts.apis.io/airthings/well-known/airthings-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/airthings-www-security.txt
- group: auth
  href: https://artifacts.apis.io/airthings/well-known/airthings-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/airthings-security.txt
- group: auth
  href: https://artifacts.apis.io/airthings/well-known/airthings-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/airthings-help-security.txt
- group: auth
  href: https://artifacts.apis.io/airthings/well-known/airthings-businesshelp-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/airthings-businesshelp-security.txt
- group: agent
  href: https://artifacts.apis.io/airthings/well-known/airthings-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/airthings-well-known.yml
- group: other
  href: https://artifacts.apis.io/airthings/hosts/airthings-hosts.yml
  title: ''
  type: Hosts
  url: hosts/airthings-hosts.yml
- group: other
  href: https://artifacts.apis.io/airthings/vendors/airthings-vendors.yml
  title: ''
  type: Vendors
  url: vendors/airthings-vendors.yml
- group: build
  href: https://artifacts.apis.io/airthings/packages/airthings-packages.yml
  title: ''
  type: SDKs
  url: packages/airthings-packages.yml
- group: build
  href: https://artifacts.apis.io/airthings/packages/airthings-packages.yml
  title: ''
  type: Packages
  url: packages/airthings-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.airthings.com/legal/terms-of-use
- group: operate
  title: ''
  type: Support
  url: https://help.airthings.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.airthings.com/legal/privacy-notice
- group: company
  title: ''
  type: Newsroom
  url: https://www.airthings.com/newsroom
- group: start
  title: ''
  type: Login
  url: https://www.airthings.com/sso/account/login/
- group: company
  title: ''
  type: Blog
  url: https://www.airthings.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://help.airthings.com/en/articles/3668912-dashboard-getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://developer.airthings.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Airthings
- group: auth
  href: https://artifacts.apis.io/airthings/scopes/airthings-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/airthings-scopes.yml
- group: auth
  href: https://artifacts.apis.io/airthings/authentication/airthings-authentication.yml
  title: ''
  type: Authentication
  url: authentication/airthings-authentication.yml
- group: auth
  href: https://artifacts.apis.io/airthings/security/airthings-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/airthings-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/airthings/security/airthings-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/airthings-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://airthings.com/
created: '2026-10-28'
description: Airthings provides smart indoor air quality and radon monitoring solutions. Their products include wireless sensors that track radon, CO₂, temperature, humidity, and VOCs, delivering real‑time data via a cloud platform and mobile apps. The company focuses on improving indoor health for homes, workplaces, and schools, offering insights, alerts, and historical trends to help users maintain safe air quality.
image: https://www.airthings.com/media/og_image/default/airthings.com_1_1__1.png
json_schemas:
- name: AccountsResponse
  property_count: 1
  slug: airthings-accounts-response
- name: DevicesResponse
  property_count: 1
  slug: airthings-devices-response
- name: SensorsResponse
  property_count: 4
  slug: airthings-sensors-response
jsonld:
- class_count: 80
  name: Airthings Context
  property_count: 121
  slug: airthings-context
layout: provider
modified: '2026-10-28'
name: Airthings
nav: Providers
network: true
overview: 'Airthings publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Device API, Devices API, and 8 more. Tagged areas include Company, AirQuality, Radon, Sensors, and IoT.


  The Airthings catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Airthings'' developer surface includes support, engineering blog, getting-started guide, documentation, authentication, and 29 more developer resources.'
plans:
- name: Airthings Plans Pricing
  plan_count: 1
  slug: airthings-plans-pricing
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: Airthings API Rules
  rule_count: 16
  severity_counts:
    error: 9
    hint: 0
    info: 4
    warn: 3
  slug: airthings-rules
scopes:
- name: Airthings Scopes
  scope_count: 2
  slug: airthings-scopes
  summary_line: 2 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 53.4
  coverage:
    artifact_dirs: 21
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 55.3
    contract_governance: 35.6
    contract_quality: 63.6
    developer_ergonomics: 47.6
    discoverability: 67.9
    operational_transparency: 15.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 63.6
      total: 11
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 40.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Airthings Authentication
  slug: airthings-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Airthings Domain Security
  slug: airthings-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Airthings Vulnerability Disclosure
  slug: airthings-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: airthings
tags:
- Company
- AirQuality
- Radon
- Sensors
- IoT
website: https://airthings.com/
---
