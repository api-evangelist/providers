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
    mcp_server: false
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
  score: 2.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/alpaycelik-dev/llms/alpaycelik-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/alpaycelik-dev-llms.txt
- group: other
  href: https://artifacts.apis.io/alpaycelik-dev/hosts/alpaycelik-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alpaycelik-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/alpaycelik-dev/vendors/alpaycelik-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/alpaycelik-dev-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AlpayC
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/AlpayC/mcp-migration-check/releases/latest
- group: auth
  href: https://artifacts.apis.io/alpaycelik-dev/security/alpaycelik-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alpaycelik-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://alpaycelik.dev/
coverage:
  checked: '2026-11-01'
  detail: No public API documentation or OpenAPI spec found; all probes to typical spec URLs returned 404.
  evidence:
  - status: 404
    url: https://api.alpaycelik.dev/openapi.json
  reason: no-developer-program
  state: none
created: '2026-11-01'
description: Alpay Celik is an AI full‑stack engineer based in North Rhine‑Westphalia, Germany, offering end‑to‑end software development services. The site showcases capabilities in building AI‑driven applications, covering data modeling, API design, front‑end implementation, and deployment. It highlights projects such as MCP migration checks, Abfall‑MCP, and Claude skill sets, and provides links to GitHub repositories, a status page, and an llms.txt index. The portfolio emphasizes agentic development, modern tooling, and a focus on verifiable, evidence‑backed software solutions.
image: https://alpaycelik.dev/portrait.webp
layout: provider
modified: '2026-11-01'
name: Alpay Celik
nav: Providers
network: true
overview: 'Alpay Celik is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Full-Stack, Engineer, Germany, and Software Development.


  Alpay Celik''s developer surface includes changelog and 6 more developer resources.'
random_paper: 3
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
  delta: -1.4
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 6.1
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Alpaycelik Dev Domain Security
  slug: alpaycelik-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: alpaycelik-dev
tags:
- Artificial Intelligence
- Full-Stack
- Engineer
- Germany
- Software Development
- Portfolio
website: https://alpaycelik.dev/
---
