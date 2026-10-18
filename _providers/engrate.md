---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 61.3
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Engrate Agentic Access
  operation_count: 54
  slug: engrate-agentic-access
  summary_line: 54 operations · 9 acting
api_count: 2
apis:
- baseURL: https://api.engrate.io
  baseurl_source: declared
  description: The audit-logs API from Engrate — 1 operation(s) for audit-logs.
  name: Engrate Audit Logs API
  slug: engrate-audit-logs-api
- baseURL: https://api.engrate.io
  baseurl_source: declared
  description: Abonnement von Änderungsereignissen.
  name: Engrate Benachrichtigung API
  slug: engrate-benachrichtigung-api
- baseURL: https://api.engrate.io
  baseurl_source: declared
  description: Umsetzungsstand und Betriebsinformationen.
  name: Engrate Betrieb API
  slug: engrate-betrieb-api
- baseURL: https://api.engrate.io
  baseurl_source: declared
  description: Abweichende Sichtweisen als Vorgang mit definiertem Endzustand.
  name: Engrate Clearing API
  slug: engrate-clearing-api
- baseURL: https://api.engrate.io
  baseurl_source: declared
  description: The Core API from Engrate — 5 operation(s) for core.
  name: Engrate Core API
  slug: engrate-core-api
- baseURL: https://api.engrate.io
  baseurl_source: declared
  description: The Cost Of Energy API from Engrate — 5 operation(s) for cost of energy.
  name: Engrate Cost Of Energy API
  slug: engrate-cost-of-energy-api
- baseURL: https://api.engrate.io
  baseurl_source: declared
  description: The geo API from Engrate — 1 operation(s) for geo.
  name: Engrate Geo API
  slug: engrate-geo-api
- baseURL: https://api.engrate.io
  baseurl_source: declared
  description: The holidays API from Engrate — 1 operation(s) for holidays.
  name: Engrate Holidays API
  slug: engrate-holidays-api
- baseURL: https://api.engrate.io
  baseurl_source: declared
  description: Einzelressourcen der referenzierten Netz-, Markt- und Messlokationen.
  name: Engrate Lokationen API
  slug: engrate-lokationen-api
- baseURL: https://api.engrate.io
  baseurl_source: declared
  description: Abruf und Pflege von Lokationsbündeln in der Hoheit des Netzbetreibers.
  name: Engrate Lokationsbündel API
  slug: engrate-lokationsb-ndel-api
- baseURL: https://api.engrate.io
  baseurl_source: declared
  description: The mabis API from Engrate — 13 operation(s) for mabis.
  name: Engrate Mabis API
  slug: engrate-mabis-api
- baseURL: https://api.engrate.io
  baseurl_source: declared
  description: Übergabepaket beim Wechsel des zuständigen Netzbetreibers.
  name: Engrate Netzbetreiberwechsel API
  slug: engrate-netzbetreiberwechsel-api
- baseURL: https://api.engrate.io
  baseurl_source: declared
  description: The nl-settlement API from Engrate — 4 operation(s) for nl-settlement.
  name: Engrate Nl Settlement API
  slug: engrate-nl-settlement-api
- baseURL: https://api.engrate.io
  baseurl_source: declared
  description: The profiles API from Engrate — 2 operation(s) for profiles.
  name: Engrate Profiles API
  slug: engrate-profiles-api
- baseURL: https://api.engrate.io
  baseurl_source: declared
  description: The reference API from Engrate — 2 operation(s) for reference.
  name: Engrate Reference API
  slug: engrate-reference-api
- baseURL: https://api.engrate.io
  baseurl_source: declared
  description: The schedules API from Engrate — 10 operation(s) for schedules.
  name: Engrate Schedules API
  slug: engrate-schedules-api
- baseURL: https://api.engrate.io
  baseurl_source: declared
  description: The status-request API from Engrate — 1 operation(s) for status-request.
  name: Engrate Status Request API
  slug: engrate-status-request-api
- baseURL: https://api.engrate.io
  baseurl_source: declared
  description: The Time Series API from Engrate — 3 operation(s) for time series.
  name: Engrate Time Series API
  slug: engrate-time-series-api
