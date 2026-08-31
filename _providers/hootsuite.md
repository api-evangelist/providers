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
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.3
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 39
  human_in_the_loop: 0
  name: Hootsuite Agentic Access
  operation_count: 76
  slug: hootsuite-agentic-access
  summary_line: 76 operations · 39 acting
api_count: 8
apis:
- description: A remote Model Context Protocol endpoint served from Hootsuite's own ReadMe-hosted developer documentation site. Reachable and real, but gated — initialize and tools/list both return HTTP 401 "Authori
  name: Hootsuite Developer Documentation MCP
  slug: mcp
- description: Hootsuite Analytics API
  name: Hootsuite Analytics API
  slug: hootsuite-analytics-api-api
- description: Hootsuite uses OAuth2 to authenticate end users. Members authenticated with the Hootsuite API are subject to the same permissions configured as when using the Hootsuite Web Dashboard. Learn more about
  name: Hootsuite Authentication API
  slug: hootsuite-authentication-api
- description: The Comments API from Hootsuite — 3 operation(s) for comments.
  name: Hootsuite Comments API
  slug: hootsuite-comments-api
- description: If you want to update contact attributes asynchronously, you'll need to call the Contact API. When calling the Contact API, the client needs to be authenticated. The [REST API authentication](#tag/res
  name: Hootsuite CRM Rest API
  slug: hootsuite-crm-rest-api-api
- description: '### Webhook authentication When receiving data from Inbox 2.0, we provide two authentication options. Both mechanisms are in place so that you can make sure the request originates from Inbox 2.0. ####'
  name: Hootsuite CRM Webhooks API
  slug: hootsuite-crm-webhooks-api
- description: Operations that you can do related with your authenticated member
  name: Hootsuite Me API
  slug: hootsuite-me-api
- description: The Media API from Hootsuite — 2 operation(s) for media.
  name: Hootsuite Media API
  slug: hootsuite-media-api
- description: The Members API from Hootsuite — 3 operation(s) for members.
  name: Hootsuite Members API
  slug: hootsuite-members-api
- description: The Messages API from Hootsuite — 5 operation(s) for messages.
  name: Hootsuite Messages API
  slug: hootsuite-messages-api
- description: The Organizations API from Hootsuite — 7 operation(s) for organizations.
  name: Hootsuite Organizations API
  slug: hootsuite-organizations-api
- description: When calling the Proactive Messaging API, the client needs to be authenticated. The [REST API authentication](#tag/rest-api-authentication) section contains more details on how to authenticate your cl
  name: Hootsuite Proactive Messaging Rest API
  slug: hootsuite-proactive-messaging-rest-api-api
- description: When calling the Queue API, the client needs to be authenticated. The [REST API authentication](#tag/rest-api-authentication) section contains more details on how to authenticate your client.
  name: Hootsuite Queue Rest API
  slug: hootsuite-queue-rest-api-api
- description: When calling the Real-time Metrics API, the client needs to be authenticated. The [REST API authentication](#tag/rest-api-authentication) section contains more details on how to authenticate your clie
  name: Hootsuite Real Time Metrics Rest API
  slug: hootsuite-real-time-metrics-rest-api-api
- description: 'Follow the steps below to make an authenticated API request. # 1. Request client credentials ### Step 1: Create your OAuth 2.0 app Follow [these steps](https://developer.hootsuite.com/docs/getting-sta'
  name: Hootsuite Rest API Authentication API
  slug: hootsuite-rest-api-authentication-api
- description: The SCIM 2.0 API from Hootsuite — 5 operation(s) for scim 2.0.
  name: Hootsuite SCIM 2.0 API
  slug: hootsuite-scim-2-0-api
- description: A social profile is a publishing channel on a social network account.
  name: Hootsuite Social Profiles API
  slug: hootsuite-social-profiles-api
- description: The Teams API from Hootsuite — 6 operation(s) for teams.
  name: Hootsuite Teams API
  slug: hootsuite-teams-api
- description: When calling the User Presence API, the client needs to be authenticated. The [REST API authentication](#tag/rest-api-authentication) section contains more details on how to authenticate your client.
  name: Hootsuite User Presence Rest API
  slug: hootsuite-user-presence-rest-api-api
- description: If you want to send the replies asynchronously or manipulate the conversation in your fulfillment code, you'll need to call the Virtual Agent REST API. The [REST API authentication](#tag/rest-api-auth
  name: Hootsuite Vai Rest API
  slug: hootsuite-vai-rest-api-api
- description: '### Webhook authentication When setting up a virtual agent, you received a secret key that you can use to verify whether an incoming webhook request really comes from Inbox 2.0 without alterations. In'
  name: Hootsuite Vai Webhooks API
  slug: hootsuite-vai-webhooks-api
artifact_total: 36
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
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/hootsuite-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/hootsuite-rest-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/hootsuite-analytics-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/hootsuite-inbox-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/hootsuite-amplify-api-overlay.yaml
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
- description: Hootsuite serves a remote Model Context Protocol endpoint from its own developer-documentation host at https://developer.hootsuite.com/mcp. A plain GET returns the plain-text banner "This URL can only
  name: Hootsuite Developer Documentation MCP
  slug: hootsuite-developer-documentation-mcp
modified: '2026-08-13'
name: Hootsuite
nav: Providers
network: true
overview: 'Hootsuite publishes 20 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, Authentication API, Comments API, and 17 more. Tagged areas include Social-Media, Social Media Management, Marketing, Content Scheduling, and Analytics.


  The Hootsuite catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Hootsuite''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, signup flow, pricing, and 41 more developer resources.'
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
  composite: 61.4
  coverage:
    artifact_dirs: 25
    catalog_gap: 58.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 1.9
  facets:
    access_clarity: 77.6
    commercial_clarity: 77.6
    contract_governance: 4.5
    contract_quality: 69.0
    developer_ergonomics: 49.4
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 81.6
  previous_composite: 59.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 4
    mcp: first-party
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
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
- Social-Media
- Social Media Management
- Marketing
- Content Scheduling
- Analytics
- Engagement
- Social Listening
- Employee Advocacy
- Customer Service
- SCIM
- Authentication
- Webhook
website: https://www.hootsuite.com
---
