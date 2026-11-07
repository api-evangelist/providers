---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
api_count: 1
apis:
- description: API documentation for Chain of Title services.
  name: Chain of Title API
  slug: chain-of-title-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/chainoftitle-org/plans/chainoftitle-org-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/chainoftitle-org-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/chainoftitle-org/llms/chainoftitle-org-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/chainoftitle-org-llms.txt
- group: agent
  href: https://artifacts.apis.io/chainoftitle-org/mcp/chainoftitle-org-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/chainoftitle-org-mcp.yml
- group: other
  href: https://artifacts.apis.io/chainoftitle-org/hosts/chainoftitle-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chainoftitle-org-hosts.yml
- group: other
  href: https://artifacts.apis.io/chainoftitle-org/vendors/chainoftitle-org-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chainoftitle-org-vendors.yml
- group: auth
  href: https://artifacts.apis.io/chainoftitle-org/security/chainoftitle-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chainoftitle-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://chainoftitle.org/
- group: commercial
  title: ''
  type: Pricing
  url: https://chainoftitle.org/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://chainoftitle.org/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://chainoftitle.org/privacy
coverage:
  checked: '2026-11-03'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable spec found despite accessible API documentation page.
  evidence:
  - status: 200
    url: https://chainoftitle.org/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: Chain of Title provides launch-time provenance for Solana tokens, recording over three million token launches from creation transactions. It offers an API to retrieve detailed launch records, including claimed metadata, transaction data, and on-chain documents. The service also includes brand protection alerts and detailed provenance reports for token launches, supporting developers and brands in blockchain forensics and token verification.
image: https://chainoftitle.org/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at chainoftitle.org.
  name: Chain of Title MCP Server
  slug: chainoftitle-org-mcp-yml
modified: '2026-11-03'
name: Chain of Title
nav: Providers
network: true
overview: 'Chain of Title is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Blockchain, Solana, Tokens, Provenance, and Company.


  Chain of Title''s developer surface includes pricing and 9 more developer resources.'
plans:
- name: Chainoftitle Org Plans Pricing
  plan_count: 5
  slug: chainoftitle-org-plans-pricing
random_paper: 15
score:
  band: emerging
  composite: 14.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 56.7
    operational_transparency: 0.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Chainoftitle Org Domain Security
  slug: chainoftitle-org-domain-security
  summary_line: TLSv1.3 · DMARC
slug: chainoftitle-org
tags:
- Blockchain
- Solana
- Tokens
- Provenance
- Company
website: https://chainoftitle.org/
---
