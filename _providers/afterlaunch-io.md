---
access_model:
  confidence: low
  label: Freemium (free trial)
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: true
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: derived
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Public API for AfterLaunch product automation
  name: AfterLaunch API
  slug: afterlaunch-api
- baseURL: https://afterlaunch.io
  baseurl_source: declared
  description: 'AfterLaunch is the agentic growth engine: continuous measurement of how a product gets found, kept as a record and ranked into briefed growth moves. This API is access to one AfterLaunch product run: '
  name: AfterLaunch public API API
  slug: afterlaunch-public-api-api
artifact_total: 7
common:
- group: commercial
  href: https://artifacts.apis.io/afterlaunch-io/plans/afterlaunch-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/afterlaunch-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/afterlaunch-io/rules/afterlaunch-io-rules.yml
  title: ''
  type: Spectral
  url: rules/afterlaunch-io-rules.yml
- group: design
  href: https://artifacts.apis.io/afterlaunch-io/json-ld/afterlaunch-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/afterlaunch-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/afterlaunch-io/vocabulary/afterlaunch-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/afterlaunch-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/afterlaunch-io/data-model/afterlaunch-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/afterlaunch-io-data-model.yml
- group: design
  href: https://artifacts.apis.io/afterlaunch-io/conventions/afterlaunch-io-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/afterlaunch-io-conventions.yml
- group: design
  href: https://artifacts.apis.io/afterlaunch-io/conventions/afterlaunch-io-conventions.yml
  title: ''
  type: Conventions
  url: conventions/afterlaunch-io-conventions.yml
- group: design
  href: https://artifacts.apis.io/afterlaunch-io/errors/afterlaunch-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/afterlaunch-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/afterlaunch-io/conformance/afterlaunch-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/afterlaunch-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/afterlaunch-io/llms/afterlaunch-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/afterlaunch-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/afterlaunch-io/mcp/afterlaunch-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/afterlaunch-io-mcp.yml
- group: agent
  href: https://artifacts.apis.io/afterlaunch-io/well-known/afterlaunch-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/afterlaunch-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/afterlaunch-io/hosts/afterlaunch-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/afterlaunch-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/afterlaunch-io/vendors/afterlaunch-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/afterlaunch-io-vendors.yml
- group: build
  href: https://artifacts.apis.io/afterlaunch-io/packages/afterlaunch-io-packages.yml
  title: ''
  type: SDKs
  url: packages/afterlaunch-io-packages.yml
- group: build
  href: https://artifacts.apis.io/afterlaunch-io/packages/afterlaunch-io-packages.yml
  title: ''
  type: Packages
  url: packages/afterlaunch-io-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://afterlaunch.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://afterlaunch.io/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://afterlaunch.io/pricing
- group: start
  title: ''
  type: Login
  url: https://afterlaunch.io/login
- group: docs
  title: ''
  type: Documentation
  url: https://afterlaunch.io/guides
- group: docs
  title: ''
  type: APIReference
  url: https://afterlaunch.io/developers
- group: auth
  href: https://artifacts.apis.io/afterlaunch-io/security/afterlaunch-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/afterlaunch-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://afterlaunch.io/
created: '2026-10-31'
description: AfterLaunch offers an organic growth engine for AI search and SEO that scans a website and returns ranked growth moves to improve visibility on Google and leading AI search engines. The service connects to a user’s AI agent and provides free scans, recommendations, and tools such as an AI crawlability checker and entity check. It is aimed at founders and businesses that want to increase AI‑driven discovery of their products.
image: https://afterlaunch.io/opengraph-image-pwu6ef/v3?2bfc49a6cb33939a
jsonld:
- class_count: 1
  name: Afterlaunch Io Context
  property_count: 1
  slug: afterlaunch-io-context
layout: provider
mcp_servers:
- description: Remote MCP server at afterlaunch.io requiring an API key.
  name: AfterLaunch MCP Server
  slug: afterlaunch-io-mcp-yml
modified: '2026-10-31'
name: AfterLaunch
nav: Providers
network: true
overview: 'AfterLaunch publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including public API API, and 1 more. Tagged areas include SEO, AI Search, Growth Engine, Site Scan, and AI Visibility.


  The AfterLaunch catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AfterLaunch''s developer surface includes pricing, documentation, API reference, and 21 more developer resources.'
plans:
- name: Afterlaunch Io Plans Pricing
  plan_count: 2
  slug: afterlaunch-io-plans-pricing
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: AfterLaunch API Rules
  rule_count: 16
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 2
  slug: afterlaunch-io-rules
score:
  band: thin
  composite: 29.4
  coverage:
    artifact_dirs: 17
    catalog_earned: 55.8
    catalog_earned_first_party: 8.0
    catalog_gap: 59.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.7
  facets:
    access_clarity: 43.4
    contract_governance: 22.0
    contract_quality: 30.7
    developer_ergonomics: 15.5
    discoverability: 65.0
    operational_transparency: 0.0
  previous_composite: 36.1
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Afterlaunch Io Domain Security
  slug: afterlaunch-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: afterlaunch-io
tags:
- SEO
- AI Search
- Growth Engine
- Site Scan
- AI Visibility
- Software-as-a-Service
- Founder Tools
website: https://afterlaunch.io/
---
