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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/breezm/refs/heads/main/llms/breezm-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/breezm-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/breezm/refs/heads/main/hosts/breezm-hosts.yml
  title: ''
  type: Hosts
  url: hosts/breezm-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://breezm.com/policy/privacy
- group: start
  title: ''
  type: Login
  url: https://breezm.com/user/signin
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/breezm/refs/heads/main/security/breezm-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/breezm-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://breezm.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://equityzen.com/company/breezm
  reason: no-developer-program
  state: none
created: '2026-10-03'
description: Breezm is a South Korean eyewear company that offers custom 3D‑scanned prescription glasses. Their platform lets users scan their face online, undergo a detailed 12‑step eye exam, and order personalized frames that are produced using 3D printing and laser cutting. The service emphasizes sustainability by reducing material waste and carbon emissions, and provides a 45‑day guarantee with after‑care support. Founded by Seong‑woo Kim and Hyung‑jin Park, Breezm operates retail locations in Seoul and ships internationally, blending technology with fashion to deliver tailored vision solutions.
image: https://breezm.com/img/seo/preview_breezm.png
layout: provider
modified: '2026-10-03'
name: Breezm
nav: Providers
network: true
overview: Breezm is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Eyewear, Custom Glasses, 3D Scanning, and Sustainable.
random_paper: 7
score:
  band: minimal
  composite: 9.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 55.4
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Breezm Domain Security
  slug: breezm-domain-security
  summary_line: TLSv1.2 · DMARC
slug: breezm
tags:
- Company
- Eyewear
- Custom Glasses
- 3D Scanning
- Sustainable
website: https://breezm.com
---
