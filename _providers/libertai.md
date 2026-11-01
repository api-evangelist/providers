---
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
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 22.5
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Libertai Agentic Access
  operation_count: 9
  slug: libertai-agentic-access
  summary_line: 9 operations · 2 acting
api_count: 2
apis:
- baseURL: https://api.libertai.io
  baseurl_source: declared
  description: The Aleph Credits API from LibertAI — 1 operation(s) for aleph credits.
  name: LibertAI Aleph Credits API
  slug: libertai-aleph-credits-api
- baseURL: https://api.libertai.io
  baseurl_source: declared
  description: The Auth API from LibertAI — 1 operation(s) for auth.
  name: LibertAI Auth API
  slug: libertai-auth-api
- baseURL: https://api.libertai.io
  baseurl_source: declared
  description: The Health API from LibertAI — 1 operation(s) for health.
  name: LibertAI Health API
  slug: libertai-health-api
- baseURL: https://api.libertai.io
  baseurl_source: declared
  description: The Models API from LibertAI — 3 operation(s) for models.
  name: LibertAI Models API
  slug: libertai-models-api
- baseURL: https://api.libertai.io
  baseurl_source: declared
  description: The Proxy API from LibertAI — 1 operation(s) for proxy.
  name: LibertAI Proxy API
  slug: libertai-proxy-api
- baseURL: https://api.libertai.io
  baseurl_source: declared
  description: The Search API from LibertAI — 2 operation(s) for search.
  name: LibertAI Search API
  slug: libertai-search-api
artifact_total: 16
common:
- group: agent
  href: https://artifacts.apis.io/libertai/agentic-access/libertai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/libertai-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/libertai/plans/libertai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/libertai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/libertai/rules/libertai-rules.yml
  title: ''
  type: Spectral
  url: rules/libertai-rules.yml
- group: design
  href: https://artifacts.apis.io/libertai/json-ld/libertai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/libertai-context.jsonld
- group: design
  href: https://artifacts.apis.io/libertai/vocabulary/libertai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/libertai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/libertai/data-model/libertai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/libertai-data-model.yml
- group: auth
  href: https://artifacts.apis.io/libertai/authentication/libertai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/libertai-authentication.yml
- group: design
  href: https://artifacts.apis.io/libertai/lifecycle/libertai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/libertai-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/libertai/errors/libertai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/libertai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/libertai/conformance/libertai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/libertai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/libertai/llms/libertai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/libertai-llms.txt
- group: agent
  href: https://artifacts.apis.io/libertai/well-known/libertai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/libertai-well-known.yml
- group: other
  href: https://artifacts.apis.io/libertai/hosts/libertai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/libertai-hosts.yml
- group: build
  href: https://artifacts.apis.io/libertai/integrations/libertai-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/libertai-integration-edges.yml
- group: build
  href: https://artifacts.apis.io/libertai/packages/libertai-packages.yml
  title: ''
  type: SDKs
  url: packages/libertai-packages.yml
- group: build
  href: https://artifacts.apis.io/libertai/packages/libertai-packages.yml
  title: ''
  type: Packages
  url: packages/libertai-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.libertai.io/
- group: auth
  href: https://artifacts.apis.io/libertai/security/libertai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/libertai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://libertai.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.libertai.io
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.libertai.io/quickstart.html
- group: company
  title: ''
  type: Blog
  url: https://blog.libertai.io
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Libertai
- group: start
  title: ''
  type: Login
  url: https://console.libertai.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://libertai.io/#pricing
- group: operate
  title: ''
  type: Support
  url: https://t.me/libertai
- group: other
  title: ''
  type: X
  url: https://x.com/Libertai_DAI
created: '2026-10-13'
description: 'LibertAI provides private, TEE-attested AI inference on the decentralized Aleph Cloud network through an OpenAI-compatible API at api.libertai.io: text (chat completions), image, embeddings, audio and web search APIs over leading open models such as GLM-5.3, with no KYC, no prompt logging, API keys from the developer console or keyless pay-per-request x402 payments in USDC on Base, plus an agents framework.'
finops:
- has_sources: true
  method: derived
  name: Libertai Finops
  primary_unit: 1m input tokens
  service_category: ''
  slug: libertai-finops
  template: false
image: https://libertai.io/og.png
json_schemas:
- name: AlephCreditsRequest
  property_count: 2
  slug: libertai-aleph-credits-request
- name: ProxyRequest
  property_count: 1
  slug: libertai-proxy-request
jsonld:
- class_count: 4
  name: Libertai Context
  property_count: 7
  slug: libertai-context
layout: provider
modified: '2026-10-13'
name: LibertAI
nav: Providers
network: true
overview: 'LibertAI publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Aleph Credits API, Auth API, Health API, and 3 more. Tagged areas include Company, Artificial Intelligence, Inference, Model Routing, and OpenAI-Compatible.


  The LibertAI catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  LibertAI''s developer surface includes authentication, documentation, getting-started guide, engineering blog, pricing, support, and 21 more developer resources.'
plans:
- name: Libertai Plans Pricing
  plan_count: 9
  slug: libertai-plans-pricing
- name: Libertai Price Estimates
  plan_count: 0
  slug: libertai-price-estimates
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: LibertAI API Rules
  rule_count: 12
  severity_counts:
    error: 9
    hint: 0
    info: 2
    warn: 1
  slug: libertai-rules
score:
  band: developing
  composite: 45.8
  coverage:
    artifact_dirs: 21
    catalog_earned: 71.8
    catalog_earned_first_party: 12.0
    catalog_gap: 43.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 4.1
  facets:
    access_clarity: 63.2
    contract_governance: 22.0
    contract_quality: 46.5
    developer_ergonomics: 47.6
    discoverability: 66.1
    operational_transparency: 21.1
  previous_composite: 41.7
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
    score: 15.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Libertai Authentication
  slug: libertai-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Libertai Domain Security
  slug: libertai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: libertai
tags:
- Company
- Artificial Intelligence
- Inference
- Model Routing
- OpenAI-Compatible
- Decentralized
- Confidential Computing
- x402
website: https://libertai.io
---
