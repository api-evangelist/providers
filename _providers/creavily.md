---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: mostly
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 46.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 155
  human_in_the_loop: 16
  name: Creavily Agentic Access
  operation_count: 241
  slug: creavily-agentic-access
  summary_line: 241 operations · 155 acting · 16 human-in-the-loop
api_count: 1
apis:
- baseURL: https://creavily-api.ecomwith.com
  baseurl_source: declared
  description: The Admin API from Creavily — 2 operation(s) for admin.
  name: Creavily Admin API
  slug: creavily-admin-api
- baseURL: https://creavily-api.ecomwith.com
  baseurl_source: declared
  description: The Agent API from Creavily — 24 operation(s) for agent.
  name: Creavily Agent API
  slug: creavily-agent-api
- baseURL: https://creavily-api.ecomwith.com
  baseurl_source: declared
  description: The Analytics API from Creavily — 6 operation(s) for analytics.
  name: Creavily Analytics API
  slug: creavily-analytics-api
- baseURL: https://creavily-api.ecomwith.com
  baseurl_source: declared
  description: The Assets API from Creavily — 6 operation(s) for assets.
  name: Creavily Assets API
  slug: creavily-assets-api
- baseURL: https://creavily-api.ecomwith.com
  baseurl_source: declared
  description: The Auth API from Creavily — 19 operation(s) for auth.
  name: Creavily Auth API
  slug: creavily-auth-api
- baseURL: https://creavily-api.ecomwith.com
  baseurl_source: declared
  description: The Automations API from Creavily — 11 operation(s) for automations.
  name: Creavily Automations API
  slug: creavily-automations-api
- baseURL: https://creavily-api.ecomwith.com
  baseurl_source: declared
  description: The Billing API from Creavily — 17 operation(s) for billing.
  name: Creavily Billing API
  slug: creavily-billing-api
- baseURL: https://creavily-api.ecomwith.com
  baseurl_source: declared
  description: The Blog API from Creavily — 14 operation(s) for blog.
  name: Creavily Blog API
  slug: creavily-blog-api
- baseURL: https://creavily-api.ecomwith.com
  baseurl_source: declared
  description: The Brands API from Creavily — 2 operation(s) for brands.
  name: Creavily Brands API
  slug: creavily-brands-api
- baseURL: https://creavily-api.ecomwith.com
  baseurl_source: declared
  description: The Bridges API from Creavily — 2 operation(s) for bridges.
  name: Creavily Bridges API
  slug: creavily-bridges-api
- baseURL: https://creavily-api.ecomwith.com
  baseurl_source: declared
  description: The Channels API from Creavily — 11 operation(s) for channels.
  name: Creavily Channels API
  slug: creavily-channels-api
- baseURL: https://creavily-api.ecomwith.com
  baseurl_source: declared
  description: The Developer API from Creavily — 7 operation(s) for developer.
  name: Creavily Developer API
  slug: creavily-developer-api
- baseURL: https://creavily-api.ecomwith.com
  baseurl_source: declared
  description: The Engagement API from Creavily — 21 operation(s) for engagement.
  name: Creavily Engagement API
  slug: creavily-engagement-api
- baseURL: https://creavily-api.ecomwith.com
  baseurl_source: declared
  description: The Inquiries API from Creavily — 3 operation(s) for inquiries.
  name: Creavily Inquiries API
  slug: creavily-inquiries-api
- baseURL: https://creavily-api.ecomwith.com
  baseurl_source: declared
  description: The Media API from Creavily — 13 operation(s) for media.
  name: Creavily Media API
  slug: creavily-media-api
- baseURL: https://creavily-api.ecomwith.com
  baseurl_source: declared
  description: The OAuth API from Creavily — 4 operation(s) for oauth.
  name: Creavily OAuth API
  slug: creavily-oauth-api
- baseURL: https://creavily-api.ecomwith.com
  baseurl_source: declared
  description: The Platform API from Creavily — 14 operation(s) for platform.
  name: Creavily Platform API
  slug: creavily-platform-api
- baseURL: https://creavily-api.ecomwith.com
  baseurl_source: declared
  description: The Provider Tools API from Creavily — 2 operation(s) for provider tools.
  name: Creavily Provider Tools API
  slug: creavily-provider-tools-api
- baseURL: https://creavily-api.ecomwith.com
  baseurl_source: declared
  description: The Publishing API from Creavily — 35 operation(s) for publishing.
  name: Creavily Publishing API
  slug: creavily-publishing-api
- baseURL: https://creavily-api.ecomwith.com
  baseurl_source: declared
  description: The System API from Creavily — 4 operation(s) for system.
  name: Creavily System API
  slug: creavily-system-api
- baseURL: https://creavily-api.ecomwith.com
  baseurl_source: declared
  description: The Webhooks API from Creavily — 9 operation(s) for webhooks.
  name: Creavily Webhooks API
  slug: creavily-webhooks-api
artifact_total: 37
asyncapis:
- description: ''
  name: Creavily Webhooks
  slug: creavily-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/creavily/agentic-access/creavily-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/creavily-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/creavily/plans/creavily-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/creavily-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/creavily/rules/creavily-rules.yml
  title: ''
  type: Spectral
  url: rules/creavily-rules.yml
