---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/autoridaddigital-com/plans/autoridaddigital-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/autoridaddigital-com-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/autoridaddigital-com/security/autoridaddigital-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/autoridaddigital-com-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/autoridaddigital-com/llms/autoridaddigital-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/autoridaddigital-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/autoridaddigital-com/mcp/autoridaddigital-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/autoridaddigital-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/autoridaddigital-com/well-known/autoridaddigital-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/autoridaddigital-com-security.txt
- group: auth
  href: https://artifacts.apis.io/autoridaddigital-com/well-known/autoridaddigital-com-autoridaddigital-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/autoridaddigital-com-autoridaddigital-security.txt
- group: agent
  href: https://artifacts.apis.io/autoridaddigital-com/well-known/autoridaddigital-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/autoridaddigital-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/autoridaddigital-com/hosts/autoridaddigital-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/autoridaddigital-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/autoridaddigital-com/vendors/autoridaddigital-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/autoridaddigital-com-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.autoridaddigital.com/en/privacy
- group: auth
  href: https://artifacts.apis.io/autoridaddigital-com/security/autoridaddigital-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/autoridaddigital-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/autoridaddigital-com/security/autoridaddigital-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/autoridaddigital-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://autoridaddigital.com/
- group: company
  title: ''
  type: Blog
  url: https://www.autoridaddigital.com/blog
coverage:
  checked: '2026-11-02'
  detail: Autoridad Digital provides SEO and digital marketing services and does not expose a public API.
  evidence:
  - status: 200
    url: https://www.autoridaddigital.com/
  reason: not-a-software-company
  state: none
created: '2026-11-02'
description: Autoridad Digital es una agencia especializada en SEO avanzado, GEO (Generative Engine Optimization) y construcción de autoridad digital para dominar nichos. Fundada por Federico Noya y operada por TONYBERIA SL en Fuengirola, España, ofrece servicios de SEO, GEO, Answer Engine Optimization, Topical Authority, Authority Stacking y Digital PR, atendiendo a clientes en España y América Latina.
image: https://www.autoridaddigital.com/autoridad-digital-logo.png
layout: provider
mcp_servers:
- description: Remote MCP server at www.autoridaddigital.com.
  name: Autoridad Digital MCP Server
  slug: autoridaddigital-com-mcp-yml
modified: '2026-11-02'
name: Autoridad Digital
nav: Providers
network: true
overview: 'Autoridad Digital is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include SEO, Digital Marketing, Geo, Spain, and Agency.


  Autoridad Digital''s developer surface includes engineering blog and 13 more developer resources.'
plans:
- name: Autoridaddigital Com Plans Pricing
  plan_count: 4
  slug: autoridaddigital-com-plans-pricing
random_paper: 15
score:
  band: emerging
  composite: 13.6
  coverage:
    artifact_dirs: 10
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.6
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 48.3
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - spain
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 15.2
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Autoridaddigital Com Domain Security
  slug: autoridaddigital-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Autoridaddigital Com Vulnerability Disclosure
  slug: autoridaddigital-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: autoridaddigital-com
tags:
- SEO
- Digital Marketing
- Geo
- Spain
- Agency
website: https://autoridaddigital.com/
---
