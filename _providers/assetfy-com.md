---
access_model:
  confidence: medium
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 24.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/assetfy-com/plans/assetfy-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/assetfy-com-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/assetfy-com/security/assetfy-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/assetfy-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/assetfy-com/authentication/assetfy-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/assetfy-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/assetfy-com/conformance/assetfy-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/assetfy-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/assetfy-com/llms/assetfy-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/assetfy-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/assetfy-com/well-known/assetfy-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/assetfy-com-security.txt
- group: agent
  href: https://artifacts.apis.io/assetfy-com/well-known/assetfy-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/assetfy-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/assetfy-com/hosts/assetfy-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/assetfy-com-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://assetfy.com/news/
- group: auth
  href: https://artifacts.apis.io/assetfy-com/security/assetfy-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/assetfy-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/assetfy-com/security/assetfy-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/assetfy-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://assetfy.com/
- group: company
  title: ''
  type: Blog
  url: https://assetfy.com/geoportal-news/de/
- group: commercial
  title: ''
  type: Pricing
  url: https://assetfy.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://assetfy.com/impressum/
- group: start
  title: ''
  type: GettingStarted
  url: https://assetfy.com/start/
coverage:
  checked: '2026-11-02'
  detail: The provider's public website does not expose any machine‑readable API specification such as OpenAPI, AsyncAPI, GraphQL SDL, gRPC or WSDL.
  evidence:
  - status: 200
    url: https://assetfy.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: 'Assetfy verbindet Claude, ChatGPT und andere KI-Tools über einen MCP-Konnektor mit amtlichen Geodaten: Flurstücke, Gebäude, Bebauungspläne aus 15 Bundesländern, Bodenrichtwerte, Gelände und LoD2-Gebäude in 3D. Architekten und Planer fragen nach einem Grundstück und bekommen Baurecht, Gelände und Nachbarbebauung in die Antwort, dazu einen Lageplan als DXF, IFC oder PDF. Der Konnektor ist im Tarif PROFESSIONAL enthalten.'
image: https://assetfy.com/images/assetfy_globe.png
layout: provider
modified: '2026-11-01'
name: Assetfy
nav: Providers
network: true
overview: 'Assetfy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Real Estate, Geodata, Architecture, Artificial Intelligence, and MCP.


  Assetfy''s developer surface includes authentication, engineering blog, pricing, getting-started guide, and 12 more developer resources.'
plans:
- name: Assetfy Com Plans Pricing
  plan_count: 1
  slug: assetfy-com-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Assetfy Com Rate Limits
  slug: assetfy-com-rate-limits
score:
  band: emerging
  composite: 19.7
  coverage:
    artifact_dirs: 14
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.9
  facets:
    access_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 49.1
    operational_transparency: 10.5
  previous_composite: 23.6
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Assetfy Com Authentication
  slug: assetfy-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Assetfy Com Domain Security
  slug: assetfy-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Assetfy Com Vulnerability Disclosure
  slug: assetfy-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: assetfy-com
tags:
- Real Estate
- Geodata
- Architecture
- Artificial Intelligence
- MCP
website: https://assetfy.com/
---
