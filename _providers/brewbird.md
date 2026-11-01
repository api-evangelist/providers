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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/brewbird/hosts/brewbird-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brewbird-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://brewbird.com/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://brewbird.com/blog
- group: auth
  href: https://artifacts.apis.io/brewbird/security/brewbird-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brewbird-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://brewbird.com/
coverage:
  checked: '2026-10-23'
  detail: Brewbird's website provides no developer documentation or API reference.
  evidence:
  - status: 200
    url: https://brewbird.com
  reason: no-developer-program
  state: none
created: '2026-10-23'
description: Brewbird provides self‑serve, whole‑bean specialty coffee solutions for offices and hospitality spaces. Their platform lets workplaces offer fresh brewed coffee on demand, using compostable pods filled with beans from top‑tier roasters. Brewbird emphasizes sustainability, zero‑fuss brewing, and a curated selection of local roasters, aiming to replace traditional coffee machines and reduce waste.
image: https://framerusercontent.com/images/CSTpfrHDl4rHQYTBtqKnVjB3M.png
layout: provider
modified: '2026-10-23'
name: Brewbird
nav: Providers
network: true
overview: 'Brewbird is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Coffee, B2B, Sustainability, and Office.


  Brewbird''s developer surface includes engineering blog and 4 more developer resources.'
random_paper: 9
score:
  band: minimal
  composite: 6.6
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
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Brewbird Domain Security
  slug: brewbird-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: brewbird
tags:
- Company
- Coffee
- B2B
- Sustainability
- Office
website: https://brewbird.com/
---
