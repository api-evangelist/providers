---
api_count: 1
apis:
- baseURL: https://neuronto.com
  baseurl_source: declared
  description: 'Search, explore and audit Agentic Resource Discovery entries: MCP servers, A2A agents, OpenAPI services and documentation. REST, MCP and A2A answer from one index. No key, no signup.'
  name: Neuronto ARD Registry API
  slug: ard-registry
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/neuronto-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/neuronto-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/neuronto-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/neuronto-cli.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/neuronto-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/neuronto-llms.txt
- group: company
  title: ''
  type: Website
  url: https://neuronto.com
- group: design
  title: ''
  type: Conformance
  url: conformance/neuronto-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/neuronto-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/neuronto-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/neuronto-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/neuronto-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/neuronto-plans-pricing.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://neuronto.com/pricing
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/neuronto-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Blog
  url: https://neuronto.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://neuronto.com/feed.xml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://neuronto.com/privacy
- group: start
  title: ''
  type: GettingStarted
  url: https://neuronto.com/publish
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/neuronto
created: '2026-08-31'
description: Agentic Resource Discovery (ARD) index. One search covers this index and every other public ARD registry, and results carry the tools each MCP server actually exposes, read from its own tools/list. The index holds 15,412 resources from 6,926 publishers, 14,522 verified to respond, and answers over REST, MCP and A2A with no key and no signup.
image: https://neuronto.com/icon.svg
layout: provider
mcp_servers:
- description: Official hosted MCP server for the Neuronto ARD Registry. tools/list answered a live anonymous POST on 2026-09-07 (HTTP 200, application/json) with 4 tools; the response is saved verbatim in neuronto-
  name: Neuronto ARD Registry MCP Server
  slug: neuronto-ard-registry-mcp-server
modified: '2026-09-07'
name: Neuronto ARD Registry
nav: Providers
network: true
overview: 'Neuronto ARD Registry publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Agentic Resource Discovery, ARD, MCP, A2A, and API Discovery.


  Neuronto ARD Registry''s developer surface includes CLI, authentication, pricing, engineering blog, getting-started guide, and 16 more developer resources.'
plans:
- name: Neuronto Plans Pricing
  plan_count: 4
  slug: neuronto-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Neuronto Rate Limits
  slug: neuronto-rate-limits
security:
- kind: authentication
  name: Neuronto Authentication
  slug: neuronto-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Neuronto Domain Security
  slug: neuronto-domain-security
  summary_line: TLSv1.3 · HSTS
slug: neuronto
tags:
- Agentic Resource Discovery
- ARD
- MCP
- A2A
- API Discovery
- Registry
website: https://neuronto.com
---
