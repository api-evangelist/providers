---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
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
api_count: 3
apis:
- description: Book It lets people find local home-service and trade businesses inside Claude and ChatGPT, see the services and price ranges those businesses set themselves, check the windows they take work, and sen
  name: Book It
  slug: book-it
- description: Owner's Desk is a remote MCP server over Streamable HTTP with its own OAuth 2.1 authorization server.
  name: Owner's Desk
  slug: owner-s-desk
- description: AI Front Door provides each business a connector inside Claude and ChatGPT, offering tools to query services, availability, and request bookings.
  name: AI Front Door
  slug: ai-front-door
artifact_total: 6
common:
- group: auth
  href: https://artifacts.apis.io/modernmustardseed-com/authentication/modernmustardseed-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/modernmustardseed-com-authentication.yml
- group: agent
  href: https://artifacts.apis.io/modernmustardseed-com/llms/modernmustardseed-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/modernmustardseed-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/modernmustardseed-com/mcp/modernmustardseed-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/modernmustardseed-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/modernmustardseed-com/well-known/modernmustardseed-com-frontdoor-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/modernmustardseed-com-frontdoor-security.txt
- group: auth
  href: https://artifacts.apis.io/modernmustardseed-com/well-known/modernmustardseed-com-desk-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/modernmustardseed-com-desk-security.txt
- group: auth
  href: https://artifacts.apis.io/modernmustardseed-com/well-known/modernmustardseed-com-book-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/modernmustardseed-com-book-security.txt
- group: agent
  href: https://artifacts.apis.io/modernmustardseed-com/well-known/modernmustardseed-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/modernmustardseed-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/modernmustardseed-com/hosts/modernmustardseed-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/modernmustardseed-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/modernmustardseed-com/vendors/modernmustardseed-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/modernmustardseed-com-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ModernMustardSeed
- group: auth
  href: https://artifacts.apis.io/modernmustardseed-com/security/modernmustardseed-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/modernmustardseed-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://modernmustardseed.com/
- group: company
  title: ''
  type: Blog
  url: https://modernmustardseed.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://modernmustardseed.com/about
- group: operate
  title: ''
  type: Support
  url: https://modernmustardseed.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://modernmustardseed.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://modernmustardseed.com/privacy
coverage:
  checked: '2026-10-29'
  detail: No OpenAPI, GraphQL, AsyncAPI, gRPC, or WSDL contract found; only human‑readable documentation pages.
  evidence:
  - status: 200
    url: https://book.modernmustardseed.com/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Modern Mustard Seed is an AI product studio in Kalispell, Montana that designs and builds websites, AI voice agents, AI agents, custom software and Claude connectors for businesses across the United States, and manages them end‑to‑end. It offers AI‑driven web experiences, voice receptionists, and software solutions for enterprises, emphasizing integration with large language models and marketing automation.
image: https://modernmustardseed.com/brand/mms-share-flathead-20261025.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at book.modernmustardseed.com.
  name: modernmustardseed-com MCP Server
  slug: modernmustardseed-com-mcp-yml
modified: '2026-10-29'
name: modernmustardseed-com
nav: Providers
network: true
overview: 'modernmustardseed-com is listed with 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Studio, Web Development, Voice Agents, and Software.


  modernmustardseed-com''s developer surface includes authentication, engineering blog, documentation, support, and 13 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 15.3
  coverage:
    artifact_dirs: 13
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.7
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 20.2
    discoverability: 80.0
    operational_transparency: 13.2
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 20.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/modernmustardseed-com/modernmustardseed-com-2026-11-03T135749.png
security:
- kind: authentication
  name: Modernmustardseed Com Authentication
  slug: modernmustardseed-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Modernmustardseed Com Domain Security
  slug: modernmustardseed-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: modernmustardseed-com
tags:
- Artificial Intelligence
- Studio
- Web Development
- Voice Agents
- Software
website: https://modernmustardseed.com/
---
