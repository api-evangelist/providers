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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.2
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Bulk (1-to-many) SMS. Small batches dispatch inline; >30 recipients queue asynchronously.
  name: Crescendo Lab Broadcast API
  slug: crescendo-lab-broadcast-api
- description: Address book with NCC-consent tracking.
  name: Crescendo Lab Contacts API
  slug: crescendo-lab-contacts-api
- description: Transactional (1-to-1) SMS send + status.
  name: Crescendo Lab SMS API
  slug: crescendo-lab-sms-api
- description: Cost-attribution teams. Tag sends with a team to see which team sent/spent how much (shared wallet — reporting only, not a wallet split).
  name: Crescendo Lab Teams API
  slug: crescendo-lab-teams-api
- description: The MAAC Go API API from Crescendo Lab — 0 operation(s) for maac go api.
  name: Crescendo Lab MAAC Go API
  slug: crescendo-lab-maac-go-api-api
artifact_total: 16
asyncapis:
- description: ''
  name: Crescendo Lab Maacgo Webhooks
  slug: crescendo-lab-maacgo-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: MAAC Go Broadcast API
  slug: open-crescendo-lab-broadcast-api
- collection_type: open
  name: MAAC Go Broadcast Contacts API
  slug: open-crescendo-lab-contacts-api
- collection_type: open
  name: MAAC Go Broadcast SMS API
  slug: open-crescendo-lab-sms-api
- collection_type: open
  name: MAAC Go Broadcast Teams API
  slug: open-crescendo-lab-teams-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/crescendo-lab-maacgo-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://cresclab.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://sms.cresclab.com/developers.html
- group: docs
  title: ''
  type: Documentation
  url: https://sms.cresclab.com/developers.html#api
- group: company
  title: ''
  type: Blog
  url: https://blog.cresclab.com/zh-tw
- group: operate
  title: ''
  type: HelpCenter
  url: https://crescendolab.zendesk.com/hc/zh-tw
- group: commercial
  title: ''
  type: Pricing
  url: https://cresclab.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://sms.cresclab.com/signup.html
- group: start
  title: ''
  type: Login
  url: https://sms.cresclab.com/app.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sms.cresclab.com/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sms.cresclab.com/privacy.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Crescendo-Lab
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/crescendo-lab-llms.txt
- group: build
  title: ''
  type: SDKs
  url: packages/crescendo-lab-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/crescendo-lab-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/crescendo-lab-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/crescendo-lab-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/crescendo-lab-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/crescendo-lab-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/crescendo-lab-rate-limits.yml
- group: docs
  title: ''
  type: APIReference
  url: https://sms.cresclab.com/openapi.yaml
- group: start
  title: ''
  type: GettingStarted
  url: https://sms.cresclab.com/developers.html
- group: start
  title: ''
  type: Sandbox
  url: sandbox/crescendo-lab-sandbox.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/crescendo-lab-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/crescendo-lab-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/crescendo-lab-conventions.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/crescendo-lab-domain-security.yml
created: '2026-07-17'
description: Crescendo Lab is a Taiwan-based, Asia-leading AI omnichannel customer communication software company (cresclab.com) serving 800+ global brands, and a LINE Biz-Solutions Gold Partner. Its platform spans MAAC (AI marketing automation), CAAC (conversational applications), and DAAC (data intelligence) across LINE, WhatsApp, SMS, email, and social channels. Its developer-facing surface is MAAC Go (sms.cresclab.com) — a self-serve, NCC-compliant Taiwan SMS API with a published OpenAPI spec, first-party Node/Python SDKs, a CLI, an official MCP server, and delivery webhooks. Surfaced as a 500 Global portfolio company and enriched into the API Evangelist network.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/crescendo-lab.png
layout: provider
mcp_servers:
- description: Official hosted + local MCP server for MAAC Go (Crescendo Lab's self-serve Taiwan SMS platform). Lets Claude / Cursor / Windsurf / Codex send SMS, run broadcasts, pull logs, and check wallet balance o
  name: MAAC Go MCP
  slug: maac-go-mcp
modified: '2026-08-13'
name: Crescendo Lab
nav: Providers
network: true
overview: 'Crescendo Lab publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Broadcast API, Contacts API, SMS API, and 2 more. Tagged areas include Company, SMS, Messaging, Marketing Automation, and Customer Engagement.


  The Crescendo Lab catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Crescendo Lab''s developer surface includes documentation, engineering blog, pricing, signup flow, CLI, API reference, getting-started guide, and 21 more developer resources.'
plans:
- name: Crescendo Lab Plans Pricing
  plan_count: 8
  slug: crescendo-lab-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 2
  name: Crescendo Lab Rate Limits
  slug: crescendo-lab-rate-limits
score:
  band: strong
  composite: 58.3
  coverage:
    artifact_dirs: 24
    catalog_gap: 58.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 4.5
    contract_quality: 55.6
    developer_ergonomics: 80.4
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 31.6
  previous_composite: 58.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 34.7
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/crescendo-lab/refs/heads/main/screenshots/crescendo-lab-2026-07-25T210727.png
security:
- kind: authentication
  name: Crescendo Lab Authentication
  slug: crescendo-lab-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Crescendo Lab Domain Security
  slug: crescendo-lab-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: crescendo-lab
tags:
- Company
- SMS
- Messaging
- Marketing Automation
- Customer Engagement
- Taiwan
- Omnichannel
- MCP
website: https://cresclab.com
---
