---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 32.0
  scored_at: '2026-09-24'
api_count: 1
apis:
- description: 'An A2A 1.0 agent (JSON-RPC 2.0 over HTTP POST, streaming declared) exposing ten skills: get_company_profile, get_services, get_portfolio_projects, get_development_process, estimate_project_timeline_an'
  name: SursaTech AI Advisor A2A API
  slug: sursatech-ai-advisor-a2a-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.sursatech.com/
- group: company
  title: ''
  type: About
  url: https://www.sursatech.com/about
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sursatech.com/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://api.sursatech.com/auth.md
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sursatech
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sursatech
- group: other
  title: ''
  type: Sitemap
  url: https://www.sursatech.com/sitemap.xml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/sursatech-com/refs/heads/main/llms/sursatech-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sursatech-com-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://www.sursatech.com/llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sursatech-com/refs/heads/main/a2a/sursatech-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/sursatech-com-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/sursatech-com/refs/heads/main/well-known/sursatech-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sursatech-com-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sursatech-com/refs/heads/main/well-known/sursatech-com-openid-configuration.json
  title: ''
  type: OpenIDConnect
  url: well-known/sursatech-com-openid-configuration.json
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sursatech-com/refs/heads/main/well-known/sursatech-com-oauth-authorization-server.json
  title: ''
  type: OAuthAuthorizationServer
  url: well-known/sursatech-com-oauth-authorization-server.json
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sursatech-com/refs/heads/main/well-known/sursatech-com-oauth-protected-resource.json
  title: ''
  type: OAuthProtectedResource
  url: well-known/sursatech-com-oauth-protected-resource.json
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sursatech-com/refs/heads/main/well-known/sursatech-com-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/sursatech-com-api-catalog.json
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/sursatech-com/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sursatech-com/refs/heads/main/authentication/sursatech-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sursatech-com-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sursatech-com/refs/heads/main/scopes/sursatech-com-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/sursatech-com-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sursatech-com/refs/heads/main/conformance/sursatech-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sursatech-com-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sursatech-com/refs/heads/main/conventions/sursatech-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/sursatech-com-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sursatech-com/refs/heads/main/errors/sursatech-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/sursatech-com-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sursatech-com/refs/heads/main/lifecycle/sursatech-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/sursatech-com-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/sursatech-com/refs/heads/main/rate-limits/sursatech-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/sursatech-com-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/sursatech-com/refs/heads/main/plans/sursatech-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sursatech-com-plans-pricing.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/sursatech-com/refs/heads/main/packages/sursatech-com-packages.yml
  title: ''
  type: Packages
  url: packages/sursatech-com-packages.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sursatech-com/refs/heads/main/regulatory/sursatech-com-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/sursatech-com-regulatory-posture.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sursatech-com/refs/heads/main/security/sursatech-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sursatech-com-domain-security.yml
created: '2026-09-19'
description: 'SursaTech (Sursa Technology Private Limited) is an AI-native product engineering and consulting company founded in 2017 in Kathmandu, Nepal, building production AI agents, RAG and knowledge systems, AI-enabled SaaS products, automation and integrations, and QA leadership for clients in Nepal, Japan, Norway, the United States and the United Kingdom, and operating its own products (Humafu, AcademyKit, Buy Me a Momo). Its public machine surface is an A2A 1.0 agent — the SursaTech AI Advisor — served as a conformant agent card at /.well-known/agent-card.json with a JSON-RPC endpoint at api.sursatech.com/api/a2a: ten skills covering company knowledge (profile, services, portfolio, process, pricing), lead-requirement capture, tentative project estimates and guarded consultation booking, payment and cancel/reschedule flows. Any agent can self-register anonymously for an opaque bearer token; the provider publishes RFC 8414/OIDC authorization-server metadata, RFC 9728 protected-resource
  metadata, an RFC 9727 api-catalog, an agentskills.io skill index and an llms.txt, but no OpenAPI, SDK, MCP server, status page, pricing for the API, or legal pages.'
image: https://www.sursatech.com/brand/apple-icon.png
layout: provider
modified: '2026-09-19'
name: SursaTech
nav: Providers
network: true
overview: 'SursaTech publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI Agents, A2A, AI Consulting, Product Engineering, and Software Development.


  SursaTech''s developer surface includes pricing, documentation, authentication, and 24 more developer resources.'
plans:
- name: Sursatech Com Plans Pricing
  plan_count: 2
  slug: sursatech-com-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 2
  name: Sursatech Com Rate Limits
  slug: sursatech-com-rate-limits
scopes:
- name: Sursatech Com Scopes
  scope_count: 4
  slug: sursatech-com-scopes
  summary_line: 4 scopes · clientCredentials
score:
  band: emerging
  composite: 25.2
  coverage:
    artifact_dirs: 16
    catalog_earned: 53.0
    catalog_earned_first_party: 16.0
    catalog_gap: 62.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 75.9
    operational_transparency: 26.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 25.2
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Sursatech Com Authentication
  slug: sursatech-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Sursatech Com Domain Security
  slug: sursatech-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: sursatech-com
tags:
- AI Agents
- A2A
- AI Consulting
- Product Engineering
- Software Development
- RAG
- QA Automation
- Nepal
- Agent-Native
- Company
website: https://www.sursatech.com/
---
