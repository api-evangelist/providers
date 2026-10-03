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
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: Baebies provides diagnostic testing platforms; see their website for product information.
  name: Baebies API
  slug: baebies-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/baebies/refs/heads/main/hosts/baebies-hosts.yml
  title: ''
  type: Hosts
  url: hosts/baebies-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/baebies/refs/heads/main/vendors/baebies-vendors.yml
  title: ''
  type: Vendors
  url: vendors/baebies-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://baebies.com/privacy-policy/
- group: company
  title: ''
  type: Blog
  url: https://baebies.com/category/blog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/baebies/refs/heads/main/security/baebies-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/baebies-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://baebies.com
coverage:
  checked: 2026-09-27
  detail: Baebies website provides only marketing pages with no machine‑readable API specification.
  evidence:
  - status: 0
    url: https://api.baebies.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-27'
description: Baebies is a diagnostics company specializing in digital microfluidics technology to deliver rapid, multifunctional point‑of‑care tests. Based in Durham, North Carolina, Baebies creates platforms such as the FINDER series for G6PD, Flu A/B, SARS‑CoV‑2, and Anti‑Factor Xa, aiming to bring high‑quality testing to laboratories and bedside settings worldwide.
layout: provider
modified: '2026-09-27'
name: Baebies
nav: Providers
network: true
overview: 'Baebies publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Diagnostics, Digital Microfluidics, Point of Care, and Healthcare.


  Baebies'' developer surface includes engineering blog and 5 more developer resources.'
random_paper: 11
score:
  band: minimal
  composite: 7.2
  coverage:
    artifact_dirs: 4
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 53.6
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.8
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Baebies Domain Security
  slug: baebies-domain-security
  summary_line: TLSv1.3 · DMARC
slug: baebies
tags:
- Company
- Diagnostics
- Digital Microfluidics
- Point of Care
- Healthcare
website: https://baebies.com
---
