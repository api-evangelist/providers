---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: ASAPDEVS provides a Machine Control Protocol (MCP) endpoint at https://asapdevs.it/api/mcp, but it requires authentication and the contract is not publicly accessible.
  name: ASAPDEVS API
  slug: asapdevs-api
artifact_total: 4
common:
- group: agent
  href: https://artifacts.apis.io/asapdevs-it/llms/asapdevs-it-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/asapdevs-it-llms.txt
- group: other
  href: https://artifacts.apis.io/asapdevs-it/hosts/asapdevs-it-hosts.yml
  title: ''
  type: Hosts
  url: hosts/asapdevs-it-hosts.yml
- group: other
  href: https://artifacts.apis.io/asapdevs-it/vendors/asapdevs-it-vendors.yml
  title: ''
  type: Vendors
  url: vendors/asapdevs-it-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://asapdevs.it/privacy-policy
- group: auth
  href: https://artifacts.apis.io/asapdevs-it/security/asapdevs-it-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/asapdevs-it-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://asapdevs.it/
- group: company
  title: ''
  type: Blog
  url: https://asapdevs.it/blog
- group: operate
  title: ''
  type: Support
  url: https://asapdevs.it/contact
coverage:
  checked: '2026-11-02'
  detail: MCP endpoint requires authentication, returning 406 Not Acceptable for tools/list request.
  evidence:
  - status: 406
    url: https://asapdevs.it/api/mcp
  reason: auth-required
  state: gated
created: '2026-11-01'
description: ASAPDEVS sp. z o.o. is a Polish software house founded in 2015, offering end‑to‑end digital solutions. With over 200 successful deployments, they build e‑commerce stores, web and mobile applications, AI‑driven automations, and provide ongoing IT support and maintenance. Their team operates remotely across Poland and internationally, delivering custom software, migrations, and consultancy services. They emphasize security, implementing ISO/IEC 27001 standards and data protection agreements for client projects.
image: https://asapdevs.it/assets/img/asapdevs-logo-light.png
layout: provider
modified: '2026-11-02'
name: ASAPDEVS sp. z o.o.
nav: Providers
network: true
overview: 'ASAPDEVS sp. z o.o. is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Software House, Poland, E-Commerce, AI Automation, and IT Support.


  ASAPDEVS sp. z o.o.''s developer surface includes engineering blog, support, and 6 more developer resources.'
random_paper: 17
scopes:
- name: Asapdevs It Scopes
  scope_count: 0
  slug: asapdevs-it-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 7.9
  coverage:
    artifact_dirs: 19
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.0
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 57.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - poland
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - cee
    - europe
  previous_composite: 9.9
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Asapdevs It Authentication
  slug: asapdevs-it-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Asapdevs It Domain Security
  slug: asapdevs-it-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: asapdevs-it
tags:
- Software House
- Poland
- E-Commerce
- AI Automation
- IT Support
website: https://asapdevs.it/
---
