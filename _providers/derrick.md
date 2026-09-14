---
api_count: 2
apis:
- description: REST API for B2B data enrichment (emails, phones, profile/company enrichment, verification, search, SIRET/SIREN). Bearer API-key auth; requires Standard plan or above.
  name: Derrick REST API
  slug: derrick-rest-api
- description: Hosted streamable-HTTP MCP server exposing 12 enrichment tools; also available as a local npm package (derrick-mcp). Bearer API-key auth; requires Standard plan or above.
  name: Derrick MCP Server
  slug: derrick-mcp-server
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://derrick-app.com
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/derrick-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/derrick-domain-security.yml
- group: auth
  title: ''
  type: Security
  url: security/derrick-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/derrick-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/derrick-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/derrick-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/derrick-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/derrick-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/derrick-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/derrick-rate-limits.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/derrick-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/derrick-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/derrick-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/derrick-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/derrick-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/derrick-changelog.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://derrick-app.com/#pricing
- group: operate
  title: ''
  type: Roadmap
  url: https://derrick.productlift.dev/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://derrick-app.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://derrick-app.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://derrick-app.com/get-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DerrickAppOrg
created: '2026-09-09'
description: B2B data-enrichment engine providing professional emails, phone numbers, LinkedIn/company enrichment, tech-stack detection, email verification, lead/company search, and French SIRET/SIREN data. Delivered via a Google Sheets add-on, a REST API, and an MCP server for AI agents.
image: https://derrick-app.com/og/index.png
layout: provider
mcp_servers:
- description: ''
  name: Derrick MCP Server
  slug: derrick-mcp-server
- description: ''
  name: Derrick MCP Server
  slug: derrick-mcp-server-2
modified: '2026-09-09'
name: Derrick
nav: Providers
network: true
overview: 'Derrick publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include b2b-data-enrichment, email-finder, phone-finder, company-firmographics, and lead-generation.


  Derrick''s developer surface includes authentication, changelog, pricing, engineering blog, signup flow, and 19 more developer resources.'
plans:
- name: Derrick Plans Pricing
  plan_count: 6
  slug: derrick-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 1
  name: Derrick Rate Limits
  slug: derrick-rate-limits
security:
- kind: authentication
  name: Derrick Authentication
  slug: derrick-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Derrick Domain Security
  slug: derrick-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Derrick Vulnerability Disclosure
  slug: derrick-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: derrick
tags:
- b2b-data-enrichment
- email-finder
- phone-finder
- company-firmographics
- lead-generation
- sales-intelligence
- crm-enrichment
- tech-stack-detection
- email-verification
- siret-siren-france
- mcp-server
- llms-txt
- google-sheets
- gtm-tools
website: https://derrick-app.com
---
