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
    mcp_server: platform
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.7
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/beamtlc-com/llms/beamtlc-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/beamtlc-com-llms.txt
- group: build
  href: https://artifacts.apis.io/beamtlc-com/mcp/beamtlc-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/beamtlc-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/beamtlc-com/mcp/beamtlc-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/beamtlc-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/beamtlc-com/well-known/beamtlc-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/beamtlc-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/beamtlc-com/hosts/beamtlc-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/beamtlc-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/beamtlc-com/vendors/beamtlc-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/beamtlc-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://shopbeam.com/pages/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://shopbeam.com/pages/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://shopbeam.com/blogs/news
- group: auth
  href: https://artifacts.apis.io/beamtlc-com/security/beamtlc-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/beamtlc-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://beamtlc.com
- group: company
  title: ''
  type: About
  url: https://shopbeam.com/pages/about-us
- group: company
  title: ''
  type: Blog
  url: https://shopbeam.com/blogs/all
- group: operate
  title: ''
  type: Support
  url: https://shopbeam.com/pages/support
coverage:
  checked: '2026-10-23'
  detail: The provider’s website is a Shopify storefront that renders documentation via JavaScript and provides no machine‑readable API specification.
  evidence:
  - status: 301
    url: https://shopbeam.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-22'
description: Beam is a wellness-focused consumer brand offering science-backed nutritional supplements and health products. Through its online storefront shopbeam.com, Beam provides a range of items such as sleep aids, gut health powders, women's health supplements, and fitness nutrition. The company emphasizes evidence-based formulations and aims to improve everyday health and performance for a broad audience.
layout: provider
mcp_servers:
- description: Remote MCP server at beamtlc.myshopify.com.
  name: Beam MCP Server
  slug: beamtlc-com-mcp-yml
modified: '2026-10-22'
name: Beam
nav: Providers
network: true
overview: 'Beam is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Wellness, Supplements, Health, and E-commerce.


  Beam''s developer surface includes engineering blog, support, and 12 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 10.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 46.7
    operational_transparency: 0.0
  provenance:
    mcp: platform-generated
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Beamtlc Com Domain Security
  slug: beamtlc-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: beamtlc-com
tags:
- Company
- Wellness
- Supplements
- Health
- E-commerce
website: https://beamtlc.com
---
