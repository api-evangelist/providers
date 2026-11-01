---
agent_readiness:
  band: human-only
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Scan a UK parking ticket, council PCN, private parking charge, bus lane, ULEZ or Clean Air Zone notice, get the grounds and a drafted appeal, and have AppealGo file it.
  name: AppealGo API
  slug: appealgo-api
artifact_total: 3
common:
- group: design
  href: https://artifacts.apis.io/appealgo-com/conformance/appealgo-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/appealgo-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/appealgo-com/llms/appealgo-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/appealgo-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/appealgo-com/mcp/appealgo-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/appealgo-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/appealgo-com/hosts/appealgo-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/appealgo-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/appealgo-com/vendors/appealgo-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/appealgo-com-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://appealgo.com/status
- group: auth
  href: https://artifacts.apis.io/appealgo-com/security/appealgo-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/appealgo-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://appealgo.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://appealgo.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://appealgo.com/guides
- group: docs
  title: ''
  type: APIReference
  url: https://appealgo.com/api/v1/openapi.json
- group: commercial
  title: ''
  type: TermsOfService
  url: https://appealgo.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://appealgo.com/privacy
created: '2026-10-29'
description: AppealGo provides an online service that helps drivers appeal parking tickets and Penalty Charge Notices (PCNs) across the UK. Using AI, the platform processes uploaded ticket images or PDFs, generates appeal letters, and can file them with the relevant council or parking operator on the user’s behalf. The service offers a free initial check and charges a fee only if the appeal proceeds, with refunds if filing fails. It supports multiple councils, offers fleet management tools, and provides resources such as deadline calculators and contravention code guides.
image: https://appealgo.com/opengraph-image.png?opengraph-image.2kx2xzqf9atda.png
layout: provider
mcp_servers:
- description: Remote MCP server at appealgo.com requiring an API key.
  name: appealgo-com MCP Server
  slug: appealgo-com-mcp-yml
modified: '2026-10-29'
name: appealgo-com
nav: Providers
network: true
overview: 'appealgo-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Parking, AI, UK, and Appeals.


  appealgo-com''s developer surface includes documentation, API reference, and 11 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 18.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 65.0
    operational_transparency: 15.8
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Appealgo Com Domain Security
  slug: appealgo-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: appealgo-com
tags:
- Company
- Parking
- AI
- UK
- Appeals
website: https://appealgo.com/
---
