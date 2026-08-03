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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: documented
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.2
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 2
  human_in_the_loop: 1
  name: Knownwell Agentic Access
  operation_count: 25
  slug: knownwell-agentic-access
  summary_line: 25 operations · 2 acting · 1 human-in-the-loop
api_count: 9
apis:
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
artifact_total: 16
common:
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
created: '2026-07-17'
description: Knownwell is an AI-powered commercial intelligence platform for B2B professional services firms, built around client retention and expansion rather than new-logo acquisition. The platform ingests communications, CRM records, and enterprise data through connectors to Microsoft 365, Google Workspace, Salesforce, HubSpot, Slack, Teams, and conversation intelligence tools, then synthesizes an objective Knownwell score for every client relationship. Teams use it to detect churn risk before a renewal conversation, surface growth opportunities across a portfolio, and track relationship health over time without manual data entry. Knownwell publishes a read-only public REST API at api.knownwell.com/ci/v1 that exposes client scores, score history, portfolios, streams, topics, priorities, notes, and key people, authenticated with an X-API-Key header. Knownwell was acquired by 2X to form a human-agentic GTM services company.
image: https://knownwell.com/wp-content/uploads/2023/08/favicon21.svg
layout: provider
mcp_servers:
- description: ''
  name: knownwell-mcp.yml
  slug: knownwell-mcpyml
modified: '2026-07-19'
name: Knownwell
nav: Providers
network: true
overview: 'Knownwell publishes 9 APIs on the [APIs.io](https://apis.io/) network, including api-keys API, clients API, documentation API, and 6 more. Tagged areas include Company, Commercial Intelligence, Client Intelligence, Customer Success, and Revenue Operations.


  Knownwell''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 24 more developer resources.'
random_paper: 43
rate_limits:
- limit_count: 3
  name: Knownwell Rate Limits
  slug: knownwell-rate-limits
score:
  band: strong
  composite: 56.1
  delta: 4.1
  facets:
    commercial_clarity: 60.5
    contract_quality: 50.7
    developer_ergonomics: 60.3
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 57.9
  previous_composite: 52.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  schema_version: 0.9
  scored_at: '2026-08-03'
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
