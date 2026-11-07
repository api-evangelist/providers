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
  score: 3.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Appscripthub provides a searchable marketplace for Google Apps Script libraries via its web interface and API.
  name: Appscripthub API
  slug: appscripthub-api
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/appscripthub-com/llms/appscripthub-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/appscripthub-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/appscripthub-com/mcp/appscripthub-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/appscripthub-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/appscripthub-com/hosts/appscripthub-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/appscripthub-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/appscripthub-com/vendors/appscripthub-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/appscripthub-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://appscripthub.com/terms
- group: build
  title: ''
  type: SDKs
  url: https://appscripthub.com/auth/register?redirect=/user/libraries/request
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://appscripthub.com/privacy
- group: start
  title: ''
  type: Login
  url: https://appscripthub.com/auth/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tani
- group: auth
  href: https://artifacts.apis.io/appscripthub-com/security/appscripthub-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/appscripthub-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://appscripthub.com/
coverage:
  checked: '2026-11-01'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract was found on the API host.
  evidence:
  - status: 404
    url: https://api.appscripthub.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: wywy LLC operates the GAS Library Hub, a searchable marketplace for Google Apps Script libraries and web apps. The platform lets developers discover, browse, and integrate community‑contributed GAS libraries, offering details such as library IDs, descriptions, usage stats, and licensing. It also provides tools for library authors to publish and manage their scripts, with support for OAuth2, Firestore, and other Google services. The service is free to use, with plans for future paid features, and emphasizes open collaboration within the Google Workspace ecosystem.
image: https://appscripthub.com/logo.png
layout: provider
mcp_servers:
- description: Remote MCP server at appscripthub.com.
  name: wywy LLC MCP Server
  slug: appscripthub-com-mcp-yml
modified: '2026-11-01'
name: wywy LLC
nav: Providers
network: true
overview: wywy LLC is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Google Apps Script, Library Marketplace, Open Source, and Developer Tools.
random_paper: 9
score:
  band: minimal
  composite: 9.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.3
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 56.7
    operational_transparency: 2.6
  previous_composite: 13.9
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Appscripthub Com Domain Security
  slug: appscripthub-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: appscripthub-com
tags:
- Company
- Google Apps Script
- Library Marketplace
- Open Source
- Developer Tools
website: https://appscripthub.com/
---
