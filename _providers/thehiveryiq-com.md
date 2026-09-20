---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 9.2
  scored_at: '2026-09-19'
api_count: 0
artifact_total: 3
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/thehiveryiq-com/refs/heads/main/security/thehiveryiq-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/thehiveryiq-com-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/thehiveryiq-com/refs/heads/main/security/thehiveryiq-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/thehiveryiq-com-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/thehiveryiq-com/refs/heads/main/security/thehiveryiq-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/thehiveryiq-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://thehiveryiq.com/
created: '2026-09-19'
description: 'Hive Civilization is a company surfaced via the API Evangelist harvest backlog (source: a2a-registry) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-09-19'
name: Hive Civilization
nav: Providers
network: true
overview: Hive Civilization is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 4
score:
  band: minimal
  composite: 6.5
  coverage:
    artifact_dirs: 21
    catalog_earned: 15.0
    catalog_earned_first_party: 0.0
    catalog_gap: 100.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 7.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 27.8
    operational_transparency: 0.0
  schema_version: 0.22.0
  scored_at: '2026-09-19'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Thehiveryiq Com Domain Security
  slug: thehiveryiq-com-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Thehiveryiq Com Vulnerability Disclosure
  slug: thehiveryiq-com-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Thehiveryiq Com Trust Center
  slug: thehiveryiq-com-trust-center
  summary_line: SOC 2, ISO 27001, FedRAMP, GDPR
slug: thehiveryiq-com
tags:
- Company
website: https://thehiveryiq.com/
---
