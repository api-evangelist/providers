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
- group: docs
  title: ''
  type: Documentation
  url: https://docs.malachyte.com/
- group: auth
  href: https://artifacts.apis.io/malachyte/well-known/malachyte-malachyte1-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/malachyte-malachyte1-security.txt
- group: agent
  href: https://artifacts.apis.io/malachyte/well-known/malachyte-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/malachyte-well-known.yml
- group: other
  href: https://artifacts.apis.io/malachyte/hosts/malachyte-hosts.yml
  title: ''
  type: Hosts
  url: hosts/malachyte-hosts.yml
- group: other
  href: https://artifacts.apis.io/malachyte/vendors/malachyte-vendors.yml
  title: ''
  type: Vendors
  url: vendors/malachyte-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://help.malachyte.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.malachyte.com/get-started/headless
- group: auth
  href: https://artifacts.apis.io/malachyte/security/malachyte-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/malachyte-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.malachyte.com/
- group: company
  title: ''
  type: Blog
  url: https://www.malachyte.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.malachyte.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.malachyte.com/privacy-policy
created: '2026-10-24'
description: Malachyte provides a real‑time personalization platform that builds live shopper profiles from the first click, without requiring login or historical data. Backed by Gradient Ventures with a $10M seed round, the company helps retailers increase add‑to‑cart rates and conversion by delivering intent‑based product recommendations. Their solution integrates via APIs and SDKs to power continuous, intent‑driven experiences across e‑commerce sites.
image: https://www.malachyte.com/og/malachyte-share.png
layout: provider
modified: '2026-10-24'
name: Malachyte
nav: Providers
network: true
overview: 'Malachyte is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Personalization, Retail, Real-time, and API.


  Malachyte''s developer surface includes documentation, support, getting-started guide, engineering blog, and 8 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 15.9
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
    developer_ergonomics: 28.6
    discoverability: 48.2
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Malachyte Domain Security
  slug: malachyte-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: malachyte
tags:
- Company
- Personalization
- Retail
- Real-time
- API
website: https://www.malachyte.com/
---
