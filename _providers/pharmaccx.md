---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
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
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pharmaccx-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ccx.tech/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ccx.tech/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://marketaccess.ccxterminal.com/login
- group: operate
  title: ''
  type: Support
  url: mailto:support@ccx.tech
created: '2026-07-17'
description: 'PharmaCCX, operating as CCX (Contingent Commitment Exchange), is a digital market-access and pricing software company for the pharmaceutical industry, serving pharma manufacturers, payers, and health systems. Its enterprise platform provides a single source of truth for global pricing strategy and contract management through three products: CCX Planning (contract scenario planning, modeling, and analysis), Deal Admin (contract administration and pharma-payer coordination), and CCX Digital Negotiation (an invite-only deal negotiation tool). The platform is delivered as an invite-only enterprise SaaS terminal (marketaccess.ccxterminal.com) with Terminal and Sandbox environments; no public developer API, documentation, or portal is published as of this profiling.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pharmaccx.png
layout: provider
modified: '2026-07-20'
name: PharmaCCX
nav: Providers
network: true
overview: 'PharmaCCX is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Pharmaceuticals, Market Access, and Pricing.


  PharmaCCX''s developer surface includes support and 4 more developer resources.'
random_paper: 6
score:
  band: minimal
  composite: 8.5
  delta: 0.0
  facets:
    access_clarity: 17.1
    commercial_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: domain-security
  name: Pharmaccx Domain Security
  slug: pharmaccx-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: pharmaccx
tags:
- Company
- Healthcare
- Pharmaceuticals
- Market Access
- Pricing
- Contract Management
- Payers
- Enterprise Saas
website: https://www.ccx.tech/
---
