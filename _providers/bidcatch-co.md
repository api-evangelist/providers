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
  href: https://artifacts.apis.io/bidcatch-co/llms/bidcatch-co-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bidcatch-co-llms.txt
- group: agent
  href: https://artifacts.apis.io/bidcatch-co/mcp/bidcatch-co-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bidcatch-co-mcp.yml
- group: other
  href: https://artifacts.apis.io/bidcatch-co/hosts/bidcatch-co-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bidcatch-co-hosts.yml
- group: other
  href: https://artifacts.apis.io/bidcatch-co/vendors/bidcatch-co-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bidcatch-co-vendors.yml
- group: auth
  href: https://artifacts.apis.io/bidcatch-co/security/bidcatch-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bidcatch-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bidcatch.co/
- group: company
  title: ''
  type: Blog
  url: https://bidcatch.co/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://bidcatch.co/#pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bidcatch.co/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bidcatch.co/terms
coverage:
  checked: '2026-11-02'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found despite probing known hosts.
  evidence:
  - status: 200
    url: https://bidcatch.co/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: BidCatch provides a daily email digest of government bids, awards, and rebid intelligence. It aggregates public procurement data from SAM.gov, DLA DIBBS, and state portals, filters by user‑specified codes, and delivers clean morning emails. The service is independent, free to use without an account, and offers searchable archives of bids, awards, and protest decisions across federal, state, and local levels.
layout: provider
mcp_servers:
- description: Remote MCP server at bidcatch.co.
  name: BidCatch MCP Server
  slug: bidcatch-co-mcp-yml
modified: '2026-11-02'
name: BidCatch
nav: Providers
network: true
overview: 'BidCatch is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Government, Procurement, Bids, and EmailDigest.


  BidCatch''s developer surface includes engineering blog, pricing, and 8 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 6.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 36.7
    operational_transparency: 0.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bidcatch Co Domain Security
  slug: bidcatch-co-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bidcatch-co
tags:
- Government
- Procurement
- Bids
- EmailDigest
website: https://bidcatch.co/
---
