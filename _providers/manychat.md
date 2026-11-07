---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 22
  human_in_the_loop: 0
  name: Manychat Agentic Access
  operation_count: 35
  slug: manychat-agentic-access
  summary_line: 35 operations · 22 acting
api_count: 3
apis:
- baseURL: https://api.manychat.com
  baseurl_source: declared
  description: 'Page-level configuration for a connected ManyChat page: connected page info, tags, typed custom user field definitions, global bot fields, automations (flows) and folders, growth tools and One-Time No'
  name: ManyChat Page API
  slug: manychat-page-api
- baseURL: https://api.manychat.com
  baseurl_source: declared
  description: 'Send Dynamic Block content and trigger automations for a subscriber across Messenger, Instagram and WhatsApp. 3 operations. This is the surface governed by Meta policy rather than by ManyChat: outside'
  name: ManyChat Sending API
  slug: manychat-sending-api
- baseURL: https://api.manychat.com
  baseurl_source: declared
  description: Look up, search, create, update, tag and set custom field values on subscribers. 15 operations. A subscriber carries per-channel identity fields for Messenger, Instagram, WhatsApp, email and SMS on on
  name: ManyChat Subscriber API
  slug: manychat-subscriber-api
- baseURL: https://api.manychat.com
  baseurl_source: declared
  description: White-label profile / template management (Profile API)
  name: ManyChat Template API
  slug: manychat-template-api
artifact_total: 23
asyncapis:
- description: ''
  name: Manychat Dynamic Block Webhooks
  slug: manychat-dynamic-block-webhooks
collections:
- collection_type: open
  name: ManyChat Page API
  slug: open-manychat-page-api
- collection_type: open
  name: ManyChat Profile API
  slug: open-manychat-profile-api
- collection_type: open
  name: ManyChat Sending API
  slug: open-manychat-sending-api
- collection_type: open
  name: ManyChat Subscriber API
  slug: open-manychat-subscriber-api
- collection_type: open
  name: ManyChat API
  slug: open-manychat
common:
- group: company
  title: ''
  type: Blog
  url: https://manychat.com/blog/
- group: other
  href: https://artifacts.apis.io/manychat/capabilities/manychat-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/manychat-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/manychat/overlays/manychat-profile-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/manychat-profile-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/manychat/agentic-access/manychat-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/manychat-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/manychat/security/manychat-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/manychat-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://manychat.com/security/vulnerability
- group: auth
  href: https://artifacts.apis.io/manychat/security/manychat-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/manychat-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/manychat/authentication/manychat-authentication.yml
  title: ''
  type: Authentication
  url: authentication/manychat-authentication.yml
- group: design
  href: https://artifacts.apis.io/manychat/conventions/manychat-conventions.yml
  title: ''
  type: Conventions
  url: conventions/manychat-conventions.yml
- group: design
  href: https://artifacts.apis.io/manychat/conformance/manychat-conformance.yml
  title: ''
  type: Conformance
  url: conformance/manychat-conformance.yml
- group: design
  href: https://artifacts.apis.io/manychat/errors/manychat-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/manychat-problem-types.yml
- group: design
  href: https://artifacts.apis.io/manychat/data-model/manychat-data-model.yml
  title: ''
  type: DataModel
  url: data-model/manychat-data-model.yml
- group: operate
  href: https://artifacts.apis.io/manychat/rate-limits/manychat-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/manychat-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/manychat/plans/manychat-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/manychat-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/manychat/lifecycle/manychat-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/manychat-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.manychat.com
- group: build
  href: https://artifacts.apis.io/manychat/packages/manychat-packages.yml
  title: ''
  type: Packages
  url: packages/manychat-packages.yml
- group: build
  href: https://artifacts.apis.io/manychat/packages/manychat-packages.yml
  title: ''
  type: SDKs
  url: packages/manychat-packages.yml
- group: design
  href: https://artifacts.apis.io/manychat/vocabulary/manychat-dynamic-block-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/manychat-dynamic-block-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/manychat/asyncapi/manychat-dynamic-block-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/manychat-dynamic-block-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/manychat/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/manychat/llms/manychat-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/manychat-llms.txt
- group: agent
  href: https://artifacts.apis.io/manychat/well-known/manychat-well-known.yml
  title: ''
  type: WellKnownProbe
  url: well-known/manychat-well-known.yml
