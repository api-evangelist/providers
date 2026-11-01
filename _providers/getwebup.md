---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.7
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Manage your Getwebup Cloud servers from code.
  name: Getwebup Cloud API
  slug: getwebup-cloud-api
- baseURL: https://cloud.getwebup.in/api
  baseurl_source: declared
  description: 'Manage your Getwebup Cloud servers from code. Production keys (cx_live_…) act on your real account; sandbox keys (cx_test_…) on a simulated copy where nothing is built or billed. Full guide: https://c'
  name: Getwebup Cloud API V1 API
  slug: getwebup-cloud-api-v1-api
artifact_total: 9
common:
- group: design
  href: https://artifacts.apis.io/getwebup/rules/getwebup-rules.yml
  title: ''
  type: Spectral
  url: rules/getwebup-rules.yml
- group: design
  href: https://artifacts.apis.io/getwebup/json-ld/getwebup-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/getwebup-context.jsonld
- group: design
  href: https://artifacts.apis.io/getwebup/vocabulary/getwebup-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/getwebup-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/getwebup/conventions/getwebup-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/getwebup-conventions.yml
- group: auth
  title: ''
  type: Security
  url: https://www.getwebup.in/privacy.php
- group: agent
  href: https://artifacts.apis.io/getwebup/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/getwebup/data-model/getwebup-data-model.yml
  title: ''
  type: DataModel
  url: data-model/getwebup-data-model.yml
- group: design
  href: https://artifacts.apis.io/getwebup/conventions/getwebup-conventions.yml
  title: ''
  type: Conventions
  url: conventions/getwebup-conventions.yml
- group: auth
  href: https://artifacts.apis.io/getwebup/authentication/getwebup-authentication.yml
  title: ''
  type: Authentication
  url: authentication/getwebup-authentication.yml
- group: auth
  href: https://artifacts.apis.io/getwebup/scopes/getwebup-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/getwebup-scopes.yml
- group: design
  href: https://artifacts.apis.io/getwebup/errors/getwebup-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/getwebup-problem-types.yml
- group: design
  href: https://artifacts.apis.io/getwebup/conformance/getwebup-conformance.yml
  title: ''
  type: Conformance
  url: conformance/getwebup-conformance.yml
- group: agent
  href: https://artifacts.apis.io/getwebup/llms/getwebup-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/getwebup-llms.txt
- group: auth
  href: https://artifacts.apis.io/getwebup/well-known/getwebup-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/getwebup-security.txt
- group: agent
  href: https://artifacts.apis.io/getwebup/well-known/getwebup-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/getwebup-well-known.yml
- group: other
  href: https://artifacts.apis.io/getwebup/hosts/getwebup-hosts.yml
  title: ''
  type: Hosts
  url: hosts/getwebup-hosts.yml
- group: other
  href: https://artifacts.apis.io/getwebup/vendors/getwebup-vendors.yml
  title: ''
  type: Vendors
  url: vendors/getwebup-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.getwebup.in/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.getwebup.in/legal/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.getwebup.in/pricing
- group: start
  title: ''
  type: Login
  url: https://cloud.getwebup.in/login
- group: docs
  title: ''
  type: Documentation
  url: https://www.getwebup.in/docs
- group: company
  title: ''
  type: Blog
  url: https://www.getwebup.in/blog/
- group: docs
  title: ''
  type: APIReference
  url: https://www.getwebup.in/llms.txt
- group: auth
  href: https://artifacts.apis.io/getwebup/security/getwebup-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/getwebup-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/getwebup/security/getwebup-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/getwebup-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.getwebup.in/
created: '2026-10-30'
description: 'Getwebup is a company surfaced via the API Evangelist harvest backlog (source: new-submission) and added to the network as a stub for full-pipeline profiling.'
image: https://www.getwebup.in/assets/og-default.jpg
jsonld:
- class_count: 1
  name: Getwebup Context
  property_count: 1
  slug: getwebup-context
layout: provider
modified: '2026-10-30'
name: Getwebup
nav: Providers
network: true
overview: 'Getwebup publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Cloud API V1 API, and 1 more. Tagged areas include Company.


  The Getwebup catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Getwebup''s developer surface includes authentication, pricing, documentation, engineering blog, API reference, and 22 more developer resources.'
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: Getwebup API Rules
  rule_count: 18
  severity_counts:
    error: 16
    hint: 0
    info: 1
    warn: 1
  slug: getwebup-rules
scopes:
- name: Getwebup Scopes
  scope_count: 0
  slug: getwebup-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 39.8
  coverage:
    artifact_dirs: 25
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 77.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 35.6
    contract_quality: 36.7
    developer_ergonomics: 37.4
    discoverability: 48.2
    operational_transparency: 10.5
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 21
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
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
  name: Getwebup Authentication
  slug: getwebup-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Getwebup Domain Security
  slug: getwebup-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Getwebup Vulnerability Disclosure
  slug: getwebup-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: server-management
  slug: getwebup-server-management
slug: getwebup
tags:
- Company
website: https://www.getwebup.in/
---
