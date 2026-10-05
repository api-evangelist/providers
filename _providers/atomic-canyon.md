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
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/atomic-canyon/refs/heads/main/hosts/atomic-canyon-hosts.yml
  title: ''
  type: Hosts
  url: hosts/atomic-canyon-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/atomic-canyon/refs/heads/main/security/atomic-canyon-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/atomic-canyon-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.atomiccanyon.com
coverage:
  checked: 2026-09-26
  detail: No OpenAPI or other machine-readable contract found after probing known hosts.
  evidence:
  - status: 0
    url: https://api.atomiccanyon.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-26'
description: Atomic Canyon provides a platform focused on data consent and privacy management, enabling users to control data sharing preferences across web services. The site offers tools for consent preferences, basic operations, content personalization, and site optimization, ensuring compliance with privacy regulations and enhancing user trust. Through its services, Atomic Canyon aims to secure data access while delivering personalized experiences.
image: https://atomiccanyon.com/wp-content/uploads/2024/01/facebook.png
layout: provider
modified: '2026-09-26'
name: Atomic Canyon
nav: Providers
network: true
overview: Atomic Canyon is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Privacy, Consent Management, and Platform.
random_paper: 10
score:
  band: minimal
  composite: 2.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 39.3
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Atomic Canyon Domain Security
  slug: atomic-canyon-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: atomic-canyon
tags:
- Company
- Privacy
- Consent Management
- Platform
website: https://www.atomiccanyon.com
---
