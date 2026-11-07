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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.1
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API for FluxA wallet operations, as documented in the HTTP API guide.
  name: FluxA Wallet API
  slug: fluxa-wallet-api
- baseURL: https://walletapi.fluxapay.xyz
  baseurl_source: declared
  description: 'FluxA API as documented publicly: 16 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: FluxA API
  slug: fluxapay-xyz-api
artifact_total: 11
common:
- group: design
  href: https://artifacts.apis.io/fluxapay-xyz/rules/fluxapay-xyz-rules.yml
  title: ''
  type: Spectral
  url: rules/fluxapay-xyz-rules.yml
- group: design
  href: https://artifacts.apis.io/fluxapay-xyz/json-ld/fluxapay-xyz-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/fluxapay-xyz-context.jsonld
- group: design
  href: https://artifacts.apis.io/fluxapay-xyz/vocabulary/fluxapay-xyz-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/fluxapay-xyz-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/fluxapay-xyz/data-model/fluxapay-xyz-data-model.yml
  title: ''
  type: DataModel
  url: data-model/fluxapay-xyz-data-model.yml
- group: build
  href: https://artifacts.apis.io/fluxapay-xyz/cli/fluxapay-xyz-cli.yml
  title: ''
  type: CLI
  url: cli/fluxapay-xyz-cli.yml
- group: design
  href: https://artifacts.apis.io/fluxapay-xyz/conformance/fluxapay-xyz-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fluxapay-xyz-conformance.yml
- group: agent
  href: https://artifacts.apis.io/fluxapay-xyz/llms/fluxapay-xyz-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fluxapay-xyz-llms.txt
- group: agent
  href: https://artifacts.apis.io/fluxapay-xyz/well-known/fluxapay-xyz-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/fluxapay-xyz-well-known.yml
- group: other
  href: https://artifacts.apis.io/fluxapay-xyz/hosts/fluxapay-xyz-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fluxapay-xyz-hosts.yml
- group: other
  href: https://artifacts.apis.io/fluxapay-xyz/vendors/fluxapay-xyz-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fluxapay-xyz-vendors.yml
- group: start
  title: ''
  type: Sandbox
  url: https://fluxapay.xyz/playground
- group: auth
  href: https://artifacts.apis.io/fluxapay-xyz/security/fluxapay-xyz-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fluxapay-xyz-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fluxapay.xyz/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.fluxapay.xyz/wallet/http-api.html
- group: company
  title: ''
  type: Blog
  url: https://fluxapay.xyz/blog
- group: operate
  title: ''
  type: Support
  url: https://fluxapay.xyz/security
- group: start
  title: ''
  type: GettingStarted
  url: https://fluxapay.xyz/learning
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.fluxapay.xyz
- group: docs
  title: ''
  type: APIReference
  url: https://docs.fluxapay.xyz/wallet/http-api.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FluxA-Agent-Payment
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://fluxapay.xyz/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: FluxA provides payment infrastructure for AI agents, offering a co‑wallet, virtual AgentCards, the AEP2 embedded payment protocol, and tools to monetize MCP servers and APIs. Their platform enables autonomous agents to pay, earn, and transact with built‑in risk controls, spend limits, and approval workflows, supporting AI‑driven commerce across services.
json_schemas:
- name: GetApiMandatesAgentMandateidResponse
  property_count: 17
  slug: fluxapay-xyz-get-api-mandates-agent-mandateid-response
- name: GetApiPaymentLinksRefundsRefundidResponse
  property_count: 19
  slug: fluxapay-xyz-get-api-payment-links-refunds-refundid-response
- name: GetApiPaymentLinksRefundsResponse
  property_count: 20
  slug: fluxapay-xyz-get-api-payment-links-refunds-response
- name: PostApiPaymentLinksRefundsInitiateResponse
  property_count: 13
  slug: fluxapay-xyz-post-api-payment-links-refunds-initiate-response
- name: PostApiPaymentPaymentidRequest
  property_count: 18
  slug: fluxapay-xyz-post-api-payment-paymentid-request
- name: PostApiPayoutsRequest
  property_count: 11
  slug: fluxapay-xyz-post-api-payouts-request
jsonld:
- class_count: 26
  name: Fluxapay Xyz Context
  property_count: 100
  slug: fluxapay-xyz-context
layout: provider
modified: '2026-11-04'
name: FluxA
nav: Providers
network: true
overview: 'FluxA is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Artificial Intelligence, Agents, and Infrastructure.


  The FluxA catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  FluxA''s developer surface includes CLI, sandbox, documentation, engineering blog, support, getting-started guide, API reference, and 13 more developer resources.'
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 81
  extends:
  - spectral:oas
  name: FluxA API Rules
  rule_count: 40
  severity_counts:
    error: 38
    hint: 0
    info: 1
    warn: 1
  slug: fluxapay-xyz-rules
score:
  band: emerging
  composite: 26.0
  coverage:
    artifact_dirs: 16
    catalog_earned: 55.8
    catalog_earned_first_party: 0.0
    catalog_gap: 59.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 24.8
    developer_ergonomics: 59.5
    discoverability: 53.6
    operational_transparency: 5.3
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
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 14.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Fluxapay Xyz Domain Security
  slug: fluxapay-xyz-domain-security
  summary_line: TLSv1.3 · HSTS
slug: fluxapay-xyz
tags:
- Company
- Payments
- Artificial Intelligence
- Agents
- Infrastructure
website: https://fluxapay.xyz/
---
