---
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
    error_semantics: derived
    event_surface_described: false
    idempotency: derived
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Webhook delivery reliability platform API
  name: HookBridge API
  slug: hookbridge-api
- baseURL: https://api.hookbridge.io
  baseurl_source: declared
  description: 'HookBridge is a webhook delivery reliability platform that provides:'
  name: HookBridge API API
  slug: hookbridge-api-api
artifact_total: 13
common:
- group: design
  href: https://artifacts.apis.io/hookbridge/rules/hookbridge-rules.yml
  title: ''
  type: Spectral
  url: rules/hookbridge-rules.yml
- group: design
  href: https://artifacts.apis.io/hookbridge/json-ld/hookbridge-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hookbridge-context.jsonld
- group: design
  href: https://artifacts.apis.io/hookbridge/vocabulary/hookbridge-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/hookbridge-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/hookbridge/conventions/hookbridge-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/hookbridge-conventions.yml
- group: design
  href: https://artifacts.apis.io/hookbridge/conventions/hookbridge-conventions.yml
  title: ''
  type: Conventions
  url: conventions/hookbridge-conventions.yml
- group: design
  href: https://artifacts.apis.io/hookbridge/conformance/hookbridge-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hookbridge-conformance.yml
- group: operate
  href: https://artifacts.apis.io/hookbridge/rate-limits/hookbridge-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/hookbridge-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/hookbridge/data-model/hookbridge-data-model.yml
  title: ''
  type: DataModel
  url: data-model/hookbridge-data-model.yml
- group: build
  href: https://artifacts.apis.io/hookbridge/cli/hookbridge-cli.yml
  title: ''
  type: CLI
  url: cli/hookbridge-cli.yml
- group: auth
  href: https://artifacts.apis.io/hookbridge/authentication/hookbridge-authentication.yml
  title: ''
  type: Authentication
  url: authentication/hookbridge-authentication.yml
- group: design
  href: https://artifacts.apis.io/hookbridge/errors/hookbridge-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/hookbridge-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/hookbridge/llms/hookbridge-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hookbridge-llms.txt
- group: other
  href: https://artifacts.apis.io/hookbridge/hosts/hookbridge-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hookbridge-hosts.yml
- group: other
  href: https://artifacts.apis.io/hookbridge/vendors/hookbridge-vendors.yml
  title: ''
  type: Vendors
  url: vendors/hookbridge-vendors.yml
- group: build
  href: https://artifacts.apis.io/hookbridge/packages/hookbridge-packages.yml
  title: ''
  type: SDKs
  url: packages/hookbridge-packages.yml
- group: build
  href: https://artifacts.apis.io/hookbridge/packages/hookbridge-packages.yml
  title: ''
  type: Packages
  url: packages/hookbridge-packages.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hookbridge
- group: auth
  href: https://artifacts.apis.io/hookbridge/security/hookbridge-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hookbridge-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hookbridge.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.hookbridge.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.hookbridge.io/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.hookbridge.io/getting-started/introduction/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.hookbridge.io/pricing.html
- group: company
  title: ''
  type: Blog
  url: https://www.hookbridge.io/blog.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hookbridge.io/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hookbridge.io/privacy.html
created: '2026-10-17'
description: Hookbridge provides a webhook delivery service that ensures reliable event transmission with automatic retries, signature verification, and flexible delivery modes including send, receive, and pull. The platform offers developer tools, a GitHub Action for CI testing, comprehensive documentation, pricing plans, and a blog with engineering guides. It targets SaaS products needing robust webhook infrastructure, simplifying integration and improving reliability for customers.
json_schemas:
- name: CreateInboundEndpointRequest
  property_count: 20
  slug: hookbridge-create-inbound-endpoint-request
- name: CreateInboundEndpointResponse
  property_count: 2
  slug: hookbridge-create-inbound-endpoint-response
- name: GetSubscriptionResponse
  property_count: 2
  slug: hookbridge-get-subscription-response
- name: ListenInboundEndpointResponse
  property_count: 2
  slug: hookbridge-listen-inbound-endpoint-response
- name: MessageSummary
  property_count: 14
  slug: hookbridge-message-summary
- name: UpdateInboundEndpointRequest
  property_count: 18
  slug: hookbridge-update-inbound-endpoint-request
jsonld:
- class_count: 100
  name: Hookbridge Context
  property_count: 149
  slug: hookbridge-context
layout: provider
modified: '2026-10-17'
name: Hookbridge
nav: Providers
network: true
overview: 'Hookbridge publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including API API, and 1 more. Tagged areas include Company, Webhook, Software-as-a-Service, and Integration.


  The Hookbridge catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Hookbridge''s developer surface includes CLI, authentication, documentation, API reference, getting-started guide, pricing, engineering blog, and 19 more developer resources.'
random_paper: 22
rate_limits:
- limit_count: 3
  name: Hookbridge Rate Limits
  slug: hookbridge-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: Hookbridge API Rules
  rule_count: 15
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 3
  slug: hookbridge-rules
score:
  band: developing
  composite: 45.7
  coverage:
    artifact_dirs: 21
    catalog_earned: 67.8
    catalog_earned_first_party: 12.0
    catalog_gap: 47.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 31.6
    contract_governance: 22.0
    contract_quality: 55.0
    developer_ergonomics: 57.1
    discoverability: 53.6
    operational_transparency: 36.8
  previous_composite: 46.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Hookbridge Authentication
  slug: hookbridge-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Hookbridge Domain Security
  slug: hookbridge-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hookbridge
tags:
- Company
- Webhook
- Software-as-a-Service
- Integration
website: https://hookbridge.io/
---
