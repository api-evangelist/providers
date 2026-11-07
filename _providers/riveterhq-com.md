---
access_model:
  confidence: high
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
  - rate-limits
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
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 51.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 63
  human_in_the_loop: 3
  name: Riveterhq Com Agentic Access
  operation_count: 117
  slug: riveterhq-com-agentic-access
  summary_line: 117 operations · 63 acting · 3 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.riveterhq.com/v1
  baseurl_source: declared
  description: Account and API key information
  name: riveterhq-com Account API
  slug: riveterhq-com-account-api
- baseURL: https://api.riveterhq.com/v1
  baseurl_source: declared
  description: 'Templated list builds (`cds_...`): a list generation whose prompt and columns staff configured for your account, run with `parameters` and a `tier`. The rows land in a dataset named by the run''s `data'
  name: riveterhq-com Configured list builds API
  slug: riveterhq-com-configured-list-builds-api
- baseURL: https://api.riveterhq.com/v1
  baseurl_source: declared
  description: Tables Riveter keeps for you — rows you send or Riveter generates, filled column by column by an enrichment ([POST /enrich](#tag/enrich/post/enrich) with `dataset_id`). The preferred way to enrich dat
  name: riveterhq-com Datasets API
  slug: riveterhq-com-datasets-api
- baseURL: https://api.riveterhq.com/v1
  baseurl_source: declared
  description: Fill in new columns for rows — a dataset's rows ([POST /enrich](#tag/enrich/post/enrich) with `dataset_id`, the preferred way) or rows sent inline for a one-off — and manage saved enrichment configura
  name: riveterhq-com Enrich API
  slug: riveterhq-com-enrich-api
- baseURL: https://api.riveterhq.com/v1
  baseurl_source: declared
  description: Reusable site scrape/extract recipes and their runs
  name: riveterhq-com Extractions API
  slug: riveterhq-com-extractions-api
- baseURL: https://api.riveterhq.com/v1
  baseurl_source: declared
  description: A dataset filled again on a schedule, each cell compared with the previous run, with webhooks
  name: riveterhq-com Monitors API
  slug: riveterhq-com-monitors-api
- baseURL: https://api.riveterhq.com/v1
  baseurl_source: declared
  description: 'The uniform lifecycle for every async operation — status, results, stop. **The run** (returned by kickoffs and every `/runs` endpoint): ```json { "id": "run_018f6a70-1234-7abc-89ab-0123456789ab", "typ'
  name: riveterhq-com Runs API
  slug: riveterhq-com-runs-api
- baseURL: https://api.riveterhq.com/v1
  baseurl_source: declared
  description: Synchronous and quick utilities — web search and scraping.
  name: riveterhq-com Tools API
  slug: riveterhq-com-tools-api
artifact_total: 24
common:
- group: agent
  href: https://artifacts.apis.io/riveterhq-com/agentic-access/riveterhq-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/riveterhq-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/riveterhq-com/rate-limits/riveterhq-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/riveterhq-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/riveterhq-com/plans/riveterhq-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/riveterhq-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/riveterhq-com/rules/riveterhq-com-rules.yml
  title: ''
  type: Spectral
  url: rules/riveterhq-com-rules.yml
- group: design
  href: https://artifacts.apis.io/riveterhq-com/json-ld/riveterhq-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/riveterhq-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/riveterhq-com/vocabulary/riveterhq-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/riveterhq-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/riveterhq-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/riveterhq-com/data-model/riveterhq-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/riveterhq-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/riveterhq-com/conventions/riveterhq-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/riveterhq-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/riveterhq-com/conventions/riveterhq-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/riveterhq-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/riveterhq-com/authentication/riveterhq-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/riveterhq-com-authentication.yml
- group: operate
  href: https://artifacts.apis.io/riveterhq-com/lifecycle/riveterhq-com-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/riveterhq-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/riveterhq-com/lifecycle/riveterhq-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/riveterhq-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/riveterhq-com/errors/riveterhq-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/riveterhq-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/riveterhq-com/conformance/riveterhq-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/riveterhq-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/riveterhq-com/llms/riveterhq-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/riveterhq-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/riveterhq-com/mcp/riveterhq-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/riveterhq-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/riveterhq-com/well-known/riveterhq-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/riveterhq-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/riveterhq-com/hosts/riveterhq-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/riveterhq-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/riveterhq-com/vendors/riveterhq-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/riveterhq-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/riveterhq-com/packages/riveterhq-com-packages.yml
  title: ''
  type: SDKs
  url: packages/riveterhq-com-packages.yml
- group: build
  href: https://artifacts.apis.io/riveterhq-com/packages/riveterhq-com-packages.yml
  title: ''
  type: Packages
  url: packages/riveterhq-com-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://www.riveterhq.com/support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.riveterhq.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.riveterhq.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.riveterhq.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://www.riveterhq.com/press
- group: start
  title: ''
  type: Login
  url: https://app.riveterhq.com/login
- group: company
  title: ''
  type: Blog
  url: https://www.riveterhq.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://docs.riveterhq.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.riveterhq.com
- group: auth
  href: https://artifacts.apis.io/riveterhq-com/security/riveterhq-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/riveterhq-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://riveterhq.com/
created: '2026-10-31'
description: Riveter provides an AI‑powered web data extraction and enrichment API that lets developers describe data needs in plain language. Its agents search the live web, navigate pages, handle bot detection and proxies, and return structured datasets via a single API endpoint. The platform supports PDFs, images, and third‑party APIs, offering scalable, reliable access for e‑commerce, marketing, finance, product engineering, and more.
image: https://www.riveterhq.com/images/Meta-image.jpg
json_schemas:
- name: DatasetRow
  property_count: 8
  slug: riveterhq-com-dataset-row
- name: Dataset
  property_count: 12
  slug: riveterhq-com-dataset
- name: Enrichment
  property_count: 12
  slug: riveterhq-com-enrichment
- name: Monitor
  property_count: 22
  slug: riveterhq-com-monitor
- name: Run
  property_count: 19
  slug: riveterhq-com-run
- name: ToolCatalog
  property_count: 2
  slug: riveterhq-com-tool-catalog
jsonld:
- class_count: 34
  name: Riveterhq Com Context
  property_count: 158
  slug: riveterhq-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.riveterhq.com requiring an API key.
  name: riveterhq-com MCP Server
  slug: riveterhq-com-mcp-yml
modified: '2026-10-31'
name: riveterhq-com
nav: Providers
network: true
overview: 'riveterhq-com publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Configured list builds API, Datasets API, and 5 more. Tagged areas include Artificial Intelligence, Web Data, Extraction, Data Enrichment, and Automation.


  The riveterhq-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  riveterhq-com''s developer surface includes authentication, support, pricing, engineering blog, documentation, API reference, and 27 more developer resources.'
plans:
- name: Riveterhq Com Plans Pricing
  plan_count: 3
  slug: riveterhq-com-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 1
  name: Riveterhq Com Rate Limits
  slug: riveterhq-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: riveterhq-com API Rules
  rule_count: 17
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 2
  slug: riveterhq-com-rules
scopes:
- name: Riveterhq Com Scopes
  scope_count: 0
  slug: riveterhq-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 49.9
  coverage:
    artifact_dirs: 34
    catalog_earned: 82.8
    catalog_earned_first_party: 20.0
    catalog_gap: 32.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.2
  facets:
    access_clarity: 48.7
    contract_governance: 22.0
    contract_quality: 68.0
    developer_ergonomics: 37.4
    discoverability: 65.8
    operational_transparency: 36.8
  previous_composite: 57.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/riveterhq-com/riveterhq-com-2026-11-03T142334.png
security:
- kind: authentication
  name: Riveterhq Com Authentication
  slug: riveterhq-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Riveterhq Com Domain Security
  slug: riveterhq-com-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: riveterhq-com-enrich
  slug: riveterhq-com-enrich
slug: riveterhq-com
tags:
- Artificial Intelligence
- Web Data
- Extraction
- Data Enrichment
- Automation
website: https://riveterhq.com/
---
