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
  href: https://artifacts.apis.io/dgfm-dk/llms/dgfm-dk-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dgfm-dk-llms.txt
- group: other
  href: https://artifacts.apis.io/dgfm-dk/hosts/dgfm-dk-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dgfm-dk-hosts.yml
- group: other
  href: https://artifacts.apis.io/dgfm-dk/vendors/dgfm-dk-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dgfm-dk-vendors.yml
- group: auth
  href: https://artifacts.apis.io/dgfm-dk/security/dgfm-dk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dgfm-dk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dgfm.dk/
- group: docs
  title: ''
  type: Documentation
  url: https://dgfm.dk/vejledninger
- group: company
  title: ''
  type: About
  url: https://dgfm.dk/om
- group: agent
  title: ''
  type: llms.txt
  url: https://dgfm.dk/llms.txt
coverage:
  checked: '2026-11-05'
  detail: The company provides procurement advisory services and does not expose a software API.
  evidence:
  - status: 200
    url: https://dgfm.dk/
  reason: not-a-software-company
  state: none
created: '2026-11-05'
description: Damsgaard FM provides procurement advisory services for property owners with many properties. They offer a single contract covering tenders across all your estates, with specialist work conducted through Properly.fm. Their mission is to simplify and professionalize public procurement for large real‑estate portfolios, ensuring compliance and efficiency.
image: https://dgfm.dk/og/forside.png
layout: provider
modified: '2026-11-05'
name: Damsgaard FM
nav: Providers
network: true
overview: 'Damsgaard FM is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Procurement, Real Estate, Advisory, Facility Management, and Denmark.


  Damsgaard FM''s developer surface includes documentation and 7 more developer resources.'
random_paper: 18
score:
  band: minimal
  composite: 5.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dgfm Dk Domain Security
  slug: dgfm-dk-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: dgfm-dk
tags:
- Procurement
- Real Estate
- Advisory
- Facility Management
- Denmark
- Company
website: https://dgfm.dk/
---
