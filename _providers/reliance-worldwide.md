---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: platform
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.6
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: REST API for RWC's Streamlabs smart water monitor brand, covering locations (get, list, update home/away mode), water usage and usage summaries, and alert subscriptions delivered to a customer endpoin
  name: Streamlabs Water Developer API
  slug: streamlabs-water-developer-api
artifact_total: 6
common:
- group: design
  href: https://artifacts.apis.io/reliance-worldwide/conventions/reliance-worldwide-conventions.yml
  title: ''
  type: Conventions
  url: conventions/reliance-worldwide-conventions.yml
- group: auth
  href: https://artifacts.apis.io/reliance-worldwide/authentication/reliance-worldwide-authentication.yml
  title: ''
  type: Authentication
  url: authentication/reliance-worldwide-authentication.yml
- group: design
  href: https://artifacts.apis.io/reliance-worldwide/lifecycle/reliance-worldwide-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/reliance-worldwide-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/reliance-worldwide/errors/reliance-worldwide-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/reliance-worldwide-error-codes.yml
- group: design
  href: https://artifacts.apis.io/reliance-worldwide/conformance/reliance-worldwide-conformance.yml
  title: ''
  type: Conformance
  url: conformance/reliance-worldwide-conformance.yml
- group: agent
  href: https://artifacts.apis.io/reliance-worldwide/llms/reliance-worldwide-streamlabs-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/reliance-worldwide-streamlabs-llms.txt
- group: agent
  href: https://artifacts.apis.io/reliance-worldwide/mcp/reliance-worldwide-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/reliance-worldwide-mcp.yml
- group: agent
  href: https://artifacts.apis.io/reliance-worldwide/well-known/reliance-worldwide-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/reliance-worldwide-well-known.yml
- group: other
  href: https://artifacts.apis.io/reliance-worldwide/hosts/reliance-worldwide-hosts.yml
  title: ''
  type: Hosts
  url: hosts/reliance-worldwide-hosts.yml
- group: other
  href: https://artifacts.apis.io/reliance-worldwide/vendors/reliance-worldwide-vendors.yml
  title: ''
  type: Vendors
  url: vendors/reliance-worldwide-vendors.yml
- group: auth
  href: https://artifacts.apis.io/reliance-worldwide/security/reliance-worldwide-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/reliance-worldwide-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.rwc.com/
- group: company
  title: ''
  type: About
  url: https://www.rwc.com/about-rwc
- group: company
  title: ''
  type: Newsroom
  url: https://www.rwc.com/news
- group: company
  title: ''
  type: Investors
  url: https://www.rwc.com/investors
- group: company
  title: ''
  type: Careers
  url: https://www.rwc.com/careers
- group: operate
  title: ''
  type: Support
  url: https://www.rwc.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rwc.com/privacy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/reliance-worldwide-corporation
created: '2026-10-22'
description: 'Reliance Worldwide Corporation Limited (RWC, ASX: RWC) is a global manufacturer of plumbing, heating and water control solutions, founded in Brisbane, Australia in 1949. Through a family of brands including SharkBite, HoldRite, Cash Acme, John Guest, Eastman, EZ-FLO, RMC, Holman and Auspex, it sells plumbing, water management, irrigation and building services products into residential and commercial new construction, repair and remodel markets across the Americas, EMEA and APAC, distributed through wholesale, retail and OEM channels. RWC publishes no public developer portal or API documentation on rwc.com.'
image: https://www.rwc.com/themes/custom/rwc_theme/components/images/favicon/favicon-196x196.png
layout: provider
mcp_servers:
- description: Remote MCP server for the Streamlabs online store (streamlabswater.com), RWC's smart water monitoring brand. The store's own llms.txt advertises it, and so does its /.well-known/ucp profile (UCP versi
  name: Streamlabs (Reliance Worldwide) UCP shopping MCP server
  slug: universal-commerce
modified: '2026-10-22'
name: Reliance Worldwide
nav: Providers
network: true
overview: 'Reliance Worldwide is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Plumbing, Manufacturing, Building Products, and Water Control.


  Reliance Worldwide''s developer surface includes authentication, support, and 17 more developer resources.'
plans:
- name: Reliance Worldwide Plans Pricing
  plan_count: 0
  slug: reliance-worldwide-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Reliance Worldwide Rate Limits
  slug: reliance-worldwide-rate-limits
score:
  band: emerging
  composite: 17.0
  coverage:
    artifact_dirs: 16
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 66.7
    operational_transparency: 0.0
  previous_composite: 17.0
  provenance:
    conformance: first-party
    mcp: platform-generated
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Reliance Worldwide Authentication
  slug: reliance-worldwide-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Reliance Worldwide Domain Security
  slug: reliance-worldwide-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: reliance-worldwide
tags:
- Company
- Plumbing
- Manufacturing
- Building Products
- Water Control
- Heating
- ASX Listed
- Australia
website: https://www.rwc.com/
---
