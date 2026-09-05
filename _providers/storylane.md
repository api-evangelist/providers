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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
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
  score: 42.1
  scored_at: '2026-09-04'
api_count: 4
apis:
- description: 'The Storylane External API allows Enterprise plan customers to programmatically list published demos, retrieve demo details including chapters and steps, manage demo links, create new shareable links '
  name: Storylane External API
  slug: storylane-external-api
- description: Storylane's first-party hosted Model Context Protocol server, the widest programmatic surface the company operates. It exposes 22 documented tools covering demo analytics, engaged accounts and capture
  name: Storylane MCP Server
  slug: storylane-mcp
- description: 'A public, unauthenticated oEmbed 1.0 provider endpoint that resolves any Storylane demo share URL into a rich embed response containing the demo title, provider metadata, a preview thumbnail, and the '
  name: Storylane oEmbed API
  slug: storylane-oembed-api
- description: Storylane's event surface, in two channels. Outbound HTTPS webhooks deliver completed demo sessions to a customer endpoint, signed with a base64 HMAC-SHA256 of the raw body in an x-storylane-signature
  name: Storylane Webhooks and Demo Events
  slug: storylane-webhooks
artifact_total: 14
asyncapis:
- description: ''
  name: Storylane Webhooks
  slug: storylane-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/storylane-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/storylane-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.storylane.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.storylane.io
- group: company
  title: ''
  type: Blog
  url: https://www.storylane.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.storylane.io/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.storylane.io
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/storylane-io
- group: other
  title: ''
  type: X
  url: https://x.com/storylaneio
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/storylane
- group: commercial
  title: ''
  type: Plans
  url: plans/storylane-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/storylane-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/storylane-finops.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/storylane-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/storylane-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/storylane-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/storylane-well-known.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/storylane-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/storylane-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/storylane-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/storylane-trust-center.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/storylane-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/storylane-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/storylane-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/storylane-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/storylane-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/storylane-webhooks.yml
- group: design
  title: ''
  type: Components
  url: components/storylane-components.yml
- group: build
  title: ''
  type: Packages
  url: packages/storylane-packages.yml
- group: docs
  title: ''
  type: APIReference
  url: https://docs.storylane.io/integrations/integrations-and-data-flow/external-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.storylane.io/welcome-to-storylane
- group: operate
  title: ''
  type: HelpCenter
  url: https://docs.storylane.io
- group: operate
  title: ''
  type: Support
  url: mailto:support@storylane.io
- group: operate
  title: ''
  type: ChangeLogURL
  url: https://docs.storylane.io/changelog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.storylane.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.storylane.io/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://app.storylane.io/register
- group: start
  title: ''
  type: Login
  url: https://app.storylane.io/login
- group: auth
  title: ''
  type: TrustCenterURL
  url: https://trust.storylane.io/
created: '2026-06-13'
description: Storylane is an interactive demo platform that enables sales and marketing teams to build and share self-serve product walkthroughs, embedded demos, and demo galleries without engineering involvement. The platform offers an External REST API for Enterprise customers to programmatically manage published demos, generate secure shareable links with passcodes and expiration dates, and personalize demo experiences via email parameters. Storylane also provides webhooks, cross-frame events, and 30-plus native integrations with CRM, marketing automation, and analytics tools to connect demo engagement data with existing GTM workflows. Its widest programmatic surface is not REST but a first-party hosted Model Context Protocol server at identity.storylane.io/mcp, secured with OAuth 2.0 dynamic client registration and PKCE, exposing 22 documented tools for demo creation from media, AI personalization, publishing, hubs, voices, analytics, leads and accounts to Claude, ChatGPT and other MCP
  clients.
finops:
- name: Storylane Finops
  service_category: ''
  slug: storylane-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/storylane.png
jsonld:
- class_count: 0
  name: Storylane Context
  property_count: 0
  slug: storylane-context
layout: provider
mcp_servers:
- description: Storylane operates a first-party hosted (remote) Model Context Protocol server that exposes the demo library, analytics, lead and link surface to MCP-capable AI clients. The server is documented publi
  name: Storylane MCP
  slug: storylane-mcp
modified: '2026-08-13'
name: Storylane
nav: Providers
network: true
overview: 'Storylane publishes 1 API on the [APIs.io](https://apis.io/) network: External API. Tagged areas include Interactive Demos, Product Walkthroughs, Sales Enablement, Marketing, and Demo Analytics.


  The Storylane catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 JSON-LD context.


  Storylane''s developer surface includes documentation, engineering blog, pricing, authentication, changelog, API reference, getting-started guide, and 33 more developer resources.'
plans:
- name: Storylane Plans Pricing
  plan_count: 8
  slug: storylane-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 8
  name: Storylane Rate Limits
  slug: storylane-rate-limits
scopes:
- name: Storylane Scopes
  scope_count: 0
  slug: storylane-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 62.1
  coverage:
    artifact_dirs: 22
    catalog_earned: 72.0
    catalog_earned_first_party: 24.0
    catalog_gap: 43.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.3
  facets:
    access_clarity: 93.4
    commercial_clarity: 93.4
    contract_governance: 18.2
    contract_quality: 53.2
    developer_ergonomics: 49.4
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 76.3
  previous_composite: 60.8
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/storylane/refs/heads/main/screenshots/storylane-2026-06-20T194611.png
security:
- kind: authentication
  name: Storylane Authentication
  slug: storylane-authentication
  summary_line: 5 schemes
- kind: domain-security
  name: Storylane Domain Security
  slug: storylane-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Storylane Trust Center
  slug: storylane-trust-center
  summary_line: SOC 2 Type 2, GDPR
slug: storylane
tags:
- Interactive Demos
- Product Walkthroughs
- Sales Enablement
- Marketing
- Demo Analytics
- Demo Automation
- Buyer Hub
- Sales
- MCP
- Agent Tools
- Webhook
- Embeds
- oEmbed
- Demo Automation Platform
website: https://www.storylane.io
---
