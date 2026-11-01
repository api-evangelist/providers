---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 37.6
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 97
  human_in_the_loop: 12
  name: Easee Agentic Access
  operation_count: 175
  slug: easee-agentic-access
  summary_line: 175 operations · 97 acting · 12 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.easee.com
  baseurl_source: declared
  description: Sign in, refresh tokens and manage the logged-in account.
  name: Easee Account API
  slug: easee-account-api
- baseURL: https://api.easee.com
  baseurl_source: declared
  description: Start charging on a charger.
  name: Easee Authorize Charging API
  slug: easee-authorizecharging-api
- baseURL: https://api.easee.com
  baseurl_source: declared
  description: Latest, ongoing and historical charging sessions for a charger.
  name: Easee Charge Session API
  slug: easee-charge-session-api
- baseURL: https://api.easee.com
  baseurl_source: declared
  description: Read, configure and control chargers.
  name: Easee Charger API
  slug: easee-charger-api
- baseURL: https://api.easee.com
  baseurl_source: declared
  description: Configure Cloud OCPP settings and custom endpoints for operators.
  name: Easee Cloud OCPP API
  slug: easee-cloud-ocpp-api
- baseURL: https://api.easee.com
  baseurl_source: declared
  description: Charge at the same times every day.
  name: Easee Daily schedule API
  slug: easee-daily-schedule-api
- baseURL: https://api.easee.com
  baseurl_source: declared
  description: Start charging after a delay.
  name: Easee Delayed schedule API
  slug: easee-delayed-schedule-api
- baseURL: https://api.easee.com
  baseurl_source: declared
  description: Operators manage direct OCPP connections on their chargers and sites.
  name: Easee Direct OCPP - For Operators API
  slug: easee-direct-ocpp-for-operators-api
- baseURL: https://api.easee.com
  baseurl_source: declared
  description: Users manage direct OCPP on their own chargers.
  name: Easee Direct OCPP - For Users API
  slug: easee-direct-ocpp-for-users-api
- baseURL: https://api.easee.com
  baseurl_source: declared
  description: Manage Easee keys linked to an account.
  name: Easee Easee Keys API
  slug: easee-easeekeys-api
- baseURL: https://api.easee.com
  baseurl_source: declared
  description: Lifetime energy measurements for chargers, hourly to yearly.
  name: Easee Energy Reporting API
  slug: easee-energy-reporting-api
- baseURL: https://api.easee.com
  baseurl_source: declared
  description: Read and manage equalizers.
  name: Easee Equalizer API
  slug: easee-equalizer-api
- baseURL: https://api.easee.com
  baseurl_source: declared
  description: Observations reported by devices.
  name: Easee Observations API
  slug: easee-observations-api
- baseURL: https://api.easee.com
  baseurl_source: declared
  description: Reference data such as countries and currencies.
  name: Easee Resources API
  slug: easee-resources-api
- baseURL: https://api.easee.com
  baseurl_source: declared
  description: Read and manage sites.
  name: Easee Site API
  slug: easee-site-api
- baseURL: https://api.easee.com
  baseurl_source: declared
  description: Energy usage, cost and sessions for a site.
  name: Easee Site Charge Session API
  slug: easee-site-charge-session-api
- baseURL: https://api.easee.com
  baseurl_source: declared
  description: Read the active scheduling state of a charger.
  name: Easee State API
  slug: easee-state-api
- baseURL: https://api.easee.com
  baseurl_source: declared
  description: Charge at set times for each day of the week.
  name: Easee Weekly schedule API
  slug: easee-weekly-schedule-api
artifact_total: 28
common:
- group: agent
  href: https://artifacts.apis.io/easee/agentic-access/easee-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/easee-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/easee/rules/easee-rules.yml
  title: ''
  type: Spectral
  url: rules/easee-rules.yml
- group: design
  href: https://artifacts.apis.io/easee/json-ld/easee-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/easee-context.jsonld
- group: design
  href: https://artifacts.apis.io/easee/vocabulary/easee-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/easee-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/easee/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/easee/data-model/easee-data-model.yml
  title: ''
  type: DataModel
  url: data-model/easee-data-model.yml
