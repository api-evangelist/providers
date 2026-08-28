---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/limra-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.limra.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/limra
- group: docs
  title: ''
  type: Documentation
  url: https://www.limra.com/en/solutions-and-services/data-exchange-standards/
- group: docs
  title: ''
  type: Documentation
  url: https://www.limra.com/en/solutions-and-services/data-exchange-standards/standards-documentation/
- group: company
  title: ''
  type: Website
  url: https://www.limra.com/en/research/
- group: commercial
  title: ''
  type: Plans
  url: plans/limra-plans-pricing.yml
created: '2026-07-11'
description: LIMRA is a member-based research and trade association for the life insurance and financial services industry, operating alongside LOMA under the LL Global umbrella. It provides industry research, sales and market data, benchmarking, experience studies, and professional development to member companies - primarily life insurers, annuity providers, and workplace benefits carriers. LIMRA does not operate a public developer API or developer portal. Its research, benchmarking, and experience-study data are delivered through the member-gated LIMRA.com portal, reports, and consortium programs rather than a programmatic interface. LIMRA's most API-relevant offering is the LIMRA Data Exchange (LDEx) Standards - free, industry-developed data exchange standards for workplace benefits (benefits enrollment management, benefits configuration management, and evidence of insurability) that define payloads in XML and JSON and, in recent releases, REST endpoints specified in OpenAPI 3.1. LDEx
  is a specification that insurance carriers and benefits administration platforms implement between themselves; LIMRA publishes the standard (registration required to download, membership not required) but does not host any live endpoints. This entry is an honest documentation stub kept for catalog completeness; it will be updated if LIMRA ever ships a hosted public API.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/limra.png
layout: provider
modified: '2026-07-11'
name: LIMRA
nav: Providers
network: true
overview: 'LIMRA is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Life Insurance, Insurance Research, Benchmarking, Financial-Services, and Employee Benefits.


  LIMRA''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Limra Plans Pricing
  plan_count: 2
  slug: limra-plans-pricing
random_paper: 8
score:
  band: minimal
  composite: 8.4
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 9.1
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/limra/refs/heads/main/screenshots/limra-2026-07-25T225211.png
security:
- kind: domain-security
  name: Limra Domain Security
  slug: limra-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: limra
tags:
- Life Insurance
- Insurance Research
- Benchmarking
- Financial-Services
- Employee Benefits
- Data Exchange Standards
- Trade Association
- No Public API
website: https://www.limra.com
---
