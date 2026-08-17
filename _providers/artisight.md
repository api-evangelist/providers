---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 23.4
  scored_at: '2026-08-17'
api_count: 2
apis:
- description: The public WordPress REST API served from artisight.com. It is the marketing/content API for the corporate website — posts, pages, media, taxonomies, case studies and the site route index — not a clin
  name: Artisight Website Content API
  slug: website-content-api
- description: A Model Context Protocol server published from artisight.com by the WordPress MCP Adapter, backed by the WordPress Abilities API. Discovery is anonymous — RFC 8414 authorization-server metadata and RF
  name: Artisight MCP Server
  slug: mcp-server
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://artisight.com/
- group: company
  title: ''
  type: About
  url: https://artisight.com/about/
- group: company
  title: ''
  type: Blog
  url: https://artisight.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://artisight.com/feed/
- group: company
  title: ''
  type: Press
  url: https://artisight.com/press-releases/
- group: other
  title: ''
  type: CaseStudies
  url: https://artisight.com/case-studies/
- group: company
  title: ''
  type: Partners
  url: https://artisight.com/partners/
- group: company
  title: ''
  type: Careers
  url: https://artisight.com/careers/
- group: operate
  title: ''
  type: Support
  url: https://artisight.com/contact/
- group: start
  title: ''
  type: SignUp
  url: https://artisight.com/demo/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://artisight.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/artisight
- group: auth
  title: ''
  type: Compliance
  url: https://artisight.com/smart-hospital-technology/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/artisight-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/artisight-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/artisight-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/artisight-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/artisight-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/artisight-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/artisight-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/artisight-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/artisight-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/artisight-domain-security.yml
created: '2026-08-02'
description: Artisight is a smart hospital platform company founded in 2015 out of Northwestern Medicine that pairs NVIDIA GPU-powered edge sensors — dual 4K cameras, multi-microphone arrays and RTLS radios — with computer vision, speech recognition and deep learning to deliver virtual nursing, ambient clinical documentation, operating-room coordination, patient-safety monitoring, asset and staff tracking, environmental monitoring and predictive analytics across 400+ hospitals in 30+ US health systems. The platform integrates natively and bi-directionally with Epic and Oracle Cerner EHRs, processes video on-premise rather than in the public cloud, and holds HIPAA Expert Determination Certification. Artisight publishes no public developer program, product API or SDK; its only public machine-readable surfaces are the WordPress content REST API, an OAuth 2.0-protected MCP server and an llms.txt on artisight.com.
image: https://artisight.com/wp-content/uploads/2026/01/Artisight-Fallback-Homepage-Image-Video.jpg
layout: provider
mcp_servers:
- description: ''
  name: artisight-mcp.yml
  slug: artisight-mcpyml
modified: '2026-08-02'
name: Artisight
nav: Providers
network: true
overview: 'Artisight publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Artificial Intelligence, Computer Vision, and Hospitals.


  Artisight''s developer surface includes engineering blog, support, signup flow, authentication, and 19 more developer resources.'
random_paper: 81
scopes:
- name: Artisight Scopes
  scope_count: 1
  slug: artisight-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: emerging
  composite: 26.2
  delta: 0.0
  facets:
    commercial_clarity: 31.6
    contract_quality: 0.0
    developer_ergonomics: 26.1
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 5.3
  previous_composite: 26.2
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 53.8
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/artisight/refs/heads/main/screenshots/artisight-2026-08-07T161741.png
security:
- kind: authentication
  name: Artisight Authentication
  slug: artisight-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Artisight Domain Security
  slug: artisight-domain-security
  summary_line: TLSv1.3 · DMARC
slug: artisight
tags:
- Company
- Healthcare
- Artificial Intelligence
- Computer Vision
- Hospitals
- Ambient Intelligence
- Electronic Health Records
- Machine Learning
- Patient Monitoring
- Internet of Things
website: https://artisight.com/
---
