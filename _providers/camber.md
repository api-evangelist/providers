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
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.camber.health
- group: company
  title: ''
  type: About
  url: https://www.camber.health/company
- group: start
  title: ''
  type: SignUp
  url: https://app.camber.health/login
- group: start
  title: ''
  type: Login
  url: https://app.camber.health/login
- group: company
  title: ''
  type: Blog
  url: https://www.camber.health/company/news
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.camber.health/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.camber.health/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://www.camber.health/responsible-disclosure
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/camber-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/camber-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/camberhealth/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Juniper-Health
- group: auth
  title: ''
  type: Compliance
  url: https://www.camber.health/platform
- group: design
  title: ''
  type: Conformance
  url: conformance/camber-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/camber-llms.txt
coverage:
  checked: '2026-08-15'
  detail: 'Camber runs a real production API at api.camber.health (AWS API Gateway behind Cloudflare) that answers HTTP 401 with `WWW-Authenticate: Bearer` on every single path — including /openapi.json and every /.well-known/* path — and it publishes no developer portal, reference or docs host at all (docs.camber.health and developer.camber.health do not resolve), so the contract is readable only by an authenticated customer.'
  evidence:
  - status: 401
    url: https://api.camber.health/openapi.json
  - status: 401
    url: https://api.camber.health/
  - status: 404
    url: https://www.camber.health/developers
  - status: 404
    url: https://www.camber.health/llms.txt
  reason: customer-only-docs
  state: gated
created: '2026-07-17'
description: Camber is a healthcare revenue cycle management (RCM) and medical billing software platform purpose-built for specialty care providers, including ABA (applied behavior analysis) therapy, physical therapy, and ENT and allergy clinics. The platform automates the full claims lifecycle — creation and submission, pre-submission scrubbing and eligibility verification, payment posting and reconciliation, and denial management and prevention — using a rules engine and AI trained on billions of dollars in real claims data, combined with human review where judgment matters. Founded in 2021 (Y Combinator W21, rebranded from Juniper Behavioral Health to Camber), the New York-based company is backed by Craft Ventures, a16z, and Y Combinator, and processes over a million claims annually for hundreds of specialty care providers across all 50 states.
image: https://rwqqrnsxhishecvdnalx.supabase.co/storage/v1/object/public/assets/8c14c2ae-b41e-4c31-8afb-9c947abb4801/02740e5b-c5e3-4202-8bfc-6fdab7588fc5.png
layout: provider
modified: '2026-08-15'
name: Camber
nav: Providers
network: true
overview: 'Camber is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, Revenue Cycle Management, and Medical Billing.


  Camber''s developer surface includes signup flow, engineering blog, and 13 more developer resources.'
plans:
- name: Camber Plans Pricing
  plan_count: 0
  slug: camber-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 0
  name: Camber Rate Limits
  slug: camber-rate-limits
score:
  band: emerging
  composite: 19.8
  delta: -2.2
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 13.2
  previous_composite: 22.0
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/camber/refs/heads/main/screenshots/camber-2026-07-25T204252.png
security:
- kind: domain-security
  name: Camber Domain Security
  slug: camber-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Camber Vulnerability Disclosure
  slug: camber-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: camber
tags:
- Company
- Health
- Healthcare
- Revenue Cycle Management
- Medical Billing
- Claims
- Behavioral Health
- Health Tech
website: https://www.camber.health
---
