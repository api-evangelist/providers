---
access_model:
  confidence: high
  label: Self-serve signup with a 30-day trial
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - https://knownwell.com/pricing/
  - https://knownwell.com/free-trial/
  - https://api.knownwell.com/ci/docs
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.5
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 2
  human_in_the_loop: 1
  name: Knownwell Agentic Access
  operation_count: 25
  slug: knownwell-agentic-access
  summary_line: 25 operations · 2 acting · 1 human-in-the-loop
api_count: 10
apis:
- description: The alignment API from Knownwell — 2 operation(s) for alignment. Returns the Red/Amber/Green alignment read a client team files by hand each week, alongside the machine-computed Knownwell score, so th
  name: Knownwell alignment API
  slug: knownwell-alignment-api
- description: The api-keys API from Knownwell — 2 operation(s) for api-keys.
  name: Knownwell api-keys API
  slug: knownwell-api-keys-api
- description: The clients API from Knownwell — 14 operation(s) for clients.
  name: Knownwell clients API
  slug: knownwell-clients-api
- description: The documentation API from Knownwell — 1 operation(s) for documentation.
  name: Knownwell documentation API
  slug: knownwell-documentation-api
- description: The health API from Knownwell — 1 operation(s) for health.
  name: Knownwell health API
  slug: knownwell-health-api
- description: The portfolios API from Knownwell — 2 operation(s) for portfolios.
  name: Knownwell portfolios API
  slug: knownwell-portfolios-api
- description: The root API from Knownwell — 1 operation(s) for root.
  name: Knownwell root API
  slug: knownwell-root-api
- description: The status API from Knownwell — 1 operation(s) for status.
  name: Knownwell status API
  slug: knownwell-status-api
- description: The streams API from Knownwell — 1 operation(s) for streams.
  name: Knownwell streams API
  slug: knownwell-streams-api
- description: The topics API from Knownwell — 1 operation(s) for topics.
  name: Knownwell topics API
  slug: knownwell-topics-api
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Knownwell api-keys API
  slug: open-knownwell-api-keys-api
- collection_type: open
  name: Knownwell api-keys clients API
  slug: open-knownwell-clients-api
- collection_type: open
  name: Knownwell api-keys documentation API
  slug: open-knownwell-documentation-api
- collection_type: open
  name: Knownwell api-keys health API
  slug: open-knownwell-health-api
- collection_type: open
  name: Knownwell api-keys portfolios API
  slug: open-knownwell-portfolios-api
- collection_type: open
  name: Knownwell api-keys root API
  slug: open-knownwell-root-api
- collection_type: open
  name: Knownwell api-keys status API
  slug: open-knownwell-status-api
- collection_type: open
  name: Knownwell api-keys streams API
  slug: open-knownwell-streams-api
- collection_type: open
  name: Knownwell api-keys topics API
  slug: open-knownwell-topics-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/knownwell-ci-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/knownwell-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/knownwell-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://knownwell.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.knownwell.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://api.knownwell.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.knownwell.com/docs#introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://api.knownwell.com/docs#get-started
- group: build
  title: ''
  type: Postman
  url: https://api.knownwell.com/static/knownwell-api-postman-collection.json
- group: company
  title: ''
  type: Blog
  url: https://knownwell.com/insights/
- group: operate
  title: ''
  type: Support
  url: https://knownwell.com/contact/
- group: commercial
  title: ''
  type: Pricing
  url: https://knownwell.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://knownwell.com/experience-the-knownwell-platform-checkout/
- group: start
  title: ''
  type: Login
  url: https://ci.knownwell.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://knownwell.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://knownwell.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.knownwell.com
- group: auth
  title: ''
  type: TrustCenter
  url: security/knownwell-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://knownwell.com/security/
- group: auth
  title: ''
  type: Security
  url: https://knownwell.com/security/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/knownwell-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/knownwell-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/knownwell-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/knownwell-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/knownwell-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/knownwell-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/knownwell-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/knownwell-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/knownwell-data-model.yml
- group: build
  title: ''
  type: Examples
  url: examples/knownwell-code-examples.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/knownwell-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/knownwell-plans-pricing.yml
- group: start
  title: ''
  type: Console
  url: sandbox/knownwell-sandbox.yml
created: '2026-07-17'
description: Knownwell is an AI-powered commercial intelligence platform for B2B professional services firms, built around client retention and expansion rather than new-logo acquisition. The platform ingests communications, CRM records, and enterprise data through connectors to Microsoft 365, Google Workspace, Salesforce, HubSpot, Slack, Teams, and conversation intelligence tools, then synthesizes an objective Knownwell score for every client relationship. Teams use it to detect churn risk before a renewal conversation, surface growth opportunities across a portfolio, and track relationship health over time without manual data entry. Knownwell publishes a read-only public REST API at api.knownwell.com/ci/v1 that exposes client scores, score history, portfolios, streams, topics, priorities, notes, key people, and the weekly Red/Amber/Green alignment reads a client team files by hand, authenticated with an X-API-Key header. Platform pricing is published as a live per-client volume calculator
  rather than named tiers, with a 30-day trial and no per-seat charge. Knownwell was acquired by 2X to form a human-agentic GTM services company.
image: https://knownwell.com/wp-content/uploads/2023/08/favicon21.svg
layout: provider
mcp_servers:
- description: Knownwell publishes no hosted or remote MCP server (no MCP reference in the developer docs, no /.well-known/ai-plugin.json, no npm or registry listing). This is a candidate server derived one-to-one f
  name: Knownwell MCP Server
  slug: knownwell-mcp-server
modified: '2026-08-13'
name: Knownwell
nav: Providers
network: true
overview: 'Knownwell publishes 10 APIs on the [APIs.io](https://apis.io/) network, including alignment API, api-keys API, clients API, and 7 more. Tagged areas include Company, Commercial Intelligence, Client Intelligence, Customer Success, and Revenue Operations.


  Knownwell''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 27 more developer resources.'
plans:
- name: Knownwell Plans Pricing
  plan_count: 0
  slug: knownwell-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 3
  name: Knownwell Rate Limits
  slug: knownwell-rate-limits
score:
  band: strong
  composite: 55.5
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 30.3
    contract_quality: 48.0
    developer_ergonomics: 70.8
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 42.1
  previous_composite: 55.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/knownwell/refs/heads/main/screenshots/knownwell-2026-07-25T224012.png
security:
- kind: authentication
  name: Knownwell Authentication
  slug: knownwell-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Knownwell Domain Security
  slug: knownwell-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Knownwell Vulnerability Disclosure
  slug: knownwell-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Knownwell Trust Center
  slug: knownwell-trust-center
  summary_line: SOC 2, Data Privacy Framework
slug: knownwell
tags:
- Company
- Commercial Intelligence
- Client Intelligence
- Customer Success
- Revenue Operations
- Professional Services
- Artificial Intelligence
- Analytics
- CRM
- Churn Risk
website: https://knownwell.com/
---
