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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/chrome-river-emburse-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chrome-river-emburse-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.emburse.com/enterprise/
- group: operate
  title: ''
  type: Support
  url: https://help.emburse.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.emburse.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://legal.emburse.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://legal.emburse.com/
- group: start
  title: ''
  type: Login
  url: https://app.chromeriver.com/login
- group: operate
  title: ''
  type: StatusPage
  url: https://status.emburse.com/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.emburse.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/chrome-river-emburse-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: https://www.emburse.com/responsible-disclosure
- group: agent
  title: ''
  type: WellKnown
  url: well-known/chrome-river-emburse-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/chrome-river-emburse-security.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/chrome-river-emburse-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/chrome-river-emburse-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/chrome-river-emburse-llms.txt
created: '2026-07-17'
description: Chrome River is an enterprise travel and expense (T&E) management platform now part of Emburse, offering expense reporting, invoice management, corporate card reconciliation, and travel spend controls for large and global organizations. The chromeriver.com brand now redirects to Emburse Enterprise; expense, invoice, and analytics data are exchanged through Emburse's gated API host (api.emburse.com) and app.chromeriver.com sign-in. Emburse publishes a broad compliance posture (SOC 1/2 Type 2, ISO/IEC 27001/27701/42001, PCI DSS, GDPR/CCPA/CPRA, TX-RAMP) via its trust center and operates a public responsible-disclosure program and Atlassian-hosted status page. This profile was surfaced as a Bain Capital Ventures portfolio lead and enriched by the API Evangelist pipeline from Emburse's public surface; no open developer portal or OpenAPI is published, so spec-bearing artifacts are intentionally absent.
image: https://cdn.sanity.io/images/l5mo20ew/production/d30ee9875c084270cf6a7b0daa1827ae69c0bb09-1200x630.png?fm=jpg&q=75
layout: provider
modified: '2026-07-18'
name: Chrome River (Emburse)
nav: Providers
network: true
overview: 'Chrome River (Emburse) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai Apps, Expense Management, Travel And Expense, and Invoice Management.


  Chrome River (Emburse)''s developer surface includes support, engineering blog, and 15 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 23.7
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 23.7
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 46.9
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/chrome-river-emburse/refs/heads/main/screenshots/chrome-river-emburse-2026-07-25T205304.png
security:
- kind: domain-security
  name: Chrome River Emburse Domain Security
  slug: chrome-river-emburse-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Chrome River Emburse Vulnerability Disclosure
  slug: chrome-river-emburse-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Chrome River Emburse Trust Center
  slug: chrome-river-emburse-trust-center
  summary_line: SOC 1 Type 2, SOC 2 Type 2, ISO/IEC 27001, ISO/IEC 27701, ISO/IEC 42001:2023, PCI DSS, GDPR, CCPA, CPRA, EU-US DPF, TX-RAMP
slug: chrome-river-emburse
tags:
- Company
- Ai Apps
- Expense Management
- Travel And Expense
- Invoice Management
- Corporate Cards
- Spend Management
- Fintech
- Enterprise Software
website: https://www.emburse.com/enterprise/
---
