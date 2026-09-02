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
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.6
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: REST API for retrieving, aggregating, and delivering structured patient medical records. Covers patient management, record-retrieval requests, previous-provider retrievals, record uploads, granular cl
  name: Predoc Partner API
  slug: predoc-partner-api
artifact_total: 6
asyncapis:
- description: ''
  name: Predoc Webhooks
  slug: predoc-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/predoc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.predoc.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.predoc.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.predoc.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.predoc.ai/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://www.predoc.ai/get-started
- group: start
  title: ''
  type: Login
  url: https://app.predoc.ai/login
- group: company
  title: ''
  type: Blog
  url: https://www.predoc.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://www.predoc.ai/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.predoc.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.predoc.ai/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://predoc.statuspage.io
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.predoc.ai/changelog
- group: auth
  title: ''
  type: Compliance
  url: https://www.predoc.ai/security-compliance
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/predoc-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/predoc-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/predoc-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/predoc-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/predoc-trust-center.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/predoc-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/predoc-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/predoc-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/predoc-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/predoc-mcp.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/predoc-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/predoc-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/predoc-problem-types.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Predoc is an AI-native medical records platform that automates the retrieval, aggregation, normalization, de-duplication, and structured delivery of complete patient histories. It queries health information exchanges (HIEs) and initiates outreach to non-connected providers, ingests faxes, PDFs, and digital formats, and delivers clean, FHIR-compliant clinical data to healthcare organizations and clinical research teams via a REST Partner API, file exports, or direct EHR integration. The Predoc Partner API (v1.4.1) exposes patient management, record-retrieval requests, record uploads, granular clinical document endpoints (medications, labs, imaging, procedures, notes, vaccines, allergies), clinical summaries, and webhook event notifications, secured with short-lived JWT bearer tokens.
image: https://cdn.prod.website-files.com/6827c1994862c627993a82d8/688c883a300cc1480f08f8a1_favicon_32.png
layout: provider
mcp_servers:
- description: ''
  name: Predoc MCP Server
  slug: predoc-mcp-server
modified: '2026-07-20'
name: Predoc
nav: Providers
network: true
overview: 'Predoc publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Medical Records, Health Information Exchange, and FHIR.


  The Predoc catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Predoc''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, changelog, authentication, and 21 more developer resources.'
random_paper: 7
score:
  band: developing
  composite: 48.9
  coverage:
    artifact_dirs: 16
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.3
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 53.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 39.5
  previous_composite: 49.2
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 47.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/predoc/refs/heads/main/screenshots/predoc-2026-08-17T081335.png
security:
- kind: authentication
  name: Predoc Authentication
  slug: predoc-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Predoc Domain Security
  slug: predoc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Predoc Trust Center
  slug: predoc-trust-center
  summary_line: SOC 2 Type II, HIPAA, FDA 21 CFR Part 11
slug: predoc
tags:
- Company
- Healthcare
- Medical Records
- Health Information Exchange
- FHIR
- Clinical Data
- Artificial Intelligence
- Interoperability
- EHR Integration
- Webhook
- Clinical Research
website: https://www.predoc.ai
---
