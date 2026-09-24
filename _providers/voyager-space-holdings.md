---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: true
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.2
  scored_at: '2026-09-24'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://voyagertechnologies.com
- group: company
  title: ''
  type: About
  url: https://voyagertechnologies.com/our-story/
- group: company
  title: ''
  type: Newsroom
  url: https://voyagertechnologies.com/newsroom/
- group: company
  title: ''
  type: Blog
  url: https://voyagertechnologies.com/insights/
- group: company
  title: ''
  type: BlogRSS
  url: https://voyagertechnologies.com/press-releases/feed/
- group: company
  title: ''
  type: Careers
  url: https://voyagertechnologies.com/company/join-us/
- group: company
  title: ''
  type: InvestorRelations
  url: https://investors.voyagertechnologies.com/
- group: operate
  title: ''
  type: Contact
  url: https://voyagertechnologies.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://voyagertechnologies.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://voyagertechnologies.com/privacy-policy-2/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/voyagertechnologies-inc
- group: other
  title: ''
  type: X
  url: https://x.com/voyagertech_
- group: other
  title: ''
  type: X-SecondaryMarket
  url: https://forgeglobal.com/voyager-space-holdings_stock/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/voyager-space-holdings/refs/heads/main/mcp/voyager-space-holdings-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/voyager-space-holdings-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/voyager-space-holdings/refs/heads/main/well-known/voyager-space-holdings-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/voyager-space-holdings-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/voyager-space-holdings/refs/heads/main/well-known/voyager-space-holdings-robots.txt
  title: ''
  type: ContentSignal
  url: well-known/voyager-space-holdings-robots.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/voyager-space-holdings/refs/heads/main/authentication/voyager-space-holdings-authentication.yml
  title: ''
  type: Authentication
  url: authentication/voyager-space-holdings-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/voyager-space-holdings/refs/heads/main/scopes/voyager-space-holdings-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/voyager-space-holdings-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/voyager-space-holdings/refs/heads/main/conformance/voyager-space-holdings-conformance.yml
  title: ''
  type: Conformance
  url: conformance/voyager-space-holdings-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/voyager-space-holdings/refs/heads/main/llms/voyager-space-holdings-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/voyager-space-holdings-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/voyager-space-holdings/refs/heads/main/security/voyager-space-holdings-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/voyager-space-holdings-domain-security.yml
coverage:
  checked: '2026-09-18'
  detail: Voyager Technologies is a defense and space hardware manufacturer (propulsion, energetics, C4ISR electronics, lunar landers) whose site has no developer, docs or API section; the only machine surface on voyagertechnologies.com is the WordPress CMS's MCP adapter, which answers 401 to anonymous tools/list.
  evidence:
  - status: 404
    url: https://voyagertechnologies.com/developers
  - status: 404
    url: https://voyagertechnologies.com/openapi.json
  - status: 404
    url: https://voyagertechnologies.com/.well-known/agent-card.json
  - status: 401
    url: https://voyagertechnologies.com/wp-json/mcp/mcp-oauth-server
  - status: 301
    url: https://voyagerspace.com/
  reason: not-a-software-company
  state: none
created: '2026-09-18'
description: 'Voyager Technologies, Inc. (NYSE: VOYG), formerly Voyager Space Holdings, is a Denver-based defense and space technology company that listed on the New York Stock Exchange in June 2025. It delivers domestic end-to-end propulsion and energetics, spectrum-dominance and C4ISR electronics, science and space-exploration hardware, mission management and lunar systems, and is a partner in the Starlab commercial space station. Since 2019 it has acquired twelve companies, including Nanoracks (commercial ISS payload services), ZIN Technologies, Space Micro, Valley Tech Systems, Altius Space Machines, ExoTerra, Estes Energetics and Astrobotic. Voyager Space rebranded to Voyager Technologies in January 2025; voyagerspace.com now redirects to voyagertechnologies.com. The company publishes no developer program, public API, SDK or machine-readable contract; the only machine surface on its domain is the WordPress MCP adapter guarding the corporate CMS.'
image: https://voyagertechnologies.com/wp-content/uploads/2026/05/Voyager-Technologies-OG-Image.png
layout: provider
mcp_servers:
- description: ''
  name: Voyager Technologies MCP Server
  slug: voyager-technologies-mcp-server
modified: '2026-09-18'
name: Voyager Technologies
nav: Providers
network: true
overview: 'Voyager Technologies is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Space, Defense, Aerospace, and Propulsion.


  Voyager Technologies'' developer surface includes engineering blog, authentication, and 19 more developer resources.'
random_paper: 13
scopes:
- name: Voyager Space Holdings Scopes
  scope_count: 0
  slug: voyager-space-holdings-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 14.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 50.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 14.3
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Voyager Space Holdings Authentication
  slug: voyager-space-holdings-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Voyager Space Holdings Domain Security
  slug: voyager-space-holdings-domain-security
  summary_line: TLSv1.3 · DMARC
slug: voyager-space-holdings
tags:
- Company
- Space
- Defense
- Aerospace
- Propulsion
- Satellite
- Lunar
- Space Stations
- Public Company
website: https://voyagertechnologies.com
---
