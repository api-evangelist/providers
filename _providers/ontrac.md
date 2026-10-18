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
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ontrac/refs/heads/main/hosts/ontrac-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ontrac-hosts.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ontrac
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ontrac/refs/heads/main/security/ontrac-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ontrac-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ontrac.com
- group: operate
  title: ''
  type: Support
  url: https://www.ontrac.com/support/
- group: docs
  title: ''
  type: Documentation
  url: https://www.ontrac.com/knowledge-center/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ontrac.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ontrac.com/privacy/
coverage:
  checked: '2026-10-14'
  detail: API reference endpoint returns 404 and documentation pages contain only HTML without a machine‑readable OpenAPI spec.
  evidence:
  - status: 404
    url: https://www.ontrac.com/api/
  - status: 200
    url: https://www.ontrac.com/knowledge-center/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-13'
description: OnTrac provides last‑mile delivery services for e‑commerce parcels across the western United States, offering ground, express, and specialized logistics solutions. Their platform integrates with major marketplaces and shipping software, enabling businesses to ship quickly and track packages in real time. OnTrac emphasizes reliability, speed, and customer support for both residential and commercial deliveries.
image: https://www.ontrac.com/wp-content/themes/ontrac/assets/images/ogp.jpg
layout: provider
modified: '2026-10-13'
name: OnTrac
nav: Providers
network: true
overview: 'OnTrac is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Logistics, Delivery, E-Commerce, Shipping, and United States.


  OnTrac''s developer surface includes support, documentation, and 6 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 12.4
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
    developer_ergonomics: 14.3
    discoverability: 48.2
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ontrac Domain Security
  slug: ontrac-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ontrac
tags:
- Logistics
- Delivery
- E-Commerce
- Shipping
- United States
website: https://www.ontrac.com
---
