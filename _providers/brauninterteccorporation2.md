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
api_count: 1
apis:
- description: Engineering and environmental consulting services API (documentation site)
  name: Braun Intertec API
  slug: braun-intertec-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/brauninterteccorporation2/refs/heads/main/hosts/brauninterteccorporation2-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brauninterteccorporation2-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/brauninterteccorporation2/refs/heads/main/vendors/brauninterteccorporation2-vendors.yml
  title: ''
  type: Vendors
  url: vendors/brauninterteccorporation2-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/brauninterteccorporation2/refs/heads/main/security/brauninterteccorporation2-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brauninterteccorporation2-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.braunintertec.com
coverage:
  checked: '2026-10-03'
  detail: The provider's website offers only HTML documentation with no OpenAPI, GraphQL, or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://www.braunintertec.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-03'
description: 'Brauninterteccorporation2 is a company surfaced via the API Evangelist harvest backlog (source: secondary-market) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-10-03'
name: Brauninterteccorporation2
nav: Providers
network: true
overview: Brauninterteccorporation2 publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 8
score:
  band: minimal
  composite: 2.1
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
  name: Brauninterteccorporation2 Domain Security
  slug: brauninterteccorporation2-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: brauninterteccorporation2
tags:
- Company
website: https://www.braunintertec.com
---
