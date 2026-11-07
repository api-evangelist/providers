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
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 23.6
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Weav provides AI-powered customer service APIs as described in their documentation.
  name: Weav API
  slug: weav-api
- baseURL: https://api.weav.com
  baseurl_source: declared
  description: 'weav-com API as documented publicly: 30 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: weav-com API
  slug: weav-com-api
artifact_total: 14
asyncapis:
- description: ''
  name: Weav Com Webhooks
  slug: weav-com-webhooks
common:
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.weav.com/google-groups-setup
- group: commercial
  href: https://artifacts.apis.io/weav-com/plans/weav-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/weav-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/weav-com/rules/weav-com-rules.yml
  title: ''
  type: Spectral
  url: rules/weav-com-rules.yml
- group: design
  href: https://artifacts.apis.io/weav-com/json-ld/weav-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/weav-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/weav-com/vocabulary/weav-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/weav-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/weav-com/asyncapi/weav-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/weav-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/weav-com/data-model/weav-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/weav-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/weav-com/conformance/weav-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/weav-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/weav-com/llms/weav-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/weav-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/weav-com/mcp/weav-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/weav-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/weav-com/well-known/weav-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/weav-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/weav-com/hosts/weav-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/weav-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/weav-com/vendors/weav-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/weav-com-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://app.weav.com/sign-in
- group: operate
  title: ''
  type: ChangeLog
  url: https://weav.com/changelog
- group: auth
  href: https://artifacts.apis.io/weav-com/security/weav-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/weav-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://weav.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.weav.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.weav.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.weav.com/api-introduction
- group: operate
  title: ''
  type: Support
  url: https://weav.com/contact
- group: company
  title: ''
  type: Blog
  url: https://weav.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://weav.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://weav.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://weav.com/privacy
coverage:
  checked: '2026-10-30'
  detail: Documentation site renders content via JavaScript, preventing machine-readable spec discovery.
  evidence:
  - status: 200
    url: https://docs.weav.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-30'
description: Weav provides AI-powered customer service solutions that learn from a company’s website and documentation to automatically resolve customer inquiries. The platform offers customizable AI agents, integrates with various channels, and includes tools for training, workflow automation, and analytics. It aims to reduce support headcount while improving response accuracy and speed, serving brands seeking scalable, intelligent support experiences.
image: https://framerusercontent.com/assets/osAv9IQb5LAtZvrFN8zwRONww2c.png
json_schemas:
- name: GetV1CustomersResponse
  property_count: 1
  slug: weav-com-get-v1-customers-response
- name: GetV1KbArticlesIdResponse
  property_count: 10
  slug: weav-com-get-v1-kb-articles-id-response
- name: GetV1KbArticlesResponse
  property_count: 1
  slug: weav-com-get-v1-kb-articles-response
- name: GetV1MessagesResponse
  property_count: 1
  slug: weav-com-get-v1-messages-response
- name: PostV1KbArticlesResponse
  property_count: 10
  slug: weav-com-post-v1-kb-articles-response
- name: PutV1KbArticlesIdResponse
  property_count: 10
  slug: weav-com-put-v1-kb-articles-id-response
jsonld:
- class_count: 36
  name: Weav Com Context
  property_count: 51
  slug: weav-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at weav.com.
  name: weav-com MCP Server
  slug: weav-com-mcp-yml
modified: '2026-10-30'
name: weav-com
nav: Providers
network: true
overview: 'weav-com is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Customer Service, Automation, Software-as-a-Service, and Chatbots.


  The weav-com catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  weav-com''s developer surface includes getting-started guide, changelog, documentation, API reference, support, engineering blog, pricing, and 18 more developer resources.'
plans:
- name: Weav Com Plans Pricing
  plan_count: 4
  slug: weav-com-plans-pricing
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: weav-com API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: weav-com-rules
score:
  band: thin
  composite: 35.0
  coverage:
    artifact_dirs: 20
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.6
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 36.1
    developer_ergonomics: 22.6
    discoverability: 66.7
    operational_transparency: 15.8
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 45.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 13.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/weav-com/weav-com-2026-11-03T150034.png
security:
- kind: domain-security
  name: Weav Com Domain Security
  slug: weav-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: weav-com
tags:
- Artificial Intelligence
- Customer Service
- Automation
- Software-as-a-Service
- Chatbots
website: https://weav.com/
---
