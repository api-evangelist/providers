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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.8
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: The contacts API from Hatch — 1 operation(s) for contacts.
  name: Hatch contacts API
  slug: hatch-contacts-api
artifact_total: 8
asyncapis:
- description: ''
  name: Hatch Webhooks
  slug: hatch-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Hatch contacts API
  slug: open-hatch-contacts-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/hatch-mcp.yml
- group: company
  title: ''
  type: Website
  url: https://www.usehatchapp.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.usehatchapp.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.usehatchapp.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.usehatchapp.com/integrations/hatch-api/hatch-api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.usehatchapp.com/getting-started/intro-to-hatch/what-is-hatch
- group: operate
  title: ''
  type: Support
  url: https://docs.usehatchapp.com/
- group: company
  title: ''
  type: Blog
  url: https://www.usehatchapp.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.usehatchapp.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.usehatchapp.com/
- group: start
  title: ''
  type: Login
  url: https://app.usehatchapp.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.usehatchapp.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.usehatchapp.com/legal/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.usehatchapp.com
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/hatch-openapi-original.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/hatch-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hatch-problem-types.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/hatch-openapi-overlay.yaml
- group: design
  title: ''
  type: Conventions
  url: conventions/hatch-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hatch-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hatch-rate-limits.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/hatch-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hatch-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/hatch-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hatch-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hatch-llms.txt
created: '2026-07-17'
description: Hatch is an AI-powered customer communication platform for service businesses, unifying voice, SMS, and email into a single system with custom AI agents (AI CSRs) that text and call leads and customers to qualify them, book appointments, and drive bottom-line growth without adding headcount. Products include Voice AI, Messaging AI, Journey Builder for multi-channel campaigns, a Knowledge Engine, and a Command Center for performance tracking. For developers, Hatch exposes a public REST API (bearer-token auth) whose primary operation upserts contacts into campaigns, a Bulk Export API for BI/analytics, and an outbound webhook surface (11 event types, EdDSA-signed) for pushing events to downstream systems and Zapier. Backed by Bessemer Venture Partners and True Ventures. Added to the API Evangelist network and enriched from the provider's own public developer surface.
image: https://cdn.prod.website-files.com/6979136a27d403634304b470/69c2be9beb7874c215169569_hatch-homepage-og-image.png
layout: provider
mcp_servers:
- description: ''
  name: hatch-mcp.yml
  slug: hatch-mcpyml
modified: '2026-07-19'
name: Hatch
nav: Providers
network: true
overview: 'Hatch publishes 1 API on the [APIs.io](https://apis.io/) network: contacts API. Tagged areas include Company, Vertical Software, Customer Communication, Conversational AI, and SMS.


  The Hatch catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Hatch''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 20 more developer resources.'
random_paper: 73
rate_limits:
- limit_count: 1
  name: Hatch Rate Limits
  slug: hatch-rate-limits
score:
  band: developing
  composite: 49.2
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 67.2
    developer_ergonomics: 56.0
    discoverability: 75.9
    governance: 11.5
    operational_transparency: 44.7
  previous_composite: 49.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 34.7
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hatch/refs/heads/main/screenshots/hatch-2026-07-25T220750.png
security:
- kind: authentication
  name: Hatch Authentication
  slug: hatch-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Hatch Domain Security
  slug: hatch-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hatch
tags:
- Company
- Vertical Software
- Customer Communication
- Conversational AI
- SMS
- Voice
- Email
- Marketing
- Home Services
- Contact Center
website: https://www.usehatchapp.com/
---
