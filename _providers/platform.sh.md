---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.9
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: 'The public REST API for the Platform.sh / Upsun cloud application platform: 263 operations over 187 paths covering projects, environments, deployments, backups and restores, domains, TLS certificates,'
  name: Platform.sh REST API
  slug: platform.sh-rest-api
artifact_total: 9
asyncapis:
- description: ''
  name: Platform.Sh Webhooks
  slug: platform.sh-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://upsun.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.upsun.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.upsun.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.upsun.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.upsun.com/docs/get-started
- group: operate
  title: ''
  type: Support
  url: https://developer.upsun.com/docs/core-concepts/get-support
- group: company
  title: ''
  type: Blog
  url: https://upsun.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/platformsh
- group: operate
  title: ''
  type: StatusPage
  url: https://status.upsun.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://upsun.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://console.upsun.com/
- group: start
  title: ''
  type: Console
  url: https://console.platform.sh/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://upsun.com/trust-center/legal/tos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://upsun.com/trust-center/privacy/privacy-notice/
- group: auth
  title: ''
  type: TrustCenter
  url: https://upsun.com/trust-center/
- group: auth
  title: ''
  type: Authentication
  url: authentication/platform.sh-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/platform.sh-scopes.yml
- group: build
  title: ''
  type: Packages
  url: packages/platform.sh-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/platform.sh-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/platform.sh-cli.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/platform.sh-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/platform.sh-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/platform.sh-security.txt
- group: auth
  title: ''
  type: Security
  url: security/platform.sh-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/platform.sh-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/platform.sh-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/platform.sh-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/platform.sh-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/platform.sh-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/platform.sh-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/platform.sh-changelog.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/platform.sh-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/platform.sh-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/platform.sh-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/platform.sh-rest-api-overlay.yaml
- group: commercial
  title: ''
  type: Plans
  url: plans/platform.sh-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/platform.sh-rate-limits.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/platform.sh-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/platform.sh-webhooks.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/platform.sh-tool-crosswalk.yml
created: '2026-08-26'
description: 'Platform.sh is the container-based Platform-as-a-Service (PaaS) founded in 2010 and headquartered in Paris and San Francisco, best known for Git-driven deployments in which a single push plus a few YAML files provisions an entire cluster of applications and managed services (PostgreSQL, MySQL, Redis, RabbitMQ, OpenSearch and more) together with byte-for-byte preview environments cloned from production. The company rebranded to Upsun: platform.sh now redirects to upsun.com, the original Platform.sh product is documented as ''Upsun Fixed'' at docs.upsun.com, and the public REST API - whose own OpenAPI description reads ''Upsun, formerly Platform.sh'' - is still authenticated by the OAuth 2.0 authorization server at auth.api.platform.sh with regional gateways on platform.sh hosts. That API exposes 263 operations across projects, environments, backups, domains, certificates, variables, activities, organizations, teams, subscriptions and billing, returns RFC 9457 application/problem+json
  errors, and is accompanied by a first-party CLI, PHP/JavaScript API clients and language config readers published under the platformsh namespace.'
image: https://upsun.com/default_social.png
layout: provider
mcp_servers:
- description: ''
  name: Upsun MCP Server
  slug: upsun-mcp-server
modified: '2026-08-26'
name: Platform.sh
nav: Providers
network: true
overview: 'Platform.sh publishes 1 API on the [APIs.io](https://apis.io/) network: REST API. Tagged areas include Platform as a Service, Cloud Hosting, Application Hosting, Deployment, and DevOps.


  The Platform.sh catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Platform.sh''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 34 more developer resources.'
plans:
- name: Platform.Sh Plans Pricing
  plan_count: 0
  slug: platform.sh-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Platform.Sh Rate Limits
  slug: platform.sh-rate-limits
scopes:
- name: Platform.Sh Scopes
  scope_count: 1
  slug: platform.sh-scopes
  summary_line: 1 scope · authorizationCode/clientCredentials
score:
  band: strong
  composite: 56.4
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 30.3
    contract_quality: 59.5
    developer_ergonomics: 73.2
    discoverability: 79.6
    governance: 30.3
    operational_transparency: 44.7
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
security:
- kind: authentication
  name: Platform.Sh Authentication
  slug: platform.sh-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Platform.Sh Domain Security
  slug: platform.sh-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Platform.Sh Vulnerability Disclosure
  slug: platform.sh-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: platform.sh
tags:
- Platform as a Service
- Cloud Hosting
- Application Hosting
- Deployment
- DevOps
- Continuous Deployment
- Containers
- Managed Services
- Developer Tools
- Infrastructure
- Multicloud
- Web Hosting
website: https://upsun.com/
---
