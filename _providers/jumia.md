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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/jumia-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jumia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://group.jumia.com
- group: other
  title: ''
  type: Marketplace
  url: https://www.jumia.com.ng
- group: other
  title: ''
  type: JumiaPay
  url: https://pay.jumia.com.ng
- group: other
  title: ''
  type: JumiaPayBusiness
  url: https://business-pay.jumia.com.ng
- group: other
  title: ''
  type: VendorCenter
  url: https://vendorcenter.jumia.com
- group: other
  title: ''
  type: VendorAPI
  url: https://vendorcenter.jumia.com/api-docs/
- group: other
  title: ''
  type: SellerCenterAPI
  url: http://sellerapi.sellercenter.jumia.com/v2.7.11/overview/getting-started/
- group: docs
  title: ''
  type: SellerCenterGuide
  url: http://guide.sellercenter.jumia.com/
- group: other
  title: ''
  type: JumiaPayAPI
  url: https://merchant-api-doc-pay.jumia.com.ng/
- group: docs
  title: ''
  type: JumiaPayIntegrationGuides
  url: https://business-pay.jumia.com.ng/integration-guides/
- group: start
  title: ''
  type: SandboxBaseUrl
  url: https://api-sandbox-pay.jumia.com.ng
- group: other
  title: ''
  type: ProductionBaseUrl
  url: https://api-pay.jumia.com.ng
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/jumiagandalf/jumia-vendor-api/overview
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Jumia
- group: build
  title: ''
  type: GitHubJumiaPay
  url: https://github.com/JumiaPayAIG
- group: other
  title: ''
  type: OpenSourcePlaybook
  url: https://github.com/Jumia/open-source
- group: company
  title: ''
  type: TechBlog
  url: https://github.com/Jumia/techblog
- group: company
  title: ''
  type: Blog
  url: https://www.jumia-blog.com
- group: company
  title: ''
  type: Investors
  url: https://investor.jumia.com
- group: other
  title: ''
  type: SECFilings
  url: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001756708&type=&dateb=&owner=include&count=40
- group: company
  title: ''
  type: Newsroom
  url: https://group.jumia.com/press
- group: company
  title: ''
  type: Careers
  url: https://group.jumia.com/careers
- group: operate
  title: ''
  type: Contact
  url: https://group.jumia.com/contact
- group: other
  title: ''
  type: VendorHubNigeria
  url: https://www.jumia.com.ng/sp-vendor-hub-jumia/
- group: other
  title: ''
  type: SellOnJumiaEgypt
  url: https://www.jumia.com.eg/sell-on-jumia/
- group: build
  title: ''
  type: WooCommercePlugin
  url: https://github.com/JumiaPayAIG/woocommerce-plugin
- group: build
  title: ''
  type: MagentoPlugin
  url: https://github.com/JumiaPayAIG/magento-plugin
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/jumia-group
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/JumiaGroup
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@JumiaGroup
created: '2026-05-24'
description: 'Jumia is a pan-African e-commerce company often described as the "Amazon of Africa." Headquartered in Berlin and listed on the New York Stock Exchange under the ticker JMIA since its 2019 IPO, Jumia Technologies AG operates a third-party marketplace, a logistics network (Jumia Logistics), and a digital payments arm (JumiaPay) across eight African markets as of 2026: Egypt, Ghana, Ivory Coast, Kenya, Morocco, Nigeria, Senegal, and Uganda. The company exited Algeria in February 2026 and previously wound down Cameroon, Gabon, Rwanda, and Tunisia as part of a multi-year restructuring program targeting full-year profitability in 2027. Jumia''s commerce platform connects more than 100,000 sellers with consumers across diverse categories including phones and electronics, fashion, home and living, beauty, FMCG, and groceries. Its developer surface is non-trivial: the Jumia Vendor API (vendor center, OAuth 2.0) supports order, inventory, product, and shipment integration for marketplace
  sellers, while the legacy SellerCenter API (a SellerCenter / Rocket Internet lineage shared with Lazada and Daraz) remains documented with PHP, Python, Ruby, and Node SDKs. JumiaPay exposes a Merchant API for payment creation, verification, refund, recurring-payment agreements, and callback-based webhooks, plus official WooCommerce and Magento payment-gateway plugins. The Jumia GitHub organization is sparse (an open-source playbook, Jumia Tech Blog, and Tech in Porto event site) while the JumiaPay AIG GitHub org hosts the WooCommerce and Magento gateway plugins under Apache 2.0.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jumia.png
layout: provider
modified: '2026-05-24'
name: Jumia
nav: Providers
network: true
overview: 'Jumia is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include E-Commerce, Marketplace, Africa, Pan-African, and Retail.


  Jumia''s developer surface includes GitHub presence, engineering blog, YouTube channel, and 29 more developer resources.'
random_paper: 9
score:
  band: minimal
  composite: 5.1
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 5.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jumia/refs/heads/main/screenshots/jumia-2026-06-20T183828.png
security:
- kind: domain-security
  name: Jumia Domain Security
  slug: jumia-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Jumia Vulnerability Disclosure
  slug: jumia-vulnerability-disclosure
  summary_line: Hackerone
slug: jumia
tags:
- E-Commerce
- Marketplace
- Africa
- Pan-African
- Retail
- Payments
- Logistics
- Vendor Management
- Sellers
- Merchant Services
- Mobile Commerce
- Emerging Markets
- Public Company
website: https://group.jumia.com
---
