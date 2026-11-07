---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: MCP tool list for AnwaltX providing various legal compensation calculators and utilities.
  name: AnwaltX MCP
  slug: anwaltx-mcp
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/anwaltx-de/plans/anwaltx-de-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/anwaltx-de-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/anwaltx-de/llms/anwaltx-de-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/anwaltx-de-llms.txt
- group: build
  href: https://artifacts.apis.io/anwaltx-de/mcp/anwaltx-de-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/anwaltx-de-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/anwaltx-de/mcp/anwaltx-de-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/anwaltx-de-mcp.yml
- group: agent
  href: https://artifacts.apis.io/anwaltx-de/well-known/anwaltx-de-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/anwaltx-de-well-known.yml
- group: other
  href: https://artifacts.apis.io/anwaltx-de/hosts/anwaltx-de-hosts.yml
  title: ''
  type: Hosts
  url: hosts/anwaltx-de-hosts.yml
- group: other
  href: https://artifacts.apis.io/anwaltx-de/vendors/anwaltx-de-vendors.yml
  title: ''
  type: Vendors
  url: vendors/anwaltx-de-vendors.yml
- group: auth
  href: https://artifacts.apis.io/anwaltx-de/security/anwaltx-de-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/anwaltx-de-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://anwaltx.de/
- group: docs
  title: ''
  type: Documentation
  url: https://anwaltx.de/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://anwaltx.de/docs
- group: docs
  title: ''
  type: APIReference
  url: https://anwaltx.de/docs
- group: operate
  title: ''
  type: Support
  url: https://anwaltx.de/contact
- group: company
  title: ''
  type: Blog
  url: https://anwaltx.de/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://anwaltx.de/preise
- group: start
  title: ''
  type: SignUp
  url: https://anwaltx.de/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://anwaltx.de/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://anwaltx.de/datenschutz
created: '2026-11-01'
description: AnwaltX is a KI‑gestützte Rechtsassistenz für Online‑Händler, Amazon‑Seller und Creator. Die Plattform analysiert hochgeladene Schreiben oder beschriebene Fälle, ermittelt Fristen, liefert rechtliche Einschätzungen und generiert Antwortentwürfe. Sie deckt Abmahnungen, Kontosperrungen, Vertragsprüfung, AGB‑Erstellung und DSGVO‑Compliance ab und bietet ein monatliches Abonnement von 64,99 €.
examples:
- key_count: 2
  name: Anwaltx De Mcp Tools
  slug: anwaltx-de-mcp-tools
image: https://anwaltx.de/og-image.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at anwaltx.de.
  name: AnwaltX MCP Server
  slug: anwaltx-de-mcp-yml
modified: '2026-11-01'
name: AnwaltX
nav: Providers
network: true
overview: 'AnwaltX is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Legal Tech, Artificial Intelligence, E-Commerce, Compliance, and Germany.


  AnwaltX''s developer surface includes documentation, API reference, support, engineering blog, pricing, signup flow, and 12 more developer resources.'
plans:
- name: Anwaltx De Plans Pricing
  plan_count: 3
  slug: anwaltx-de-plans-pricing
random_paper: 5
score:
  band: emerging
  composite: 19.7
  coverage:
    artifact_dirs: 11
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.4
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 65.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 28.1
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Anwaltx De Domain Security
  slug: anwaltx-de-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: anwaltx-de
tags:
- Legal Tech
- Artificial Intelligence
- E-Commerce
- Compliance
- Germany
website: https://anwaltx.de/
---
