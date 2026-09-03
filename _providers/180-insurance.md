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
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.2
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: Single embedded-insurance API covering the full lifecycle — quotation, proposal, sale/policy issuance, endorsement, renewal, claims and webhooks.
  name: 180 Seguros Sagas API
  slug: 180-seguros-sagas-api
artifact_total: 4
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
  type: X-MCPServerCandidate
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
modified: '2026-07-17'
name: 180 Insurance
nav: Providers
network: true
overview: '180 Insurance publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurtech, Insurance, Embedded Insurance, and Brazil.


  The 180 Insurance catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  180 Insurance''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, authentication, and 18 more developer resources.'
random_paper: 11
score:
  band: developing
  composite: 40.3
  coverage:
    artifact_dirs: 15
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 40.3
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: BR
      standard: lgpd
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 38.6
  schema_version: 0.18.2
  scored_at: '2026-09-03'
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
- Webhook
website: https://180s.com.br
---
