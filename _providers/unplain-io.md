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
    agent_skills: unknown
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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 53.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 10
  human_in_the_loop: 2
  name: Unplain Io Agentic Access
  operation_count: 20
  slug: unplain-io-agentic-access
  summary_line: 20 operations · 10 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://app.unplain.io
  baseurl_source: declared
  description: Machine-readable descriptions of this API.
  name: unplain-io Discovery API
  slug: unplain-io-discovery-api
- baseURL: https://app.unplain.io
  baseurl_source: declared
  description: The public, anonymous feature-request leaderboard.
  name: unplain-io Feature requests API
  slug: unplain-io-feature-requests-api
- baseURL: https://app.unplain.io
  baseurl_source: declared
  description: Model Context Protocol endpoint. One multiplexed JSON-RPC path, API key required.
  name: unplain-io MCP API
  slug: unplain-io-mcp-api
artifact_total: 18
common:
- group: agent
  href: https://artifacts.apis.io/unplain-io/agentic-access/unplain-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/unplain-io-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/unplain-io/plans/unplain-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/unplain-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/unplain-io/rules/unplain-io-rules.yml
  title: ''
  type: Spectral
  url: rules/unplain-io-rules.yml
- group: design
  href: https://artifacts.apis.io/unplain-io/json-ld/unplain-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/unplain-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/unplain-io/vocabulary/unplain-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/unplain-io-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/unplain-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/unplain-io/data-model/unplain-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/unplain-io-data-model.yml
- group: auth
  href: https://artifacts.apis.io/unplain-io/authentication/unplain-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/unplain-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/unplain-io/errors/unplain-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/unplain-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/unplain-io/conformance/unplain-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/unplain-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/unplain-io/llms/unplain-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/unplain-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/unplain-io/well-known/unplain-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/unplain-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/unplain-io/hosts/unplain-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/unplain-io-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://app.unplain.io/auth/sign-in
- group: docs
  title: ''
  type: Documentation
  url: https://unplain.io/guides
- group: docs
  title: ''
  type: APIReference
  url: https://unplain.io/developers
- group: auth
  href: https://artifacts.apis.io/unplain-io/security/unplain-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/unplain-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://unplain.io/
- group: company
  title: ''
  type: Blog
  url: https://unplain.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://unplain.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://unplain.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://unplain.io/privacy
- group: operate
  title: ''
  type: Support
  url: https://unplain.io/contact
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://unplain.io/openapi.json
  - status: null
    url: https://app.unplain.io/openapi.json
  - status: 401
    url: https://app.unplain.io/api/mcp
  - status: 200
    url: https://unplain.io/
  reason: partner-login
  state: gated
created: '2026-10-31'
description: Unplain turns docs, AI drafts and web pages (text, Markdown, Word, or a link to a public page) into publish‑ready PDFs (ebooks, lead magnets, reports and guides) in minutes, with consistent layouts and no manual formatting. It separates writing from design, letting users upload a finished document and automatically generating cover, contents, pagination, branding, and a call‑to‑action page. The service is aimed at marketers, agencies, creators and anyone who wants professional PDFs without a design sprint, offering a free tier and paid plans with unlimited exports and AI image generation.
image: https://unplain.io/og-v3.png
json_schemas:
- name: FeatureListResult
  property_count: 6
  slug: unplain-io-feature-list-result
- name: FeatureRequest
  property_count: 6
  slug: unplain-io-feature-request
- name: JsonRpcRequest
  property_count: 4
  slug: unplain-io-json-rpc-request
- name: JsonRpcResponse
  property_count: 4
  slug: unplain-io-json-rpc-response
- name: SubmitResult
  property_count: 2
  slug: unplain-io-submit-result
- name: VoteResult
  property_count: 3
  slug: unplain-io-vote-result
jsonld:
- class_count: 9
  name: Unplain Io Context
  property_count: 23
  slug: unplain-io-context
layout: provider
modified: '2026-10-31'
name: unplain-io
nav: Providers
network: true
overview: 'unplain-io publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Discovery API, Feature requests API, and MCP API. Tagged areas include Company, PDF, Artificial Intelligence, Marketing, and Software-as-a-Service.


  The unplain-io catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  unplain-io''s developer surface includes authentication, documentation, API reference, engineering blog, pricing, support, and 17 more developer resources.'
plans:
- name: Unplain Io Plans Pricing
  plan_count: 3
  slug: unplain-io-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Unplain Io Rate Limits
  slug: unplain-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: unplain-io API Rules
  rule_count: 15
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 1
  slug: unplain-io-rules
scopes:
- name: Unplain Io Scopes
  scope_count: 0
  slug: unplain-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 44.3
  coverage:
    artifact_dirs: 32
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.4
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 65.1
    developer_ergonomics: 30.2
    discoverability: 66.1
    operational_transparency: 0.0
  previous_composite: 51.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: unknown
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
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/unplain-io/unplain-io-2026-11-03T145451.png
security:
- kind: authentication
  name: Unplain Io Authentication
  slug: unplain-io-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Unplain Io Domain Security
  slug: unplain-io-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: feature-requests
  slug: unplain-io-feature-requests
slug: unplain-io
tags:
- Company
- PDF
- Artificial Intelligence
- Marketing
- Software-as-a-Service
website: https://unplain.io/
---
