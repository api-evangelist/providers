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
  href: https://raw.githubusercontent.com/api-evangelist/augmodo/refs/heads/main/hosts/augmodo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/augmodo-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/augmodo/refs/heads/main/vendors/augmodo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/augmodo-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.augmodo.com/terms-of-use
- group: company
  title: ''
  type: Newsroom
  url: https://www.augmodo.com/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/augmodo/refs/heads/main/security/augmodo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/augmodo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.augmodo.com/
coverage:
  checked: 2026-09-26
  detail: No public API documentation or OpenAPI spec was found on the company's website or API subdomain.
  evidence:
  - status: dns_error
    url: https://api.augmodo.com
  - status: 200
    url: https://www.augmodo.com
  reason: no-developer-program
  state: none
created: '2026-09-26'
description: Augmodo provides Spatial AI solutions to augment retail workforces, enabling real‑time inventory tracking across stores. Their platform offers a visual dashboard that helps retailers stay stocked, leveraging computer‑vision and AI to monitor product placement and availability instantly. Clients include major brands such as Amazon, Grammarly, Wyze, Oculus, and others, showcasing broad applicability across e‑commerce and physical retail environments.
layout: provider
modified: '2026-09-26'
name: Augmodo
nav: Providers
network: true
overview: Augmodo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Retail, Spatial AI, Smartbadge, Supply Chain, and Compliance.
random_paper: 0
score:
  band: minimal
  composite: 5.9
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.4
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Augmodo Domain Security
  slug: augmodo-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: augmodo
tags:
- Retail
- Spatial AI
- Smartbadge
- Supply Chain
- Compliance
website: https://www.augmodo.com/
---
