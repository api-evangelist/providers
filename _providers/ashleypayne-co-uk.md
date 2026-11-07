---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/ashleypayne-co-uk/llms/ashleypayne-co-uk-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ashleypayne-co-uk-llms.txt
- group: agent
  href: https://artifacts.apis.io/ashleypayne-co-uk/mcp/ashleypayne-co-uk-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/ashleypayne-co-uk-mcp.yml
- group: other
  href: https://artifacts.apis.io/ashleypayne-co-uk/hosts/ashleypayne-co-uk-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ashleypayne-co-uk-hosts.yml
- group: other
  href: https://artifacts.apis.io/ashleypayne-co-uk/vendors/ashleypayne-co-uk-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ashleypayne-co-uk-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ashleypayne.co.uk/privacy
- group: auth
  href: https://artifacts.apis.io/ashleypayne-co-uk/security/ashleypayne-co-uk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ashleypayne-co-uk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ashleypayne.co.uk/
- group: company
  title: ''
  type: About
  url: https://www.ashleypayne.co.uk/about
- group: operate
  title: ''
  type: Contact
  url: https://www.ashleypayne.co.uk/contact
coverage:
  checked: '2026-11-01'
  detail: Ashley Payne offers consulting services and has no public API developer program.
  evidence:
  - status: 200
    url: https://www.ashleypayne.co.uk/
  reason: not-a-software-company
  state: none
created: '2026-11-01'
description: Ashley Payne is a fractional CTO and technical co‑founder offering AI‑enabled software solutions, diagnostics, and consulting. He helps businesses define technical strategy, build bespoke SaaS platforms, and implement AI automation, focusing on data‑driven decision making and scalable architecture.
image: https://www.ashleypayne.co.uk/assets/img/og-card.png
layout: provider
mcp_servers:
- description: Remote MCP server at www.ashleypayne.co.uk.
  name: Ashley Payne MCP Server
  slug: ashleypayne-co-uk-mcp-yml
modified: '2026-11-01'
name: Ashley Payne
nav: Providers
network: true
overview: Ashley Payne is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Consulting, Artificial Intelligence, Fractional-CTO, Software Engineering, and United Kingdom.
random_paper: 7
score:
  band: minimal
  composite: 4.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.3
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.3
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 6.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ashleypayne Co Uk Domain Security
  slug: ashleypayne-co-uk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ashleypayne-co-uk
tags:
- Consulting
- Artificial Intelligence
- Fractional-CTO
- Software Engineering
- United Kingdom
website: https://www.ashleypayne.co.uk/
---
