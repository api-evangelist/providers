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
  href: https://raw.githubusercontent.com/api-evangelist/lansforsakringar/refs/heads/main/hosts/lansforsakringar-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lansforsakringar-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lansforsakringar.se/other-languages/english/about-lansforsakringar/lansforsakringar-bank/terms-of-usage-for-emtn-base-prospectus/
- group: company
  title: ''
  type: Newsroom
  url: https://www.lansforsakringar.se/other-languages/english/about-lansforsakringar/press/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/lansforsakringar/refs/heads/main/security/lansforsakringar-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lansforsakringar-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lansforsakringar.se/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://lansforsakringar.se/
  reason: no-developer-program
  state: none
created: '2026-10-14'
description: Länsförsäkringar is a Swedish financial services group offering banking, insurance, loans, savings and pension products. It operates regionally across Sweden, providing digital and physical services to private customers and businesses. The company’s website presents extensive information about its offerings, corporate governance, sustainability initiatives, and customer support.
image: https://www.lansforsakringar.se/4901eb/globalassets/stockholm/bilder/topp/sthlm_pano1200x648.jpg?w=1200&h=630
layout: provider
modified: '2026-10-14'
name: Länsförsäkringar
nav: Providers
network: true
overview: Länsförsäkringar is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Banking, Insurance, Financial Services, and Sweden.
random_paper: 3
score:
  band: minimal
  composite: 5.9
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 8.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Lansforsakringar Domain Security
  slug: lansforsakringar-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: lansforsakringar
tags:
- Company
- Banking
- Insurance
- Financial Services
- Sweden
website: https://lansforsakringar.se/
---
