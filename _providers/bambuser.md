---
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.3
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Bambuser provides a video commerce platform with live shopping, shoppable video, and video consultation APIs.
  name: Bambuser API
  slug: bambuser-api
artifact_total: 5
common:
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bambuser.com/privacy-policy
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/bambuser/refs/heads/main/plans/bambuser-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bambuser-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://bambuser.com/security
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bambuser/refs/heads/main/llms/bambuser-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bambuser-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bambuser/refs/heads/main/mcp/bambuser-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bambuser-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bambuser/refs/heads/main/well-known/bambuser-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bambuser-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bambuser/refs/heads/main/hosts/bambuser-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bambuser-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bambuser/refs/heads/main/vendors/bambuser-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bambuser-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://bambuser.com/security
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bambuser
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bambuser/refs/heads/main/security/bambuser-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/bambuser-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bambuser/refs/heads/main/security/bambuser-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bambuser-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bambuser.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://bambuser.com/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://bambuser.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://bambuser.com/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://bambuser.com/docs/
- group: operate
  title: ''
  type: Support
  url: https://bambuser.com/contact
- group: company
  title: ''
  type: Blog
  url: https://bambuser.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://bambuser.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bambuser.com/terms-of-service
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://bambuser.com/mcp
  - status: 403
    url: https://dashboard.bambuser.com/mcp
  - status: 200
    url: https://bambuser.com/
  reason: no-developer-program
  state: none
created: '2026-10-15'
description: Bambuser provides a video commerce platform enabling brands and retailers to embed live shopping, shoppable video, and video consultation experiences directly into their websites and apps. The solution combines real‑time video streaming with interactive product overlays, AI‑driven product knowledge, and integration SDKs for iOS, Android, and web, helping merchants increase engagement and conversion through immersive, social shopping experiences.
image: https://cdn.prod.website-files.com/5de0e7623719a14060d5e857/66601a19b1c58b6be8ba370a_bambuser-open-graph-icon.gif
layout: provider
mcp_servers:
- description: Remote MCP server at mcp-prod-eu.liveshopping.bambuser.com requiring an API key.
  name: Bambuser MCP Server
  slug: bambuser-mcp-yml
modified: '2026-10-15'
name: Bambuser
nav: Providers
network: true
overview: 'Bambuser is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Video Commerce, Live Shopping, Shoppable Video, E-Commerce, and Software-as-a-Service.


  Bambuser''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, and 15 more developer resources.'
plans:
- name: Bambuser Plans Pricing
  plan_count: 4
  slug: bambuser-plans-pricing
random_paper: 13
score:
  band: thin
  composite: 34.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 78.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 66.7
    operational_transparency: 15.8
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bambuser Domain Security
  slug: bambuser-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Bambuser Trust Center
  slug: bambuser-trust-center
  summary_line: SOC 2, ISO 27001
slug: bambuser
tags:
- Video Commerce
- Live Shopping
- Shoppable Video
- E-Commerce
- Software-as-a-Service
website: https://bambuser.com/
---
