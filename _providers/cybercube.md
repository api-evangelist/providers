---
agent_readiness:
  band: agent-aware
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
    well_known_catalog: true
  schema_version: 0.2
  score: 6.8
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: CyberConnect is CyberCube's API layer for integrating its cyber risk models, analytics and signals into a customer's own systems. CyberCube advertises API capabilities across catastrophe risk manageme
  name: CyberConnect
  slug: cyberconnect
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.cybcube.com/
- group: start
  title: ''
  type: Login
  url: https://login.cybcube.com/
- group: operate
  title: ''
  type: Support
  url: https://www.cybcube.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cybcube.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cybcube.com/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://www.cybcube.com/news/2020/07/cybercube-completes-soc-2-type-ii-certification-demonstrating-level-of-customer-data-security
- group: design
  title: ''
  type: Conformance
  url: conformance/cybercube-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cybercube-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cybercube-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/cybercube-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cybercube-rate-limits.yml
coverage:
  checked: '2026-08-11'
  detail: CyberCube's Atlas documentation portal ships a SwaggerUI/apidom OpenAPI renderer in its JS bundle but serves every anonymous request the same 2,259-byte login shell, and the production API host api.cybcube.com answers unauthenticated calls with an AWS API Gateway MissingAuthenticationTokenException — the specification exists, only its distribution is closed.
  evidence:
  - status: 403
    url: https://api.cybcube.com/openapi.json
  - status: 200
    url: https://docs.atlas.cybcube.com/openapi.json
  - status: 403
    url: https://api.docs.atlas.cybcube.com/
  - status: 404
    url: https://www.cybcube.com/llms.txt
  reason: customer-only-docs
  state: gated
created: '2026-08-11'
description: CyberCube is a cyber risk analytics provider for the insurance industry — brokers, insurers, reinsurers and cyber ILS investors — translating cyber risk into quantified financial impact. Its product line spans Account Manager (single-risk underwriting), Portfolio Manager (portfolio aggregation and catastrophe loss modeling), Broking Manager, Exposure Manager, SPoF Intelligence (digital supply-chain single points of failure) and the Industry Exposure Databases. CyberConnect is the company's API layer, marketed as a way to deliver CyberCube models, insights and signals into a customer's own underwriting, exposure-management and capital-modeling workflows, spanning catastrophe risk management, risk scoring, financial loss modeling, reinsurance modeling, SPoF intelligence, risk intelligence and threat modeling. The CyberConnect reference and the Atlas documentation portal sit behind a customer login, and the production API host answers unauthenticated requests with an AWS API Gateway
  authentication challenge.
image: https://www.cybcube.com/hubfs/cybercube-logo-white.svg
layout: provider
modified: '2026-08-11'
name: CyberCube
nav: Providers
network: true
overview: 'CyberCube publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cyber Risk, Insurance, Analytics, and Risk Modeling.


  CyberCube''s developer surface includes support and 10 more developer resources.'
plans:
- name: Cybercube Plans Pricing
  plan_count: 0
  slug: cybercube-plans-pricing
random_paper: 108
rate_limits:
- limit_count: 0
  name: Cybercube Rate Limits
  slug: cybercube-rate-limits
score:
  band: emerging
  composite: 22.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 0.0
    developer_ergonomics: 4.3
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 36.4
  schema_version: 0.11.0
  scored_at: '2026-08-12'
security:
- kind: domain-security
  name: Cybercube Domain Security
  slug: cybercube-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cybercube
tags:
- Company
- Cyber Risk
- Insurance
- Analytics
- Risk Modeling
- Cybersecurity
- Reinsurance
- Catastrophe Modeling
- Underwriting
- InsurTech
website: https://www.cybcube.com/
---
