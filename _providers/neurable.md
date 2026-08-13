---
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
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.3
  scored_at: '2026-08-12'
api_count: 5
apis:
- description: The Core API from Neurable — 2 operation(s) for core.
  name: Neurable Core API
  slug: neurable-core-api
- description: The OAuth API from Neurable — 3 operation(s) for oauth.
  name: Neurable O Auth API
  slug: neurable-oauth-api
- description: The OIDC API from Neurable — 2 operation(s) for oidc.
  name: Neurable OIDC API
  slug: neurable-oidc-api
- description: The open API from Neurable — 1 operation(s) for open.
  name: Neurable Open API
  slug: neurable-open-api
- description: The protected API from Neurable — 5 operation(s) for protected.
  name: Neurable Protected API
  slug: neurable-protected-api
artifact_total: 9
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/neurable-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/neurable-analytics-service-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/neurable-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.neurable.com/
- group: company
  title: ''
  type: About
  url: https://www.neurable.com/about
- group: company
  title: ''
  type: Blog
  url: https://www.neurable.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.neurable.com/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.neurable.com/faqs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/neurable
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.neurable.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.neurable.com/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/neurable-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/neurable-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/neurable-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/neurable-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/neurable-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/neurable-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/neurable-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/neurable-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/neurable-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-04'
description: 'Neurable is a Boston, Massachusetts neurotechnology company, founded in 2015 on University of Michigan EEG signal-processing research, that builds non-invasive brain-computer interface (BCI) hardware and the AI models that interpret the signal. Its consumer product is the MW75 Neuro — Master & Dynamic over-ear headphones with dry conductive-fabric EEG electrodes that measure focus, fatigue and cognitive load — and it also ships an MW75 Neuro Research Kit (12-channel, 500 Hz raw EEG plus accelerometer/gyroscope, exported for LSL and BrainVision toolchains) and a partner Development Kit for hardware and software OEMs embedding Neurable sensing into their own devices. Neurable publishes no public developer portal or API reference, but its production backend services expose FastAPI-generated OpenAPI 3.1.0 descriptions at their host roots: an Analytics Service handling the EEG recording lifecycle and headset feature licensing, a real-time data processing pipe service that is also
  a full OpenID Connect authorization server, and a Brain Health Service.'
image: https://cdn.prod.website-files.com/65773cb2354a620eb230d1e4/657b30529e7a3d9845248e54_Neurable-December-Opengraph%20(2).jpg
layout: provider
mcp_servers:
- description: ''
  name: neurable-mcp.yml
  slug: neurable-mcpyml
modified: '2026-08-04'
name: Neurable
nav: Providers
network: true
overview: 'Neurable publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Core API, O Auth API, OIDC API, and 2 more. Tagged areas include neurotechnology, brain-computer-interface, eeg, neuroscience, and wearables.


  Neurable''s developer surface includes engineering blog, support, authentication, and 18 more developer resources.'
random_paper: 6
scopes:
- name: Neurable Scopes
  scope_count: 5
  slug: neurable-scopes
  summary_line: 5 scopes
score:
  band: thin
  composite: 35.7
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 47.3
    developer_ergonomics: 21.2
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 5.3
  previous_composite: 35.7
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 52.5
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Neurable Authentication
  slug: neurable-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Neurable Domain Security
  slug: neurable-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: neurable
tags:
- neurotechnology
- brain-computer-interface
- eeg
- neuroscience
- wearables
- biosignals
- hardware
- consumer-electronics
- research-tools
- cognitive-analytics
- health-data
- oauth
- openid-connect
website: https://www.neurable.com/
---
