---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    error_semantics: false
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
  score: 19.7
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API documented at Claudeers documentation pages.
  name: Claudeers API
  slug: claudeers-api
- description: 'Claudeers API as documented publicly: 34 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: Claudeers API
  slug: claudeers-com-api
artifact_total: 12
common:
- group: commercial
  href: https://artifacts.apis.io/claudeers-com/plans/claudeers-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/claudeers-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/claudeers-com/rules/claudeers-com-rules.yml
  title: ''
  type: Spectral
  url: rules/claudeers-com-rules.yml
- group: design
  href: https://artifacts.apis.io/claudeers-com/json-ld/claudeers-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/claudeers-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/claudeers-com/vocabulary/claudeers-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/claudeers-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/claudeers-com/data-model/claudeers-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/claudeers-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/claudeers-com/conformance/claudeers-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/claudeers-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/claudeers-com/llms/claudeers-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/claudeers-com-llms.txt
- group: other
  href: https://artifacts.apis.io/claudeers-com/hosts/claudeers-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/claudeers-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/claudeers-com/vendors/claudeers-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/claudeers-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://claudeers.com/terms
- group: auth
  title: ''
  type: Security
  url: https://claudeers.com/tag/security
- group: start
  title: ''
  type: Sandbox
  url: https://claudeers.com/tag/sandbox
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://claudeers.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://claudeers.com/pricing
- group: start
  title: ''
  type: Login
  url: https://claudeers.com/signin
- group: docs
  title: ''
  type: Documentation
  url: https://claudeers.com/tag/docs
- group: company
  title: ''
  type: Blog
  url: https://claudeers.com/tag/blog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.astral.sh/uv/?utm_source=claudeers.com&amp;utm_medium=referral&amp;utm_campaign=listing
- group: auth
  href: https://artifacts.apis.io/claudeers-com/security/claudeers-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/claudeers-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://claudeers.com/
coverage:
  checked: '2026-11-04'
  detail: Documentation pages are rendered with JavaScript and no machine‑readable spec was found.
  evidence:
  - status: 200
    url: https://claudeers.com/tag/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-03'
description: Claudeers is the community‑driven registry for Claude AI projects, skills, plugins, MCP servers, and integrations. It helps discover, share, and collaborate on Claude ecosystem resources, providing a searchable index, project pages, and tools for developers to contribute and explore the growing landscape of Claude‑based applications.
image: https://claudeers.com/og-default.png
json_schemas:
- name: PostApiChatRequest
  property_count: 3
  slug: claudeers-com-post-api-chat-request
- name: PostApiConfigQuickSetupRequest
  property_count: 2
  slug: claudeers-com-post-api-config-quick-setup-request
- name: PostV2ScrapeResponse
  property_count: 1
  slug: claudeers-com-post-v2-scrape-response
- name: PostV2ScrapeScrapeidInteractRequest
  property_count: 1
  slug: claudeers-com-post-v2-scrape-scrapeid-interact-request
- name: PostV2ScrapeScrapeidInteractResponse
  property_count: 3
  slug: claudeers-com-post-v2-scrape-scrapeid-interact-response
- name: PostV2SearchRequest
  property_count: 2
  slug: claudeers-com-post-v2-search-request
jsonld:
- class_count: 8
  name: Claudeers Com Context
  property_count: 13
  slug: claudeers-com-context
layout: provider
modified: '2026-11-03'
name: Claudeers
nav: Providers
network: true
overview: 'Claudeers is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Registry, Community, Project, and Claude.


  The Claudeers catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Claudeers'' developer surface includes sandbox, pricing, documentation, engineering blog, and 16 more developer resources.'
plans:
- name: Claudeers Com Plans Pricing
  plan_count: 0
  slug: claudeers-com-plans-pricing
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 81
  extends:
  - spectral:oas
  name: Claudeers API Rules
  rule_count: 40
  severity_counts:
    error: 35
    hint: 0
    info: 4
    warn: 1
  slug: claudeers-com-rules
score:
  band: emerging
  composite: 23.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 24.7
    developer_ergonomics: 14.3
    discoverability: 64.3
    operational_transparency: 5.3
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
    score: 13.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Claudeers Com Domain Security
  slug: claudeers-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: claudeers-com
tags:
- Artificial Intelligence
- Registry
- Community
- Project
- Claude
website: https://claudeers.com/
---