artifact_total: 35
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/engrate/refs/heads/main/agentic-access/engrate-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/engrate-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/engrate/refs/heads/main/rules/engrate-rules.yml
  title: ''
  type: Spectral
  url: rules/engrate-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/engrate/refs/heads/main/json-ld/engrate-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/engrate-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/engrate/refs/heads/main/vocabulary/engrate-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/engrate-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/engrate/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/engrate/refs/heads/main/data-model/engrate-data-model.yml
  title: ''
  type: DataModel
  url: data-model/engrate-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/engrate/refs/heads/main/changelog/engrate-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/engrate-changelog.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/engrate/refs/heads/main/authentication/engrate-authentication.yml
  title: ''
  type: Authentication
  url: authentication/engrate-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/engrate/refs/heads/main/errors/engrate-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/engrate-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/engrate/refs/heads/main/conformance/engrate-conformance.yml
  title: ''
  type: Conformance
  url: conformance/engrate-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/engrate/refs/heads/main/llms/engrate-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/engrate-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/engrate/refs/heads/main/a2a/engrate-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/engrate-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/engrate/refs/heads/main/well-known/engrate-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/engrate-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/engrate/refs/heads/main/hosts/engrate-hosts.yml
  title: ''
  type: Hosts
  url: hosts/engrate-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/engrate/refs/heads/main/vendors/engrate-vendors.yml
  title: ''
  type: Vendors
  url: vendors/engrate-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/engrate/refs/heads/main/packages/engrate-packages.yml
  title: ''
  type: SDKs
  url: packages/engrate-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/engrate/refs/heads/main/packages/engrate-packages.yml
  title: ''
  type: Packages
  url: packages/engrate-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.engrate.io/changelog/product-updates
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/engrate
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/engrate/refs/heads/main/security/engrate-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/engrate-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://engrate.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.engrate.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://console.engrate.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.engrate.io/api-reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.engrate.io/guides/welcome
- group: commercial
  title: ''
  type: TermsOfService
  url: https://engrate.io/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://engrate.io/legal/privacy-policy
created: '2026-10-15'
description: Engrate provides a unified platform for energy market communication, enabling balance responsible parties and suppliers to integrate with multiple energy markets through a single API. The solution abstracts diverse market protocols, message formats, identifiers, and deadlines, allowing seamless asset trading across bidding zones. By offering a comprehensive market communication layer, Engrate reduces integration complexity, accelerates time‑to‑market, and supports cost‑of‑energy analysis, documentation, and developer tools. Book a demo or explore the docs to learn how Engrate simplifies energy market interactions.
image: https://engrate.io/og/home.png
json_schemas:
- name: ClearingCaseWrite
  property_count: 4
  slug: engrate-clearing-case-write
- name: ClearingPeriodResponse
  property_count: 12
  slug: engrate-clearing-period-response
- name: ImplementationStatus
  property_count: 3
  slug: engrate-implementation-status
- name: MarketLocationDocument
  property_count: 2
  slug: engrate-market-location-document
- name: MeteringLocationDocument
  property_count: 2
  slug: engrate-metering-location-document
- name: NetworkLocationDocument
  property_count: 2
  slug: engrate-network-location-document
- name: ObjectionResponse
  property_count: 11
  slug: engrate-objection-response
- name: ScheduleSeriesResponse
  property_count: 9
  slug: engrate-schedule-series-response
- name: ScheduleVersionResponse
  property_count: 14
  slug: engrate-schedule-version-response
- name: SimplifiedTariffResponse
  property_count: 3
  slug: engrate-simplified-tariff-response
- name: SubscriptionWrite
  property_count: 3
  slug: engrate-subscription-write
- name: Tariff
  property_count: 8
  slug: engrate-tariff
jsonld:
- class_count: 120
  name: Engrate Context
  property_count: 224
  slug: engrate-context
layout: provider
modified: '2026-10-15'
name: Engrate
nav: Providers
network: true
overview: 'Engrate publishes 18 API contracts indexed on the [APIs.io](https://apis.io/) network, including Audit Logs API, Benachrichtigung API, Betrieb API, and 15 more. Tagged areas include Company, Energy, Platform, Integration, and Markets.


  The Engrate catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Engrate''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, and 22 more developer resources.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Engrate API Rules
  rule_count: 13
  severity_counts:
    error: 9
    hint: 0
    info: 2
    warn: 2
  slug: engrate-rules
score:
  band: developing
  composite: 45.3
  coverage:
    artifact_dirs: 22
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 65.0
    developer_ergonomics: 58.9
    discoverability: 73.2
    operational_transparency: 21.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 18
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 20.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Engrate Authentication
  slug: engrate-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Engrate Domain Security
  slug: engrate-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: engrate
tags:
- Company
- Energy
- Platform
- Integration
- Markets
website: https://engrate.io/
---