- group: design
  href: https://artifacts.apis.io/creavily/json-ld/creavily-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/creavily-context.jsonld
- group: design
  href: https://artifacts.apis.io/creavily/vocabulary/creavily-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/creavily-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/creavily/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/creavily/asyncapi/creavily-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/creavily-webhooks.yml
- group: design
  href: https://artifacts.apis.io/creavily/data-model/creavily-data-model.yml
  title: ''
  type: DataModel
  url: data-model/creavily-data-model.yml
- group: design
  href: https://artifacts.apis.io/creavily/conventions/creavily-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/creavily-conventions.yml
- group: design
  href: https://artifacts.apis.io/creavily/conventions/creavily-conventions.yml
  title: ''
  type: Conventions
  url: conventions/creavily-conventions.yml
- group: design
  href: https://artifacts.apis.io/creavily/errors/creavily-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/creavily-problem-types.yml
- group: design
  href: https://artifacts.apis.io/creavily/conformance/creavily-conformance.yml
  title: ''
  type: Conformance
  url: conformance/creavily-conformance.yml
- group: agent
  href: https://artifacts.apis.io/creavily/llms/creavily-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/creavily-llms.txt
- group: agent
  href: https://artifacts.apis.io/creavily/well-known/creavily-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/creavily-well-known.yml
- group: other
  href: https://artifacts.apis.io/creavily/hosts/creavily-hosts.yml
  title: ''
  type: Hosts
  url: hosts/creavily-hosts.yml
- group: other
  href: https://artifacts.apis.io/creavily/vendors/creavily-vendors.yml
  title: ''
  type: Vendors
  url: vendors/creavily-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://creavily.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://creavily.com/privacy
- group: start
  title: ''
  type: Login
  url: https://creavily.com/signin
- group: auth
  href: https://artifacts.apis.io/creavily/authentication/creavily-authentication.yml
  title: ''
  type: Authentication
  url: authentication/creavily-authentication.yml
- group: auth
  href: https://artifacts.apis.io/creavily/security/creavily-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/creavily-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://creavily.com/
- group: docs
  title: ''
  type: Documentation
  url: https://creavily.com/developers
- group: commercial
  title: ''
  type: Pricing
  url: https://creavily.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://creavily.com/terms
- group: company
  title: ''
  type: Blog
  url: https://creavily.com/blog
- group: docs
  title: ''
  type: APIReference
  url: https://creavily.com/api/v1/openapi/public.json
created: '2026-11-02'
description: Creavily provides product-aware social publishing for ecommerce brands, enabling preparation of product media, review of channel readiness, scheduling of social posts, and delivery tracking across multiple brand workspaces. Their platform offers scoped API access for integration, supporting free plans with email or Google sign‑up, and delivers receipts from each channel, consolidating comments for streamlined replies.
image: https://creavily.com/brand/og-creavily.jpg
json_schemas:
- name: ChannelAccountPatchRequest
  property_count: 7
  slug: creavily-channel-account-patch-request
- name: ChannelAccountUpsertRequest
  property_count: 12
  slug: creavily-channel-account-upsert-request
- name: HealthReadinessResponse
  property_count: 4
  slug: creavily-health-readiness-response
- name: ProviderCapabilitiesResponse
  property_count: 3
  slug: creavily-provider-capabilities-response
- name: PublishingProfileSaveRequest
  property_count: 10
  slug: creavily-publishing-profile-save-request
- name: StorageReadinessResponse
  property_count: 3
  slug: creavily-storage-readiness-response
jsonld:
- class_count: 54
  name: Creavily Context
  property_count: 224
  slug: creavily-context
layout: provider
modified: '2026-11-02'
name: Creavily
nav: Providers
network: true
overview: 'Creavily publishes 21 API contracts indexed on the [APIs.io](https://apis.io/) network, including Admin API, Agent API, Analytics API, and 18 more. Tagged areas include Social Media, E-Commerce, Publishing, and Automation.


  The Creavily catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Creavily''s developer surface includes support, authentication, documentation, pricing, engineering blog, API reference, and 21 more developer resources.'
plans:
- name: Creavily Plans Pricing
  plan_count: 5
  slug: creavily-plans-pricing
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 97
  extends:
  - spectral:oas
  name: Creavily API Rules
  rule_count: 56
  severity_counts:
    error: 36
    hint: 0
    info: 2
    warn: 18
  slug: creavily-rules
score:
  band: developing
  composite: 42.8
  coverage:
    artifact_dirs: 23
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 66.6
    developer_ergonomics: 25.6
    discoverability: 57.1
    operational_transparency: 7.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 21
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
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Creavily Authentication
  slug: creavily-authentication
  summary_line: apiKey/http · 5 schemes
- kind: domain-security
  name: Creavily Domain Security
  slug: creavily-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 3
skills:
- name: creavily-billing-subscribe-workspace
  slug: creavily-billing-subscribe-workspace
- name: creavily-engagement-manage-comment-reply-automation
  slug: creavily-engagement-manage-comment-reply-automation
- name: creavily-manage-platform-admins
  slug: creavily-manage-platform-admins
slug: creavily
tags:
- Social Media
- E-Commerce
- Publishing
- Automation
website: https://creavily.com/
---
