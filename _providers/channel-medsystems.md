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
  href: https://raw.githubusercontent.com/api-evangelist/channel-medsystems/refs/heads/main/hosts/channel-medsystems-hosts.yml
  title: ''
  type: Hosts
  url: hosts/channel-medsystems-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/channel-medsystems/refs/heads/main/vendors/channel-medsystems-vendors.yml
  title: ''
  type: Vendors
  url: vendors/channel-medsystems-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.cerene.com/news
- group: other
  title: ''
  type: Leadership
  url: https://www.cerene.com/leadership
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/channel-medsystems/refs/heads/main/security/channel-medsystems-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/channel-medsystems-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cerene.com
- group: company
  title: ''
  type: Blog
  url: https://www.cerene.com/blog-1
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cerene.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cerene.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.cerene.com/contact-us
coverage:
  checked: '2026-10-08'
  detail: No public developer documentation or API specifications were found on Cerene's website.
  evidence:
  - status: 200
    url: https://www.cerene.com
  reason: no-developer-program
  state: none
created: '2026-10-08'
description: Cerene Cryotherapy develops and provides FDA‑cleared cryotherapy devices for the treatment of heavy menstrual bleeding and other gynecological conditions. The company offers a range of clinical solutions, training, and patient resources, targeting healthcare professionals and women seeking minimally invasive therapy. Cerene focuses on evidence‑based outcomes, safety information, and regulatory compliance, operating primarily in the United States.
image: http://static1.squarespace.com/static/6989076d9b77f94e3728bdd8/t/698b6b7c92bd8d242acf90d1/1770744700913/Know+Your+Flow+Logo++%282%29.png?format=1500w
layout: provider
modified: '2026-10-08'
name: Cerene
nav: Providers
network: true
overview: 'Cerene is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Health Tech, Cryotherapy, Women''s Health, Medical Devices, and FDA Cleared.


  Cerene''s developer surface includes engineering blog, support, and 8 more developer resources.'
random_paper: 6
score:
  band: minimal
  composite: 10.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 51.8
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Channel Medsystems Domain Security
  slug: channel-medsystems-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: channel-medsystems
tags:
- Health Tech
- Cryotherapy
- Women's Health
- Medical Devices
- FDA Cleared
website: https://www.cerene.com
---
