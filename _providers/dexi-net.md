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
    agent_card: conformant
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 48.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Dexi Net Agentic Access
  operation_count: 3
  slug: dexi-net-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 1
apis:
- baseURL: https://api.dexi.net
  baseurl_source: declared
  description: The Bookmarks API from Dexi — 1 operation(s) for bookmarks.
  name: Dexi Bookmarks API
  slug: dexi-net-bookmarks-api
- baseURL: https://api.dexi.net
  baseurl_source: declared
  description: The Publisher API from Dexi — 2 operation(s) for publisher.
  name: Dexi Publisher API
  slug: dexi-net-publisher-api
artifact_total: 10
common:
- group: agent
  href: https://artifacts.apis.io/dexi-net/agentic-access/dexi-net-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/dexi-net-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/dexi-net/plans/dexi-net-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dexi-net-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/dexi-net/rules/dexi-net-rules.yml
  title: ''
  type: Spectral
  url: rules/dexi-net-rules.yml
- group: design
  href: https://artifacts.apis.io/dexi-net/json-ld/dexi-net-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dexi-net-context.jsonld
- group: design
  href: https://artifacts.apis.io/dexi-net/vocabulary/dexi-net-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dexi-net-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/dexi-net/data-model/dexi-net-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dexi-net-data-model.yml
- group: auth
  href: https://artifacts.apis.io/dexi-net/authentication/dexi-net-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dexi-net-authentication.yml
- group: operate
  href: https://artifacts.apis.io/dexi-net/lifecycle/dexi-net-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/dexi-net-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/dexi-net/lifecycle/dexi-net-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/dexi-net-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/dexi-net/errors/dexi-net-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dexi-net-problem-types.yml
- group: design
  href: https://artifacts.apis.io/dexi-net/conformance/dexi-net-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dexi-net-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dexi-net/llms/dexi-net-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dexi-net-llms.txt
- group: other
  href: https://artifacts.apis.io/dexi-net/a2a/dexi-net-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/dexi-net-a2a.yml
- group: agent
  href: https://artifacts.apis.io/dexi-net/well-known/dexi-net-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dexi-net-well-known.yml
- group: other
  href: https://artifacts.apis.io/dexi-net/hosts/dexi-net-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dexi-net-hosts.yml
- group: other
  href: https://artifacts.apis.io/dexi-net/vendors/dexi-net-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dexi-net-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dexi.net/terms
- group: operate
  title: ''
  type: Support
  url: https://dexi.net/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dexi.net/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://dexi.net/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dexi
- group: start
  title: ''
  type: SignUp
  url: https://app.dexi.net/account/register
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.dexi.net/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dexi.net/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.dexi.net\
- group: docs
  title: ''
  type: APIReference
  url: https://docs.dexi.net/api/overview
- group: auth
  href: https://artifacts.apis.io/dexi-net/security/dexi-net-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dexi-net-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dexi.net/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://dexi.net/openapi.json
  - status: null
    url: https://docs.dexi.net/mcp
  - status: 401
    url: https://api.dexi.net/mcp
  - status: 200
    url: https://dexi.net/
  reason: partner-login
  state: gated
created: '2026-11-05'
description: Dexi is a personal knowledge management app that consolidates notes, bookmarks, newsletters, and RSS feeds into a searchable workspace. It offers a free starter tier and aims to streamline research and lifelong learning, with features like tagging, full‑text search, and integration with popular services. The official site dexi.net provides documentation, pricing, and a community blog.
image: https://dexi.net/opengraph-image.png?opengraph-image.34lvqa92u32aq.png
json_schemas:
- name: BookmarkSaveResult
  property_count: 4
  slug: dexi-net-bookmark-save-result
- name: PublishedFeed
  property_count: 6
  slug: dexi-net-published-feed
jsonld:
- class_count: 9
  name: Dexi Net Context
  property_count: 19
  slug: dexi-net-context
layout: provider
modified: '2026-11-05'
name: Dexi
nav: Providers
network: true
overview: 'Dexi publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Bookmarks API and Publisher API. Tagged areas include Knowledge Management, Personal-Productivity, Note Taking, Bookmarking, and RSS-Feeds.


  The Dexi catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Dexi''s developer surface includes authentication, support, pricing, signup flow, getting-started guide, documentation, API reference, and 21 more developer resources.'
plans:
- name: Dexi Net Plans Pricing
  plan_count: 3
  slug: dexi-net-plans-pricing
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 98
  extends:
  - spectral:oas
  name: Dexi API Rules
  rule_count: 57
  severity_counts:
    error: 55
    hint: 0
    info: 1
    warn: 1
  slug: dexi-net-rules
score:
  band: strong
  composite: 54.3
  coverage:
    artifact_dirs: 22
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 62.9
    developer_ergonomics: 54.8
    discoverability: 66.1
    operational_transparency: 13.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Dexi Net Authentication
  slug: dexi-net-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Dexi Net Domain Security
  slug: dexi-net-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dexi-net
tags:
- Knowledge Management
- Personal-Productivity
- Note Taking
- Bookmarking
- RSS-Feeds
website: https://dexi.net/
---
