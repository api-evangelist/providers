---
access_model:
  confidence: high
  label: Sales-gated
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://open.ezrpro.com/#/apiFile/guide/00001
  - https://www.ezrpro.com/contact
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 31.7
  scored_at: '2026-09-02'
api_count: 2
apis:
- description: The EZR 开放平台 integration surface — 236 documented interfaces across 11 business domains (base data, member master data, loyalty points, coupons, sales data, WeChat mall, external mall distribution, me
  name: EZR Open Platform
  slug: ezr-open-platform
- description: 'The KOS (Key Opinion Sales) open platform — EZR''s separate integration surface for guide/associate-led social selling, documented in its own developer guide with its own hosts. It uses the same AppId '
  name: EZR KOS Open Platform
  slug: ezr-kos-open-platform
artifact_total: 7
asyncapis:
- description: ''
  name: Ezr Webhooks
  slug: ezr-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.ezrpro.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://open.ezrpro.com/
- group: docs
  title: ''
  type: Documentation
  url: https://open.ezrpro.com/#/apiFile
- group: docs
  title: ''
  type: APIReference
  url: https://open.ezrpro.com/#/apiFile
- group: start
  title: ''
  type: GettingStarted
  url: https://open.ezrpro.com/#/apiFile/guide/00001
- group: company
  title: ''
  type: Blog
  url: https://www.ezrpro.com/about/news
- group: operate
  title: ''
  type: Support
  url: https://www.ezrpro.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: http://www.ezrpro.com/privacy.html
- group: auth
  title: ''
  type: Authentication
  url: authentication/ezr-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ezr-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ezr-status-codes.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/ezr-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ezr-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ezr-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ezr-plans-pricing.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/ezr-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ezr-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/ezr-changelog.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/ezr-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ezr-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ezr-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ezr-llms.txt
created: '2026-07-17'
description: EZR (上海驿氪 / Shanghai EasyRetailPro) is a Shanghai-based retail marketing technology company founded in 2015 that builds SCRM and new-retail CRM software for multi-store and chain brands. Its platform combines a Marketing Cloud and in-store CRM to deliver omnichannel member management, WeChat mini-program malls, guide (导购) distribution and full-staff sales tools, live-streaming commerce, points malls, and campaign automation. EZR serves 800+ brands across fashion, beauty, home goods, food, and pharmacy, and is backed by Tencent, JD.com, DCM, and Lenovo Star. The EZR Open Platform (开放平台) at open.ezrpro.com publishes a reference for 236 interfaces across 11 business domains — stores and staff, member master data, loyalty points, coupons, sales receipts, WeChat mall, gift cards, messaging and third-party platform binding — of which 31 are EZR-to-integrator push callbacks. Every interface is an HTTP POST with a form-encoded, SHA1/MD5-signed envelope carrying the business payload
  as a JSON string; there is no OpenAPI, no OAuth, no versioning scheme and no self-service onboarding. EZR does publish a packaged Agent Skill for generating integration code.
image: https://www.ezrpro.com/public/icon.png
layout: provider
modified: '2026-08-13'
name: EZR
nav: Providers
network: true
overview: 'EZR publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise, SCRM, CRM, and Retail.


  The EZR catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  EZR''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, sandbox, and 16 more developer resources.'
plans:
- name: Ezr Plans Pricing
  plan_count: 0
  slug: ezr-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 1
  name: Ezr Rate Limits
  slug: ezr-rate-limits
score:
  band: developing
  composite: 40.0
  coverage:
    artifact_dirs: 19
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 41.6
    developer_ergonomics: 71.4
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 44.7
  previous_composite: 40.0
  provenance:
    conformance: derived
    mcp: derived
    skills: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ezr/refs/heads/main/screenshots/ezr-2026-07-25T214058.png
security:
- kind: authentication
  name: Ezr Authentication
  slug: ezr-authentication
  summary_line: signedRequest · 1 scheme
- kind: domain-security
  name: Ezr Domain Security
  slug: ezr-domain-security
  summary_line: TLSv1.3 · HSTS
slug: ezr
tags:
- Company
- Enterprise
- SCRM
- CRM
- Retail
- Marketing
- WeChat
- E-Commerce
- Loyalty
- Membership
- Coupons
- Point-of-Sale
- Webhook
- China
website: https://www.ezrpro.com/
---
