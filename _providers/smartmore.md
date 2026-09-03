---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://global.smartmore.com/
- group: company
  title: ''
  type: About
  url: https://global.smartmore.com/company.html
- group: operate
  title: ''
  type: Support
  url: https://global.smartmore.com/contact-us.html
- group: company
  title: ''
  type: Blog
  url: https://global.smartmore.com/blogs.html
- group: company
  title: ''
  type: News
  url: https://global.smartmore.com/news.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://global.smartmore.com/terms-of-use.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://global.smartmore.com/privacy.html
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/smartmore-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/smartmore-domain-security.yml
coverage:
  checked: '2026-08-28'
  detail: SmartMore sells the SMore ViMo vision platform and its own camera/sensor hardware as licensed end-user products and publishes no developer surface at all — api., developer. and docs.smartmore.com do not resolve in DNS, every /.well-known/ path on global., inside., cn. and www.smartmore.com returns a hard 404, no OpenAPI/Swagger/GraphQL/AsyncAPI contract exists on any host, and the "export to SDK" ViMo Deeplearning advertises has no public download, reference, or package in npm, PyPI or crates.io. (The platform answers HTTP 200 with an empty body for arbitrary non-existent file paths, so a 200 from these hosts is a catch-all, not a document.)
  evidence:
  - status: 0
    url: https://developer.smartmore.com/
  - status: 0
    url: https://api.smartmore.com/
  - status: 404
    url: https://global.smartmore.com/.well-known/api-catalog
  - status: 404
    url: https://global.smartmore.com/.well-known/agent-card.json
  - status: 404
    url: https://inside.smartmore.com/.well-known/security.txt
  - status: 200
    url: https://global.smartmore.com/company.html
  reason: no-developer-program
  state: none
created: '2026-08-28'
description: SmartMore Corporation (思谋科技) is a Hong Kong- and Shenzhen-headquartered industrial AI and machine vision company founded in 2019, building products and solutions for smart manufacturing and digital innovation. Its flagship SMore ViMo platform bundles ViMo Cloud, ViMo Deeplearning and ViMo Studio into a low-code industrial vision stack covering data management, model training, visual solution design and production-line deployment, and is sold alongside first-party hardware — industrial smart cameras, barcode readers (VS600/VS800P/VS1000/VS2000), vision sensors (VN2000/VN4000) and lenses — through the SmartMoreInside sub-brand. The company also markets digital platforms (Light3D, Data, Gauge, AIoT) and industrial large models (IndustryGPT, SMore LrMo). SmartMore states it has filed 400+ global patent applications with 200+ granted, served 200+ enterprise customers, and reached unicorn status on a Series B that exceeded USD 200 million in 2021, with R&D and business centers in
  Hong Kong, Shenzhen, Shanghai, Suzhou, Tokyo, Beijing, Hangzhou and Singapore. As of this pass the company publishes no public developer program, API reference or machine-readable contract; ViMo model export to an SDK is described in marketing copy but is delivered with the licensed product rather than documented publicly.
image: https://global.smartmore.com/upload/sysconfigs/2024-02/65dff166cb8a2.png
layout: provider
modified: '2026-08-28'
name: SmartMore
nav: Providers
network: true
overview: 'SmartMore is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Industrial AI, Machine Vision, Computer-Vision, and Smart Manufacturing.


  SmartMore''s developer surface includes support, engineering blog, product news, and 6 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 10.6
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.6
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/smartmore/refs/heads/main/screenshots/smartmore-2026-09-02T155939.png
security:
- kind: domain-security
  name: Smartmore Domain Security
  slug: smartmore-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: smartmore
tags:
- Company
- Industrial AI
- Machine Vision
- Computer-Vision
- Smart Manufacturing
- Quality Inspection
- Deep Learning
- Industrial Automation
- Edge AI
- Hardware
website: https://global.smartmore.com/
---
