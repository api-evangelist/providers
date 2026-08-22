---
access_model:
  confidence: high
  label: Public spec, gated credentials
  onboarding: unknown
  pricing: unknown
  public: true
  source:
  - https://docs.ritten.io/
  - https://docs.ritten.io/swagger/openapi.yaml
  - https://www.ritten.io/
  trial: false
  try_now: false
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.9
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: 'The Ritten External API is the public REST contract for Ritten integrating partners. It covers patients (create, read, patch, vitals, forms, relationships, attachments, external-id lookup), contacts, '
  name: Ritten External API
  slug: ritten-external-api
artifact_total: 6
asyncapis:
- description: ''
  name: Ritten Webhooks
  slug: ritten-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://ritten.io
- group: company
  title: ''
  type: Blog
  url: https://www.ritten.io/blog
- group: operate
  title: ''
  type: Support
  url: https://www.ritten.io/support
- group: start
  title: ''
  type: Login
  url: https://secure.ritten.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ritten.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ritten.io/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://www.ritten.io/
- group: design
  title: ''
  type: Conformance
  url: conformance/ritten-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ritten-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.ritten.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ritten.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.ritten.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rittenlabs
- group: auth
  title: ''
  type: Authentication
  url: authentication/ritten-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ritten-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ritten-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ritten-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ritten-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ritten-plans-pricing.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/ritten-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ritten-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/ritten-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/ritten-external-api-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ritten-llms.txt
created: '2026-07-17'
description: Ritten is a cloud-based electronic medical record (EMR), CRM and revenue-cycle platform built specifically for behavioral health and substance-use treatment organizations - detox, residential, PHP/IOP, and outpatient providers. Its browser-based product covers clinical documentation (group and individual notes, AI-assisted charting), scheduling, revenue-cycle management (claims, billing, authorizations), a HIPAA-compliant patient portal, treatment planning, compliance tooling (audit trails, signature routing), and outcomes reporting. Ritten publishes a public REST contract for integrating partners - the Ritten External API - documented with an OpenAPI 3.1.0 definition covering 56 paths, 71 operations and 93 schemas across patients, contacts, CRM cases, programs, facilities, organizations, tasks, encounters, forms, insurance payers, users and a 17-operation insights and reporting family, plus six webhook events. Authentication is OAuth 2.0 client_credentials with a required X-Ritten-Tenant
  header selecting the clinic instance; credentials are provisioned by Ritten to partners rather than self-service. Ritten is built for HIPAA-regulated and 42 CFR Part 2 confidentiality requirements with role-based access controls and audit logs, and supports operational integrations for e-prescribing, labs, eligibility/billing clearinghouses, and telehealth. Backed by 8VC and Threshold Ventures; based in Philadelphia, PA.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ritten.png
layout: provider
modified: '2026-08-15'
name: Ritten
nav: Providers
network: true
overview: 'Ritten publishes 1 API on the [APIs.io](https://apis.io/) network: External API. Tagged areas include Company, Behavioral Health, EMR, EHR, and Healthcare.


  The Ritten catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Ritten''s developer surface includes engineering blog, support, documentation, API reference, authentication, sandbox, and 19 more developer resources.'
plans:
- name: Ritten Plans Pricing
  plan_count: 0
  slug: ritten-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 3
  name: Ritten Rate Limits
  slug: ritten-rate-limits
score:
  band: developing
  composite: 52.6
  delta: 4.6
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 30.3
    contract_quality: 60.6
    developer_ergonomics: 54.2
    discoverability: 75.9
    governance: 30.3
    operational_transparency: 42.1
  previous_composite: 48.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ritten/refs/heads/main/screenshots/ritten-2026-08-17T081615.png
security:
- kind: authentication
  name: Ritten Authentication
  slug: ritten-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Ritten Domain Security
  slug: ritten-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: ritten
tags:
- Company
- Behavioral Health
- EMR
- EHR
- Healthcare
- Practice Management
- HIPAA
- Revenue Cycle Management
- Clinical Documentation
- Telehealth
- API
- OpenAPI
- Webhooks
- Behavioral Health API
- Substance Use Treatment
- 42 CFR Part 2
- Electronic Health Records
website: https://ritten.io
---
