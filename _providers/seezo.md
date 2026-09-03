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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
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
  score: 15.1
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://seezo.io/
- group: company
  title: ''
  type: Blog
  url: https://seezo.io/blog
- group: start
  title: ''
  type: SignUp
  url: https://app.seezo.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://seezo.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://seezo.io/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: security/seezo-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.seezo.io/
- group: auth
  title: ''
  type: Security
  url: https://seezo.io/vulnerability-disclosure-program
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/seezo-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/seezo-authentication.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/seezo-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/seezo-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/seezo-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/seezo-llms.txt
created: '2026-07-17'
description: Seezo is an automated, AI-powered security design review platform. It analyzes design documents and product requirement docs (PRDs) to generate explainable, consistent, and contextual security requirements — threat models, data-flow diagrams, and component maps — before developers begin coding, then routes those requirements into the tools engineering teams already use (Jira, GitHub, Slack, Confluence, Linear, ServiceNow, and more). Seezo is SOC 2 and ISO 27001 certified. It does not currently publish a public developer API, SDKs, or an OpenAPI definition; its OAuth surface authenticates users of the Seezo web app.
image: https://framerusercontent.com/assets/w3DTWdd9nW72eDXAyRElIJMMHFo.jpg
layout: provider
modified: '2026-07-21'
name: Seezo
nav: Providers
network: true
overview: 'Seezo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Security, Application Security, and Threat Modeling.


  Seezo''s developer surface includes engineering blog, signup flow, authentication, and 11 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 19.2
  coverage:
    artifact_dirs: 7
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 57.4
    governance: 4.5
    operational_transparency: 10.5
  previous_composite: 19.2
  provenance:
    conformance: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/seezo/refs/heads/main/screenshots/seezo-2026-09-02T154810.png
security:
- kind: authentication
  name: Seezo Authentication
  slug: seezo-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Seezo Domain Security
  slug: seezo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Seezo Vulnerability Disclosure
  slug: seezo-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Seezo Trust Center
  slug: seezo-trust-center
  summary_line: SOC 2, ISO 27001
slug: seezo
tags:
- Company
- Artificial Intelligence
- Security
- Application Security
- Threat Modeling
- Security Design Review
- Developer Tools
- DevSecOps
website: https://seezo.io/
---
