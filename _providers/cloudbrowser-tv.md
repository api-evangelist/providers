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
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 20
  human_in_the_loop: 1
  name: Cloudbrowser Tv Agentic Access
  operation_count: 29
  slug: cloudbrowser-tv-agentic-access
  summary_line: 29 operations · 20 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://cloudbrowser.tv/api/v1
  baseurl_source: declared
  description: The B API from Cloudbrowser — 3 operation(s) for b.
  name: Cloudbrowser B API
  slug: cloudbrowser-tv-b-api
- baseURL: https://cloudbrowser.tv/api/v1
  baseurl_source: declared
  description: The Billing API from Cloudbrowser — 6 operation(s) for billing.
  name: Cloudbrowser Billing API
  slug: cloudbrowser-tv-billing-api
- baseURL: https://cloudbrowser.tv/api/v1
  baseurl_source: declared
  description: The Browsers API from Cloudbrowser — 9 operation(s) for browsers.
  name: Cloudbrowser Browsers API
  slug: cloudbrowser-tv-browsers-api
- baseURL: https://cloudbrowser.tv/api/v1
  baseurl_source: declared
  description: The Library API from Cloudbrowser — 4 operation(s) for library.
  name: Cloudbrowser Library API
  slug: cloudbrowser-tv-library-api
- baseURL: https://cloudbrowser.tv/api/v1
  baseurl_source: declared
  description: The Operations API from Cloudbrowser — 1 operation(s) for operations.
  name: Cloudbrowser Operations API
  slug: cloudbrowser-tv-operations-api
- baseURL: https://cloudbrowser.tv/api/v1
  baseurl_source: declared
  description: The Usage API from Cloudbrowser — 1 operation(s) for usage.
  name: Cloudbrowser Usage API
  slug: cloudbrowser-tv-usage-api
artifact_total: 20
common:
- group: agent
  href: https://artifacts.apis.io/cloudbrowser-tv/agentic-access/cloudbrowser-tv-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cloudbrowser-tv-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/cloudbrowser-tv/plans/cloudbrowser-tv-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cloudbrowser-tv-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/cloudbrowser-tv/rules/cloudbrowser-tv-rules.yml
  title: ''
  type: Spectral
  url: rules/cloudbrowser-tv-rules.yml
- group: design
  href: https://artifacts.apis.io/cloudbrowser-tv/json-ld/cloudbrowser-tv-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cloudbrowser-tv-context.jsonld
- group: design
  href: https://artifacts.apis.io/cloudbrowser-tv/vocabulary/cloudbrowser-tv-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cloudbrowser-tv-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/cloudbrowser-tv/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/cloudbrowser-tv/data-model/cloudbrowser-tv-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cloudbrowser-tv-data-model.yml
- group: build
  href: https://artifacts.apis.io/cloudbrowser-tv/cli/cloudbrowser-tv-cli.yml
  title: ''
  type: CLI
  url: cli/cloudbrowser-tv-cli.yml
- group: design
  href: https://artifacts.apis.io/cloudbrowser-tv/conventions/cloudbrowser-tv-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/cloudbrowser-tv-conventions.yml
- group: design
  href: https://artifacts.apis.io/cloudbrowser-tv/conventions/cloudbrowser-tv-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cloudbrowser-tv-conventions.yml
- group: auth
  href: https://artifacts.apis.io/cloudbrowser-tv/authentication/cloudbrowser-tv-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cloudbrowser-tv-authentication.yml
- group: design
  href: https://artifacts.apis.io/cloudbrowser-tv/errors/cloudbrowser-tv-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cloudbrowser-tv-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cloudbrowser-tv/conformance/cloudbrowser-tv-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cloudbrowser-tv-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cloudbrowser-tv/llms/cloudbrowser-tv-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cloudbrowser-tv-llms.txt
- group: other
  href: https://artifacts.apis.io/cloudbrowser-tv/hosts/cloudbrowser-tv-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cloudbrowser-tv-hosts.yml
- group: other
  href: https://artifacts.apis.io/cloudbrowser-tv/vendors/cloudbrowser-tv-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cloudbrowser-tv-vendors.yml
- group: auth
  href: https://artifacts.apis.io/cloudbrowser-tv/security/cloudbrowser-tv-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cloudbrowser-tv-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cloudbrowser.tv
- group: docs
  title: ''
  type: Documentation
  url: https://cloudbrowser.tv/docs
- group: docs
  title: ''
  type: APIReference
  url: https://cloudbrowser.tv/docs/api
- group: commercial
  title: ''
  type: Pricing
  url: https://cloudbrowser.tv/pricing
- group: company
  title: ''
  type: Blog
  url: https://cloudbrowser.tv/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://cloudbrowser.tv/docs/quickstart
created: '2026-11-02'
description: Cloudbrowser offers a persistent Chrome cloud browser tailored for AI agents, enabling isolated sessions with saved login state, the ability to fork, pause, and resume browsers. Agents can connect via the Chrome DevTools Protocol, view live sessions, and manage browsers through a console or REST API. The platform supports billing, security tokens, and provides an OpenAPI specification for integration.
image: https://cloudbrowser.tv/icon.svg
json_schemas:
- name: BrowserLibraryEntry
  property_count: 15
  slug: cloudbrowser-tv-browser-library-entry
- name: Browser
  property_count: 10
  slug: cloudbrowser-tv-browser
- name: LiveViewGrant
  property_count: 19
  slug: cloudbrowser-tv-live-view-grant
- name: UpdateLiveViewGrant
  property_count: 2
  slug: cloudbrowser-tv-update-live-view-grant
- name: Usage
  property_count: 19
  slug: cloudbrowser-tv-usage
- name: ViewerSession
  property_count: 10
  slug: cloudbrowser-tv-viewer-session
jsonld:
- class_count: 19
  name: Cloudbrowser Tv Context
  property_count: 66
  slug: cloudbrowser-tv-context
layout: provider
modified: '2026-11-02'
name: Cloudbrowser
nav: Providers
network: true
overview: 'Cloudbrowser publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including B API, Billing API, Browsers API, and 3 more. Tagged areas include Artificial Intelligence, Browser, Cloud, Chrome, and Automation.


  The Cloudbrowser catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Cloudbrowser''s developer surface includes CLI, authentication, documentation, API reference, pricing, engineering blog, getting-started guide, and 16 more developer resources.'
plans:
- name: Cloudbrowser Tv Plans Pricing
  plan_count: 3
  slug: cloudbrowser-tv-plans-pricing
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 87
  extends:
  - spectral:oas
  name: Cloudbrowser API Rules
  rule_count: 46
  severity_counts:
    error: 38
    hint: 0
    info: 7
    warn: 1
  slug: cloudbrowser-tv-rules
scopes:
- name: Cloudbrowser Tv Scopes
  scope_count: 0
  slug: cloudbrowser-tv-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 40.6
  coverage:
    artifact_dirs: 30
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 22.0
    contract_quality: 57.4
    developer_ergonomics: 41.0
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: unknown
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
  name: Cloudbrowser Tv Authentication
  slug: cloudbrowser-tv-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Cloudbrowser Tv Domain Security
  slug: cloudbrowser-tv-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: cloudbrowser-tv-general
  slug: cloudbrowser-tv-general
slug: cloudbrowser-tv
tags:
- Artificial Intelligence
- Browser
- Cloud
- Chrome
- Automation
website: https://cloudbrowser.tv
---
