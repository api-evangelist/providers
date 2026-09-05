---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
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
    well_known_catalog: false
  schema_version: 0.2
  score: 28.6
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: The DevRev public REST API for managing works (issues/tickets), parts, accounts, articles, conversations, timeline entries, webhooks, and more. Resource-oriented URLs, JSON request/response bodies, PA
  name: DevRev REST API
  slug: devrev-rest-api
artifact_total: 7
asyncapis:
- description: ''
  name: Devrev Webhooks
  slug: devrev-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/devrev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://devrev.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.devrev.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.devrev.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.devrev.ai/public/about/for-developers
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.devrev.ai/api-reference/getting-started
- group: company
  title: ''
  type: Blog
  url: https://devrev.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/devrev
- group: commercial
  title: ''
  type: Pricing
  url: https://devrev.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.devrev.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://devrev.ai/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://devrev.ai/legal/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.devrev.ai/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/devrev-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/devrev-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/devrev-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/devrev-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/devrev-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/devrev-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/devrev-mcp.yml
- group: design
  title: ''
  type: Components
  url: components/devrev-components.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/devrev-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/devrev-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/devrev-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/devrev-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/devrev-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://security.devrev.ai/
- group: auth
  title: ''
  type: TrustCenter
  url: security/devrev-trust-center.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/devrev-webhooks.yml
created: '2026-07-17'
description: DevRev is an AI-native platform that unifies customer support, product development, and analytics on a single knowledge graph connecting end users (Rev), builders (Dev), and their work. Its REST API is organized around resource-oriented URLs, accepts and returns JSON, and uses standard HTTP verbs and status codes. Endpoints cover works (issues and tickets), parts (the product hierarchy), accounts, articles and the knowledge base, conversations and timeline entries, tags, schedules, SLAs, surveys, webhooks, and snap-ins (custom automations and apps that extend the platform). Authentication uses Personal Access Tokens (PATs) passed as a Bearer token, and both a stable Public API and an early-access Beta API are published. DevRev also ships first-party SDKs, a Go-based CLI, the embeddable PLuG support widget, and Airdrop (ADaaS) data-sync tooling.
image: https://cdn.sanity.io/images/umrbtih2/production/c7a33aa73687dea1ff37c39c2f8a4f0fc350e0d6-2880x1620.png
layout: provider
mcp_servers:
- description: DevRev ships an official local MCP server as part of the Airdrop/Airsync `chef-cli` toolchain. It is run locally over stdio (not a remote hosted endpoint) and is scoped to Airdrop metadata-mapping dev
  name: Devrev MCP Server
  slug: devrev-mcp-server
modified: '2026-07-18'
name: Devrev
nav: Providers
network: true
overview: 'Devrev publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Customer-Support, Product Development, Issue Tracking, and Knowledge Base.


  The Devrev catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Devrev''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, changelog, and 22 more developer resources.'
random_paper: 1
rate_limits:
- limit_count: 0
  name: Devrev Rate Limits
  slug: devrev-rate-limits
score:
  band: developing
  composite: 43.0
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 65.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 43.0
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/devrev/refs/heads/main/screenshots/devrev-2026-07-25T211828.png
security:
- kind: authentication
  name: Devrev Authentication
  slug: devrev-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Devrev Domain Security
  slug: devrev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Devrev Trust Center
  slug: devrev-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: devrev
tags:
- Company
- Customer-Support
- Product Development
- Issue Tracking
- Knowledge Base
- CRM
- Developer Tools
- Artificial Intelligence
- Webhook
- Automation
website: https://devrev.ai
---
