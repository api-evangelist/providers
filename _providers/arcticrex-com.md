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
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/arcticrex-com/llms/arcticrex-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/arcticrex-com-llms.txt
- group: other
  href: https://artifacts.apis.io/arcticrex-com/hosts/arcticrex-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arcticrex-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/arcticrex-com/vendors/arcticrex-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/arcticrex-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/arcticrex-com/security/arcticrex-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arcticrex-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.arcticrex.com/
- group: company
  title: ''
  type: Blog
  url: https://www.arcticrex.com/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.arcticrex.com/privacy.html
coverage:
  checked: '2026-11-02'
  detail: ArcticRex is a Finnish AI advisory firm offering consulting services and does not provide a public API.
  evidence:
  - status: 200
    url: https://www.arcticrex.com/
  reason: not-a-software-company
  state: none
created: '2026-11-01'
description: ArcticRex is a Finnish AI advisory firm specializing in cybersecurity and critical infrastructure environments. The company provides hands‑on strategic advice, organizational upskilling, and training programs to help leaders and engineers integrate AI safely and securely. Their services focus on developing secure AI strategies, risk mitigation, and compliance with industry regulations, leveraging deep expertise in both artificial intelligence and cyber defense. ArcticRex works with enterprises to design AI roadmaps, conduct threat modeling, and implement governance frameworks. Their team of seasoned AI practitioners and security experts delivers customized workshops and continuous support to ensure resilient AI deployments across critical sectors.
image: https://www.arcticrex.com/assets/logo-horizontal.png
layout: provider
modified: '2026-11-01'
name: ArcticRex
nav: Providers
network: true
overview: 'ArcticRex is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Cybersecurity, Advisory, Training, and Finland.


  ArcticRex''s developer surface includes engineering blog and 6 more developer resources.'
random_paper: 9
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.5
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 48.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - finland
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - nordics
  previous_composite: 6.5
  provenance:
    mcp: derived
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
  name: Arcticrex Com Domain Security
  slug: arcticrex-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: arcticrex-com
tags:
- Artificial Intelligence
- Cybersecurity
- Advisory
- Training
- Finland
website: https://www.arcticrex.com/
---
