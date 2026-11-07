---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 58.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Govly Agentic Access
  operation_count: 32
  slug: govly-agentic-access
  summary_line: 32 operations · 13 acting
api_count: 1
apis:
- baseURL: https://app.govly.com
  baseurl_source: declared
  description: Search and inspect awarded government contracts.
  name: Govly Awards API
  slug: govly-awards-api
- baseURL: https://app.govly.com
  baseurl_source: declared
  description: Read document representations and request temporary original-file downloads.
  name: Govly Documents API
  slug: govly-documents-api
- baseURL: https://app.govly.com
  baseurl_source: declared
  description: Follow opportunities and related workspace activity.
  name: Govly Follows API
  slug: govly-follows-api
- baseURL: https://app.govly.com
  baseurl_source: declared
  description: Read and triage the authenticated user's matched inbox items.
  name: Govly Inbox API
  slug: govly-inbox-api
- baseURL: https://app.govly.com
  baseurl_source: declared
  description: Search, fetch, and inspect Govly opportunity records.
  name: Govly Opportunities API
  slug: govly-opportunities-api
- baseURL: https://app.govly.com
  baseurl_source: declared
  description: Inspect quote submission requirements, submit quotes, and poll submission status.
  name: Govly Quote Submissions API
  slug: govly-quote-submissions-api
- baseURL: https://app.govly.com
  baseurl_source: declared
  description: List saved opportunity searches and cached matches.
  name: Govly Saved Searches API
  slug: govly-saved-searches-api
- baseURL: https://app.govly.com
  baseurl_source: declared
  description: List and upload workspace attachments.
  name: Govly Workspace Attachments API
  slug: govly-workspace-attachments-api
- baseURL: https://app.govly.com
  baseurl_source: declared
  description: Post comments to workspaces.
  name: Govly Workspace Comments API
  slug: govly-workspace-comments-api
- baseURL: https://app.govly.com
  baseurl_source: declared
  description: Add users and teams to workspaces.
  name: Govly Workspace Members API
  slug: govly-workspace-members-api
- baseURL: https://app.govly.com
  baseurl_source: declared
  description: Create, update, and inspect opportunity workspaces.
  name: Govly Workspaces API
  slug: govly-workspaces-api
- baseURL: https://app.govly.com
  baseurl_source: declared
  description: Search and inspect government points of contact.
  name: Govly Contacts API
  slug: govly-contacts-api
- baseURL: https://app.govly.com
  baseurl_source: declared
  description: List, create, rename, recolor, and delete the organization's labels.
  name: Govly Organization Labels API
  slug: govly-organization-labels-api
- baseURL: https://app.govly.com
  baseurl_source: declared
  description: Discover the members of your organization and their account status.
  name: Govly Organization Users API
  slug: govly-organization-users-api
- baseURL: https://app.govly.com
  baseurl_source: declared
  description: Resolve place names to canonical Govly Place ids.
  name: Govly Places API
  slug: govly-places-api
- baseURL: https://app.govly.com
  baseurl_source: declared
  description: List government contract price lists and search their line items.
  name: Govly Product Catalogs API
  slug: govly-product-catalogs-api
- baseURL: https://app.govly.com
  baseurl_source: declared
  description: Share opportunities, awards, and contacts with colleagues by email.
  name: Govly Shares API
  slug: govly-shares-api
- baseURL: https://app.govly.com
  baseurl_source: declared
  description: Search clustered procurement and market intelligence signals.
  name: Govly Signals API
  slug: govly-signals-api
artifact_total: 42
asyncapis:
- description: ''
  name: Govly Webhooks
  slug: govly-webhooks
collections:
- collection_type: open
  name: Govly Tools API (Alpha) Awards API
  slug: open-govly-awards-api
- collection_type: open
  name: Govly Tools API (Alpha) Awards Documents API
  slug: open-govly-documents-api
- collection_type: open
  name: Govly Tools API (Alpha) Awards Follows API
  slug: open-govly-follows-api
- collection_type: open
  name: Govly Tools API (Alpha) Awards Inbox API
  slug: open-govly-inbox-api
- collection_type: open
  name: Govly Tools API (Alpha) Awards Opportunities API
  slug: open-govly-opportunities-api
- collection_type: open
  name: Govly Tools API (Alpha) Awards Quote Submissions API
  slug: open-govly-quote-submissions-api
- collection_type: open
  name: Govly Tools API (Alpha) Awards Saved Searches API
  slug: open-govly-saved-searches-api
- collection_type: open
  name: Govly Tools API (Alpha) Awards Workspace Attachments API
  slug: open-govly-workspace-attachments-api
- collection_type: open
  name: Govly Tools API (Alpha) Awards Workspace Comments API
  slug: open-govly-workspace-comments-api
- collection_type: open
  name: Govly Tools API (Alpha) Awards Workspace Members API
  slug: open-govly-workspace-members-api
- collection_type: open
  name: Govly Tools API (Alpha) Awards Workspaces API
  slug: open-govly-workspaces-api
