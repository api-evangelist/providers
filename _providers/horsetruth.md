---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
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
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 25.3
  scored_at: '2026-10-17'
api_count: 6
apis:
- baseURL: https://horsestruth.com.au
  baseurl_source: declared
  description: The Horses API from Horse Truth — 1 operation(s) for horses.
  name: Horse Truth Horses API
  slug: horsetruth-horses-api
- baseURL: https://horsestruth.com.au
  baseurl_source: declared
  description: The Identity API from Horse Truth — 1 operation(s) for identity.
  name: Horse Truth Identity API
  slug: horsetruth-identity-api
- baseURL: https://horsestruth.com.au
  baseurl_source: declared
  description: The Machine API from Horse Truth — 1 operation(s) for machine.
  name: Horse Truth Machine API
  slug: horsetruth-machine-api
- baseURL: https://horsestruth.com.au
  baseurl_source: declared
  description: The Mcp API from Horse Truth — 1 operation(s) for mcp.
  name: Horse Truth MCP API
  slug: horsetruth-mcp-api
- baseURL: https://horsestruth.com.au
  baseurl_source: declared
  description: The Sandbox API from Horse Truth — 1 operation(s) for sandbox.
  name: Horse Truth Sandbox API
  slug: horsetruth-sandbox-api
- baseURL: https://horsestruth.com.au
  baseurl_source: declared
  description: The X402 API from Horse Truth — 1 operation(s) for x402.
  name: Horse Truth X402 API
  slug: horsetruth-x402-api
artifact_total: 13
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/horsetruth/refs/heads/main/plans/horsetruth-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/horsetruth-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/horsetruth/refs/heads/main/rules/horsetruth-rules.yml
  title: ''
  type: Spectral
  url: rules/horsetruth-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/horsetruth/refs/heads/main/json-ld/horsetruth-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/horsetruth-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/horsetruth/refs/heads/main/vocabulary/horsetruth-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/horsetruth-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/horsetruth/refs/heads/main/data-model/horsetruth-data-model.yml
  title: ''
  type: DataModel
  url: data-model/horsetruth-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/horsetruth/refs/heads/main/authentication/horsetruth-authentication.yml
  title: ''
  type: Authentication
  url: authentication/horsetruth-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/horsetruth/refs/heads/main/conformance/horsetruth-conformance.yml
  title: ''
  type: Conformance
  url: conformance/horsetruth-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/horsetruth/refs/heads/main/llms/horsetruth-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/horsetruth-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/horsetruth/refs/heads/main/a2a/horsetruth-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/horsetruth-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/horsetruth/refs/heads/main/mcp/horsetruth-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/horsetruth-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/horsetruth/refs/heads/main/well-known/horsetruth-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/horsetruth-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/horsetruth/refs/heads/main/hosts/horsetruth-hosts.yml
  title: ''
  type: Hosts
  url: hosts/horsetruth-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://horsetruth.com.au/terms
- group: start
  title: ''
  type: Sandbox
  url: https://horsetruth.com.au/api/v1/sandbox/chance-with-wolves
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://horsetruth.com.au/privacy
- group: start
  title: ''
  type: GettingStarted
  url: https://horsetruth.com.au/developers/machine
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/horsetruth/refs/heads/main/security/horsetruth-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/horsetruth-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://horsetruth.com.au
- group: docs
  title: ''
  type: Documentation
  url: https://horsetruth.com.au/developers
coverage:
  checked: '2026-10-14'
  detail: Developers page returns a JavaScript redirect shell with no readable content.
  evidence:
  - status: 200
    url: https://horsetruth.com/developers
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-14'
description: Horse Truth provides plain-English intelligence on Australian thoroughbred racehorses, offering a public sealed record and machine-readable data. Users can access horse performance, evidence of form, and receive daily feeds or full access plans. The service includes x402 micro-payments for machine access and A$19 monthly subscriptions for people, with detailed reports available for purchase.
json_schemas:
- name: PostApiV1MachineMachineidRequest
  property_count: 1
  slug: horsetruth-post-api-v1-machine-machineid-request
jsonld:
- class_count: 1
  name: Horsetruth Context
  property_count: 1
  slug: horsetruth-context
layout: provider
mcp_servers:
- description: Remote MCP server at horse-truth-edge-production.up.railway.app.
  name: Horse Truth MCP Server
  slug: horsetruth-mcp-yml
modified: '2026-10-14'
name: Horse Truth
nav: Providers
network: true
overview: 'Horse Truth is listed with 6 APIs on the [APIs.io](https://apis.io/) network, including Horses API, Identity API, Machine API, and 3 more. Tagged areas include Racehorse Intelligence, Horse Reports, Developers, and Trainers.


  The Horse Truth catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Horse Truth''s developer surface includes authentication, sandbox, getting-started guide, documentation, and 15 more developer resources.'
plans:
- name: Horsetruth Plans Pricing
  plan_count: 1
  slug: horsetruth-plans-pricing
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Horse Truth API Rules
  rule_count: 12
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 0
  slug: horsetruth-rules
score:
  band: thin
  composite: 31.2
  coverage:
    artifact_dirs: 18
    catalog_earned: 56.4
    catalog_earned_first_party: 8.0
    catalog_gap: 58.6
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 19.7
    contract_quality: 19.0
    developer_ergonomics: 40.5
    discoverability: 68.3
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 7
      marker_coverage: 100.0
      total: 7
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Horsetruth Authentication
  slug: horsetruth-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Horsetruth Domain Security
  slug: horsetruth-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: horsetruth
tags:
- Racehorse Intelligence
- Horse Reports
- Developers
- Trainers
website: https://horsetruth.com.au
---
