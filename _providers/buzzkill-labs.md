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
  href: https://raw.githubusercontent.com/api-evangelist/buzzkill-labs/refs/heads/main/hosts/buzzkill-labs-hosts.yml
  title: ''
  type: Hosts
  url: hosts/buzzkill-labs-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/buzzkill-labs/refs/heads/main/vendors/buzzkill-labs-vendors.yml
  title: ''
  type: Vendors
  url: vendors/buzzkill-labs-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/buzzkill-labs/refs/heads/main/security/buzzkill-labs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/buzzkill-labs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nasdaqprivatemarket.com/
coverage:
  checked: '2026-10-06'
  detail: No developer program or API documentation was found for Buzzkill Labs.
  evidence:
  - status: null
    url: https://www.buzzkill-labs.com
  reason: no-developer-program
  state: none
created: '2026-10-06'
description: Buzzkill Labs is a technology startup focused on developing innovative solutions for digital content moderation and user engagement analytics. The company aims to provide APIs that enable developers to integrate sentiment analysis, toxicity detection, and real-time moderation tools into their applications, helping platforms maintain healthy online communities. While the company is currently in early stages, it plans to release a suite of RESTful services and SDKs across multiple programming languages.
layout: provider
modified: '2026-10-06'
name: Buzzkill Labs
nav: Providers
network: true
overview: Buzzkill Labs is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Moderation, Sentiment, and Analytics.
random_paper: 8
score:
  band: minimal
  composite: 2.2
  coverage:
    artifact_dirs: 4
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 35.7
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: venue_as_website
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
  name: Buzzkill Labs Domain Security
  slug: buzzkill-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: buzzkill-labs
tags:
- Company
- Moderation
- Sentiment
- Analytics
website: https://www.nasdaqprivatemarket.com/
---
