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
- group: other
  href: https://artifacts.apis.io/deepsightinc-com/hosts/deepsightinc-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/deepsightinc-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/deepsightinc-com/vendors/deepsightinc-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/deepsightinc-com-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: http://deepsight.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.deepsight.com/news
- group: auth
  href: https://artifacts.apis.io/deepsightinc-com/security/deepsightinc-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/deepsightinc-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.deepsight.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.deepsight.com/
  reason: no-developer-program
  state: none
created: '2026-10-24'
description: DeepSight Technology develops advanced physical AI platforms powered by next‑generation ultrasound sensors. Their NeedleVue™ technology delivers exceptional clarity, precision, and confidence for real‑time interventional imaging across medical applications. Backed by Wing Venture Capital, DeepSight aims to transform diagnostic and therapeutic procedures with AI‑driven insights.
image: http://static1.squarespace.com/static/687a711668b01e2fa0e2e38a/t/687a728d8bd84c175d073a12/1752855181516/DeepSight+%28TM%29+Tech+2-clr+blk%402x.png?format=1500w
layout: provider
modified: '2026-10-24'
name: Deepsight
nav: Providers
network: true
overview: Deepsight is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Ultrasound, Medical Imaging, and Technology.
random_paper: 3
score:
  band: minimal
  composite: 6.4
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
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Deepsightinc Com Domain Security
  slug: deepsightinc-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: deepsightinc-com
tags:
- Company
- AI
- Ultrasound
- Medical Imaging
- Technology
website: https://www.deepsight.com/
---
