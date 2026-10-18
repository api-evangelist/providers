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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/circulate/refs/heads/main/llms/circulate-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/circulate-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/circulate/refs/heads/main/hosts/circulate-hosts.yml
  title: ''
  type: Hosts
  url: hosts/circulate-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/circulate/refs/heads/main/vendors/circulate-vendors.yml
  title: ''
  type: Vendors
  url: vendors/circulate-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/circulate/refs/heads/main/security/circulate-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/circulate-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://circulatepack.com/
- group: docs
  title: ''
  type: Documentation
  url: https://circulatepack.com/knowledge-hub
- group: start
  title: ''
  type: DeveloperPortal
  url: https://circulatepack.com/about-us
- group: commercial
  title: ''
  type: Pricing
  url: https://circulatepack.com/solutions/reporting
coverage:
  checked: '2026-10-08'
  detail: Documentation pages are JavaScript-rendered and provide no machine‑readable API specifications.
  evidence:
  - status: 200
    url: https://circulatepack.com/knowledge-hub
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-08'
description: Circulate is a sustainable packaging data platform founded in Sweden. It aggregates, structures, and enriches packaging supplier information, turning PDFs, spreadsheets, and certificates into a searchable database. The platform enables businesses to source compliant packaging quickly, reduces greenwashing, and supports sustainability reporting with AI‑driven insights.
image: https://circulatepack.com/images/hero-circulate.avif
layout: provider
modified: '2026-10-08'
name: Circulate
nav: Providers
network: true
overview: 'Circulate is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Packaging Data, Compliance Reporting, Sustainability, ERP Integration, and European Suppliers.


  Circulate''s developer surface includes documentation, pricing, and 6 more developer resources.'
random_paper: 10
score:
  band: minimal
  composite: 10.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 55.4
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Circulate Domain Security
  slug: circulate-domain-security
  summary_line: TLSv1.3 · DMARC
slug: circulate
tags:
- Packaging Data
- Compliance Reporting
- Sustainability
- ERP Integration
- European Suppliers
- PPWR
website: https://circulatepack.com/
---
