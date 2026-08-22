---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 19.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: Free keyless RESTful JSON API serving random anime/neko images across many categories with rich metadata, a tags endpoint, session mechanism, and content ratings.
  name: Nekosia REST API
  slug: nekosia-rest-api
artifact_total: 13
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/nekosia-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nekosia-domain-security.yml
- group: auth
  title: ''
  type: Security
  url: security/nekosia-vulnerability-disclosure.yml
- group: company
  title: ''
  type: Website
  url: https://nekosia.cat/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://nekosia.cat/documentation
- group: docs
  title: ''
  type: Documentation
  url: https://nekosia.cat/documentation?page=introduction
- group: docs
  title: ''
  type: APIReference
  url: https://nekosia.cat/documentation?page=endpoints
- group: start
  title: ''
  type: GettingStarted
  url: https://nekosia.cat/documentation?page=getting-started
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/pba76vJhcP
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Nekosia-API
- group: start
  title: ''
  type: Login
  url: https://nekosia.cat/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nekosia.cat/documentation?page=tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nekosia.cat/documentation?page=privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.nekosia.cat
- group: operate
  title: ''
  type: ChangeLog
  url: https://nekosia.cat/documentation?page=changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/nekosia-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nekosia-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nekosia-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nekosia-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nekosia-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/nekosia-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/nekosia-data-model.yml
- group: build
  title: ''
  type: Examples
  url: examples/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/nekosia-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/nekosia-packages.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nekosia-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/nekosia-plans-pricing.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/nekosia-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/nekosia-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nekosia-llms.txt
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/Nekosia-API/documentation
- group: docs
  title: ''
  type: X-Documentation-Source
  url: https://raw.githubusercontent.com/Nekosia-API/documentation/main/endpoints.md
created: '2026-08-19'
description: Nekosia is a free, keyless anime-image REST API serving cute anime "neko" (catgirl) imagery and related metadata, backed by the provider's own Booru. Three documented GET operations return JSON carrying dominant colours, original and compressed image variants, dimensions, tags, content ratings, anime and character names, the original source and full artist attribution. No API key, no registration and no account are required; rate limits are enforced per IP address and reported through standards-track RateLimit response headers. Standard public use is free, but commercial use requires prior written consent from the operator.
examples:
- key_count: 6
  name: Nekosia Api Root 200
  slug: nekosia-api-root-200
- key_count: 4
  name: Nekosia Error 400 No Match
  slug: nekosia-error-400-no-match
- key_count: 4
  name: Nekosia Error 404 Not Found
  slug: nekosia-error-404-not-found
- key_count: 12
  name: Nekosia Get Image By Id 200
  slug: nekosia-get-image-by-id-200
- key_count: 13
  name: Nekosia Images Category 200
  slug: nekosia-images-category-200
- key_count: 4
  name: Nekosia Images Nothing 200
  slug: nekosia-images-nothing-200
- key_count: 5
  name: Nekosia Tags 200
  slug: nekosia-tags-200
image: https://nekosia.cat/images/og-preview.gif
layout: provider
modified: '2026-08-19'
name: Nekosia API
nav: Providers
network: true
overview: 'Nekosia API publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include anime, neko, api, nekos, and neko api.


  Nekosia API''s developer surface includes documentation, API reference, getting-started guide, support, changelog, authentication, code examples, and 25 more developer resources.'
plans:
- name: Nekosia Plans Pricing
  plan_count: 0
  slug: nekosia-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Nekosia Rate Limits
  slug: nekosia-rate-limits
score:
  band: thin
  composite: 36.6
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 1.4
    developer_ergonomics: 61.9
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 47.4
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
security:
- kind: authentication
  name: Nekosia Authentication
  slug: nekosia-authentication
  summary_line: none · 1 scheme
- kind: domain-security
  name: Nekosia Domain Security
  slug: nekosia-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Nekosia Vulnerability Disclosure
  slug: nekosia-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: nekosia
tags:
- anime
- neko
- api
- nekos
- neko api
- booru
- image
- media
- entertainment
- images
- free api
- open access
website: https://nekosia.cat/
---
