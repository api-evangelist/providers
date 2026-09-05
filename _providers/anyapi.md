---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 50.2
  scored_at: '2026-09-04'
api_count: 1
apis:
- baseURL: https://api.getanyapi.com
  baseurl_source: declared
  description: 'Unified REST gateway to 363 normalized scraping and data APIs, published as an OpenAPI 3.1.0 document with 370 operations. Execute jobs via POST /v1/run/{sku}, browse and search the catalog without a '
  name: AnyAPI Gateway API
  slug: anyapi-gateway-api
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/anyapi-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/anyapi-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/anyapi-scopes.yml
- group: build
  title: ''
  type: Packages
  url: packages/anyapi-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/anyapi-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/anyapi-cli.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/anyapi-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: https://getanyapi.com/.well-known/api-catalog
- group: design
  title: ''
  type: Conventions
  url: conventions/anyapi-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/anyapi-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/anyapi-problem-types.yml
- group: design
  title: ''
  type: ErrorCodes
  url: errors/anyapi-error-codes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/anyapi-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/anyapi-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/anyapi-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/anyapi-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/anyapi-sandbox.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/anyapi-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/anyapi-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/anyapi-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://getanyapi.com/security
- group: start
  title: ''
  type: DeveloperPortal
  url: https://getanyapi.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://getanyapi.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://getanyapi.com/docs/api-reference/browse-the-api-catalog
- group: start
  title: ''
  type: GettingStarted
  url: https://getanyapi.com/docs/quickstart
- group: operate
  title: ''
  type: Support
  url: https://getanyapi.com/contact
- group: company
  title: ''
  type: Blog
  url: https://getanyapi.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getanyapi-com
- group: commercial
  title: ''
  type: Pricing
  url: https://getanyapi.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://getanyapi.com/dashboard
- group: commercial
  title: ''
  type: TermsOfService
  url: https://getanyapi.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://getanyapi.com/privacy
created: '2026-09-04'
description: 'AnyAPI is a unified gateway and marketplace for scraping and data APIs, operated by AnyAPI Labs, Inc. One key and one prepaid USD wallet reach 363 normalized third-party data sources - social profiles and posts, search and SEO, commerce listings and reviews, sales enrichment and email verification, and clean Markdown for any page with no API at all - through a single REST interface, billed pay-per-successful-request with no subscriptions and no seats. Each SKU is one discovered operation with a normalized JSON input and output schema, priced in real dollars and served by several independent sources ordered cheapest-first with automatic failover. It is unusually agent-native: a public OpenAPI 3.1.0 with 370 operations, a hosted MCP server whose tools/list answers anonymously, OAuth 2.1 with device flow, llms.txt, a published Agent Skill, an RFC 9727 api-catalog, agents that mint their own capped trial credential with no human, and inline per-call crypto payment over x402 and
  MPP.'
image: https://getanyapi.com/og-v7.png
layout: provider
mcp_servers:
- description: ''
  name: AnyAPI
  slug: anyapi
- description: ''
  name: AnyAPI MCP Server
  slug: anyapi-mcp-server
modified: '2026-09-04'
name: AnyAPI
nav: Providers
network: true
overview: 'AnyAPI publishes 1 API on the [APIs.io](https://apis.io/) network: Gateway API. Tagged areas include developer_tools, data, search, scraping, and social_media.


  AnyAPI''s developer surface includes authentication, CLI, changelog, sandbox, documentation, API reference, getting-started guide, and 26 more developer resources.'
plans:
- name: Anyapi Plans Pricing
  plan_count: 0
  slug: anyapi-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Anyapi Rate Limits
  slug: anyapi-rate-limits
scopes:
- name: Anyapi Scopes
  scope_count: 2
  slug: anyapi-scopes
  summary_line: 2 scopes · authorizationCode/refreshToken/deviceCode
score:
  band: developing
  composite: 52.5
  coverage:
    artifact_dirs: 21
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 26.7
    developer_ergonomics: 85.7
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 31.6
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 64.1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
security:
- kind: authentication
  name: Anyapi Authentication
  slug: anyapi-authentication
  summary_line: apiKey/http/oauth2/inline-payment · 6 schemes
- kind: domain-security
  name: Anyapi Domain Security
  slug: anyapi-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Anyapi Vulnerability Disclosure
  slug: anyapi-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Anyapi Trust Center
  slug: anyapi-trust-center
  summary_line: trust center published
slug: anyapi
tags:
- developer_tools
- data
- search
- scraping
- social_media
- ecommerce
- seo
- enrichment
- mcp
- agent-native
- web-data
- api-marketplace
- agent-payments
- x402
website: https://getanyapi.com/docs
---
