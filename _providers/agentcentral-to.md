---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
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
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.3
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: REST API for accessing Amazon Seller Central data via Agent Central. Documentation at https://agentcentral.to/docs/rest-api.
  name: Agent Central API
  slug: agent-central-api
- baseURL: https://mcp.agentcentral.to
  baseurl_source: declared
  description: 'Agent Central API as documented publicly: 22 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: Agent Central API
  slug: agentcentral-to-api
artifact_total: 15
common:
- group: agent
  href: https://artifacts.apis.io/agentcentral-to/mcp/agentcentral-to-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agentcentral-to-mcp.yml
- group: docs
  title: ''
  type: Documentation
  url: https://agentcentral.to/docs/quickstart/claude
- group: commercial
  href: https://artifacts.apis.io/agentcentral-to/plans/agentcentral-to-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agentcentral-to-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/agentcentral-to/rules/agentcentral-to-rules.yml
  title: ''
  type: Spectral
  url: rules/agentcentral-to-rules.yml
- group: design
  href: https://artifacts.apis.io/agentcentral-to/json-ld/agentcentral-to-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/agentcentral-to-context.jsonld
- group: design
  href: https://artifacts.apis.io/agentcentral-to/vocabulary/agentcentral-to-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agentcentral-to-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/agentcentral-to/data-model/agentcentral-to-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agentcentral-to-data-model.yml
- group: build
  href: https://artifacts.apis.io/agentcentral-to/cli/agentcentral-to-cli.yml
  title: ''
  type: CLI
  url: cli/agentcentral-to-cli.yml
- group: design
  href: https://artifacts.apis.io/agentcentral-to/conventions/agentcentral-to-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/agentcentral-to-conventions.yml
- group: design
  href: https://artifacts.apis.io/agentcentral-to/conventions/agentcentral-to-conventions.yml
  title: ''
  type: Conventions
  url: conventions/agentcentral-to-conventions.yml
- group: auth
  href: https://artifacts.apis.io/agentcentral-to/authentication/agentcentral-to-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agentcentral-to-authentication.yml
- group: design
  href: https://artifacts.apis.io/agentcentral-to/conformance/agentcentral-to-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentcentral-to-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agentcentral-to/llms/agentcentral-to-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentcentral-to-llms.txt
- group: auth
  href: https://artifacts.apis.io/agentcentral-to/well-known/agentcentral-to-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/agentcentral-to-security.txt
- group: agent
  href: https://artifacts.apis.io/agentcentral-to/well-known/agentcentral-to-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentcentral-to-well-known.yml
- group: other
  href: https://artifacts.apis.io/agentcentral-to/hosts/agentcentral-to-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentcentral-to-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentcentral-to/vendors/agentcentral-to-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentcentral-to-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agentcentral.to/terms
- group: start
  title: ''
  type: SignUp
  url: https://agentcentral.to/signup?tab=signin
- group: auth
  title: ''
  type: Security
  url: https://agentcentral.to/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agentcentral.to/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://agentcentral.to/docs/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://agentcentral.to/docs
- group: company
  title: ''
  type: Blog
  url: https://agentcentral.to/blog
- group: docs
  title: ''
  type: APIReference
  url: https://agentcentral.to/docs/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://agentcentral.to/docs/quickstart/claude
- group: auth
  href: https://artifacts.apis.io/agentcentral-to/security/agentcentral-to-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/agentcentral-to-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/agentcentral-to/security/agentcentral-to-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentcentral-to-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentcentral.to/
coverage:
  checked: '2026-11-01'
  detail: Documentation pages are JavaScript-rendered and no machine-readable spec was found.
  evidence:
  - status: 200
    url: https://agentcentral.to/docs/reference
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-31'
description: Agent Central provides AI agents access to Amazon Seller Central data via a REST API and CLI, enabling automated bid adjustments, inventory management, and financial insights. The platform offers read‑only and write‑enabled keys, integrates with Claude, ChatGPT, Muse, OpenClaw, Hermes, and Grok, and includes dashboards, custom tools, and daily reporting. It targets Amazon sellers seeking AI‑driven automation and analytics across multiple marketplaces.
image: https://agentcentral.to/og?title=Agent%20Central%20%7C%20Amazon%20seller%20data%20for%20AI%20agents
json_schemas:
- name: GetV1AccountResponse
  property_count: 15
  slug: agentcentral-to-get-v1-account-response
- name: PostSdCampaignsRequest
  property_count: 5
  slug: agentcentral-to-post-sd-campaigns-request
- name: PostSdNegativetargetsRequest
  property_count: 6
  slug: agentcentral-to-post-sd-negativetargets-request
- name: PostV1ResponsesRequest
  property_count: 3
  slug: agentcentral-to-post-v1-responses-request
- name: PutSdCampaignsRequest
  property_count: 5
  slug: agentcentral-to-put-sd-campaigns-request
- name: PutSdNegativetargetsRequest
  property_count: 6
  slug: agentcentral-to-put-sd-negativetargets-request
jsonld:
- class_count: 16
  name: Agentcentral To Context
  property_count: 31
  slug: agentcentral-to-context
layout: provider
mcp_servers:
- description: ''
  name: Agent Central MCP Server
  slug: agentcentral-to-mcp-yml
modified: '2026-10-31'
name: Agent Central
nav: Providers
network: true
overview: 'Agent Central is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include E-Commerce, Artificial Intelligence, Automation, Amazon, and Seller Central.


  The Agent Central catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Agent Central''s developer surface includes documentation, CLI, authentication, signup flow, pricing, engineering blog, API reference, and 22 more developer resources.'
plans:
- name: Agentcentral To Plans Pricing
  plan_count: 4
  slug: agentcentral-to-plans-pricing
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Agent Central API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: agentcentral-to-rules
score:
  band: thin
  composite: 34.6
  coverage:
    artifact_dirs: 18
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.9
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 26.1
    developer_ergonomics: 34.5
    discoverability: 56.7
    operational_transparency: 5.3
  previous_composite: 43.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agentcentral To Authentication
  slug: agentcentral-to-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Agentcentral To Domain Security
  slug: agentcentral-to-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Agentcentral To Vulnerability Disclosure
  slug: agentcentral-to-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: agentcentral-to
tags:
- E-Commerce
- Artificial Intelligence
- Automation
- Amazon
- Seller Central
website: https://agentcentral.to/
---
