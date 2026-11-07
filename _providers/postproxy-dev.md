---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: true
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 61.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 91
  human_in_the_loop: 6
  name: Postproxy Dev Agentic Access
  operation_count: 157
  slug: postproxy-dev-agentic-access
  summary_line: 157 operations · 91 acting · 6 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.postproxy.dev
  baseurl_source: declared
  description: Provision and revoke profile-group-scoped API keys. All endpoints require an account-wide API key.
  name: postproxy-dev API Keys API
  slug: postproxy-dev-api-keys-api
- baseURL: https://api.postproxy.dev
  baseurl_source: declared
  description: Public scheduled-posts calendar
  name: postproxy-dev Calendar API
  slug: postproxy-dev-calendar-api
- baseURL: https://api.postproxy.dev
  baseurl_source: declared
  description: Read and reply to comments on published posts
  name: postproxy-dev Comments API
  slug: postproxy-dev-comments-api
- baseURL: https://api.postproxy.dev
  baseurl_source: declared
  description: 1:1 chats and messages
  name: postproxy-dev Direct Messages API
  slug: postproxy-dev-direct-messages-api
- baseURL: https://api.postproxy.dev
  baseurl_source: declared
  description: 'Read and update a Facebook Page''s profile: about, description, website, phone, emails'
  name: postproxy-dev Facebook Page API
  slug: postproxy-dev-facebook-page-api
- baseURL: https://api.postproxy.dev
  baseurl_source: declared
  description: 'Read and update a Business Profile location: hours, attributes, services, food menus, action links, profile media'
  name: postproxy-dev Google Business API
  slug: postproxy-dev-google-business-api
- baseURL: https://api.postproxy.dev
  baseurl_source: declared
  description: Search Instagram's audio library for music and original sounds to attach to reels, and list, accept or decline incoming collaboration invites (Facebook-login profiles)
  name: postproxy-dev Instagram API
  slug: postproxy-dev-instagram-api
- baseURL: https://api.postproxy.dev
  baseurl_source: declared
  description: Create and delete Pinterest boards
  name: postproxy-dev Pinterest API
  slug: postproxy-dev-pinterest-api
- baseURL: https://api.postproxy.dev
  baseurl_source: declared
  description: Account-wide placements and the profile serving each one
  name: postproxy-dev Placements API
  slug: postproxy-dev-placements-api
- baseURL: https://api.postproxy.dev
  baseurl_source: declared
  description: Create, list, publish, and delete posts
  name: postproxy-dev Posts API
  slug: postproxy-dev-posts-api
- baseURL: https://api.postproxy.dev
  baseurl_source: declared
  description: Profile-scoped comments (Google Business reviews, Facebook Page recommendations)
  name: postproxy-dev Profile Comments API
  slug: postproxy-dev-profile-comments-api
- baseURL: https://api.postproxy.dev
  baseurl_source: declared
  description: Workspaces for profiles, credentials, and access scope
  name: postproxy-dev Profile Groups API
  slug: postproxy-dev-profile-groups-api
- baseURL: https://api.postproxy.dev
  baseurl_source: declared
  description: Connected social media profiles
  name: postproxy-dev Profiles API
  slug: postproxy-dev-profiles-api
- baseURL: https://api.postproxy.dev
  baseurl_source: declared
  description: Posting queues with recurring timeslots and priority
  name: postproxy-dev Queues API
  slug: postproxy-dev-queues-api
- baseURL: https://api.postproxy.dev
  baseurl_source: declared
  description: Subscribe to post lifecycle and engagement events
  name: postproxy-dev Webhooks API
  slug: postproxy-dev-webhooks-api
- baseURL: https://api.postproxy.dev
  baseurl_source: declared
  description: List, create, update and delete YouTube playlists
  name: postproxy-dev YouTube API
  slug: postproxy-dev-youtube-api
- baseURL: https://api.postproxy.dev
  baseurl_source: declared
  description: 'WhatsApp Business: message templates, phone number administration, business profile, blocked users, groups, and Click-to-WhatsApp conversions. Conversations themselves use the Direct Messages endpoint'
  name: postproxy-dev Whats App API
  slug: postproxy-dev-whats-app-api
artifact_total: 33
asyncapis:
- description: ''
  name: Postproxy Dev Webhooks
  slug: postproxy-dev-webhooks
common:
- group: auth
  href: https://artifacts.apis.io/postproxy-dev/well-known/postproxy-dev-postproxy-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/postproxy-dev-postproxy-security.txt
- group: agent
  href: https://artifacts.apis.io/postproxy-dev/agentic-access/postproxy-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/postproxy-dev-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/postproxy-dev/plans/postproxy-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/postproxy-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/postproxy-dev/rules/postproxy-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/postproxy-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/postproxy-dev/json-ld/postproxy-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/postproxy-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/postproxy-dev/vocabulary/postproxy-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/postproxy-dev-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/postproxy-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/postproxy-dev/asyncapi/postproxy-dev-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/postproxy-dev-webhooks.yml
- group: design
  href: https://artifacts.apis.io/postproxy-dev/data-model/postproxy-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/postproxy-dev-data-model.yml
