---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.8
  scored_at: '2026-09-02'
api_count: 2
apis:
- description: Totogi Charging-as-a-Service is a serverless, multi-tenant 5G Standalone and 5G Advanced converged charging system delivered as SaaS on AWS, with built-in policy control. Its account-management surfac
  name: Totogi Charging-as-a-Service API
  slug: totogi-charging-as-a-service
- description: Whoosh! is Totogi's Application-to-Person (A2P) messaging API, launched in September 2023 and positioned as a drop-in replacement for Twilio's A2P APIs that network operators can resell to keep enterp
  name: Whoosh Programmable Messaging API
  slug: whoosh-programmable-messaging-api
artifact_total: 7
asyncapis:
- description: ''
  name: Totogi Whoosh Webhooks
  slug: totogi-whoosh-webhooks
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/totogi-mcp.yml
- group: company
  title: ''
  type: Website
  url: https://totogi.com
- group: company
  title: ''
  type: About
  url: https://totogi.com/company/
- group: operate
  title: ''
  type: FAQ
  url: https://totogi.com/company/faqs/
- group: company
  title: ''
  type: Blog
  url: https://totogi.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://totogi.com/feed/
- group: company
  title: ''
  type: Newsroom
  url: https://totogi.com/newsroom/press-releases/
- group: other
  title: ''
  type: CaseStudies
  url: https://totogi.com/resources/case-studies/
- group: operate
  title: ''
  type: Support
  url: https://support.ccab.totogi.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/totogi
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/totogi/
- group: other
  title: ''
  type: X
  url: https://x.com/totogi
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@Totogi
- group: commercial
  title: ''
  type: TermsOfService
  url: https://totogi.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://totogi.com/privacy/
- group: agent
  title: ''
  type: LLMsTxt
  url: https://totogi.com/llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/totogi-llms.txt
- group: other
  title: ''
  type: Facts
  url: https://totogi.com/facts.json
- group: other
  title: ''
  type: Evidence
  url: https://totogi.com/evidence.json
- group: other
  title: ''
  type: Glossary
  url: https://totogi.com/glossary.json
- group: build
  title: ''
  type: Packages
  url: packages/totogi-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/totogi-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/totogi-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/totogi-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/totogi-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/totogi-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/totogi-error-catalog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/totogi-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/totogi-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/totogi-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/totogi-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/totogi-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/totogi-conformance.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/totogi-domain-security.yml
created: '2026-07-25'
description: 'Totogi LLC is an Austin, Texas based vertical AI and BSS software vendor that builds telecom operator software natively on the public cloud (AWS). Its two products are the Totogi Ontology (formerly BSS Magic), a machine-readable semantic layer that sits above a carrier''s existing BSS, OSS, core, and network systems so AI agents can reason and act across them, and Totogi Charging-as-a-Service, a multi-tenant, serverless 5G Standalone converged charging system with built-in policy control that integrates over the 4G/5G NSA Sy (PCRF), 5G SA N28 (PCF), Npcf_SMPolicyControl (N7) and Gx interfaces, and implements the 3GPP TS 32.291 Nchf_ConvergedCharging v3 (N40) resource surface. Totogi sits in the telecom value chain as a vendor to communications service providers, MNOs, MVNOs, and MVNEs — it does not own spectrum and it does not sell to developers directly. Its API posture is split three ways. Charging-as-a-Service is a fully public GraphQL contract: a SpectaQL reference at docs.api.totogi.com
  publishes 32 queries, 61 mutations and 480 type definitions, with per-operation named authorization roles, typed result-union errors, caller-supplied transaction ids for idempotency, and dated field deprecations. Whoosh! is a Twilio-compatible A2P messaging API sold through operators, with open quickstarts, a live API host and four published helper libraries. The platform''s other reference at docs.totogi.solutions is a Redocly login wall, and there is no self-serve signup anywhere. Totogi holds TM Forum Platinum Open API Conformance Certification for 31 certified Open APIs and once ranked #1 on the TM Forum Open API Certification Leaderboard. No CAMARA, GSMA Open Gateway, or Aduna reference appears anywhere in Totogi''s own canonical AI index.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: Totogi MCP Server
  slug: totogi-mcp-server
modified: '2026-07-25'
name: Totogi
nav: Providers
network: true
overview: 'Totogi publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Telecommunications, United States, BSS, OSS, and Charging.


  The Totogi catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Totogi''s developer surface includes FAQ, engineering blog, support, YouTube channel, authentication, changelog, and 29 more developer resources.'
random_paper: 11
scopes:
- name: Totogi Scopes
  scope_count: 0
  slug: totogi-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 54.0
  coverage:
    artifact_dirs: 19
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 53.1
    developer_ergonomics: 73.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 34.2
  previous_composite: 54.0
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 70.1
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/totogi/refs/heads/main/screenshots/totogi-2026-08-17T082413.png
security:
- kind: authentication
  name: Totogi Authentication
  slug: totogi-authentication
  summary_line: oauth2/http · 3 schemes
- kind: domain-security
  name: Totogi Domain Security
  slug: totogi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: totogi
tags:
- Telecommunications
- United States
- BSS
- OSS
- Charging
- Messaging
- SMS
- A2P
- 5G
- TM Forum
- Standards
- Network Vendor
- Vertical AI
- GraphQL
- Policy Control
website: https://totogi.com
---
