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
  href: https://raw.githubusercontent.com/api-evangelist/codebase/refs/heads/main/hosts/codebase-hosts.yml
  title: ''
  type: Hosts
  url: hosts/codebase-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/codebase/refs/heads/main/vendors/codebase-vendors.yml
  title: ''
  type: Vendors
  url: vendors/codebase-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.codebase.com/privacy-policy/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/codebase/refs/heads/main/security/codebase-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/codebase-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.codebase.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.codebase.com
  - status: 403
    url: https://equityzen.com/company/codebase
  reason: no-developer-program
  state: none
created: '2026-10-09'
description: Codebase is a global technology services company that provides dedicated software development teams to help businesses build, scale, and maintain high-quality digital products. They specialize in offering offshore talent, agile development processes, and end‑to‑end project management, enabling clients to accelerate product delivery while reducing costs. Codebase serves a wide range of industries, delivering custom web, mobile, and cloud solutions, and emphasizes transparent collaboration, robust security, and long‑term partnership with its customers.
image: https://www.codebase.com/wp-content/uploads/2024/12/codebase-preview.jpg
layout: provider
modified: '2026-10-09'
name: Codebase
nav: Providers
network: true
overview: Codebase is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Software Development, Offshore Teams, Agile, and Digital Products.
random_paper: 8
score:
  band: minimal
  composite: 6.1
  coverage:
    artifact_dirs: 6
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
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Codebase Domain Security
  slug: codebase-domain-security
  summary_line: TLSv1.3 · DMARC
slug: codebase
tags:
- Company
- Software Development
- Offshore Teams
- Agile
- Digital Products
website: https://www.codebase.com
---
