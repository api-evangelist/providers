---
api_count: 1
apis:
- baseURL: https://anew.page
  baseurl_source: declared
  description: REST/HTTP API to encode self-contained HTML into shareable URLs (POST /write) and read pages back (GET /{slug}), with OpenAPI 3.1.1 contract. Unauthenticated and free.
  name: anew Write/Read API
  slug: anew-writeread-api
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://www.anew.page/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://anew.page
- group: docs
  title: ''
  type: Documentation
  url: https://anew.page/llms.txt
- group: docs
  title: ''
  type: APIReference
  url: https://anew.page/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://setup.anew.page
- group: operate
  title: ''
  type: Support
  url: https://github.com/round/anew.page/issues
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/round
- group: commercial
  title: ''
  type: TermsOfService
  url: https://github.com/round/anew.page/blob/main/LICENSE.md#terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://github.com/round/anew.page/blob/main/LICENSE.md#privacy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/anew-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/anew-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/anew-api-catalog.json
- group: design
  title: ''
  type: Conformance
  url: conformance/anew-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/anew-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/anew-lifecycle.yml
- group: auth
  title: ''
  type: Security
  url: security/anew-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/anew-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/anew-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/anew-packages.yml
- group: design
  title: ''
  type: Components
  url: components/anew-components.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/anew-plans-pricing.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/anew-tool-crosswalk.yml
created: '2026-09-04'
description: A stateless "page-in-a-URL" service that encodes a self-contained HTML document into a shareable, immutable URL (HTML → URL) and reads it back (URL → HTML). No account, no hosting; free, deterministic, and unauthenticated. Exposes a REST/HTTP API, a hosted MCP server, an A2A agent, and llms.txt.
image: https://anew.page/anew.png
layout: provider
mcp_servers:
- description: ''
  name: anew MCP Server
  slug: anew-mcp-server
modified: '2026-09-04'
name: anew
nav: Providers
network: true
overview: 'anew publishes 1 API on the [APIs.io](https://apis.io/) network: Write/Read API. Tagged areas include html, webpage, website, url, and encode.


  anew''s developer surface includes documentation, API reference, getting-started guide, support, and 19 more developer resources.'
plans:
- name: Anew Plans Pricing
  plan_count: 0
  slug: anew-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 1
  name: Anew Rate Limits
  slug: anew-rate-limits
security:
- kind: authentication
  name: Anew Authentication
  slug: anew-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Anew Domain Security
  slug: anew-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
- kind: vulnerability-disclosure
  name: Anew Vulnerability Disclosure
  slug: anew-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Anew Trust Center
  slug: anew-trust-center
  summary_line: trust center published
slug: anew
tags:
- html
- webpage
- website
- url
- encode
- share
- web-publishing
- developer-tools
- mcp
- a2a
- ai-agent-tooling
- llms-txt
- agents-txt
- agent-skills
- webmcp
- openapi
- stateless
- immutable
- no-auth
- static-site
- url-encoding
website: https://www.anew.page/
---
