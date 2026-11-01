---
agent_readiness:
  band: agent-aware
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/dudko-dev/hosts/dudko-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dudko-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/dudko-dev/vendors/dudko-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dudko-dev-vendors.yml
- group: auth
  href: https://artifacts.apis.io/dudko-dev/security/dudko-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dudko-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dudko.dev/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dudko-dev
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dudko.dev/privacy_policy.html
coverage:
  checked: '2026-10-29'
  detail: OpenAPI spec endpoint returned HTTP 526, indicating no machine‑readable spec is available.
  evidence:
  - status: 526
    url: https://api.dudko.dev/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: I/E Siarhei Dudko is a software development company offering consulting, architecture, automation, and open‑source libraries. The site showcases an interactive 3D neural map of products and projects spanning AI assistants, fintech, e‑commerce, IoT, and more, highlighting expertise in modern software solutions.
image: https://dudko.dev/og.png
layout: provider
modified: '2026-10-29'
name: dudko-dev
nav: Providers
network: true
overview: dudko-dev is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Software, Consulting, AI, and Open-Source.
random_paper: 11
score:
  band: minimal
  composite: 6.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dudko Dev Domain Security
  slug: dudko-dev-domain-security
  summary_line: TLSv1.3 · DMARC
slug: dudko-dev
tags:
- Company
- Software
- Consulting
- AI
- Open-Source
website: https://dudko.dev/
---
