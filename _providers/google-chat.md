---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Google Chat Agentic Access
  operation_count: 14
  slug: google-chat-agentic-access
  summary_line: 14 operations · 8 acting
api_count: 1
apis:
- baseURL: https://chat.googleapis.com
  baseurl_source: declared
  description: The Google Chat API API from Google Chat — 1 operation(s) for google chat api.
  name: Google Chat Google Chat API
  slug: google-chat-google-chat-api-api
- baseURL: https://chat.googleapis.com
  baseurl_source: declared
  description: The Members API from Google Chat — 1 operation(s) for members.
  name: Google Chat Members API
  slug: google-chat-members-api
- baseURL: https://chat.googleapis.com
  baseurl_source: declared
  description: The Messages API from Google Chat — 1 operation(s) for messages.
  name: Google Chat Messages API
  slug: google-chat-messages-api
- baseURL: https://chat.googleapis.com
  baseurl_source: declared
  description: The Reactions API from Google Chat — 1 operation(s) for reactions.
  name: Google Chat Reactions API
  slug: google-chat-reactions-api
- baseURL: https://chat.googleapis.com
  baseurl_source: declared
  description: The Spaces API from Google Chat — 1 operation(s) for spaces.
  name: Google Chat Spaces API
  slug: google-chat-spaces-api
- baseURL: https://chat.googleapis.com
  baseurl_source: declared
  description: The Spaces:setup API from Google Chat — 1 operation(s) for spaces:setup.
  name: Google Chat Spaces:setup API
  slug: google-chat-spaces-setup-api
- baseURL: https://chat.googleapis.com
  baseurl_source: declared
  description: The Custom Emojis API from Google Chat — 1 operation(s) for custom emojis.
  name: Google Chat Custom Emojis API
  slug: google-chat-custom-emojis-api
artifact_total: 31
collections:
- collection_type: postman
  name: Google Chat customEmojis API
  slug: postman-google-chat-customemojis-api
- collection_type: postman
  name: Google Chat customEmojis Google Chat API API
  slug: postman-google-chat-google-chat-api-api
- collection_type: postman
  name: Google Chat customEmojis Members API
  slug: postman-google-chat-members-api
- collection_type: postman
  name: Google Chat customEmojis Messages API
  slug: postman-google-chat-messages-api
- collection_type: postman
  name: Google Chat customEmojis Reactions API
  slug: postman-google-chat-reactions-api
- collection_type: postman
  name: Google Chat customEmojis Spaces API
  slug: postman-google-chat-spaces-api
- collection_type: postman
  name: Google Chat customEmojis Spaces:setup API
  slug: postman-google-chat-spaces-setup-api
- collection_type: open
  name: Google Chat customEmojis API
  slug: open-google-chat-customemojis-api
- collection_type: open
  name: Google Chat customEmojis Google Chat API API
  slug: open-google-chat-google-chat-api-api
- collection_type: open
  name: Google Chat customEmojis Members API
  slug: open-google-chat-members-api
- collection_type: open
  name: Google Chat customEmojis Messages API
  slug: open-google-chat-messages-api
- collection_type: open
  name: Google Chat customEmojis Reactions API
  slug: open-google-chat-reactions-api
- collection_type: open
  name: Google Chat customEmojis Spaces API
  slug: open-google-chat-spaces-api
- collection_type: open
  name: Google Chat customEmojis Spaces:setup API
  slug: open-google-chat-spaces-setup-api
- collection_type: open
  name: Google Chat API
  slug: open-openapi
common:
- group: other
  href: https://artifacts.apis.io/google-chat/capabilities/google-chat-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/google-chat-capability-edges.yml
- group: commercial
  href: https://artifacts.apis.io/google-chat/plans/google-chat-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/google-chat-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/google-chat/rate-limits/google-chat-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/google-chat-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/google-chat/finops/google-chat-finops.yml
  title: ''
  type: FinOps
  url: finops/google-chat-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.google.com/
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-chat/overview
- group: agent
  href: https://artifacts.apis.io/google-chat/agentic-access/google-chat-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/google-chat-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/google-chat/security/google-chat-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-chat-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/google-chat/security/google-chat-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/google-chat-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/googleworkspace
- group: start
  title: ''
  type: Portal
  url: https://developers.google.com/workspace/chat
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/workspace/chat/api/guides
- group: auth
  title: ''
  type: Authentication
  url: https://developers.google.com/identity/protocols/oauth2
- group: commercial
  title: ''
  type: Pricing
  url: https://workspace.google.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.google.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://www.google.com/appsstatus/dashboard/
- group: operate
  title: ''
  type: Support
  url: https://developers.google.com/workspace/chat/support
- group: company
  title: ''
  type: Blog
  url: https://workspaceupdates.googleblog.com/
- group: design
  href: https://artifacts.apis.io/google-chat/json-ld/json-ld.jsonld
  title: ''
  type: JSONLD
  url: json-ld/json-ld.jsonld
created: '2026-03-13'
description: The Google Chat API enables building Chat apps that integrate with Google Chat. It provides RESTful access to manage Chat spaces, memberships, messages, reactions, attachments, and custom emojis. The API supports creating conversational bots, automating messaging workflows, and managing organizational chat resources programmatically.
finops:
- has_sources: true
  method: derived
  name: Google Chat Finops
  primary_unit: user
  service_category: ''
  slug: google-chat-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-chat.png
jsonld:
- class_count: 4
  name: Json Ld Context
  property_count: 4
  slug: json-ld
layout: provider
modified: '2026-09-16'
name: Google Chat
nav: Providers
network: true
overview: 'Google Chat publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Google Chat API, Members API, Messages API, and 4 more. Tagged areas include Chat, Collaboration, Google, Google Workspace, and Messaging.


  The Google Chat catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Chat''s developer surface includes developer portal, getting-started guide, authentication, pricing, support, engineering blog, and 14 more developer resources.'
plans:
- name: Google Chat Plans Pricing
  plan_count: 4
  slug: google-chat-plans-pricing
- name: Google Chat Price Estimates
  plan_count: 0
  slug: google-chat-price-estimates
random_paper: 18
rate_limits:
- limit_count: 5
  name: Google Chat Rate Limits
  slug: google-chat-rate-limits
rules:
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: Google Chat — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: google-chat-jsonschema-spectral-rules
score:
  band: developing
  composite: 51.6
  coverage:
    artifact_dirs: 17
    catalog_earned: 68.7
    catalog_earned_first_party: 12.0
    catalog_gap: 46.4
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 71.1
    contract_governance: 9.8
    contract_quality: 51.8
    developer_ergonomics: 51.2
    discoverability: 66.1
    operational_transparency: 36.8
  previous_composite: 51.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/google-chat/google-chat-2026-06-20T182033.png
security:
- kind: domain-security
  name: Google Chat Domain Security
  slug: google-chat-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Chat Vulnerability Disclosure
  slug: google-chat-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-chat
tags:
- Chat
- Collaboration
- Google
- Google Workspace
- Messaging
- Spaces
website: https://www.google.com/
---
