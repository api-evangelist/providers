---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 47.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'A live, OAuth-protected Model Context Protocol server that involve.me serves from its own infrastructure and advertises through RFC 9728 protected-resource metadata on www.involve.me. SCOPE: it expose'
  name: involve.me Website Content MCP Server
  slug: involveme-website-content-mcp-server
artifact_total: 12
asyncapis:
- description: ''
  name: Involve Me Webhooks
  slug: involve-me-webhooks
common:
- group: operate
  href: https://artifacts.apis.io/involve-me/rate-limits/involve-me-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/involve-me-rate-limits.yml
- group: auth
  href: https://artifacts.apis.io/involve-me/security/involve-me-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/involve-me-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/involve-me/security/involve-me-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/involve-me-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/involve-me/security/involve-me-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/involve-me-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/involve-me/security/involve-me-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/involve-me-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.involve.me/
- group: docs
  title: ''
  type: Documentation
  url: https://help.involve.me/en/
- group: operate
  title: ''
  type: Support
  url: https://www.involve.me/contact
- group: company
  title: ''
  type: Blog
  url: https://www.involve.me/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.involve.me/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.involve.me/register
- group: start
  title: ''
  type: Login
  url: https://app.involve.me/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.involve.me/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.involve.me/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/stereosense
- group: operate
  title: ''
  type: StatusPage
  url: https://status.involve.me/
- group: commercial
  title: ''
  type: DataProcessingAgreement
  url: https://www.involve.me/data-processing
- group: agent
  href: https://artifacts.apis.io/involve-me/llms/involve-me-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/involve-me-llms.txt
- group: agent
  href: https://artifacts.apis.io/involve-me/well-known/involve-me-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/involve-me-well-known.yml
- group: auth
  href: https://artifacts.apis.io/involve-me/well-known/involve-me-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/involve-me-security.txt
- group: design
  href: https://artifacts.apis.io/involve-me/asyncapi/involve-me-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/involve-me-webhooks.yml
- group: auth
  href: https://artifacts.apis.io/involve-me/authentication/involve-me-authentication.yml
  title: ''
  type: Authentication
  url: authentication/involve-me-authentication.yml
- group: auth
  href: https://artifacts.apis.io/involve-me/scopes/involve-me-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/involve-me-scopes.yml
- group: agent
  href: https://artifacts.apis.io/involve-me/mcp/involve-me-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/involve-me-mcp.yml
- group: design
  href: https://artifacts.apis.io/involve-me/conformance/involve-me-conformance.yml
  title: ''
  type: Conformance
  url: conformance/involve-me-conformance.yml
- group: auth
  href: https://artifacts.apis.io/involve-me/conformance/involve-me-conformance.yml
  title: ''
  type: Compliance
  url: conformance/involve-me-conformance.yml
- group: design
  href: https://artifacts.apis.io/involve-me/lifecycle/involve-me-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/involve-me-lifecycle.yml
- group: commercial
  href: https://artifacts.apis.io/involve-me/plans/involve-me-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/involve-me-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/involve-me/conventions/involve-me-conventions.yml
  title: ''
  type: Conventions
  url: conventions/involve-me-conventions.yml
- group: design
  href: https://artifacts.apis.io/involve-me/components/involve-me-components.yml
  title: ''
  type: Components
  url: components/involve-me-components.yml
- group: design
  href: https://artifacts.apis.io/involve-me/data-model/involve-me-data-model.yml
  title: ''
  type: DataModel
  url: data-model/involve-me-data-model.yml
created: '2026-08-12'
description: 'involve.me is an AI quiz, form and funnel builder with built-in email automation and a lightweight CRM, operated by stereosense GmbH and used by marketing teams to capture, qualify and follow up on leads. Customers build quizzes, assessments, calculators, product finders, landing pages, surveys and payment pages in a no-code editor, publish them as a hosted page or an embedded widget, and route submissions into 55+ native CRM and email destinations. Its programmable surface is deliberately narrow: there is no public REST API and no OpenAPI, and the only machine-addressable paths are an outbound webhook that fires when a participant completes a funnel (Scale plan and above), a copy-paste JavaScript embed loader, Zapier and Make connectors, and an OAuth-protected Model Context Protocol server that exposes the marketing website''s Statamic CMS rather than the product itself.'
finops:
- has_sources: true
  method: derived
  name: Involve Me Finops
  primary_unit: user
  service_category: ''
  slug: involve-me-finops
  template: false
image: https://www.involve.me/favicons/favicon-32x32.png
layout: provider
mcp_servers:
- description: involve.me serves a live, OAuth-protected Model Context Protocol server. It is advertised by RFC 9728 protected-resource metadata on the public marketing host and it answers. IMPORTANT SCOPE NOTE — th
  name: involve.me Statamic Content MCP
  slug: involve-me-statamic-content-mcp
modified: '2026-08-12'
name: involve.me
nav: Providers
network: true
overview: 'involve.me is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketing, Lead Generation, Forms, and Surveys.


  The involve.me catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  involve.me''s developer surface includes documentation, support, engineering blog, pricing, signup flow, authentication, and 25 more developer resources.'
plans:
- name: Involve Me Plans Pricing
  plan_count: 10
  slug: involve-me-plans-pricing
- name: Involve Me Price Estimates
  plan_count: 0
  slug: involve-me-price-estimates
random_paper: 18
rate_limits:
- limit_count: 0
  name: Involve Me Rate Limits
  slug: involve-me-rate-limits
scopes:
- name: Involve Me Scopes
  scope_count: 21
  slug: involve-me-scopes
  summary_line: 21 scopes
score:
  band: strong
  composite: 54.4
  coverage:
    artifact_dirs: 23
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 39.0
    developer_ergonomics: 28.6
    discoverability: 75.0
    operational_transparency: 36.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - austria
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 54.4
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/involve-me/involve-me-2026-08-17T081000.png
security:
- kind: authentication
  name: Involve Me Authentication
  slug: involve-me-authentication
  summary_line: 5 schemes
- kind: domain-security
  name: Involve Me Domain Security
  slug: involve-me-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Involve Me Vulnerability Disclosure
  slug: involve-me-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Involve Me Trust Center
  slug: involve-me-trust-center
  summary_line: SOC 2 Type II, GDPR
slug: involve-me
tags:
- Company
- Marketing
- Lead Generation
- Forms
- Surveys
- Quizzes
- No-Code
- Email Marketing
- CRM
- Webhook
- MCP
- Austria
website: https://www.involve.me/
---
