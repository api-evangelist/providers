---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 11.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Instapaper API v2 provides endpoints to manage bookmarks, folders, tags, highlights, and account information.
  name: Instapaper API
  slug: instapaper-api
artifact_total: 4
common:
- group: agent
  href: https://artifacts.apis.io/instapaper/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/instapaper/authentication/instapaper-authentication.yml
  title: ''
  type: Authentication
  url: authentication/instapaper-authentication.yml
- group: design
  href: https://artifacts.apis.io/instapaper/errors/instapaper-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/instapaper-problem-types.yml
- group: other
  href: https://artifacts.apis.io/instapaper/hosts/instapaper-hosts.yml
  title: ''
  type: Hosts
  url: hosts/instapaper-hosts.yml
- group: other
  href: https://artifacts.apis.io/instapaper/vendors/instapaper-vendors.yml
  title: ''
  type: Vendors
  url: vendors/instapaper-vendors.yml
- group: build
  href: https://artifacts.apis.io/instapaper/packages/instapaper-packages.yml
  title: ''
  type: SDKs
  url: packages/instapaper-packages.yml
- group: build
  href: https://artifacts.apis.io/instapaper/packages/instapaper-packages.yml
  title: ''
  type: Packages
  url: packages/instapaper-packages.yml
- group: auth
  href: https://artifacts.apis.io/instapaper/security/instapaper-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/instapaper-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://instapaper.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.instapaper.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://www.instapaper.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.instapaper.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://www.instapaper.com/getting-started
- group: operate
  title: ''
  type: Support
  url: https://www.instapaper.com/docs
- group: company
  title: ''
  type: Blog
  url: https://www.instapaper.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.instapaper.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.instapaper.com/about-legal/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.instapaper.com/about-legal/legal/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/instapaper
coverage:
  checked: '2026-10-28'
  detail: Developers page documents API v2 endpoints but no OpenAPI/Swagger spec is published.
  evidence:
  - status: 200
    url: https://instapaper.com/developers
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Instapaper is a read‑it‑later service that lets users save web articles to read later across devices such as iOS, Android, desktop browsers, and e‑readers. Founded in 2008, it offers a clean, distraction‑free reading experience, supports offline access, highlights, notes, and integrates with services like Pocket, Flipboard, and Twitter. The service provides a simple HTTP API for developers to add, retrieve, and manage saved items, documented at https://www.instapaper.com/api/1.
image: https://www.instapaper.com/static/img/instapaper-logo.png
layout: provider
modified: '2026-10-28'
name: Instapaper
nav: Providers
network: true
overview: 'Instapaper is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, read-it-later, productivity, web-service, and bookmarking.


  Instapaper''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 12 more developer resources.'
random_paper: 23
scopes:
- name: Instapaper Scopes
  scope_count: 0
  slug: instapaper-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 29.9
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 70.7
    discoverability: 66.1
    operational_transparency: 5.3
  provenance:
    conformance: unknown
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Instapaper Authentication
  slug: instapaper-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Instapaper Domain Security
  slug: instapaper-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: instapaper
tags:
- Company
- read-it-later
- productivity
- web-service
- bookmarking
- API
website: https://instapaper.com/
---
