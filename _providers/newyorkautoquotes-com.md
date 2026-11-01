---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 27.3
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Indicative US personal auto insurance prices for AI agents acting on behalf of a consumer in New York.
  name: New York Insurance API
  slug: new-york-insurance-api
- baseURL: https://newyorkautoquotes.com
  baseurl_source: declared
  description: 'New York Insurance: Indicative US personal auto insurance prices for AI agents acting on behalf of a consumer in New York, and a consented path to licensed agents. Call /v1/eligibility first. Read /v1'
  name: New York Insurance Api API
  slug: new-york-insurance-api-api
artifact_total: 5
common:
- group: design
  href: https://artifacts.apis.io/newyorkautoquotes-com/rules/newyorkautoquotes-com-rules.yml
  title: ''
  type: Spectral
  url: rules/newyorkautoquotes-com-rules.yml
- group: design
  href: https://artifacts.apis.io/newyorkautoquotes-com/conformance/newyorkautoquotes-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/newyorkautoquotes-com-conformance.yml
- group: design
  href: https://artifacts.apis.io/newyorkautoquotes-com/errors/newyorkautoquotes-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/newyorkautoquotes-com-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/newyorkautoquotes-com/llms/newyorkautoquotes-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/newyorkautoquotes-com-llms.txt
- group: other
  href: https://artifacts.apis.io/newyorkautoquotes-com/a2a/newyorkautoquotes-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/newyorkautoquotes-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/newyorkautoquotes-com/mcp/newyorkautoquotes-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/newyorkautoquotes-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/newyorkautoquotes-com/well-known/newyorkautoquotes-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/newyorkautoquotes-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/newyorkautoquotes-com/hosts/newyorkautoquotes-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/newyorkautoquotes-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/newyorkautoquotes-com/vendors/newyorkautoquotes-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/newyorkautoquotes-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/newyorkautoquotes-com/security/newyorkautoquotes-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/newyorkautoquotes-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://newyorkautoquotes.com/
- group: docs
  title: ''
  type: APIReference
  url: https://newyorkautoquotes.com/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://newyorkautoquotes.com/?format=md
- group: operate
  title: ''
  type: Support
  url: https://newyorkautoquotes.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://newyorkautoquotes.com/rates
- group: start
  title: ''
  type: SignUp
  url: https://newyorkautoquotes.com/join
created: '2026-10-30'
description: New York Auto Quotes provides auto insurance quotes in New York from licensed agents without requiring a phone number. Users can obtain price estimates by entering vehicle and driver information, and the service connects them with up to four licensed agents who confirm the quotes. The platform emphasizes privacy, allowing users to withdraw requests and ensuring no personal data is sold without consent. It is operated by TheChattyAI under the CoverIntent brand.
layout: provider
mcp_servers:
- description: Remote MCP server at newyorkautoquotes.com.
  name: newyorkautoquotes-com MCP Server
  slug: newyorkautoquotes-com-mcp-yml
modified: '2026-10-30'
name: newyorkautoquotes-com
nav: Providers
network: true
overview: 'newyorkautoquotes-com publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including New York Insurance Api API, and 1 more. Tagged areas include Insurance, Quotes, NewYork, AI, and Platform.


  The newyorkautoquotes-com catalog on APIs.io includes 1 Spectral governance ruleset.


  newyorkautoquotes-com''s developer surface includes API reference, getting-started guide, support, pricing, signup flow, and 11 more developer resources.'
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: newyorkautoquotes-com API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: newyorkautoquotes-com-rules
score:
  band: thin
  composite: 26.4
  coverage:
    artifact_dirs: 13
    catalog_earned: 39.5
    catalog_earned_first_party: 0.0
    catalog_gap: 75.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 18.2
    contract_quality: 38.6
    developer_ergonomics: 23.8
    discoverability: 61.7
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 9.0
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Newyorkautoquotes Com Domain Security
  slug: newyorkautoquotes-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: newyorkautoquotes-com
tags:
- Insurance
- Quotes
- NewYork
- AI
- Platform
website: https://newyorkautoquotes.com/
---