- group: operate
  href: https://artifacts.apis.io/postproxy-dev/changelog/postproxy-dev-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/postproxy-dev-changelog.yml
- group: design
  href: https://artifacts.apis.io/postproxy-dev/conventions/postproxy-dev-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/postproxy-dev-conventions.yml
- group: design
  href: https://artifacts.apis.io/postproxy-dev/conventions/postproxy-dev-conventions.yml
  title: ''
  type: Conventions
  url: conventions/postproxy-dev-conventions.yml
- group: auth
  href: https://artifacts.apis.io/postproxy-dev/authentication/postproxy-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/postproxy-dev-authentication.yml
- group: design
  href: https://artifacts.apis.io/postproxy-dev/lifecycle/postproxy-dev-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/postproxy-dev-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/postproxy-dev/errors/postproxy-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/postproxy-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/postproxy-dev/conformance/postproxy-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/postproxy-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/postproxy-dev/llms/postproxy-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/postproxy-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/postproxy-dev/well-known/postproxy-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/postproxy-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/postproxy-dev/hosts/postproxy-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/postproxy-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/postproxy-dev/vendors/postproxy-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/postproxy-dev-vendors.yml
- group: build
  href: https://artifacts.apis.io/postproxy-dev/packages/postproxy-dev-packages.yml
  title: ''
  type: SDKs
  url: packages/postproxy-dev-packages.yml
- group: build
  href: https://artifacts.apis.io/postproxy-dev/packages/postproxy-dev-packages.yml
  title: ''
  type: Packages
  url: packages/postproxy-dev-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://postproxy.dev/terms-conditions/
- group: operate
  title: ''
  type: StatusPage
  url: https://postproxy.statuspage.io/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://postproxy.dev/privacy-policy/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.postproxy.dev\n```\n\n
- group: auth
  href: https://artifacts.apis.io/postproxy-dev/security/postproxy-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/postproxy-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://postproxy.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://postproxy.dev/getting-started/quickstart/
- group: docs
  title: ''
  type: APIReference
  url: https://postproxy.dev/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://postproxy.dev/getting-started/quickstart/
- group: company
  title: ''
  type: Blog
  url: https://postproxy.dev/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/postproxy
- group: commercial
  title: ''
  type: Pricing
  url: https://postproxy.dev/pricing/
created: '2026-10-31'
description: Postproxy provides a unified social media API for agencies, SaaS products, and AI agents, enabling publishing, managing comments, direct messages, and reviews across platforms such as Instagram, TikTok, LinkedIn, X, YouTube, Facebook, Threads, Bluesky, Pinterest, Telegram, and Google Business. The service offers analytics and scheduling capabilities, targeting developers who need a single integration point for multi‑platform social media interactions.
image: https://postproxy.dev/og-image.png
json_schemas:
- name: Comment
  property_count: 20
  slug: postproxy-dev-comment
- name: DmChat
  property_count: 17
  slug: postproxy-dev-dm-chat
- name: DmMessage
  property_count: 31
  slug: postproxy-dev-dm-message
- name: DmMessageSendRequest
  property_count: 17
  slug: postproxy-dev-dm-message-send-request
- name: ProfileComment
  property_count: 15
  slug: postproxy-dev-profile-comment
- name: Profile
  property_count: 13
  slug: postproxy-dev-profile
jsonld:
- class_count: 83
  name: Postproxy Dev Context
  property_count: 218
  slug: postproxy-dev-context
layout: provider
modified: '2026-10-31'
name: postproxy-dev
nav: Providers
network: true
overview: 'postproxy-dev publishes 17 API contracts indexed on the [APIs.io](https://apis.io/) network, including API Keys API, Calendar API, Comments API, and 14 more. Tagged areas include Social Media, Software-as-a-Service, Marketing, and Automation.


  The postproxy-dev catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  postproxy-dev''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, engineering blog, pricing, and 27 more developer resources.'
plans:
- name: Postproxy Dev Plans Pricing
  plan_count: 4
  slug: postproxy-dev-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Postproxy Dev Rate Limits
  slug: postproxy-dev-rate-limits
rules:
- authorship: generated
  effective_rule_count: 114
  extends:
  - spectral:oas
  name: postproxy-dev API Rules
  rule_count: 73
  severity_counts:
    error: 61
    hint: 0
    info: 1
    warn: 11
  slug: postproxy-dev-rules
scopes:
- name: Postproxy Dev Scopes
  scope_count: 0
  slug: postproxy-dev-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 55.0
  coverage:
    artifact_dirs: 35
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.1
  facets:
    access_clarity: 47.4
    contract_governance: 35.6
    contract_quality: 73.1
    developer_ergonomics: 45.7
    discoverability: 57.1
    operational_transparency: 44.7
  previous_composite: 65.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/postproxy-dev/postproxy-dev-2026-11-03T141426.png
security:
- kind: authentication
  name: Postproxy Dev Authentication
  slug: postproxy-dev-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Postproxy Dev Domain Security
  slug: postproxy-dev-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
skill_count: 1
skills:
- name: comments
  slug: postproxy-dev-comments-skill
slug: postproxy-dev
tags:
- Social Media
- Software-as-a-Service
- Marketing
- Automation
website: https://postproxy.dev/
---
