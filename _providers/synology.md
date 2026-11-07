---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.6
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/synology/well-known/synology-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/synology-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.synology.com/security/bounty_program
- group: auth
  href: https://artifacts.apis.io/synology/well-known/synology-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/synology-www-security.txt
- group: agent
  href: https://artifacts.apis.io/synology/well-known/synology-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/synology-well-known.yml
- group: other
  href: https://artifacts.apis.io/synology/hosts/synology-hosts.yml
  title: ''
  type: Hosts
  url: hosts/synology-hosts.yml
- group: other
  href: https://artifacts.apis.io/synology/vendors/synology-vendors.yml
  title: ''
  type: Vendors
  url: vendors/synology-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://c2.synology.com/legal/terms_conditions
- group: company
  title: ''
  type: Blog
  url: https://blog.synology.com/
- group: auth
  href: https://artifacts.apis.io/synology/security/synology-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/synology-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/synology/security/synology-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/synology-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://synology.com/
coverage:
  checked: '2026-10-28'
  detail: Synology provides no public developer program or API documentation.
  evidence:
  - status: 200
    url: https://www.synology.com/
  reason: no-developer-program
  state: none
created: '2026-10-28'
description: Synology C2 provides cloud backup and storage solutions for businesses and consumers, offering secure data protection, scalable storage, and integrated services such as ActiveProtect appliances and AI‑powered surveillance. The company emphasizes reliability, performance, and enterprise‑grade features across its DSM operating system and hardware lineup.
image: https://fileres.synology.com/images/common/meta-tag-preview-image/img_synology.jpg
layout: provider
modified: '2026-10-28'
name: Synology C2
nav: Providers
network: true
overview: 'Synology C2 is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cloud, Backup, Storage, and Enterprise.


  Synology C2''s developer surface includes engineering blog and 10 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 7.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.2
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 48.2
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 9.7
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/synology/synology-2026-11-03T144248.png
security:
- kind: domain-security
  name: Synology Domain Security
  slug: synology-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Synology Vulnerability Disclosure
  slug: synology-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: synology
tags:
- Company
- Cloud
- Backup
- Storage
- Enterprise
website: https://synology.com/
---
