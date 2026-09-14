---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Opslevel Agentic Access
  operation_count: 1
  slug: opslevel-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: 'The OpsLevel GraphQL API allows you to integrate OpsLevel with your other operational tools, enrich internal tickets, incidents, and other systems with service and team data pulled from OpsLevel. The '
  name: OpsLevel GraphQL API
  slug: graphql-api
- baseURL: https://api.opslevel.com
  baseurl_source: declared
  description: OpsLevel GraphQL endpoint.
  name: OpsLevel GraphQL API
  slug: opslevel-graphql-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: OpsLevel GraphQL API
  slug: open-opslevel-graphql-api
- collection_type: open
  name: OpsLevel GraphQL API
  slug: open-opslevel
common:
- group: company
  title: ''
  type: Website
  url: https://www.opslevel.com/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/opslevel-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/opslevel-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/opslevel-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/opslevel-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://www.opslevel.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.opslevel.com/
- group: company
  title: ''
  type: Blog
  url: https://www.opslevel.com/resource/blog
- group: start
  title: ''
  type: Signup
  url: https://www.opslevel.com/request-a-demo
- group: start
  title: ''
  type: Login
  url: https://app.opslevel.com/users/sign_in
- group: commercial
  title: ''
  type: Pricing
  url: https://www.opslevel.com/pricing
- group: company
  title: ''
  type: About
  url: https://www.opslevel.com/about
- group: operate
  title: ''
  type: StatusPage
  url: https://opslevelstatus.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.opslevel.com/legal/t4-terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.opslevel.com/legal/privacy
- group: auth
  title: ''
  type: Security
  url: https://www.opslevel.com/legal/security
- group: operate
  title: ''
  type: Contact
  url: https://www.opslevel.com/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OpsLevel
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/opslevel
- group: other
  title: ''
  type: Terraform Provider
  url: https://registry.terraform.io/providers/OpsLevel/opslevel/latest/docs
- group: other
  title: ''
  type: Customers
  url: https://www.opslevel.com/customers
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/OpsLevel/opslevel-mcp
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.opslevel.com/llms.txt
created: '2026-03-03'
description: OpsLevel is a prescriptive internal developer portal for cataloging, measuring, and scaffolding services according to engineering best practices.
finops:
- name: Opslevel Finops
  service_category: API
  slug: opslevel-finops
graphqls:
- description: 'The OpsLevel GraphQL API allows you to integrate OpsLevel with your other operational tools, enrich internal tickets, incidents, and other systems with service and team data pulled from OpsLevel. The '
  name: OpsLevel GraphQL API
  slug: opslevel-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/opslevel.png
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: OpsLevel
nav: Providers
network: true
overview: 'OpsLevel publishes 1 API on the [APIs.io](https://apis.io/) network: GraphQL API. Tagged areas include Developer Portal, Developer Tools, DevOps, Experience, and Internal Developer Portal.


  OpsLevel''s developer surface includes authentication, developer portal, documentation, engineering blog, signup flow, pricing, and 17 more developer resources.'
plans:
- name: Opslevel Plans Pricing
  plan_count: 3
  slug: opslevel-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Opslevel Rate Limits
  slug: opslevel-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/opslevel/refs/heads/main/screenshots/opslevel-2026-06-20T191105.png
security:
- kind: authentication
  name: Opslevel Authentication
  slug: opslevel-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Opslevel Domain Security
  slug: opslevel-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Opslevel Vulnerability Disclosure
  slug: opslevel-vulnerability-disclosure
  summary_line: disclosure policy published
slug: opslevel
tags:
- Developer Portal
- Developer Tools
- DevOps
- Experience
- Internal Developer Portal
- Microservices
- Platform Engineering
- Service Catalog
- Service Maturity
website: https://www.opslevel.com/
---
