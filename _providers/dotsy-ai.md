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
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 51.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 111
  human_in_the_loop: 4
  name: Dotsy Ai Agentic Access
  operation_count: 190
  slug: dotsy-ai-agentic-access
  summary_line: 190 operations · 111 acting · 4 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.dotsy.ai
  baseurl_source: declared
  description: Your account, its workspaces and its API keys.
  name: dotsy Account API
  slug: dotsy-ai-account-api
- baseURL: https://api.dotsy.ai
  baseurl_source: declared
  description: Upload, list and delete images, fonts and other files a site serves.
  name: dotsy Assets API
  slug: dotsy-ai-assets-api
- baseURL: https://api.dotsy.ai
  baseurl_source: declared
  description: 'The site brief: what the site is for, who it serves and how it should sound.'
  name: dotsy Brief API
  slug: dotsy-ai-brief-api
- baseURL: https://api.dotsy.ai
  baseurl_source: declared
  description: Define the fields of a site's collections, edit field values in bulk and export items as CSV.
  name: dotsy Collections API
  slug: dotsy-ai-collections-api
- baseURL: https://api.dotsy.ai
  baseurl_source: declared
  description: Read and write page bodies and other content files in a site's draft.
  name: dotsy Content API
  slug: dotsy-ai-content-api
- baseURL: https://api.dotsy.ai
  baseurl_source: declared
  description: Connect custom domains to a site and check their status.
  name: dotsy Domains API
  slug: dotsy-ai-domains-api
- baseURL: https://api.dotsy.ai
  baseurl_source: declared
  description: Review what changed in the draft, then publish it or discard it.
  name: dotsy Draft & publish API
  slug: dotsy-ai-draft-publish-api
- baseURL: https://api.dotsy.ai
  baseurl_source: declared
  description: Read the submissions a site's forms have collected.
  name: dotsy Forms API
  slug: dotsy-ai-forms-api
- baseURL: https://api.dotsy.ai
  baseurl_source: declared
  description: Start a site without an account using a guest token, then claim it later.
  name: dotsy Guest API
  slug: dotsy-ai-guest-api
- baseURL: https://api.dotsy.ai
  baseurl_source: declared
  description: Bring an existing website into dotsy from its URL.
  name: dotsy Import API
  slug: dotsy-ai-import-api
- baseURL: https://api.dotsy.ai
  baseurl_source: declared
  description: Poll long-running work (imports, bulk content writes, renames) by job id.
  name: dotsy Jobs API
  slug: dotsy-ai-jobs-api
- baseURL: https://api.dotsy.ai
  baseurl_source: declared
  description: Invite people to a site and manage their roles.
  name: dotsy Members API
  slug: dotsy-ai-members-api
- baseURL: https://api.dotsy.ai
  baseurl_source: declared
  description: List a site's pages with their routes, titles and draft state.
  name: dotsy Pages API
  slug: dotsy-ai-pages-api
- baseURL: https://api.dotsy.ai
  baseurl_source: declared
  description: Map URL paths to content, including redirects.
  name: dotsy Routes API
  slug: dotsy-ai-routes-api
- baseURL: https://api.dotsy.ai
  baseurl_source: declared
  description: Create, list, read, update and delete sites.
  name: dotsy Sites API
  slug: dotsy-ai-sites-api
- baseURL: https://api.dotsy.ai
  baseurl_source: declared
  description: Bug reports and the support inbox. This is rolling out.
  name: dotsy Support API
  slug: dotsy-ai-support-api
artifact_total: 30
common:
- group: agent
  href: https://artifacts.apis.io/dotsy-ai/agentic-access/dotsy-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/dotsy-ai-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/dotsy-ai/plans/dotsy-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dotsy-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/dotsy-ai/rules/dotsy-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/dotsy-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/dotsy-ai/json-ld/dotsy-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dotsy-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/dotsy-ai/vocabulary/dotsy-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dotsy-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/dotsy-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/dotsy-ai/data-model/dotsy-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dotsy-ai-data-model.yml
