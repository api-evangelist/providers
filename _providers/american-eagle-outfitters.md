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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 25.0
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: 'The one callable, machine-reachable surface in the American Eagle Outfitters estate: a Universal Commerce Protocol shopping server, transported over MCP, on the Unsubscribed brand storefront. Anonymou'
  name: Unsubscribed Commerce (UCP/MCP)
  slug: unsubscribed-commerce
artifact_total: 28
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/american-eagle-outfitters-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/american-eagle-outfitters-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/american-eagle-outfitters-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/american-eagle-outfitters-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/american-eagle-outfitters-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/american-eagle-outfitters-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/american-eagle-outfitters-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/american-eagle-outfitters-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/american-eagle-outfitters-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/american-eagle-outfitters-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/american-eagle-outfitters-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/american-eagle-outfitters-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/american-eagle-outfitters-packages.yml
- group: company
  title: ''
  type: Blog
  url: https://www.aeo-inc.com/news-media/
- group: operate
  title: ''
  type: Support
  url: https://www.ae.com/us/en/content/help/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ae.com/us/en/content/help/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ae.com/content/help/privacy-notice/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/american-eagle-outfitters
- group: company
  title: ''
  type: Website
  url: https://www.ae.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aeo
created: '2026-04-19'
description: American Eagle Outfitters (AEO) is a global specialty retailer operating the American Eagle and Aerie brands, offering on-trend clothing, accessories, and personal care products at affordable prices. The company operates over 1,000 stores across the Americas and online, with a unified commerce strategy spanning e-commerce, mobile, and in-store experiences.
features:
- description: Seamless integration of in-store, mobile, and online channels through a unified commerce strategy powered by Jumpmind Commerce POS.
  name: Unified Commerce Platform
- description: Oracle CrowdTwist-powered loyalty program with points, rewards, and personalized offers across American Eagle and Aerie brands.
  name: Loyalty Program
- description: Native iOS and Android apps for browsing, purchasing, order tracking, and loyalty rewards management.
  name: Mobile Commerce
- description: Google Cloud Dataplex-based data fabric enabling unified data governance, cataloging, and analytics across the enterprise.
  name: Data Fabric
- description: AI-driven personalization for product recommendations, search results, and marketing communications.
  name: Personalization Engine
- description: Buy online pick up in store (BOPIS), curbside pickup, same-day delivery, and ship-from-store capabilities.
  name: Omnichannel Fulfillment
- description: Unified real-time inventory visibility across all store locations and distribution centers.
  name: Real-Time Inventory
- description: MicroStrategy-powered business intelligence and analytics for sales, inventory, and customer insights.
  name: Retail Analytics
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/american-eagle-outfitters.png
integrations:
- description: Point-of-sale platform powering in-store checkout across all AEO store locations with omnichannel capabilities.
  name: Jumpmind Commerce
- description: Oracle Retail solutions for merchandise planning, inventory management, and store operations.
  name: Oracle Retail
- description: Loyalty and engagement platform powering the AEO Connected rewards program.
  name: Oracle CrowdTwist
- description: Data fabric platform for unified data governance, cataloging, and analytics across AEO enterprise data.
  name: Google Cloud Dataplex
- description: Business intelligence and analytics platform for retail performance reporting and decision support.
  name: MicroStrategy
- description: SAP enterprise systems for procurement, sourcing, and financial management.
  name: SAP
- description: Amazon Web Services cloud infrastructure supporting e-commerce and data workloads.
  name: AWS
layout: provider
mcp_servers:
- description: 'American Eagle Outfitters exposes one live, anonymously reachable MCP endpoint across its estate: the Universal Commerce Protocol (UCP) shopping server on www.unsubscribed.com, the AEO brand storefron'
  name: Unsubscribed Commerce (UCP/MCP)
  slug: unsubscribed-commerce-ucpmcp
modified: '2026-09-02'
name: American Eagle Outfitters
nav: Providers
network: true
overview: 'American Eagle Outfitters publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Retail, E-Commerce, Fashion, Apparel, and Consumer Goods.


  American Eagle Outfitters'' developer surface includes authentication, engineering blog, support, and 18 more developer resources.'
plans:
- name: American Eagle Outfitters Plans Pricing
  plan_count: 0
  slug: american-eagle-outfitters-plans-pricing
press:
- date: '2026-05-25'
  title: Grid Dynamics Helps American Eagle To Reimagine ...
  url: https://www.griddynamics.com/press-releases/pr-5-18-2021
- date: '2026-05-25'
  title: American Eagle turns to AI for help managing inventory
  url: https://www.supplychaindive.com/news/american-eagle-ai-inventory-management-Q2-earnings/693719/
- date: '2026-05-25'
  title: American Eagle jeans, Aerie's anti-AI pledge, and Sydney ...
  url: https://www.facebook.com/businessinsider/posts/american-eagle-jeans-aeries-anti-ai-pledge-and-sydney-sweeney-boosted-revenue-st/1222224646442484/
- date: '2026-05-25'
  title: Aerie by AEO vows to avoid AI-generated images in ads
  url: https://www.linkedin.com/posts/adweek_aeriereal-activity-7382069002602323968-LsV9
- date: '2026-05-25'
  title: American Eagle uses Meta AI ads to get Gen Z to stores
  url: https://adage.com/article/digital-marketing-ad-tech-news/american-eagle-uses-meta-ai-ads-get-gen-z-stores/2606366/
random_paper: 4
rate_limits:
- limit_count: 0
  name: American Eagle Outfitters Rate Limits
  slug: american-eagle-outfitters-rate-limits
scopes:
- name: American Eagle Outfitters Scopes
  scope_count: 0
  slug: american-eagle-outfitters-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 19.7
  coverage:
    artifact_dirs: 18
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 13.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 30.4
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 6.7
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/american-eagle-outfitters/refs/heads/main/screenshots/american-eagle-outfitters-2026-06-20T171908.png
security:
- kind: authentication
  name: American Eagle Outfitters Authentication
  slug: american-eagle-outfitters-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: American Eagle Outfitters Domain Security
  slug: american-eagle-outfitters-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: american-eagle-outfitters
tags:
- Retail
- E-Commerce
- Fashion
- Apparel
- Consumer Goods
- Fortune 1000
use_cases:
- description: Customers browse and purchase American Eagle and Aerie products through ae.com and aerie.com with personalized recommendations.
  name: E-Commerce Shopping
- description: Jumpmind Commerce POS handles in-store transactions with loyalty integration and omnichannel order fulfillment.
  name: In-Store Checkout
- description: Customers earn and redeem AEO Connected rewards points across all shopping channels.
  name: Loyalty Rewards
- description: SAP-based procurement and supply chain processes for sourcing, vendor management, and inventory replenishment.
  name: Supply Chain Management
- description: Google Cloud Dataplex and MicroStrategy analytics for understanding customer behavior and optimizing merchandising.
  name: Customer Data Analytics
- description: Unified order management supporting split shipments, returns, and exchanges across channels.
  name: Order Management
website: https://www.ae.com
---
