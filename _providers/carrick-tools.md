---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 35.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.carrick.tools/mcp
  baseurl_source: declared
  description: 'Carrick API as documented publicly: 6 operations. Contract generated from the documentation by API Evangelist (2026-11-03); not the provider''s own document.'
  name: Carrick API
  slug: carrick-tools-api
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/carrick-tools/plans/carrick-tools-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/carrick-tools-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/carrick-tools/rules/carrick-tools-rules.yml
  title: ''
  type: Spectral
  url: rules/carrick-tools-rules.yml
- group: design
  href: https://artifacts.apis.io/carrick-tools/vocabulary/carrick-tools-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/carrick-tools-vocabulary.yml
- group: build
  href: https://artifacts.apis.io/carrick-tools/cli/carrick-tools-cli.yml
  title: ''
  type: CLI
  url: cli/carrick-tools-cli.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/carrick-tools/carrick/blob/main/SECURITY.md
- group: design
  href: https://artifacts.apis.io/carrick-tools/conformance/carrick-tools-conformance.yml
  title: ''
  type: Conformance
  url: conformance/carrick-tools-conformance.yml
- group: agent
  href: https://artifacts.apis.io/carrick-tools/llms/carrick-tools-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/carrick-tools-llms.txt
- group: auth
  href: https://artifacts.apis.io/carrick-tools/well-known/carrick-tools-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/carrick-tools-security.txt
- group: agent
  href: https://artifacts.apis.io/carrick-tools/well-known/carrick-tools-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/carrick-tools-well-known.yml
- group: other
  href: https://artifacts.apis.io/carrick-tools/hosts/carrick-tools-hosts.yml
  title: ''
  type: Hosts
  url: hosts/carrick-tools-hosts.yml
- group: other
  href: https://artifacts.apis.io/carrick-tools/vendors/carrick-tools-vendors.yml
  title: ''
  type: Vendors
  url: vendors/carrick-tools-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.carrick.tools/quickstart
- group: auth
  href: https://artifacts.apis.io/carrick-tools/security/carrick-tools-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/carrick-tools-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/carrick-tools/security/carrick-tools-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/carrick-tools-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://carrick.tools/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.carrick.tools/
- group: commercial
  title: ''
  type: Pricing
  url: https://carrick.tools/pricing/
- group: company
  title: ''
  type: Blog
  url: https://carrick.tools/blog/
- group: operate
  title: ''
  type: Contact
  url: https://carrick.tools/contact/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/carrick-tools
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://carrick.tools/privacy/
- group: other
  title: ''
  type: CookiesPolicy
  url: https://carrick.tools/cookies/
coverage:
  checked: '2026-11-03'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract is published on the API host.
  evidence:
  - status: 404
    url: https://api.carrick.tools/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: Carrick provides TypeScript codebase intelligence for AI agents and IDEs, building a unified index of services, routes, and types across monorepos. It enables agents to query contracts, detect duplicate implementations, and ensure code changes are safe. The platform offers a free tier for up to 5,000 indexed functions and paid plans for larger teams, with direct support and encrypted data storage.
image: https://carrick.tools/brand/carrick-social-card.png
layout: provider
modified: '2026-11-03'
name: Carrick
nav: Providers
network: true
overview: 'Carrick is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, TypeScript, Code Intelligence, Developer Tools, and Open Source.


  The Carrick catalog on APIs.io includes 1 Spectral governance ruleset.


  Carrick''s developer surface includes CLI, getting-started guide, documentation, pricing, engineering blog, and 17 more developer resources.'
plans:
- name: Carrick Tools Plans Pricing
  plan_count: 4
  slug: carrick-tools-plans-pricing
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 71
  extends:
  - spectral:oas
  name: Carrick API Rules
  rule_count: 30
  severity_counts:
    error: 28
    hint: 0
    info: 1
    warn: 1
  slug: carrick-tools-rules
score:
  band: thin
  composite: 26.3
  coverage:
    artifact_dirs: 16
    catalog_earned: 54.8
    catalog_earned_first_party: 12.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 22.0
    contract_quality: 10.7
    developer_ergonomics: 19.0
    discoverability: 66.1
    operational_transparency: 7.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
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
- kind: domain-security
  name: Carrick Tools Domain Security
  slug: carrick-tools-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Carrick Tools Vulnerability Disclosure
  slug: carrick-tools-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: carrick-tools
tags:
- Artificial Intelligence
- TypeScript
- Code Intelligence
- Developer Tools
- Open Source
website: https://carrick.tools/
---
