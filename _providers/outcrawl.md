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
    agent_skills: false
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Outcrawl Agentic Access
  operation_count: 1
  slug: outcrawl-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- baseURL: https://api.outcrawl.ai
  baseurl_source: declared
  description: The Scrape API from Outcrawl — 1 operation(s) for scrape.
  name: Outcrawl Scrape API
  slug: outcrawl-scrape-api
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/outcrawl/agentic-access/outcrawl-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/outcrawl-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/outcrawl/plans/outcrawl-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/outcrawl-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/outcrawl/rules/outcrawl-rules.yml
  title: ''
  type: Spectral
  url: rules/outcrawl-rules.yml
- group: design
  href: https://artifacts.apis.io/outcrawl/json-ld/outcrawl-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/outcrawl-context.jsonld
- group: design
  href: https://artifacts.apis.io/outcrawl/vocabulary/outcrawl-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/outcrawl-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/outcrawl/data-model/outcrawl-data-model.yml
  title: ''
  type: DataModel
  url: data-model/outcrawl-data-model.yml
- group: build
  href: https://artifacts.apis.io/outcrawl/cli/outcrawl-cli.yml
  title: ''
  type: CLI
  url: cli/outcrawl-cli.yml
- group: auth
  href: https://artifacts.apis.io/outcrawl/authentication/outcrawl-authentication.yml
  title: ''
  type: Authentication
  url: authentication/outcrawl-authentication.yml
- group: design
  href: https://artifacts.apis.io/outcrawl/errors/outcrawl-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/outcrawl-problem-types.yml
- group: design
  href: https://artifacts.apis.io/outcrawl/conformance/outcrawl-conformance.yml
  title: ''
  type: Conformance
  url: conformance/outcrawl-conformance.yml
- group: agent
  href: https://artifacts.apis.io/outcrawl/llms/outcrawl-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/outcrawl-llms.txt
- group: agent
  href: https://artifacts.apis.io/outcrawl/well-known/outcrawl-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/outcrawl-well-known.yml
- group: other
  href: https://artifacts.apis.io/outcrawl/hosts/outcrawl-hosts.yml
  title: ''
  type: Hosts
  url: hosts/outcrawl-hosts.yml
- group: other
  href: https://artifacts.apis.io/outcrawl/vendors/outcrawl-vendors.yml
  title: ''
  type: Vendors
  url: vendors/outcrawl-vendors.yml
- group: build
  href: https://artifacts.apis.io/outcrawl/packages/outcrawl-packages.yml
  title: ''
  type: Packages
  url: packages/outcrawl-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: https://outcrawl.ai/console
- group: build
  title: ''
  type: SDKs
  url: https://outcrawl.ai/platform/sdk
- group: commercial
  title: ''
  type: Pricing
  url: https://outcrawl.ai/pricing
- group: start
  title: ''
  type: Login
  url: https://outcrawl.ai/sign-in
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aeonmindai
- group: docs
  title: ''
  type: APIReference
  url: https://outcrawl.ai/docs/api-reference/scrape/fetch-one-url-and-return-clean-content-in-the-requested-formats
- group: start
  title: ''
  type: GettingStarted
  url: https://outcrawl.ai/docs/getting-started/quickstart
- group: auth
  href: https://artifacts.apis.io/outcrawl/security/outcrawl-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/outcrawl-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://outcrawl.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://outcrawl.ai/docs
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://outcrawl.ai/legal/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://outcrawl.ai/legal/terms
- group: auth
  title: ''
  type: Security
  url: https://outcrawl.ai/legal/security
created: '2026-11-03'
description: Outcrawl provides web infrastructure for AI agents, delivering clean data from any page, searchable results, real browsers in the cloud, and end‑to‑end task completion. Users receive 1,000 free credits each month with no credit card required, enabling developers to integrate web browsing capabilities into their AI workflows without handling authentication or scraping complexities.
image: https://outcrawl.ai/og/home.png?v=271e9bad28
jsonld:
- class_count: 1
  name: Outcrawl Context
  property_count: 3
  slug: outcrawl-context
layout: provider
modified: '2026-11-03'
name: Outcrawl
nav: Providers
network: true
overview: 'Outcrawl publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Scrape API. Tagged areas include Company, Artificial Intelligence, Web Infrastructure, Data Extraction, and Automation.


  The Outcrawl catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Outcrawl''s developer surface includes CLI, authentication, sandbox, pricing, API reference, getting-started guide, documentation, and 21 more developer resources.'
plans:
- name: Outcrawl Plans Pricing
  plan_count: 5
  slug: outcrawl-plans-pricing
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 94
  extends:
  - spectral:oas
  name: Outcrawl API Rules
  rule_count: 53
  severity_counts:
    error: 51
    hint: 0
    info: 1
    warn: 1
  slug: outcrawl-rules
score:
  band: developing
  composite: 44.2
  coverage:
    artifact_dirs: 20
    catalog_earned: 59.8
    catalog_earned_first_party: 12.0
    catalog_gap: 55.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 54.8
    developer_ergonomics: 44.0
    discoverability: 66.1
    operational_transparency: 7.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
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
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Outcrawl Authentication
  slug: outcrawl-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Outcrawl Domain Security
  slug: outcrawl-domain-security
  summary_line: TLSv1.3 · HSTS
slug: outcrawl
tags:
- Company
- Artificial Intelligence
- Web Infrastructure
- Data Extraction
- Automation
website: https://outcrawl.ai/
---
