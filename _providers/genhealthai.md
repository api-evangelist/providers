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
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 24.3
  scored_at: '2026-08-11'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://genhealth.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.genhealth.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.genhealth.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.genhealth.ai/docs/prior-authorization-automation
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.genhealth.ai/docs/getting-started-1
- group: operate
  title: ''
  type: Support
  url: mailto:support@genhealth.ai
- group: company
  title: ''
  type: Blog
  url: https://genhealth.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/genhealth
- group: start
  title: ''
  type: SignUp
  url: https://umpa.genhealth.ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://genhealth.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://genhealth.ai/privacy
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.genhealth.ai
- group: operate
  title: ''
  type: StatusPage
  url: https://status.genhealth.ai
- group: auth
  title: ''
  type: Compliance
  url: https://trust.genhealth.ai
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/genhealthai-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/genhealthai-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/genhealthai-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/genhealthai-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/genhealthai-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/genhealthai-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/genhealthai-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/genhealthai-conventions.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/genhealthai-domain-security.yml
created: '2026-07-17'
description: 'GenHealth.ai builds generative AI for healthcare operations, powered by a Large Medical Model (LMM) trained on sequences of medical events. Its products automate the administrative back office for providers, health plans, and DME suppliers: fax intake routing, prior authorization and medical-necessity review (UMPA), and revenue cycle management. The developer platform exposes an Inference API that generates simulated patient futures from demographic, ICD diagnosis, CPT/HCPCS procedure, and NDC medication codes, an Embeddings API for semantic search over medical sequences, and a UM/PA API that uploads, extracts, and adjudicates prior-authorization PDFs. GenHealth integrates with any FHIR server implementing the HL7 Da Vinci prior-authorization guides (CRD, DTR, PAS). The platform is SOC 2 and HIPAA compliant with a public trust center and status page.'
image: https://genhealth.ai/apple-touch-icon.png
layout: provider
mcp_servers:
- description: ''
  name: genhealthai-mcp.yml
  slug: genhealthai-mcpyml
modified: '2026-07-19'
name: GenHealth.ai
nav: Providers
network: true
overview: 'GenHealth.ai is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, Artificial Intelligence, and Generative AI.


  GenHealth.ai''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 17 more developer resources.'
random_paper: 102
score:
  band: thin
  composite: 36.9
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 73.9
    discoverability: 57.4
    governance: 12.5
    operational_transparency: 36.8
  previous_composite: 36.9
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/genhealthai/refs/heads/main/screenshots/genhealthai-2026-07-25T215613.png
security:
- kind: authentication
  name: Genhealthai Authentication
  slug: genhealthai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Genhealthai Domain Security
  slug: genhealthai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Genhealthai Trust Center
  slug: genhealthai-trust-center
  summary_line: SOC 2, HIPAA
slug: genhealthai
tags:
- Company
- Health
- Healthcare
- Artificial Intelligence
- Generative AI
- Prior Authorization
- Revenue Cycle Management
- FHIR
- HL7 Da Vinci
- Medical Coding
- Utilization Management
website: https://genhealth.ai
---
