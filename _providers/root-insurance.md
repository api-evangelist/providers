---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: iOS and Android app that measures driving behavior via smartphone telematics, generates a usage-based price, and handles enrollment, policy management, and claims (3-minute claim filing). Telematics i
  name: Root Consumer Mobile App
  slug: consumer-app
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/root-insurance-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/root-insurance-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.joinroot.com/blog
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/root-insurance-company
- group: company
  title: ''
  type: Website
  url: https://www.joinroot.com/
- group: company
  title: ''
  type: InvestorRelations
  url: https://ir.joinroot.com/
- group: company
  title: ''
  type: Careers
  url: https://www.joinroot.com/careers
- group: commercial
  title: ''
  type: Plans
  url: plans/root-insurance-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/root-insurance-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/root-insurance-finops.yml
created: '2026-05-23'
description: 'Root is a U.S. app-first auto insurer that prices policies primarily on real driving behavior captured by smartphone telematics. The Root mobile app handles enrollment, telematics scoring, policy management, claims, and optional roadside assistance, with renters insurance as an add-on line. Root has reorganized its tech stack around APIs to power embedded auto insurance with partners such as Carvana and Hyundai Capital America; partner APIs are gated and not publicly documented. Note: Root Insurance (joinroot.com) is distinct from the unrelated Root Platform (rootplatform.com) insurtech in South Africa / UK.'
finops:
- name: Root Insurance Finops
  service_category: API
  slug: root-insurance-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/root-insurance.png
layout: provider
modified: '2026-07-25'
name: Root Insurance
nav: Providers
network: true
overview: 'Root Insurance publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Auto, Telematics, Insurtech, and Embedded Insurance.


  Root Insurance''s developer surface includes engineering blog and 9 more developer resources.'
plans:
- name: Root Insurance Plans Pricing
  plan_count: 1
  slug: root-insurance-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 2
  name: Root Insurance Rate Limits
  slug: root-insurance-rate-limits
score:
  band: emerging
  composite: 16.2
  delta: -3.2
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 19.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 18.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/root-insurance/refs/heads/main/screenshots/root-insurance-2026-06-20T193219.png
security:
- kind: domain-security
  name: Root Insurance Domain Security
  slug: root-insurance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Root Insurance Vulnerability Disclosure
  slug: root-insurance-vulnerability-disclosure
  summary_line: disclosure policy published
slug: root-insurance
tags:
- Insurance
- Auto
- Telematics
- Insurtech
- Embedded Insurance
- Mobile
- Usage-Based
website: https://www.joinroot.com/
---
