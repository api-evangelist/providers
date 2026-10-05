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
  href: https://raw.githubusercontent.com/api-evangelist/bite-squad/refs/heads/main/hosts/bite-squad-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bite-squad-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bite-squad/refs/heads/main/security/bite-squad-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bite-squad-domain-security.yml
coverage:
  checked: '2026-09-28'
  detail: Attempts to fetch OpenAPI files returned HTML redirects to the landing page.
  evidence:
  - status: 200
    url: https://bite-squad.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-28'
description: Bite Squad is a startup that provides a platform for ordering and delivering meals from local restaurants. The company aims to simplify the food ordering experience through an API that enables developers to integrate menu browsing, order placement, and delivery tracking into their applications. While detailed public information is limited, Bite Squad positions itself as a modern solution for on‑demand food services, targeting both consumers and partner restaurants seeking streamlined digital ordering capabilities.
image: https://ruffcreekmarkets.com/img/slot.webp
layout: provider
modified: '2026-09-28'
name: Bite Squad
nav: Providers
network: true
overview: Bite Squad is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Food, Delivery, Startups, and Restaurant.
random_paper: 17
score:
  band: minimal
  composite: 3.4
  coverage:
    artifact_dirs: 4
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
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  provenance:
    mcp: unknown
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
  name: Bite Squad Domain Security
  slug: bite-squad-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bite-squad
tags:
- Company
- Food
- Delivery
- Startups
- Restaurant
---
