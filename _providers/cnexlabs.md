---
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
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/cnexlabs/hosts/cnexlabs-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cnexlabs-hosts.yml
- group: other
  href: https://artifacts.apis.io/cnexlabs/vendors/cnexlabs-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cnexlabs-vendors.yml
- group: auth
  href: https://artifacts.apis.io/cnexlabs/security/cnexlabs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cnexlabs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://equityzen.com/company/cnexlabs
coverage:
  checked: '2026-10-09'
  detail: The cnexlabs.com site serves HTML with JavaScript rendering and no machine‑readable API spec was found.
  evidence:
  - status: 200
    url: https://www.cnexlabs.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-09'
description: Cnexlabs is a privately held semiconductor storage company founded in 2013, developing innovative NVMe and Open-Channel SSD controller solutions. Based in San Jose, CA, it partners with storage manufacturers and data center customers to deliver next‑generation storage semiconductor and software products.
layout: provider
modified: '2026-10-09'
name: Cnexlabs
nav: Providers
network: true
overview: Cnexlabs is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 8
score:
  band: minimal
  composite: 2.2
  coverage:
    artifact_dirs: 4
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 35.7
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 2.2
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cnexlabs Domain Security
  slug: cnexlabs-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cnexlabs
tags:
- Company
website: https://equityzen.com/company/cnexlabs
---