- group: auth
  href: https://artifacts.apis.io/easee/authentication/easee-authentication.yml
  title: ''
  type: Authentication
  url: authentication/easee-authentication.yml
- group: design
  href: https://artifacts.apis.io/easee/errors/easee-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/easee-problem-types.yml
- group: design
  href: https://artifacts.apis.io/easee/conformance/easee-conformance.yml
  title: ''
  type: Conformance
  url: conformance/easee-conformance.yml
- group: agent
  href: https://artifacts.apis.io/easee/llms/easee-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/easee-llms.txt
- group: auth
  href: https://artifacts.apis.io/easee/well-known/easee-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/easee-status-security.txt
- group: agent
  href: https://artifacts.apis.io/easee/well-known/easee-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/easee-well-known.yml
- group: other
  href: https://artifacts.apis.io/easee/hosts/easee-hosts.yml
  title: ''
  type: Hosts
  url: hosts/easee-hosts.yml
- group: other
  href: https://artifacts.apis.io/easee/vendors/easee-vendors.yml
  title: ''
  type: Vendors
  url: vendors/easee-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://easee.com/en/terms/
- group: operate
  title: ''
  type: Support
  url: https://support.easee.com/hc/en-gb
- group: operate
  title: ''
  type: StatusPage
  url: https://status.easee.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://easee.com/en/privacy/
- group: company
  title: ''
  type: Newsroom
  url: https://easee.com/sv/om-oss/press/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.easee.com/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.easee.com/docs/onboarding-introduction
- group: docs
  title: ''
  type: Documentation
  url: https://developer.easee.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.easee.com/reference/open-api-specification.md
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/easee
- group: auth
  href: https://artifacts.apis.io/easee/security/easee-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/easee-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://easee.com/
created: '2026-10-27'
description: Easee provides smart electric vehicle (EV) charging solutions, offering Wi‑Fi‑enabled, app‑controlled home and commercial chargers that optimize charging speed, energy usage, and integration with renewable sources. Their platform includes a cloud‑based dashboard for monitoring, scheduling, and firmware updates, as well as APIs for third‑party integration, enabling developers to retrieve charger status, control charging sessions, and manage user access across multiple locations.
image: https://easee.com/wp-content/uploads/2026/03/mnmt_15_plugged-e1773234476872.webp
jsonld:
- class_count: 120
  name: Easee Context
  property_count: 260
  slug: easee-context
layout: provider
modified: '2026-10-27'
name: Easee
nav: Providers
network: true
overview: 'Easee publishes 18 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Authorize Charging API, Charge Session API, and 15 more. Tagged areas include Company, EVCharging, SmartHome, IoT, and Energy.


  The Easee catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Easee''s developer surface includes authentication, support, changelog, getting-started guide, documentation, API reference, and 20 more developer resources.'
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Easee API Rules
  rule_count: 13
  severity_counts:
    error: 10
    hint: 0
    info: 2
    warn: 1
  slug: easee-rules
score:
  band: developing
  composite: 43.3
  coverage:
    artifact_dirs: 17
    catalog_earned: 48.8
    catalog_earned_first_party: 0.0
    catalog_gap: 66.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 55.5
    developer_ergonomics: 47.0
    discoverability: 58.9
    operational_transparency: 47.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 18
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 20.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Easee Authentication
  slug: easee-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Easee Domain Security
  slug: easee-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
skill_count: 5
skills:
- name: easee-apply-ocpp-connection-to-charger
  slug: easee-apply-ocpp-connection-to-charger
- name: easee-get-charger-info
  slug: easee-get-charger-info
- name: easee-get-site-chargers
  slug: easee-get-site-chargers
- name: easee-manage-charger-favorites
  slug: easee-manage-charger-favorites
- name: easee-manage-direct-ocpp-connection
  slug: easee-manage-direct-ocpp-connection
slug: easee
tags:
- Company
- EVCharging
- SmartHome
- IoT
- Energy
website: https://easee.com/
---
