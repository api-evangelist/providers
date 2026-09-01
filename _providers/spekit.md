---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 50.0
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Spekit Agentic Access
  operation_count: 5
  slug: spekit-agentic-access
  summary_line: 5 operations
api_count: 2
apis:
- description: The Searches API from Spekit — 1 operation(s) for searches.
  name: Spekit Searches API
  slug: spekit-searches-api
- description: The Spek Reactions API from Spekit — 1 operation(s) for spek reactions.
  name: Spekit Spek Reactions API
  slug: spekit-spek-reactions-api
- description: The Spek Views API from Spekit — 1 operation(s) for spek views.
  name: Spekit Spek Views API
  slug: spekit-spek-views-api
- description: The User Activities API from Spekit — 1 operation(s) for user activities.
  name: Spekit User Activities API
  slug: spekit-user-activities-api
- description: The Users API from Spekit — 1 operation(s) for users.
  name: Spekit Users API
  slug: spekit-users-api
artifact_total: 14
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/spekit-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/spekit-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://spekit.com
- group: agent
  title: ''
  type: MCPServer
  url: mcp/spekit-mcp.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/spekit-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.spekit.com
- group: design
  title: ''
  type: Conformance
  url: conformance/spekit-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.spekit.com/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/spekit-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spekit-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/spekit-llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.spekit.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.spekit.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.spekit.co/signup
- group: start
  title: ''
  type: Login
  url: https://app.spekit.co
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.spekit.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.spekit.com/legal/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.spekit.com/legal/msa
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/spekit-openapi.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/spekit-openapi-overlay.yaml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/spekit-tool-crosswalk.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/spekit-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/spekit-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/spekit-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/spekit-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/spekit-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/spekit-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/spekit-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/spekit-well-known.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/spekit-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.spekit.com/vulnerability-disclosure-program
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.spekit.co/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://help.spekit.com/hc/en-us/articles/31041891807643-Spekit-API-Overview
- group: docs
  title: ''
  type: APIReference
  url: https://api.spekit.co/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.spekit.com/hc/en-us/articles/53977808268699-Spekit-MCP-Overview-Setup
- group: operate
  title: ''
  type: Support
  url: https://help.spekit.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/spekit-co
- group: commercial
  title: ''
  type: License
  url: https://www.spekit.com/legal/api-license-agreement
- group: other
  title: ''
  type: AcceptableUsePolicy
  url: https://www.spekit.com/legal/spekit-acceptable-use-policy
- group: operate
  title: ''
  type: Contact
  url: https://www.spekit.com/contact
created: '2026-07-17'
description: 'Spekit is an AI-powered revenue enablement platform for B2B sales teams, delivering coaching, content, and deal intelligence inside rep workflows. Its GTM Knowledge Engine keeps governed go-to-market knowledge accurate and on-brand, pairs agentic coaching (the AI Sidekick) with unified deal context from Salesforce, Gong, and email, and generates personalized buyer experiences such as automated deal rooms. Spekit exposes its governed knowledge to AI agents over the Model Context Protocol (MCP) so any LLM or MCP-enabled tool always has the latest content. It is SOC 2 Type II audited and integrates across Salesforce, Slack, Gmail, Outlook, HubSpot, and major SSO providers. Spekit ships two independent programmatic surfaces that do not overlap: a read-only REST API at api.spekit.co, published as OpenAPI 3.0.3 and rendered in Swagger UI, returning users, searches, Spek views and reactions, and a 21-type activity feed for BI and enablement-ROI reporting; and a remote MCP connector
  at mcp.spekit.co/mcp with 19 read and write tools over governed content, secured by OAuth 2.0 authorization code with PKCE and dynamic client registration. Surfaced as a portfolio company of Craft Ventures, Felicis, and Foundry Group and enriched by the API Evangelist pipeline.'
image: https://cdn.prod.website-files.com/67928cf7ed419b596caac76b/6a307193f0dd93f6607b0971_OpenGraphImage_2026.jpg
layout: provider
mcp_servers:
- description: The Spekit MCP connector exposes governed Spekit GTM content — Speks, topics, templates, companies and Deal Rooms — to any AI tool that supports a custom MCP connector by URL with dynamic client regis
  name: Spekit MCP Server
  slug: spekit-mcp-server
modified: '2026-08-14'
name: Spekit
nav: Providers
network: true
overview: 'Spekit publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Searches API, Spek Reactions API, Spek Views API, and 2 more. Tagged areas include Company, Software-as-a-Service, Sales Enablement, Revenue Enablement, and Digital Adoption.


  Spekit''s developer surface includes authentication, engineering blog, pricing, signup flow, documentation, API reference, getting-started guide, and 34 more developer resources.'
plans:
- name: Spekit Plans Pricing
  plan_count: 0
  slug: spekit-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 1
  name: Spekit Rate Limits
  slug: spekit-rate-limits
scopes:
- name: Spekit Scopes
  scope_count: 4
  slug: spekit-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: developing
  composite: 51.5
  coverage:
    artifact_dirs: 21
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 18.2
    contract_quality: 50.7
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 50.0
  previous_composite: 51.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/spekit/refs/heads/main/screenshots/spekit-2026-08-17T082023.png
security:
- kind: authentication
  name: Spekit Authentication
  slug: spekit-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Spekit Domain Security
  slug: spekit-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Spekit Vulnerability Disclosure
  slug: spekit-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Spekit Trust Center
  slug: spekit-trust-center
  summary_line: SOC 2, ISO 27001
slug: spekit
tags:
- Company
- Software-as-a-Service
- Sales Enablement
- Revenue Enablement
- Digital Adoption
- Knowledge-Management
- MCP
- Artificial Intelligence
- Analytics
- Sales
- Content Management
- Agents
- Authentication
website: https://spekit.com
---
