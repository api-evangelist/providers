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
    error_semantics: false
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.7
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API documentation for AskBase, describing endpoints for knowledge base, AI chatbot, and other features.
  name: AskBase API
  slug: askbase-api
- description: 'AskBase API as documented publicly: 97 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: AskBase API
  slug: askbase-com-api
artifact_total: 12
common:
- group: commercial
  href: https://artifacts.apis.io/askbase-com/plans/askbase-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/askbase-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/askbase-com/rules/askbase-com-rules.yml
  title: ''
  type: Spectral
  url: rules/askbase-com-rules.yml
- group: design
  href: https://artifacts.apis.io/askbase-com/json-ld/askbase-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/askbase-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/askbase-com/vocabulary/askbase-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/askbase-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/askbase-com/data-model/askbase-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/askbase-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/askbase-com/conformance/askbase-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/askbase-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/askbase-com/well-known/askbase-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/askbase-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/askbase-com/hosts/askbase-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/askbase-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/askbase-com/vendors/askbase-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/askbase-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/askbase-com/security/askbase-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/askbase-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://askbase.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.askbase.com/
- group: docs
  title: ''
  type: Documentation
  url: https://askbase.com/guides
- group: start
  title: ''
  type: Login
  url: https://askbase.com/signin
- group: commercial
  title: ''
  type: Pricing
  url: https://askbase.com/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://askbase.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://askbase.com/signup
- group: operate
  title: ''
  type: StatusPage
  url: https://status.askbase.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://askbase.com/terms
coverage:
  checked: '2026-11-03'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract files were found on the provider's documented hosts.
  evidence:
  - status: 404
    url: https://askbase.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: AskBase provides an AI-powered knowledge base that keeps itself up to date. It offers features like knowledge base articles, AI chatbot, help desk software, multilingual support, and team collaboration, allowing businesses to automate customer support and internal documentation while learning from interactions.
image: https://askbase.com/og?title=The+AI+knowledge+base+that+keeps+itself+up+to+date
json_schemas:
- name: PostApiV1OpsConversationRatedraftRequest
  property_count: 4
  slug: askbase-com-post-api-v1-ops-conversation-ratedraft-request
- name: PostApiV1OpsConversationReplyRequest
  property_count: 9
  slug: askbase-com-post-api-v1-ops-conversation-reply-request
- name: PostApiV1OpsInboxListRequest
  property_count: 6
  slug: askbase-com-post-api-v1-ops-inbox-list-request
- name: PostApiV1OpsSuggestionsApproveRequest
  property_count: 5
  slug: askbase-com-post-api-v1-ops-suggestions-approve-request
- name: PostApiV1OpsSuggestionsDraftforgapRequest
  property_count: 5
  slug: askbase-com-post-api-v1-ops-suggestions-draftforgap-request
- name: PostApiV1OpsTranslationSaveRequest
  property_count: 4
  slug: askbase-com-post-api-v1-ops-translation-save-request
jsonld:
- class_count: 120
  name: Askbase Com Context
  property_count: 70
  slug: askbase-com-context
layout: provider
modified: '2026-11-01'
name: AskBase
nav: Providers
network: true
overview: 'AskBase is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Knowledge Base, Customer Service, Software-as-a-Service, and Automation.


  The AskBase catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AskBase''s developer surface includes engineering blog, documentation, pricing, signup flow, and 15 more developer resources.'
plans:
- name: Askbase Com Plans Pricing
  plan_count: 4
  slug: askbase-com-plans-pricing
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 82
  extends:
  - spectral:oas
  name: AskBase API Rules
  rule_count: 41
  severity_counts:
    error: 39
    hint: 0
    info: 1
    warn: 1
  slug: askbase-com-rules
score:
  band: thin
  composite: 28.3
  coverage:
    artifact_dirs: 15
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.2
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 25.2
    developer_ergonomics: 6.0
    discoverability: 57.1
    operational_transparency: 7.9
  previous_composite: 35.5
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
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Askbase Com Domain Security
  slug: askbase-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: askbase-com
tags:
- Artificial Intelligence
- Knowledge Base
- Customer Service
- Software-as-a-Service
- Automation
website: https://askbase.com/
---
