---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Key-authenticated REST gateway over the same publishing pipeline as the PosteAhora web app.
  name: PosteAhora API
  slug: posteahora-api
- baseURL: https://api.posteahora.com/functions/v1/api
  baseurl_source: declared
  description: The Accounts API from PosteAhora — 3 operation(s) for accounts.
  name: PosteAhora Accounts API
  slug: posteahora-accounts-api
- baseURL: https://api.posteahora.com/functions/v1/api
  baseurl_source: declared
  description: The Analytics API from PosteAhora — 1 operation(s) for analytics.
  name: PosteAhora Analytics API
  slug: posteahora-analytics-api
- baseURL: https://api.posteahora.com/functions/v1/api
  baseurl_source: declared
  description: The Ideas API from PosteAhora — 2 operation(s) for ideas.
  name: PosteAhora Ideas API
  slug: posteahora-ideas-api
- baseURL: https://api.posteahora.com/functions/v1/api
  baseurl_source: declared
  description: The Media API from PosteAhora — 1 operation(s) for media.
  name: PosteAhora Media API
  slug: posteahora-media-api
- baseURL: https://api.posteahora.com/functions/v1/api
  baseurl_source: declared
  description: The Posts API from PosteAhora — 3 operation(s) for posts.
  name: PosteAhora Posts API
  slug: posteahora-posts-api
artifact_total: 19
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://posteahora.com/blog/rss.xml
- group: other
  href: https://artifacts.apis.io/posteahora/capabilities/posteahora-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/posteahora-capability-edges.yml
- group: design
  href: https://artifacts.apis.io/posteahora/rules/posteahora-rules.yml
  title: ''
  type: Spectral
  url: rules/posteahora-rules.yml
- group: design
  href: https://artifacts.apis.io/posteahora/json-ld/posteahora-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/posteahora-context.jsonld
- group: design
  href: https://artifacts.apis.io/posteahora/vocabulary/posteahora-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/posteahora-vocabulary.yml
- group: commercial
  href: https://artifacts.apis.io/posteahora/plans/posteahora-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/posteahora-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/posteahora/data-model/posteahora-data-model.yml
  title: ''
  type: DataModel
  url: data-model/posteahora-data-model.yml
- group: operate
  href: https://artifacts.apis.io/posteahora/changelog/posteahora-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/posteahora-changelog.yml
- group: auth
  href: https://artifacts.apis.io/posteahora/authentication/posteahora-authentication.yml
  title: ''
  type: Authentication
  url: authentication/posteahora-authentication.yml
- group: design
  href: https://artifacts.apis.io/posteahora/errors/posteahora-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/posteahora-problem-types.yml
- group: design
  href: https://artifacts.apis.io/posteahora/conformance/posteahora-conformance.yml
  title: ''
  type: Conformance
  url: conformance/posteahora-conformance.yml
- group: agent
  href: https://artifacts.apis.io/posteahora/llms/posteahora-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/posteahora-llms.txt
- group: other
  href: https://artifacts.apis.io/posteahora/hosts/posteahora-hosts.yml
  title: ''
  type: Hosts
  url: hosts/posteahora-hosts.yml
- group: other
  href: https://artifacts.apis.io/posteahora/vendors/posteahora-vendors.yml
  title: ''
  type: Vendors
  url: vendors/posteahora-vendors.yml
- group: build
  href: https://artifacts.apis.io/posteahora/packages/posteahora-packages.yml
  title: ''
  type: SDKs
  url: packages/posteahora-packages.yml
- group: build
  href: https://artifacts.apis.io/posteahora/packages/posteahora-packages.yml
  title: ''
  type: Packages
  url: packages/posteahora-packages.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://posteahora.com/docs/quickstart
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/posteahora
- group: auth
  href: https://artifacts.apis.io/posteahora/security/posteahora-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/posteahora-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://posteahora.com/
- group: docs
  title: ''
  type: Documentation
  url: https://posteahora.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://posteahora.com/docs/api
- group: company
  title: ''
  type: Blog
  url: https://posteahora.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://posteahora.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://posteahora.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://posteahora.com/privacy
- group: operate
  title: ''
  type: Roadmap
  url: https://posteahora.com/roadmap
- group: operate
  title: ''
  type: Changelog
  url: https://posteahora.com/changelog
created: '2026-09-27'
description: PosteAhora provides an AI‑driven social media automation platform that lets creators and businesses schedule, cross‑post, and analyze content across multiple networks via a single dashboard. It offers an MCP (Model Context Protocol) server enabling Claude, ChatGPT, Perplexity, Cursor and other AI agents to plan, write, schedule and publish posts automatically. Plans start at $24/month for up to 5 channels, with unlimited posts and API/MCP access.
finops:
- has_sources: true
  method: derived
  name: Posteahora Finops
  primary_unit: seat
  service_category: ''
  slug: posteahora-finops
  template: false
image: https://posteahora.com/og-image.png
json_schemas:
- name: Account
  property_count: 8
  slug: posteahora-account
- name: AnalyticsResult
  property_count: 3
  slug: posteahora-analytics-result
- name: CreatePostRequest
  property_count: 13
  slug: posteahora-create-post-request
- name: IdeaInput
  property_count: 6
  slug: posteahora-idea-input
- name: Post
  property_count: 12
  slug: posteahora-post
- name: UpdatePostRequest
  property_count: 11
  slug: posteahora-update-post-request
jsonld:
- class_count: 22
  name: Posteahora Context
  property_count: 104
  slug: posteahora-context
layout: provider
modified: '2026-10-06'
name: PosteAhora
nav: Providers
network: true
overview: 'PosteAhora publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Analytics API, Ideas API, and 3 more. Tagged areas include Company, Social Media, AI Automation, Marketing, and Software-as-a-Service.


  The PosteAhora catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  PosteAhora''s developer surface includes changelog, authentication, getting-started guide, documentation, API reference, engineering blog, pricing, and 21 more developer resources.'
plans:
- name: Posteahora Plans Pricing
  plan_count: 4
  slug: posteahora-plans-pricing
- name: Posteahora Price Estimates
  plan_count: 0
  slug: posteahora-price-estimates
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: PosteAhora API Rules
  rule_count: 12
  severity_counts:
    error: 9
    hint: 0
    info: 2
    warn: 1
  slug: posteahora-rules
score:
  band: developing
  composite: 50.2
  coverage:
    artifact_dirs: 24
    catalog_earned: 77.8
    catalog_earned_first_party: 12.0
    catalog_gap: 37.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.2
  facets:
    access_clarity: 55.3
    contract_governance: 35.6
    contract_quality: 71.1
    developer_ergonomics: 34.5
    discoverability: 73.2
    operational_transparency: 21.1
  previous_composite: 56.4
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 5
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/posteahora/posteahora-2026-10-11T112726.png
security:
- kind: authentication
  name: Posteahora Authentication
  slug: posteahora-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Posteahora Domain Security
  slug: posteahora-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: posteahora
tags:
- Company
- Social Media
- AI Automation
- Marketing
- Software-as-a-Service
website: https://posteahora.com/
---
