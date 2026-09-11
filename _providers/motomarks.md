---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 15.0
  scored_at: '2026-09-10'
api_count: 3
apis:
- description: Bearer-authenticated REST/JSON API for listing brands and retrieving full brand detail including color palettes, website, social links, and metadata.
  name: JSON API
  slug: json-api
- description: Token-authenticated global image CDN delivering car logos in full, badge, and wordmark variants across multiple sizes and formats.
  name: Image CDN
  slug: image-cdn
- description: Hosted streamable-HTTP MCP server exposing read-only brand tools, account tools, resources, and prompts. Auth via OAuth 2.1 or Bearer secret key. Registry name io.motomarks/mcp.
  name: MCP Server
  slug: mcp-server
artifact_total: 11
common:
- group: company
  title: ''
  type: Website
  url: https://motomarks.io
- group: auth
  title: ''
  type: DomainSecurity
  url: security/motomarks-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/motomarks-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/motomarks-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/motomarks-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/motomarks-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/motomarks-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/motomarks-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/motomarks-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/motomarks-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://motomarks.io/changelog
- group: commercial
  title: ''
  type: Plans
  url: plans/motomarks-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/motomarks-rate-limits.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/motomarks-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/motomarks-packages.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/motomarks-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/motomarks-vulnerability-disclosure.yml
- group: docs
  title: ''
  type: APIReference
  url: https://motomarks.io/docs/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://motomarks.io/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://motomarks.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://motomarks.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://motomarks.io/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/motomarks
created: '2026-09-08'
description: A car-manufacturer logo API and image CDN delivering badge, wordmark, and full-logo assets plus structured brand data for 420+ automotive brands. Offers a REST/JSON API, a token-authenticated image CDN, a hosted MCP server, an llms.txt, and published agent skills.
image: https://motomarks.io/favicon.png
layout: provider
mcp_servers:
- description: ''
  name: Motomarks MCP Server
  slug: motomarks-mcp-server
- description: Official hosted Model Context Protocol server for the Motomarks car-logo API and image CDN. Streamable-HTTP transport at https://motomarks.io/api/mcp, MCP Registry name io.motomarks/mcp. Anonymous ses
  name: Motomarks MCP Server
  slug: motomarks-mcp-server-2
modified: '2026-09-09'
name: Motomarks
nav: Providers
network: true
overview: 'Motomarks publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include automotive, logo, image-cdn, manufacturer, and brand-assets.


  Motomarks'' developer surface includes authentication, changelog, API reference, getting-started guide, pricing, and 18 more developer resources.'
plans:
- name: Motomarks Plans Pricing
  plan_count: 4
  slug: motomarks-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 4
  name: Motomarks Rate Limits
  slug: motomarks-rate-limits
scopes:
- name: Motomarks Scopes
  scope_count: 0
  slug: motomarks-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 38.2
  coverage:
    artifact_dirs: 16
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    commercial_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 47.6
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 60.5
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Motomarks Authentication
  slug: motomarks-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Motomarks Domain Security
  slug: motomarks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Motomarks Vulnerability Disclosure
  slug: motomarks-vulnerability-disclosure
  summary_line: Hackerone
slug: motomarks
tags:
- automotive
- logo
- image-cdn
- manufacturer
- brand-assets
- images
- CDN
- developer-tools
- agent-native
- MCP
- reference-data
website: https://motomarks.io
---
