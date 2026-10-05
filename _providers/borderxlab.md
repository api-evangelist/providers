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
- description: API for Borderxlab platform (no public machine‑readable spec discovered).
  name: Borderxlab API
  slug: borderxlab-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/borderxlab/refs/heads/main/llms/borderxlab-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/borderxlab-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/borderxlab/refs/heads/main/hosts/borderxlab-hosts.yml
  title: ''
  type: Hosts
  url: hosts/borderxlab-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/borderxlab/refs/heads/main/vendors/borderxlab-vendors.yml
  title: ''
  type: Vendors
  url: vendors/borderxlab-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.borderxlab.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://www.borderxlab.com/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/borderxlab/refs/heads/main/security/borderxlab-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/borderxlab-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.borderxlab.com
coverage:
  checked: '2026-10-02'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract found at api.borderxlab.com despite probing common spec endpoints.
  evidence:
  - status: 0
    url: https://api.borderxlab.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-02'
description: Borderxlab is a Silicon Valley‑based AI‑driven cross‑border e‑commerce platform. Founded in 2014 by three former Google PhDs, it offers products such as CloudStore AI, BeyondStyle, and BieYang app to enable brands and merchants to sell globally. The company reports over 5 million successful orders, 20 million SKUs and $1 billion GMV, positioning itself as a leader in agentic commerce.
layout: provider
modified: '2026-10-02'
name: Borderxlab
nav: Providers
network: true
overview: 'Borderxlab publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, E-Commerce, Cross-Border, and Agentic Commerce.


  Borderxlab''s developer surface includes engineering blog and 6 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 7.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 60.7
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Borderxlab Domain Security
  slug: borderxlab-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: borderxlab
tags:
- Company
- Artificial Intelligence
- E-Commerce
- Cross-Border
- Agentic Commerce
website: https://www.borderxlab.com
---
