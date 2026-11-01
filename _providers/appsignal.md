---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://appsignal.com
  baseurl_source: declared
  description: 'AppSignal API as documented publicly: 16 operations. Contract generated from the documentation by API Evangelist (2026-10-27); not the provider''s own document.'
  name: AppSignal API
  slug: appsignal-api
artifact_total: 12
common:
- group: commercial
  href: https://artifacts.apis.io/appsignal/plans/appsignal-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/appsignal-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/appsignal/rules/appsignal-rules.yml
  title: ''
  type: Spectral
  url: rules/appsignal-rules.yml
- group: design
  href: https://artifacts.apis.io/appsignal/json-ld/appsignal-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/appsignal-context.jsonld
- group: design
  href: https://artifacts.apis.io/appsignal/vocabulary/appsignal-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/appsignal-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/appsignal/data-model/appsignal-data-model.yml
  title: ''
  type: DataModel
  url: data-model/appsignal-data-model.yml
- group: build
  href: https://artifacts.apis.io/appsignal/cli/appsignal-cli.yml
  title: ''
  type: CLI
  url: cli/appsignal-cli.yml
- group: operate
  href: https://artifacts.apis.io/appsignal/changelog/appsignal-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/appsignal-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.appsignal.com/security
- group: design
  href: https://artifacts.apis.io/appsignal/conformance/appsignal-conformance.yml
  title: ''
  type: Conformance
  url: conformance/appsignal-conformance.yml
- group: agent
  href: https://artifacts.apis.io/appsignal/llms/appsignal-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/appsignal-llms.txt
- group: other
  href: https://artifacts.apis.io/appsignal/a2a/appsignal-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/appsignal-a2a.yml
- group: agent
  href: https://artifacts.apis.io/appsignal/well-known/appsignal-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/appsignal-well-known.yml
- group: other
  href: https://artifacts.apis.io/appsignal/hosts/appsignal-hosts.yml
  title: ''
  type: Hosts
  url: hosts/appsignal-hosts.yml
- group: other
  href: https://artifacts.apis.io/appsignal/vendors/appsignal-vendors.yml
  title: ''
  type: Vendors
  url: vendors/appsignal-vendors.yml
- group: build
  href: https://artifacts.apis.io/appsignal/packages/appsignal-packages.yml
  title: ''
  type: SDKs
  url: packages/appsignal-packages.yml
- group: build
  href: https://artifacts.apis.io/appsignal/packages/appsignal-packages.yml
  title: ''
  type: Packages
  url: packages/appsignal-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.appsignal.com/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://status.appsignal.com/
- group: auth
  title: ''
  type: Security
  url: https://www.appsignal.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.appsignal.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/appsignal
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.appsignal.com/changelog
- group: auth
  href: https://artifacts.apis.io/appsignal/security/appsignal-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/appsignal-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/appsignal/security/appsignal-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/appsignal-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.appsignal.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.appsignal.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.appsignal.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.appsignal.com/getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://www.appsignal.com/plans
- group: company
  title: ''
  type: Blog
  url: https://blog.appsignal.com
- group: operate
  title: ''
  type: Support
  url: https://www.appsignal.com/contact
coverage:
  checked: '2026-10-27'
  detail: Docs are served as static markdown via llms.txt with no OpenAPI or other machine‑readable contract.
  evidence:
  - status: 308
    url: https://docs.appsignal.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: AppSignal provides error tracking, performance monitoring, and host monitoring for modern applications. It offers features like anomaly detection, uptime monitoring, metric dashboards, log management, and distributed tracing across multiple languages including Ruby, Elixir, Node.js, Python, Go, Java, PHP, and Rust. The platform integrates with OpenTelemetry and supports deployment on Vercel, Kubernetes, and AWS CloudWatch, catering to startups, enterprises, and regulated industries with HIPAA compliance and long‑term log storage options.
image: https://www.appsignal.com/api/v2/og?title=Application%20Monitoring%20for%20Ruby%20on%20Rails%2C%20Elixir%2C%20Node.js
json_schemas:
- name: GetApiAppIdMarkersJsonResponse
  property_count: 2
  slug: appsignal-get-api-app-id-markers-json-response
- name: PostApiAppIdMarkersJsonRequest
  property_count: 1
  slug: appsignal-post-api-app-id-markers-json-request
- name: PostApiAppIdMarkersJsonResponse
  property_count: 1
  slug: appsignal-post-api-app-id-markers-json-response
- name: PostApiSourcemapsRequest
  property_count: 6
  slug: appsignal-post-api-sourcemaps-request
- name: PostApiSourcemapsResponse
  property_count: 1
  slug: appsignal-post-api-sourcemaps-response
- name: PostMainAbc123JsResponse
  property_count: 1
  slug: appsignal-post-main-abc123-js-response
jsonld:
- class_count: 6
  name: Appsignal Context
  property_count: 9
  slug: appsignal-context
layout: provider
modified: '2026-10-27'
name: AppSignal
nav: Providers
network: true
overview: 'AppSignal is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Monitoring, ErrorTracking, Performance, Observability, and SaaS.


  The AppSignal catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AppSignal''s developer surface includes CLI, changelog, documentation, API reference, getting-started guide, pricing, engineering blog, and 24 more developer resources.'
plans:
- name: Appsignal Plans Pricing
  plan_count: 4
  slug: appsignal-plans-pricing
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: AppSignal API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: appsignal-rules
score:
  band: developing
  composite: 50.7
  coverage:
    artifact_dirs: 20
    catalog_earned: 71.8
    catalog_earned_first_party: 12.0
    catalog_gap: 43.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 78.9
    contract_governance: 35.6
    contract_quality: 22.9
    developer_ergonomics: 50.0
    discoverability: 66.1
    operational_transparency: 47.4
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 13
      marker_coverage: 100.0
      total: 13
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Appsignal Domain Security
  slug: appsignal-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Appsignal Trust Center
  slug: appsignal-trust-center
  summary_line: ISO 27001, HIPAA, GDPR
slug: appsignal
tags:
- Monitoring
- ErrorTracking
- Performance
- Observability
- SaaS
website: https://www.appsignal.com/
---
