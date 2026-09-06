---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Embeddable AI chat surface for EV charging driver support. Ships as a lemonflow-chat custom element loaded from a single script tag, or as a headless iframe at /embed for teams that already operate th
  name: Lemonflow Chat Widget
  slug: chat-widget
artifact_total: 4
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/lemonflow-ai-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lemonflow-ai-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://lemonflow-ai.github.io/lemonflow-docs/
- group: docs
  title: ''
  type: Documentation
  url: https://lemonflow-ai.github.io/lemonflow-docs/
- group: docs
  title: ''
  type: APIReference
  url: https://lemonflow-ai.github.io/lemonflow-docs/protected/integration/integration-requirements.html
- group: start
  title: ''
  type: GettingStarted
  url: https://lemonflow-ai.github.io/lemonflow-docs/protected/integration/widget-integration.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lemonflow-ai
- group: operate
  title: ''
  type: StatusPage
  url: https://status.lemonflow.ai
- group: auth
  title: ''
  type: Compliance
  url: conformance/lemonflow-ai-conformance.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lemonflow.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lemonflow.ai/privacy
- group: operate
  title: ''
  type: Support
  url: mailto:tech@lemonflow.ai
- group: start
  title: ''
  type: SignUp
  url: https://lemonflow.ai/#request-demo
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lemonflow-ai-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/lemonflow-ai-well-known.yml
- group: design
  title: ''
  type: Components
  url: components/lemonflow-ai-components.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/lemonflow-ai-conventions.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lemonflow-ai-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/lemonflow-ai-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lemonflow-ai-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lemonflow-ai-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/lemonflow-ai-data-model.yml
created: '2026-07-17'
description: Lemonflow Technologies GmbH is a Munich-based company building AI agents purpose-built for the electric-vehicle charging industry. Its platform gives charge point operators (CPOs), eMobility service providers and charging software vendors 24/7 AI-driven driver support across voice, chat and email in 30+ languages, plus an Operations Hub for proactive network monitoring, OCPP log interpretation, anomaly detection and self-healing automations such as remote charger resets. The developer-facing surface is an embeddable Chat Widget - a lemonflow-chat web component (and an equivalent headless iframe) loaded from chat.lemonflow.ai and driven through a postMessage command/event API - together with a documented set of CPMS integration requirements covering bulk station data, real-time status, OCPP logs, remote actions and ticketing. Lemonflow is backed by Speedinvest.
image: https://lemonflow.ai/favicons/apple-touch-icon.png
layout: provider
modified: '2026-07-19'
name: Lemonflow
nav: Providers
network: true
overview: 'Lemonflow publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, AI Agents, Customer-Support, and Electric Vehicle Charging.


  Lemonflow''s developer surface includes documentation, API reference, getting-started guide, support, signup flow, authentication, and 16 more developer resources.'
random_paper: 8
score:
  band: thin
  composite: 31.8
  coverage:
    artifact_dirs: 13
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 54.8
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 18.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 31.8
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lemonflow-ai/refs/heads/main/screenshots/lemonflow-ai-2026-07-25T224851.png
security:
- kind: authentication
  name: Lemonflow Ai Authentication
  slug: lemonflow-ai-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Lemonflow Ai Domain Security
  slug: lemonflow-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Lemonflow Ai Trust Center
  slug: lemonflow-ai-trust-center
  summary_line: ISO/IEC 27001, SOC 2 Type II
slug: lemonflow-ai
tags:
- Company
- Artificial Intelligence
- AI Agents
- Customer-Support
- Electric Vehicle Charging
- E-Mobility
- OCPP
- Chat Widget
- Voice
- Europe
website: https://lemonflow-ai.github.io/lemonflow-docs/
---
