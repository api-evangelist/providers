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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 20.1
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Karakeep API allows programmatic management of bookmarks, lists, tags, highlights, assets, and backups. All endpoints require a Bearer token. Supports cursor‑based pagination.
  name: Karakeep API
  slug: karakeep-api-2
- description: 'Karakeep API as documented publicly: 28 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: Karakeep API
  slug: karakeep-api
artifact_total: 13
common:
- group: commercial
  href: https://artifacts.apis.io/karakeep/plans/karakeep-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/karakeep-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/karakeep/rules/karakeep-rules.yml
  title: ''
  type: Spectral
  url: rules/karakeep-rules.yml
- group: design
  href: https://artifacts.apis.io/karakeep/json-ld/karakeep-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/karakeep-context.jsonld
- group: design
  href: https://artifacts.apis.io/karakeep/vocabulary/karakeep-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/karakeep-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/karakeep/data-model/karakeep-data-model.yml
  title: ''
  type: DataModel
  url: data-model/karakeep-data-model.yml
- group: auth
  href: https://artifacts.apis.io/karakeep/security/karakeep-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/karakeep-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/karakeep/conformance/karakeep-conformance.yml
  title: ''
  type: Conformance
  url: conformance/karakeep-conformance.yml
- group: agent
  href: https://artifacts.apis.io/karakeep/llms/karakeep-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/karakeep-llms.txt
- group: auth
  href: https://artifacts.apis.io/karakeep/well-known/karakeep-try-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/karakeep-try-security.txt
- group: auth
  href: https://artifacts.apis.io/karakeep/well-known/karakeep-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/karakeep-security.txt
- group: agent
  href: https://artifacts.apis.io/karakeep/well-known/karakeep-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/karakeep-well-known.yml
- group: other
  href: https://artifacts.apis.io/karakeep/hosts/karakeep-hosts.yml
  title: ''
  type: Hosts
  url: hosts/karakeep-hosts.yml
- group: other
  href: https://artifacts.apis.io/karakeep/vendors/karakeep-vendors.yml
  title: ''
  type: Vendors
  url: vendors/karakeep-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.karakeep.com/getting-started/screenshots
- group: auth
  href: https://artifacts.apis.io/karakeep/security/karakeep-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/karakeep-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/karakeep/security/karakeep-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/karakeep-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://karakeep.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.karakeep.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.karakeep.com/api/karakeep-api
- group: commercial
  title: ''
  type: Pricing
  url: https://karakeep.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://karakeep.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://karakeep.com/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.karakeep.dev/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/karakeep-app
- group: company
  title: ''
  type: Blog
  url: https://karakeep.com/blog/
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://karakeep.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Karakeep provides a bookmark‑everything app that lets users save, organize, and tag links, notes, images, and PDFs across devices. Using AI it automatically tags content for fast retrieval, offers full‑text and semantic search, automation rules, and collaborative lists. The platform is open‑source, self‑hostable via Docker, and also offers a cloud service with a CLI and agentic skills for AI assistants.
image: https://karakeep.com/opengraph-image.png
json_schemas:
- name: PatchBookmarksBookmarkidRequest
  property_count: 5
  slug: karakeep-patch-bookmarks-bookmarkid-request
- name: PostBookmarksBookmarkidSummarizeResponse
  property_count: 3
  slug: karakeep-post-bookmarks-bookmarkid-summarize-response
- name: PostBookmarksResponse
  property_count: 4
  slug: karakeep-post-bookmarks-response
- name: PostHighlightsResponse
  property_count: 4
  slug: karakeep-post-highlights-response
- name: PostListsResponse
  property_count: 3
  slug: karakeep-post-lists-response
- name: PutAdminUsersUseridResponse
  property_count: 5
  slug: karakeep-put-admin-users-userid-response
jsonld:
- class_count: 11
  name: Karakeep Context
  property_count: 4
  slug: karakeep-context
layout: provider
modified: '2026-10-28'
name: Karakeep
nav: Providers
network: true
overview: 'Karakeep is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Bookmarking, AI, Collaboration, and OpenSource.


  The Karakeep catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Karakeep''s developer surface includes getting-started guide, documentation, API reference, pricing, engineering blog, and 20 more developer resources.'
plans:
- name: Karakeep Plans Pricing
  plan_count: 4
  slug: karakeep-plans-pricing
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Karakeep API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: karakeep-rules
score:
  band: thin
  composite: 38.1
  coverage:
    artifact_dirs: 17
    catalog_earned: 66.8
    catalog_earned_first_party: 12.0
    catalog_gap: 48.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 22.0
    contract_quality: 22.6
    developer_ergonomics: 31.0
    discoverability: 57.1
    operational_transparency: 31.6
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 9
      marker_coverage: 100.0
      total: 9
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Karakeep Domain Security
  slug: karakeep-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Karakeep Vulnerability Disclosure
  slug: karakeep-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: karakeep
tags:
- Company
- Bookmarking
- AI
- Collaboration
- OpenSource
website: https://karakeep.com/
---
