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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
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
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Datasink Ing Agentic Access
  operation_count: 9
  slug: datasink-ing-agentic-access
  summary_line: 9 operations · 1 acting
api_count: 1
apis:
- baseURL: https://api.datasink.ing
  baseurl_source: declared
  description: The Documents API from DataSinking — 4 operation(s) for documents.
  name: DataSinking Documents API
  slug: datasink-ing-documents-api
- baseURL: https://api.datasink.ing
  baseurl_source: declared
  description: The Exchanges API from DataSinking — 1 operation(s) for exchanges.
  name: DataSinking Exchanges API
  slug: datasink-ing-exchanges-api
- baseURL: https://api.datasink.ing
  baseurl_source: declared
  description: The Feedback API from DataSinking — 2 operation(s) for feedback.
  name: DataSinking Feedback API
  slug: datasink-ing-feedback-api
- baseURL: https://api.datasink.ing
  baseurl_source: declared
  description: The Free Key API from DataSinking — 1 operation(s) for free key.
  name: DataSinking Free Key API
  slug: datasink-ing-free-key-api
- baseURL: https://api.datasink.ing
  baseurl_source: declared
  description: The Stocks API from DataSinking — 1 operation(s) for stocks.
  name: DataSinking Stocks API
  slug: datasink-ing-stocks-api
artifact_total: 11
common:
- group: agent
  href: https://artifacts.apis.io/datasink-ing/agentic-access/datasink-ing-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/datasink-ing-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/datasink-ing/plans/datasink-ing-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/datasink-ing-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/datasink-ing/rules/datasink-ing-rules.yml
  title: ''
  type: Spectral
  url: rules/datasink-ing-rules.yml
- group: agent
  href: https://artifacts.apis.io/datasink-ing/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/datasink-ing/authentication/datasink-ing-authentication.yml
  title: ''
  type: Authentication
  url: authentication/datasink-ing-authentication.yml
- group: design
  href: https://artifacts.apis.io/datasink-ing/errors/datasink-ing-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/datasink-ing-problem-types.yml
- group: design
  href: https://artifacts.apis.io/datasink-ing/conformance/datasink-ing-conformance.yml
  title: ''
  type: Conformance
  url: conformance/datasink-ing-conformance.yml
- group: agent
  href: https://artifacts.apis.io/datasink-ing/llms/datasink-ing-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/datasink-ing-llms.txt
- group: agent
  href: https://artifacts.apis.io/datasink-ing/well-known/datasink-ing-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/datasink-ing-well-known.yml
- group: other
  href: https://artifacts.apis.io/datasink-ing/hosts/datasink-ing-hosts.yml
  title: ''
  type: Hosts
  url: hosts/datasink-ing-hosts.yml
- group: other
  href: https://artifacts.apis.io/datasink-ing/vendors/datasink-ing-vendors.yml
  title: ''
  type: Vendors
  url: vendors/datasink-ing-vendors.yml
- group: build
  href: https://artifacts.apis.io/datasink-ing/packages/datasink-ing-packages.yml
  title: ''
  type: SDKs
  url: packages/datasink-ing-packages.yml
- group: build
  href: https://artifacts.apis.io/datasink-ing/packages/datasink-ing-packages.yml
  title: ''
  type: Packages
  url: packages/datasink-ing-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://datasink.ing/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://datasink.ing/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://datasink.ing/whats-new
- group: start
  title: ''
  type: GettingStarted
  url: https://datasink.ing/docs/mcp
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.datasink.ing<!--
- group: auth
  href: https://artifacts.apis.io/datasink-ing/security/datasink-ing-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/datasink-ing-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://datasink.ing/
- group: docs
  title: ''
  type: Documentation
  url: https://datasink.ing/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.datasink.ing/openapi.json
- group: commercial
  title: ''
  type: Pricing
  url: https://datasink.ing/pricing
- group: start
  title: ''
  type: SignUp
  url: https://datasink.ing/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/heubme2020/datasinking
- group: operate
  title: ''
  type: Forum
  url: https://datasink.ing/forum
created: '2026-11-05'
description: DataSinking provides full-text financial reports for listed companies across the US, China, Europe, Japan, Korea and Taiwan. The reports are parsed from official disclosures into clean Markdown and served via a simple REST API and MCP server, enabling searchable, structured data access for developers and analysts.
layout: provider
modified: '2026-11-05'
name: DataSinking
nav: Providers
network: true
overview: 'DataSinking publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Documents API, Exchanges API, Feedback API, and 2 more. Tagged areas include Finance, Reports, Markdown, and Data.


  The DataSinking catalog on APIs.io includes 1 Spectral governance ruleset.


  DataSinking''s developer surface includes authentication, changelog, getting-started guide, documentation, API reference, pricing, signup flow, and 19 more developer resources.'
plans:
- name: Datasink Ing Plans Pricing
  plan_count: 2
  slug: datasink-ing-plans-pricing
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 81
  extends:
  - spectral:oas
  name: DataSinking API Rules
  rule_count: 40
  severity_counts:
    error: 38
    hint: 0
    info: 1
    warn: 1
  slug: datasink-ing-rules
score:
  band: developing
  composite: 47.8
  coverage:
    artifact_dirs: 17
    catalog_earned: 42.5
    catalog_earned_first_party: 8.0
    catalog_gap: 72.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 18.2
    contract_quality: 40.8
    developer_ergonomics: 63.7
    discoverability: 53.6
    operational_transparency: 21.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
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
  name: Datasink Ing Authentication
  slug: datasink-ing-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Datasink Ing Domain Security
  slug: datasink-ing-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: datasink-ing-fetch-documents
  slug: datasink-ing-fetch-documents
slug: datasink-ing
tags:
- Finance
- Reports
- Markdown
- Data
website: https://datasink.ing/
---
