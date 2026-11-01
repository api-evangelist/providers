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
api_count: 1
apis:
- description: Real-time AI security API providing prompt-layer defense and threat monitoring.
  name: PromptHalo API
  slug: prompthalo-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: Security
  url: https://prompthalo.ai/trustcenter/policies/vulnerability-disclosure.html
- group: auth
  href: https://artifacts.apis.io/prompthalo/well-known/prompthalo-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/prompthalo-security.txt
- group: auth
  href: https://artifacts.apis.io/prompthalo/well-known/prompthalo-prompthalo-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/prompthalo-prompthalo-security.txt
- group: agent
  href: https://artifacts.apis.io/prompthalo/well-known/prompthalo-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/prompthalo-well-known.yml
- group: other
  href: https://artifacts.apis.io/prompthalo/hosts/prompthalo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/prompthalo-hosts.yml
- group: other
  href: https://artifacts.apis.io/prompthalo/vendors/prompthalo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/prompthalo-vendors.yml
- group: auth
  href: https://artifacts.apis.io/prompthalo/security/prompthalo-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/prompthalo-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/prompthalo/security/prompthalo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/prompthalo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.prompthalo.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://www.prompthalo.ai/docs
created: '2026-10-18'
description: PromptHalo provides real-time AI security with prompt-layer defense, sandboxed control, and continuous threat monitoring. It protects AI applications by detecting malicious prompts, securing model outputs, and offering comprehensive threat intelligence for developers and enterprises.
image: https://www.prompthalo.ai/assets/ph-screenshot.png
layout: provider
modified: '2026-10-18'
name: PromptHalo
nav: Providers
network: true
overview: 'PromptHalo is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Security, Real-Time, and Monitoring.


  PromptHalo''s developer surface includes documentation and 9 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 8.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 57.1
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Prompthalo Domain Security
  slug: prompthalo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Prompthalo Vulnerability Disclosure
  slug: prompthalo-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: prompthalo
tags:
- Company
- Artificial Intelligence
- Security
- Real-Time
- Monitoring
website: https://www.prompthalo.ai/
---
