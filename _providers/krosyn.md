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
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 44.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Krosyn Agentic Access
  operation_count: 2
  slug: krosyn-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 1
apis:
- baseURL: https://krosyn.com/api/v1
  baseurl_source: declared
  description: The Connectors API from Chmura Software — 1 operation(s) for connectors.
  name: Chmura Software Connectors API
  slug: krosyn-connectors-api
artifact_total: 10
common:
- group: agent
  href: https://artifacts.apis.io/krosyn/agentic-access/krosyn-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/krosyn-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/krosyn/plans/krosyn-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/krosyn-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/krosyn/rules/krosyn-rules.yml
  title: ''
  type: Spectral
  url: rules/krosyn-rules.yml
- group: design
  href: https://artifacts.apis.io/krosyn/json-ld/krosyn-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/krosyn-context.jsonld
- group: design
  href: https://artifacts.apis.io/krosyn/vocabulary/krosyn-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/krosyn-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/krosyn/data-model/krosyn-data-model.yml
  title: ''
  type: DataModel
  url: data-model/krosyn-data-model.yml
- group: operate
  href: https://artifacts.apis.io/krosyn/changelog/krosyn-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/krosyn-changelog.yml
- group: design
  href: https://artifacts.apis.io/krosyn/conventions/krosyn-conventions.yml
  title: ''
  type: Conventions
  url: conventions/krosyn-conventions.yml
- group: auth
  href: https://artifacts.apis.io/krosyn/authentication/krosyn-authentication.yml
  title: ''
  type: Authentication
  url: authentication/krosyn-authentication.yml
- group: design
  href: https://artifacts.apis.io/krosyn/errors/krosyn-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/krosyn-problem-types.yml
- group: design
  href: https://artifacts.apis.io/krosyn/conformance/krosyn-conformance.yml
  title: ''
  type: Conformance
  url: conformance/krosyn-conformance.yml
- group: agent
  href: https://artifacts.apis.io/krosyn/llms/krosyn-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/krosyn-llms.txt
- group: agent
  href: https://artifacts.apis.io/krosyn/well-known/krosyn-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/krosyn-well-known.yml
- group: other
  href: https://artifacts.apis.io/krosyn/hosts/krosyn-hosts.yml
  title: ''
  type: Hosts
  url: hosts/krosyn-hosts.yml
- group: other
  href: https://artifacts.apis.io/krosyn/vendors/krosyn-vendors.yml
  title: ''
  type: Vendors
  url: vendors/krosyn-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://krosyn.com/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://krosyn.com/changelog
- group: auth
  href: https://artifacts.apis.io/krosyn/security/krosyn-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/krosyn-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://krosyn.com/
- group: docs
  title: ''
  type: Documentation
  url: https://krosyn.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://krosyn.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://krosyn.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://krosyn.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://krosyn.com/blog
created: '2026-10-18'
description: Chmura Software provides a platform for building and managing cloud-native applications, offering services such as API gateways, authentication, and developer tooling. The company focuses on simplifying integration and deployment for modern software teams, with a strong emphasis on security, scalability, and developer experience.
image: https://krosyn.com/images/og-default.png
json_schemas:
- name: AsyncResponse
  property_count: 3
  slug: krosyn-async-response
- name: SkippedResponse
  property_count: 4
  slug: krosyn-skipped-response
- name: SuccessResponse
  property_count: 5
  slug: krosyn-success-response
jsonld:
- class_count: 5
  name: Krosyn Context
  property_count: 7
  slug: krosyn-context
layout: provider
modified: '2026-10-18'
name: Chmura Software
nav: Providers
network: true
overview: 'Chmura Software publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Connectors API. Tagged areas include Company, Cloud, Developer Tools, and Security.


  The Chmura Software catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Chmura Software''s developer surface includes changelog, authentication, documentation, pricing, engineering blog, and 19 more developer resources.'
plans:
- name: Krosyn Plans Pricing
  plan_count: 4
  slug: krosyn-plans-pricing
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: Chmura Software API Rules
  rule_count: 17
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 1
  slug: krosyn-rules
score:
  band: developing
  composite: 42.0
  coverage:
    artifact_dirs: 28
    catalog_earned: 66.8
    catalog_earned_first_party: 12.0
    catalog_gap: 48.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.2
  facets:
    access_clarity: 53.9
    contract_governance: 35.6
    contract_quality: 63.0
    developer_ergonomics: 17.9
    discoverability: 64.3
    operational_transparency: 7.9
  previous_composite: 49.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
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
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/krosyn/krosyn-2026-11-03T134543.png
security:
- kind: authentication
  name: Krosyn Authentication
  slug: krosyn-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Krosyn Domain Security
  slug: krosyn-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: krosyn
tags:
- Company
- Cloud
- Developer Tools
- Security
website: https://krosyn.com/
---
