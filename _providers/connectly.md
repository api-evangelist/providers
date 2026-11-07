---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 31.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Connectly Agentic Access
  operation_count: 4
  slug: connectly-agentic-access
  summary_line: 4 operations · 4 acting
api_count: 1
apis:
- baseURL: https://api.connectly.ai
  baseurl_source: declared
  description: The Businesses API from Connectly — 4 operation(s) for businesses.
  name: Connectly Businesses API
  slug: connectly-businesses-api
artifact_total: 15
asyncapis:
- description: ''
  name: Connectly Webhooks
  slug: connectly-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/connectly/agentic-access/connectly-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/connectly-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/connectly/finops/connectly-finops.yml
  title: ''
  type: FinOps
  url: finops/connectly-finops.yml
- group: commercial
  href: https://artifacts.apis.io/connectly/plans/connectly-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/connectly-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/connectly/rules/connectly-rules.yml
  title: ''
  type: Spectral
  url: rules/connectly-rules.yml
- group: design
  href: https://artifacts.apis.io/connectly/json-ld/connectly-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/connectly-context.jsonld
- group: design
  href: https://artifacts.apis.io/connectly/vocabulary/connectly-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/connectly-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/connectly/asyncapi/connectly-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/connectly-webhooks.yml
- group: design
  href: https://artifacts.apis.io/connectly/data-model/connectly-data-model.yml
  title: ''
  type: DataModel
  url: data-model/connectly-data-model.yml
- group: auth
  href: https://artifacts.apis.io/connectly/authentication/connectly-authentication.yml
  title: ''
  type: Authentication
  url: authentication/connectly-authentication.yml
- group: design
  href: https://artifacts.apis.io/connectly/conformance/connectly-conformance.yml
  title: ''
  type: Conformance
  url: conformance/connectly-conformance.yml
- group: agent
  href: https://artifacts.apis.io/connectly/llms/connectly-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/connectly-llms.txt
- group: other
  href: https://artifacts.apis.io/connectly/a2a/connectly-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/connectly-a2a.yml
- group: agent
  href: https://artifacts.apis.io/connectly/well-known/connectly-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/connectly-well-known.yml
- group: other
  href: https://artifacts.apis.io/connectly/hosts/connectly-hosts.yml
  title: ''
  type: Hosts
  url: hosts/connectly-hosts.yml
- group: other
  href: https://artifacts.apis.io/connectly/vendors/connectly-vendors.yml
  title: ''
  type: Vendors
  url: vendors/connectly-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.connectly.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.connectly.ai/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://www.connectly.ai/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.connectly.ai/en/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.connectly.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.connectly.ai/en/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.connectly.ai/get-started/quick-start
- group: docs
  title: ''
  type: Documentation
  url: https://dev.connectly.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.connectly.ai\
- group: auth
  href: https://artifacts.apis.io/connectly/security/connectly-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/connectly-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.connectly.ai
coverage:
  checked: '2026-10-10'
  detail: Connectly provides public documentation but no machine‑readable OpenAPI, GraphQL, AsyncAPI, or other contract was found.
  evidence:
  - status: 200
    url: https://docs.connectly.ai/introduction.md
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-10'
description: Connectly is an AI-native platform delivering intelligent agents that sell, serve, and engage customers across industries such as retail, healthcare, financial services, telecommunications, utilities, and education. Backed by Unusual Ventures, Alibaba, and Volpe Capital, Connectly provides AI agents for large enterprises in the US, Latin America, and the Middle East, offering features like product recommendation, order handling, prescription processing, and compliance support, all ISO‑27001 certified and GDPR compliant.
finops:
- has_sources: true
  method: derived
  name: Connectly Finops
  primary_unit: ''
  service_category: ''
  slug: connectly-finops
  template: true
image: https://www.connectly.ai/redesign/4570d00b6da8068d2c0954804a5dbe2d4c4bfc248d284f10b3f6140c1fc2b3c3/hero.webp
json_schemas:
- name: PostV1BusinessesBusinessidRequest
  property_count: 2
  slug: connectly-post-v1-businesses-businessid-request
- name: PostV1BusinessesBusinessidResponse
  property_count: 1
  slug: connectly-post-v1-businesses-businessid-response
- name: PostV1BusinessesBusinessidSendSendidRequest
  property_count: 8
  slug: connectly-post-v1-businesses-businessid-send-sendid-request
- name: PostV1BusinessesBusinessidSendSendidResponse
  property_count: 1
  slug: connectly-post-v1-businesses-businessid-send-sendid-response
- name: PostV1BusinessesRequest
  property_count: 4
  slug: connectly-post-v1-businesses-request
- name: PostV1BusinessesResponse
  property_count: 4
  slug: connectly-post-v1-businesses-response
jsonld:
- class_count: 6
  name: Connectly Context
  property_count: 15
  slug: connectly-context
layout: provider
modified: '2026-10-10'
name: Connectly
nav: Providers
network: true
overview: 'Connectly is listed with 1 API on the [APIs.io](https://apis.io/) network: Businesses API. Tagged areas include Artificial Intelligence, Platform, Customer Engagement, Enterprise, and Automation.


  The Connectly catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Connectly''s developer surface includes authentication, support, pricing, engineering blog, getting-started guide, documentation, and 20 more developer resources.'
plans:
- name: Connectly Plans Pricing
  plan_count: 1
  slug: connectly-plans-pricing
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 82
  extends:
  - spectral:oas
  name: Connectly API Rules
  rule_count: 41
  severity_counts:
    error: 39
    hint: 0
    info: 1
    warn: 1
  slug: connectly-rules
score:
  band: thin
  composite: 35.7
  coverage:
    artifact_dirs: 25
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.4
  facets:
    access_clarity: 40.8
    contract_governance: 35.6
    contract_quality: 34.1
    developer_ergonomics: 31.0
    discoverability: 73.2
    operational_transparency: 7.9
  previous_composite: 44.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/connectly/connectly-2026-11-03T125124.png
security:
- kind: authentication
  name: Connectly Authentication
  slug: connectly-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Connectly Domain Security
  slug: connectly-domain-security
  summary_line: TLSv1.3 · DMARC
slug: connectly
tags:
- Artificial Intelligence
- Platform
- Customer Engagement
- Enterprise
- Automation
website: https://www.connectly.ai
---
