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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/arkerah-com/llms/arkerah-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/arkerah-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/arkerah-com/well-known/arkerah-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/arkerah-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/arkerah-com/hosts/arkerah-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arkerah-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/arkerah-com/vendors/arkerah-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/arkerah-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/arkerah-com/security/arkerah-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arkerah-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arkerah.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://arkerah.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://arkerah.com/terms
coverage:
  checked: '2026-11-02'
  detail: No documentation host or machine‑readable API specification was found on arkerah.com or its subdomains.
  evidence:
  - status: 200
    url: https://arkerah.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: arkerah is a European job‑matching service that ranks open corporate positions in the Netherlands, Belgium, France, Germany and Spain against a candidate’s profile. It hides roles the candidate is unlikely to obtain and automatically generates a tailored CV for each suitable position. The platform is free to use, offers AI‑assisted storytelling, and provides transparent ranking methodology. Founded to simplify job search, arkerah leverages data‑driven algorithms and a user‑friendly web interface to streamline applications across multiple markets, helping job seekers focus on realistic opportunities.
image: https://arkerah.com/brand/arkerah-icon-512.png
layout: provider
modified: '2026-11-01'
name: arkerah
nav: Providers
network: true
overview: arkerah is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Job Matching, Careers, Europe, and Artificial Intelligence.
random_paper: 18
score:
  band: minimal
  composite: 5.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.6
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 39.3
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
  previous_composite: 9.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Arkerah Com Domain Security
  slug: arkerah-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: arkerah-com
tags:
- Job Matching
- Careers
- Europe
- Artificial Intelligence
website: https://arkerah.com/
---
