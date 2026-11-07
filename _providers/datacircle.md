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
    mcp_server: verified
    mcp_tool_quality: full
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 15.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Remote Streamable HTTP MCP server, open with no key, answering from the Datacircle sheet of GTM APIs: list_apis lists the GTM APIs on it, and search_plans finds their plans by API, provider or price, '
  name: Datacircle MCP Server
  slug: datacircle-mcp
artifact_total: 3
common:
- group: build
  href: https://artifacts.apis.io/datacircle/integrations/datacircle-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/datacircle-integration-edges.yml
- group: agent
  href: https://artifacts.apis.io/datacircle/llms/datacircle-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/datacircle-llms.txt
- group: agent
  href: https://artifacts.apis.io/datacircle/mcp/datacircle-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/datacircle-mcp.yml
- group: docs
  title: ''
  type: Documentation
  url: https://datacircle.dev/docs/mcp
- group: agent
  href: https://artifacts.apis.io/datacircle/well-known/datacircle-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/datacircle-well-known.yml
- group: other
  href: https://artifacts.apis.io/datacircle/hosts/datacircle-hosts.yml
  title: ''
  type: Hosts
  url: hosts/datacircle-hosts.yml
- group: auth
  href: https://artifacts.apis.io/datacircle/security/datacircle-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/datacircle-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://datacircle.dev
- group: docs
  title: ''
  type: Documentation
  url: https://datacircle.dev/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/waynehamadi/datacircle
- group: start
  title: ''
  type: Login
  url: https://datacircle.dev/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://datacircle.dev/terms
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/datacircle-org
- group: other
  title: ''
  type: X
  url: https://x.com/datacircle_dev
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://datacircle.dev/privacy
- group: operate
  title: ''
  type: Support
  url: https://datacircle.dev/support
created: '2026-10-09'
description: 'Datacircle lists all the GTM APIs. Its MCP server is open to anyone, with no key: add api.datacircle.dev/mcp to Claude, ChatGPT or Cursor. It answers from the sheet. list_apis lists the GTM APIs on it, and search_plans finds their plans by API, provider or price. Each plan comes with its score, and the best come first, as on the sheet.'
image: https://datacircle.dev/og-datacircle-lists-all-the-gtm-apis.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at api.datacircle.dev over streamable HTTP; 2 tools listed.
  name: Datacircle MCP Server
  slug: datacircle-mcp-server
modified: '2026-10-21'
name: Datacircle
nav: Providers
network: true
overview: 'Datacircle is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, B2B Data, and MCP.


  Datacircle''s developer surface includes documentation, support, and 14 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 10.3
  coverage:
    artifact_dirs: 23
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -23.9
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 66.7
    operational_transparency: 2.6
  previous_composite: 34.2
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/datacircle/datacircle-2026-10-11T103549.png
security:
- kind: domain-security
  name: Datacircle Domain Security
  slug: datacircle-domain-security
  summary_line: TLSv1.3 · DMARC
slug: datacircle
tags:
- Company
- B2B Data
- MCP
website: https://datacircle.dev
---
