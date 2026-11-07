---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
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
  band: agent-ready
  band_gated_from: agent-native
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 42.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Dnsdoctor Dev Agentic Access
  operation_count: 23
  slug: dnsdoctor-dev-agentic-access
  summary_line: 23 operations · 14 acting
api_count: 1
apis:
- baseURL: https://dnsdoctor.dev/api/v1
  baseurl_source: declared
  description: The domains API from DNS Doctor — 5 operation(s) for domains.
  name: DNS Doctor Domains API
  slug: dnsdoctor-dev-domains-api
- baseURL: https://dnsdoctor.dev/api/v1
  baseurl_source: declared
  description: The monitoring API from DNS Doctor — 4 operation(s) for monitoring.
  name: DNS Doctor Monitoring API
  slug: dnsdoctor-dev-monitoring-api
- baseURL: https://dnsdoctor.dev/api/v1
  baseurl_source: declared
  description: The scan API from DNS Doctor — 5 operation(s) for scan.
  name: DNS Doctor Scan API
  slug: dnsdoctor-dev-scan-api
- baseURL: https://dnsdoctor.dev/api/v1
  baseurl_source: declared
  description: The tools API from DNS Doctor — 3 operation(s) for tools.
  name: DNS Doctor Tools API
  slug: dnsdoctor-dev-tools-api
- baseURL: https://dnsdoctor.dev/api/v1
  baseurl_source: declared
  description: The watch API from DNS Doctor — 5 operation(s) for watch.
  name: DNS Doctor Watch API
  slug: dnsdoctor-dev-watch-api
artifact_total: 20
common:
- group: agent
  href: https://artifacts.apis.io/dnsdoctor-dev/agentic-access/dnsdoctor-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/dnsdoctor-dev-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/dnsdoctor-dev/plans/dnsdoctor-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dnsdoctor-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/dnsdoctor-dev/rules/dnsdoctor-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/dnsdoctor-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/dnsdoctor-dev/json-ld/dnsdoctor-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dnsdoctor-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/dnsdoctor-dev/vocabulary/dnsdoctor-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dnsdoctor-dev-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/dnsdoctor-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/dnsdoctor-dev/data-model/dnsdoctor-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dnsdoctor-dev-data-model.yml
- group: auth
  href: https://artifacts.apis.io/dnsdoctor-dev/security/dnsdoctor-dev-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/dnsdoctor-dev-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/dnsdoctor-dev/errors/dnsdoctor-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dnsdoctor-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/dnsdoctor-dev/conformance/dnsdoctor-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dnsdoctor-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dnsdoctor-dev/llms/dnsdoctor-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dnsdoctor-dev-llms.txt
- group: auth
  href: https://artifacts.apis.io/dnsdoctor-dev/well-known/dnsdoctor-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dnsdoctor-dev-security.txt
- group: agent
  href: https://artifacts.apis.io/dnsdoctor-dev/well-known/dnsdoctor-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dnsdoctor-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/dnsdoctor-dev/hosts/dnsdoctor-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dnsdoctor-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/dnsdoctor-dev/vendors/dnsdoctor-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dnsdoctor-dev-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://dnsdoctor.dev/scan/vanta.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dnsdoctor.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dnsdoctor.dev/privacy
- group: docs
  title: ''
  type: APIReference
  url: https://dnsdoctor.dev/api/v1/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dnsdoctor
- group: auth
  href: https://artifacts.apis.io/dnsdoctor-dev/authentication/dnsdoctor-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dnsdoctor-dev-authentication.yml
- group: auth
  href: https://artifacts.apis.io/dnsdoctor-dev/security/dnsdoctor-dev-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/dnsdoctor-dev-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/dnsdoctor-dev/security/dnsdoctor-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dnsdoctor-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dnsdoctor.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://dnsdoctor.dev/learn
- group: commercial
  title: ''
  type: Pricing
  url: https://dnsdoctor.dev/pricing
- group: start
  title: ''
  type: SignUp
  url: https://dnsdoctor.dev/login
created: '2026-11-05'
description: DNS Doctor provides a free DNS scanner and tools for domains, offering deterministic copy‑paste fixes for email authentication (SPF, DMARC, DKIM), MX, DNS health, blacklist checks, SSL expiry, global propagation, and reverse DNS lookups. It aims to help users quickly identify and resolve DNS issues without requiring sign‑up or payment.
image: https://dnsdoctor.dev/opengraph-image?e11df9e033a19390
json_schemas:
- name: DmarcUpgradeOut
  property_count: 7
  slug: dnsdoctor-dev-dmarc-upgrade-out
- name: ReadinessOut
  property_count: 16
  slug: dnsdoctor-dev-readiness-out
- name: ScanReportOut
  property_count: 12
  slug: dnsdoctor-dev-scan-report-out
- name: WatchCreated
  property_count: 13
  slug: dnsdoctor-dev-watch-created
- name: WatchPropagationIn
  property_count: 4
  slug: dnsdoctor-dev-watch-propagation-in
- name: WatchStatus
  property_count: 12
  slug: dnsdoctor-dev-watch-status
jsonld:
- class_count: 73
  name: Dnsdoctor Dev Context
  property_count: 213
  slug: dnsdoctor-dev-context
layout: provider
modified: '2026-11-05'
name: DNS Doctor
nav: Providers
network: true
overview: 'DNS Doctor publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Domains API, Monitoring API, Scan API, and 2 more. Tagged areas include DNS, DNS Tools, Email Authentication, and Web Application.


  The DNS Doctor catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  DNS Doctor''s developer surface includes API reference, authentication, documentation, pricing, signup flow, and 22 more developer resources.'
plans:
- name: Dnsdoctor Dev Plans Pricing
  plan_count: 3
  slug: dnsdoctor-dev-plans-pricing
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 99
  extends:
  - spectral:oas
  name: DNS Doctor API Rules
  rule_count: 58
  severity_counts:
    error: 48
    hint: 0
    info: 3
    warn: 7
  slug: dnsdoctor-dev-rules
score:
  band: developing
  composite: 52.8
  coverage:
    artifact_dirs: 22
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 84.2
    contract_governance: 22.0
    contract_quality: 65.8
    developer_ergonomics: 30.4
    discoverability: 57.1
    operational_transparency: 15.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Dnsdoctor Dev Authentication
  slug: dnsdoctor-dev-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Dnsdoctor Dev Domain Security
  slug: dnsdoctor-dev-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Dnsdoctor Dev Vulnerability Disclosure
  slug: dnsdoctor-dev-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 2
skills:
- name: dnsdoctor-dev-add-and-verify-domain
  slug: dnsdoctor-dev-add-and-verify-domain
- name: dnsdoctor-dev-scan-domain
  slug: dnsdoctor-dev-scan-domain
slug: dnsdoctor-dev
tags:
- DNS
- DNS Tools
- Email Authentication
- Web Application
website: https://dnsdoctor.dev/
---
