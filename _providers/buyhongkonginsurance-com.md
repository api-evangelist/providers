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
  band: human-only
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/buyhongkonginsurance-com/llms/buyhongkonginsurance-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/buyhongkonginsurance-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/buyhongkonginsurance-com/mcp/buyhongkonginsurance-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/buyhongkonginsurance-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/buyhongkonginsurance-com/hosts/buyhongkonginsurance-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/buyhongkonginsurance-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/buyhongkonginsurance-com/vendors/buyhongkonginsurance-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/buyhongkonginsurance-com-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://buyhongkonginsurance.com/trust/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://buyhongkonginsurance.com/privacy/
- group: docs
  title: ''
  type: Documentation
  url: https://buyhongkonginsurance.com/guides/
- group: auth
  href: https://artifacts.apis.io/buyhongkonginsurance-com/security/buyhongkonginsurance-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/buyhongkonginsurance-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://buyhongkonginsurance.com/
coverage:
  checked: '2026-11-03'
  detail: The website provides only consumer information and no developer documentation or API specifications.
  evidence:
  - status: 200
    url: https://buyhongkonginsurance.com
  reason: no-developer-program
  state: none
created: '2026-11-03'
description: Hong Kong Insurance Connect provides a comparative platform for Hong Kong insurance plans, covering savings, critical illness, VHIS, and fulfillment ratios. It aggregates public sources and offers information-only licensed broker referrals, enabling users to explore plan cover, exclusions, and insurer sources, and request broker introductions.
image: https://buyhongkonginsurance.com/icons/logo-en.png
layout: provider
mcp_servers:
- description: Remote MCP server at buyhongkonginsurance.com.
  name: Hong Kong Insurance Connect MCP Server
  slug: buyhongkonginsurance-com-mcp-yml
modified: '2026-11-03'
name: Hong Kong Insurance Connect
nav: Providers
network: true
overview: 'Hong Kong Insurance Connect is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Hong Kong, Comparison, Brokerage, and Finance.


  Hong Kong Insurance Connect''s developer surface includes documentation and 8 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 6.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 9.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 48.3
    operational_transparency: 0.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 9.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Buyhongkonginsurance Com Domain Security
  slug: buyhongkonginsurance-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: buyhongkonginsurance-com
tags:
- Insurance
- Hong Kong
- Comparison
- Brokerage
- Finance
website: https://buyhongkonginsurance.com/
---
