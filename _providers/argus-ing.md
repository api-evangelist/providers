---
access_model:
  confidence: low
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.2
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: auth
  href: https://artifacts.apis.io/argus-ing/authentication/argus-ing-authentication.yml
  title: ''
  type: Authentication
  url: authentication/argus-ing-authentication.yml
- group: agent
  href: https://artifacts.apis.io/argus-ing/mcp/argus-ing-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/argus-ing-mcp.yml
- group: agent
  href: https://artifacts.apis.io/argus-ing/well-known/argus-ing-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/argus-ing-well-known.yml
- group: other
  href: https://artifacts.apis.io/argus-ing/hosts/argus-ing-hosts.yml
  title: ''
  type: Hosts
  url: hosts/argus-ing-hosts.yml
- group: other
  href: https://artifacts.apis.io/argus-ing/vendors/argus-ing-vendors.yml
  title: ''
  type: Vendors
  url: vendors/argus-ing-vendors.yml
- group: auth
  href: https://artifacts.apis.io/argus-ing/security/argus-ing-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/argus-ing-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://argus.ing/
- group: company
  title: ''
  type: Blog
  url: https://argus.ing/blog
- group: docs
  title: ''
  type: Documentation
  url: https://argus.ing/llms.txt
- group: operate
  title: ''
  type: Support
  url: https://argus.ing/faq
- group: start
  title: ''
  type: SignUp
  url: https://argus.ing/auth/register
- group: start
  title: ''
  type: Login
  url: https://argus.ing/auth/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://argus.ing/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://argus.ing/privacy
coverage:
  checked: '2026-11-02'
  detail: Argus does not publish any developer program or API documentation, and no machine‑readable contract was found.
  evidence:
  - status: 200
    url: https://argus.ing/
  reason: no-developer-program
  state: none
created: '2026-11-01'
description: Argus provides AI‑enhanced analytics on Belgian public procurement tenders, delivering bid/no‑bid insights, winning price trends, and detailed award report analysis. By aggregating data from the Belgian Federal eProcurement platform, TED, and user‑uploaded award reports, Argus helps businesses understand market dynamics, identify competitors, and craft stronger proposals. The service is offered via a Model Context Protocol (MCP) endpoint for seamless integration with AI assistants like Claude and ChatGPT.
image: https://argus.ing/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at argus.ing.
  name: Argus MCP Server
  slug: argus-ing-mcp-yml
modified: '2026-11-01'
name: Argus
nav: Providers
network: true
overview: 'Argus is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Tender, Procurement, Analytics, Artificial Intelligence, and Belgium.


  Argus'' developer surface includes authentication, engineering blog, documentation, support, signup flow, and 9 more developer resources.'
random_paper: 21
score:
  band: emerging
  composite: 12.2
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.7
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 20.2
    discoverability: 48.3
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - belgium
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - benelux
    - europe
  previous_composite: 17.9
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Argus Ing Authentication
  slug: argus-ing-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Argus Ing Domain Security
  slug: argus-ing-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: argus-ing
tags:
- Tender
- Procurement
- Analytics
- Artificial Intelligence
- Belgium
website: https://argus.ing/
---
