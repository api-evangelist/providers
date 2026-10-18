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
artifact_total: 3
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/geant/refs/heads/main/llms/geant-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/geant-llms.txt
- group: auth
  title: ''
  type: Compliance
  url: https://security.geant.org/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/geant/refs/heads/main/security/geant-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/geant-vulnerability-disclosure.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/geant/refs/heads/main/hosts/geant-hosts.yml
  title: ''
  type: Hosts
  url: hosts/geant-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/geant/refs/heads/main/vendors/geant-vendors.yml
  title: ''
  type: Vendors
  url: vendors/geant-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/geant/refs/heads/main/packages/geant-packages.yml
  title: ''
  type: SDKs
  url: packages/geant-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/geant/refs/heads/main/packages/geant-packages.yml
  title: ''
  type: Packages
  url: packages/geant-packages.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GEANT
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/geant/refs/heads/main/security/geant-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/geant-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/geant/refs/heads/main/security/geant-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/geant-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/geant/refs/heads/main/security/geant-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/geant-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://geant.org/
created: '2026-10-13'
description: 'GEANT is a company surfaced via the API Evangelist harvest backlog (source: tag-qc) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-10-13'
name: GEANT
nav: Providers
network: true
overview: GEANT is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 21
score:
  band: minimal
  composite: 10.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 15.0
    catalog_earned_first_party: 0.0
    catalog_gap: 100.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 33.9
    operational_transparency: 15.8
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Geant Domain Security
  slug: geant-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Geant Vulnerability Disclosure
  slug: geant-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Geant Trust Center
  slug: geant-trust-center
  summary_line: ISO 27001, GDPR
slug: geant
tags:
- Company
website: https://geant.org/
---
