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
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.9
  scored_at: '2026-09-05'
api_count: 2
apis:
- baseURL: https://api.godiligent.ai
  baseurl_source: declared
  description: Customer Due Diligence
  name: Diligent CDD API
  slug: diligent-cdd-api
- baseURL: https://api.godiligent.ai
  baseurl_source: declared
  description: Company Information
  name: Diligent Company API
  slug: diligent-company-api
- baseURL: https://api.godiligent.ai
  baseurl_source: declared
  description: Instant Website Screening API
  name: Diligent Instant Screening (experimental) API
  slug: diligent-instant-screening-experimental-api
- baseURL: https://api.godiligent.ai
  baseurl_source: declared
  description: Website monitoring and alerts for changes and risks
  name: Diligent Monitorings API
  slug: diligent-monitorings-api
- baseURL: https://api.godiligent.ai
  baseurl_source: declared
  description: Name screening remediation
  name: Diligent Name Screening API
  slug: diligent-name-screening-api
- baseURL: https://api.godiligent.ai
  baseurl_source: declared
  description: '## How to Secure Webhook Deliveries To ensure that webhook payloads are securely transmitted and verified. This guide explains how to configure and validate webhook deliveries using a shared secret. #'
  name: Diligent Webhooks API
  slug: diligent-webhooks-api
artifact_total: 17
asyncapis:
- description: ''
  name: Diligent Webhooks
  slug: diligent-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Diligent CDD API
  slug: open-diligent-cdd-api
- collection_type: open
  name: Diligent CDD Company API
  slug: open-diligent-company-api
- collection_type: open
  name: Diligent CDD Instant Screening (experimental) API
  slug: open-diligent-instant-screening-experimental-api
- collection_type: open
  name: Diligent CDD Monitorings API
  slug: open-diligent-monitorings-api
- collection_type: open
  name: Diligent CDD Name Screening API
  slug: open-diligent-name-screening-api
- collection_type: open
  name: Diligent CDD Webhooks API
  slug: open-diligent-webhooks-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/diligent-api-overlay.yaml
- group: auth
  title: ''
  type: TrustCenter
  url: security/diligent-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/diligent-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/diligent-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.godiligent.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.godiligent.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.godiligent.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.godiligent.ai/guides/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.godiligent.ai/guides/introduction
- group: start
  title: ''
  type: Login
  url: https://app.godiligent.ai/
- group: operate
  title: ''
  type: Support
  url: https://docs.godiligent.ai/support
- group: company
  title: ''
  type: Blog
  url: https://www.godiligent.ai/news
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.godiligent.ai/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.godiligent.ai/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.godiligent.ai/
- group: auth
  title: ''
  type: Compliance
  url: https://www.godiligent.ai/security
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/godiligentai
- group: company
  title: ''
  type: Twitter
  url: https://x.com/goDiligent
- group: build
  title: ''
  type: Postman
  url: https://raw.githubusercontent.com/paylaneio/api/refs/heads/master/postman_collection.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/diligent-llms.txt
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/diligent-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/diligent-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/diligent-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/diligent-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/diligent-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/diligent-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/diligent-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/diligent-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/diligent-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Diligent (Diligent AI, godiligent.ai) builds autonomous AI agents for financial-crime compliance, automating the reasoning-heavy KYC/AML workflows that banks and fintechs run at scale. Its API exposes Customer Due Diligence (CDD) and business/merchant verification, name screening against sanctions and PEP providers with AI-powered alert remediation, ongoing monitoring with alerting, company identification and registry document retrieval, a blocked-company list, and an experimental instant website screening endpoint. The platform is API-first (X-API-KEY auth, production and sandbox environments, idempotency, and signed webhooks) and is used by fintechs and banks including Scalapay, Flywire, Allica Bank, Tamara, Teya, Vivid and Alma. Diligent is SOC 2 Type II certified, ISO 27001 certified, and GDPR compliant. It is backed by Speedinvest, Y Combinator and Shapers, and operates out of London and Berlin.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/diligent.png
layout: provider
modified: '2026-07-18'
name: Diligent
nav: Providers
network: true
overview: 'Diligent publishes 6 APIs on the [APIs.io](https://apis.io/) network, including CDD API, Company API, Instant Screening (experimental) API, and 3 more. Tagged areas include Company, Compliance, RegTech, KYC, and AML.


  The Diligent catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Diligent''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, sandbox, and 23 more developer resources.'
random_paper: 8
score:
  band: developing
  composite: 47.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 4.5
    contract_quality: 59.6
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 15.8
  previous_composite: 46.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/diligent/refs/heads/main/screenshots/diligent-2026-07-25T212039.png
security:
- kind: authentication
  name: Diligent Authentication
  slug: diligent-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Diligent Domain Security
  slug: diligent-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Diligent Trust Center
  slug: diligent-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: diligent
tags:
- Company
- Compliance
- RegTech
- KYC
- AML
- Financial Crime
- Due Diligence
- Screening
- Sanctions
- Monitoring
- Artificial Intelligence
- Fintech
- Webhook
website: https://www.godiligent.ai
---
