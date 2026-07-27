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
    agent_skills: true
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 71.2
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Medigo Agentic Access
  operation_count: 25
  slug: medigo-agentic-access
  summary_line: 25 operations · 15 acting
api_count: 6
apis:
- description: File that contains content relevant to a medical inquiry
  name: Medigo attachments API
  slug: medigo-attachments-api
- description: The inquiries API from Medigo — 1 operation(s) for inquiries.
  name: Medigo inquiries API
  slug: medigo-inquiries-api
- description: Search endpoints
  name: Medigo search API
  slug: medigo-search-api
- description: Professional review of a diagnosis or treatment already suggested by a doctor
  name: Medigo second-opinions API
  slug: medigo-second-opinions-api
- description: Insurance TPA service APIs
  name: Medigo tpa API
  slug: medigo-tpa-api
- description: Push notification related to events in MEDIGO's system
  name: Medigo webhooks API
  slug: medigo-webhooks-api
artifact_total: 11
asyncapis:
- description: ''
  name: Medigo Webhooks
  slug: medigo-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/medigo-agentic-access.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/medigo-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/medigo-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/medigo-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/medigo-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/medigo-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/medigo-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/medigo-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/medigo-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/medigo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/medigo-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.medigo.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MEDIGO
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.medigo.com/partnership-terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.medigo.com/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://www.medigo.com/contact/
created: '2026-07-17'
description: Medigo (MEDIGO GmbH) is a Berlin-based health-tech company, founded in 2013, that enables global access to quality healthcare as a third party administrator (TPA). It helps insurers and organisations navigate healthcare worldwide with a curated provider network spanning 100+ countries, tech-driven cost containment, claims handling, medical concierge, and second medical opinions. Medigo exposes a partner REST API (MEDIGO API V2) that lets insurers and integrators manage members, insurance policies, terms and insured members, submit and track TPA claims, request and track second medical opinions, upload medical attachments, search procedures, and receive event webhooks. Backed by Accel and Atlantic Labs.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/medigo.png
layout: provider
mcp_servers:
- description: ''
  name: medigo-mcp.yml
  slug: medigo-mcpyml
modified: '2026-07-20'
name: Medigo
nav: Providers
network: true
overview: 'Medigo publishes 6 APIs on the [APIs.io](https://apis.io/) network, including attachments API, inquiries API, search API, and 3 more. Tagged areas include Company, Consumer, Healthcare, Insurance, and Third Party Administrator.


  The Medigo catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Medigo''s developer surface includes authentication, support, and 15 more developer resources.'
random_paper: 17
score:
  band: thin
  composite: 39.7
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 60.4
    developer_ergonomics: 30.4
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 39.7
  regulatory:
    applies: true
    regime: Health
    regime_id: health
    score: 54.3
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Medigo Authentication
  slug: medigo-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Medigo Domain Security
  slug: medigo-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: medigo
tags:
- Company
- Consumer
- Healthcare
- Insurance
- Third Party Administrator
- Claims
- Cost Containment
- Second Medical Opinion
- Medical Travel
- Health Insurance
website: https://www.medigo.com
---
