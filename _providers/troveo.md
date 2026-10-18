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
  href: https://raw.githubusercontent.com/api-evangelist/troveo/refs/heads/main/hosts/troveo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/troveo-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/troveo/refs/heads/main/vendors/troveo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/troveo-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.troveo.ai:443/legal/privacy-policy
- group: start
  title: ''
  type: GettingStarted
  url: https://support.troveo.com/collections/3651166952-getting_started
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/troveo/refs/heads/main/security/troveo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/troveo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://troveo.ai
- group: docs
  title: ''
  type: Documentation
  url: https://support.troveo.com
- group: operate
  title: ''
  type: Support
  url: https://support.troveo.com
coverage:
  checked: '2026-10-12'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL files were found at the API hosts despite probing known endpoints.
  evidence:
  - status: 0
    url: https://api.troveo.com/openapi.json
  - status: 0
    url: https://api.troveo.ai/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-12'
description: Troveo provides a platform that unlocks non‑public, real‑world data for frontier AI applications. By aggregating multimodal business data—including company information, videos, audio, gaming content, and more—Troveo enables data owners to license their datasets and generate recurring revenue. The service offers tools for data assessment, sourcing, and monetization, catering to enterprises seeking to enrich AI models with high‑quality, verified data across 30+ systems of record.
image: https://www.troveo.ai/opengraph-image
layout: provider
modified: '2026-10-12'
name: Troveo
nav: Providers
network: true
overview: 'Troveo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Data, Artificial Intelligence, Marketplace, Licensing, and Real-World Data.


  Troveo''s developer surface includes getting-started guide, documentation, support, and 5 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 11.3
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
    developer_ergonomics: 26.2
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Troveo Domain Security
  slug: troveo-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: troveo
tags:
- Data
- Artificial Intelligence
- Marketplace
- Licensing
- Real-World Data
website: https://troveo.ai
---
