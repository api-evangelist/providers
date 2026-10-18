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
artifact_total: 2
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/galley/refs/heads/main/plans/galley-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/galley-plans-pricing.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/galley/refs/heads/main/hosts/galley-hosts.yml
  title: ''
  type: Hosts
  url: hosts/galley-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/galley/refs/heads/main/vendors/galley-vendors.yml
  title: ''
  type: Vendors
  url: vendors/galley-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://support.galleysolutions.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/galley/refs/heads/main/security/galley-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/galley-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.galleysolutions.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.galleysolutions.com/pricing-test
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.galleysolutions.com/terms
- group: company
  title: ''
  type: Blog
  url: https://www.galleysolutions.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://www.galleysolutions.com/demo-reservation
coverage:
  checked: '2026-10-13'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract was found on the provider's hosts.
  evidence:
  - status: 404
    url: https://api.galleysolutions.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-13'
description: Galley Solutions provides culinary resource planning software that helps kitchens manage inventory, scheduling, and financial reporting. The platform offers tools for menu planning, supplier coordination, and real‑time analytics to improve operational efficiency and reduce waste. Targeted at restaurants, catering services, and food‑service enterprises, Galley aims to align kitchen creativity with financial accuracy, supporting both small independent eateries and large multi‑site operations.
image: http://static1.squarespace.com/static/6007cf1ee5265a1eeaa92165/t/6a95e901299ba568fe1f9e6a/1788209409869/galley-og-1200x630.png?format=1500w
layout: provider
modified: '2026-10-13'
name: Galley
nav: Providers
network: true
overview: 'Galley is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Culinary, Software-as-a-Service, ResourcePlanning, and RestaurantTech.


  Galley''s developer surface includes support, pricing, engineering blog, getting-started guide, and 6 more developer resources.'
plans:
- name: Galley Plans Pricing
  plan_count: 1
  slug: galley-plans-pricing
random_paper: 0
score:
  band: emerging
  composite: 16.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Galley Domain Security
  slug: galley-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: galley
tags:
- Company
- Culinary
- Software-as-a-Service
- ResourcePlanning
- RestaurantTech
website: https://www.galleysolutions.com
---
