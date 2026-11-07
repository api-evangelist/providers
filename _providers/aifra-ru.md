---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
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
  score: 22.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 1
  name: Aifra Ru Agentic Access
  operation_count: 12
  slug: aifra-ru-agentic-access
  summary_line: 12 operations · 6 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.aifra.ru
  baseurl_source: declared
  description: The Analytics API from AIfra — 1 operation(s) for analytics.
  name: AIfra Analytics API
  slug: aifra-ru-analytics-api
- baseURL: https://api.aifra.ru
  baseurl_source: declared
  description: The Health API from AIfra — 1 operation(s) for health.
  name: AIfra Health API
  slug: aifra-ru-health-api
- baseURL: https://api.aifra.ru
  baseurl_source: declared
  description: The Mcp API from AIfra — 1 operation(s) for mcp.
  name: AIfra MCP API
  slug: aifra-ru-mcp-api
- baseURL: https://api.aifra.ru
  baseurl_source: declared
  description: The Previews API from AIfra — 2 operation(s) for previews.
  name: AIfra Previews API
  slug: aifra-ru-previews-api
- baseURL: https://api.aifra.ru
  baseurl_source: declared
  description: The Ready API from AIfra — 1 operation(s) for ready.
  name: AIfra Ready API
  slug: aifra-ru-ready-api
- baseURL: https://api.aifra.ru
  baseurl_source: declared
  description: The Remote API from AIfra — 4 operation(s) for remote.
  name: AIfra Remote API
  slug: aifra-ru-remote-api
artifact_total: 10
common:
- group: agent
  href: https://artifacts.apis.io/aifra-ru/agentic-access/aifra-ru-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/aifra-ru-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/aifra-ru/rules/aifra-ru-rules.yml
  title: ''
  type: Spectral
  url: rules/aifra-ru-rules.yml
- group: build
  href: https://artifacts.apis.io/aifra-ru/cli/aifra-ru-cli.yml
  title: ''
  type: CLI
  url: cli/aifra-ru-cli.yml
- group: design
  href: https://artifacts.apis.io/aifra-ru/errors/aifra-ru-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aifra-ru-problem-types.yml
- group: design
  href: https://artifacts.apis.io/aifra-ru/conformance/aifra-ru-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aifra-ru-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aifra-ru/llms/aifra-ru-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aifra-ru-llms.txt
- group: other
  href: https://artifacts.apis.io/aifra-ru/hosts/aifra-ru-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aifra-ru-hosts.yml
- group: build
  href: https://artifacts.apis.io/aifra-ru/packages/aifra-ru-packages.yml
  title: ''
  type: SDKs
  url: packages/aifra-ru-packages.yml
- group: build
  href: https://artifacts.apis.io/aifra-ru/packages/aifra-ru-packages.yml
  title: ''
  type: Packages
  url: packages/aifra-ru-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aifra.ru/legal/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aifra.ru/legal/privacy/
- group: start
  title: ''
  type: GettingStarted
  url: https://aifra.ru/en/docs/mcp/
- group: docs
  title: ''
  type: APIReference
  url: https://aifra.ru/docs/
- group: auth
  href: https://artifacts.apis.io/aifra-ru/authentication/aifra-ru-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aifra-ru-authentication.yml
- group: auth
  href: https://artifacts.apis.io/aifra-ru/security/aifra-ru-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aifra-ru-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aifra.ru/
created: '2026-11-01'
description: AIfra provides a SaaS platform for temporary static previews of AI‑generated websites and HTML content. Users can upload a folder or files and receive a secure HTTPS link valid for 48 hours, without needing an account, API key, or domain setup. The service targets developers and AI agents, offering a CLI, REST API, and MCP integration, with special support for viewing previews in Russia without VPN. Documentation, guides, and example projects are publicly available.
image: https://aifra.ru/media/aifra-share.png
layout: provider
modified: '2026-11-01'
name: AIfra
nav: Providers
network: true
overview: 'AIfra publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Analytics API, Health API, MCP API, and 3 more. Tagged areas include Software-as-a-Service, Static-Previews, Artificial Intelligence, CLI, and REST.


  The AIfra catalog on APIs.io includes 1 Spectral governance ruleset.


  AIfra''s developer surface includes CLI, getting-started guide, API reference, authentication, and 12 more developer resources.'
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: AIfra API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 1
  slug: aifra-ru-rules
score:
  band: thin
  composite: 29.1
  coverage:
    artifact_dirs: 15
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.5
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 41.8
    developer_ergonomics: 35.7
    discoverability: 66.1
    operational_transparency: 0.0
  previous_composite: 33.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
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
- kind: authentication
  name: Aifra Ru Authentication
  slug: aifra-ru-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Aifra Ru Domain Security
  slug: aifra-ru-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: aifra-ru
tags:
- Software-as-a-Service
- Static-Previews
- Artificial Intelligence
- CLI
- REST
website: https://aifra.ru/
---
