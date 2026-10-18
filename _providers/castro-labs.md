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
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/castro-labs/refs/heads/main/hosts/castro-labs-hosts.yml
  title: ''
  type: Hosts
  url: hosts/castro-labs-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/castro-labs/refs/heads/main/vendors/castro-labs-vendors.yml
  title: ''
  type: Vendors
  url: vendors/castro-labs-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/castro-labs/refs/heads/main/security/castro-labs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/castro-labs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.castrolabs.co/
coverage:
  checked: '2026-10-12'
  detail: No public developer documentation or API endpoints were discovered for Castro Labs.
  evidence:
  - status: 200
    url: https://www.castrolabs.co/
  reason: no-developer-program
  state: none
created: '2026-10-12'
description: Castro Labs builds modern social products for people to feel seen, valued, and connected. Based in San Francisco, the team creates inclusive platforms for the gay community, focusing on love-driven software from the historic Castro neighborhood. Their mission is to foster happier, more connected spaces through innovative technology and community-focused design.
image: https://cdn.prod.website-files.com/611d365d081adc686a569372/611fda6570c1fb1b6265966f_CastroLabs.png
layout: provider
modified: '2026-10-12'
name: Castro Labs
nav: Providers
network: true
overview: Castro Labs is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Social, Community, Software-as-a-Service, LGBTQ+, and San Francisco.
random_paper: 15
score:
  band: minimal
  composite: 3.4
  coverage:
    artifact_dirs: 6
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
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Castro Labs Domain Security
  slug: castro-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: castro-labs
tags:
- Social
- Community
- Software-as-a-Service
- LGBTQ+
- San Francisco
website: https://www.castrolabs.co/
---
