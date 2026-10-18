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
api_count: 1
apis:
- description: API for developers and homebuilders to integrate with Cecian's Residential OS platform.
  name: Residential OS API
  slug: residential-os-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cecilian-partners/refs/heads/main/hosts/cecilian-partners-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cecilian-partners-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cecilian-partners/refs/heads/main/vendors/cecilian-partners-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cecilian-partners-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cecilianpartners.com/legals/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cecilianpartners.com/legals/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.cecilianpartners.com/press
- group: other
  title: ''
  type: Leadership
  url: https://www.cecilianpartners.com/team-member-filters/leadership
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.cecilianpartners.com/customer/developers
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cecilian-partners/refs/heads/main/security/cecilian-partners-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cecilian-partners-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cecilianpartners.com/
coverage:
  checked: '2026-10-07'
  detail: Developer portal provides only HTML pages with no machine‑readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://www.cecilianpartners.com/customer/developers
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-07'
description: Cecilian Partners is a PropTech company delivering the Residential OS® platform for homebuilders and developers. Their solution provides interactive 3D maps, resident engagement tools, inventory insights, and workflow management, serving over 200 clients nationwide. The platform is SOC 2 compliant, ranked in Inc. 5000, and recognized by industry awards for innovation and workplace excellence.
image: https://cdn.prod.website-files.com/6604e9aa5ea2c90f987ad109/66263e94dea67e4b629b6a2b_Open%20graph.jpeg
layout: provider
modified: '2026-10-07'
name: Cecilian Partners
nav: Providers
network: true
overview: Cecilian Partners is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include PropTech, Home Builders, Developers, ERP, and Interactive Maps.
random_paper: 10
score:
  band: emerging
  composite: 12.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 60.7
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
  name: Cecilian Partners Domain Security
  slug: cecilian-partners-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cecilian-partners
tags:
- PropTech
- Home Builders
- Developers
- ERP
- Interactive Maps
- CRM
- Community Management
- Real Estate Development
website: https://www.cecilianpartners.com/
---
