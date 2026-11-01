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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.3
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Lumeo provides video analytics APIs as described in their documentation hub.
  name: Lumeo API
  slug: lumeo-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/lumeo/plans/lumeo-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/lumeo-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/lumeo/changelog/lumeo-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/lumeo-changelog.yml
- group: design
  href: https://artifacts.apis.io/lumeo/conformance/lumeo-conformance.yml
  title: ''
  type: Conformance
  url: conformance/lumeo-conformance.yml
- group: agent
  href: https://artifacts.apis.io/lumeo/llms/lumeo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lumeo-llms.txt
- group: agent
  href: https://artifacts.apis.io/lumeo/mcp/lumeo-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/lumeo-mcp.yml
- group: agent
  href: https://artifacts.apis.io/lumeo/well-known/lumeo-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/lumeo-well-known.yml
- group: other
  href: https://artifacts.apis.io/lumeo/hosts/lumeo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lumeo-hosts.yml
- group: other
  href: https://artifacts.apis.io/lumeo/vendors/lumeo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/lumeo-vendors.yml
- group: build
  href: https://artifacts.apis.io/lumeo/packages/lumeo-packages.yml
  title: ''
  type: SDKs
  url: packages/lumeo-packages.yml
- group: build
  href: https://artifacts.apis.io/lumeo/packages/lumeo-packages.yml
  title: ''
  type: Packages
  url: packages/lumeo-packages.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.lumeo.com/
- group: auth
  title: ''
  type: Security
  url: https://www.lumeo.com/verticals/security
- group: auth
  href: https://artifacts.apis.io/lumeo/security/lumeo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lumeo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lumeo.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lumeo.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.lumeo.com
- group: start
  title: ''
  type: GettingStarted
  url: https://www.lumeo.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.lumeo.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.lumeo.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.lumeo.com/contact
- group: start
  title: ''
  type: SignUp
  url: https://www.lumeo.com/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lumeo.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lumeo.com/legal
- group: build
  title: ''
  type: Postman
  url: https://www.lumeo.com
coverage:
  checked: '2026-10-12'
  detail: Documentation site renders via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://docs.lumeo.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-12'
description: Lumeo provides an AI-powered video analytics platform that enables businesses to build, customize, and deploy video analytics solutions quickly. The platform offers AI search, flexible dashboards, drag‑and‑drop analytics builder, and a library of pre‑trained AI models for use cases such as retail customer behavior, logistics monitoring, security, and healthcare. Users can sign up for a free trial, request demos, and integrate the solution via APIs and SDKs, making it suitable for integrators, partners, and enterprises seeking scalable video analytics.
finops:
- has_sources: true
  method: derived
  name: Lumeo Finops
  primary_unit: seat
  service_category: ''
  slug: lumeo-finops
  template: false
image: https://www.lumeo.com/assets/og-image.png
layout: provider
mcp_servers:
- description: Remote MCP server at docs.lumeo.com.
  name: Lumeo MCP Server
  slug: lumeo-mcp-yml
modified: '2026-10-12'
name: Lumeo
nav: Providers
network: true
overview: 'Lumeo is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Video Analytics, Platform, and Enterprise.


  Lumeo''s developer surface includes changelog, documentation, getting-started guide, pricing, engineering blog, support, signup flow, and 17 more developer resources.'
plans:
- name: Lumeo Plans Pricing
  plan_count: 4
  slug: lumeo-plans-pricing
- name: Lumeo Price Estimates
  plan_count: 0
  slug: lumeo-price-estimates
random_paper: 18
score:
  band: developing
  composite: 40.7
  coverage:
    artifact_dirs: 11
    catalog_earned: 47.0
    catalog_earned_first_party: 12.0
    catalog_gap: 68.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.6
  facets:
    access_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 56.7
    operational_transparency: 26.3
  previous_composite: 39.1
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Lumeo Domain Security
  slug: lumeo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lumeo
tags:
- Company
- Artificial Intelligence
- Video Analytics
- Platform
- Enterprise
website: https://lumeo.com
---
