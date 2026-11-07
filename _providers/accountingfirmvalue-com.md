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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.3
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: Security
  url: https://accountingfirmvalue.com/terms
- group: agent
  href: https://artifacts.apis.io/accountingfirmvalue-com/llms/accountingfirmvalue-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/accountingfirmvalue-com-llms.txt
- group: build
  href: https://artifacts.apis.io/accountingfirmvalue-com/mcp/accountingfirmvalue-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/accountingfirmvalue-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/accountingfirmvalue-com/mcp/accountingfirmvalue-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/accountingfirmvalue-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/accountingfirmvalue-com/well-known/accountingfirmvalue-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/accountingfirmvalue-com-security.txt
- group: agent
  href: https://artifacts.apis.io/accountingfirmvalue-com/well-known/accountingfirmvalue-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/accountingfirmvalue-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/accountingfirmvalue-com/hosts/accountingfirmvalue-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/accountingfirmvalue-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/accountingfirmvalue-com/vendors/accountingfirmvalue-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/accountingfirmvalue-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://accountingfirmvalue.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://accountingfirmvalue.com/privacy/
- group: auth
  href: https://artifacts.apis.io/accountingfirmvalue-com/security/accountingfirmvalue-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/accountingfirmvalue-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/accountingfirmvalue-com/security/accountingfirmvalue-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/accountingfirmvalue-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://accountingfirmvalue.com/
coverage:
  checked: '2026-10-31'
  detail: The provider's site returns an OpenAPI JSON that describes a different service, so no valid contract for Accounting Firm Value was found.
  evidence:
  - status: 200
    url: https://accountingfirmvalue.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: Accounting Firm Value provides comprehensive business valuation reports, comparing report types, accepted purposes, required signatories, and detailed content guidelines. The site offers insights into valuation methods, regulatory requirements, and practical guidance for both commercial and charitable contexts, helping users understand which report best fits their needs.
image: https://accountingfirmvalue.com/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at accountingfirmvalue.com.
  name: Accounting Firm Value MCP Server
  slug: accountingfirmvalue-com-mcp-yml
modified: '2026-10-31'
name: Accounting Firm Value
nav: Providers
network: true
overview: Accounting Firm Value is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Valuation, Business, Accounting, Finance, and Reports.
random_paper: 2
score:
  band: minimal
  composite: 7.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.4
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.3
    operational_transparency: 5.3
  previous_composite: 11.1
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Accountingfirmvalue Com Domain Security
  slug: accountingfirmvalue-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Accountingfirmvalue Com Vulnerability Disclosure
  slug: accountingfirmvalue-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: accountingfirmvalue-com
tags:
- Valuation
- Business
- Accounting
- Finance
- Reports
website: https://accountingfirmvalue.com/
---
