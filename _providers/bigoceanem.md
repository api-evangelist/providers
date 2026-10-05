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
  href: https://raw.githubusercontent.com/api-evangelist/bigoceanem/refs/heads/main/hosts/bigoceanem-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bigoceanem-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bigoceanem/refs/heads/main/vendors/bigoceanem-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bigoceanem-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bigoceanem/refs/heads/main/security/bigoceanem-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bigoceanem-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bigocean-official.com
coverage:
  checked: '2026-09-28'
  detail: OpenAPI spec endpoints returned 404, and no documentation host was found.
  evidence:
  - status: 404
    url: https://bigocean-official.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-28'
description: Bigoceanem is a South Korean entertainment and celebrity management company, originally formed from the merger of several media entities. It manages K‑pop artists, produces television content, and operates fan community platforms. The company expanded its portfolio in 2021 by acquiring Big Whale Entertainment and continues to develop multimedia projects across music, video, and digital fan engagement services.
image: https://image.static.bstage.in/cdn-cgi/image/metadata=none/bigocean/95b3c8ed-882f-4bc6-aa29-a01f835f096e/6684c8f1-cac6-42bd-889a-65092c29052b/ori.jpg
layout: provider
modified: '2026-09-28'
name: Bigoceanem
nav: Providers
network: true
overview: Bigoceanem is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Entertainment, K-pop, Media, and South Korea.
random_paper: 0
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
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - south-korea
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
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
  name: Bigoceanem Domain Security
  slug: bigoceanem-domain-security
  summary_line: TLSv1.3
slug: bigoceanem
tags:
- Company
- Entertainment
- K-pop
- Media
- South Korea
website: https://bigocean-official.com
---
