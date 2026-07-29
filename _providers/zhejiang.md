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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
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
  score: 12.2
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: Zhejiang University's unified identity authentication platform, a Central Authentication Service (CAS) single sign-on login used to access campus systems. It supports username/password, QR-code scanni
  name: Unified Identity Authentication (CAS / SSO)
  slug: sso
- description: Zhejiang University operates a Shibboleth SAML 2.0 Identity Provider (entityID https://idp.zju.edu.cn/idp/shibboleth) used for federated single sign-on to external academic resources and services. Thi
  name: Shibboleth Identity Provider (SAML)
  slug: shibboleth
artifact_total: 8
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/zhejiang-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zhejiang-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.zju.edu.cn/english/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/zjulug
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/zhejiang-university/
- group: auth
  title: ''
  type: Authentication
  url: https://zjuam.zju.edu.cn/cas/login?locale=en
- group: commercial
  title: ''
  type: Plans
  url: plans/zhejiang-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/zhejiang-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/zhejiang-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: other
  title: ''
  type: ProductPage
  url: https://mirrors.zju.edu.cn/
created: '2026-06-03'
description: 'Zhejiang University (ZJU) is a comprehensive public research university based in Hangzhou, Zhejiang Province, China, ranked #44 in the QS World University Rankings 2025. ZJU is one of China''s oldest and most selective institutions, with strengths across AI, engineering, medicine, and the sciences. ZJU does not publish a centralized, public developer portal or documented open API program. Its confirmable public technical surface is limited to infrastructure endpoints: a unified identity / single sign-on (CAS + Shibboleth SAML IdP) platform and a community-run open-source software mirror, alongside numerous research-lab GitHub organizations. No open, self-service application APIs were found at the time of review.'
finops:
- name: Zhejiang Finops
  service_category: Education
  slug: zhejiang-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zhejiang.png
jsonld:
- class_count: 13
  name: Zhejiang Context
  property_count: 3
  slug: zhejiang-context
layout: provider
modified: '2026-07-25'
name: Zhejiang University
nav: Providers
network: true
overview: 'Zhejiang University publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and China.


  The Zhejiang University catalog on APIs.io includes 1 JSON-LD context.


  Zhejiang University''s developer surface includes GitHub presence, authentication, and 9 more developer resources.'
plans:
- name: Zhejiang Plans Pricing
  plan_count: 2
  slug: zhejiang-plans-pricing
random_paper: 48
rate_limits:
- limit_count: 1
  name: Zhejiang Rate Limits
  slug: zhejiang-rate-limits
score:
  band: emerging
  composite: 21.5
  delta: -2.9
  facets:
    commercial_clarity: 28.9
    contract_quality: 12.9
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 24.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zhejiang/refs/heads/main/screenshots/zhejiang-2026-06-20T201856.png
security:
- kind: domain-security
  name: Zhejiang Domain Security
  slug: zhejiang-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Zhejiang Vulnerability Disclosure
  slug: zhejiang-vulnerability-disclosure
  summary_line: disclosure policy published
slug: zhejiang
tags:
- Education
- Higher Education
- University
- Research
- China
- Identity
- SSO
website: https://www.zju.edu.cn/english/
---
