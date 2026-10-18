---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 39.7
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 13
  human_in_the_loop: 3
  name: Trolie Agentic Access
  operation_count: 28
  slug: trolie-agentic-access
  summary_line: 28 operations · 13 acting · 3 human-in-the-loop
api_count: 2
apis:
- baseURL: https://trolie.example.com
  baseurl_source: spec
  description: The Forecasting API operations define the exchange of forecasted ratings, including the 240-hour-ahead forecasted AAR data exchange required by FERC Order 881. The operations support submitting rating
  name: TROLIE Forecasting API
  slug: trolie-forecasting-api
- baseURL: https://trolie.example.com
  baseurl_source: spec
  description: '[Monitoring Sets](https://trolie.energy/concepts#monitoring-sets) are named sets of power system resources that may be used to filter ratings and limits returned by queries against these APIs. How Mon'
  name: TROLIE Monitoring Sets API
  slug: trolie-monitoring-sets-api
- baseURL: https://trolie.example.com
  baseurl_source: spec
  description: Seasonal ratings are static ratings associated with extended durations, typically months. These are typically used in both planning and operations. Power system resources that are exempt from providin
  name: TROLIE Seasonal API
  slug: trolie-seasonal-api
- baseURL: https://trolie.example.com
  baseurl_source: spec
  description: A Seasonal Override instructs the system to use a temporary static rating instead of any concurrent Seasonal Rating for a resource. A typical use case is a so-called 'de-rate' due to a temporary clear
  name: TROLIE Seasonal Overrides API
  slug: trolie-seasonal-overrides-api
