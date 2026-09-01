---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.4
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: JFrog Container Registry is a free, hybrid, and multi-cloud Docker registry and Helm chart repository for managing and distributing container images with advanced access control and vulnerability scan
  name: JFrog Container Registry
  slug: jfrog-container-registry
artifact_total: 11
asyncapis:
- description: ''
  name: Jfrog Container Registry Platform Webhooks
  slug: jfrog-container-registry-platform-webhooks
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/jfrog-container-registry-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jfrog-container-registry-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/jfrog-ltd
- group: company
  title: ''
  type: Website
  url: https://jfrog.com/container-registry/
- group: docs
  title: ''
  type: Documentation
  url: https://jfrog.com/help/r/jfrog-artifactory-documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.jfrog.com/setup/docs/get-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jfrog
- group: commercial
  title: ''
  type: Pricing
  url: https://jfrog.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://jfrog.com/blog/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.jfrog.com/
- group: start
  title: ''
  type: Signup
  url: https://jfrog.com/start-free/
- group: agent
  title: ''
  type: LlmsText
  url: https://jfrog.com/llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/jfrog-container-registry-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/jfrog-container-registry-security.txt
- group: auth
  title: ''
  type: Security
  url: security/jfrog-container-registry-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/jfrog-container-registry-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/jfrog-container-registry-trust-center.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/jfrog-container-registry-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/jfrog-container-registry-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/jfrog-container-registry-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/jfrog-container-registry-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/jfrog-container-registry-cli.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/jfrog-container-registry-conventions.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/jfrog-container-registry-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/jfrog-container-registry-scopes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/jfrog-container-registry-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/jfrog-container-registry-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/jfrog-container-registry-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/jfrog-container-registry-platform-webhooks.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/jfrog-container-registry-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/jfrog-container-registry-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/jfrog-container-registry-finops.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/jfrog-container-registry-llms.txt
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.jfrog.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.jfrog.com/artifactory/reference/
- group: operate
  title: ''
  type: Support
  url: https://jfrog.com/support/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://jfrog.com/eula/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://jfrog.com/privacy-policy/
created: '2026-03-26'
description: JFrog Container Registry is a free, hybrid, and multi-cloud Docker registry and Helm chart repository for managing and distributing container images. It provides advanced access control, vulnerability scanning, and scales to support enterprise container workflows across any cloud or on-premises infrastructure.
finops:
- name: Jfrog Container Registry Finops
  service_category: API
  slug: jfrog-container-registry-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jfrog-container-registry.png
layout: provider
mcp_servers:
- description: JFrog ships a first-party REMOTE MCP server hosted on the customer's own JFrog Platform Deployment (JPD). It is generally available on JFrog Cloud (SaaS) and in Beta for self-managed installs. The too
  name: JFrog MCP Server
  slug: jfrog-mcp-server
modified: '2026-08-29'
name: JFrog Container Registry
nav: Providers
network: true
overview: 'JFrog Container Registry publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Container Images, Containers, Docker, Helm, and JFrog.


  The JFrog Container Registry catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  JFrog Container Registry''s developer surface includes documentation, getting-started guide, pricing, engineering blog, signup flow, CLI, authentication, and 32 more developer resources.'
plans:
- name: Jfrog Container Registry Plans Pricing
  plan_count: 6
  slug: jfrog-container-registry-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 1
  name: Jfrog Container Registry Rate Limits
  slug: jfrog-container-registry-rate-limits
scopes:
- name: Jfrog Container Registry Scopes
  scope_count: 0
  slug: jfrog-container-registry-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 51.1
  coverage:
    artifact_dirs: 19
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 42.7
    developer_ergonomics: 50.0
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 57.9
  previous_composite: 51.1
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jfrog-container-registry/refs/heads/main/screenshots/jfrog-container-registry-2026-06-20T183727.png
security:
- kind: authentication
  name: Jfrog Container Registry Authentication
  slug: jfrog-container-registry-authentication
  summary_line: 9 schemes
- kind: domain-security
  name: Jfrog Container Registry Domain Security
  slug: jfrog-container-registry-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Jfrog Container Registry Vulnerability Disclosure
  slug: jfrog-container-registry-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Jfrog Container Registry Trust Center
  slug: jfrog-container-registry-trust-center
  summary_line: SOC 2 Type II, SOC 3, ISO/IEC 27001, ISO/IEC 27701
slug: jfrog-container-registry
tags:
- Container Images
- Containers
- Docker
- Helm
- JFrog
- Registry
website: https://jfrog.com/container-registry/
---
