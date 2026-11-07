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
  href: https://artifacts.apis.io/ooma/llms/ooma-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ooma-llms.txt
- group: agent
  href: https://artifacts.apis.io/ooma/mcp/ooma-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/ooma-mcp.yml
- group: other
  href: https://artifacts.apis.io/ooma/hosts/ooma-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ooma-hosts.yml
- group: other
  href: https://artifacts.apis.io/ooma/vendors/ooma-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ooma-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://help.ooma.com/en/
- group: start
  title: ''
  type: SignUp
  url: https://www.ooma.com/office-phones/sign-up-for-early-access-form/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ooma.com/office-modules/plans-page-activate-saving-lead-form/
- group: company
  title: ''
  type: Blog
  url: https://www.ooma.com/blog/voip-callers/
- group: docs
  title: ''
  type: Documentation
  url: https://help.ooma.com/
- group: auth
  href: https://artifacts.apis.io/ooma/security/ooma-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ooma-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ooma.com/
coverage:
  checked: '2026-10-28'
  detail: The main site https://ooma.com returns a JavaScript shell with no machine‑readable API documentation.
  evidence:
  - status: 200
    url: https://ooma.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: Ooma provides cloud‑based voice over IP (VoIP) telephone services for residential and business customers, offering hardware devices, mobile apps, and a suite of communication features such as call forwarding, voicemail, and virtual receptionists. The company’s platform integrates with business tools and supports international calling, aiming to replace traditional landlines with affordable internet‑based phone solutions.
layout: provider
mcp_servers:
- description: Remote MCP server at help.ooma.com.
  name: Ooma MCP Server
  slug: ooma-mcp-yml
modified: '2026-10-28'
name: Ooma
nav: Providers
network: true
overview: 'Ooma is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include VoIP, Telecommunications, Cloud Services, Business Communications, and Residential.


  Ooma''s developer surface includes support, signup flow, pricing, engineering blog, documentation, and 6 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 7.2
  coverage:
    artifact_dirs: 9
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.1
  facets:
    access_clarity: 11.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 55.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 11.3
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 5.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/ooma/ooma-2026-11-03T140625.png
security:
- kind: domain-security
  name: Ooma Domain Security
  slug: ooma-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ooma
tags:
- VoIP
- Telecommunications
- Cloud Services
- Business Communications
- Residential
website: https://ooma.com/
---
