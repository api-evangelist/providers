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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/rheaply/llms/rheaply-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/rheaply-llms.txt
- group: auth
  href: https://artifacts.apis.io/rheaply/well-known/rheaply-support-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/rheaply-support-security.txt
- group: auth
  href: https://artifacts.apis.io/rheaply/well-known/rheaply-issuu-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/rheaply-issuu-security.txt
- group: agent
  href: https://artifacts.apis.io/rheaply/well-known/rheaply-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/rheaply-well-known.yml
- group: other
  href: https://artifacts.apis.io/rheaply/hosts/rheaply-hosts.yml
  title: ''
  type: Hosts
  url: hosts/rheaply-hosts.yml
- group: other
  href: https://artifacts.apis.io/rheaply/vendors/rheaply-vendors.yml
  title: ''
  type: Vendors
  url: vendors/rheaply-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://rheaply.com/about-us/leadership/
- group: docs
  title: ''
  type: Documentation
  url: https://rheaply.com/resources/guides/adaptive-reuse/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Rheaply
- group: company
  title: ''
  type: Website
  url: https://rheaply.com/
- group: start
  title: ''
  type: SignUp
  url: https://rheaply.com/register/
- group: start
  title: ''
  type: Login
  url: https://app.rheaply.com/
- group: operate
  title: ''
  type: Support
  url: https://support.rheaply.com/en/
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.rheaply.com/en/
- group: company
  title: ''
  type: Blog
  url: https://rheaply.com/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://rheaply.com/terms/privacy-statement/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://rheaply.com/terms/
- group: operate
  title: ''
  type: ChangeLog
  url: https://rheaply.com/release-notes/
- group: company
  title: ''
  type: Newsroom
  url: https://rheaply.com/press/
- group: auth
  href: https://artifacts.apis.io/rheaply/security/rheaply-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rheaply-domain-security.yml
coverage:
  checked: '2026-10-20'
  detail: api.rheaply.com only 302-redirects every path (including /openapi.json and /graphql) to the app.rheaply.com web app, and neither the site, its llms.txt nor the support center documents any public API, SDK or MCP server.
  evidence:
  - status: 302
    url: https://api.rheaply.com/openapi.json
  - status: 200
    url: https://rheaply.com/llms.txt
  - status: 403
    url: https://support.rheaply.com/mcp
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: Rheaply is a circular-economy platform for enterprise asset lifecycle management. It gives organizations real-time inventory visibility, an internal reuse marketplace with approval workflows for reallocating surplus furniture, equipment, IT assets, and lab supplies, and sustainable disposition through a network of 3,400+ verified nonprofit and commercial partners. Rheaply helps companies, universities, and governments cut procurement costs, divert waste from landfill, track embodied-carbon savings, and run decommissioning and office move-outs. Backed by Techstars, the company operates a web application at app.rheaply.com. As of this enrichment pass Rheaply publishes no public developer/API program, SDKs, or OpenAPI surface.
image: https://rheaply.com/wp-content/uploads/Homepage.png
layout: provider
modified: '2026-10-20'
name: Rheaply
nav: Providers
network: true
overview: 'Rheaply is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Circular Economy, Sustainability, Asset Management, and Inventory.


  Rheaply''s developer surface includes documentation, signup flow, support, engineering blog, changelog, and 15 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 17.0
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.9
  facets:
    access_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 57.1
    operational_transparency: 21.1
  previous_composite: 20.9
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/rheaply/rheaply-2026-09-02T153753.png
security:
- kind: domain-security
  name: Rheaply Domain Security
  slug: rheaply-domain-security
  summary_line: TLSv1.3 · DMARC
slug: rheaply
tags:
- Company
- Circular Economy
- Sustainability
- Asset Management
- Inventory
- Reuse Marketplace
- Decommissioning
- ESG
website: https://rheaply.com/
---
