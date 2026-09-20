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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-09-19'
api_count: 0
artifact_total: 15
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/belk/refs/heads/main/security/belk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/belk-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/belk
- group: company
  title: ''
  type: Website
  url: https://www.belk.com
- group: start
  title: Belk Vendor Portal (login-gated supplier application)
  type: Portal
  url: https://vendorportal.belk.com/VendorPortal/
- group: docs
  title: Vendor Resources (X12 4030 EDI implementation guides, PDF)
  type: Documentation
  url: https://www.belk.com/customer-service/policies-guidelines/vendor-resources/
- group: operate
  title: ''
  type: Support
  url: https://www.belk.com/customer-service/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.belk.com/customer-service/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.belk.com/customer-service/policies-guidelines/privacy-policy/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/belk/refs/heads/main/conformance/belk-conformance.yml
  title: ''
  type: Conformance
  url: conformance/belk-conformance.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/belk/refs/heads/main/plans/belk-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/belk-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/belk/refs/heads/main/rate-limits/belk-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/belk-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/belk/refs/heads/main/llms/belk-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/belk-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/belk/refs/heads/main/regulatory/belk-regulatory-posture.yml
  title: ''
  type: DataSubjectRequest
  url: regulatory/belk-regulatory-posture.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/belk/refs/heads/main/regulatory/belk-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/belk-regulatory-posture.yml
coverage:
  checked: '2026-09-19'
  detail: Belk is a department-store retailer whose only published integration contract is a mandatory X12 4030 EDI supplier program (PDF implementation guides, VAN-routed, no direct AS2); developer.belk.com is a dangling CNAME into Apigee's legacy devportal edge (dev-belk.devportal.apigee.com -> ui-ea.apigee.net, *.apigee.com certificate, 504) and api.belk.com is an Akamai edge with a *.test.edgekey.net certificate answering 503, so no HTTP API exists to profile.
  evidence:
  - status: 504
    url: https://developer.belk.com/
  - status: 503
    url: https://api.belk.com/
  - status: 200
    url: https://www.belk.com/customer-service/policies-guidelines/vendor-resources/
  - status: 200
    url: https://vendorportal.belk.com/VendorPortal/
  reason: not-a-software-company
  state: none
created: '2026-03-23'
description: 'Belk is a privately-held American department store chain headquartered in Charlotte, North Carolina, serving the southeastern United States. The company sells clothing, handbags, jewelry, beauty products, and home goods. Belk operates an omnichannel retail model with physical stores and an online marketplace. Supplier and marketplace integrations are handled via EDI through value-added networks, with order management integration available through Rithum (formerly CommerceHub) and other channel management platforms. Belk publishes no public HTTP API, developer portal, OpenAPI or SDK: the only integration contract it publishes is the mandatory X12 4030 EDI supplier program (850/856/810/820/824/855/860 and more), documented as PDF implementation guides and routed through a VAN.'
features:
- description: Belk operates physical stores across the southeastern United States alongside an online retail and marketplace presence at belk.com.
  name: Omnichannel Retail
- description: Third-party vendors can list and sell products on Belk.com through the marketplace program, integrated via Rithum (formerly CommerceHub) channel management platform.
  name: Marketplace Seller Program
- description: Belk uses X12 EDI version 4030 for supplier integration, transmitted through value-added networks (VANs). Required documents include EDI 850 purchase orders, EDI 856 advance ship notices, and EDI 846 inventory feeds.
  name: EDI Supplier Integration
- description: Belk's vendor portal provides document specifications, EDI information, and vendor FAQ resources for suppliers to configure EDI integrations.
  name: Vendor Portal
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/belk.png
integrations:
- description: Rithum, formerly CommerceHub, is the primary integration platform for Belk marketplace sellers to manage orders, inventory, and fulfillment.
  name: Rithum (CommerceHub)
- description: Sellercloud supports Belk account integration through Rithum for omnichannel ecommerce order management and inventory synchronization.
  name: Sellercloud
- description: Alloy.ai provides a Belk retailer portal integration for demand forecasting and retail analytics based on Belk point-of-sale data.
  name: Alloy.ai
- description: Tradeshift supports Belk supplier invoice and procurement document exchange through its B2B network integration.
  name: Tradeshift
- description: ConnectPointz provides EDI compliance and channel management integration for Belk marketplace and supplier connections.
  name: ConnectPointz
layout: provider
modified: '2026-09-19'
name: Belk
nav: Providers
network: true
overview: 'Belk is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Apparel, Beauty, Department Store, E-Commerce, and Fashion.


  Belk''s developer surface includes developer portal, documentation, support, and 11 more developer resources.'
plans:
- name: Belk Plans Pricing
  plan_count: 0
  slug: belk-plans-pricing
press:
- date: ''
  title: TCS ignio™ AIOps Helps Belk Secure AI Edge for Operations
  url: https://www.tcs.com/what-we-do/industries/retail/video/tcs-ignio-aiops-secure-ai-edge-operations
- date: ''
  title: Belk is using gen AI to build its next generation of community
  url: https://www.linkedin.com/posts/lee-t-moore_new-way-now-belk-is-using-gen-ai-to-build-activity-7207357537459851264-DVw9
- date: ''
  title: How Belk elevated its customer experience with ...
  url: https://martech.org/how-belk-elevated-its-customer-experience-with-personalization/
- date: ''
  title: Belk harnesses AI to manage inventory
  url: https://www.retaildive.com/news/belk-harnesses-ai-to-manage-inventory/570588/
- date: ''
  title: BEAUTYSPACE Partners with Belk to Expand Retail and ...
  url: https://www.prnewswire.com/news-releases/beautyspace-partners-with-belk-to-expand-retail-and-digital-footprint-302730630.html
random_paper: 18
rate_limits:
- limit_count: 0
  name: Belk Rate Limits
  slug: belk-rate-limits
score:
  band: emerging
  composite: 16.2
  coverage:
    artifact_dirs: 12
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 9.3
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 50.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 6.9
  provenance:
    conformance: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-19'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/belk/refs/heads/main/screenshots/belk-2026-06-20T173133.png
security:
- kind: domain-security
  name: Belk Domain Security
  slug: belk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: belk
tags:
- Apparel
- Beauty
- Department Store
- E-Commerce
- Fashion
- Home Goods
- Jewelry
- Marketplace
- Retail
- Southeastern US
use_cases:
- description: Third-party vendors integrate with the Belk marketplace to list products, receive orders, and manage fulfillment through approved channel platforms.
  name: Marketplace Selling
- description: Manufacturers and distributors connect to Belk's EDI network to exchange purchase orders, advance ship notices, and inventory feeds in X12 format.
  name: EDI Supplier Compliance
- description: Retail suppliers and analytics platforms consume Belk point-of-sale data through retail portal integrations for demand planning and replenishment.
  name: Retail Analytics
website: https://www.belk.com
---
