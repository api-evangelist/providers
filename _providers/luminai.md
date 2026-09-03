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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/luminai-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/luminai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://luminai.com
- group: company
  title: ''
  type: Blog
  url: https://luminai.com/blog
- group: auth
  title: ''
  type: Compliance
  url: https://luminai.com/security
- group: commercial
  title: ''
  type: TermsOfService
  url: https://luminai.com/terms
created: '2026-07-17'
description: Luminai is an AI-powered automation platform for health system operations, marketed as "The AI Platform for Health System Operations." It automates complex, high-volume healthcare back-office workflows including referral intake and processing, provider inbox automation, patient registration, orders and referrals, pharmacy renewals, payor contract management, denial appeals, and underpayment recovery. The company reports over 12 million automations driven, an average 5.3x ROI, and a 48-day average time to value, with enterprise-grade security and flexible deployment options (on-premises, VPC, or fully managed). Luminai is SOC 2, HIPAA, and GDPR compliant. It is a venture-backed company in the General Catalyst portfolio. Luminai does not publish a public developer API, API documentation, or developer portal at this time; this profile captures its public identity and security posture.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/luminai.png
layout: provider
modified: '2026-07-20'
name: Luminai
nav: Providers
network: true
overview: 'Luminai is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Health System Operations, Automation, and Artificial Intelligence.


  Luminai''s developer surface includes engineering blog and 5 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 10.8
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 18.8
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/luminai/refs/heads/main/screenshots/luminai-2026-07-25T225712.png
security:
- kind: domain-security
  name: Luminai Domain Security
  slug: luminai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Luminai Trust Center
  slug: luminai-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: luminai
tags:
- Company
- Healthcare
- Health System Operations
- Automation
- Artificial Intelligence
- AI Agents
- Workflow-Automation
- Revenue Cycle Management
- Business Process Automation
website: https://luminai.com
---
