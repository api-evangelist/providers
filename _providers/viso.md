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
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: Authenticated Apollo GraphQL API backing the Viso Now agentic computer vision app. Anonymous access is denied (HTTP 403); sign-in is via Google Identity Services with a session credential. GraphQL int
  name: Viso Now GraphQL API
  slug: viso-now-graphql-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://viso.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.now.viso.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.now.viso.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://viso.ai/viso-now/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://now.viso.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://viso.ai/legal/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://viso.ai/legal/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.viso.ai/status/viso-now
- group: auth
  title: ''
  type: Authentication
  url: authentication/viso-authentication.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/viso-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/viso-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/viso-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/viso-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/viso-domain-security.yml
created: '2026-07-17'
description: 'viso.ai builds Visual General Intelligence, a new kind of computer vision that understands any scene out of the box without data collection, annotation, or per-question retraining. The company ships two products: Viso Suite, an industry- and hardware-agnostic no-code/low-code cloud platform to build, deploy, scale, and operate real-world computer vision applications; and Viso Now, an agentic computer vision platform whose vision agents connect a camera feed, recognize the scene, write the detection logic, and wire the alerts on auto-pilot. Viso Now plugs into the cameras and video systems teams already run through ready-made connectors, then pushes outputs anywhere: alerts to Slack, Teams, or email, and media forwarded into any ERP, BI tool, or third-party system over a direct API. The Viso Now backend is exposed as an authenticated Apollo GraphQL API at now.viso.ai with Google sign-in.'
image: https://viso.ai/wp-content/uploads/2021/03/viso-ai-logo.png
layout: provider
modified: '2026-07-21'
name: VISO
nav: Providers
network: true
overview: 'VISO publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Computer-Vision, Machine-Learning, and Video Analytics.


  VISO''s developer surface includes documentation, pricing, signup flow, authentication, and 10 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 14.2
  coverage:
    artifact_dirs: 7
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 15.8
  previous_composite: 14.2
  provenance:
    conformance: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/viso/refs/heads/main/screenshots/viso-2026-09-02T170044.png
security:
- kind: authentication
  name: Viso Authentication
  slug: viso-authentication
  summary_line: oauth2/session · 2 schemes
- kind: domain-security
  name: Viso Domain Security
  slug: viso-domain-security
  summary_line: TLSv1.3 · DMARC
slug: viso
tags:
- Company
- Artificial Intelligence
- Computer-Vision
- Machine-Learning
- Video Analytics
- Vision Agents
- Edge AI
- GraphQL
- No-Code
website: https://viso.ai/
---
