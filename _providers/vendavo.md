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
  url: http://www.vendavo.com/
- group: company
  title: ''
  type: Blog
  url: https://www.vendavo.com/insights/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.vendavo.com/company/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.vendavo.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vendavo.com/privacy-policy/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vendavo-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vendavo-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/vendavo
- group: auth
  title: ''
  type: TrustCenter
  url: security/vendavo-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/vendavo-trust-center.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/vendavo-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/vendavo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/vendavo-rate-limits.yml
coverage:
  checked: '2026-08-13'
  detail: Vendavo's only product documentation portal, one.vendavo.com, 301s to vendavoinc.atlassian.net/wiki/spaces/doc/overview which then 302s to an Atlassian ID login, and the support portal 302s to a Salesforce Community login, so the API reference behind Vendavo's marketed "real-time APIs" is readable only with an active tenant.
  evidence:
  - status: 301
    url: https://one.vendavo.com/
  - status: 302
    url: https://vendavoinc.atlassian.net/wiki/spaces/doc/overview
  - status: 301
    url: https://support.vendavo.com/
  - status: 404
    url: https://www.vendavo.com/openapi.json
  - status: 404
    url: https://www.vendavo.com/.well-known/agent-card.json
  reason: customer-only-docs
  state: gated
created: '2026-07-17'
description: 'Vendavo is an enterprise B2B commercial-excellence software company whose platform helps manufacturers and distributors optimize pricing, automate quoting and agreements, and manage rebate and incentive programs using AI-powered pricing intelligence and margin analytics. Vendavo has been named a Leader in the Gartner Magic Quadrant for B2B Pricing & Rebate Optimization Software and integrates with enterprise ERP, CRM, and eCommerce systems. Vendavo markets "real-time APIs for dynamic pricing and quoting workflows" alongside batch and file-based integration, but as of this enrichment pass it publishes no public developer portal, API reference or machine-readable contract: the Vendavo Documentation Portal (one.vendavo.com) redirects to an Atlassian ID login and the support portal to a Salesforce Community login, so the integration surface is reachable only by contracted customers and partners. Vendavo does publish a substantive public security posture — ISO/IEC 27001:2022, annual
  SOC 1 and SOC 2 Type 2 audits, a CSA STAR CAIQ self-assessment and a Trust Center at trustvault.vendavo.com. This profile was seeded as a portfolio lead of DCM Ventures and Sapphire Ventures.'
image: https://www.vendavo.com/wp-content/uploads/2026/04/Image-2-1024x431.png
layout: provider
modified: '2026-08-13'
name: Vendavo
nav: Providers
network: true
overview: 'Vendavo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise, Pricing, CPQ, and Quoting.


  Vendavo''s developer surface includes engineering blog, support, and 11 more developer resources.'
plans:
- name: Vendavo Plans Pricing
  plan_count: 0
  slug: vendavo-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Vendavo Rate Limits
  slug: vendavo-rate-limits
score:
  band: emerging
  composite: 17.0
  delta: 0.4
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 16.6
  provenance:
    conformance: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: domain-security
  name: Vendavo Domain Security
  slug: vendavo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Vendavo Trust Center
  slug: vendavo-trust-center
  summary_line: ISO/IEC 27001:2022, SOC 1 Type 2, SOC 2 Type 2, CSA STAR Level 1 (CAIQ self-assessment), ISO 22301
slug: vendavo
tags:
- Company
- Enterprise
- Pricing
- CPQ
- Quoting
- Rebates
- B2B
- Commercial Optimization
- Margin Optimization
- AI
website: http://www.vendavo.com/
---
