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
  href: https://artifacts.apis.io/automate/hosts/automate-hosts.yml
  title: ''
  type: Hosts
  url: hosts/automate-hosts.yml
- group: other
  href: https://artifacts.apis.io/automate/vendors/automate-vendors.yml
  title: ''
  type: Vendors
  url: vendors/automate-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://automate.com/dms/contact-us/contact-support/
- group: commercial
  title: ''
  type: Pricing
  url: https://automate.com/dms/pricing/
- group: company
  title: ''
  type: Blog
  url: https://automate.com/blog/
- group: auth
  href: https://artifacts.apis.io/automate/security/automate-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/automate-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://automate.com/
coverage:
  checked: '2026-10-28'
  detail: No OpenAPI or other machine-readable contract found despite accessible documentation pages.
  evidence:
  - status: 403
    url: https://api.automate.com/openapi.json
  - status: 403
    url: https://automate.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Automate provides dealer management software solutions, including variable operations, eDeal, sales and finance, eContracting, service merchandising, parts, payroll, and more. Their platform helps automotive dealerships streamline operations, improve efficiency, and integrate various business functions into a unified system.
image: https://automate.com/wp-content/uploads/2026/04/Dealer-site-launch-web-banner-1883x312_opt3.jpg
layout: provider
modified: '2026-10-28'
name: Automate
nav: Providers
network: true
overview: 'Automate is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Automotive, DealerManagement, Software, and SaaS.


  Automate''s developer surface includes support, pricing, engineering blog, and 4 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 7.0
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
    developer_ergonomics: 7.1
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
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Automate Domain Security
  slug: automate-domain-security
  summary_line: TLSv1.3 · DMARC
slug: automate
tags:
- Company
- Automotive
- DealerManagement
- Software
- SaaS
website: https://automate.com/
---
