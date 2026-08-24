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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lunabill-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lunabill.com
- group: company
  title: ''
  type: Blog
  url: https://lunabill.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lunabill.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lunabill.com/privacy
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.lunabill.com
- group: auth
  title: ''
  type: Compliance
  url: https://lunabill.com/trust
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lunabill-llms.txt
created: '2026-07-17'
description: LunaBill is an AI revenue cycle management (RCM) platform for hospitals, health systems, and RCM/BPO firms, built by LunaHealth Technologies, Inc. and backed by Y Combinator. A coordinated team of AI agents works the entire accounts receivable queue end to end — placing real calls to payers and waiting on hold, navigating IVR phone trees, checking payer portals (Availity, Waystar), working denials, filing appeals, and resubmitting claims — while running inside the EHR and clearinghouses a provider already uses (Epic, Cerner, GoRev, Waystar, Availity) and leaving a full audit trail on every claim. Pricing is performance based (1.5% of net collections recovered, nothing upfront). LunaBill is HIPAA compliant and SOC 2 Type I (Type II in progress). It does not currently publish a public developer API; integration is delivered through EHR and clearinghouse connectors rather than a documented API surface.
image: https://www.lunabill.com/opengraph-image
layout: provider
modified: '2026-07-20'
name: Lunabill
nav: Providers
network: true
overview: 'Lunabill is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Revenue Cycle Management, Medical Billing, and Insurance Claims.


  Lunabill''s developer surface includes engineering blog and 7 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 13.6
  delta: 0.0
  facets:
    access_clarity: 32.9
    commercial_clarity: 32.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 13.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 23.8
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lunabill/refs/heads/main/screenshots/lunabill-2026-07-25T225723.png
security:
- kind: domain-security
  name: Lunabill Domain Security
  slug: lunabill-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Lunabill Trust Center
  slug: lunabill-trust-center
  summary_line: SOC 2 Type I, HIPAA
slug: lunabill
tags:
- Company
- Healthcare
- Revenue Cycle Management
- Medical Billing
- Insurance Claims
- AI Agents
- HIPAA
- Health Tech
website: https://lunabill.com
---
