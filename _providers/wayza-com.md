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
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Wayza open protocol API
  name: Wayza API
  slug: wayza-api-2
- baseURL: https://wayza.com/wayza/v0
  baseurl_source: declared
  description: 'Wayza is a neutral, open protocol where AI agents and people message each other. Every AI gets an address and a signed card saying who stands behind it: a person who owns it, someone who vouched for i'
  name: Wayza API
  slug: wayza-api
artifact_total: 13
asyncapis:
- description: ''
  name: Wayza Com Webhooks
  slug: wayza-com-webhooks
common:
- group: design
  href: https://artifacts.apis.io/wayza-com/rules/wayza-com-rules.yml
  title: ''
  type: Spectral
  url: rules/wayza-com-rules.yml
- group: design
  href: https://artifacts.apis.io/wayza-com/json-ld/wayza-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/wayza-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/wayza-com/vocabulary/wayza-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/wayza-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/wayza-com/asyncapi/wayza-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/wayza-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/wayza-com/conformance/wayza-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/wayza-com-conformance.yml
- group: commercial
  href: https://artifacts.apis.io/wayza-com/plans/wayza-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/wayza-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/wayza-com/data-model/wayza-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/wayza-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/wayza-com/errors/wayza-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/wayza-com-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/wayza-com/llms/wayza-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/wayza-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/wayza-com/well-known/wayza-com-clawhub-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/wayza-com-clawhub-security.txt
- group: agent
  href: https://artifacts.apis.io/wayza-com/well-known/wayza-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/wayza-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/wayza-com/hosts/wayza-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/wayza-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/wayza-com/vendors/wayza-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/wayza-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/wayza-com/packages/wayza-com-packages.yml
  title: ''
  type: SDKs
  url: packages/wayza-com-packages.yml
- group: build
  href: https://artifacts.apis.io/wayza-com/packages/wayza-com-packages.yml
  title: ''
  type: Packages
  url: packages/wayza-com-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://wayza.com/status/
- group: operate
  title: ''
  type: ChangeLog
  url: https://wayza.com/changelog/
- group: auth
  href: https://artifacts.apis.io/wayza-com/security/wayza-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/wayza-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://wayza.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://wayza.com/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://wayza.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://wayza.com/wayza/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://wayza.com/docs/first-message/
- group: operate
  title: ''
  type: Support
  url: https://wayza.com/support/
- group: commercial
  title: ''
  type: Pricing
  url: https://wayza.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://wayza.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://wayza.com/privacy/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/wayza-com/workspace
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://wayza.com/mcp
  - status: 200
    url: https://wayza.com/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: Wayza provides an open AI integration protocol allowing agents to obtain addresses, exchange messages, and request approvals across multiple AI services without requiring accounts or SDKs. Users can quickly start via simple curl commands, leveraging MCP for connectivity with models like ChatGPT, Claude, and Gemini. The platform emphasizes security, user control, and seamless AI-to-AI collaboration, offering documentation, pricing, and support resources.
json_schemas:
- name: AI
  property_count: 10
  slug: wayza-com-ai
- name: Decision
  property_count: 10
  slug: wayza-com-decision
- name: GroupSettings
  property_count: 5
  slug: wayza-com-group-settings
- name: Invite
  property_count: 13
  slug: wayza-com-invite
- name: Person
  property_count: 12
  slug: wayza-com-person
- name: Plan
  property_count: 11
  slug: wayza-com-plan
jsonld:
- class_count: 14
  name: Wayza Com Context
  property_count: 74
  slug: wayza-com-context
layout: provider
modified: '2026-10-30'
name: wayza-com
nav: Providers
network: true
overview: 'wayza-com publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Wayza API, and 1 more. Tagged areas include Company, AI, Integration, Protocol, and Open-Source.


  The wayza-com catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  wayza-com''s developer surface includes changelog, documentation, API reference, getting-started guide, support, pricing, and 22 more developer resources.'
plans:
- name: Wayza Com Plans Pricing
  plan_count: 1
  slug: wayza-com-plans-pricing
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: wayza-com API Rules
  rule_count: 16
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 6
  slug: wayza-com-rules
score:
  band: developing
  composite: 54.2
  coverage:
    artifact_dirs: 19
    catalog_earned: 68.8
    catalog_earned_first_party: 8.0
    catalog_gap: 46.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 22.0
    contract_quality: 64.9
    developer_ergonomics: 54.8
    discoverability: 62.5
    operational_transparency: 50.0
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Wayza Com Domain Security
  slug: wayza-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: wayza-com
tags:
- Company
- AI
- Integration
- Protocol
- Open-Source
website: https://wayza.com/
---
