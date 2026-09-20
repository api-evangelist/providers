---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 57.6
  scored_at: '2026-09-19'
agentic_access:
- acting_count: 21
  human_in_the_loop: 1
  name: Statable Stats Api Agentic Access
  operation_count: 35
  slug: statable-stats-api-agentic-access
  summary_line: 35 operations · 21 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://statable.com/api/v1
  baseurl_source: declared
  description: Read-focused REST HTTP API for privacy-first web analytics. Bearer (stbl_) auth, server-side only (no CORS). Endpoints include GET /sites, POST /query, GET /current-visitors, GET /props, GET /funnels,
  name: Statable Stats API
  slug: statable-stats-api
artifact_total: 10
common:
- group: company
  title: ''
  type: Website
  url: https://statable.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://statable.com/docs/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://statable.com/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://statable.com/docs/getting-started/quick-start/
- group: operate
  title: ''
  type: Support
  url: https://statable.com/docs/help/service-status/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/key-arg
- group: commercial
  title: ''
  type: Pricing
  url: https://statable.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://statable.com/auth/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://statable.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://statable.com/privacy
- group: auth
  title: ''
  type: Security
  url: https://statable.com/security
- group: auth
  title: ''
  type: Compliance
  url: https://statable.com/gdpr
- group: operate
  title: ''
  type: StatusPage
  url: https://status.statable.com
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/statable-stats-api/refs/heads/main/agentic-access/statable-stats-api-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/statable-stats-api-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/statable-stats-api/refs/heads/main/authentication/statable-stats-api-authentication.yml
  title: ''
  type: Authentication
  url: authentication/statable-stats-api-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/statable-stats-api/refs/heads/main/scopes/statable-stats-api-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/statable-stats-api-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/statable-stats-api/refs/heads/main/security/statable-stats-api-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/statable-stats-api-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/statable-stats-api/refs/heads/main/security/statable-stats-api-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/statable-stats-api-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/statable-stats-api/refs/heads/main/security/statable-stats-api-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/statable-stats-api-trust-center.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/statable-stats-api/refs/heads/main/conformance/statable-stats-api-conformance.yml
  title: ''
  type: Conformance
  url: conformance/statable-stats-api-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/statable-stats-api/refs/heads/main/well-known/statable-stats-api-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/statable-stats-api-well-known.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/statable-stats-api/refs/heads/main/errors/statable-stats-api-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/statable-stats-api-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/statable-stats-api/refs/heads/main/lifecycle/statable-stats-api-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/statable-stats-api-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/statable-stats-api/refs/heads/main/rate-limits/statable-stats-api-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/statable-stats-api-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/statable-stats-api/refs/heads/main/conventions/statable-stats-api-conventions.yml
  title: ''
  type: Conventions
  url: conventions/statable-stats-api-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/statable-stats-api/refs/heads/main/conventions/statable-stats-api-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/statable-stats-api-conventions.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/statable-stats-api/refs/heads/main/packages/statable-stats-api-packages.yml
  title: ''
  type: Packages
  url: packages/statable-stats-api-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/statable-stats-api/refs/heads/main/packages/statable-stats-api-packages.yml
  title: ''
  type: SDKs
  url: packages/statable-stats-api-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/statable-stats-api/refs/heads/main/cli/statable-stats-api-cli.yml
  title: ''
  type: CLI
  url: cli/statable-stats-api-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/statable-stats-api/refs/heads/main/components/statable-stats-api-components.yml
  title: ''
  type: Components
  url: components/statable-stats-api-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/statable-stats-api/refs/heads/main/data-model/statable-stats-api-data-model.yml
  title: ''
  type: DataModel
  url: data-model/statable-stats-api-data-model.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/statable-stats-api/refs/heads/main/plans/statable-stats-api-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/statable-stats-api-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/statable-stats-api/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/statable-stats-api/refs/heads/main/overlays/statable-stats-api-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/statable-stats-api-openapi-overlay.yaml
created: '2026-09-18'
description: Privacy-first, cookieless web analytics from Statable (Key Arg B.V.), EU-hosted in the Netherlands with GDPR compliance and a ~2 KB tracking script. Exposes a server-side REST HTTP API with a public OpenAPI 3.1 contract, a hosted MCP server, an llms.txt, and a CLI for querying visitors, pages, sources, goals, funnels, custom events and live visitors.
image: https://statable.com/thumbnail.png
layout: provider
mcp_servers:
- description: ''
  name: Statable Stats API MCP Server
  slug: statable-stats-api-mcp-server
modified: '2026-09-18'
name: Statable Stats API
nav: Providers
network: true
overview: 'Statable Stats API publishes 1 API on the [APIs.io](https://apis.io/) network: Statable Stats API. Tagged areas include Analytics, Web Analytics, Cookieless, Privacy, and GDPR.


  Statable Stats API''s developer surface includes documentation, getting-started guide, support, pricing, signup flow, authentication, CLI, and 27 more developer resources.'
plans:
- name: Statable Stats Api Plans Pricing
  plan_count: 10
  slug: statable-stats-api-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Statable Stats Api Rate Limits
  slug: statable-stats-api-rate-limits
scopes:
- name: Statable Stats Api Scopes
  scope_count: 2
  slug: statable-stats-api-scopes
  summary_line: 2 scopes
score:
  band: strong
  composite: 62.1
  coverage:
    artifact_dirs: 21
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.3
  facets:
    access_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 55.2
    developer_ergonomics: 70.8
    discoverability: 75.9
    operational_transparency: 21.1
  previous_composite: 63.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-19'
  trend: flat
  upsert:
    applies: true
    score: 38.9
security:
- kind: authentication
  name: Statable Stats Api Authentication
  slug: statable-stats-api-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Statable Stats Api Domain Security
  slug: statable-stats-api-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Statable Stats Api Vulnerability Disclosure
  slug: statable-stats-api-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Statable Stats Api Trust Center
  slug: statable-stats-api-trust-center
  summary_line: trust center published
slug: statable-stats-api
tags:
- Analytics
- Web Analytics
- Cookieless
- Privacy
- GDPR
- OpenAPI
- MCP
- llms-txt
- EU-hosted
website: https://statable.com
---
