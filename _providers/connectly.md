---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.0
  scored_at: '2026-10-17'
api_count: 1
apis:
- baseURL: https://api.connectly.ai
  baseurl_source: declared
  description: The Businesses API from Connectly — 4 operation(s) for businesses.
  name: Connectly Businesses API
  slug: connectly-businesses-api
artifact_total: 12
asyncapis:
- description: ''
  name: Connectly Webhooks
  slug: connectly-webhooks
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/connectly/refs/heads/main/rules/connectly-rules.yml
  title: ''
  type: Spectral
  url: rules/connectly-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/connectly/refs/heads/main/json-ld/connectly-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/connectly-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/connectly/refs/heads/main/vocabulary/connectly-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/connectly-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/connectly/refs/heads/main/asyncapi/connectly-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/connectly-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/connectly/refs/heads/main/data-model/connectly-data-model.yml
  title: ''
  type: DataModel
  url: data-model/connectly-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/connectly/refs/heads/main/authentication/connectly-authentication.yml
  title: ''
  type: Authentication
  url: authentication/connectly-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/connectly/refs/heads/main/conformance/connectly-conformance.yml
  title: ''
  type: Conformance
  url: conformance/connectly-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/connectly/refs/heads/main/llms/connectly-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/connectly-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/connectly/refs/heads/main/a2a/connectly-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/connectly-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/connectly/refs/heads/main/well-known/connectly-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/connectly-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/connectly/refs/heads/main/hosts/connectly-hosts.yml
  title: ''
  type: Hosts
  url: hosts/connectly-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/connectly/refs/heads/main/vendors/connectly-vendors.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/connectly/refs/heads/main/security/connectly-domain-security.yml
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
overview: 'Connectly is listed with 1 API on the [APIs.io](https://apis.io/) network: Businesses API. Tagged areas include Artificial Intelligence, Platform, CustomerEngagement, Enterprise, and Automation.


  The Connectly catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Connectly''s developer surface includes authentication, support, pricing, engineering blog, getting-started guide, documentation, and 17 more developer resources.'
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Connectly API Rules
  rule_count: 11
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 0
  slug: connectly-rules
score:
  band: developing
  composite: 39.9
  coverage:
    artifact_dirs: 16
    catalog_earned: 62.0
    catalog_earned_first_party: 0.0
    catalog_gap: 53.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 39.5
    contract_governance: 33.3
    contract_quality: 34.1
    developer_ergonomics: 50.0
    discoverability: 73.2
    operational_transparency: 7.9
  provenance:
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
    score: 27.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
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
- CustomerEngagement
- Enterprise
- Automation
website: https://www.connectly.ai
---
