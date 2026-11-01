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
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/altair-semi-com/hosts/altair-semi-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/altair-semi-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/altair-semi-com/vendors/altair-semi-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/altair-semi-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.altairsemi.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.altairsemi.com/privacy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.altairsemi.com/news/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.altairsemi.com/developer/
- group: company
  title: ''
  type: Blog
  url: https://www.altairsemi.com/blog/
- group: auth
  href: https://artifacts.apis.io/altair-semi-com/security/altair-semi-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/altair-semi-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://altair-semi.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://altair-semi.com/
  reason: no-developer-program
  state: none
created: '2026-10-21'
description: Altair Semiconductor provides cellular IoT chipsets, including LTE‑M, NB‑IoT, LPWA and 5G‑ready modems and system‑on‑chip solutions. Its products integrate ultra‑low‑power connectivity, hardware security and carrier‑grade iSIM for industrial and consumer applications such as smart meters, wearables, trackers and vehicle telematics.
image: https://www.altairsemi.com/wp-content/uploads/2026/03/og_image_altair.png
layout: provider
modified: '2026-10-21'
name: Altair Semiconductor
nav: Providers
network: true
overview: 'Altair Semiconductor is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Cellular IoT, LTE‑M, NB‑IoT, LPWA, and Modems.


  Altair Semiconductor''s developer surface includes engineering blog and 8 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 11.4
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
    developer_ergonomics: 11.9
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: derived
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
  name: Altair Semi Com Domain Security
  slug: altair-semi-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: altair-semi-com
tags:
- Cellular IoT
- LTE‑M
- NB‑IoT
- LPWA
- Modems
- System‑on‑Chip
- IoT Chipsets
website: https://altair-semi.com/
---
