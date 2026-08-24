---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.8
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Facebook Lead Ads Agentic Access
  operation_count: 9
  slug: facebook-lead-ads-agentic-access
  summary_line: 9 operations · 3 acting
api_count: 7
apis:
- description: Graph API endpoints for managing Facebook and Instagram lead generation forms, retrieving captured leads, exporting bulk lead data, and subscribing to leadgen webhooks. Authentication uses Page access
  name: Meta Marketing API - Lead Ads
  slug: graph-api
- description: The Bulk Leads API from Facebook Lead Ads — 1 operation(s) for bulk leads.
  name: Facebook Lead Ads Bulk Leads API
  slug: facebook-lead-ads-bulk-leads-api
- description: The Leadgen Forms API from Facebook Lead Ads — 1 operation(s) for leadgen forms.
  name: Facebook Lead Ads Leadgen Forms API
  slug: facebook-lead-ads-leadgen-forms-api
- description: The Leads API from Facebook Lead Ads — 2 operation(s) for leads.
  name: Facebook Lead Ads Leads API
  slug: facebook-lead-ads-leads-api
- description: The Meta Marketing API Lead Ads API from Facebook Lead Ads — 2 operation(s) for meta marketing api lead ads.
  name: Facebook Lead Ads Meta Marketing API Lead Ads API
  slug: facebook-lead-ads-meta-marketing-api-lead-ads-api
- description: The Subscribed Apps API from Facebook Lead Ads — 1 operation(s) for subscribed apps.
  name: Facebook Lead Ads Subscribed Apps API
  slug: facebook-lead-ads-subscribed-apps-api
- description: The Subscriptions API from Facebook Lead Ads — 1 operation(s) for subscriptions.
  name: Facebook Lead Ads Subscriptions API
  slug: facebook-lead-ads-subscriptions-api
artifact_total: 24
asyncapis:
- description: ''
  name: Facebook Lead Ads Webhooks
  slug: facebook-lead-ads-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Meta Marketing API - Lead Ads Bulk Leads API
  slug: open-facebook-lead-ads-bulk-leads-api
- collection_type: open
  name: Meta Marketing API - Lead Ads Bulk Leads Leadgen Forms API
  slug: open-facebook-lead-ads-leadgen-forms-api
- collection_type: open
  name: Meta Marketing API - Lead Ads Bulk Leads API
  slug: open-facebook-lead-ads-leads-api
- collection_type: open
  name: Meta Marketing API - Lead Ads Bulk Leads Meta Marketing API Lead Ads API
  slug: open-facebook-lead-ads-meta-marketing-api-lead-ads-api
- collection_type: open
  name: Meta Marketing API - Lead Ads Bulk Leads Subscribed Apps API
  slug: open-facebook-lead-ads-subscribed-apps-api
- collection_type: open
  name: Meta Marketing API - Lead Ads Bulk Leads Subscriptions API
  slug: open-facebook-lead-ads-subscriptions-api
- collection_type: open
  name: Meta Marketing API - Lead Ads
  slug: open-facebook-lead-ads
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/facebook-lead-ads-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/facebook-lead-ads-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/facebook-lead-ads-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.facebook.com/business/ads/lead-ads
- group: docs
  title: ''
  type: Documentation
  url: https://developers.facebook.com/docs/marketing-api/guides/lead-ads/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.facebook.com
- group: other
  title: ''
  type: Marketing API
  url: https://developers.facebook.com/docs/marketing-api/
- group: start
  title: ''
  type: SignUp
  url: https://developers.facebook.com/async/registration/
- group: other
  title: ''
  type: App Dashboard
  url: https://developers.facebook.com/apps/
- group: operate
  title: ''
  type: Support
  url: https://developers.facebook.com/support/
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.facebook.com/llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/facebook-lead-ads-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/facebook-lead-ads-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/facebook-lead-ads-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/facebook-lead-ads-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/facebook-lead-ads-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/facebook-lead-ads-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/facebook-lead-ads-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/facebook-lead-ads-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/facebook-lead-ads-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://metastatus.com/marketing-api
- group: operate
  title: ''
  type: Deprecation
  url: https://developers.facebook.com/docs/graph-api/guides/versioning
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/facebook-lead-ads-changelog.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/facebook-lead-ads-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/facebook-lead-ads-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://bugbounty.meta.com/
- group: start
  title: ''
  type: Sandbox
  url: sandbox/facebook-lead-ads-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/facebook-lead-ads-conventions.yml
- group: build
  title: ''
  type: CLI
  url: cli/facebook-lead-ads-cli.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/facebook-lead-ads-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/facebook-lead-ads-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/facebook-lead-ads-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/facebook-lead-ads-plans-pricing.yml
- group: docs
  title: ''
  type: APIReference
  url: https://developers.facebook.com/docs/marketing-api/reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.facebook.com/docs/marketing-api/get-started
- group: company
  title: ''
  type: Blog
  url: https://developers.facebook.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/facebook
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.facebook.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.facebook.com/privacy/policy/
created: '2026-05-11'
description: Facebook Lead Ads (part of the Meta Marketing API) lets advertisers create instant lead-generation forms on Facebook and Instagram and programmatically retrieve the leads captured through those forms. Through the Meta Graph API developers can list lead generation forms on a Page, read submitted leads, download bulk lead exports, and subscribe to webhooks for real-time lead delivery. Authentication uses Page access tokens issued via Facebook Login / Meta Business Login with the leads_retrieval, pages_show_list, and pages_manage_ads permissions.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/facebook-lead-ads.png
layout: provider
mcp_servers:
- description: ''
  name: Meta Ads MCP Server
  slug: meta-ads-mcp-server
modified: '2026-08-14'
name: Facebook Lead Ads
nav: Providers
network: true
overview: 'Facebook Lead Ads publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Bulk Leads API, Leadgen Forms API, Leads API, and 3 more. Tagged areas include Advertising, Lead Generation, Lead Ads, Marketing API, and Facebook.


  The Facebook Lead Ads catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Facebook Lead Ads'' developer surface includes authentication, documentation, signup flow, support, changelog, sandbox, CLI, and 33 more developer resources.'
plans:
- name: Facebook Lead Ads Plans Pricing
  plan_count: 0
  slug: facebook-lead-ads-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 10
  name: Facebook Lead Ads Rate Limits
  slug: facebook-lead-ads-rate-limits
scopes:
- name: Facebook Lead Ads Scopes
  scope_count: 6
  slug: facebook-lead-ads-scopes
  summary_line: 6 scopes · authorizationCode
score:
  band: strong
  composite: 56.3
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 16.7
    contract_quality: 60.1
    developer_ergonomics: 76.8
    discoverability: 92.6
    governance: 16.7
    operational_transparency: 76.3
  previous_composite: 56.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/facebook-lead-ads/refs/heads/main/screenshots/facebook-lead-ads-2026-06-20T181004.png
security:
- kind: authentication
  name: Facebook Lead Ads Authentication
  slug: facebook-lead-ads-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Facebook Lead Ads Domain Security
  slug: facebook-lead-ads-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Facebook Lead Ads Vulnerability Disclosure
  slug: facebook-lead-ads-vulnerability-disclosure
  summary_line: Hackerone
slug: facebook-lead-ads
tags:
- Advertising
- Lead Generation
- Lead Ads
- Marketing API
- Facebook
- Instagram
- Meta
- Webhook
website: https://www.facebook.com/business/ads/lead-ads
---
