---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.9
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Re:amaze provides an API for programmatic access to certain data. API access is provided in a REST-like interface exposing Re:amaze resources in a JSON format.
  name: Re:amaze API
  slug: re-amaze-api
- description: 'Re:amaze API as documented publicly: 43 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: Re:amaze API
  slug: reamaze-api
artifact_total: 14
common:
- group: design
  href: https://artifacts.apis.io/reamaze/rules/reamaze-rules.yml
  title: ''
  type: Spectral
  url: rules/reamaze-rules.yml
- group: design
  href: https://artifacts.apis.io/reamaze/json-ld/reamaze-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/reamaze-context.jsonld
- group: design
  href: https://artifacts.apis.io/reamaze/vocabulary/reamaze-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/reamaze-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/reamaze/data-model/reamaze-data-model.yml
  title: ''
  type: DataModel
  url: data-model/reamaze-data-model.yml
- group: auth
  href: https://artifacts.apis.io/reamaze/security/reamaze-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/reamaze-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/reamaze/conformance/reamaze-conformance.yml
  title: ''
  type: Conformance
  url: conformance/reamaze-conformance.yml
- group: other
  href: https://artifacts.apis.io/reamaze/hosts/reamaze-hosts.yml
  title: ''
  type: Hosts
  url: hosts/reamaze-hosts.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/reamaze
- group: auth
  href: https://artifacts.apis.io/reamaze/security/reamaze-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/reamaze-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/reamaze/security/reamaze-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/reamaze-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://reamaze.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.reamaze.com/developer
- group: docs
  title: ''
  type: Documentation
  url: https://www.reamaze.com/developer
- group: docs
  title: ''
  type: APIReference
  url: https://www.reamaze.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://www.reamaze.com/getting-started
- group: operate
  title: ''
  type: Support
  url: https://www.reamaze.com/support
- group: company
  title: ''
  type: Blog
  url: https://www.reamaze.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.reamaze.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.reamaze.com/signup
- group: start
  title: ''
  type: Login
  url: https://www.reamaze.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.reamaze.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.reamaze.com/privacy
- group: operate
  title: ''
  type: Roadmap
  url: https://www.reamaze.com/roadmap
coverage:
  checked: '2026-10-29'
  detail: The Re:amaze developer pages provide HTML documentation but no publicly accessible OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts.
  evidence:
  - status: 200
    url: https://www.reamaze.com/developer
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Re:amaze provides an AI‑powered customer service and engagement platform designed for eCommerce and online businesses. The simple, intuitive software lets teams support, engage, and convert customers through chat, social media, SMS, FAQ, and email—all from a single interface. Built with AI agents, it helps automate responses, streamline workflows, and deliver a seamless experience that impresses customers and drives sales.
image: https://cdn.reamaze.com/assets/site/logo-mint-256-7b4e082a4d38628b5692747463c52e8ce20e48d500a56a2bf5ec4556e9a5b611.png
json_schemas:
- name: GetApiV1ArticlesResponse
  property_count: 4
  slug: reamaze-get-api-v1-articles-response
- name: GetApiV1ChannelsResponse
  property_count: 2
  slug: reamaze-get-api-v1-channels-response
- name: GetApiV1ChannelsSlugResponse
  property_count: 15
  slug: reamaze-get-api-v1-channels-slug-response
- name: GetApiV1MessagesResponse
  property_count: 9
  slug: reamaze-get-api-v1-messages-response
- name: GetApiV1ReportsChannelSummaryResponse
  property_count: 1
  slug: reamaze-get-api-v1-reports-channel-summary-response
- name: PostConversationsSlugMessagesRequest
  property_count: 9
  slug: reamaze-post-conversations-slug-messages-request
jsonld:
- class_count: 43
  name: Reamaze Context
  property_count: 65
  slug: reamaze-context
layout: provider
modified: '2026-10-28'
name: Re:amaze
nav: Providers
network: true
overview: 'Re:amaze is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Customer Service, Help Desk, Live Chat, Artificial Intelligence, and E-Commerce.


  The Re:amaze catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Re:amaze''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 16 more developer resources.'
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Re:amaze API Rules
  rule_count: 11
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 0
  slug: reamaze-rules
scopes:
- name: Reamaze Scopes
  scope_count: 0
  slug: reamaze-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 26.7
  coverage:
    artifact_dirs: 25
    catalog_earned: 57.0
    catalog_earned_first_party: 0.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.2
  facets:
    access_clarity: 22.4
    contract_governance: 19.7
    contract_quality: 25.2
    developer_ergonomics: 22.6
    discoverability: 57.1
    operational_transparency: 15.8
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 36.9
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/reamaze/reamaze-2026-11-03T142029.png
security:
- kind: authentication
  name: Reamaze Authentication
  slug: reamaze-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Reamaze Domain Security
  slug: reamaze-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Reamaze Vulnerability Disclosure
  slug: reamaze-vulnerability-disclosure
  summary_line: no policy recorded
slug: reamaze
tags:
- Customer Service
- Help Desk
- Live Chat
- Artificial Intelligence
- E-Commerce
website: https://reamaze.com/
---
