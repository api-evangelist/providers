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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: verified
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 64.4
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 8
  human_in_the_loop: 1
  name: Healthsherpa Agentic Access
  operation_count: 15
  slug: healthsherpa-agentic-access
  summary_line: 15 operations · 8 acting · 1 human-in-the-loop
api_count: 5
apis:
- description: The Enrollment Sessions API from HealthSherpa — 1 operation(s) for enrollment sessions.
  name: HealthSherpa Enrollment Sessions API
  slug: healthsherpa-enrollment-sessions-api
- description: The Enrollments API from HealthSherpa — 7 operation(s) for enrollments.
  name: HealthSherpa Enrollments API
  slug: healthsherpa-enrollments-api
- description: The Quotes API from HealthSherpa — 1 operation(s) for quotes.
  name: HealthSherpa Quotes API
  slug: healthsherpa-quotes-api
- description: The Reference API from HealthSherpa — 3 operation(s) for reference.
  name: HealthSherpa Reference API
  slug: healthsherpa-reference-api
- description: The Utility API from HealthSherpa — 1 operation(s) for utility.
  name: HealthSherpa Utility API
  slug: healthsherpa-utility-api
artifact_total: 11
asyncapis:
- description: ''
  name: Healthsherpa Ichra Webhooks
  slug: healthsherpa-ichra-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://one.healthsherpa.com/
- group: docs
  title: ''
  type: Documentation
  url: https://one.healthsherpa.com/docs.html
- group: docs
  title: ''
  type: APIReference
  url: https://one.healthsherpa.com/docs.html
- group: start
  title: ''
  type: GettingStarted
  url: https://one.healthsherpa.com/vibe-coders.html
- group: start
  title: ''
  type: SignUp
  url: https://one.healthsherpa.com/register.html
- group: start
  title: ''
  type: Login
  url: https://one.healthsherpa.com/portal.html
- group: operate
  title: ''
  type: Support
  url: mailto:developers@one.healthsherpa.com
- group: company
  title: ''
  type: Website
  url: https://www.healthsherpa.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/healthsherpa
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/healthsherpa-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/healthsherpa-authentication.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/healthsherpa-conventions.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/healthsherpa-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/healthsherpa-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/healthsherpa-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/healthsherpa-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/healthsherpa-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.healthsherpa.com/agents_agencies
- group: agent
  title: ''
  type: MCPServer
  url: mcp/healthsherpa-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/healthsherpa-one-overlay.yaml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/healthsherpa-ichra-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/healthsherpa-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/healthsherpa-agentic-access.yml
created: '2026-07-17'
description: HealthSherpa is the leading ACA (Affordable Care Act) health insurance quoting and enrollment platform, and was the first company to partner with CMS to offer Enhanced Direct Enrollment (EDE) for agents. Its developer surface, HealthSherpa ONE (one.healthsherpa.com), exposes a public OpenAPI 3.1 REST API for on- and off-exchange ACA plan quoting, county/issuer/provider reference lookups, agent and self-service enrollment sessions, and an approval-gated direct enrollment API covering the full off-exchange (ICHRA) application lifecycle — create, update, submit, cancel, terminate, supporting-document upload, and payment redirect. Authentication is a single x-api-key header; enrollment writes support Idempotency-Key with 24-hour retention. Separate ICHRA and Medicare Partner APIs provide QuoteConnect/EnrollConnect, deeplinked enrollment, and webhooks. HealthSherpa publishes first-party Agent Skills, an llms.txt, and vibe-coding prompts for agents.
image: https://healthsherpa-21715791.hs-sites.com/hubfs/raw_assets/public/HealthSherpa%20Theme/HealthSherpa/images/favicon/apple-touch-icon.png
layout: provider
mcp_servers:
- description: ''
  name: healthsherpa-mcp.yml
  slug: healthsherpa-mcpyml
modified: '2026-07-19'
name: HealthSherpa
nav: Providers
network: true
overview: 'HealthSherpa publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Enrollment Sessions API, Enrollments API, Quotes API, and 2 more. Tagged areas include Company, Health Insurance, Healthcare, ACA, and Enrollment.


  The HealthSherpa catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  HealthSherpa''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, authentication, and 18 more developer resources.'
random_paper: 58
score:
  band: developing
  composite: 43.8
  delta: -2.5
  facets:
    commercial_clarity: 21.1
    contract_quality: 69.4
    developer_ergonomics: 58.7
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 13.2
  previous_composite: 46.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 33.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/healthsherpa/refs/heads/main/screenshots/healthsherpa-2026-07-25T220840.png
security:
- kind: authentication
  name: Healthsherpa Authentication
  slug: healthsherpa-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Healthsherpa Domain Security
  slug: healthsherpa-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
skill_count: 1
skills:
- name: ichra-platform-integration
  slug: ichra-platform-integration
slug: healthsherpa
tags:
- Company
- Health Insurance
- Healthcare
- ACA
- Enrollment
- Quoting
- Insurance
- Enhanced Direct Enrollment
- ICHRA
website: https://www.healthsherpa.com
---
