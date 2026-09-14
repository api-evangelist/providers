---
access_model:
  confidence: medium
  label: Enterprise · Requires approval
  onboarding: approval
  pricing: enterprise
  public: false
  source:
  - plans
  trial: false
  try_now: false
api_count: 5
apis:
- description: REST APIs for the Nexus digital reality platform enabling manufacturers to build connected workflows integrating metrology, quality inspection, and production monitoring data. All endpoints are authen
  name: Hexagon Nexus API
  slug: nexus-api
- description: Enterprise Asset Management REST API providing programmatic access to asset lifecycle data including equipment management, work orders, preventive maintenance, document attachments, and service reques
  name: HxGN EAM REST API
  slug: hxgn-eam-api
- description: Smart Digital eXchange API Services enabling integration with Hexagon's engineering data management platform for plant design, document control, and digital twin workflows in process and power industr
  name: HxGN SDx API Services
  slug: hxgn-sdx-api
- description: 'The federated GraphQL API behind Hexagon GeoCloud (formerly HxDR / Reality Cloud Studio) for uploading, processing, organising, streaming and sharing reality-capture and geospatial data. 1,125 types, '
  name: Hexagon GeoCloud GraphQL API
  slug: geocloud-graphql
- description: A remote Model Context Protocol endpoint served from the Hexagon GeoCloud web property and discoverable through RFC 9728 protected-resource metadata and RFC 8414 authorization-server metadata on the s
  name: Hexagon GeoCloud MCP Server
  slug: geocloud-mcp
artifact_total: 13
common:
- group: docs
  title: ''
  type: APIReference
  url: https://rcdocs.leica-geosystems.com/en/hexagon-geocloud/latest.md
- group: start
  title: ''
  type: DeveloperPortal
  url: https://nexus.hexagon.com/developerportal
- group: start
  title: ''
  type: GettingStarted
  url: https://rcdocs.leica-geosystems.com/en/hexagon-geocloud/latest/getting-started.md
- group: operate
  title: ''
  type: Support
  url: https://geocloud.hexagon.com/contact-support/
- group: start
  title: ''
  type: SignUp
  url: https://geocloud.hexagon.com/free-demo/
- group: start
  title: ''
  type: Login
  url: https://geocloud.hxdr.app/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://geocloud.hexagon.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hexagon.com/legal/privacy-notice
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/hexagon-changelog.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/hexagon-lifecycle.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hexagon-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hexagon-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/hexagon-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/hexagon-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hexagon-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://geocloud.hexagon.com/security-compliance/
- group: auth
  title: ''
  type: TrustCenter
  url: security/hexagon-trust-center.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hexagon-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/hexagon-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/hexagon-packages.yml
- group: operate
  title: ''
  type: FAQ
  url: https://geocloud.hexagon.com/faq/
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hexagon-oss
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hexagon-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hexagon.com
- group: docs
  title: ''
  type: Documentation
  url: https://nexus.hexagon.com/documentationcenter/en-US/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/hexagonab
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hexagon-ab
- group: company
  title: ''
  type: Blog
  url: https://blog.manufacturing.hexagon.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://hexagon.com/products/product-groups/nexus
- group: operate
  title: ''
  type: StatusPage
  url: https://status.hxdr.app/
- group: other
  title: ''
  type: X
  url: https://x.com/hexagonab
- group: commercial
  title: ''
  type: Plans
  url: plans/hexagon-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hexagon-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/hexagon-finops.yml
created: '2026-06-13'
description: Hexagon is a global leader in digital reality solutions, combining sensor, software and autonomous technologies. Through the Nexus platform and product APIs, Hexagon delivers manufacturing intelligence capabilities spanning metrology, quality inspection, production monitoring, and digital factory solutions. The Nexus Developer Portal provides REST APIs authenticated via OAuth 2.0, enabling manufacturers and third-party developers to build connected, collaborative workflows integrating measurement data, quality processes, and industrial automation across the smart factory lifecycle.
finops:
- name: Hexagon Finops
  service_category: ''
  slug: hexagon-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hexagon.png
layout: provider
mcp_servers:
- description: ''
  name: Hexagon GeoCloud MCP
  slug: hexagon-geocloud-mcp
modified: '2026-06-13'
name: Hexagon
nav: Providers
network: true
overview: 'Hexagon publishes 1 API on the [APIs.io](https://apis.io/) network: Nexus API. Tagged areas include Manufacturing, Metrology, Quality Inspection, Digital Factory, and Production Monitoring.


  Hexagon''s developer surface includes API reference, getting-started guide, support, signup flow, changelog, authentication, FAQ, and 28 more developer resources.'
plans:
- name: Hexagon Plans Pricing
  plan_count: 3
  slug: hexagon-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Hexagon Rate Limits
  slug: hexagon-rate-limits
scopes:
- name: Hexagon Scopes
  scope_count: 0
  slug: hexagon-scopes
  summary_line: OAuth 2.0 · no documented scopes
screenshot: https://raw.githubusercontent.com/api-evangelist/hexagon/refs/heads/main/screenshots/hexagon-2026-06-20T182709.png
security:
- kind: authentication
  name: Hexagon Authentication
  slug: hexagon-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Hexagon Domain Security
  slug: hexagon-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Hexagon Trust Center
  slug: hexagon-trust-center
  summary_line: SOC 2 Type II, ISO/IEC 27001:2022, CSA STAR Level 1
slug: hexagon
tags:
- Manufacturing
- Metrology
- Quality Inspection
- Digital Factory
- Production Monitoring
- Industrial IoT
- Smart Manufacturing
website: https://hexagon.com
---
