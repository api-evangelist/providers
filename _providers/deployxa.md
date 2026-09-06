---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: flavored
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: self
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 51.1
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Deployxa Agentic Access
  operation_count: 2
  slug: deployxa-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 1
apis:
- baseURL: https://deployxa.com
  baseurl_source: declared
  description: 'AI-first autonomous cloud deployment platform API. The published OpenAPI 3.0.3 contract covers project creation and deployment execution under /api/v1 (versioned URI paths, Deprecation/Sunset headers '
  name: Deployxa Platform
  slug: deployxa-platform
artifact_total: 10
common:
- group: company
  title: ''
  type: Website
  url: https://deployxa.com
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/deployxa-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/deployxa-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/deployxa-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/deployxa-domain-security.yml
- group: auth
  title: ''
  type: Security
  url: https://deployxa.com/security
- group: start
  title: ''
  type: DeveloperPortal
  url: https://deployxa.com/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://deployxa.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://deployxa.com/contact
- group: company
  title: ''
  type: Blog
  url: https://deployxa.com/dispatch
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/deployxa
- group: commercial
  title: ''
  type: Pricing
  url: https://deployxa.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://deployxa.com/dashboard
- group: commercial
  title: ''
  type: TermsOfService
  url: https://deployxa.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://deployxa.com/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://deployxa.com/changelog
- group: operate
  title: ''
  type: StatusPage
  url: https://deployxa.com/status
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/deployxa-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/deployxa-lifecycle.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/deployxa-well-known.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/deployxa-a2a.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/deployxa-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/deployxa-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/deployxa-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/deployxa-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/deployxa-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/deployxa-conventions.yml
- group: build
  title: ''
  type: Packages
  url: packages/deployxa-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/deployxa-cli.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/deployxa-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/deployxa-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/deployxa-openapi-overlay.yaml
- group: design
  title: ''
  type: DataModel
  url: data-model/deployxa-data-model.yml
created: '2026-09-05'
description: AI-first autonomous cloud deployment platform for deploying AI-built and containerized web apps to production, featuring a deployment intelligence engine, global edge deployment, managed databases, VPS clusters, and a CLI. Publishes an OpenAPI 3.0.3 contract at /openapi.json, an llms.txt, an A2A agent card with an AP2 agentic-payments extension, an RFC 9727 api-catalog, OAuth 2.0 discovery metadata, and an OAuth-gated hosted MCP server at mcp.deployxa.com — all verified live 2026-09-05.
image: https://deployxa.com/og/home.png
layout: provider
mcp_servers:
- description: ''
  name: Deployxa MCP Server
  slug: deployxa-mcp-server
modified: '2026-09-05'
name: Deployxa
nav: Providers
network: true
overview: 'Deployxa publishes 1 API on the [APIs.io](https://apis.io/) network: Platform. Tagged areas include platform-as-a-service, cloud-deployment, devops, ci-cd, and containers-docker.


  Deployxa''s developer surface includes getting-started guide, support, engineering blog, pricing, signup flow, changelog, authentication, and 27 more developer resources.'
plans:
- name: Deployxa Plans Pricing
  plan_count: 4
  slug: deployxa-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Deployxa Rate Limits
  slug: deployxa-rate-limits
scopes:
- name: Deployxa Scopes
  scope_count: 11
  slug: deployxa-scopes
  summary_line: 11 scopes · authorizationCode
score:
  band: strong
  composite: 57.0
  coverage:
    artifact_dirs: 20
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 40.1
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 55.3
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: authentication
  name: Deployxa Authentication
  slug: deployxa-authentication
  summary_line: http-bearer/oauth2 · 3 schemes
- kind: domain-security
  name: Deployxa Domain Security
  slug: deployxa-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Deployxa Vulnerability Disclosure
  slug: deployxa-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Deployxa Trust Center
  slug: deployxa-trust-center
  summary_line: trust center published
slug: deployxa
tags:
- platform-as-a-service
- cloud-deployment
- devops
- ci-cd
- containers-docker
- edge-hosting
- managed-databases
- ai-ops
- developer-tools
website: https://deployxa.com
---
