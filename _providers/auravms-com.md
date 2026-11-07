---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 57.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 15
  human_in_the_loop: 1
  name: Auravms Com Agentic Access
  operation_count: 35
  slug: auravms-com-agentic-access
  summary_line: 35 operations · 15 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.auravms.com
  baseurl_source: declared
  description: Dashboard stats, PDF exports, and data file downloads.
  name: AuraVMS Analytics & Export API
  slug: auravms-com-analytics-export-api
- baseURL: https://api.auravms.com
  baseurl_source: declared
  description: Create, list, and revoke API keys.
  name: AuraVMS API Key Management API
  slug: auravms-com-api-key-management-api
- baseURL: https://api.auravms.com
  baseurl_source: declared
  description: Upload and download documents attached to RFQ items.
  name: AuraVMS Attachments API
  slug: auravms-com-attachments-api
- baseURL: https://api.auravms.com
  baseurl_source: declared
  description: Create a JWT session.
  name: AuraVMS Authentication API
  slug: auravms-com-authentication-api
- baseURL: https://api.auravms.com
  baseurl_source: declared
  description: Unauthenticated service discovery.
  name: AuraVMS Discovery API
  slug: auravms-com-discovery-api
- baseURL: https://api.auravms.com
  baseurl_source: declared
  description: Save RFQs as drafts before sending to suppliers.
  name: AuraVMS Draft RFQs API
  slug: auravms-com-draft-rfqs-api
- baseURL: https://api.auravms.com
  baseurl_source: declared
  description: Submit feature requests, bug reports, or general feedback to the AuraVMS team.
  name: AuraVMS Feedback API
  slug: auravms-com-feedback-api
- baseURL: https://api.auravms.com
  baseurl_source: declared
  description: Units of measurement and product catalog.
  name: AuraVMS Reference Data API
  slug: auravms-com-reference-data-api
- baseURL: https://api.auravms.com
  baseurl_source: declared
  description: Create RFQs, send to suppliers, view quotes with L1/L2/L3 ranking, place orders.
  name: AuraVMS RFQ Lifecycle API
  slug: auravms-com-rfq-lifecycle-api
- baseURL: https://api.auravms.com
  baseurl_source: declared
  description: Create, list, and manage your supplier directory.
  name: AuraVMS Supplier Management API
  slug: auravms-com-supplier-management-api
artifact_total: 17
common:
- group: agent
  href: https://artifacts.apis.io/auravms-com/agentic-access/auravms-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/auravms-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/auravms-com/plans/auravms-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/auravms-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/auravms-com/rules/auravms-com-rules.yml
  title: ''
  type: Spectral
  url: rules/auravms-com-rules.yml
- group: design
  href: https://artifacts.apis.io/auravms-com/json-ld/auravms-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/auravms-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/auravms-com/vocabulary/auravms-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/auravms-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/auravms-com/data-model/auravms-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/auravms-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/auravms-com/conventions/auravms-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/auravms-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/auravms-com/conventions/auravms-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/auravms-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/auravms-com/authentication/auravms-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/auravms-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/auravms-com/errors/auravms-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/auravms-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/auravms-com/conformance/auravms-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/auravms-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/auravms-com/llms/auravms-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/auravms-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/auravms-com/mcp/auravms-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/auravms-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/auravms-com/well-known/auravms-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/auravms-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/auravms-com/hosts/auravms-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/auravms-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/auravms-com/vendors/auravms-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/auravms-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/auravms-com/packages/auravms-com-packages.yml
  title: ''
  type: SDKs
  url: packages/auravms-com-packages.yml
- group: build
  href: https://artifacts.apis.io/auravms-com/packages/auravms-com-packages.yml
  title: ''
  type: Packages
  url: packages/auravms-com-packages.yml
- group: start
  title: ''
  type: Login
  url: https://app.auravms.com/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.auravms.com/changelog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.auravms.com</code
- group: auth
  href: https://artifacts.apis.io/auravms-com/security/auravms-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/auravms-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://auravms.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.auravms.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.auravms.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.auravms.com/blogs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.auravms.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.auravms.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.auravms.com/privacy
created: '2026-11-02'
description: AuraVMS provides RFQ software for small businesses, enabling buyers to invite suppliers, collect private quotations, compare prices and terms, and place orders through a simple procurement OS. It replaces email and spreadsheets with a centralized platform, offering AI and MCP features, ranking quotes, supplier directory, reminders, and auditable records, all via a public REST API.
image: https://www.auravms.com/demo-screenshots/comparison.png
jsonld:
- class_count: 1
  name: Auravms Com Context
  property_count: 2
  slug: auravms-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.auravms.com.
  name: AuraVMS MCP Server
  slug: auravms-com-mcp-yml
modified: '2026-11-02'
name: AuraVMS
nav: Providers
network: true
overview: 'AuraVMS publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Analytics & Export API, API Key Management API, Attachments API, and 7 more. Tagged areas include Procurement, RFQ, Small Business, and Artificial Intelligence.


  The AuraVMS catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AuraVMS''s developer surface includes authentication, changelog, documentation, getting-started guide, engineering blog, pricing, and 23 more developer resources.'
plans:
- name: Auravms Com Plans Pricing
  plan_count: 4
  slug: auravms-com-plans-pricing
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 106
  extends:
  - spectral:oas
  name: AuraVMS API Rules
  rule_count: 65
  severity_counts:
    error: 57
    hint: 0
    info: 1
    warn: 7
  slug: auravms-com-rules
score:
  band: developing
  composite: 43.6
  coverage:
    artifact_dirs: 21
    catalog_earned: 54.8
    catalog_earned_first_party: 12.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.2
  facets:
    access_clarity: 53.9
    contract_governance: 35.6
    contract_quality: 56.3
    developer_ergonomics: 35.7
    discoverability: 56.7
    operational_transparency: 7.9
  previous_composite: 53.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Auravms Com Authentication
  slug: auravms-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Auravms Com Domain Security
  slug: auravms-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: auravms-com
tags:
- Procurement
- RFQ
- Small Business
- Artificial Intelligence
website: https://auravms.com/
---
