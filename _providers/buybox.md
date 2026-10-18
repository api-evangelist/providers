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
  href: https://raw.githubusercontent.com/api-evangelist/buybox/refs/heads/main/hosts/buybox-hosts.yml
  title: ''
  type: Hosts
  url: hosts/buybox-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/buybox/refs/heads/main/vendors/buybox-vendors.yml
  title: ''
  type: Vendors
  url: vendors/buybox-vendors.yml
- group: company
  title: ''
  type: Blog
  url: https://www.buybox.net/blog
- group: docs
  title: ''
  type: Documentation
  url: https://help.buybox.net/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/buybox/refs/heads/main/security/buybox-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/buybox-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.buybox.net
coverage:
  checked: '2026-10-06'
  detail: The provider's support site (help.buybox.net) offers only HTML help pages with no OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract.
  evidence:
  - status: 404
    url: https://help.buybox.net/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-06'
description: Buybox provides an omnichannel gift card solution for brands, enabling B2C and B2B gift card programs across Europe and beyond. Their platform offers integrated tools for distribution, analytics, and compliance, supporting multiple languages, currencies, and regulatory environments. The company emphasizes rapid international deployment, ROI guarantees, and deep integrations with major CMS, PSP, and POS systems, positioning itself as a strategic partner for brands seeking efficient customer acquisition through gift cards.
image: https://cdn.prod.website-files.com/64a2887a6c53ed8a34373381/64a7f202b6461b26dd727364_opengraph.png
layout: provider
modified: '2026-10-06'
name: Buybox
nav: Providers
network: true
overview: 'Buybox is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Gift Cards, B2B, Consumer, and Europe.


  Buybox''s developer surface includes engineering blog, documentation, and 4 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 5.1
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
    developer_ergonomics: 11.9
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 5.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Buybox Domain Security
  slug: buybox-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: buybox
tags:
- Company
- Gift Cards
- B2B
- Consumer
- Europe
website: https://www.buybox.net
---
