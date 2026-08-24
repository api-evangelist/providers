---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: na
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.4
  scored_at: '2026-08-24'
api_count: 2
apis:
- description: The Llms Full.txt API from Bounti — 1 operation(s) for llms full.txt.
  name: Bounti Llms Full.txt API
  slug: bounti-llms-full-txt-api
- description: The Llms.txt API from Bounti — 1 operation(s) for llms.txt.
  name: Bounti Llms.txt API
  slug: bounti-llms-txt-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Bounti.ai Content Llms Full.txt API
  slug: open-bounti-llms-full-txt-api
- collection_type: open
  name: Bounti.ai Content Llms Full.txt Llms.txt API
  slug: open-bounti-llms-txt-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/bounti-content-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://bounti.ai/
- group: company
  title: ''
  type: About
  url: https://bounti.ai/about
- group: company
  title: ''
  type: Blog
  url: https://bounti.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://bounti.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://claw.bounti.ai/sign-up
- group: start
  title: ''
  type: Login
  url: https://re.bounti.ai/real-estate/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bounti.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bounti.ai/privacy-policy
- group: operate
  title: ''
  type: Support
  url: mailto:support@bounti.ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bounti-ai
- group: agent
  title: ''
  type: WellKnown
  url: well-known/bounti-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bounti-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/bounti-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bounti-domain-security.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/bounti-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bounti-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/bounti-vulnerability-disclosure.yml
- group: build
  title: ''
  type: Packages
  url: packages/bounti-packages.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/bounti-tool-crosswalk.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bounti-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bounti-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bounti-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bounti-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bounti-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/bounti-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bounti-rate-limits.yml
created: '2026-07-17'
description: Bounti (Bounti Labs, bounti.ai) is an AI-powered real estate visualization and automation platform founded in 2023 by Ashar Rizqi and Matt Cooley and backed by GV (Google Ventures), Bloomberg Beta, Floodgate, Haystack, Octave Ventures and MS&AD. Its products include AI virtual staging and photo enhancement, cinematic listing-photo animation, automated marketing-video creation, before/after reveal videos, collaborative client studios, and B.Claw — an AI operating system that consolidates 13+ real estate tools (Gmail, calendar, CRM, WhatsApp, website builder) into one conversational interface. Bounti does not publish a general integration API, but it does expose an agent-facing, unauthenticated Content API (advertised via an AI-plugin manifest at /.well-known/ai-plugin.json, alongside an MCP discovery manifest at /.well-known/mcp.json) plus /llms.txt and /llms-full.txt so AI assistants can accurately answer questions about its products, pricing, and content. Bounti also publishes
  a catalog of 303 named B.Claw skills as machine-readable schema.org SoftwareApplication definitions at bounti.ai/skills, and 34 connector listings at bounti.ai/integrations — but those skills execute only inside the authenticated B.Claw product, whose API at claw.bounti.ai/api has no published contract.
image: https://bounti.ai/favicon.png
layout: provider
mcp_servers:
- description: ''
  name: Bounti MCP Server
  slug: bounti-mcp-server
modified: '2026-08-14'
name: Bounti
nav: Providers
network: true
overview: 'Bounti publishes 2 APIs on the [APIs.io](https://apis.io/) network: Llms Full.txt API and Llms.txt API. Tagged areas include Company, Real-Estate, Artificial Intelligence, Marketing, and Sales Enablement.


  Bounti''s developer surface includes engineering blog, pricing, signup flow, support, authentication, and 23 more developer resources.'
plans:
- name: Bounti Plans Pricing
  plan_count: 5
  slug: bounti-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Bounti Rate Limits
  slug: bounti-rate-limits
score:
  band: developing
  composite: 43.3
  delta: 0.0
  facets:
    access_clarity: 69.7
    commercial_clarity: 69.7
    contract_governance: 16.7
    contract_quality: 48.3
    developer_ergonomics: 26.2
    discoverability: 87.0
    governance: 16.7
    operational_transparency: 10.5
  previous_composite: 43.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: first-party
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bounti/refs/heads/main/screenshots/bounti-2026-07-25T203646.png
security:
- kind: authentication
  name: Bounti Authentication
  slug: bounti-authentication
  summary_line: none · 1 scheme
- kind: domain-security
  name: Bounti Domain Security
  slug: bounti-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bounti Vulnerability Disclosure
  slug: bounti-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: bounti
tags:
- Company
- Real-Estate
- Artificial Intelligence
- Marketing
- Sales Enablement
- Virtual Staging
- Content Generation
- AI Agents
website: https://bounti.ai/
---
