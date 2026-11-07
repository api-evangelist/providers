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
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
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
  score: 33.1
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Unified social media API and MCP platform
  name: WoopSocial API
  slug: woopsocial-api
- baseURL: https://api.woopsocial.com/v1
  baseurl_source: declared
  description: This is the public-facing OpenAPI contract for WoopSocial. It supports scheduling posts for various social media platforms such as Bluesky, Facebook, Instagram, LinkedIn, LinkedIn Pages, Pinterest, Th
  name: woopsocial-com Openapi API
  slug: woopsocial-com-openapi-api
- baseURL: https://api.woopsocial.com/v1
  baseurl_source: declared
  description: This is the public-facing OpenAPI contract for WoopSocial. It supports scheduling posts for various social media platforms such as Facebook, Instagram, LinkedIn, LinkedIn Pages, Pinterest, TikTok, X (
  name: woopsocial-com Out.Openapi API
  slug: woopsocial-com-out-openapi-api
artifact_total: 17
asyncapis:
- description: ''
  name: Woopsocial Com Webhooks
  slug: woopsocial-com-webhooks
common:
- group: design
  href: https://artifacts.apis.io/woopsocial-com/data-model/woopsocial-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/woopsocial-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/woopsocial-com/errors/woopsocial-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/woopsocial-com-problem-types.yml
- group: commercial
  href: https://artifacts.apis.io/woopsocial-com/plans/woopsocial-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/woopsocial-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/woopsocial-com/rules/woopsocial-com-rules.yml
  title: ''
  type: Spectral
  url: rules/woopsocial-com-rules.yml
- group: design
  href: https://artifacts.apis.io/woopsocial-com/json-ld/woopsocial-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/woopsocial-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/woopsocial-com/vocabulary/woopsocial-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/woopsocial-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/woopsocial-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/woopsocial-com/asyncapi/woopsocial-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/woopsocial-com-webhooks.yml
- group: auth
  href: https://artifacts.apis.io/woopsocial-com/authentication/woopsocial-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/woopsocial-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/woopsocial-com/conformance/woopsocial-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/woopsocial-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/woopsocial-com/llms/woopsocial-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/woopsocial-com-llms.txt
- group: other
  href: https://artifacts.apis.io/woopsocial-com/a2a/woopsocial-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/woopsocial-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/woopsocial-com/well-known/woopsocial-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/woopsocial-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/woopsocial-com/hosts/woopsocial-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/woopsocial-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/woopsocial-com/vendors/woopsocial-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/woopsocial-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/woopsocial-com/packages/woopsocial-com-packages.yml
  title: ''
  type: SDKs
  url: packages/woopsocial-com-packages.yml
- group: build
  href: https://artifacts.apis.io/woopsocial-com/packages/woopsocial-com-packages.yml
  title: ''
  type: Packages
  url: packages/woopsocial-com-packages.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.woopsocial.com/api-reference/api-onboarding
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/WoopSocial
- group: auth
  href: https://artifacts.apis.io/woopsocial-com/security/woopsocial-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/woopsocial-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://woopsocial.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.woopsocial.com/api-reference/overview
- group: commercial
  title: ''
  type: Pricing
  url: https://woopsocial.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://woopsocial.com/blog
- group: company
  title: ''
  type: About
  url: https://woopsocial.com/about
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://woopsocial.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://woopsocial.com/terms-of-service
created: '2026-10-31'
description: WoopSocial provides a unified social media API and a Multi‑Channel Publishing (MCP) platform for AI agents and developers. It offers tools for engagement calculation, image resizing, UTM generation, and content scheduling across major platforms like X/Twitter, LinkedIn, Pinterest, Instagram, Threads, BlueSky, Facebook, TikTok, and YouTube. The service includes a developer portal, pricing plans, and comprehensive documentation for integrating social media functionalities into applications.
image: https://woopsocial.com/images/WoopSocial%20Featured%20Image.png
json_schemas:
- name: CreateOAuthAuthorizationRequest
  property_count: 3
  slug: woopsocial-com-create-oauth-authorization-request
- name: CreatePostRequest
  property_count: 5
  slug: woopsocial-com-create-post-request
- name: Post
  property_count: 9
  slug: woopsocial-com-post
- name: SocialAccount
  property_count: 6
  slug: woopsocial-com-social-account
- name: UploadSession
  property_count: 5
  slug: woopsocial-com-upload-session
- name: UploadSessionStatus
  property_count: 0
  slug: woopsocial-com-upload-session-status
- name: ValidatePostResponse
  property_count: 3
  slug: woopsocial-com-validate-post-response
jsonld:
- class_count: 93
  name: Woopsocial Com Context
  property_count: 107
  slug: woopsocial-com-context
layout: provider
modified: '2026-10-31'
name: woopsocial-com
nav: Providers
network: true
overview: 'woopsocial-com publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network, including Openapi API, Out.Openapi API, and 1 more. Tagged areas include Company, Social Media, MCP, and AI Agents.


  The woopsocial-com catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  woopsocial-com''s developer surface includes authentication, getting-started guide, documentation, pricing, engineering blog, and 22 more developer resources.'
plans:
- name: Woopsocial Com Plans Pricing
  plan_count: 4
  slug: woopsocial-com-plans-pricing
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 97
  extends:
  - spectral:oas
  name: woopsocial-com API Rules
  rule_count: 56
  severity_counts:
    error: 46
    hint: 0
    info: 3
    warn: 7
  slug: woopsocial-com-rules
score:
  band: developing
  composite: 40.6
  coverage:
    artifact_dirs: 23
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.4
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 56.2
    developer_ergonomics: 32.7
    discoverability: 57.1
    operational_transparency: 10.5
  previous_composite: 48.0
  provenance:
    conformance: derived
    mcp: unknown
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
- kind: authentication
  name: Woopsocial Com Authentication
  slug: woopsocial-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Woopsocial Com Domain Security
  slug: woopsocial-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: posts
  slug: woopsocial-com-posts
slug: woopsocial-com
tags:
- Company
- Social Media
- MCP
- AI Agents
website: https://woopsocial.com/
---