common:
- group: commercial
  href: https://artifacts.apis.io/govly/plans/govly-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/govly-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/govly/capabilities/govly-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/govly-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/govly/agentic-access/govly-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/govly-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/govly/security/govly-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/govly-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/govly/authentication/govly-authentication.yml
  title: ''
  type: Authentication
  url: authentication/govly-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.govly.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.govly.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.govly.com/getting-started/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.govly.com/api-reference/tools-v1/opportunities/search-opportunities
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.govly.com/getting-started/introduction
- group: company
  title: ''
  type: Blog
  url: https://www.govly.com/blog
- group: operate
  title: ''
  type: Support
  url: https://intercom.help/govly/en
- group: commercial
  title: ''
  type: Pricing
  url: https://www.govly.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.govly.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.govly.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.govly.com
- group: auth
  title: ''
  type: TrustCenter
  url: https://security.govly.com
- group: auth
  title: ''
  type: Compliance
  url: https://docs.govly.com/enterprise/security
- group: agent
  href: https://artifacts.apis.io/govly/mcp/govly-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/govly-mcp.yml
- group: agent
  href: https://artifacts.apis.io/govly/llms/govly-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/govly-llms.txt
- group: docs
  href: https://artifacts.apis.io/govly/openapi/_original/govly-tools-v1-openapi-original.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/govly-tools-v1-openapi-original.yml
- group: design
  href: https://artifacts.apis.io/govly/asyncapi/govly-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/govly-webhooks.yml
- group: design
  href: https://artifacts.apis.io/govly/conventions/govly-conventions.yml
  title: ''
  type: Conventions
  url: conventions/govly-conventions.yml
- group: design
  href: https://artifacts.apis.io/govly/errors/govly-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/govly-problem-types.yml
- group: design
  href: https://artifacts.apis.io/govly/lifecycle/govly-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/govly-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/govly/conformance/govly-conformance.yml
  title: ''
  type: Conformance
  url: conformance/govly-conformance.yml
- group: design
  href: https://artifacts.apis.io/govly/data-model/govly-data-model.yml
  title: ''
  type: DataModel
  url: data-model/govly-data-model.yml
- group: other
  href: https://artifacts.apis.io/govly/overlays/govly-tools-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/govly-tools-v1-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/govly/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Govly is an AI-powered market network for government contractors — primes, OEMs, VARs, and distributors — that ingests, parses, and analyzes federal and SLED (state, local, education) procurement data to surface RFQ/RFI opportunities and contract awards across 40+ federal contract vehicles and state/local procurement portals. The platform provides pipeline building, award tracking, competitor intelligence, AI matching agents, shared opportunity workspaces, and quote submission automation. Govly exposes an enterprise Tools API (agent- and automation-oriented, REST/JSON over HTTPS with API-key auth), a hosted MCP server for AI clients, webhooks for real-time opportunity and workspace events, and CRM integrations (Salesforce, HubSpot). Govly is SOC 2 Type I and CMMC compliant, hosted on AWS in the USA, and backed by Insight Partners.
finops:
- has_sources: true
  method: derived
  name: Govly Finops
  primary_unit: ''
  service_category: ''
  slug: govly-finops
  template: true
image: https://cdn.prod.website-files.com/65f9f755792648d187d6d0dd/69e7b31d3d986500bd367ba0_webclip-256.png
layout: provider
mcp_servers:
- description: Remote MCP server at app.govly.com over HTTP; 7 tools listed.
  name: Govly MCP Server
  slug: govly
modified: '2026-07-19'
name: Govly
nav: Providers
network: true
overview: 'Govly publishes 18 API contracts indexed on the [APIs.io](https://apis.io/) network, including Awards API, Documents API, Follows API, and 15 more. Tagged areas include Company, Government, Public Sector, Procurement, and Government Contracting.


  The Govly catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Govly''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, support, pricing, and 22 more developer resources.'
plans:
- name: Govly Plans Pricing
  plan_count: 2
  slug: govly-plans-pricing
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 100
  extends:
  - spectral:oas
  name: Govly API Rules
  rule_count: 59
  severity_counts:
    error: 49
    hint: 0
    info: 2
    warn: 8
  slug: govly-rules
score:
  band: strong
  composite: 55.1
  coverage:
    artifact_dirs: 27
    catalog_earned: 49.5
    catalog_earned_first_party: 8.0
    catalog_gap: 65.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.8
  facets:
    access_clarity: 60.5
    contract_governance: 31.8
    contract_quality: 60.3
    developer_ergonomics: 58.9
    discoverability: 75.0
    operational_transparency: 23.7
  previous_composite: 54.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 60.0
      total: 30
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 29.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/govly/govly-2026-07-25T220138.png
security:
- kind: authentication
  name: Govly Authentication
  slug: govly-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Govly Domain Security
  slug: govly-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Govly Trust Center
  slug: govly-trust-center
  summary_line: SOC 2 Type I, CMMC Level 1, CMMC Level 2
skill_count: 4
skills:
- name: Find and track a government opportunity
  slug: govly-find-and-track-opportunity
- name: Research government contract awards
  slug: govly-research-awards
- name: Submit a quote to a procurement portal
  slug: govly-submit-a-quote
- name: Triage the Govly AI-match inbox
  slug: govly-triage-inbox
slug: govly
tags:
- Company
- Government
- Public Sector
- Procurement
- Government Contracting
- GovTech
- Market Intelligence
- Awards
- Opportunities
- Agents
website: https://www.govly.com/
---
