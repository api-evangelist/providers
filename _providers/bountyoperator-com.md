---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Bounty Operator API as documented publicly: 8 operations. Contract generated from the documentation by API Evangelist (2026-11-03); not the provider''s own document.'
  name: Bounty Operator API
  slug: bountyoperator-com-api
artifact_total: 10
common:
- group: commercial
  href: https://artifacts.apis.io/bountyoperator-com/plans/bountyoperator-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bountyoperator-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/bountyoperator-com/rules/bountyoperator-com-rules.yml
  title: ''
  type: Spectral
  url: rules/bountyoperator-com-rules.yml
- group: design
  href: https://artifacts.apis.io/bountyoperator-com/json-ld/bountyoperator-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bountyoperator-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/bountyoperator-com/vocabulary/bountyoperator-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bountyoperator-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/bountyoperator-com/data-model/bountyoperator-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bountyoperator-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/bountyoperator-com/changelog/bountyoperator-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/bountyoperator-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/bountyoperator-com/conventions/bountyoperator-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/bountyoperator-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/bountyoperator-com/conventions/bountyoperator-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/bountyoperator-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/bountyoperator-com/authentication/bountyoperator-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bountyoperator-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/bountyoperator-com/conformance/bountyoperator-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bountyoperator-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bountyoperator-com/llms/bountyoperator-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bountyoperator-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/bountyoperator-com/mcp/bountyoperator-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bountyoperator-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/bountyoperator-com/well-known/bountyoperator-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bountyoperator-com-security.txt
- group: agent
  href: https://artifacts.apis.io/bountyoperator-com/well-known/bountyoperator-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bountyoperator-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/bountyoperator-com/hosts/bountyoperator-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bountyoperator-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/bountyoperator-com/vendors/bountyoperator-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bountyoperator-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bountyoperator.com/terms
- group: operate
  title: ''
  type: Support
  url: https://bountyoperator.com/support
- group: auth
  title: ''
  type: Security
  url: https://bountyoperator.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bountyoperator.com/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://bountyoperator.com/changelog
- group: auth
  href: https://artifacts.apis.io/bountyoperator-com/security/bountyoperator-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bountyoperator-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/bountyoperator-com/security/bountyoperator-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bountyoperator-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bountyoperator.com/
- group: docs
  title: ''
  type: Documentation
  url: https://bountyoperator.com/docs/model-api
- group: commercial
  title: ''
  type: Pricing
  url: https://bountyoperator.com/pricing
coverage:
  checked: '2026-11-03'
  detail: The provider's documentation pages are HTML without any published OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://bountyoperator.com/docs/model-api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Bounty Operator provides a pre‑submission review platform for bug bounty reports, helping researchers ensure their evidence is complete and impactful before sending to program triagers. The service offers free daily reviews, multiple review types, and paid plans for unlimited usage, integrating with popular AI tools for code and report drafting. It aims to streamline the bounty submission process and improve success rates for security researchers.
image: https://bountyoperator.com/social-spec-v3.png
json_schemas:
- name: GetInvoicesIdResponse
  property_count: 2
  slug: bountyoperator-com-get-invoices-id-response
- name: PostV1ChatCompletionsRequest
  property_count: 18
  slug: bountyoperator-com-post-v1-chat-completions-request
jsonld:
- class_count: 2
  name: Bountyoperator Com Context
  property_count: 20
  slug: bountyoperator-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at bountyoperator.com.
  name: Bounty Operator MCP Server
  slug: bountyoperator-com-mcp-yml
modified: '2026-11-02'
name: Bounty Operator
nav: Providers
network: true
overview: 'Bounty Operator is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Bug Bounty, Review, and Artificial Intelligence.


  The Bounty Operator catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Bounty Operator''s developer surface includes changelog, authentication, support, documentation, pricing, and 21 more developer resources.'
plans:
- name: Bountyoperator Com Plans Pricing
  plan_count: 2
  slug: bountyoperator-com-plans-pricing
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 82
  extends:
  - spectral:oas
  name: Bounty Operator API Rules
  rule_count: 41
  severity_counts:
    error: 38
    hint: 0
    info: 2
    warn: 1
  slug: bountyoperator-com-rules
score:
  band: thin
  composite: 28.1
  coverage:
    artifact_dirs: 21
    catalog_earned: 62.8
    catalog_earned_first_party: 8.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 22.0
    contract_quality: 22.1
    developer_ergonomics: 19.0
    discoverability: 56.7
    operational_transparency: 13.2
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
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
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Bountyoperator Com Authentication
  slug: bountyoperator-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Bountyoperator Com Domain Security
  slug: bountyoperator-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Bountyoperator Com Vulnerability Disclosure
  slug: bountyoperator-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bountyoperator-com
tags:
- Company
- Security
- Bug Bounty
- Review
- Artificial Intelligence
website: https://bountyoperator.com/
---
