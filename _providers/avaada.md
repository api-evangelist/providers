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
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/avaada/refs/heads/main/well-known/avaada-clarity-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/avaada-clarity-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/avaada/refs/heads/main/well-known/avaada-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/avaada-well-known.yml
- group: auth
  title: ''
  type: Security
  url: https://clarity.com/vdp
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/avaada/refs/heads/main/llms/avaada-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/avaada-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaada/refs/heads/main/hosts/avaada-hosts.yml
  title: ''
  type: Hosts
  url: hosts/avaada-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.avaada.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.avaada.com/privacy-policy/
- group: other
  title: ''
  type: Leadership
  url: https://www.avaada.com/leadership/
- group: company
  title: ''
  type: Blog
  url: https://www.avaada.com/blog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/avaada/refs/heads/main/security/avaada-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/avaada-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/avaada/refs/heads/main/security/avaada-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/avaada-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.avaada.com/
coverage:
  checked: 2026-09-26
  detail: Main website loads via JavaScript and no machine‑readable API spec was found despite probing known endpoints.
  evidence:
  - status: 0
    url: https://api.avaada.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-26'
description: Avaada is India’s largest clean energy conglomerate, integrating solar, wind, hydro, and battery energy storage solutions. The company provides affordable, round‑the‑clock power to accelerate India’s energy transition, offering renewable energy generation, green fuels, data center power, and sustainability services across a global footprint.
image: https://www.avaada.com/wp-content/uploads/SOlar-Home.jpg
layout: provider
modified: '2026-09-26'
name: Avaada
nav: Providers
network: true
overview: 'Avaada is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Clean Energy, Renewable Energy, Solar, Wind, and Battery Storage.


  Avaada''s developer surface includes engineering blog and 11 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 12.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.1
    operational_transparency: 10.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 16.4
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Avaada Domain Security
  slug: avaada-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Avaada Vulnerability Disclosure
  slug: avaada-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: avaada
tags:
- Clean Energy
- Renewable Energy
- Solar
- Wind
- Battery Storage
- Company
website: https://www.avaada.com/
---
