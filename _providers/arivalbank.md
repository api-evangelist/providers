---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    mcp_tool_quality: three_quarters
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Arivalbank provides digital banking services; API details are not publicly documented.
  name: Arivalbank API
  slug: arivalbank-api
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/arivalbank/llms/arivalbank-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/arivalbank-llms.txt
- group: agent
  href: https://artifacts.apis.io/arivalbank/mcp/arivalbank-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/arivalbank-mcp.yml
- group: other
  href: https://artifacts.apis.io/arivalbank/hosts/arivalbank-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arivalbank-hosts.yml
- group: other
  href: https://artifacts.apis.io/arivalbank/vendors/arivalbank-vendors.yml
  title: ''
  type: Vendors
  url: vendors/arivalbank-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://arival.com/document/terms-of-use
- group: auth
  title: ''
  type: Security
  url: https://arival.com/user-guide/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://arival.com/document/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://arival.com/faq/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://developers.arival.com/
- group: auth
  href: https://artifacts.apis.io/arivalbank/security/arivalbank-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arivalbank-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arival.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: null
    url: https://status.arival.com/mcp
  - status: 403
    url: https://app.arival.com/mcp
  - status: 403
    url: https://developers.arival.com/mcp
  - status: 403
    url: https://equityzen.com/company/arivalbank
  reason: no-developer-program
  state: none
created: '2026-09-26'
description: Arivalbank is a digital banking platform offering global financial services for businesses and startups. It provides multi-currency accounts, stablecoin solutions, and card issuance, enabling users to manage personal and corporate finances worldwide. Licensed in Puerto Rico, Arival Bank operates internationally with a focus on seamless cross-border transactions and modern banking experiences.
image: https://arival.com/_gatsby/file/a7a4555ab04c405ae4cf299b99b69c2c/og-image_eng.png?u=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fark6fr17%2Fproduction%2F8bebeaa1427f46010fcaf6e3f916dc07ea940994-4800x2520.png
layout: provider
mcp_servers:
- description: Remote MCP server at status.arival.com; 193 tools listed.
  name: Arivalbank MCP Server
  slug: arivalbank-mcp-yml
modified: '2026-09-26'
name: Arivalbank
nav: Providers
network: true
overview: 'Arivalbank is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Fintech, Banking, Digital Banking, Global Payments, and Stablecoins.


  Arivalbank''s developer surface includes pricing, documentation, and 9 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 9.6
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.2
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 66.7
    operational_transparency: 5.3
  previous_composite: 14.8
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 7.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/arivalbank/arivalbank-2026-10-11T100311.png
security:
- kind: domain-security
  name: Arivalbank Domain Security
  slug: arivalbank-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: arivalbank
tags:
- Fintech
- Banking
- Digital Banking
- Global Payments
- Stablecoins
website: https://arival.com
---
