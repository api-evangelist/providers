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
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 41.7
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Single embedded-insurance API covering the full lifecycle — quotation, proposal, sale/policy issuance, endorsement, renewal, claims and webhooks.
  name: 180 Seguros Sagas API
  slug: 180-seguros-sagas-api
artifact_total: 5
asyncapis:
- description: ''
  name: 180 Insurance Webhooks
  slug: 180-insurance-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://180s.com.br
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.180s.com.br/reference/introducao
- group: docs
  title: ''
  type: Documentation
  url: https://docs.180s.com.br/reference/introducao
- group: docs
  title: ''
  type: APIReference
  url: https://docs.180s.com.br/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.180s.com.br/reference/introducao
- group: company
  title: ''
  type: Blog
  url: https://180s.com.br/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://180s.com.br/condicoes-gerais/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://180s.com.br/wp-content/uploads/2026/03/Politica-de-Privacidade-180-Seguros-new.docx-1.pdf
- group: operate
  title: ''
  type: Support
  url: https://180s.com.br/contato/
- group: start
  title: ''
  type: SignUp
  url: https://180s.com.br/contato/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/180seg
- group: auth
  title: ''
  type: Authentication
  url: authentication/180-insurance-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/180-insurance-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/180-insurance-problem-types.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/180-insurance-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/180-insurance-mcp.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/180-insurance-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/180-insurance-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://180s.com.br/tecnologia-180/
- group: design
  title: ''
  type: DataModel
  url: data-model/180-insurance-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/180-insurance-sandbox.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/180-insurance-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/180-insurance-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/180-insurance-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: '180 Seguros (180 Insurance) is the first tech-native insurer in Brazil, an SUSEP-authorized insurtech that lets fintechs, digital banks, credit cooperatives and other financial and non-financial businesses embed insurance into their own products through a single API — the Sagas API. The platform covers the full insurance lifecycle: product/combo listing, quotation (cotação), proposal (proposta), sale/policy issuance (venda), endorsements, renewals (renovações) and claims (sinistros), plus HMAC-signed webhooks for real-time visibility. Authentication is OAuth2 client-credentials via Auth0, errors follow RFC 9457 problem-details, and the company publishes a security posture including AICPA SOC 2, LGPD and SUSEP Circular 638 compliance. 180 Seguros is backed by 8VC, Monashees, Dragoneer, Atlantico and Canary, and was added to the API Evangelist network as an 8VC portfolio company.'
image: https://files.readme.io/21b0f8e-small-180_seguros_logo.jpeg
layout: provider
mcp_servers:
- description: ''
  name: 180-insurance-mcp.yml
  slug: 180-insurance-mcpyml
modified: '2026-07-17'
name: 180 Insurance
nav: Providers
network: true
overview: '180 Insurance publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurtech, Insurance, Embedded Insurance, and Brazil.


  The 180 Insurance catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  180 Insurance''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, authentication, and 18 more developer resources.'
random_paper: 46
score:
  band: developing
  composite: 45.7
  delta: 2.1
  facets:
    commercial_clarity: 42.1
    contract_quality: 51.6
    developer_ergonomics: 62.5
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 13.2
  previous_composite: 43.6
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 45.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/180-insurance/refs/heads/main/screenshots/180-insurance-2026-07-25T181107.png
security:
- kind: authentication
  name: 180 Insurance Authentication
  slug: 180-insurance-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: 180 Insurance Domain Security
  slug: 180-insurance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: 180-insurance
tags:
- Company
- Insurtech
- Insurance
- Embedded Insurance
- Brazil
- Fintech
- API
- Webhooks
website: https://180s.com.br
---
