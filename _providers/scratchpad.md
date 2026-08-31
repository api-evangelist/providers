---
access_model:
  confidence: high
  label: Free tier, self-service sign-up
  onboarding: unknown
  pricing: freemium
  public: true
  source:
  - https://www.scratchpad.com/pricing
  - https://clearskies.cc/pricing
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 27.6
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: The Clearskies Customer Context Graph exposed as a single remote Model Context Protocol server. Connected AI clients (Claude, ChatGPT, Cursor, n8n, Retool) query unified, identity-resolved customer co
  name: Clearskies MCP Server
  slug: clearskies-mcp-server
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://www.scratchpad.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.scratchpad.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.scratchpad.com/blog
- group: operate
  title: ''
  type: Support
  url: https://help.scratchpad.com/en/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.scratchpad.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.scratchpad.com/legal/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.scratchpad.com/
- group: auth
  title: ''
  type: Security
  url: https://www.scratchpad.com/security
- group: auth
  title: ''
  type: Compliance
  url: https://www.scratchpad.com/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/scratchpad-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/scratchpad-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/scratchpad-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://clearskies.cc/docs
- group: docs
  title: ''
  type: Documentation
  url: https://clearskies.cc/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://clearskies.cc/docs/getting-started/quick-start
- group: start
  title: ''
  type: SignUp
  url: https://app.clearskies.cc/login
- group: agent
  title: ''
  type: MCPServer
  url: mcp/scratchpad-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/scratchpad-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/scratchpad-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/scratchpad-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/scratchpad-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/scratchpad-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/scratchpad-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/scratchpad-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/scratchpad-plans-pricing.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/scratchpad-sandbox.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/scratchpad-llms.txt
created: '2026-07-17'
description: Scratchpad is an AI-powered workspace for sales teams that sits on top of Salesforce, reducing the friction of keeping the CRM up to date. Reps manage notes, opportunities, tasks, and pipeline from a fast, lightweight interface that syncs everything back to Salesforce, with AI-native sheets and Kanban boards, an AI notetaker and call recorder, automated field updates, executive summaries, and CRM hygiene monitoring. The product connects to Salesforce via API and inherits its permissions and guardrails, and integrates with Slack, Zoom, and Gong. Founded in 2019 by Pouyan Salehi and Cyrus Karbassiyoon in San Francisco, and backed by Accel and Craft Ventures. Scratchpad publishes no REST API for its own Salesforce-native workspace, but the same company ships Clearskies (clearskies.cc), a Customer Context Graph delivered as a single remote MCP server at https://mcp.clearskies.cc/mcp, OAuth-protected with dynamic client registration and PKCE, that unifies Salesforce, HubSpot, Gong,
  Scratchpad, Gmail/Outlook, calendars, Slack, Linear, Jira and Pylon behind one endpoint for Claude, ChatGPT, Cursor, n8n and Retool. This profile captures Scratchpad identity, its commercial surface, its agent surface, and its security posture.
image: https://cdn.prod.website-files.com/5ec58e445ff9859286816f53/689655f9a5b2bc821c89f95e_Scratchpad%20-%20The%20AI%20workspace%20for%20sellers.png
layout: provider
mcp_servers:
- description: ''
  name: Clearskies
  slug: clearskies
modified: '2026-08-13'
name: Scratchpad
nav: Providers
network: true
overview: 'Scratchpad publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Productivity, Sales, CRM, and Salesforce.


  Scratchpad''s developer surface includes pricing, engineering blog, support, documentation, getting-started guide, signup flow, authentication, and 20 more developer resources.'
plans:
- name: Scratchpad Plans Pricing
  plan_count: 0
  slug: scratchpad-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Scratchpad Rate Limits
  slug: scratchpad-rate-limits
scopes:
- name: Scratchpad Scopes
  scope_count: 3
  slug: scratchpad-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: thin
  composite: 34.1
  coverage:
    artifact_dirs: 15
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 57.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 34.1
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Scratchpad Authentication
  slug: scratchpad-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Scratchpad Domain Security
  slug: scratchpad-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Scratchpad Vulnerability Disclosure
  slug: scratchpad-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Scratchpad Trust Center
  slug: scratchpad-trust-center
  summary_line: SOC 2, GDPR
slug: scratchpad
tags:
- Company
- Productivity
- Sales
- CRM
- Salesforce
- Revenue Operations
- Artificial Intelligence
- Software-as-a-Service
- MCP
- Agents
- Sales Intelligence
website: https://www.scratchpad.com
---
