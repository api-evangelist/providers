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
- description: Colektia provides AI-powered digital debt collection infrastructure across Latin America and Spain.
  name: Colektia API
  slug: colektia-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/colektia/refs/heads/main/hosts/colektia-hosts.yml
  title: ''
  type: Hosts
  url: hosts/colektia-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/colektia/refs/heads/main/vendors/colektia-vendors.yml
  title: ''
  type: Vendors
  url: vendors/colektia-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://colektia.com/en/terms-and-conditions
- group: operate
  title: ''
  type: StatusPage
  url: https://status.colektia.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://colektia.com/en/privacy-notice
- group: company
  title: ''
  type: Newsroom
  url: https://colektia.com/en/blog-categories/news
- group: company
  title: ''
  type: Blog
  url: https://colektia.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/colektia
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/colektia/refs/heads/main/security/colektia-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/colektia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://colektia.com
coverage:
  checked: '2026-10-09'
  detail: API spec endpoints on https://api.colektia.com return 403, preventing access to OpenAPI definitions.
  evidence:
  - status: 403
    url: https://api.colektia.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-09'
description: Colektia provides AI-powered digital debt collection infrastructure across Latin America and Spain, offering predictive scoring, automated omnichannel communication, and integration with banking, fintech, telecom, and retail systems to increase recovery rates while reducing operational costs.
image: https://cdn.prod.website-files.com/5e67f74a495c76eb16065e0a/6ac40ffb1dafad9a561cd5d5_OG.webp
layout: provider
modified: '2026-10-09'
name: Colektia
nav: Providers
network: true
overview: 'Colektia is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Debt-Collection, Fintech, and Latin-America.


  Colektia''s developer surface includes engineering blog and 9 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 13.0
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
    developer_ergonomics: 2.4
    discoverability: 58.9
    operational_transparency: 21.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Colektia Domain Security
  slug: colektia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: colektia
tags:
- Company
- Artificial Intelligence
- Debt-Collection
- Fintech
- Latin-America
website: https://colektia.com
---
