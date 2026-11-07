---
access_model:
  confidence: low
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: Security
  url: https://app-kit.dev/privacy
- group: agent
  href: https://artifacts.apis.io/app-kit-dev/llms/app-kit-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/app-kit-dev-llms.txt
- group: auth
  href: https://artifacts.apis.io/app-kit-dev/well-known/app-kit-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/app-kit-dev-security.txt
- group: agent
  href: https://artifacts.apis.io/app-kit-dev/well-known/app-kit-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/app-kit-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/app-kit-dev/hosts/app-kit-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/app-kit-dev-hosts.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/app-kit-dev
- group: auth
  href: https://artifacts.apis.io/app-kit-dev/security/app-kit-dev-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/app-kit-dev-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/app-kit-dev/security/app-kit-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/app-kit-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://app-kit.dev/
- group: company
  title: ''
  type: Blog
  url: https://app-kit.dev/blog
- group: other
  title: ''
  type: Team
  url: https://app-kit.dev/team
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://app-kit.dev/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://app-kit.dev/terms
coverage:
  checked: '2026-10-30'
  detail: API documentation and OpenAPI specs are behind a login page requiring authentication.
  evidence:
  - status: 200
    url: https://admin.app-kit.dev/openapi.json
  reason: auth-required
  state: gated
created: '2026-10-30'
description: App‑Kit builds free web tools and backend infrastructure for developers. It offers a suite of utilities such as image compression, WebP/AVIF conversion, PDF‑to‑image conversion, SEO audit with 400+ checks, text analysis for readability and keyword stuffing, and more. All tools are free, require no sign‑up, and are delivered without watermarks, providing developers with quick, on‑the‑fly processing directly in the browser.
image: https://app-kit.dev/opengraph-image
layout: provider
modified: '2026-10-30'
name: app-kit-dev
nav: Providers
network: true
overview: 'app-kit-dev is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Free, Image Processing, SEO, and Developer Utilities.


  app-kit-dev''s developer surface includes engineering blog and 12 more developer resources.'
random_paper: 2
scopes:
- name: App Kit Dev Scopes
  scope_count: 0
  slug: app-kit-dev-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 10.1
  coverage:
    artifact_dirs: 22
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.8
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 39.3
    operational_transparency: 7.9
  previous_composite: 14.9
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 32.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/app-kit-dev/app-kit-dev-2026-11-03T121022.png
security:
- kind: authentication
  name: App Kit Dev Authentication
  slug: app-kit-dev-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: App Kit Dev Domain Security
  slug: app-kit-dev-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: App Kit Dev Vulnerability Disclosure
  slug: app-kit-dev-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: app-kit-dev
tags:
- Free
- Image Processing
- SEO
- Developer Utilities
website: https://app-kit.dev/
---