- baseURL: https://trolie.example.com
  baseurl_source: spec
  description: A [Temporary AAR Exception](https://trolie.energy/concepts#temporary-aar-exception) is provided by the Ratings Provider when a Ratings Obligation cannot be fulfilled, due to some temporary operating c
  name: TROLIE Temporary AAR Exceptions API
  slug: trolie-temporary-aar-exceptions-api
- baseURL: https://trolie.example.com
  baseurl_source: spec
  description: If permitted by the Clearinghouse Provider, its Ratings Providers can use these functions to exchange real-time ratings, supplementing or replacing traditional telemetry protocols like ICCP.
  name: TROLIE Realtime API
  slug: trolie-realtime-api
artifact_total: 26
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/trolie/refs/heads/main/agentic-access/trolie-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/trolie-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/trolie/refs/heads/main/rules/trolie-spec-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/trolie-spec-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/trolie/refs/heads/main/rules/trolie-rules.yml
  title: ''
  type: Spectral
  url: rules/trolie-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/trolie/refs/heads/main/json-ld/trolie-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/trolie-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/trolie/refs/heads/main/vocabulary/trolie-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/trolie-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/trolie/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/trolie/refs/heads/main/data-model/trolie-data-model.yml
  title: ''
  type: DataModel
  url: data-model/trolie-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/trolie/refs/heads/main/changelog/trolie-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/trolie-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/trolie/refs/heads/main/conventions/trolie-conventions.yml
  title: ''
  type: Conventions
  url: conventions/trolie-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/trolie/refs/heads/main/lifecycle/trolie-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/trolie-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/trolie/refs/heads/main/lifecycle/trolie-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/trolie-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/trolie/refs/heads/main/errors/trolie-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/trolie-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/trolie/refs/heads/main/conformance/trolie-conformance.yml
  title: ''
  type: Conformance
  url: conformance/trolie-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/trolie/refs/heads/main/overlays/trolie-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/trolie-openapi-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/trolie/refs/heads/main/well-known/trolie-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/trolie-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/trolie/refs/heads/main/hosts/trolie-hosts.yml
  title: ''
  type: Hosts
  url: hosts/trolie-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/trolie/refs/heads/main/vendors/trolie-vendors.yml
  title: ''
  type: Vendors
  url: vendors/trolie-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/trolie/refs/heads/main/packages/trolie-packages.yml
  title: ''
  type: SDKs
  url: packages/trolie-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/trolie/refs/heads/main/packages/trolie-packages.yml
  title: ''
  type: Packages
  url: packages/trolie-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/trolie/refs/heads/main/authentication/trolie-authentication.yml
  title: ''
  type: Authentication
  url: authentication/trolie-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/trolie/refs/heads/main/scopes/trolie-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/trolie-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/trolie/refs/heads/main/security/trolie-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/trolie-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://trolie.energy/
- group: design
  title: ''
  type: SpectralRules
  url: https://github.com/trolie/spec/blob/39741d03365cb430ab5d7e677312759a7f4a6d14/.spectral.yaml
- group: docs
  title: ''
  type: APIReference
  url: https://trolie.energy/spec-1.0
- group: start
  title: ''
  type: GettingStarted
  url: https://trolie.energy/concepts.html
- group: build
  title: ''
  type: UsageExamples
  url: https://trolie.energy/usage-examples.html
- group: operate
  title: ''
  type: FAQ
  url: https://trolie.energy/faq.html
- group: company
  title: ''
  type: Blog
  url: https://trolie.energy/community_events.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/trolie
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/TROLIE/spec
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/trolie/spec/releases
- group: operate
  title: ''
  type: Issues
  url: https://github.com/trolie/spec/issues
- group: operate
  title: ''
  type: Support
  url: https://lists.lfenergy.org/g/trolie-general
- group: other
  title: ''
  type: Foundation
  url: https://lfenergy.org/projects/trolie/
created: '2026-10-09'
description: TROLIE (Transmission Ratings and Operating Limits Information Exchange) is an open-source LF Energy project, hosted under LF Projects, that defines an OpenAPI-based REST specification for exchanging transmission facility ratings and operating limits. It responds to FERC Order 881, which requires North American Transmission Owners, Transmission Operators, Transmission Providers and Reliability Coordinators to exchange ambient-adjusted and forecasted ratings. The project publishes the 1.0 specification, usage examples for forecast, real-time, seasonal and temporary ratings, decision records, a conformance suite and a Java client SDK on GitHub.
examples:
- key_count: 4
  name: Trolie Rc A Monitoring Set
  slug: trolie-RC-A-monitoring-set
- key_count: 4
  name: Trolie Rc B Monitoring Set
  slug: trolie-RC-B-monitoring-set
- key_count: 4
  name: Trolie Compression Required
  slug: trolie-compression-required
- key_count: 4
  name: Trolie Forecast Proposal Late
  slug: trolie-forecast-proposal-late
- key_count: 4
  name: Trolie Proposal Invalid Units
  slug: trolie-proposal-invalid-units
image: https://trolie.energy/images/TROLIE-icon-white.svg
json_schemas:
- name: forecast-limits-snapshot-slim-inputs-used
  property_count: 3
  slug: trolie-forecast-limits-snapshot-slim-inputs-used
- name: forecast-proposal-status
  property_count: 6
  slug: trolie-forecast-proposal-status
- name: real-time-proposal-status
  property_count: 5
  slug: trolie-real-time-proposal-status
- name: realtime-limits-snapshot-slim-inputs-used
  property_count: 3
  slug: trolie-realtime-limits-snapshot-slim-inputs-used
- name: realtime-proposal
  property_count: 3
  slug: trolie-realtime-proposal
- name: seasonal-ratings-proposal-status
  property_count: 5
  slug: trolie-seasonal-ratings-proposal-status
jsonld:
- class_count: 81
  name: Trolie Context
  property_count: 57
  slug: trolie-context
layout: provider
modified: '2026-10-09'
name: TROLIE
nav: Providers
network: true
overview: 'TROLIE publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Forecasting API, Monitoring Sets API, Seasonal API, and 3 more. Tagged areas include Company, Energy, Electric Grid, Transmission, and Open Standard.


  The TROLIE catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  TROLIE''s developer surface includes changelog, authentication, API reference, getting-started guide, FAQ, engineering blog, support, and 28 more developer resources.'
plans:
- name: Trolie Plans Pricing
  plan_count: 0
  slug: trolie-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Trolie Rate Limits
  slug: trolie-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: TROLIE API Rules
  rule_count: 16
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 1
  slug: trolie-rules
- authorship: provider
  effective_rule_count: 46
  extends:
  - spectral:oas
  - https://unpkg.com/@stoplight/spectral-owasp-ruleset@1.4.3/dist/ruleset.mjs
  name: TROLIE — spec rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 5
  slug: trolie-spec-spectral-rules
scopes:
- name: Trolie Scopes
  scope_count: 15
  slug: trolie-scopes
  summary_line: 15 scopes · clientCredentials
score:
  band: developing
  composite: 43.5
  coverage:
    artifact_dirs: 27
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.2
  facets:
    access_clarity: 0.0
    contract_governance: 35.6
    contract_quality: 67.7
    developer_ergonomics: 56.5
    discoverability: 57.1
    operational_transparency: 28.9
  previous_composite: 43.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 27.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/trolie/refs/heads/main/screenshots/trolie-2026-10-11T131208.png
security:
- kind: authentication
  name: Trolie Authentication
  slug: trolie-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Trolie Domain Security
  slug: trolie-domain-security
  summary_line: TLSv1.3 · HSTS
slug: trolie
tags:
- Company
- Energy
- Electric Grid
- Transmission
- Open Standard
- OpenAPI
- LF Energy
- Open Source
website: https://trolie.energy/
---
