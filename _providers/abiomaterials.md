---
api_count: 3
apis:
- description: A live, anonymous, agent-callable WebMCP surface served from the North American storefront and discovered through the site's RFC 9727 api-catalog. Six tools with JSON Schema inputs expose site identit
  name: ABio Materials WebMCP Tools
  slug: abio-materials-webmcp-tools
- description: The WooCommerce Store API as deployed on the North American storefront. It serves the company's real product catalogue - 39 products with prices, stock, categories, brands, attributes and reviews - an
  name: ABio Materials Store API
  slug: abio-materials-store-api
- description: The WordPress REST content API on the storefront host, serving posts, pages and taxonomies anonymously. Undocumented by the company; recorded from the live route index at https://a-biousa.com/wp-json/
  name: ABio Materials Site Content API
  slug: abio-materials-site-content-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/abiomaterials-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://a-bio.co.kr/
- group: company
  title: ''
  type: Blog
  url: https://a-biousa.com/blogs/
- group: operate
  title: ''
  type: Support
  url: https://a-biousa.com/contact-us/
- group: start
  title: ''
  type: Login
  url: https://a-biousa.com/user-login/
- group: commercial
  title: ''
  type: Pricing
  url: https://a-biousa.com/shop/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://a-biousa.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://a-biousa.com/privacy-policy/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/abiomaterials-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/abiomaterials-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/abiomaterials-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/abiomaterials-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/abiomaterials-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/abiomaterials-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/abiomaterials-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/abiomaterials-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/abiomaterials-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/abiomaterials-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/abiomaterials-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/abiomaterials-packages.yml
created: '2026-09-06'
description: A-Bio Materials Co., Ltd. (에이바이오머티리얼즈) is a South Korean life-science company, founded in 2020 and led by founder and CEO Sijun Park, that develops and manufactures exosome-derived bioactive materials for cosmetics, aesthetics and medical devices. It produces plant-, human- and microbial-derived exosome formulations and PDRN raw materials through its own Exo-traction, Celltivation and Escentraction purification and cultivation processes, supplying skincare and medical-device manufacturers with ingredients for cell signalling, inflammation reduction, collagen synthesis and tissue regeneration. Its North American arm, ABio materials USA Inc. of Tustin, California, is the official importer and distributor for the region and operates the company's English-language storefront. A-Bio Materials runs no developer programme and publishes no API specification; the machine-readable surfaces recorded in this profile are the WordPress, WooCommerce and WebMCP endpoints its North American
  storefront serves.
image: https://a-biousa.com/storage/2026/01/social-share-by-a-bio-usa-materials-in-tustin-ca.png
layout: provider
mcp_servers:
- description: ABio materials USA Inc. serves a live, anonymous, agent-callable WebMCP surface from its WordPress storefront at a-biousa.com. It was discovered through the RFC 9727 catalog at https://a-biousa.com/.w
  name: Abiomaterials WebMCP tool surface
  slug: abiomaterials-webmcp-tool-surface
modified: '2026-09-06'
name: A-Bio Materials
nav: Providers
network: true
overview: 'A-Bio Materials publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biomaterials, Life Sciences, Cosmetics, and Medical Devices.


  A-Bio Materials'' developer surface includes engineering blog, support, pricing, and 17 more developer resources.'
plans:
- name: Abiomaterials Plans Pricing
  plan_count: 0
  slug: abiomaterials-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Abiomaterials Rate Limits
  slug: abiomaterials-rate-limits
security:
- kind: authentication
  name: Abiomaterials Authentication
  slug: abiomaterials-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Abiomaterials Domain Security
  slug: abiomaterials-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: abiomaterials
tags:
- Company
- Biomaterials
- Life Sciences
- Cosmetics
- Medical Devices
- Exosomes
- Manufacturing
- E-Commerce
- South Korea
website: https://a-bio.co.kr/
---
