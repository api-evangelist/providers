---
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aerwave-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aerwave.com/
- group: company
  title: ''
  type: Blog
  url: https://www.aerwave.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.aerwave.com/blog-feed.xml
- group: operate
  title: ''
  type: Support
  url: https://www.aerwave.com/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://aerwave.zendesk.com/hc/en-us
- group: start
  title: ''
  type: SignUp
  url: https://register.getaerwave.com
- group: start
  title: ''
  type: Login
  url: https://portal.getaerwave.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aerwave.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aerwave.com/privacy-policy
- group: other
  title: ''
  type: AcceptableUsePolicy
  url: https://www.aerwave.com/acceptable-use-policy
- group: company
  title: ''
  type: Press
  url: https://www.aerwave.com/press
- group: operate
  title: ''
  type: Contact
  url: https://www.aerwave.com/contact-us
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aerwave
- group: company
  title: ''
  type: Careers
  url: https://www.aerwave.com/careers
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aerwave-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/aerwave-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/aerwave-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/aerwave-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/aerwave-rate-limits.yml
- group: other
  title: ''
  type: NetworkManagementPolicy
  url: https://www.aerwave.com/accessibility-statement-1
- group: other
  title: ''
  type: Accessibility
  url: https://www.aerwave.com/accessibility-statement
coverage:
  checked: '2026-09-12'
  detail: 'Aerwave sells managed Wi-Fi as an operated service, not as a developer product: aerwave.com is a Wix marketing site with no developer, API or documentation link anywhere in its navigation or sitemap, the only two application hosts are Blazor WebAssembly apps for resident registration and the resident portal, and api/docs/developer/portal subdomains on aerwave.com all return NXDOMAIN.'
  evidence:
  - status: 400
    url: https://www.aerwave.com/openapi.json
  - status: 404
    url: https://portal.getaerwave.com/openapi.json
  - status: 400
    url: https://www.aerwave.com/.well-known/api-catalog
  - status: 200
    url: https://www.aerwave.com/pages-sitemap.xml
  - status: 200
    url: https://www.aerwave.com/llms.txt
  - status: 200
    url: https://www.aerwave.com/_api/mcp
  reason: no-developer-program
  state: none
created: '2026-09-12'
description: Aerwave is a Dallas, Texas managed Wi-Fi provider founded in 2019 that builds and operates fiber-backed, property-wide wireless networks for multifamily apartment communities and student housing. Its HomeWiFi platform gives each resident a private, VLAN-isolated network with individual encryption and instant-on gigabit service without a rented router, while property owners and managers get a SaaS portal for network management, resident onboarding and support. Aerwave publishes no public developer program or API documentation; the machine-readable surface it does serve is an llms.txt and a live, anonymous Model Context Protocol endpoint on its marketing site, both provided by its Wix hosting platform.
image: https://register.getaerwave.com/images/aerwave_website_logo.png
layout: provider
mcp_servers:
- description: ''
  name: Aerwave Site MCP
  slug: aerwave-site-mcp
modified: '2026-09-12'
name: Aerwave
nav: Providers
network: true
overview: 'Aerwave is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Managed WiFi, Multifamily, Real Estate, and Telecommunications.


  Aerwave''s developer surface includes engineering blog, support, signup flow, and 19 more developer resources.'
plans:
- name: Aerwave Plans Pricing
  plan_count: 0
  slug: aerwave-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Aerwave Rate Limits
  slug: aerwave-rate-limits
security:
- kind: domain-security
  name: Aerwave Domain Security
  slug: aerwave-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: aerwave
tags:
- Company
- Managed WiFi
- Multifamily
- Real Estate
- Telecommunications
- Internet Service Provider
- Connectivity
- Smart Buildings
- PropTech
website: https://www.aerwave.com/
---
