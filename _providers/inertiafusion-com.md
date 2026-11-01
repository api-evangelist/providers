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
    mcp_server: documented
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
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/inertiafusion-com/hosts/inertiafusion-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/inertiafusion-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/inertiafusion-com/vendors/inertiafusion-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/inertiafusion-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://inertia.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://inertia.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://inertia.com/press
- group: auth
  href: https://artifacts.apis.io/inertiafusion-com/security/inertiafusion-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/inertiafusion-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://inertia.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.inertiafusion.com
  reason: no-developer-program
  state: none
created: '2026-10-24'
description: Inertia is a commercial fusion energy company focused on delivering limitless, clean power through advanced laser-driven fusion technology. The company builds modular laser systems and mass‑produces fusion fuel targets to operate gigawatt‑scale power plants, aiming to provide safe, affordable energy for millions of homes worldwide. Inertia’s leadership includes seasoned entrepreneurs and scientists driving the transition from experimental ignition to commercial energy generation.
image: https://inertia.com/images/inertia.png
layout: provider
modified: '2026-10-24'
name: Inertia
nav: Providers
network: true
overview: Inertia is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Fusion, CleanTech, and Renewable.
random_paper: 20
score:
  band: minimal
  composite: 9.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 11.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Inertiafusion Com Domain Security
  slug: inertiafusion-com-domain-security
  summary_line: TLSv1.3
slug: inertiafusion-com
tags:
- Company
- Energy
- Fusion
- CleanTech
- Renewable
website: https://inertia.com
---
