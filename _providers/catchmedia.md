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
  href: https://raw.githubusercontent.com/api-evangelist/catchmedia/refs/heads/main/hosts/catchmedia-hosts.yml
  title: ''
  type: Hosts
  url: hosts/catchmedia-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/catchmedia/refs/heads/main/security/catchmedia-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/catchmedia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.catchmedia.com
coverage:
  checked: '2026-10-07'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract files were found at the API host or docs host.
  evidence:
  - status: 0
    url: https://api.catchmedia.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-07'
description: Catchmedia provides an analytics and customer engagement platform designed for the digital content industry. It offers data collection, orchestration, audience segmentation, personalized content recommendations, and a clearinghouse for revenue distribution. The solution integrates a 360-degree view of customers across acquisition, engagement, and retention, delivering actionable insights to media companies, OTT services, and publishers.
layout: provider
modified: '2026-10-07'
name: Catchmedia
nav: Providers
network: true
overview: Catchmedia is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Analytics, Media, CustomerEngagement, and Data Platform.
random_paper: 15
score:
  band: minimal
  composite: 3.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
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
  name: Catchmedia Domain Security
  slug: catchmedia-domain-security
  summary_line: TLSv1.3 · HSTS
slug: catchmedia
tags:
- Company
- Analytics
- Media
- CustomerEngagement
- Data Platform
website: https://www.catchmedia.com
---
