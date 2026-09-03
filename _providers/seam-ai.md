---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: paid
  public: false
  source:
  - https://www.getseam.ai/pricing
  - https://www.getseam.ai/get-started
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.9
  scored_at: '2026-09-03'
api_count: 1
apis:
- baseURL: https://enricher.getseam.ai
  baseurl_source: declared
  description: The Completions API from Seam AI — 1 operation(s) for completions.
  name: Seam AI Completions API
  slug: seam-ai-completions-api
artifact_total: 6
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/seam-ai-enrichment-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.getseam.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.getseam.ai/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.getseam.ai/onboarding/getting-started/overview
- group: operate
  title: ''
  type: Support
  url: mailto:support@getseam.ai
- group: company
  title: ''
  type: Blog
  url: https://www.getseam.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.getseam.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.getseam.ai/get-started
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.getseam.ai/legal/master-services-agreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.getseam.ai/legal/privacy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/seam-ai-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/seam-ai-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/seam-ai-tool-crosswalk.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/seam-ai-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/seam-ai-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/seam-ai-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/seam-ai-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/seam-ai-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/seam-ai-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/seam-ai-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/seam-ai-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/seam-ai-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/seam-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/seam-ai-rate-limits.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/seam-ai-domain-security.yml
created: '2026-07-17'
description: Seam AI (legal entity Talkmore Inc.) is an AI-native account-based marketing (ABM) platform that uses AI agents to score accounts against an ICP, monitor first- and third-party buying signals, prospect and enrich contacts, and execute multi-channel outbound plays into Salesforce, HubSpot, Outreach, Salesloft, Marketo, LinkedIn Ads and the customer data warehouse. Backed by Bessemer Venture Partners, the company has been acquired and is merging its product into Clarify as "Clarify Signals"; the getseam.ai marketing site now serves an acquisition notice. The developer surface remains live at docs.getseam.ai, which publishes an OpenAPI 3.1.0 contract for the Seam AI Enrichment API, an llms.txt index, an anonymous Model Context Protocol server, an A2A agent card, and a provider-authored Agent Skill. The API host named in that spec (enricher.getseam.ai) no longer resolves in DNS.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/seam-ai.png
layout: provider
mcp_servers:
- description: 'Seam AI runs a remote, anonymous Model Context Protocol server on its documentation host. It is a documentation-search server (the Mintlify docs MCP surface), not a server over the Seam product API: t'
  name: Seam AI
  slug: seam-ai
modified: '2026-08-13'
name: Seam AI
nav: Providers
network: true
overview: 'Seam AI publishes 1 API on the [APIs.io](https://apis.io/) network: Completions API. Tagged areas include Company, Ai Ml, Account Based Marketing, Sales Intelligence, and Marketing.


  Seam AI''s developer surface includes documentation, getting-started guide, support, engineering blog, pricing, signup flow, authentication, and 19 more developer resources.'
plans:
- name: Seam Ai Plans Pricing
  plan_count: 3
  slug: seam-ai-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Seam Ai Rate Limits
  slug: seam-ai-rate-limits
score:
  band: developing
  composite: 50.1
  coverage:
    artifact_dirs: 18
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 55.8
    developer_ergonomics: 47.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 50.1
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/seam-ai/refs/heads/main/screenshots/seam-ai-2026-08-17T081740.png
security:
- kind: authentication
  name: Seam Ai Authentication
  slug: seam-ai-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Seam Ai Domain Security
  slug: seam-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: seam-ai
tags:
- Company
- Ai Ml
- Account Based Marketing
- Sales Intelligence
- Marketing
- AI Agents
- CRM
- Data Enrichment
- Intent Data
- Sales Automation
website: https://www.getseam.ai/
---
