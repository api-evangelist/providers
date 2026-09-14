---
access_model:
  confidence: medium
  label: Open discovery, gated execution — tools/list is anonymous, tools/call needs an agent profile and a JWT
  onboarding: unknown
  pricing: free
  public: true
  source:
  - '{''url'': ''https://hearthnhome.com/api/ucp/mcp'', ''status'': 200, ''note'': ''JSON-RPC tools/list returned all 13 tools with full inputSchemas and no Authorization header; tools/call on the same endpoint returned -32000 AuthenticationRequired (a Shopify agent JWT) and -32001 invalid_profile_url (a fetchable meta.ucp-agent.profile URI) — discovery is open, execution is gated (probed 2026-09-13)''}'
  - '{''url'': ''https://www.hni.com'', ''status'': 301, ''note'': ''the previously recorded website hni.com 301s to acrisure.com/midwest — that is HNI Risk Services / Acrisure Midwest, a DIFFERENT company; HNI Corporation is www.hnicorp.com (probed 2026-09-13, roadmap#169)''}'
  trial: false
  try_now: true
api_count: 1
apis:
- description: The Hearth & Home Technologies storefront implements the Universal Commerce Protocol (UCP) over an anonymous Model Context Protocol endpoint. A tools/list probe on 2026-09-13 returned 13 tools — searc
  name: Hearth & Home Technologies Agent Commerce (UCP/MCP)
  slug: hearth-home-agent-commerce
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://www.hnicorp.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hni-corporation
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hnicorp.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hnicorp.com/terms-of-use
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hni-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/hni-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hni-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/hni-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hni-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/hni-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hni-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/hni-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hni-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hni-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/hni-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/hni-packages.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hni-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/hni-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/hni-mcp.yml
created: '2026-04-28'
description: 'HNI Corporation (NYSE: HNI) is a manufacturer founded in 1944 and headquartered in Muscatine, Iowa, built around two operating segments. Workplace Furnishings makes office seating, desks, storage, tables, panel systems and ancillary furnishings sold through independent dealers under the HON, Allsteel, Gunlocke, HBF and Kimball International brands. Residential Building Products is the hearth business, operated by Hearth & Home Technologies under the Heatilator, Heat & Glo, Majestic, Monessen, Quadra-Fire, Harman, SimpliFire and PelPro brands. HNI publishes no developer portal, REST API or OpenAPI for either segment. Its one public machine-readable surface is the agent-commerce stack on the Hearth & Home Technologies storefront at hearthnhome.com, which serves an llms.txt, a Universal Commerce Protocol merchant profile and an anonymous MCP endpoint exposing 13 catalog, cart and checkout tools.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hni.png
layout: provider
mcp_servers:
- description: ''
  name: Hearth & Home Technologies Agent Commerce MCP Server
  slug: hearth-home-technologies-agent-commerce-mcp-server
modified: '2026-09-13'
name: HNI Corporation
nav: Providers
network: true
overview: 'HNI Corporation publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Fortune 1000, Manufacturing, Office Furniture, Workplace, and Building Products.


  HNI Corporation''s developer surface includes authentication and 19 more developer resources.'
plans:
- name: Hni Plans Pricing
  plan_count: 0
  slug: hni-plans-pricing
press:
- date: '2026-05-25'
  title: The companies have closed on the acquisition deal, HNI ...
  url: https://www.facebook.com/woodtv/posts/the-companies-have-closed-on-the-acquisition-deal-hni-announced-today/1362395972586911/
- date: '2026-05-25'
  title: HNI signals fifth year of double-digit EPS growth with $120 ...
  url: https://seekingalpha.com/news/4557045-hni-signals-fifth-year-of-double-digit-eps-growth-with-120m-synergy-target-following
- date: '2026-05-25'
  title: HNI Corporation
  url: https://www.hnicorp.com/
- date: '2026-05-25'
  title: HNI to purchase Steelcase Inc., HNI's headquarters ...
  url: https://www.kwqc.com/2025/08/04/hni-purchase-steelcase-inc-hnis-headquarters-remain-muscatine/
- date: '2026-05-25'
  title: HNI) 2026 proxy details Steelcase deal, pay and ESG
  url: https://www.stocktitan.net/sec-filings/HNI/def-14a-hni-corp-definitive-proxy-statement-3603a98d9fc3.html
random_paper: 4
rate_limits:
- limit_count: 0
  name: Hni Rate Limits
  slug: hni-rate-limits
scopes:
- name: Hni Scopes
  scope_count: 0
  slug: hni-scopes
  summary_line: OAuth 2.0 · no documented scopes
screenshot: https://raw.githubusercontent.com/api-evangelist/hni/refs/heads/main/screenshots/hni-2026-06-20T182807.png
security:
- kind: authentication
  name: Hni Authentication
  slug: hni-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Hni Domain Security
  slug: hni-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hni
tags:
- Fortune 1000
- Manufacturing
- Office Furniture
- Workplace
- Building Products
- Hearth
- Retail
- E-Commerce
- Agent Commerce
- MCP
website: https://www.hnicorp.com
---
