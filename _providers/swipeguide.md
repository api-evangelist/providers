---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 0.0
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: REST API for the L2L Dispatch Smart Manufacturing Platform. HTTPS GET/POST/PUT/DELETE over per-tenant hosts, API-key authenticated, JSON by default (XML optional). Covers 60+ shop-floor resources incl
  name: L2L Dispatch API
  slug: l2l-dispatch-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.l2l.com/
- group: docs
  title: ''
  type: Documentation
  url: https://support.leading2lean.com/hc/en-us/articles/360051148492-API-Documentation
- group: docs
  title: ''
  type: APIReference
  url: https://support.leading2lean.com/hc/en-us/sections/360010979571-APIs-Integration
- group: start
  title: ''
  type: GettingStarted
  url: https://support.leading2lean.com/hc/en-us/articles/360051600711-API-Code-Examples
- group: operate
  title: ''
  type: Support
  url: https://support.leading2lean.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.l2l.com/customer-support
- group: company
  title: ''
  type: Blog
  url: https://www.l2l.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/leading2lean
- group: start
  title: ''
  type: SignUp
  url: https://www.l2l.com/get-started
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.l2l.com/trust-center
- group: auth
  title: ''
  type: Compliance
  url: https://www.l2l.com/security-compliance
- group: operate
  title: ''
  type: ChangeLog
  url: https://leading2lean.atlassian.net/wiki/spaces/LCL/overview
- group: build
  title: ''
  type: Packages
  url: packages/swipeguide-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/swipeguide-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/swipeguide-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/swipeguide-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/swipeguide-llms.txt
created: '2026-07-17'
description: SwipeGuide was a frontline digital work-instruction platform for manufacturing that has since been acquired by L2L (formerly Leading2Lean); the swipeguide.com domain now 301-redirects to l2l.com. L2L operates a Connected Workforce / Connected Manufacturing Operations platform (the L2L Dispatch Smart Manufacturing Platform) spanning maintenance, production monitoring, quality, skills, and digital work instructions on the shop floor. It exposes the L2L Dispatch REST API (v1.0) for reading and writing shop-floor data — sites, areas, lines, machines, dispatches, pitches, work orders, kaizen and more — authenticated with an API key (query auth, L2LAUTH header, or POST body) plus optional HMAC-SHA512 request signing, returning JSON (default) or XML.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/swipeguide.png
layout: provider
modified: '2026-07-21'
name: Swipeguide
nav: Providers
network: true
overview: 'Swipeguide publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Manufacturing, Work Instructions, Frontline, and Shop Floor.


  Swipeguide''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, changelog, and 10 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 25.6
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 39.1
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 25.6
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Swipeguide Authentication
  slug: swipeguide-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Swipeguide Domain Security
  slug: swipeguide-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Swipeguide Trust Center
  slug: swipeguide-trust-center
  summary_line: SOC 2 Type 2, NIST 800-171, 21 CFR Part 11, ISO 13485, ISO 55000, ITAR, DFARS, GDPR, CCPA
slug: swipeguide
tags:
- Company
- Manufacturing
- Work Instructions
- Frontline
- Shop Floor
- Maintenance
- Connected Worker
- Smart Manufacturing
- Industrial
website: https://www.l2l.com/
---
