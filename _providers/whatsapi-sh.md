---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: true
    idempotency: derived
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
  score: 41.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Flat REST endpoints over your own paired WhatsApp numbers.
  name: WhatsApp API
  slug: whatsapp-api
artifact_total: 6
asyncapis:
- description: ''
  name: Whatsapi Sh Webhooks
  slug: whatsapi-sh-webhooks
common:
- group: design
  href: https://artifacts.apis.io/whatsapi-sh/rules/whatsapi-sh-rules.yml
  title: ''
  type: Spectral
  url: rules/whatsapi-sh-rules.yml
- group: design
  href: https://artifacts.apis.io/whatsapi-sh/json-ld/whatsapi-sh-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/whatsapi-sh-context.jsonld
- group: design
  href: https://artifacts.apis.io/whatsapi-sh/vocabulary/whatsapi-sh-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/whatsapi-sh-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/whatsapi-sh/conventions/whatsapi-sh-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/whatsapi-sh-conventions.yml
- group: design
  href: https://artifacts.apis.io/whatsapi-sh/conventions/whatsapi-sh-conventions.yml
  title: ''
  type: Conventions
  url: conventions/whatsapi-sh-conventions.yml
- group: design
  href: https://artifacts.apis.io/whatsapi-sh/conformance/whatsapi-sh-conformance.yml
  title: ''
  type: Conformance
  url: conformance/whatsapi-sh-conformance.yml
- group: agent
  href: https://artifacts.apis.io/whatsapi-sh/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/whatsapi-sh/asyncapi/whatsapi-sh-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/whatsapi-sh-webhooks.yml
- group: design
  href: https://artifacts.apis.io/whatsapi-sh/data-model/whatsapi-sh-data-model.yml
  title: ''
  type: DataModel
  url: data-model/whatsapi-sh-data-model.yml
- group: design
  href: https://artifacts.apis.io/whatsapi-sh/errors/whatsapi-sh-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/whatsapi-sh-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/whatsapi-sh/llms/whatsapi-sh-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/whatsapi-sh-llms.txt
- group: agent
  href: https://artifacts.apis.io/whatsapi-sh/well-known/whatsapi-sh-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/whatsapi-sh-well-known.yml
- group: other
  href: https://artifacts.apis.io/whatsapi-sh/hosts/whatsapi-sh-hosts.yml
  title: ''
  type: Hosts
  url: hosts/whatsapi-sh-hosts.yml
- group: other
  href: https://artifacts.apis.io/whatsapi-sh/vendors/whatsapi-sh-vendors.yml
  title: ''
  type: Vendors
  url: vendors/whatsapi-sh-vendors.yml
- group: build
  href: https://artifacts.apis.io/whatsapi-sh/packages/whatsapi-sh-packages.yml
  title: ''
  type: SDKs
  url: packages/whatsapi-sh-packages.yml
- group: build
  href: https://artifacts.apis.io/whatsapi-sh/packages/whatsapi-sh-packages.yml
  title: ''
  type: Packages
  url: packages/whatsapi-sh-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://whatsapi.sh/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://whatsapi.sh/privacy
- group: docs
  title: ''
  type: APIReference
  url: https://docs.whatsapi.sh/llms.txt
- group: auth
  href: https://artifacts.apis.io/whatsapi-sh/security/whatsapi-sh-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/whatsapi-sh-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://whatsapi.sh/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.whatsapi.sh/
- group: commercial
  title: ''
  type: Pricing
  url: https://whatsapi.sh/#pricing
created: '2026-10-31'
description: whatsapi.sh provides a simple HTTP API that lets developers send WhatsApp messages, login codes, and files using an existing phone number. It operates without Meta’s official Business API approval, offering a free tier with signed webhooks and an MCP server. The service emphasizes ease of integration, no template requirements, and transparent pricing, targeting developers who need quick WhatsApp communication for authentication, notifications, or chat bots.
image: https://whatsapi.sh/og/home.png
jsonld:
- class_count: 1
  name: Whatsapi Sh Context
  property_count: 1
  slug: whatsapi-sh-context
layout: provider
modified: '2026-10-31'
name: whatsapi-sh
nav: Providers
network: true
overview: 'whatsapi-sh publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Messaging, WhatsApp, and Developer Tools.


  The whatsapi-sh catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  whatsapi-sh''s developer surface includes API reference, documentation, pricing, and 20 more developer resources.'
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: whatsapi-sh API Rules
  rule_count: 18
  severity_counts:
    error: 17
    hint: 0
    info: 1
    warn: 0
  slug: whatsapi-sh-rules
score:
  band: thin
  composite: 27.9
  coverage:
    artifact_dirs: 19
    catalog_earned: 42.0
    catalog_earned_first_party: 0.0
    catalog_gap: 73.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.3
  facets:
    access_clarity: 15.8
    contract_governance: 19.7
    contract_quality: 45.5
    developer_ergonomics: 17.3
    discoverability: 57.1
    operational_transparency: 7.9
  previous_composite: 34.2
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Whatsapi Sh Domain Security
  slug: whatsapi-sh-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: send-message
  slug: whatsapi-sh-send_message
slug: whatsapi-sh
tags:
- Company
- Messaging
- WhatsApp
- Developer Tools
website: https://whatsapi.sh/
---
