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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-17'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aktana-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pharmaforceiq.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pharmaforceiq.com/privacy-policy/
- group: company
  title: ''
  type: Blog
  url: https://pharmaforceiq.com/resource-center/
- group: operate
  title: ''
  type: Support
  url: https://pharmaforceiq.com/contact/
- group: auth
  title: ''
  type: TrustCenter
  url: security/aktana-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://pharmaforceiq.com/security-center/
- group: company
  title: ''
  type: Partners
  url: https://pharmaforceiq.com/partners-integrations/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pfiq/
- group: design
  title: ''
  type: Conformance
  url: conformance/aktana-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/aktana-plans-pricing.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://appexchange.salesforce.com/appxListingDetail?listingId=a0N3A00000FAMlzUAH
- group: start
  title: ''
  type: Login
  url: https://app.pharmaforceiq.com/login
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aktana-llms.txt
coverage:
  checked: '2026-08-13'
  detail: The only integration surface — the Aktana Omnichannel Data Interface — is sold and implemented as a professional-services engagement, so its product page publishes a schema layer and pre-built adapters in prose with no endpoint, schema or auth reference, and every CTA on the site routes to /request-a-demo/; the customer help center at support.aktana.com sits behind a Cloudflare bot challenge.
  evidence:
  - status: 200
    url: https://pharmaforceiq.com/aktana-omnichannel-data-interface/
  - status: 404
    url: https://pharmaforceiq.com/pricing/
  - status: 403
    url: https://support.aktana.com/hc/en-us
  - status: 404
    url: https://pharmaforceiq.com/openapi.json
  reason: sales-gate
  state: gated
created: '2026-07-17'
description: 'Aktana is an AI-driven commercial engagement platform for the pharmaceutical and life-sciences industry, now operating as PharmaForceIQ (aktana.com redirects in full to pharmaforceiq.com). The platform provides real-time orchestration that coordinates digital and field marketing across channels ("optichannel") to drive measurable script lift and HCP (healthcare provider) adoption, with NPI-level dashboards tying engagement to outcomes for HCP marketing, DTC marketing, medical affairs, omnichannel, sales, and commercial-leadership teams. The company was surfaced as a portfolio company of Norwest Venture Partners. It publishes no public developer/API surface: integration is delivered as the Aktana Omnichannel Data Interface (a CRM-agnostic data schema layer with pre-built adapters for Salesforce, Veeva, Adobe Experience Manager, OCE, Tealium and Lytics) and as a Salesforce AppExchange managed package, both sold and implemented through sales engagements rather than documented
  for developers. This profile captures corporate identity, compliance posture (SOC 2 Type II, ISO 27001, HIPAA, CCPA, GDPR), published pricing, and web properties.'
image: https://pharmaforceiq.com/wp-content/uploads/2025/06/PharmaForceIQ_BuiltforLifeSciences.webp
layout: provider
modified: '2026-08-13'
name: Aktana (PharmaForceIQ)
nav: Providers
network: true
overview: 'Aktana (PharmaForceIQ) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Life Sciences, Pharmaceutical, HCP Engagement, and Marketing.


  Aktana (PharmaForceIQ)''s developer surface includes engineering blog, support, pricing, and 11 more developer resources.'
plans:
- name: Aktana Plans Pricing
  plan_count: 1
  slug: aktana-plans-pricing
random_paper: 28
rate_limits:
- limit_count: 0
  name: Aktana Rate Limits
  slug: aktana-rate-limits
score:
  band: emerging
  composite: 24.0
  delta: 11.4
  facets:
    commercial_clarity: 71.1
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 68.5
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 12.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 25.0
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/aktana/refs/heads/main/screenshots/aktana-2026-07-25T195518.png
security:
- kind: domain-security
  name: Aktana Domain Security
  slug: aktana-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Aktana Trust Center
  slug: aktana-trust-center
  summary_line: SOC 2 Type II, ISO 27001, HIPAA, CCPA, GDPR
slug: aktana
tags:
- Company
- Life Sciences
- Pharmaceutical
- HCP Engagement
- Marketing
- Artificial Intelligence
- Omnichannel
- Commercial Operations
website: https://pharmaforceiq.com
---
