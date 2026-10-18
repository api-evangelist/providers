---
agent_readiness:
  band: agent-ready
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
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.3
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: 'Remote Model Context Protocol server exposing the Deeplead API as tools to Claude, ChatGPT, Cursor and other agents. Sign in with OAuth (dynamic client registration supported) or pass an API key as a '
  name: Deeplead MCP Server
  slug: deeplead-mcp-server
- baseURL: https://www.deeplead.io/api/v1
  baseurl_source: declared
  description: The Account API from Deeplead — 1 operation(s) for account.
  name: Deeplead Account API
  slug: deeplead-account-api
- baseURL: https://www.deeplead.io/api/v1
  baseurl_source: declared
  description: The Businesses API from Deeplead — 1 operation(s) for businesses.
  name: Deeplead Businesses API
  slug: deeplead-businesses-api
- baseURL: https://www.deeplead.io/api/v1
  baseurl_source: declared
  description: The Contacts API from Deeplead — 1 operation(s) for contacts.
  name: Deeplead Contacts API
  slug: deeplead-contacts-api
- baseURL: https://www.deeplead.io/api/v1
  baseurl_source: declared
  description: The Deliverability API from Deeplead — 2 operation(s) for deliverability.
  name: Deeplead Deliverability API
  slug: deeplead-deliverability-api
- baseURL: https://www.deeplead.io/api/v1
  baseurl_source: declared
  description: The Organizations API from Deeplead — 3 operation(s) for organizations.
  name: Deeplead Organizations API
  slug: deeplead-organizations-api
- baseURL: https://www.deeplead.io/api/v1
  baseurl_source: declared
  description: The Persons API from Deeplead — 5 operation(s) for persons.
  name: Deeplead Persons API
  slug: deeplead-persons-api
artifact_total: 10
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/deeplead/refs/heads/main/plans/deeplead-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/deeplead-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/deeplead/refs/heads/main/mcp/deeplead-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/deeplead-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/deeplead/refs/heads/main/well-known/deeplead-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/deeplead-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/deeplead/refs/heads/main/hosts/deeplead-hosts.yml
  title: ''
  type: Hosts
  url: hosts/deeplead-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/deeplead/refs/heads/main/vendors/deeplead-vendors.yml
  title: ''
  type: Vendors
  url: vendors/deeplead-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://www.deeplead.io/help
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/deeplead/refs/heads/main/security/deeplead-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/deeplead-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.deeplead.io/
- group: docs
  title: ''
  type: Documentation
  url: https://www.deeplead.io/developers
- group: docs
  title: ''
  type: APIReference
  url: https://www.deeplead.io/api/v1/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.deeplead.io/developers
- group: start
  title: ''
  type: SignUp
  url: https://www.deeplead.io/login
- group: other
  title: ''
  type: APICatalog
  url: https://www.deeplead.io/.well-known/api-catalog
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/deeplead/refs/heads/main/llms/deeplead-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/deeplead-llms.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: https://www.deeplead.io/.well-known/security.txt
- group: operate
  title: ''
  type: RateLimits
  url: https://www.deeplead.io/api/v1/docs
- group: company
  title: ''
  type: Blog
  url: https://www.deeplead.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.deeplead.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.deeplead.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.deeplead.io/privacy-policy
created: '2026-09-27'
description: Deeplead finds B2B customers and runs cold email outreach to them. It searches local businesses, companies and people, finds decision makers with verified work emails and phone numbers, and sends personalized campaigns from warmed-up inboxes with one inbox for every reply. The same data is available to developers and AI agents through a REST API with an OpenAPI 3.1 contract and a remote MCP server, both authenticated with an API key or OAuth.
image: https://deeplead.io/opengraph-image
layout: provider
mcp_servers:
- description: Remote MCP server at www.deeplead.io requiring OAuth.
  name: Deeplead MCP Server
  slug: deeplead-mcp-yml
modified: '2026-09-27'
name: Deeplead
nav: Providers
network: true
overview: 'Deeplead publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Businesses API, Contacts API, and 4 more. Tagged areas include Company, Lead Generation, Cold Email, Artificial Intelligence, and Sales Automation.


  Deeplead''s developer surface includes support, documentation, API reference, getting-started guide, signup flow, engineering blog, pricing, and 13 more developer resources.'
plans:
- name: Deeplead Plans Pricing
  plan_count: 1
  slug: deeplead-plans-pricing
random_paper: 6
score:
  band: developing
  composite: 40.5
  coverage:
    artifact_dirs: 12
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 16.4
  facets:
    access_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 47.8
    developer_ergonomics: 35.7
    discoverability: 85.0
    operational_transparency: 0.0
  previous_composite: 24.1
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/deeplead/refs/heads/main/screenshots/deeplead-2026-10-11T103638.png
security:
- kind: domain-security
  name: Deeplead Domain Security
  slug: deeplead-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: deeplead
tags:
- Company
- Lead Generation
- Cold Email
- Artificial Intelligence
- Sales Automation
website: https://www.deeplead.io/
---