- group: agent
  href: https://artifacts.apis.io/manychat/mcp/manychat-mcp.yml
  title: ''
  type: MCPCandidate
  url: mcp/manychat-mcp.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/manychat
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/manychat
- group: company
  title: ''
  type: Website
  url: https://manychat.com
- group: docs
  title: ''
  type: Documentation
  url: https://api.manychat.com/swagger
- group: docs
  title: ''
  type: APIReference
  url: https://api.manychat.com/swagger
- group: start
  title: ''
  type: GettingStarted
  url: https://help.manychat.com/hc/en-us/articles/14281252007580-Dev-Tools-Basics
- group: operate
  title: ''
  type: Support
  url: https://help.manychat.com
- group: operate
  title: ''
  type: Help Center
  url: https://help.manychat.com
- group: operate
  title: ''
  type: Community
  url: https://community.manychat.com
- group: commercial
  title: ''
  type: Pricing
  url: https://manychat.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://manychat.com/signup
created: '2026-05-11'
description: 'ManyChat is a chat-marketing platform that lets businesses build automated conversations and marketing flows across Instagram Direct Messages, Facebook Messenger, WhatsApp, Telegram, TikTok and SMS. It provides a visual flow builder, audience segmentation, broadcasts, growth tools and integrations with ecommerce and CRM systems to drive engagement, lead capture and sales. The public ManyChat REST API is a page-scoped surface of 35 operations covering subscribers, tags, typed custom fields, page-level bot fields, automations and sending, published as OpenAPI 3.0 and served through an interactive Swagger console at api.manychat.com/swagger. Authentication is a per-page API key sent as an Authorization Bearer token in the form page-id:api-key; there is no OAuth, no scopes and no account-wide credential. ManyChat''s only asynchronous surface runs outbound: the External Request flow step calls a partner endpoint and expects a Dynamic Block v2 JSON response back, so the integrator
  is the webhook receiver rather than ManyChat pushing events.'
finops:
- has_sources: true
  method: derived
  name: Manychat Finops
  primary_unit: active contacts
  service_category: ''
  slug: manychat-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/manychat.png
layout: provider
modified: '2026-10-06'
name: ManyChat
nav: Providers
network: true
overview: 'ManyChat publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Page API, Sending API, Subscriber API, and 1 more. Tagged areas include Chat Marketing, Messenger Marketing, Conversational Commerce, Marketing Automation, and Instagram.


  The ManyChat catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  ManyChat''s developer surface includes engineering blog, authentication, documentation, API reference, getting-started guide, support, pricing, and 28 more developer resources.'
plans:
- name: Manychat Plans Pricing
  plan_count: 5
  slug: manychat-plans-pricing
- name: Manychat Price Estimates
  plan_count: 0
  slug: manychat-price-estimates
random_paper: 13
rate_limits:
- limit_count: 35
  name: Manychat Rate Limits
  slug: manychat-rate-limits
rules:
- authorship: generated
  effective_rule_count: 94
  extends:
  - spectral:oas
  name: ManyChat API Rules
  rule_count: 53
  severity_counts:
    error: 51
    hint: 0
    info: 1
    warn: 1
  slug: manychat-rules
score:
  band: strong
  composite: 56.5
  coverage:
    artifact_dirs: 30
    catalog_earned: 76.5
    catalog_earned_first_party: 29.0
    catalog_gap: 38.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 63.2
    contract_governance: 33.3
    contract_quality: 55.4
    developer_ergonomics: 56.5
    discoverability: 71.4
    operational_transparency: 60.5
  previous_composite: 56.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 25.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 23.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/manychat/manychat-2026-06-20T184935.png
security:
- kind: authentication
  name: Manychat Authentication
  slug: manychat-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Manychat Domain Security
  slug: manychat-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Manychat Vulnerability Disclosure
  slug: manychat-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 4
skills:
- name: Answer a ManyChat External Request with a Dynamic Block response
  slug: manychat-answer-external-request
- name: Find a ManyChat subscriber and tag them
  slug: manychat-find-and-tag-subscriber
- name: Manage ManyChat page tags, custom fields and bot fields
  slug: manychat-manage-page-fields-and-tags
- name: Send a ManyChat message inside Meta's messaging policy
  slug: manychat-send-message-within-policy
slug: manychat
tags:
- Chat Marketing
- Messenger Marketing
- Conversational Commerce
- Marketing Automation
- Instagram
- WhatsApp
- Facebook Messenger
- SMS
- Chatbots
- Customer Engagement
- Automation
website: https://manychat.com
---
