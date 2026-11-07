---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.7
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Remote, read-only Model Context Protocol server (streamable HTTP) that exposes a customer's synchronised business data from Exact Online, Twinfield, AFAS and 30+ sources to AI assistants such as ChatG
  name: DigiData MCP Server
  slug: digidata-mcp-server
- description: Each DigiData integration provides an OData feed of the synchronised records that can be loaded directly into Power BI ("Get Data" > OData feed, paste your DigiData URL) or Excel, alongside CSV export
  name: DigiData OData Feeds
  slug: digidata-odata-feeds
artifact_total: 8
common:
- group: commercial
  href: https://artifacts.apis.io/digi-data-nl/plans/digi-data-nl-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/digi-data-nl-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/digi-data-nl/conventions/digi-data-nl-conventions.yml
  title: ''
  type: Conventions
  url: conventions/digi-data-nl-conventions.yml
- group: auth
  href: https://artifacts.apis.io/digi-data-nl/authentication/digi-data-nl-authentication.yml
  title: ''
  type: Authentication
  url: authentication/digi-data-nl-authentication.yml
- group: auth
  href: https://artifacts.apis.io/digi-data-nl/scopes/digi-data-nl-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/digi-data-nl-scopes.yml
- group: design
  href: https://artifacts.apis.io/digi-data-nl/conformance/digi-data-nl-conformance.yml
  title: ''
  type: Conformance
  url: conformance/digi-data-nl-conformance.yml
- group: agent
  href: https://artifacts.apis.io/digi-data-nl/llms/digi-data-nl-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/digi-data-nl-llms.txt
- group: auth
  href: https://artifacts.apis.io/digi-data-nl/well-known/digi-data-nl-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/digi-data-nl-security.txt
- group: auth
  href: https://artifacts.apis.io/digi-data-nl/well-known/digi-data-nl-digi-data-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/digi-data-nl-digi-data-security.txt
- group: agent
  href: https://artifacts.apis.io/digi-data-nl/well-known/digi-data-nl-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/digi-data-nl-well-known.yml
- group: other
  href: https://artifacts.apis.io/digi-data-nl/hosts/digi-data-nl-hosts.yml
  title: ''
  type: Hosts
  url: hosts/digi-data-nl-hosts.yml
- group: build
  href: https://artifacts.apis.io/digi-data-nl/integrations/digi-data-nl-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/digi-data-nl-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/digi-data-nl/vendors/digi-data-nl-vendors.yml
  title: ''
  type: Vendors
  url: vendors/digi-data-nl-vendors.yml
- group: company
  title: ''
  type: Website
  url: https://www.digi-data.nl/
- group: auth
  href: https://artifacts.apis.io/digi-data-nl/security/digi-data-nl-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/digi-data-nl-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/digi-data-nl/security/digi-data-nl-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/digi-data-nl-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://www.digi-data.nl/en/mcp
- group: start
  title: ''
  type: Login
  url: https://app.digi-data.nl/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.digi-data.nl/en/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.digi-data.nl/en/blog
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.digi-data.nl/en/faq
- group: operate
  title: ''
  type: Support
  url: https://www.digi-data.nl/en/contact
- group: company
  title: ''
  type: About
  url: https://www.digi-data.nl/en/about
- group: auth
  title: ''
  type: Security
  url: https://www.digi-data.nl/en/security
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.digi-data.nl/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.digi-data.nl/en/privacy
- group: agent
  title: ''
  type: LLMsTxt
  url: https://www.digi-data.nl/llms.txt
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/digidatabv/about/
created: '2026-11-05'
description: DigiData (DigiData B.V., KvK 96280328, Zuidlaren, the Netherlands; founded 2025) is Dutch AI dashboard and BI software for SMEs. It connects accounting, CRM and project-administration systems such as Exact Online, Twinfield, HubSpot, Simplicate, Xero and QuickBooks Online, periodically synchronises that data into a central, isolated environment, and builds interactive KPI dashboards with an AI agent, shareable without per-viewer licences. The synchronised data is also exposed via OData feeds for Power BI and Excel, CSV export, and a remote read-only MCP connection for AI assistants such as ChatGPT and Claude.
image: https://www.digi-data.nl/og-image.png
layout: provider
modified: '2026-11-05'
name: DigiData
nav: Providers
network: true
overview: 'DigiData is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Business Intelligence, Dashboards, AI Agents, and MCP.


  DigiData''s developer surface includes authentication, documentation, pricing, engineering blog, support, and 22 more developer resources.'
plans:
- name: Digi Data Nl Plans Pricing
  plan_count: 5
  slug: digi-data-nl-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Digi Data Nl Rate Limits
  slug: digi-data-nl-rate-limits
scopes:
- name: Digi Data Nl Scopes
  scope_count: 3
  slug: digi-data-nl-scopes
  summary_line: 3 scopes
score:
  band: thin
  composite: 34.9
  coverage:
    artifact_dirs: 16
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 64.3
    operational_transparency: 10.5
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 39.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Digi Data Nl Authentication
  slug: digi-data-nl-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Digi Data Nl Domain Security
  slug: digi-data-nl-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Digi Data Nl Vulnerability Disclosure
  slug: digi-data-nl-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: digi-data-nl
tags:
- Company
- Business Intelligence
- Dashboards
- AI Agents
- MCP
- OData
- Power BI
- Data Integration
- Accounting
- Netherlands
website: https://www.digi-data.nl/
---