- group: operate
  href: https://artifacts.apis.io/dotsy-ai/changelog/dotsy-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/dotsy-ai-changelog.yml
- group: design
  href: https://artifacts.apis.io/dotsy-ai/errors/dotsy-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dotsy-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/dotsy-ai/conformance/dotsy-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dotsy-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dotsy-ai/llms/dotsy-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dotsy-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/dotsy-ai/well-known/dotsy-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dotsy-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/dotsy-ai/hosts/dotsy-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dotsy-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/dotsy-ai/vendors/dotsy-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dotsy-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dotsy.ai/terms
- group: operate
  title: ''
  type: Support
  url: https://dotsy.ai/help
- group: operate
  title: ''
  type: Roadmap
  url: https://dotsy.ai/roadmap
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dotsy.ai/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://dotsy.ai/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://dotsy.ai/changelog
- group: company
  title: ''
  type: Blog
  url: https://dotsy.ai/blog
- group: docs
  title: ''
  type: Documentation
  url: https://dev.dotsy.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.dotsy.ai`
- group: docs
  title: ''
  type: APIReference
  url: https://api.dotsy.ai/docs
- group: auth
  href: https://artifacts.apis.io/dotsy-ai/authentication/dotsy-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dotsy-ai-authentication.yml
- group: auth
  href: https://artifacts.apis.io/dotsy-ai/security/dotsy-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dotsy-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dotsy.ai/
created: '2026-11-05'
description: dotsy is an agentic platform that enables users to build, edit, and publish their online presence using AI assistants like Claude, ChatGPT, or Cursor. It offers a free, no‑card service that integrates AI-driven website creation, content management, and publishing, positioning itself as a modern solution for personal and business web presence.
json_schemas:
- name: DraftStatusResponse
  property_count: 9
  slug: dotsy-ai-draft-status-response
- name: ImportSiteRequest
  property_count: 10
  slug: dotsy-ai-import-site-request
- name: RouteRequest
  property_count: 12
  slug: dotsy-ai-route-request
- name: Route
  property_count: 16
  slug: dotsy-ai-route
- name: SearchPerformance
  property_count: 18
  slug: dotsy-ai-search-performance
- name: Site
  property_count: 37
  slug: dotsy-ai-site
jsonld:
- class_count: 120
  name: Dotsy Ai Context
  property_count: 316
  slug: dotsy-ai-context
layout: provider
modified: '2026-11-05'
name: dotsy
nav: Providers
network: true
overview: 'dotsy publishes 16 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Assets API, Brief API, and 13 more. Tagged areas include Company, Artificial Intelligence, Website Builder, No-Code, and Free.


  The dotsy catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  dotsy''s developer surface includes changelog, support, pricing, engineering blog, documentation, API reference, authentication, and 20 more developer resources.'
plans:
- name: Dotsy Ai Plans Pricing
  plan_count: 4
  slug: dotsy-ai-plans-pricing
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 103
  extends:
  - spectral:oas
  name: dotsy API Rules
  rule_count: 62
  severity_counts:
    error: 38
    hint: 0
    info: 4
    warn: 20
  slug: dotsy-ai-rules
score:
  band: developing
  composite: 50.3
  coverage:
    artifact_dirs: 23
    catalog_earned: 72.8
    catalog_earned_first_party: 12.0
    catalog_gap: 42.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 22.0
    contract_quality: 61.8
    developer_ergonomics: 47.0
    discoverability: 62.5
    operational_transparency: 21.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 16
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Dotsy Ai Authentication
  slug: dotsy-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Dotsy Ai Domain Security
  slug: dotsy-ai-domain-security
  summary_line: TLSv1.3
skill_count: 2
skills:
- name: dotsy-ai-invite-member
  slug: dotsy-ai-invite-member
- name: dotsy-ai-manage-notifications
  slug: dotsy-ai-manage-notifications
slug: dotsy-ai
tags:
- Company
- Artificial Intelligence
- Website Builder
- No-Code
- Free
website: https://dotsy.ai/
---
