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
  href: https://raw.githubusercontent.com/api-evangelist/conbody/refs/heads/main/hosts/conbody-hosts.yml
  title: ''
  type: Hosts
  url: hosts/conbody-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/conbody/refs/heads/main/vendors/conbody-vendors.yml
  title: ''
  type: Vendors
  url: vendors/conbody-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/conbody/refs/heads/main/security/conbody-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/conbody-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://conbody.com
- group: operate
  title: ''
  type: ContactUs
  url: https://conbody.com/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://conbody.com/privacy-policy/
coverage:
  checked: '2026-10-10'
  detail: Conbody's website provides fitness class information but no developer program or API documentation.
  evidence:
  - status: 200
    url: https://conbody.com
  reason: no-developer-program
  state: none
created: '2026-10-10'
description: Conbody offers prison‑style fitness classes in New York City, founded by Coss Marte while incarcerated. The program uses bodyweight workouts in a 9×6 cell‑like setting, emphasizing discipline and community. Since 2014, CONBODY provides classes, personal training, and a documentary about its origins, aiming to transform lives through rigorous, machine‑free exercise.
image: https://conbody.com/wp-content/themes/conbody/redesign/assets/coss-class.jpg
layout: provider
modified: '2026-10-10'
name: Conbody
nav: Providers
network: true
overview: Conbody is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Fitness, Health, Community, NYC, and Bodyweight.
random_paper: 2
score:
  band: minimal
  composite: 6.3
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
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Conbody Domain Security
  slug: conbody-domain-security
  summary_line: TLSv1.3 · DMARC
slug: conbody
tags:
- Fitness
- Health
- Community
- NYC
- Bodyweight
website: https://conbody.com
---
