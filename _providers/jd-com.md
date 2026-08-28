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
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-26'
api_count: 17
apis:
- description: JOS authorization is JD's OAuth 2.0 flow for shop owners and JD enterprise accounts to grant a partner ISV application access. The platform issues an access token and refresh token scoped per shop / p
  name: JD Open Platform (JOS) OAuth Authorization
  slug: jos-authorization
- description: The ware (商品) API group covers product creation, modification, deletion, and querying; SKU management, inventory, price adjustments, product attributes, and category management for JD POP merchants.
  name: JD Open Platform Ware (Product) API
  slug: jos-ware
- description: The order (订单) API group lets ERP / OMS vendors retrieve JD orders, order details, customer information, and order logistics events; update order status; cancel and split orders; and pull order financ
  name: JD Open Platform Order API
  slug: jos-order
- description: 'The promotion (促销) API group manages JD shop-level promotions: full reduction, coupons, gift promotions, and time-limited deals — including create / read / update / cancel operations.'
  name: JD Open Platform Promotion API
  slug: jos-promotion
- description: The after-sale (售后) API group handles return, refund, exchange, and complaint workflows initiated by JD buyers, including approval / rejection actions and reverse- logistics coordination.
  name: JD Open Platform After-Sale (Service) API
  slug: jos-after-sale
- description: Inventory and warehouse APIs let merchants synchronize stock levels per warehouse, manage reserved inventory, and reconcile with JD's FBP (Fulfilled by POP) and SOP (Sold on POP) fulfillment modes.
  name: JD Open Platform Warehouse / Inventory API
  slug: jos-warehouse
- description: Finance (财务) APIs return JD seller bills, payout records, invoice information, and reconciliation reports for merchants and their ERP systems.
  name: JD Open Platform Finance API
  slug: jos-finance
- description: Shop (店铺) APIs expose shop information, shop configuration, shop categories, and shop decoration metadata for JD POP merchants.
  name: JD Open Platform Shop API
  slug: jos-shop
- description: Customer service (客服) APIs integrate with JD's IM and service workflows — letting merchants pull customer inquiries, route to internal agents, and post agent responses through JD's messaging channel.
  name: JD Open Platform Customer Service API
  slug: jos-customer
- description: The JOS Message Channel pushes near-real-time events for orders, products, after-sale, inventory, and finance to partner-registered endpoints. Partners ack each event and verify the JD signature.
  name: JD Open Platform JOS Message Channel
  slug: jos-jdmessage
- description: The JD Logistics API (JD Quick Pass / JDL) lets merchants and 3PL partners create logistics orders against JD's nationwide network — including waybill generation, pickup booking, and end-to-end tracki
  name: JD Logistics API
  slug: jos-logistics
- description: The FBP (Fulfilled by POP) API lets merchants register stock into JD's warehouses, generate inbound waybills, and inspect inbound and outbound movements that JD fulfills on the merchant's behalf.
  name: JD FBP / 入仓 Fulfillment API
  slug: jos-fbp
- description: JD Cloud Compute APIs manage Cloud Virtual Machines (CVM), lightweight VMs, GPU instances, bare metal servers, and Function Compute — covering create / scale / snapshot / image lifecycle.
  name: JD Cloud Compute (VM) API
  slug: compute
- description: JD Cloud Object Storage is an S3-compatible object store for unstructured data, with bucket / object lifecycle, versioning, lifecycle, and CDN-origin support.
  name: JD Cloud Object Storage Service (OSS) API
  slug: object-storage
- description: JD Cloud CDN exposes content delivery configuration, cache rule management, purge / prefetch, and usage reporting across JD's global edge network.
  name: JD Cloud CDN API
  slug: cdn
- description: JD Cloud database APIs provision and manage relational databases (MySQL, SQL Server, PostgreSQL, MariaDB), distributed SQL (StarDB, TiDB), and NoSQL services (MongoDB, Redis, Memcached).
  name: JD Cloud Database (RDS) APIs
  slug: rds
- description: JD Cloud AI Platform exposes OCR (general, ID card, bank card, business license), speech (STT, TTS), computer vision, and the JoyBuilder model development platform.
  name: JD Cloud OCR / AI APIs
  slug: ai-ocr
artifact_total: 21
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jd-com-domain-security.yml
- group: other
  title: ''
  type: Marketplace
  url: https://www.jd.com/
- group: other
  title: ''
  type: JDWorldwide
  url: https://www.jd.id/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://open.jd.com/
- group: docs
  title: ''
  type: Documentation
  url: https://open.jd.com/home/home#/doc/common
- group: docs
  title: ''
  type: APIReference
  url: https://open.jd.com/home/home#/doc/api
- group: other
  title: ''
  type: JDCloud
  url: https://www.jdcloud.com/en/
- group: docs
  title: ''
  type: JDCloudDocs
  url: https://docs.jdcloud.com/cn/
- group: other
  title: ''
  type: JDLogistics
  url: https://www.jdl.com/
- group: other
  title: ''
  type: JDHealth
  url: https://www.jdhealth.com/
- group: other
  title: ''
  type: ParentCompany
  url: https://corporate.jd.com/
- group: company
  title: ''
  type: InvestorRelations
  url: https://ir.jd.com/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/jd-opensource
- group: company
  title: ''
  type: TechBlog
  url: https://tech.jd.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/jd.com/
created: '2026-05-23'
description: 'JD.com (Jingdong) is one of China''s largest direct-sales e-commerce platforms, operating a vast first-party retail business and a third-party (POP) marketplace alongside JD Logistics (one of China''s largest integrated logistics networks), JD Health, JD Industrials, JD Property, and JD Cloud. JD exposes two distinct developer platforms: JD Open Platform (open.jd.com) — also known as JOS (Jingdong Open Service) — which hosts the partner / ISV REST API for sellers and ERP / OMS vendors covering ware (product), order, promotion, after-sale, warehouse, finance, customer service, message, JD logistics, and B2B; and JD Cloud (jdcloud.com) — JD''s public cloud with compute (Cloud Virtual Machine, GPU, bare metal, function compute), storage (object, block, file), network (VPC, CDN, load balancer), database (MySQL, TiDB, StarDB, Redis, MongoDB, ClickHouse), AI (JoyBuilder, JoyAgent, JoyCode, OCR, speech), and security services.'
finops:
- name: Jd Com Finops
  service_category: API
  slug: jd-com-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jd-com.png
layout: provider
modified: '2026-05-23'
name: JD.com (Jingdong)
nav: Providers
network: true
overview: 'JD.com (Jingdong) publishes 17 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include E-Commerce, Marketplace, China, Cloud Platform, and Logistics.


  JD.com (Jingdong)''s developer surface includes documentation, API reference, GitHub presence, and 12 more developer resources.'
plans:
- name: Jd Com Plans Pricing
  plan_count: 1
  slug: jd-com-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 2
  name: Jd Com Rate Limits
  slug: jd-com-rate-limits
score:
  band: emerging
  composite: 16.6
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 16.6
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jd-com/refs/heads/main/screenshots/jd-com-2026-06-20T183726.png
security:
- kind: domain-security
  name: Jd Com Domain Security
  slug: jd-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: jd-com
tags:
- E-Commerce
- Marketplace
- China
- Cloud Platform
- Logistics
- Retail
- JD Open Platform
- JD Cloud
- JOS
website: https://open.jd.com/
---
