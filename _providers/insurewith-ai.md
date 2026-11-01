---
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Provides Medicare Part D coverage simulation and drug coverage restriction tools via MCP JSON‑RPC endpoint.
  name: InsureWith.ai API
  slug: insurewith-ai-api
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/insurewith-ai/llms/insurewith-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/insurewith-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/insurewith-ai/mcp/insurewith-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/insurewith-ai-mcp.yml
- group: other
  href: https://artifacts.apis.io/insurewith-ai/hosts/insurewith-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/insurewith-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/insurewith-ai/vendors/insurewith-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/insurewith-ai-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://insurewith.ai/news
- group: auth
  href: https://artifacts.apis.io/insurewith-ai/security/insurewith-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/insurewith-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://insurewith.ai/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://insurewith.ai/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://insurewith.ai/terms
- group: operate
  title: ''
  type: Support
  url: https://insurewith.ai/contact
- group: start
  title: ''
  type: GettingStarted
  url: https://insurewith.ai/about
created: '2026-10-30'
description: InsureWith.ai provides a searchable platform that aggregates prescription drug formulary and coverage data from Medicare Part D, ACA Marketplace plans, and commercial insurers. By combining CMS Medicare Plan Finder data, state marketplace feeds, Humana FHIR formulary API, Medicaid NADAC pricing, and FDA OpenFDA drug identifiers, the service makes drug coverage, cost estimates, and prior‑authorization requirements transparent for patients, benefits managers, and pharmacists. The company is a property of BuiltForAI, LLC, a healthcare technology firm building AI‑powered health intelligence platforms.
image: https://placehold.co/600x400?text=InsureWith.ai
layout: provider
mcp_servers:
- description: Remote MCP server at insurewith.ai.
  name: insurewith-ai MCP Server
  slug: insurewith-ai-mcp-yml
modified: '2026-10-30'
name: insurewith-ai
nav: Providers
network: true
overview: 'insurewith-ai is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Insurance, Pharmacy, and Data.


  insurewith-ai''s developer surface includes support, getting-started guide, and 9 more developer resources.'
random_paper: 9
scopes:
- name: Insurewith Ai Scopes
  scope_count: 0
  slug: insurewith-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 14.7
  coverage:
    artifact_dirs: 17
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 58.3
    operational_transparency: 0.0
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 25.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Insurewith Ai Authentication
  slug: insurewith-ai-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Insurewith Ai Domain Security
  slug: insurewith-ai-domain-security
  summary_line: TLSv1.3
slug: insurewith-ai
tags:
- Company
- Healthcare
- Insurance
- Pharmacy
- Data
- AI
website: https://insurewith.ai/
---
