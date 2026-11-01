---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 35.3
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Willow API allows programmatic management of MCP servers and other resources.
  name: Willow API
  slug: willow-api
- baseURL: https://app.withwillow.ai
  baseurl_source: declared
  description: The Willow API allows you to programmatically manage MCP servers and other resources in your organization.
  name: Willow API API
  slug: willow-api-api
artifact_total: 13
common:
- group: design
  href: https://artifacts.apis.io/webrix/rules/webrix-rules.yml
  title: ''
  type: Spectral
  url: rules/webrix-rules.yml
- group: design
  href: https://artifacts.apis.io/webrix/json-ld/webrix-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/webrix-context.jsonld
- group: design
  href: https://artifacts.apis.io/webrix/vocabulary/webrix-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/webrix-vocabulary.yml
- group: auth
  href: https://artifacts.apis.io/webrix/well-known/webrix-trust-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/webrix-trust-security.txt
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://withwillow.ai/privacy-policy
- group: commercial
  href: https://artifacts.apis.io/webrix/plans/webrix-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/webrix-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/webrix/data-model/webrix-data-model.yml
  title: ''
  type: DataModel
  url: data-model/webrix-data-model.yml
- group: operate
  href: https://artifacts.apis.io/webrix/changelog/webrix-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/webrix-changelog.yml
- group: auth
  href: https://artifacts.apis.io/webrix/authentication/webrix-authentication.yml
  title: ''
  type: Authentication
  url: authentication/webrix-authentication.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.withwillow.ai/docs/developers/api-versioning
- group: design
  href: https://artifacts.apis.io/webrix/lifecycle/webrix-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/webrix-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/webrix/errors/webrix-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/webrix-problem-types.yml
- group: design
  href: https://artifacts.apis.io/webrix/conformance/webrix-conformance.yml
  title: ''
  type: Conformance
  url: conformance/webrix-conformance.yml
- group: agent
  href: https://artifacts.apis.io/webrix/llms/webrix-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/webrix-llms.txt
- group: agent
  href: https://artifacts.apis.io/webrix/well-known/webrix-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/webrix-well-known.yml
- group: other
  href: https://artifacts.apis.io/webrix/hosts/webrix-hosts.yml
  title: ''
  type: Hosts
  url: hosts/webrix-hosts.yml
- group: other
  href: https://artifacts.apis.io/webrix/vendors/webrix-vendors.yml
  title: ''
  type: Vendors
  url: vendors/webrix-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.withwillow.ai/
- group: start
  title: ''
  type: Login
  url: https://app.withwillow.ai/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://withwillow.ai/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.withwillow.ai/docs/admin/security/guards/setup-and-coverage
- group: auth
  href: https://artifacts.apis.io/webrix/security/webrix-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/webrix-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://withwillow.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.withwillow.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://withwillow.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://withwillow.ai/terms
- group: company
  title: ''
  type: Blog
  url: https://withwillow.ai/blog
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://docs.webrix.ai/openapi.json
  - status: 401
    url: https://api.withwillow.ai/mcp
  - status: 200
    url: https://webrix.ai/
  reason: partner-login
  state: gated
created: '2026-10-19'
description: Willow AI Governance Control Plane provides an AI Agent Governance and Enablement Platform that enforces identity, scoped access, runtime policies, shadow AI detection, and audit trails for AI agents. Trusted by enterprises such as Wix, Papaya Global, and Innovid, the platform offers centralized control, compliance, and monitoring across AI workloads, helping organizations manage risk and ensure responsible AI usage.
image: https://cdn.prod.website-files.com/69ca7b2d416aeff5210dbb8b/69cacb738713ace6cf73adb6_3f79045fdc40934e21f5a447a33ab9f4_opengraph.jpg
json_schemas:
- name: Guard
  property_count: 16
  slug: webrix-guard
- name: Plugin
  property_count: 20
  slug: webrix-plugin
- name: Skill
  property_count: 17
  slug: webrix-skill
- name: Toolkit
  property_count: 14
  slug: webrix-toolkit
- name: UpdateEnforcementPolicyRequest
  property_count: 4
  slug: webrix-update-enforcement-policy-request
- name: User
  property_count: 14
  slug: webrix-user
jsonld:
- class_count: 84
  name: Webrix Context
  property_count: 224
  slug: webrix-context
layout: provider
modified: '2026-10-19'
name: Willow AI Governance Control Plane
nav: Providers
network: true
overview: 'Willow AI Governance Control Plane publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Willow API API, and 1 more. Tagged areas include Company, Artificial Intelligence, Governance, Platform, and Enterprise.


  The Willow AI Governance Control Plane catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Willow AI Governance Control Plane''s developer surface includes changelog, authentication, getting-started guide, documentation, pricing, engineering blog, and 21 more developer resources.'
plans:
- name: Webrix Plans Pricing
  plan_count: 2
  slug: webrix-plans-pricing
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: Willow AI Governance Control Plane API Rules
  rule_count: 17
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 1
  slug: webrix-rules
score:
  band: developing
  composite: 53.2
  coverage:
    artifact_dirs: 20
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.7
    contract_governance: 35.6
    contract_quality: 56.7
    developer_ergonomics: 35.7
    discoverability: 66.1
    operational_transparency: 34.2
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: derived
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
    score: 27.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Webrix Authentication
  slug: webrix-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Webrix Domain Security
  slug: webrix-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: webrix
tags:
- Company
- Artificial Intelligence
- Governance
- Platform
- Enterprise
website: https://withwillow.ai/
---
