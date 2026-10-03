---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 4.5
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/avitide/refs/heads/main/llms/avitide-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/avitide-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/avitide/refs/heads/main/well-known/avitide-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/avitide-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avitide/refs/heads/main/hosts/avitide-hosts.yml
  title: ''
  type: Hosts
  url: hosts/avitide-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avitide/refs/heads/main/vendors/avitide-vendors.yml
  title: ''
  type: Vendors
  url: vendors/avitide-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://www.repligen.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.repligen.com/company/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://www.repligen.com/header-links/Login
- group: other
  title: ''
  type: Leadership
  url: https://www.repligen.com/company/leadership
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/avitide/refs/heads/main/security/avitide-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/avitide-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.repligen.com/
coverage:
  checked: 2026-09-27
  detail: The developer portal at https://portal.repligen.com returns HTML with a JavaScript SPA and no machine‑readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://portal.repligen.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-27'
description: Avitide is a product line of Repligen, a bioprocessing solutions company. It focuses on downstream processing technologies and services for biopharma manufacturing, offering chromatography, filtration, and process intensification solutions.
image: https://www.repligen.com/Social/repligen_default_twitter_card_image.png
layout: provider
modified: '2026-09-27'
name: Avitide
nav: Providers
network: true
overview: 'Avitide is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Bioprocessing, DownstreamProcessing, Chromatography, Filtration, and Biopharma.


  Avitide''s developer surface includes support and 9 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 10.5
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
    developer_ergonomics: 4.8
    discoverability: 57.1
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
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Avitide Domain Security
  slug: avitide-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: avitide
tags:
- Bioprocessing
- DownstreamProcessing
- Chromatography
- Filtration
- Biopharma
website: https://www.repligen.com/
---
