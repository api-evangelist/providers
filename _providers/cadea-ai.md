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
  href: https://raw.githubusercontent.com/api-evangelist/cadea-ai/refs/heads/main/hosts/cadea-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cadea-ai-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cadea-ai/refs/heads/main/vendors/cadea-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cadea-ai-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cadea-ai/refs/heads/main/security/cadea-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cadea-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://forgeglobal.com/cadea-ai_stock/
created: '2026-10-06'
description: Cadea AI is a company identified in the API Evangelist harvest backlog as a stub for full-pipeline profiling. It appears to be associated with financial data services, as indicated by its listing on Forge Global. However, no dedicated corporate website could be located, and attempts to resolve a primary domain (cadea.ai) resulted in a 503 error. The available information suggests the company may operate primarily through market listings rather than a public-facing web presence.
layout: provider
modified: '2026-10-06'
name: Cadea AI
nav: Providers
network: true
overview: Cadea AI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Data, Artificial Intelligence, and Marketplace.
random_paper: 15
score:
  band: minimal
  composite: 3.0
  coverage:
    artifact_dirs: 3
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
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: venue_as_website
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
  name: Cadea Ai Domain Security
  slug: cadea-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cadea-ai
tags:
- Company
- Finance
- Data
- Artificial Intelligence
- Marketplace
website: https://forgeglobal.com/cadea-ai_stock/
---
