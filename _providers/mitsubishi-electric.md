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
artifact_total: 2
common:
- group: auth
  title: ''
  type: Security
  url: https://www.mitsubishielectric.com/psirt/policy/index.html
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mitsubishi-electric/refs/heads/main/well-known/mitsubishi-electric-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/mitsubishi-electric-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/mitsubishi-electric/refs/heads/main/well-known/mitsubishi-electric-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mitsubishi-electric-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/mitsubishi-electric/refs/heads/main/hosts/mitsubishi-electric-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mitsubishi-electric-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/mitsubishi-electric/refs/heads/main/vendors/mitsubishi-electric-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mitsubishi-electric-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://www.mitsubishielectric.com/en/about/management/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MitsubishiElectric
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mitsubishi-electric/refs/heads/main/security/mitsubishi-electric-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/mitsubishi-electric-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mitsubishi-electric/refs/heads/main/security/mitsubishi-electric-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mitsubishi-electric-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.mitsubishielectric.com
coverage:
  checked: '2026-10-14'
  detail: No machine‑readable API specification was found on the company’s sites.
  evidence:
  - status: 200
    url: https://www.mitsubishielectric.com/en/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-13'
description: Mitsubishi Electric is a global leader in manufacturing and selling electrical and electronic equipment, including factory automation, building systems, energy solutions, and transportation technologies. The company operates worldwide, offering innovative products and services across multiple sectors such as industrial automation, HVAC, power systems, and smart infrastructure. Its extensive portfolio supports digital transformation and sustainability initiatives, delivering advanced solutions for factories, homes, and public infrastructure.
image: https://www.mitsubishielectric.com/global/common/img/fb_logo_mitsubishi.gif
layout: provider
modified: '2026-10-13'
name: Mitsubishi Electric
nav: Providers
network: true
overview: Mitsubishi Electric is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Electronics, Automation, Energy, and Infrastructure.
random_paper: 19
score:
  band: minimal
  composite: 6.5
  coverage:
    artifact_dirs: 5
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
    discoverability: 50.0
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 9.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Mitsubishi Electric Domain Security
  slug: mitsubishi-electric-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Mitsubishi Electric Vulnerability Disclosure
  slug: mitsubishi-electric-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: mitsubishi-electric
tags:
- Company
- Electronics
- Automation
- Energy
- Infrastructure
website: https://www.mitsubishielectric.com
---
