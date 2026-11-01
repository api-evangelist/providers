---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 7.9
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/davis-instruments/llms/davis-instruments-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/davis-instruments-llms.txt
- group: agent
  href: https://artifacts.apis.io/davis-instruments/mcp/davis-instruments-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/davis-instruments-mcp.yml
- group: agent
  href: https://artifacts.apis.io/davis-instruments/well-known/davis-instruments-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/davis-instruments-well-known.yml
- group: other
  href: https://artifacts.apis.io/davis-instruments/hosts/davis-instruments-hosts.yml
  title: ''
  type: Hosts
  url: hosts/davis-instruments-hosts.yml
- group: other
  href: https://artifacts.apis.io/davis-instruments/vendors/davis-instruments-vendors.yml
  title: ''
  type: Vendors
  url: vendors/davis-instruments-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.davisinstruments.com/blogs/press
- group: auth
  href: https://artifacts.apis.io/davis-instruments/security/davis-instruments-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/davis-instruments-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://davisinstruments.com/
- group: operate
  title: ''
  type: Support
  url: https://www.davisinstruments.com/pages/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.davisinstruments.com/blogs/newsletter
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.davisinstruments.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.davisinstruments.com/policies/privacy-policy
coverage:
  checked: '2026-10-28'
  detail: Davis Instruments provides weather hardware but does not publish a public API or developer program.
  evidence:
  - status: 404
    url: https://www.davisinstruments.com/api
  reason: no-developer-program
  state: none
created: '2026-10-28'
description: Davis Instruments designs and manufactures personal and professional‑grade weather stations, marine instruments, and air‑quality monitors. The company provides high‑quality weather instruments for accurate data collection, offering reliable weather stations and sensors for hobbyists, researchers, and commercial users. Their product line includes the Vantage Vue, Vantage Pro2, and Vantage Pro2 Plus weather stations, as well as marine barometers and air‑quality monitoring devices.
image: https://www.davisinstruments.com/cdn/shop/files/1-1_AEM-Davis_Logo_Color_1d72da03-6ef5-4158-be6a-7ad3833e276b_1260x630.png?v=1717166114
layout: provider
mcp_servers:
- description: Remote MCP server at www.davisinstruments.com.
  name: Davis Instruments MCP Server
  slug: davis-instruments-mcp-yml
modified: '2026-10-28'
name: Davis Instruments
nav: Providers
network: true
overview: 'Davis Instruments is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Weather, Instruments, Sensors, and Environmental.


  Davis Instruments'' developer surface includes support, engineering blog, and 10 more developer resources.'
random_paper: 8
score:
  band: minimal
  composite: 10.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Davis Instruments Domain Security
  slug: davis-instruments-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: davis-instruments
tags:
- Company
- Weather
- Instruments
- Sensors
- Environmental
website: https://davisinstruments.com/
---
