---
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: CPower provides a virtual power plant platform with APIs for energy management, DER aggregation, and analytics.
  name: CPower API
  slug: cpower-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/cpowerenergymanagement-com/hosts/cpowerenergymanagement-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cpowerenergymanagement-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/cpowerenergymanagement-com/vendors/cpowerenergymanagement-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cpowerenergymanagement-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/cpowerenergymanagement-com/security/cpowerenergymanagement-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cpowerenergymanagement-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cpowerenergy.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://cpowerenergy.com/
- group: docs
  title: ''
  type: Documentation
  url: https://cpowerenergy.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://cpowerenergy.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cpowerenergy.com/terms
coverage:
  checked: '2026-10-25'
  detail: Main site returns HTML pages and redirects for OpenAPI URLs, no machine‑readable spec found.
  evidence:
  - status: 301
    url: https://cpowerenergy.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-25'
description: CPower Energy is a national leader in unlocking the full value of Distributed Energy Resources (DERs). It provides a virtual power plant platform that enables energy users across the United States to save on energy costs, balance the grid, and achieve clean energy goals. The company offers advanced DER aggregation, real‑time optimization, and analytics to help utilities and large energy consumers manage demand response, peak shaving, and renewable integration. CPower’s solutions are deployed nationwide, supporting a transition to a more resilient and sustainable energy system.
layout: provider
modified: '2026-10-25'
name: CPower, Inc.
nav: Providers
network: true
overview: 'CPower, Inc. is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Virtual Power Plant, Distributed Energy Resources, and Clean Energy.


  CPower, Inc.''s developer surface includes documentation, pricing, and 6 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 12.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cpowerenergymanagement Com Domain Security
  slug: cpowerenergymanagement-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cpowerenergymanagement-com
tags:
- Company
- Energy
- Virtual Power Plant
- Distributed Energy Resources
- Clean Energy
website: https://cpowerenergy.com/
---
