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
  score: 3.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/dinilu-ch/llms/dinilu-ch-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dinilu-ch-llms.txt
- group: auth
  href: https://artifacts.apis.io/dinilu-ch/well-known/dinilu-ch-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dinilu-ch-security.txt
- group: agent
  href: https://artifacts.apis.io/dinilu-ch/well-known/dinilu-ch-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dinilu-ch-well-known.yml
- group: other
  href: https://artifacts.apis.io/dinilu-ch/hosts/dinilu-ch-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dinilu-ch-hosts.yml
- group: auth
  href: https://artifacts.apis.io/dinilu-ch/security/dinilu-ch-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dinilu-ch-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dinilu.ch/
coverage:
  checked: '2026-11-05'
  detail: Dinilu provides promotional products and has no public API surface.
  evidence:
  - status: 200
    url: https://dinilu.ch/
  reason: not-a-software-company
  state: none
created: '2026-11-05'
description: Dinilu is a supplier of bespoke promotional products, disposables and printed matter, primarily manufactured in the Far East. Since 2003, it serves companies across Europe, offering custom merchandise, branded gifts, and printed items with competitive pricing, transparent lead times, and quality control. The website provides tools to calculate costs and delivery times, detailed product catalogs, and contact options for quotations and support.
image: https://cdn.dinilu.ch/art/dinilu-1200x1200.png
layout: provider
modified: '2026-11-05'
name: Dinilu
nav: Providers
network: true
overview: Dinilu is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Advertising, Promotional Products, Printing, Custom Merchandise, and Europe.
random_paper: 5
score:
  band: minimal
  composite: 4.8
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
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 10.5
  provenance:
    mcp: unknown
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
  name: Dinilu Ch Domain Security
  slug: dinilu-ch-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: dinilu-ch
tags:
- Advertising
- Promotional Products
- Printing
- Custom Merchandise
- Europe
website: https://dinilu.ch/
---
