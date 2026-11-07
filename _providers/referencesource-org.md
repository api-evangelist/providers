---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
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
    mcp_tool_quality: na
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
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Reference Source provides 285 curated datasets via a JSON-RPC API.
  name: Referencesource API
  slug: referencesource-api
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/referencesource-org/llms/referencesource-org-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/referencesource-org-llms.txt
- group: agent
  href: https://artifacts.apis.io/referencesource-org/mcp/referencesource-org-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/referencesource-org-mcp.yml
- group: other
  href: https://artifacts.apis.io/referencesource-org/hosts/referencesource-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/referencesource-org-hosts.yml
- group: other
  href: https://artifacts.apis.io/referencesource-org/vendors/referencesource-org-vendors.yml
  title: ''
  type: Vendors
  url: vendors/referencesource-org-vendors.yml
- group: auth
  href: https://artifacts.apis.io/referencesource-org/security/referencesource-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/referencesource-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://referencesource.org/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://referencesource.org/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://referencesource.org/terms/
coverage:
  checked: '2026-10-29'
  detail: The provider's website offers a JSON‑RPC API but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract.
  evidence:
  - status: 200
    url: https://referencesource.org/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Reference Source provides a curated data catalog of 285 reference datasets and over 109,667 records, assembled from 866 primary sources. Every value includes the source URL and the exact quoted sentence, verified on the shown date.
image: https://referencesource.org/icon.svg
layout: provider
mcp_servers:
- description: Remote MCP server at referencesource.org.
  name: referencesource-org MCP Server
  slug: referencesource-org-mcp-yml
modified: '2026-10-29'
name: referencesource-org
nav: Providers
network: true
overview: referencesource-org is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Data, Catalog, Reference, and Open Data.
random_paper: 5
scopes:
- name: Referencesource Org Scopes
  scope_count: 0
  slug: referencesource-org-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 9.7
  coverage:
    artifact_dirs: 19
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.3
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 66.7
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 13.0
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/referencesource-org/referencesource-org-2026-11-03T142112.png
security:
- kind: authentication
  name: Referencesource Org Authentication
  slug: referencesource-org-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Referencesource Org Domain Security
  slug: referencesource-org-domain-security
  summary_line: TLSv1.3
slug: referencesource-org
tags:
- Data
- Catalog
- Reference
- Open Data
website: https://referencesource.org/
---
