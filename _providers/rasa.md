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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.3
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Rasa Agentic Access
  operation_count: 20
  slug: rasa-agentic-access
  summary_line: 20 operations · 14 acting
api_count: 2
apis:
- baseURL: http://localhost:5005
  baseurl_source: declared
  description: The Domain API from Rasa — 1 operation(s) for domain.
  name: Rasa Domain API
  slug: rasa-domain-api
- baseURL: http://localhost:5005
  baseurl_source: declared
  description: The Model API from Rasa — 6 operation(s) for model.
  name: Rasa Model API
  slug: rasa-model-api
- baseURL: http://localhost:5005
  baseurl_source: declared
  description: The Rasa SDK Action Server Endpoint API from Rasa — 1 operation(s) for rasa sdk action server endpoint.
  name: Rasa Rasa SDK Action Server Endpoint API
  slug: rasa-rasa-sdk-action-server-endpoint-api
- baseURL: http://localhost:5005
  baseurl_source: declared
  description: The Server Information API from Rasa — 3 operation(s) for server information.
  name: Rasa Server Information API
  slug: rasa-server-information-api
- baseURL: http://localhost:5005
  baseurl_source: declared
  description: The Tracker API from Rasa — 7 operation(s) for tracker.
  name: Rasa Tracker API
  slug: rasa-tracker-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Rasa SDK - Action Server Endpoint Domain API
  slug: open-rasa-domain-api
- collection_type: open
  name: Rasa SDK - Action Server Endpoint Domain Model API
  slug: open-rasa-model-api
- collection_type: open
  name: Rasa SDK - Action Server Endpoint Domain Rasa SDK Action Server Endpoint API
  slug: open-rasa-rasa-sdk-action-server-endpoint-api
- collection_type: open
  name: Rasa SDK - Action Server Endpoint Domain Server Information API
  slug: open-rasa-server-information-api
- collection_type: open
  name: Rasa SDK - Action Server Endpoint Domain Tracker API
  slug: open-rasa-tracker-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/rasa-action-server-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rasa-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/rasa-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rasa-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/rasa-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/rasa-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/rasa-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/rasa-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/rasa-cli.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/rasa-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rasa-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/rasa-well-known.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/rasa-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/rasa-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://rasa.com/docs/reference/changelogs/compatibility-matrix/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/rasa-changelog.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://rasa.com/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://rasa.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://rasa.com/docs/reference/overview/
- group: start
  title: ''
  type: Quickstart
  url: https://rasa.com/docs/learn/quickstart/pro/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/RasaHQ
- group: company
  title: ''
  type: Blog
  url: https://blog.rasa.com/
- group: operate
  title: ''
  type: Support
  url: https://forum.rasa.com
- group: commercial
  title: ''
  type: Pricing
  url: https://rasa.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://rasa.com/rasa-pro-developer-edition-license-key-request
- group: company
  title: ''
  type: Website
  url: https://rasa.com
created: '2026-07-17'
description: Rasa is an open-core conversational AI framework for enterprises, built by Rasa Technologies GmbH, that natively leverages generative AI through CALM (Conversational AI with Language Models) to build reliable text and voice assistants. Rasa Pro is the pro-code framework (with Flows, custom actions, channel connectors, multi-LLM routing, observability and Kubernetes deployment); Rasa Studio is the companion no-code UI; and Rasa Open Source provides the underlying NLU and dialogue-management framework. The self-hosted runtime exposes an HTTP API for managing conversation trackers and training, testing and loading models, plus a Python SDK action server for custom actions.
image: https://rasa.com/favicon.ico
layout: provider
modified: '2026-07-20'
name: Rasa
nav: Providers
network: true
overview: 'Rasa publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Domain API, Model API, Rasa SDK Action Server Endpoint API, and 2 more. Tagged areas include Company, Artificial Intelligence, Conversational AI, Chatbots, and Voice Assistants.


  Rasa''s developer surface includes authentication, CLI, sandbox, changelog, documentation, API reference, quickstart, and 20 more developer resources.'
random_paper: 3
score:
  band: developing
  composite: 44.1
  coverage:
    artifact_dirs: 21
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 4.5
    contract_quality: 46.4
    developer_ergonomics: 85.7
    discoverability: 66.7
    governance: 4.5
    operational_transparency: 26.3
  previous_composite: 44.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rasa/refs/heads/main/screenshots/rasa-2026-08-17T081447.png
security:
- kind: authentication
  name: Rasa Authentication
  slug: rasa-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Rasa Domain Security
  slug: rasa-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rasa
tags:
- Company
- Artificial Intelligence
- Conversational AI
- Chatbots
- Voice Assistants
- NLU
- LLM
- Machine-Learning
- Agents
website: https://rasa.com
---
