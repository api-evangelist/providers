---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
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
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 45.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Buildonto Dev Agentic Access
  operation_count: 7
  slug: buildonto-dev-agentic-access
  summary_line: 7 operations · 6 acting
api_count: 1
apis:
- baseURL: https://api.buildonto.dev
  baseurl_source: declared
  description: Read, score, or extract up to 50 URLs (a list or a whole site) in one call.
  name: Onto Batch API
  slug: buildonto-dev-batch-api
- baseURL: https://api.buildonto.dev
  baseurl_source: declared
  description: Return the structured data a page declares (JSON-LD, OpenGraph, meta). Deterministic, no AI.
  name: Onto Extract API
  slug: buildonto-dev-extract-api
- baseURL: https://api.buildonto.dev
  baseurl_source: declared
  description: Discover a site's URLs via sitemap, then links — without reading them.
  name: Onto Map API
  slug: buildonto-dev-map-api
- baseURL: https://api.buildonto.dev
  baseurl_source: declared
  description: Fetch and clean public URLs into agent-ready Markdown.
  name: Onto Read API
  slug: buildonto-dev-read-api
- baseURL: https://api.buildonto.dev
  baseurl_source: declared
  description: One call, both outputs — Markdown plus the scoring metadata.
  name: Onto Read + Score API
  slug: buildonto-dev-read-score-api
- baseURL: https://api.buildonto.dev
  baseurl_source: declared
  description: Run the AIO scorer on a URL — returns 0–100 score, penalties, benefits, recommendations.
  name: Onto Score API
  slug: buildonto-dev-score-api
- baseURL: https://api.buildonto.dev
  baseurl_source: declared
  description: Plan quota, concurrent-slot state, and credit balance.
  name: Onto Usage API
  slug: buildonto-dev-usage-api
artifact_total: 21
common:
- group: agent
  href: https://artifacts.apis.io/buildonto-dev/agentic-access/buildonto-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/buildonto-dev-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/buildonto-dev/plans/buildonto-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/buildonto-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/buildonto-dev/rules/buildonto-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/buildonto-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/buildonto-dev/json-ld/buildonto-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/buildonto-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/buildonto-dev/vocabulary/buildonto-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/buildonto-dev-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/buildonto-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/buildonto-dev/data-model/buildonto-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/buildonto-dev-data-model.yml
- group: auth
  href: https://artifacts.apis.io/buildonto-dev/authentication/buildonto-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/buildonto-dev-authentication.yml
- group: design
  href: https://artifacts.apis.io/buildonto-dev/errors/buildonto-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/buildonto-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/buildonto-dev/conformance/buildonto-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/buildonto-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/buildonto-dev/llms/buildonto-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/buildonto-dev-llms.txt
- group: auth
  href: https://artifacts.apis.io/buildonto-dev/well-known/buildonto-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/buildonto-dev-security.txt
- group: agent
  href: https://artifacts.apis.io/buildonto-dev/well-known/buildonto-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/buildonto-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/buildonto-dev/hosts/buildonto-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/buildonto-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/buildonto-dev/vendors/buildonto-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/buildonto-dev-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://buildonto.dev/legal/terms
- group: auth
  title: ''
  type: Security
  url: https://buildonto.dev/legal/security
- group: operate
  title: ''
  type: Roadmap
  url: https://buildonto.dev/roadmap
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://buildonto.dev/legal/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://buildonto.dev/pricing
- group: start
  title: ''
  type: Login
  url: https://app.buildonto.dev/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://buildonto.dev/changelog
- group: company
  title: ''
  type: Blog
  url: https://buildonto.dev/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.buildonto.dev/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://docs.buildonto.dev/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.buildonto.dev/reference
- group: auth
  href: https://artifacts.apis.io/buildonto-dev/security/buildonto-dev-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/buildonto-dev-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/buildonto-dev/security/buildonto-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/buildonto-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://buildonto.dev/
created: '2026-11-03'
description: Onto provides a platform that makes website content readable to AI agents by serving clean Markdown at the same URLs. It offers a Read API, an MCP server, and tools for indexing, training data collection, and AI search integration. Free tier includes 1,000 credits per month with no credit card required. The service helps improve AI citation accuracy and reduces hallucinations by providing agents with exact page content.
image: https://buildonto.dev/opengraph-image.png?opengraph-image.789f9c1d.png
json_schemas:
- name: ReadAndScoreResponse
  property_count: 14
  slug: buildonto-dev-read-and-score-response
- name: ReadRequest
  property_count: 2
  slug: buildonto-dev-read-request
- name: ReadResponse
  property_count: 7
  slug: buildonto-dev-read-response
- name: ScoreRequest
  property_count: 1
  slug: buildonto-dev-score-request
- name: ScoreResponse
  property_count: 12
  slug: buildonto-dev-score-response
- name: UsageResponse
  property_count: 10
  slug: buildonto-dev-usage-response
jsonld:
- class_count: 12
  name: Buildonto Dev Context
  property_count: 54
  slug: buildonto-dev-context
layout: provider
modified: '2026-11-03'
name: Onto
nav: Providers
network: true
overview: 'Onto publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Batch API, Extract API, Map API, and 4 more. Tagged areas include Artificial Intelligence, Content, Markdown, Read API, and Platform.


  The Onto catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Onto''s developer surface includes authentication, pricing, changelog, engineering blog, getting-started guide, documentation, API reference, and 22 more developer resources.'
plans:
- name: Buildonto Dev Plans Pricing
  plan_count: 8
  slug: buildonto-dev-plans-pricing
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 109
  extends:
  - spectral:oas
  name: Onto API Rules
  rule_count: 68
  severity_counts:
    error: 62
    hint: 0
    info: 4
    warn: 2
  slug: buildonto-dev-rules
score:
  band: developing
  composite: 46.4
  coverage:
    artifact_dirs: 21
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 68.3
    developer_ergonomics: 29.2
    discoverability: 66.1
    operational_transparency: 15.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
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
  name: Buildonto Dev Authentication
  slug: buildonto-dev-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Buildonto Dev Domain Security
  slug: buildonto-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Buildonto Dev Vulnerability Disclosure
  slug: buildonto-dev-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: read-url
  slug: buildonto-dev-readurl
slug: buildonto-dev
tags:
- Artificial Intelligence
- Content
- Markdown
- Read API
- Platform
website: https://buildonto.dev/
---
