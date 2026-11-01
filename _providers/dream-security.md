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
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/dream-security/well-known/dream-security-clarity-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dream-security-clarity-security.txt
- group: agent
  href: https://artifacts.apis.io/dream-security/well-known/dream-security-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dream-security-well-known.yml
- group: auth
  title: ''
  type: Security
  url: https://clarity.com/vdp
- group: other
  href: https://artifacts.apis.io/dream-security/hosts/dream-security-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dream-security-hosts.yml
- group: other
  href: https://artifacts.apis.io/dream-security/vendors/dream-security-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dream-security-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dreamgroup.com/privacy-notice
- group: company
  title: ''
  type: Blog
  url: https://dreamgroup.com/blog/hey-claude-security-is-not-just-code
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dreamgroup.com/
- group: auth
  href: https://artifacts.apis.io/dream-security/security/dream-security-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/dream-security-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/dream-security/security/dream-security-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dream-security-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dreamgroup.com
coverage:
  checked: '2026-10-24'
  detail: Documentation pages require login, preventing access to API specifications.
  evidence:
  - status: 200
    url: https://docs.dreamgroup.com/
  reason: sales-gate
  state: gated
created: '2026-10-24'
description: Dream provides a sovereign AI and national cyber‑defense platform designed for governments and nation‑states. Its solutions, including the Atlas AI platform, Sphere threat‑defense suite, and Hero vulnerability‑remediation tool, are deployed on‑premises and air‑gapped to keep data within national borders. The offerings aim to secure critical infrastructure, transform fragmented government data into actionable knowledge, and support national resilience and decision‑making.
image: https://cdn.prod.website-files.com/6a1324866930e66fe78a27d6/6a324f843f505cd83850fcc0_og.jpg
layout: provider
modified: '2026-10-24'
name: Dream Security
nav: Providers
network: true
overview: 'Dream Security is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Cybersecurity, Government, National Defense, and Sovereign AI.


  Dream Security''s developer surface includes engineering blog, documentation, and 9 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 10.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 48.2
    operational_transparency: 10.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 14.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dream Security Domain Security
  slug: dream-security-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Dream Security Vulnerability Disclosure
  slug: dream-security-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: dream-security
tags:
- AI
- Cybersecurity
- Government
- National Defense
- Sovereign AI
- Critical Infrastructure
website: https://dreamgroup.com
---
