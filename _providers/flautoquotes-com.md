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
    agent_card: conformant
    agent_skills: unknown
    agentic_access: derived
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 30.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Flautoquotes Com Agentic Access
  operation_count: 2
  slug: flautoquotes-com-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 1
apis:
- baseURL: https://flautoquotes.com
  baseurl_source: declared
  description: The Eligibility API from flautoquotes-com — 1 operation(s) for eligibility.
  name: flautoquotes-com Eligibility API
  slug: flautoquotes-com-eligibility-api
- baseURL: https://flautoquotes.com
  baseurl_source: declared
  description: The Quotes API from flautoquotes-com — 1 operation(s) for quotes.
  name: flautoquotes-com Quotes API
  slug: flautoquotes-com-quotes-api
artifact_total: 8
common:
- group: agent
  href: https://artifacts.apis.io/flautoquotes-com/agentic-access/flautoquotes-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/flautoquotes-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/flautoquotes-com/rules/flautoquotes-com-rules.yml
  title: ''
  type: Spectral
  url: rules/flautoquotes-com-rules.yml
- group: design
  href: https://artifacts.apis.io/flautoquotes-com/errors/flautoquotes-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/flautoquotes-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/flautoquotes-com/conformance/flautoquotes-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/flautoquotes-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/flautoquotes-com/llms/flautoquotes-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/flautoquotes-com-llms.txt
- group: other
  href: https://artifacts.apis.io/flautoquotes-com/a2a/flautoquotes-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/flautoquotes-com-a2a.yml
- group: build
  href: https://artifacts.apis.io/flautoquotes-com/mcp/flautoquotes-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/flautoquotes-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/flautoquotes-com/mcp/flautoquotes-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/flautoquotes-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/flautoquotes-com/well-known/flautoquotes-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/flautoquotes-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/flautoquotes-com/hosts/flautoquotes-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/flautoquotes-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/flautoquotes-com/vendors/flautoquotes-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/flautoquotes-com-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://flautoquotes.com/privacy
- group: auth
  href: https://artifacts.apis.io/flautoquotes-com/security/flautoquotes-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/flautoquotes-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://flautoquotes.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://flautoquotes.com/v1/terms
- group: docs
  title: ''
  type: APIReference
  url: https://flautoquotes.com/openapi.json
created: '2026-10-30'
description: Florida Insurance provides auto insurance quotes in Florida by connecting users with licensed agents. The platform gathers vehicle and driver information, then presents multiple competing quotes, allowing users to compare coverage options and prices. It emphasizes privacy, does not sell data without consent, and offers a straightforward quoting process via phone or text.
layout: provider
mcp_servers:
- description: Remote MCP server at flautoquotes.com.
  name: flautoquotes-com MCP Server
  slug: flautoquotes-com-mcp-yml
modified: '2026-10-30'
name: flautoquotes-com
nav: Providers
network: true
overview: 'flautoquotes-com publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Eligibility API and Quotes API. Tagged areas include Insurance, Auto, Quotes, Florida, and Marketplace.


  The flautoquotes-com catalog on APIs.io includes 1 Spectral governance ruleset.


  flautoquotes-com''s developer surface includes API reference and 15 more developer resources.'
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: flautoquotes-com API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: flautoquotes-com-rules
score:
  band: emerging
  composite: 20.9
  coverage:
    artifact_dirs: 16
    catalog_earned: 39.5
    catalog_earned_first_party: 0.0
    catalog_gap: 75.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.4
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 41.0
    developer_ergonomics: 3.6
    discoverability: 61.7
    operational_transparency: 0.0
  previous_composite: 24.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 13.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/flautoquotes-com/flautoquotes-com-2026-11-03T132125.png
security:
- kind: domain-security
  name: Flautoquotes Com Domain Security
  slug: flautoquotes-com-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 2
skills:
- name: auto-insurance-leads-fl
  slug: flautoquotes-com-auto-insurance-leads-fl
- name: auto-insurance-quote-fl
  slug: flautoquotes-com-auto-insurance-quote-fl
slug: flautoquotes-com
tags:
- Insurance
- Auto
- Quotes
- Florida
- Marketplace
website: https://flautoquotes.com/
---
