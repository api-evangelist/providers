---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.6
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: The SmugMug REST API provides programmatic access to user accounts, galleries, images, and related resources.
  name: SmugMug API
  slug: smugmug-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/smugmug/plans/smugmug-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/smugmug-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/smugmug/authentication/smugmug-authentication.yml
  title: ''
  type: Authentication
  url: authentication/smugmug-authentication.yml
- group: other
  href: https://artifacts.apis.io/smugmug/hosts/smugmug-hosts.yml
  title: ''
  type: Hosts
  url: hosts/smugmug-hosts.yml
- group: other
  href: https://artifacts.apis.io/smugmug/vendors/smugmug-vendors.yml
  title: ''
  type: Vendors
  url: vendors/smugmug-vendors.yml
- group: build
  href: https://artifacts.apis.io/smugmug/packages/smugmug-packages.yml
  title: ''
  type: SDKs
  url: packages/smugmug-packages.yml
- group: build
  href: https://artifacts.apis.io/smugmug/packages/smugmug-packages.yml
  title: ''
  type: Packages
  url: packages/smugmug-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.smugmug.com/about/terms
- group: operate
  title: ''
  type: Support
  url: https://help.smugmug.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.smugmug.com/about/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.smugmug.com/plans
- group: start
  title: ''
  type: Login
  url: https://www.smugmug.com/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.smugmug.com/
- group: company
  title: ''
  type: Blog
  url: https://www.smugmug.com/blog
- group: docs
  title: ''
  type: APIReference
  url: https://api.smugmug.com/api/v2/doc/reference/user.html
- group: docs
  title: ''
  type: Documentation
  url: https://dev.smugmug.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/smugmug
- group: auth
  href: https://artifacts.apis.io/smugmug/security/smugmug-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/smugmug-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://smugmug.com/
coverage:
  checked: '2026-10-28'
  detail: Developer documentation pages are rendered via JavaScript, preventing automated retrieval of machine‑readable specs.
  evidence:
  - status: 200
    url: https://api.smugmug.com/api/v2/doc/reference/user.html
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: SmugMug is an online photo sharing, storage, and e‑commerce platform that provides photographers, enthusiasts, and businesses with tools to upload, organize, showcase, and sell images. The service offers customizable galleries, robust privacy controls, integration with third‑party apps, and a marketplace for prints and digital downloads, catering to both personal and professional users.
image: https://cdn.prod.website-files.com/68c846bddb83be493e6f813e/6a4c238191ede1c82169624b_OG-HOME.jpg
layout: provider
modified: '2026-10-28'
name: SmugMug
nav: Providers
network: true
overview: 'SmugMug is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Photography, PhotoSharing, ECommerce, CloudStorage, and SaaS.


  SmugMug''s developer surface includes authentication, support, pricing, engineering blog, API reference, documentation, and 12 more developer resources.'
plans:
- name: Smugmug Plans Pricing
  plan_count: 3
  slug: smugmug-plans-pricing
random_paper: 5
score:
  band: thin
  composite: 33.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 52.4
    discoverability: 66.1
    operational_transparency: 5.3
  provenance:
    conformance: unknown
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Smugmug Authentication
  slug: smugmug-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Smugmug Domain Security
  slug: smugmug-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: smugmug
tags:
- Photography
- PhotoSharing
- ECommerce
- CloudStorage
- SaaS
website: https://smugmug.com/
---
