---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 11.5
  scored_at: '2026-07-23'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/iambuddycom-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://buddy.insure/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://my.buddy.insure
- group: start
  title: ''
  type: Login
  url: https://my.buddy.insure
- group: operate
  title: ''
  type: Support
  url: https://buddyinsure.atlassian.net/servicedesk/customer/portals
- group: company
  title: ''
  type: Blog
  url: https://buddy.insure/buddy-blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://buddy.insure/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://buddy.insure/privacy
- group: company
  title: ''
  type: About
  url: https://buddy.insure/about
- group: commercial
  title: ''
  type: Licenses
  url: https://buddy.insure/licenses
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/buddyinsurance
- group: agent
  title: ''
  type: MCPServer
  url: mcp/iambuddycom-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/iambuddycom-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/iambuddycom-conformance.yml
- group: design
  title: ''
  type: Components
  url: components/iambuddycom-components.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/iambuddycom-llms.txt
created: '2026-07-17'
description: Buddy (iambuddy.com, now buddy.insure) is a digital insurance commerce platform that turns insurance product rules, pricing, and workflows into structured data via its Insurance Object Notation (ION) engine, so carriers, MGAs, brokers, and agents can sell P&C insurance online across direct, agent-assisted, embedded, and agentic channels without core-system changes. Its Offer Element embeddable checkout widget adds quote, apply, bind, and pay in a few lines of code, and Buddy MCP connects insurance products to AI assistants such as Claude for conversational selling. Founded by Charles Merritt and David Vogeleer in Richmond, Virginia, Buddy is licensed in all 50 states and is SOC 2 Type 2 and PCI DSS compliant, working with carriers including Allstate, Aon, W.R. Berkley, Chubb, Great American, and Starr.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/iambuddycom.png
layout: provider
mcp_servers:
- description: ''
  name: Buddy MCP
  slug: buddy-mcp
modified: '2026-07-19'
name: iambuddy.com
nav: Providers
network: true
overview: 'iambuddy.com is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurance, InsurTech, Embedded Insurance, and Insurance Commerce.


  iambuddy.com''s developer surface includes support, engineering blog, and 14 more developer resources.'
random_paper: 44
score:
  band: emerging
  composite: 24.8
  delta: 4.8
  facets:
    commercial_clarity: 42.1
    contract_quality: 0.0
    developer_ergonomics: 23.9
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 20.0
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 52.2
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: domain-security
  name: Iambuddycom Domain Security
  slug: iambuddycom-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: iambuddycom
tags:
- Company
- Insurance
- InsurTech
- Embedded Insurance
- Insurance Commerce
- P&C Insurance
- MCP
- Payments
website: https://buddy.insure/
---
