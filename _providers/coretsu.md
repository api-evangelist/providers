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
  href: https://raw.githubusercontent.com/api-evangelist/coretsu/refs/heads/main/hosts/coretsu-hosts.yml
  title: ''
  type: Hosts
  url: hosts/coretsu-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/coretsu/refs/heads/main/vendors/coretsu-vendors.yml
  title: ''
  type: Vendors
  url: vendors/coretsu-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/coretsu/refs/heads/main/security/coretsu-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coretsu-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.coretsu.com/
coverage:
  checked: '2026-10-11'
  detail: Coretsu provides no public developer program or API documentation.
  evidence:
  - status: 200
    url: https://www.coretsu.com/
  reason: no-developer-program
  state: none
created: '2026-10-11'
description: Coretsu is an AI‑focused technology company that presents itself as a platform for leveraging artificial intelligence to expand human creativity and productivity. The site emphasizes a vision of empowering individuals and organizations with AI tools while acknowledging the responsibility that comes with such power. It highlights a commitment to innovation, a range of engineering roles, and a mission to keep humanity relevant in an AI‑driven future.
image: https://www.coretsu.com/og-image.png
layout: provider
modified: '2026-10-11'
name: Coretsu
nav: Providers
network: true
overview: Coretsu is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Technology, Platform, and Innovation.
random_paper: 3
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
    score: 5.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Coretsu Domain Security
  slug: coretsu-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: coretsu
tags:
- Company
- Artificial Intelligence
- Technology
- Platform
- Innovation
website: https://www.coretsu.com/
---
