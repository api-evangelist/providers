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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Routemux Com Agentic Access
  operation_count: 1
  slug: routemux-com-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- baseURL: https://api.routemux.com
  baseurl_source: declared
  description: Text conversation and reasoning. All three protocols reach the same models — pick the one your SDK already speaks.
  name: RouteMux Chat Completions API
  slug: routemux-com-chat-completions-api
artifact_total: 6
common:
- group: design
  href: https://artifacts.apis.io/routemux-com/data-model/routemux-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/routemux-com-data-model.yml
- group: agent
  href: https://artifacts.apis.io/routemux-com/agentic-access/routemux-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/routemux-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/routemux-com/rules/routemux-com-rules.yml
  title: ''
  type: Spectral
  url: rules/routemux-com-rules.yml
- group: design
  href: https://artifacts.apis.io/routemux-com/vocabulary/routemux-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/routemux-com-vocabulary.yml
- group: auth
  href: https://artifacts.apis.io/routemux-com/authentication/routemux-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/routemux-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/routemux-com/errors/routemux-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/routemux-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/routemux-com/conformance/routemux-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/routemux-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/routemux-com/llms/routemux-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/routemux-com-llms.txt
- group: other
  href: https://artifacts.apis.io/routemux-com/hosts/routemux-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/routemux-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/routemux-com/vendors/routemux-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/routemux-com-vendors.yml
- group: start
  title: ''
  type: Sandbox
  url: https://routemux.com/console/keys
- group: operate
  title: ''
  type: ChangeLog
  url: https://routemux.com/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://routemux.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/routemux-com/security/routemux-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/routemux-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://routemux.com/
- group: docs
  title: ''
  type: Documentation
  url: https://routemux.com/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://routemux.com/console/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://routemux.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://routemux.com/about#contact
- group: company
  title: ''
  type: Blog
  url: https://routemux.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://routemux.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://routemux.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://routemux.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://routemux.com/privacy
- group: operate
  title: ''
  type: Status
  url: https://routemux.com/status
created: '2026-11-05'
description: RouteMux is an AI gateway that provides unified access to hundreds of AI models from providers such as OpenAI, Anthropic, Google, and others through a single OpenAI‑compatible API. It offers multi‑layer redundancy, refundable prepaid balances, and transparent pricing (e.g., $0.15 per 1M input tokens). The platform includes a console for managing API keys, usage, and billing, and supports various model types including text, image, and video. RouteMux emphasizes reliability, cost‑efficiency, and ease of integration for enterprises seeking to adopt AI services across multiple vendors.
image: https://routemux.com/opengraph-image
json_schemas:
- name: PassthroughBody
  property_count: 0
  slug: routemux-com-passthrough-body
layout: provider
modified: '2026-11-05'
name: RouteMux
nav: Providers
network: true
overview: 'RouteMux publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Chat Completions API. Tagged areas include Artificial Intelligence, Gateways, Multi-Model, Unified API, and Company.


  The RouteMux catalog on APIs.io includes 1 Spectral governance ruleset.


  RouteMux''s developer surface includes authentication, sandbox, changelog, API reference, documentation, getting-started guide, support, and 18 more developer resources.'
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 86
  extends:
  - spectral:oas
  name: RouteMux API Rules
  rule_count: 45
  severity_counts:
    error: 43
    hint: 0
    info: 1
    warn: 1
  slug: routemux-com-rules
score:
  band: developing
  composite: 47.4
  coverage:
    artifact_dirs: 19
    catalog_earned: 48.2
    catalog_earned_first_party: 0.0
    catalog_gap: 66.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 22.0
    contract_quality: 52.7
    developer_ergonomics: 64.3
    discoverability: 66.1
    operational_transparency: 15.8
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
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Routemux Com Authentication
  slug: routemux-com-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Routemux Com Domain Security
  slug: routemux-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: routemux-com
tags:
- Artificial Intelligence
- Gateways
- Multi-Model
- Unified API
- Company
website: https://routemux.com/
---
