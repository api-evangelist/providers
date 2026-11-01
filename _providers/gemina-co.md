---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 9.6
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Extract structured data from invoices and financial documents, then search, aggregate, and chat.
  name: Gemina API
  slug: gemina-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/gemina-co/plans/gemina-co-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/gemina-co-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/gemina-co/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/gemina-co/conformance/gemina-co-conformance.yml
  title: ''
  type: Conformance
  url: conformance/gemina-co-conformance.yml
- group: agent
  href: https://artifacts.apis.io/gemina-co/llms/gemina-co-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gemina-co-llms.txt
- group: agent
  href: https://artifacts.apis.io/gemina-co/mcp/gemina-co-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/gemina-co-mcp.yml
- group: other
  href: https://artifacts.apis.io/gemina-co/hosts/gemina-co-hosts.yml
  title: ''
  type: Hosts
  url: hosts/gemina-co-hosts.yml
- group: other
  href: https://artifacts.apis.io/gemina-co/vendors/gemina-co-vendors.yml
  title: ''
  type: Vendors
  url: vendors/gemina-co-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.gemina.co/trust-center
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.gemina.co/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gemina.co/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.gemina.co/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://www.gemina.co/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.gemina.co</code
- group: auth
  href: https://artifacts.apis.io/gemina-co/security/gemina-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gemina-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.gemina.co/
created: '2026-10-30'
description: Gemina provides document AI APIs for extraction, search, analytics, and chat. Upload any document to receive typed structured data, perform hybrid search, compute exact totals, and engage in grounded chat with citations. The platform offers a free FileTag tier with 1,500 tags per month and supports OAuth 2.1 or API‑key authentication across REST, SDKs, and MCP tools.
image: https://www.gemina.co/images/og-image.png
layout: provider
mcp_servers:
- description: Remote MCP server at api.gemina.co requiring an API key.
  name: gemina-co MCP Server
  slug: gemina-co-mcp-yml
modified: '2026-10-30'
name: gemina-co
nav: Providers
network: true
overview: 'gemina-co is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, DocumentAI, Extraction, Search, and Analytics.


  gemina-co''s developer surface includes pricing, documentation, and 13 more developer resources.'
plans:
- name: Gemina Co Plans Pricing
  plan_count: 6
  slug: gemina-co-plans-pricing
random_paper: 16
score:
  band: thin
  composite: 29.3
  coverage:
    artifact_dirs: 12
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 71.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 25.5
    discoverability: 65.0
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Gemina Co Domain Security
  slug: gemina-co-domain-security
  summary_line: TLSv1.3 · DMARC
slug: gemina-co
tags:
- Company
- DocumentAI
- Extraction
- Search
- Analytics
- Chat
website: https://www.gemina.co/
---
