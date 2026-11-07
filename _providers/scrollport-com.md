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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.1
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Scrollport provides a pay‑per‑use catalog of API tools for AI agents, offering search, scraping, enrichment, and media capabilities via a unified interface.
  name: Scrollport API
  slug: scrollport-api
- baseURL: https://api.scrollport.com
  baseurl_source: declared
  description: 'scrollport-com API as documented publicly: 11 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: scrollport-com API
  slug: scrollport-com-api
artifact_total: 9
common:
- group: design
  href: https://artifacts.apis.io/scrollport-com/rules/scrollport-com-rules.yml
  title: ''
  type: Spectral
  url: rules/scrollport-com-rules.yml
- group: design
  href: https://artifacts.apis.io/scrollport-com/json-ld/scrollport-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/scrollport-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/scrollport-com/vocabulary/scrollport-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/scrollport-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/scrollport-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/scrollport-com/data-model/scrollport-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/scrollport-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/scrollport-com/errors/scrollport-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/scrollport-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/scrollport-com/conformance/scrollport-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/scrollport-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/scrollport-com/llms/scrollport-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/scrollport-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/scrollport-com/well-known/scrollport-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/scrollport-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/scrollport-com/hosts/scrollport-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/scrollport-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/scrollport-com/vendors/scrollport-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/scrollport-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/scrollport-com/security/scrollport-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/scrollport-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://scrollport.com/
- group: docs
  title: ''
  type: Documentation
  url: https://scrollport.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://scrollport.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://scrollport.com/docs/quickstart
- group: operate
  title: ''
  type: Support
  url: https://scrollport.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://scrollport.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://scrollport.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://scrollport.com/start
- group: start
  title: ''
  type: DeveloperPortal
  url: https://scrollport.com/tools
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Scrollport
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://api.scrollport.com/mcp
  - status: 200
    url: https://scrollport.com/
  reason: partner-login
  state: gated
created: '2026-10-31'
description: 'Scrollport is a pay‑per‑use catalog of API tools for AI agents: one connection and one prepaid wallet give an agent verified search, scraping, enrichment, social data and media tools without separate provider accounts, API keys or subscriptions. Optional connected‑app tools use accounts the customer already owns and separately authorises. Scrollport is not the CSS term “scrollport”, which describes the visible area of a scroll container.'
image: https://scrollport.com/favicon-192x192.png
json_schemas:
- name: PostV1AuthInviteRedeemRequest
  property_count: 3
  slug: scrollport-com-post-v1-auth-invite-redeem-request
- name: PostV1AuthInviteRedeemResponse
  property_count: 4
  slug: scrollport-com-post-v1-auth-invite-redeem-response
jsonld:
- class_count: 2
  name: Scrollport Com Context
  property_count: 6
  slug: scrollport-com-context
layout: provider
modified: '2026-10-31'
name: scrollport-com
nav: Providers
network: true
overview: 'scrollport-com is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include AI Agents, API Tools, Pay-Per-Use, Search, and Web Scraping.


  The scrollport-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  scrollport-com''s developer surface includes documentation, API reference, getting-started guide, support, signup flow, and 17 more developer resources.'
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: scrollport-com API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: scrollport-com-rules
scopes:
- name: Scrollport Com Scopes
  scope_count: 0
  slug: scrollport-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 25.9
  coverage:
    artifact_dirs: 27
    catalog_earned: 56.8
    catalog_earned_first_party: 0.0
    catalog_gap: 58.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.7
  facets:
    access_clarity: 17.1
    contract_governance: 22.0
    contract_quality: 20.2
    developer_ergonomics: 27.9
    discoverability: 66.1
    operational_transparency: 2.6
  previous_composite: 34.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
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
screenshot: https://apis.io/screenshots/scrollport-com/scrollport-com-2026-11-03T142853.png
security:
- kind: authentication
  name: Scrollport Com Authentication
  slug: scrollport-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Scrollport Com Domain Security
  slug: scrollport-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: scrollport-com
tags:
- AI Agents
- API Tools
- Pay-Per-Use
- Search
- Web Scraping
website: https://scrollport.com/
---
