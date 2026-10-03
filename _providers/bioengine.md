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
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bioengine/refs/heads/main/llms/bioengine-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bioengine-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bioengine/refs/heads/main/hosts/bioengine-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bioengine-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bioengine/refs/heads/main/vendors/bioengine-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bioengine-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.bioengine-global.com/news/1-85349764.html
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bioengine/refs/heads/main/security/bioengine-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bioengine-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bioengine-global.com
- group: operate
  title: ''
  type: ContactUs
  url: https://www.bioengine-global.com/contact-us
- group: company
  title: ''
  type: Careers
  url: https://www.bioengine-global.com/careers
coverage:
  checked: '2026-09-28'
  detail: The BioEngine website provides product information but no machine‑readable API specification.
  evidence:
  - status: 200
    url: https://www.bioengine-global.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-28'
description: Bioengine (Shanghai BioEngine Sci-Tech Co., Ltd.) is a China‑based provider of serum‑free cell culture media and bioprocess services. With over 30 years of experience, it offers custom media solutions for antibodies, vaccines, and cell‑ and gene‑therapy production, serving global biopharma partners from its GMP‑certified manufacturing facility.
image: https://www.bioengine-global.com/uploads/202339648/logo202312141747083213424.png
layout: provider
modified: '2026-09-28'
name: Bioengine
nav: Providers
network: true
overview: Bioengine is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Biotechnology, Cell Culture, Biopharma, Media Manufacturing, and China.
random_paper: 20
score:
  band: minimal
  composite: 4.3
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
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bioengine Domain Security
  slug: bioengine-domain-security
  summary_line: TLSv1.3
slug: bioengine
tags:
- Biotechnology
- Cell Culture
- Biopharma
- Media Manufacturing
- China
website: https://www.bioengine-global.com
---
