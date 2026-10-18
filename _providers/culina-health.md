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
  href: https://raw.githubusercontent.com/api-evangelist/culina-health/refs/heads/main/hosts/culina-health-hosts.yml
  title: ''
  type: Hosts
  url: hosts/culina-health-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/culina-health/refs/heads/main/vendors/culina-health-vendors.yml
  title: ''
  type: Vendors
  url: vendors/culina-health-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://culinahealth.com/registered-dietitians
- group: company
  title: ''
  type: Blog
  url: https://culinahealth.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CulinaHealth
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/culina-health/refs/heads/main/security/culina-health-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/culina-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://culinahealth.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://my.culinahealth.com/mcp
  - status: 200
    url: https://culinahealth.com/
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: no-developer-program
  state: none
created: '2026-10-11'
description: Culina Health provides virtual registered dietitian nutrition services, offering personalized nutrition care through telehealth. Their mission is to make expert nutrition accessible for everyone, addressing chronic health conditions with science‑based, inclusive, and culturally affirming dietitian support. They serve patients across the United States via an online platform, offering specialty programs for hormone health, weight loss, eating disorders, gastrointestinal health, and more.
image: https://culinahealth.com/wp-content/uploads/2026/01/Website-Thumbnail.png
layout: provider
modified: '2026-10-11'
name: Culina Health
nav: Providers
network: true
overview: 'Culina Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Health, Nutrition, Telehealth, Dietitian, and VirtualCare.


  Culina Health''s developer surface includes signup flow, engineering blog, and 5 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 7.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Culina Health Domain Security
  slug: culina-health-domain-security
  summary_line: TLSv1.3 · DMARC
slug: culina-health
tags:
- Health
- Nutrition
- Telehealth
- Dietitian
- VirtualCare
website: https://culinahealth.com/
---
