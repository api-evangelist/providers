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
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/danads/refs/heads/main/llms/danads-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/danads-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/danads/refs/heads/main/well-known/danads-requests-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/danads-requests-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/danads/refs/heads/main/well-known/danads-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/danads-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/danads/refs/heads/main/hosts/danads-hosts.yml
  title: ''
  type: Hosts
  url: hosts/danads-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://danads.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://danads.com/privacy-policy/
- group: company
  title: ''
  type: Blog
  url: https://danads.com/blog/decade-of-danads/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/danads/refs/heads/main/security/danads-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/danads-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://danads.com/
coverage:
  checked: '2026-10-15'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found despite probing known hosts.
  evidence:
  - status: 404
    url: https://api.danads.com/openapi.json
  - status: 404
    url: https://api.danads.com/graphql
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-15'
description: DanAds is a global advertising technology company offering a self‑serve ad platform that streamlines ad sales, operations and creative management. It enables advertisers and publishers to automate workflows, maximize revenue, and expand globally through a unified solution. The platform provides tools for campaign creation, inventory management, reporting, and integration with major ad exchanges.
image: https://static.danads.com/wp-content/uploads/2025/10/08143216/Screenshot-2025-10-08-at-17.29.25-1.webp
layout: provider
modified: '2026-10-15'
name: DanAds
nav: Providers
network: true
overview: 'DanAds is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include AdTech, Publisher Tools, Advertiser Tools, Ad Operations, and Self‑Serve Advertising.


  DanAds'' developer surface includes engineering blog and 8 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 10.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 55.4
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Danads Domain Security
  slug: danads-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: danads
tags:
- AdTech
- Publisher Tools
- Advertiser Tools
- Ad Operations
- Self‑Serve Advertising
website: https://danads.com/
---
