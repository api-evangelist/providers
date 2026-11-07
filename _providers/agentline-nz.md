---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
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
  score: 35.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Email inboxes for AI agents, providing REST endpoints for email, SMS, calls and voice.
  name: Agentline API
  slug: agentline-api
- baseURL: https://agentline.nz/api/v1
  baseurl_source: declared
  description: 'Email inboxes for AI agents: send and read email and wait for one-time codes. Texting is coming soon; the SMS, calls, voice and owner mobile endpoints are not available yet. Successful authenticated r'
  name: Agentline API API
  slug: agentline-api-api
artifact_total: 13
common:
- group: commercial
  href: https://artifacts.apis.io/agentline-nz/plans/agentline-nz-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agentline-nz-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/agentline-nz/rules/agentline-nz-rules.yml
  title: ''
  type: Spectral
  url: rules/agentline-nz-rules.yml
- group: design
  href: https://artifacts.apis.io/agentline-nz/json-ld/agentline-nz-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/agentline-nz-context.jsonld
- group: design
  href: https://artifacts.apis.io/agentline-nz/vocabulary/agentline-nz-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agentline-nz-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/agentline-nz/data-model/agentline-nz-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agentline-nz-data-model.yml
- group: auth
  href: https://artifacts.apis.io/agentline-nz/authentication/agentline-nz-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agentline-nz-authentication.yml
- group: design
  href: https://artifacts.apis.io/agentline-nz/errors/agentline-nz-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agentline-nz-problem-types.yml
- group: design
  href: https://artifacts.apis.io/agentline-nz/conformance/agentline-nz-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentline-nz-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agentline-nz/llms/agentline-nz-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentline-nz-llms.txt
- group: agent
  href: https://artifacts.apis.io/agentline-nz/well-known/agentline-nz-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentline-nz-well-known.yml
- group: other
  href: https://artifacts.apis.io/agentline-nz/hosts/agentline-nz-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentline-nz-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentline-nz/vendors/agentline-nz-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentline-nz-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://agentline.nz/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://agentline.nz/changelog
- group: auth
  href: https://artifacts.apis.io/agentline-nz/security/agentline-nz-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentline-nz-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentline.nz/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://agentline.nz/developers
- group: docs
  title: ''
  type: Documentation
  url: https://agentline.nz/docs
- group: docs
  title: ''
  type: APIReference
  url: https://agentline.nz/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://agentline.nz/how-it-works
- group: commercial
  title: ''
  type: Pricing
  url: https://agentline.nz/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agentline.nz/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agentline.nz/privacy
- group: operate
  title: ''
  type: Support
  url: https://agentline.nz/help
created: '2026-11-01'
description: Agentline NZ provides AI assistants with a dedicated @agentline.nz email inbox, enabling them to receive sign‑in codes, send and read emails, and interact via a REST API and MCP server. The service offers a 7‑day free trial, plans starting at NZ$29/month, and upcoming texting and phone number features. Documentation, quickstart guides, pricing, and support are publicly available, and the platform integrates with ChatGPT, Claude, and other agents.
image: https://agentline.nz/og/default.png
json_schemas:
- name: Billing
  property_count: 11
  slug: agentline-nz-billing
- name: Call
  property_count: 9
  slug: agentline-nz-call
- name: Email
  property_count: 16
  slug: agentline-nz-email
- name: EmailSummary
  property_count: 11
  slug: agentline-nz-email-summary
- name: Me
  property_count: 13
  slug: agentline-nz-me
- name: Signup
  property_count: 12
  slug: agentline-nz-signup
jsonld:
- class_count: 15
  name: Agentline Nz Context
  property_count: 74
  slug: agentline-nz-context
layout: provider
modified: '2026-11-01'
name: Agentline NZ
nav: Providers
network: true
overview: 'Agentline NZ publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agentline API API, and 1 more. Tagged areas include Artificial Intelligence, Email, Assistant, NZ, and Software-as-a-Service.


  The Agentline NZ catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Agentline NZ''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, pricing, support, and 17 more developer resources.'
plans:
- name: Agentline Nz Plans Pricing
  plan_count: 3
  slug: agentline-nz-plans-pricing
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: Agentline NZ API Rules
  rule_count: 16
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 2
  slug: agentline-nz-rules
score:
  band: developing
  composite: 41.0
  coverage:
    artifact_dirs: 19
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.3
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 50.7
    developer_ergonomics: 33.3
    discoverability: 66.1
    operational_transparency: 7.9
  previous_composite: 51.3
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agentline Nz Authentication
  slug: agentline-nz-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Agentline Nz Domain Security
  slug: agentline-nz-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: agentline-nz
tags:
- Artificial Intelligence
- Email
- Assistant
- NZ
- Software-as-a-Service
- Company
website: https://agentline.nz/
---
