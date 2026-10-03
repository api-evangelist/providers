---
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
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.8
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: Machine‑Control‑Protocol API providing access to Deeplead's lead generation functions.
  name: Deeplead MCP API
  slug: deeplead-mcp-api
artifact_total: 4
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
  url: https://www.deeplead.io/info/about
- group: docs
  title: ''
  type: APIReference
  url: https://www.deeplead.io/mcp
- group: start
  title: ''
  type: GettingStarted
  url: https://www.deelead.io/
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
coverage:
  checked: '2026-09-27'
  detail: Deeplead's MCP API page provides only HTML documentation without a machine‑readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://www.deeplead.io/mcp
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-27'
description: Deeplead provides an automated cold‑email outreach platform that helps businesses generate qualified leads by analyzing prospect websites, LinkedIn, and other data sources. The service combines AI‑generated email copy, inbox warm‑up, deliverability testing, and multi‑channel follow‑ups to accelerate the sales pipeline. Users input their target market and receive personalized outreach campaigns that aim to secure replies within days, backed by analytics on open rates, response rates, and ROI.
image: https://deeplead.io/opengraph-image
layout: provider
mcp_servers:
- description: ''
  name: Deeplead MCP Server
  slug: deeplead-mcp-server
modified: '2026-09-27'
name: Deeplead
nav: Providers
network: true
overview: 'Deeplead publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Lead Generation, Cold Email, Artificial Intelligence, and Sales Automation.


  Deeplead''s developer surface includes support, documentation, API reference, getting-started guide, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Deeplead Plans Pricing
  plan_count: 1
  slug: deeplead-plans-pricing
random_paper: 6
score:
  band: emerging
  composite: 24.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 60.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
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
