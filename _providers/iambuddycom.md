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
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.5
  scored_at: '2026-09-02'
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
- description: Buddy MCP is built on the Model Context Protocol and gives any MCP-compatible AI assistant (e.g. Claude) access to indexed insurance products. The AI handles the conversation; Buddy's ION Engine handl
  name: Buddy MCP
  slug: buddy-mcp
modified: '2026-07-19'
name: iambuddy.com
nav: Providers
network: true
overview: 'iambuddy.com is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurance, Insurtech, Embedded Insurance, and Insurance Commerce.


  iambuddy.com''s developer surface includes support, engineering blog, and 14 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 21.1
  coverage:
    artifact_dirs: 7
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 21.1
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 36.4
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/iambuddycom/refs/heads/main/screenshots/iambuddycom-2026-07-25T221948.png
security:
- kind: domain-security
  name: Iambuddycom Domain Security
  slug: iambuddycom-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: iambuddycom
tags:
- Company
- Insurance
- Insurtech
- Embedded Insurance
- Insurance Commerce
- P&C Insurance
- MCP
- Payments
website: https://buddy.insure/
---
