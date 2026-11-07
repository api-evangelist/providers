---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: self
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 38.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Organisations and people in the Galactica Entity Standard v1
  name: Data Galactica API
  slug: data-galactica-api
- baseURL: https://api.datagalactica.com
  baseurl_source: declared
  description: Organisations and people in the Galactica Entity Standard v1 (https://datagalactica.com/standard), each with a permanent
  name: Data Galactica API API
  slug: data-galactica-api-api
artifact_total: 14
common:
- group: design
  href: https://artifacts.apis.io/datagalactica-com/rules/datagalactica-com-rules.yml
  title: ''
  type: Spectral
  url: rules/datagalactica-com-rules.yml
- group: design
  href: https://artifacts.apis.io/datagalactica-com/json-ld/datagalactica-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/datagalactica-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/datagalactica-com/vocabulary/datagalactica-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/datagalactica-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/datagalactica-com/conformance/datagalactica-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/datagalactica-com-conformance.yml
- group: commercial
  href: https://artifacts.apis.io/datagalactica-com/plans/datagalactica-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/datagalactica-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/datagalactica-com/data-model/datagalactica-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/datagalactica-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/datagalactica-com/conventions/datagalactica-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/datagalactica-com-conventions.yml
- group: auth
  title: ''
  type: Security
  url: https://datagalactica.com/terms
- group: auth
  href: https://artifacts.apis.io/datagalactica-com/authentication/datagalactica-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/datagalactica-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/datagalactica-com/errors/datagalactica-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/datagalactica-com-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/datagalactica-com/llms/datagalactica-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/datagalactica-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/datagalactica-com/well-known/datagalactica-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/datagalactica-com-security.txt
- group: agent
  href: https://artifacts.apis.io/datagalactica-com/well-known/datagalactica-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/datagalactica-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/datagalactica-com/hosts/datagalactica-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/datagalactica-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/datagalactica-com/vendors/datagalactica-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/datagalactica-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://datagalactica.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://datagalactica.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://datagalactica.com/people/function/media
- group: start
  title: ''
  type: Login
  url: https://datagalactica.com/login
- group: start
  title: ''
  type: GettingStarted
  url: https://datagalactica.com/blog/data-galactica-api-quickstart
- group: auth
  href: https://artifacts.apis.io/datagalactica-com/security/datagalactica-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/datagalactica-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/datagalactica-com/security/datagalactica-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/datagalactica-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://datagalactica.com/
- group: docs
  title: ''
  type: APIReference
  url: https://datagalactica.com/api/docs
- group: docs
  title: ''
  type: Documentation
  url: https://datagalactica.com/api/openapi.json
- group: company
  title: ''
  type: Blog
  url: https://datagalactica.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://datagalactica.com/pricing
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://datagalactica.com/mcp
  - status: 401
    url: https://api.datagalactica.com/mcp
  - status: 200
    url: https://datagalactica.com/
  reason: partner-login
  state: gated
created: '2026-11-04'
description: Data Galactica provides a permanent ID registry for every person and company, enabling verification, prospecting, and data enrichment across industries. The platform offers searchable databases, API access, and tools for confirming corporate identities, tracking company information, and integrating Galactica IDs into applications for reliable entity resolution.
image: https://datagalactica.com/og/home.png
json_schemas:
- name: Contribution
  property_count: 9
  slug: datagalactica-com-contribution
- name: Decision
  property_count: 6
  slug: datagalactica-com-decision
- name: Hit
  property_count: 11
  slug: datagalactica-com-hit
- name: Organization
  property_count: 34
  slug: datagalactica-com-organization
- name: Person
  property_count: 34
  slug: datagalactica-com-person
- name: Verification
  property_count: 7
  slug: datagalactica-com-verification
jsonld:
- class_count: 19
  name: Datagalactica Com Context
  property_count: 89
  slug: datagalactica-com-context
layout: provider
modified: '2026-11-04'
name: Data Galactica
nav: Providers
network: true
overview: 'Data Galactica publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including API API, and 1 more. Tagged areas include Data, Identity, Registry, and Prospecting.


  The Data Galactica catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Data Galactica''s developer surface includes authentication, getting-started guide, API reference, documentation, engineering blog, pricing, and 21 more developer resources.'
plans:
- name: Datagalactica Com Plans Pricing
  plan_count: 3
  slug: datagalactica-com-plans-pricing
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 103
  extends:
  - spectral:oas
  name: Data Galactica API Rules
  rule_count: 62
  severity_counts:
    error: 58
    hint: 0
    info: 1
    warn: 3
  slug: datagalactica-com-rules
score:
  band: developing
  composite: 48.7
  coverage:
    artifact_dirs: 20
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 50.7
    developer_ergonomics: 42.9
    discoverability: 58.9
    operational_transparency: 10.5
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Datagalactica Com Authentication
  slug: datagalactica-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Datagalactica Com Domain Security
  slug: datagalactica-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Datagalactica Com Vulnerability Disclosure
  slug: datagalactica-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: datagalactica-com
tags:
- Data
- Identity
- Registry
- Prospecting
website: https://datagalactica.com/
---
