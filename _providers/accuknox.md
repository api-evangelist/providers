---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 31.5
  scored_at: '2026-09-07'
api_count: 4
apis:
- description: Token-authenticated REST API behind the AccuKnox SaaS console, serving asset inventory, security findings, AI/ML model risk (ModelKnox) and tenant configuration under an /api/v1/ path prefix. Served p
  name: AccuKnox SaaS Platform API
  slug: accuknox-saas-platform-api
- description: gRPC services for AccuKnox Discovery Engine (knoxAutoPolicy), which auto-discovers least-permissive network and system policies from observed workload behaviour. Nine published proto3 contracts coveri
  name: AccuKnox Discovery Engine gRPC API
  slug: accuknox-discovery-engine
- description: gRPC services for SentryFlow, AccuKnox's API observability and classification component. Streams API access logs, API events and Envoy/API metrics from service mesh and ingress data planes, and classi
  name: AccuKnox SentryFlow API Observability gRPC API
  slug: accuknox-sentryflow
- description: First-party Model Context Protocol server published by AccuKnox that exposes the SaaS Platform API to agents as MCP tools for asset search, finding retrieval, finding filters and funnels, and AI/ML mo
  name: AccuKnox MCP Server
  slug: accuknox-mcp-server
artifact_total: 12
asyncapis:
- description: ''
  name: Accuknox Webhooks
  slug: accuknox-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/accuknox-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://accuknox.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.accuknox.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.accuknox.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.accuknox.com/how-to/
- group: operate
  title: ''
  type: Support
  url: https://accu-knox.atlassian.net/servicedesk/customer/portal/1
- group: company
  title: ''
  type: Blog
  url: https://accuknox.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://accuknox.com/feed
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/accuknox
- group: commercial
  title: ''
  type: Pricing
  url: https://accuknox.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://accuknox.com/free-trial
- group: commercial
  title: ''
  type: TermsOfService
  url: https://accuknox.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://accuknox.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.accuknox.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://help.accuknox.com/getting-started/accuknox-release-notes/
- group: build
  title: ''
  type: SourceCode
  url: https://accuknox.com/open-source-repos
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/accuknox-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/accuknox-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/accuknox-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/accuknox-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/accuknox-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/accuknox-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/accuknox-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/accuknox-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/accuknox-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/accuknox-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/accuknox-webhooks.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/accuknox-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/accuknox-rate-limits.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/accuknox-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://accuknox.com/security-advisories
created: '2026-09-06'
description: AccuKnox is a cloud-native application protection platform (CNAPP) vendor built on a Zero Trust model, covering cloud security posture management (CSPM), workload and Kubernetes runtime security (CWPP), application security posture management (ASPM), AI/ML model security (AI-SPM / ModelKnox) and API security. It originated the open source KubeArmor eBPF/LSM runtime enforcement engine (a CNCF project) and publishes the Discovery Engine and SentryFlow gRPC services, a knoxctl CLI, a Terraform provider, a first-party Model Context Protocol server, and a token-authenticated REST API on per-tenant cspm.*.accuknox.com hosts.
image: https://accuknox.com/wp-content/uploads/accuknox-logo-2.png
layout: provider
mcp_servers:
- description: ''
  name: AccuKnox Asset Manager
  slug: accuknox-asset-manager
modified: '2026-09-06'
name: AccuKnox
nav: Providers
network: true
overview: 'AccuKnox publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Cloud Security, Cloud Native Application Protection Platform, and Kubernetes Security.


  The AccuKnox catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  AccuKnox''s developer surface includes documentation, getting-started guide, support, engineering blog, pricing, signup flow, changelog, and 24 more developer resources.'
plans:
- name: Accuknox Plans Pricing
  plan_count: 0
  slug: accuknox-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Accuknox Rate Limits
  slug: accuknox-rate-limits
scopes:
- name: Accuknox Scopes
  scope_count: 0
  slug: accuknox-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 47.0
  coverage:
    artifact_dirs: 17
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.4
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 57.1
    discoverability: 72.2
    governance: 18.2
    operational_transparency: 52.6
  previous_composite: 47.4
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.20.0
  scored_at: '2026-09-07'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Accuknox Authentication
  slug: accuknox-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Accuknox Domain Security
  slug: accuknox-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Accuknox Vulnerability Disclosure
  slug: accuknox-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: accuknox
tags:
- Company
- Security
- Cloud Security
- Cloud Native Application Protection Platform
- Kubernetes Security
- Runtime Security
- Zero Trust
- DevSecOps
- Compliance
- AI Security
- Vulnerability Management
- Container Security
website: https://accuknox.com/
---
