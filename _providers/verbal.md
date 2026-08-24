---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://tryverbal.com
- group: company
  title: ''
  type: Blog
  url: https://tryverbal.com/blog
- group: start
  title: ''
  type: Login
  url: https://app.tryverbal.com
- group: start
  title: ''
  type: SignUp
  url: https://tryverbal.com/demo
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tryverbal.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tryverbal.com/terms-and-conditions
- group: auth
  title: ''
  type: DomainSecurity
  url: security/verbal-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Salusive
- group: auth
  title: ''
  type: Compliance
  url: https://www.tryverbal.com/features/secure-hipaa-compliant
- group: design
  title: ''
  type: Conformance
  url: conformance/verbal-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/verbal-llms.txt
coverage:
  checked: '2026-08-14'
  detail: Verbal ships only an end-user SaaS app and a Chrome extension; the "simple API connection" language on its integrations pages is Verbal calling RingCentral, NICE and Healthie, and its own app backend (svc-amd.app.tryverbal.com, FastAPI) has /docs, /redoc and /openapi.json all disabled behind a CORS allow-list pinned to app.tryverbal.com.
  evidence:
  - status: 404
    url: https://www.tryverbal.com/developers
  - status: 404
    url: https://www.tryverbal.com/docs
  - status: 404
    url: https://svc-amd.app.tryverbal.com/openapi.json
  - status: 200
    url: https://svc-amd.app.tryverbal.com/health
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: Verbal (tryverbal.com), from Salusive Health, is an AI-powered clinical compliance and quality-assurance platform for healthcare organizations. It automatically audits patient interactions — phone and video calls, telehealth visits, AI-agent conversations, and clinical chart notes — against customizable regulatory and quality checklists, scoring compliance in real time and surfacing gaps for supervisors and QA teams. Verbal connects to communications and EHR platforms including RingCentral, NICE, Zoom, Five9, Healthie, Epic, and Athena, and ships a Chrome extension for clinicians. It publishes a healthcare compliance posture — HIPAA compliant, HITRUST certified, CPRA, BAAs with all customers, PII redaction and US data residency. As of this enrichment pass the company exposes no public developer API — the API language on its site describes Verbal consuming partner platform APIs, not an API it publishes, and there is no developer portal, reference, machine-readable spec, or SDK
  on any Verbal host. Backed by 500 Global.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/verbal.png
layout: provider
modified: '2026-07-21'
name: Verbal
nav: Providers
network: true
overview: 'Verbal is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Compliance, Artificial Intelligence, and Quality Assurance.


  Verbal''s developer surface includes engineering blog, signup flow, and 9 more developer resources.'
plans:
- name: Verbal Plans Pricing
  plan_count: 0
  slug: verbal-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Verbal Rate Limits
  slug: verbal-rate-limits
score:
  band: emerging
  composite: 18.9
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 18.9
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 30.0
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: domain-security
  name: Verbal Domain Security
  slug: verbal-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: verbal
tags:
- Company
- Healthcare
- Compliance
- Artificial Intelligence
- Quality Assurance
- Clinical Documentation
- Conversation Intelligence
website: https://tryverbal.com
---
