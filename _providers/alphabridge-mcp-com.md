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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
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
  score: 31.7
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API documented in the tool reference pages.
  name: AlphaBridge MCP API
  slug: alphabridge-mcp-api
- description: 'AlphaBridge MCP API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: AlphaBridge MCP API
  slug: alphabridge-mcp-com-api
artifact_total: 4
common:
- group: design
  href: https://artifacts.apis.io/alphabridge-mcp-com/rules/alphabridge-mcp-com-rules.yml
  title: ''
  type: Spectral
  url: rules/alphabridge-mcp-com-rules.yml
- group: design
  href: https://artifacts.apis.io/alphabridge-mcp-com/vocabulary/alphabridge-mcp-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/alphabridge-mcp-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/alphabridge-mcp-com/conformance/alphabridge-mcp-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/alphabridge-mcp-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/alphabridge-mcp-com/llms/alphabridge-mcp-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/alphabridge-mcp-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/alphabridge-mcp-com/well-known/alphabridge-mcp-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/alphabridge-mcp-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/alphabridge-mcp-com/hosts/alphabridge-mcp-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alphabridge-mcp-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/alphabridge-mcp-com/vendors/alphabridge-mcp-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/alphabridge-mcp-com-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://alphabridge-mcp.com/Security
- group: auth
  href: https://artifacts.apis.io/alphabridge-mcp-com/security/alphabridge-mcp-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alphabridge-mcp-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://alphabridge-mcp.com/
- group: docs
  title: ''
  type: Documentation
  url: https://alphabridge-mcp.com/docs
- group: operate
  title: ''
  type: Support
  url: https://alphabridge-mcp.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://alphabridge-mcp.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://alphabridge-mcp.com/terms
coverage:
  checked: '2026-11-01'
  detail: Documentation pages exist but no OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract was found.
  evidence:
  - status: 404
    url: https://alphabridge-mcp.com/openapi.json
  - status: 0
    url: https://api.alphabridge-mcp.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: AlphaBridge MCP provides a WordPress MCP server that integrates Claude and ChatGPT into WordPress sites. It offers AI-powered content creation, editing, and site management through a single switch, with free tools and paid Pro features for deeper capabilities like code and plugin updates. The platform supports multiple languages and includes pricing, documentation, and support resources. Users can deploy the plugin directly from the WordPress plugin repository, configure AI settings via an intuitive dashboard, and access a growing library of AI‑driven tools for content, media, taxonomy, and user management. AlphaBridge emphasizes privacy, offering a clear privacy policy and data handling statements, and provides email support for Pro and Agency customers.
image: https://alphabridge-mcp.com/assets/img/og-image.png
layout: provider
modified: '2026-11-01'
name: AlphaBridge MCP
nav: Providers
network: true
overview: 'AlphaBridge MCP is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, WordPress, MCP, and Claude.


  The AlphaBridge MCP catalog on APIs.io includes 1 Spectral governance ruleset.


  AlphaBridge MCP''s developer surface includes documentation, support, and 12 more developer resources.'
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: AlphaBridge MCP API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 1
  slug: alphabridge-mcp-com-rules
score:
  band: emerging
  composite: 15.5
  coverage:
    artifact_dirs: 14
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 77.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.8
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 9.4
    developer_ergonomics: 7.1
    discoverability: 57.1
    operational_transparency: 5.3
  previous_composite: 20.3
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
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Alphabridge Mcp Com Domain Security
  slug: alphabridge-mcp-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: alphabridge-mcp-com
tags:
- Company
- Artificial Intelligence
- WordPress
- MCP
- Claude
- ChatGPT
- Pricing
- Documentation
website: https://alphabridge-mcp.com/
---
