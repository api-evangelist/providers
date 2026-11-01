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
artifact_total: 4
common:
- group: other
  href: https://artifacts.apis.io/ilmateenistus/hosts/ilmateenistus-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ilmateenistus-hosts.yml
- group: other
  href: https://artifacts.apis.io/ilmateenistus/vendors/ilmateenistus-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ilmateenistus-vendors.yml
- group: auth
  href: https://artifacts.apis.io/ilmateenistus/security/ilmateenistus-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ilmateenistus-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ilmateenistus.ee/
- group: commercial
  title: ''
  type: TermsOfUse
  url: https://www.ilmateenistus.ee/meist/kasutustingimused/?lang=en
- group: operate
  title: ''
  type: Support
  url: https://www.ilmateenistus.ee/meist/kontakt/?lang=en
coverage:
  checked: '2026-10-28'
  detail: Ilmateenistus is a government weather agency that does not expose a public API.
  evidence:
  - status: 200
    url: https://www.ilmateenistus.ee/
  reason: not-a-software-company
  state: none
created: '2026-10-28'
description: Keskkonnaagentuur tagab ilmainfo ja turvatunde ning on teie jaoks olemas. Meilt saad ilmaprognoosi, vaatlusandmed 108-st seirejaamast üle Eesti. Meie ilmaradarid aitavad jälgida sajupilvede liikumist.
image: https://www.ilmateenistus.ee/wp-content/uploads/2025/06/keskkonnaagentuur_logo.png
layout: provider
modified: '2026-10-28'
name: Ilmateenistus
nav: Providers
network: true
overview: 'Ilmateenistus is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Weather, Environment, Estonia, Government, and API.


  Ilmateenistus'' developer surface includes support and 5 more developer resources.'
plans:
- name: Ilmateenistus Plans Pricing
  plan_count: 0
  slug: ilmateenistus-plans-pricing
random_paper: 23
scopes:
- name: Ilmateenistus Scopes
  scope_count: 0
  slug: ilmateenistus-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 8.8
  coverage:
    artifact_dirs: 20
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Ilmateenistus Authentication
  slug: ilmateenistus-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Ilmateenistus Domain Security
  slug: ilmateenistus-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: ilmateenistus
tags:
- Weather
- Environment
- Estonia
- Government
- API
website: https://ilmateenistus.ee/
---
