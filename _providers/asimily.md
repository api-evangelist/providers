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
  href: https://raw.githubusercontent.com/api-evangelist/asimily/refs/heads/main/llms/asimily-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/asimily-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/asimily/refs/heads/main/hosts/asimily-hosts.yml
  title: ''
  type: Hosts
  url: hosts/asimily-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/asimily/refs/heads/main/vendors/asimily-vendors.yml
  title: ''
  type: Vendors
  url: vendors/asimily-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.asimily.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://asimily.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://asimily.com/press/
- group: other
  title: ''
  type: Leadership
  url: https://asimily.com/about-us/leadership/
- group: company
  title: ''
  type: Blog
  url: https://asimily.com/blog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/asimily/refs/heads/main/security/asimily-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/asimily-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://asimily.com/
coverage:
  checked: 2026-09-26
  detail: API specification endpoints like https://api.asimily.com/openapi.json return DNS errors, providing no machine‑readable contract.
  evidence:
  - status: DNS_ERROR
    url: https://api.asimily.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-26'
description: Asimily provides a proactive cyber asset defense platform that offers IoT device visibility, risk modeling, segmentation, and automated remediation. It serves industries such as healthcare, energy, financial services, and manufacturing, helping organizations continuously monitor, prioritize, and mitigate cyber risks across IT, OT, and IoT environments.
layout: provider
modified: '2026-09-26'
name: Asimily
nav: Providers
network: true
overview: 'Asimily is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, IoT, Cybersecurity, Asset Management, and Risk Modeling.


  Asimily''s developer surface includes engineering blog and 9 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 9.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 55.4
    operational_transparency: 15.8
  provenance:
    mcp: derived
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
  name: Asimily Domain Security
  slug: asimily-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: asimily
tags:
- Company
- IoT
- Cybersecurity
- Asset Management
- Risk Modeling
website: https://asimily.com/
---
