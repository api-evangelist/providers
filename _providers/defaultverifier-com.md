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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
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
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Defaultverifier Com Agentic Access
  operation_count: 2
  slug: defaultverifier-com-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 1
apis:
- description: DefaultVerifier provides x402 settlement witness verification endpoints.
  name: DefaultVerifier API
  slug: defaultverifier-api
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/defaultverifier-com/agentic-access/defaultverifier-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/defaultverifier-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/defaultverifier-com/rules/defaultverifier-com-rules.yml
  title: ''
  type: Spectral
  url: rules/defaultverifier-com-rules.yml
- group: design
  href: https://artifacts.apis.io/defaultverifier-com/errors/defaultverifier-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/defaultverifier-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/defaultverifier-com/conformance/defaultverifier-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/defaultverifier-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/defaultverifier-com/mcp/defaultverifier-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/defaultverifier-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/defaultverifier-com/hosts/defaultverifier-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/defaultverifier-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/defaultverifier-com/vendors/defaultverifier-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/defaultverifier-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://defaultverifier.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://defaultverifier.com/privacy
- group: auth
  href: https://artifacts.apis.io/defaultverifier-com/security/defaultverifier-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/defaultverifier-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://defaultverifier.com/
created: '2026-11-05'
description: DefaultVerifier provides evidence rails for autonomous work, issuing signed receipts with proof seals that ensure integrity. The platform enables AI agents to verify any receipt and allows users to issue their own, supporting transparent and trustworthy automation workflows across services.
image: https://defaultverifier.com/badge/agent:morpheus.svg
layout: provider
mcp_servers:
- description: Remote MCP server at defaultverifier.com.
  name: DefaultVerifier MCP Server
  slug: defaultverifier-com-mcp-yml
modified: '2026-11-05'
name: DefaultVerifier
nav: Providers
network: true
overview: 'DefaultVerifier is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Automation, Verification, and Receipts.


  The DefaultVerifier catalog on APIs.io includes 1 Spectral governance ruleset.'
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 63
  extends:
  - spectral:oas
  name: DefaultVerifier API Rules
  rule_count: 22
  severity_counts:
    error: 20
    hint: 0
    info: 1
    warn: 1
  slug: defaultverifier-com-rules
score:
  band: emerging
  composite: 13.2
  coverage:
    artifact_dirs: 11
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 65.0
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Defaultverifier Com Domain Security
  slug: defaultverifier-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: defaultverifier-com
tags:
- Company
- Artificial Intelligence
- Automation
- Verification
- Receipts
website: https://defaultverifier.com/
---
