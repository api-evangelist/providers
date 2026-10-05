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
  href: https://raw.githubusercontent.com/api-evangelist/aragen-life-sciences/refs/heads/main/llms/aragen-life-sciences-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aragen-life-sciences-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aragen-life-sciences/refs/heads/main/hosts/aragen-life-sciences-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aragen-life-sciences-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aragen.com/utlities/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aragen.com/utlities/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.aragen.com/news/project-ascent-goes-live/
- group: other
  title: ''
  type: Leadership
  url: https://www.aragen.com/our-company/leadership/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aragen-life-sciences/refs/heads/main/security/aragen-life-sciences-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aragen-life-sciences-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aragen.com
created: '2026-09-25'
description: Aragen Life Sciences provides contract research, development, and manufacturing services (CRDMO) for small and large molecule drug discovery and development. The company offers integrated solutions across chemistry, biology, analytical development, and GMP manufacturing, supporting clients from early discovery through commercial production. Their platform includes scientific expertise, global locations, and a resource hub for investors and partners.
image: https://www.aragen.com/wp-content/uploads/2021/07/PR-OG-Image.jpg
layout: provider
modified: '2026-09-25'
name: Aragen Life Sciences
nav: Providers
network: true
overview: Aragen Life Sciences is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Contract Research, Drug Discovery, Manufacturing, and Biotechnology.
random_paper: 15
score:
  band: minimal
  composite: 9.8
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 58.9
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aragen Life Sciences Domain Security
  slug: aragen-life-sciences-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aragen-life-sciences
tags:
- Company
- Contract Research
- Drug Discovery
- Manufacturing
- Biotechnology
website: https://www.aragen.com
---
