---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 23.9
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Bool API provides HTTP endpoints for building AI-powered applications, as documented in the Bool developer docs.
  name: Bool API
  slug: bool-api
- description: 'Bool API as documented publicly: 12 operations. Contract generated from the documentation by API Evangelist (2026-11-02); not the provider''s own document.'
  name: Bool API
  slug: bool-com-api
artifact_total: 13
common:
- group: commercial
  href: https://artifacts.apis.io/bool-com/plans/bool-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bool-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/bool-com/rules/bool-com-rules.yml
  title: ''
  type: Spectral
  url: rules/bool-com-rules.yml
- group: design
  href: https://artifacts.apis.io/bool-com/json-ld/bool-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bool-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/bool-com/vocabulary/bool-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bool-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/bool-com/data-model/bool-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bool-com-data-model.yml
- group: build
  href: https://artifacts.apis.io/bool-com/cli/bool-com-cli.yml
  title: ''
  type: CLI
  url: cli/bool-com-cli.yml
- group: auth
  title: ''
  type: Security
  url: https://bool.com/privacy
- group: design
  href: https://artifacts.apis.io/bool-com/conformance/bool-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bool-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bool-com/llms/bool-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bool-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/bool-com/well-known/bool-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bool-com-security.txt
- group: agent
  href: https://artifacts.apis.io/bool-com/well-known/bool-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bool-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/bool-com/hosts/bool-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bool-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/bool-com/vendors/bool-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bool-com-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://bool.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bool.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://bool.com/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://bool.com/docs
- group: operate
  title: ''
  type: ChangeLog
  url: https://bool.com/whats-new
- group: start
  title: ''
  type: GettingStarted
  url: https://bool.com/docs/getting-started
- group: auth
  href: https://artifacts.apis.io/bool-com/security/bool-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bool-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/bool-com/security/bool-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bool-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bool.com/
coverage:
  checked: '2026-11-02'
  detail: GraphQL and MCP endpoints require authentication, no public spec available.
  evidence:
  - status: 401
    url: https://bool.com/api/graphql
  - status: 401
    url: https://bool.com/api/mcp
  reason: auth-required
  state: gated
created: '2026-11-02'
description: Bool is a vibe coding platform powered by AI that lets users describe an idea and instantly receive a full‑stack application, live URL, and hosting. It offers low‑code development tools, AI‑generated code, and a marketplace for extensions, targeting developers and businesses seeking rapid prototyping and deployment.
image: https://bool.com/opengraph-image?0971fd880b97ca2b
json_schemas:
- name: GetApiProjectsIdConnectionResponse
  property_count: 9
  slug: bool-com-get-api-projects-id-connection-response
- name: GetApiProjectsIdResponse
  property_count: 7
  slug: bool-com-get-api-projects-id-response
- name: GetApiProjectsResponse
  property_count: 6
  slug: bool-com-get-api-projects-response
- name: GetResponse
  property_count: 7
  slug: bool-com-get-response
- name: PostApiDropsResponse
  property_count: 7
  slug: bool-com-post-api-drops-response
- name: PostApiProjectsResponse
  property_count: 6
  slug: bool-com-post-api-projects-response
jsonld:
- class_count: 13
  name: Bool Com Context
  property_count: 26
  slug: bool-com-context
layout: provider
modified: '2026-11-02'
name: Bool
nav: Providers
network: true
overview: 'Bool is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Low-Code, Platform, and Development.


  The Bool catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Bool''s developer surface includes CLI, support, pricing, documentation, changelog, getting-started guide, and 16 more developer resources.'
plans:
- name: Bool Com Plans Pricing
  plan_count: 3
  slug: bool-com-plans-pricing
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 82
  extends:
  - spectral:oas
  name: Bool API Rules
  rule_count: 41
  severity_counts:
    error: 39
    hint: 0
    info: 1
    warn: 1
  slug: bool-com-rules
score:
  band: thin
  composite: 29.1
  coverage:
    artifact_dirs: 18
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 22.0
    contract_quality: 24.8
    developer_ergonomics: 20.2
    discoverability: 57.1
    operational_transparency: 13.2
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bool Com Domain Security
  slug: bool-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bool Com Vulnerability Disclosure
  slug: bool-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bool-com
tags:
- Company
- Artificial Intelligence
- Low-Code
- Platform
- Development
website: https://bool.com/
---
