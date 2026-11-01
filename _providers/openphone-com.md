---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
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
    openapi_examples: verified
    operation_distinctiveness: false
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://api.quo.com
  baseurl_source: declared
  description: 'Quo API as documented publicly: 15 operations. Contract generated from the documentation by API Evangelist (2026-10-24); not the provider''s own document.'
  name: Quo API
  slug: openphone-com-api
artifact_total: 15
asyncapis:
- description: ''
  name: Openphone Com Webhooks
  slug: openphone-com-webhooks
common:
- group: operate
  href: https://artifacts.apis.io/openphone-com/rate-limits/openphone-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/openphone-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/openphone-com/plans/openphone-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/openphone-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/openphone-com/rules/openphone-com-rules.yml
  title: ''
  type: Spectral
  url: rules/openphone-com-rules.yml
- group: design
  href: https://artifacts.apis.io/openphone-com/json-ld/openphone-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/openphone-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/openphone-com/vocabulary/openphone-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/openphone-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/openphone-com/asyncapi/openphone-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/openphone-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/openphone-com/data-model/openphone-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/openphone-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/openphone-com/changelog/openphone-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/openphone-com-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.quo.com/security
- group: auth
  href: https://artifacts.apis.io/openphone-com/authentication/openphone-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/openphone-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/openphone-com/lifecycle/openphone-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/openphone-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/openphone-com/conformance/openphone-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/openphone-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/openphone-com/llms/openphone-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/openphone-com-llms.txt
- group: other
  href: https://artifacts.apis.io/openphone-com/a2a/openphone-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/openphone-com-a2a.yml
- group: other
  href: https://artifacts.apis.io/openphone-com/hosts/openphone-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/openphone-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/openphone-com/vendors/openphone-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/openphone-com-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://www.quo.com/integrations/webhooks
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.quo.com/terms
- group: operate
  title: ''
  type: Support
  url: https://www.quo.com/solutions/support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.quo.com
- group: auth
  title: ''
  type: Security
  url: https://www.quo.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.quo.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.quo.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://www.quo.com/press
- group: docs
  title: ''
  type: Documentation
  url: https://www.quo.com/docs
- group: operate
  title: ''
  type: ChangeLog
  url: https://support.quo.com/changelog
- group: company
  title: ''
  type: Blog
  url: https://www.quo.com/blog/
- group: docs
  title: ''
  type: APIReference
  url: https://www.quo.com/docs/mdx/api-reference/error-codes
- group: start
  title: ''
  type: GettingStarted
  url: https://www.quo.com/docs/2026-03-30/webhooks-quickstart
- group: auth
  href: https://artifacts.apis.io/openphone-com/security/openphone-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/openphone-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/openphone-com/security/openphone-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/openphone-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.quo.com/
created: '2026-10-24'
description: Quo (formerly OpenPhone) provides a shared phone system for small businesses, combining calling, texting, and AI-driven automation. The platform offers shared numbers, call routing, voicemail, analytics, CRM integration, and a public API for developers. It serves over 90,000 businesses, emphasizing AI agents and seamless multi-channel communication.
image: https://cdn.prod.website-files.com/6899ec2c2b29c1edf8c20f15/690d0a9bad3f5225ab9fc359_7c18f9d49ac0d507597d6c00b78e10b4_OG%20image.png
json_schemas:
- name: GetV1CallsResponse
  property_count: 3
  slug: openphone-com-get-v1-calls-response
- name: GetV1ContactsIdResponse
  property_count: 9
  slug: openphone-com-get-v1-contacts-id-response
- name: GetV1ContactsResponse
  property_count: 9
  slug: openphone-com-get-v1-contacts-response
- name: GetV1MessagesResponse
  property_count: 3
  slug: openphone-com-get-v1-messages-response
- name: GetV1TasksResponse
  property_count: 3
  slug: openphone-com-get-v1-tasks-response
- name: PostV1ContactsResponse
  property_count: 9
  slug: openphone-com-post-v1-contacts-response
jsonld:
- class_count: 13
  name: Openphone Com Context
  property_count: 16
  slug: openphone-com-context
layout: provider
modified: '2026-10-24'
name: Quo
nav: Providers
network: true
overview: 'Quo is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Phone System, Shared Numbers, AI Agent, Small Business, and Integrations.


  The Quo catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Quo''s developer surface includes changelog, authentication, support, pricing, documentation, engineering blog, API reference, and 25 more developer resources.'
plans:
- name: Openphone Com Plans Pricing
  plan_count: 3
  slug: openphone-com-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: Openphone Com Rate Limits
  slug: openphone-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Quo API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: openphone-com-rules
score:
  band: strong
  composite: 54.7
  coverage:
    artifact_dirs: 21
    catalog_earned: 82.8
    catalog_earned_first_party: 20.0
    catalog_gap: 32.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 78.9
    contract_governance: 22.0
    contract_quality: 34.3
    developer_ergonomics: 47.6
    discoverability: 67.9
    operational_transparency: 71.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 8
      marker_coverage: 100.0
      total: 8
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Openphone Com Authentication
  slug: openphone-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Openphone Com Domain Security
  slug: openphone-com-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Openphone Com Trust Center
  slug: openphone-com-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: openphone-com
tags:
- Phone System
- Shared Numbers
- AI Agent
- Small Business
- Integrations
- CRM
- Call Routing
website: https://www.quo.com/
---
