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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: true
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: na
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 45.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Navattic's hosted, remote Model Context Protocol server — the company's primary machine-readable product surface. Agents authenticate with an OAuth 2.1 authorization-code flow (PKCE, dynamic client re
  name: Navattic MCP Server
  slug: navattic-mcp-server
- baseURL: https://api.navattic.com
  baseurl_source: declared
  description: The Health API from Navattic — 1 operation(s) for health.
  name: Navattic Health API
  slug: navattic-health-api
artifact_total: 15
asyncapis:
- description: ''
  name: Navattic Webhooks
  slug: navattic-webhooks
common:
- group: other
  href: https://artifacts.apis.io/navattic/overlays/navattic-website-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/navattic-website-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/navattic/security/navattic-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/navattic-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/navattic/security/navattic-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/navattic-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.navattic.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.navattic.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Navattic
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/navattic
- group: company
  title: ''
  type: Blog
  url: https://www.navattic.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.navattic.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.navattic.com
- group: other
  title: ''
  type: X
  url: https://x.com/navattic
- group: commercial
  href: https://artifacts.apis.io/navattic/plans/navattic-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/navattic-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/navattic/rate-limits/navattic-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/navattic-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/navattic/finops/navattic-finops.yml
  title: ''
  type: FinOps
  url: finops/navattic-finops.yml
- group: company
  href: https://artifacts.apis.io/navattic/blogs/blogs.json
  title: ''
  type: BlogFeed
  url: blogs/blogs.json
- group: design
  href: https://artifacts.apis.io/navattic/json-ld/navattic-context.jsonld
  title: ''
  type: JSONLDContext
  url: json-ld/navattic-context.jsonld
- group: auth
  title: ''
  type: Security
  url: https://www.navattic.com/company/security
- group: auth
  href: https://artifacts.apis.io/navattic/security/navattic-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/navattic-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.navattic.com/
- group: agent
  href: https://artifacts.apis.io/navattic/well-known/navattic-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/navattic-well-known.yml
- group: other
  href: https://artifacts.apis.io/navattic/well-known/navattic-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/navattic-api-catalog.json
- group: other
  href: https://artifacts.apis.io/navattic/well-known/navattic-robots.txt
  title: ''
  type: ContentSignal
  url: well-known/navattic-robots.txt
- group: other
  href: https://artifacts.apis.io/navattic/a2a/navattic-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/navattic-a2a.yml
- group: agent
  href: https://artifacts.apis.io/navattic/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/navattic/llms/navattic-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/navattic-llms.txt
- group: auth
  href: https://artifacts.apis.io/navattic/authentication/navattic-authentication.yml
  title: ''
  type: Authentication
  url: authentication/navattic-authentication.yml
- group: auth
  href: https://artifacts.apis.io/navattic/scopes/navattic-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/navattic-scopes.yml
- group: design
  href: https://artifacts.apis.io/navattic/conventions/navattic-conventions.yml
  title: ''
  type: Conventions
  url: conventions/navattic-conventions.yml
- group: design
  href: https://artifacts.apis.io/navattic/errors/navattic-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/navattic-problem-types.yml
- group: design
  href: https://artifacts.apis.io/navattic/lifecycle/navattic-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/navattic-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/navattic/changelog/navattic-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/navattic-changelog.yml
- group: design
  href: https://artifacts.apis.io/navattic/conformance/navattic-conformance.yml
  title: ''
  type: Conformance
  url: conformance/navattic-conformance.yml
- group: build
  href: https://artifacts.apis.io/navattic/packages/navattic-packages.yml
  title: ''
  type: Packages
  url: packages/navattic-packages.yml
- group: design
  href: https://artifacts.apis.io/navattic/components/navattic-components.yml
  title: ''
  type: Components
  url: components/navattic-components.yml
- group: design
  href: https://artifacts.apis.io/navattic/data-model/navattic-data-model.yml
  title: ''
  type: DataModel
  url: data-model/navattic-data-model.yml
- group: design
  href: https://artifacts.apis.io/navattic/asyncapi/navattic-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/navattic-webhooks.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.navattic.com/build/demo
- group: operate
  title: ''
  type: Support
  url: https://www.navattic.com/contact
- group: start
  title: ''
  type: SignUp
  url: https://app.navattic.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.navattic.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.navattic.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.navattic.com/legal/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Navattic
created: 2026-06-13
description: Navattic is an interactive product demo platform that enables marketing and sales teams to create, manage, and embed no-code product demos without engineering involvement. The platform provides a REST API and webhook integration for automating demo workflows and syncing engagement data with CRM, marketing automation, and analytics tools. Navattic supports integrations with HubSpot, Salesforce, Marketo, Segment, Gong, and dozens of other go-to-market platforms. Teams use Navattic to accelerate sales cycles, improve lead qualification, and deliver personalized demo experiences across their entire funnel.
finops:
- has_sources: true
  method: derived
  name: Navattic Finops
  primary_unit: ''
  service_category: ''
  slug: navattic-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/navattic.png
jsonld:
- class_count: 21
  name: Navattic Context
  property_count: 0
  slug: navattic-context
layout: provider
mcp_servers:
- description: Navattic ships a first-party, hosted remote MCP server. It is the company's primary machine-readable product surface — there is no public REST API reference — and it is reachable by any MCP client tha
  name: Navattic MCP Server
  slug: navattic
modified: 2026-08-13
name: Navattic
nav: Providers
network: true
overview: 'Navattic publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Health API, and 1 more. Tagged areas include Interactive Demos, Product Demo, Sales Enablement, Marketing, and No-Code.


  The Navattic catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Navattic''s developer surface includes documentation, engineering blog, pricing, authentication, changelog, getting-started guide, support, and 36 more developer resources.'
plans:
- name: Navattic Plans Pricing
  plan_count: 5
  slug: navattic-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Navattic Rate Limits
  slug: navattic-rate-limits
rules:
- authorship: generated
  effective_rule_count: 65
  extends:
  - spectral:oas
  name: Navattic API Rules
  rule_count: 24
  severity_counts:
    error: 22
    hint: 0
    info: 1
    warn: 1
  slug: navattic-rules
scopes:
- name: Navattic Scopes
  scope_count: 11
  slug: navattic-scopes
  summary_line: 11 scopes · authorizationCode
score:
  band: strong
  composite: 63.5
  coverage:
    artifact_dirs: 31
    catalog_earned: 61.5
    catalog_earned_first_party: 12.0
    catalog_gap: 53.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.1
  facets:
    access_clarity: 85.5
    contract_governance: 31.8
    contract_quality: 57.0
    developer_ergonomics: 47.6
    discoverability: 75.0
    operational_transparency: 52.6
  previous_composite: 62.4
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 1
    mcp: first-party
    skills: first-party
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
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/navattic/navattic-2026-06-20T190058.png
security:
- kind: authentication
  name: Navattic Authentication
  slug: navattic-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Navattic Domain Security
  slug: navattic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Navattic Vulnerability Disclosure
  slug: navattic-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Navattic Trust Center
  slug: navattic-trust-center
  summary_line: SOC 2 Type II, GDPR
skill_count: 1
skills:
- name: Navattic
  slug: navattic-navattic
slug: navattic
tags:
- Interactive Demos
- Product Demo
- Sales Enablement
- Marketing
- No-Code
- Webhook
- CRM Integration
- Sales Automation
- MCP
- Agents
- Product Analytics
- A2A
website: https://www.navattic.com/
---
