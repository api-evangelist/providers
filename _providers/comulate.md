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
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://comulate.com
- group: start
  title: ''
  type: Login
  url: https://app.comulate.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://comulate.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://comulate.com/terms-of-use
- group: operate
  title: ''
  type: Support
  url: mailto:support@comulate.com
- group: operate
  title: ''
  type: StatusPage
  url: https://trust.comulate.com
- group: auth
  title: ''
  type: Compliance
  url: https://comulate.com/security
- group: auth
  title: ''
  type: Security
  url: https://comulate.com/security
- group: auth
  title: ''
  type: DomainSecurity
  url: security/comulate-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/comulate-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/comulate-trust-center.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/comulate-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/comulate-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/comulate-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/comulate-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/comulate-packages.yml
coverage:
  checked: '2026-08-14'
  detail: api.comulate.com is a live first-party Comulate API host whose root health check returns 200 but which answers HTTP 401 "Unauthorized" on every other path including /openapi.json, and Comulate publishes no developer portal at all (comulate.com/developers returns 404 and docs.comulate.com does not resolve), so the contract is reachable only by contracted broker customers.
  evidence:
  - status: 200
    url: https://api.comulate.com/
  - status: 401
    url: https://api.comulate.com/openapi.json
  - status: 404
    url: https://www.comulate.com/developers
  reason: customer-only-docs
  state: gated
created: '2026-07-17'
description: Comulate is an accounting automation and revenue intelligence platform built for large insurance brokers. It captures carrier statement data across spreadsheets, PDFs, and email, then automatically reconciles direct-bill and carrier-payables transactions against policies to eliminate manual back-office accounting work. Its Revenue Intelligence layer adds commission forecasting, variance tracking, and missing-commission detection. Comulate is delivered as a hosted application at app.comulate.com with native connectors to broker management systems including Epic, BenefitPoint, AMS360, Microsoft Dynamics, and Salesforce. The company was surfaced as a Bond Capital portfolio company and enriched in the API Evangelist network; it publishes no public developer API or documentation as of this profile.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/comulate.png
layout: provider
modified: '2026-08-14'
name: Comulate
nav: Providers
network: true
overview: 'Comulate is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurance, Insurtech, Accounting, and Reconciliation.


  Comulate''s developer surface includes support and 15 more developer resources.'
plans:
- name: Comulate Plans Pricing
  plan_count: 0
  slug: comulate-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Comulate Rate Limits
  slug: comulate-rate-limits
score:
  band: emerging
  composite: 21.7
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 21.7
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 45.5
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/comulate/refs/heads/main/screenshots/comulate-2026-07-25T210210.png
security:
- kind: domain-security
  name: Comulate Domain Security
  slug: comulate-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Comulate Vulnerability Disclosure
  slug: comulate-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Comulate Trust Center
  slug: comulate-trust-center
  summary_line: SOC 2 Type II, SOC 1 Type II
slug: comulate
tags:
- Company
- Insurance
- Insurtech
- Accounting
- Reconciliation
- Automation
- Revenue Intelligence
- Fintech
- Insurance Brokers
website: https://comulate.com
---
