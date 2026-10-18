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
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/eyeriss/refs/heads/main/llms/eyeriss-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/eyeriss-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/eyeriss/refs/heads/main/hosts/eyeriss-hosts.yml
  title: ''
  type: Hosts
  url: hosts/eyeriss-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/eyeriss/refs/heads/main/vendors/eyeriss-vendors.yml
  title: ''
  type: Vendors
  url: vendors/eyeriss-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/eyeriss/refs/heads/main/security/eyeriss-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/eyeriss-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.eyeris.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://www.eyeris.ai/about
- group: docs
  title: ''
  type: Documentation
  url: https://www.eyeris.ai/contact
- group: docs
  title: ''
  type: Documentation
  url: https://www.eyeris.ai/technology
- group: docs
  title: ''
  type: Documentation
  url: https://www.eyeris.ai/automotive
- group: company
  title: ''
  type: Blog
  url: https://www.eyeris.ai/press
coverage:
  checked: '2026-10-16'
  detail: The site provides no developer documentation or API reference pages.
  evidence:
  - status: 200
    url: https://www.eyeris.ai/
  reason: no-developer-program
  state: none
created: '2026-10-16'
description: Eyeriss, operating as Eyeris, is an automotive interior technology company focused on in‑cabin sensing AI. It develops advanced computer‑vision and AI solutions that monitor vehicle occupants to improve safety, comfort, and user experience, leveraging silicon‑valley based R&D and partnerships with automotive OEMs.
image: https://static.wixstatic.com/media/3b0818_81b7989bf45446fa844ca410c18abe7a%7Emv2.png/v1/fit/w_2500,h_1330,al_c/3b0818_81b7989bf45446fa844ca410c18abe7a%7Emv2.png
layout: provider
modified: '2026-10-16'
name: Eyeriss
nav: Providers
network: true
overview: 'Eyeriss is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Automotive, Artificial Intelligence, In‑cabin Sensing, and Technology.


  Eyeriss'' developer surface includes documentation, engineering blog, and 8 more developer resources.'
random_paper: 2
score:
  band: minimal
  composite: 6.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 55.4
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Eyeriss Domain Security
  slug: eyeriss-domain-security
  summary_line: TLSv1.3 · HSTS
slug: eyeriss
tags:
- Company
- Automotive
- Artificial Intelligence
- In‑cabin Sensing
- Technology
website: https://www.eyeris.ai/
---
