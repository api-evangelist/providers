---
access_model:
  confidence: high
  label: Free API with approved developer account
  onboarding: self-serve
  pricing: unknown
  public: true
  source:
  - https://developer.hootsuite.com/docs/faq
  - https://hootsuite.com/plans
  trial: true
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 49.2
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 39
  human_in_the_loop: 0
  name: Hootsuite Agentic Access
  operation_count: 76
  slug: hootsuite-agentic-access
  summary_line: 76 operations · 39 acting
api_count: 5
apis:
- description: The Hootsuite platform REST API — 48 operations covering OAuth 2.0 authentication, the authenticated member, media upload, message scheduling and the prescreen approval workflow, comments, social prof
  name: Hootsuite REST API
  slug: rest-api
- description: Organic and paid social analytics — published posts with lifetime metrics, daily profile metrics, and campaign / ad-set / ad entities and daily metrics for Facebook and Twitter ad accounts. Gated by t
  name: Hootsuite Analytics REST API
  slug: analytics-api
- description: The Inbox 2.0 (formerly Sparkcentral) customer-conversation API — CRM contact attribute write-back, the Virtual Agent API for bot-driven conversations and attachments, real-time reporting metrics, use
  name: Hootsuite Inbox 2.0 API
  slug: inbox-api
- description: The Amplify employee-advocacy API — publish content directly into Amplify, read the authenticated member and their organizations, manage advocacy topics, and deobfuscate UTM parameters on shared links
  name: Hootsuite Amplify REST API
  slug: amplify-api
- description: A remote Model Context Protocol endpoint served from Hootsuite's own ReadMe-hosted developer documentation site. Reachable and real, but gated — initialize and tools/list both return HTTP 401 "Authori
  name: Hootsuite Developer Documentation MCP
  slug: mcp
artifact_total: 20
asyncapis:
- description: ''
  name: Hootsuite Webhooks
  slug: hootsuite-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Hootsuite Amplify REST API
  slug: open-hootsuite-amplify-api
- collection_type: open
  name: Hootsuite Analytics REST API
  slug: open-hootsuite-analytics-api
- collection_type: open
  name: Inbox 2.0 API Reference
  slug: open-hootsuite-inbox-api
- collection_type: open
  name: Hootsuite REST API
  slug: open-hootsuite-rest-api
- collection_type: open
  name: Hootsuite Platform API
  slug: open-hootsuite
common:
- group: agent
  title: ''
  type: WellKnown
  url: well-known/hootsuite-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/hootsuite-api-catalog.json
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hootsuite-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/hootsuite-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/hootsuite-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hootsuite-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hootsuite-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/hootsuite-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hootsuite-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hootsuite-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/hootsuite-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hootsuite-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hootsuite-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/hootsuite-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.hootsuite.com
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/hootsuite-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/hootsuite-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hootsuite-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/hootsuite-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/hootsuite-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/hootsuite-packages.yml
- group: design
  title: ''
  type: Components
  url: components/hootsuite-components.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/hootsuite-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/hootsuite-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/hootsuite-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hootsuite-llms.txt
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.hootsuite.com/llms.txt
- group: build
  title: ''
  type: Postman
  url: https://app.getpostman.com/run-collection/eeda0fcdf55ea26bd0ec
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hootsuite
- group: company
  title: ''
  type: Website
  url: https://www.hootsuite.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.hootsuite.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.hootsuite.com/docs/api-overview
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.hootsuite.com/docs/api/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.hootsuite.com/docs/getting-started-with-the-rest-api
- group: start
  title: ''
  type: Signup
  url: https://hootsuite.com/plans
- group: commercial
  title: ''
  type: Pricing
  url: https://hootsuite.com/plans
- group: start
  title: ''
  type: Login
  url: https://hootsuite.com/login
- group: operate
  title: ''
  type: Support
  url: https://help.hootsuite.com
- group: company
  title: ''
  type: Blog
  url: https://blog.hootsuite.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hootsuite
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hootsuite.com/legal/api-terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hootsuite.com/legal/privacy
created: '2026-05-11'
description: Hootsuite is a social media management platform that lets organizations schedule posts, monitor conversations, run paid campaigns, and analyze performance across LinkedIn, X (Twitter), Facebook, Instagram, TikTok, YouTube, and Pinterest from a single dashboard. The platform serves marketers, agencies, and enterprises with collaboration, approval, and governance workflows. Hootsuite publishes four first-party machine-readable API contracts on platform.hootsuite.com — a 48-operation REST API for messages, media, social profiles, members, teams and SCIM 2.0 provisioning; an Analytics API for organic and paid metrics; the Inbox 2.0 (Sparkcentral) API for CRM, virtual agents, queues and proactive messaging; and the Amplify employee-advocacy API — all authenticated with OAuth 2.0. It also serves an RFC 9727 API catalog, RFC 8414 authorization server metadata and RFC 9728 protected resource metadata.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hootsuite.png
layout: provider
mcp_servers:
- description: ''
  name: hootsuite-mcp.yml
  slug: hootsuite-mcpyml
modified: '2026-08-13'
name: Hootsuite
nav: Providers
network: true
overview: 'Hootsuite publishes 4 APIs on the [APIs.io](https://apis.io/) network, including REST API, Analytics REST API, Inbox 2.0 API, and 1 more. Tagged areas include Social Media, Social Media Management, Marketing, Content Scheduling, and Analytics.


  The Hootsuite catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Hootsuite''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, signup flow, pricing, and 36 more developer resources.'
plans:
- name: Hootsuite Plans Pricing
  plan_count: 4
  slug: hootsuite-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 2
  name: Hootsuite Rate Limits
  slug: hootsuite-rate-limits
scopes:
- name: Hootsuite Scopes
  scope_count: 2
  slug: hootsuite-scopes
  summary_line: 2 scopes · authorizationCode/clientCredentials
score:
  band: strong
  composite: 63.6
  delta: -8.0
  facets:
    access_clarity: 77.6
    commercial_clarity: 77.6
    contract_governance: 16.7
    contract_quality: 69.6
    developer_ergonomics: 49.4
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 81.6
  previous_composite: 71.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 75.0
      derived: 0
      marker_coverage: 100.0
      total: 4
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/hootsuite/refs/heads/main/screenshots/hootsuite-2026-06-20T182835.png
security:
- kind: authentication
  name: Hootsuite Authentication
  slug: hootsuite-authentication
  summary_line: oauth2/http/apiKey · 6 schemes
- kind: domain-security
  name: Hootsuite Domain Security
  slug: hootsuite-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Hootsuite Vulnerability Disclosure
  slug: hootsuite-vulnerability-disclosure
  summary_line: Hackerone · security.txt
slug: hootsuite
tags:
- Social Media
- Social Media Management
- Marketing
- Content Scheduling
- Analytics
- Engagement
- Social Listening
- Employee Advocacy
- Customer Service
- SCIM
- OAuth 2.0
- Webhooks
website: https://www.hootsuite.com
---
