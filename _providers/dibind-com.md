---
access_model:
  confidence: high
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Dibind Com Agentic Access
  operation_count: 7
  slug: dibind-com-agentic-access
  summary_line: 7 operations
api_count: 1
apis:
- description: 'Static machine-readable JSON indexes published on dibind.com and listed in its llms.txt: catalogue product families (/api/catalog-products.json), capabilities summary, FSC index, NSN sample, and the D'
  name: Dibblee Catalogue and FLIS JSON Indexes
  slug: dibblee-json-indexes
- baseURL: https://daitk-tic.dibind.com
  baseurl_source: declared
  description: 'The main resolver: HS code + origin -> total duty'
  name: Dibblee Industries Duty API
  slug: dibind-com-duty-api
- baseURL: https://daitk-tic.dibind.com
  baseurl_source: declared
  description: Raw tariff schedule and trade-measure lookups
  name: Dibblee Industries Reference API
  slug: dibind-com-reference-api
- baseURL: https://daitk-tic.dibind.com
  baseurl_source: declared
  description: What this service reads and how current it is
  name: Dibblee Industries Status API
  slug: dibind-com-status-api
artifact_total: 18
common:
- group: agent
  href: https://artifacts.apis.io/dibind-com/agentic-access/dibind-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/dibind-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/dibind-com/rate-limits/dibind-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/dibind-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/dibind-com/plans/dibind-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dibind-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/dibind-com/rules/dibind-com-rules.yml
  title: ''
  type: Spectral
  url: rules/dibind-com-rules.yml
- group: design
  href: https://artifacts.apis.io/dibind-com/json-ld/dibind-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dibind-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/dibind-com/vocabulary/dibind-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dibind-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/dibind-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/dibind-com/data-model/dibind-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dibind-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/dibind-com/conventions/dibind-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/dibind-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/dibind-com/authentication/dibind-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dibind-com-authentication.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://daitk-tic.dibind.com/status
- group: design
  href: https://artifacts.apis.io/dibind-com/lifecycle/dibind-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/dibind-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/dibind-com/errors/dibind-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dibind-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/dibind-com/conformance/dibind-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dibind-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/dibind-com/overlays/dibind-com-daitk-tic-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/dibind-com-daitk-tic-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/dibind-com/llms/dibind-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dibind-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/dibind-com/llms/dibind-com-daitk-tic-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dibind-com-daitk-tic-llms.txt
- group: build
  href: https://artifacts.apis.io/dibind-com/mcp/dibind-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/dibind-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/dibind-com/mcp/dibind-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/dibind-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/dibind-com/hosts/dibind-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dibind-com-hosts.yml
- group: build
  href: https://artifacts.apis.io/dibind-com/integrations/dibind-com-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/dibind-com-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/dibind-com/vendors/dibind-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dibind-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/dibind-com/security/dibind-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dibind-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dibind.com/
- group: docs
  title: ''
  type: Documentation
  url: https://dibind.com/daitk/
- group: docs
  title: ''
  type: APIReference
  url: https://daitk-tic.dibind.com/docs
- group: operate
  title: ''
  type: Support
  url: https://dibind.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://dibind.com/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dibind.com/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Dibblee
- group: company
  title: ''
  type: LinkedIn
  url: https://ca.linkedin.com/company/dibblee-industries
- group: agent
  title: ''
  type: LLMsTxt
  url: https://dibind.com/llms.txt
created: '2026-11-05'
description: Dibblee Industries (Les Industries Dibblee) is a Montréal, Québec-based Canadian SMB, in business since 1940 (NCAGE L0TZ1), supplying NATO-catalogued marine hardware, anchor and mining chain, deck fittings, aids to navigation and industrial equipment to Canada's defence, maritime and mining sectors. It also publishes DAITK, a family of AI business tools (DAITK-NSN FLIS/NSN research desk, DAITK-TIC Canadian total import cost, DAITK-Accounting, DAITK-GC, DAITK-Transport) delivered through a web app, AI assistants, a Model Context Protocol (MCP) server and a REST API, plus machine-readable JSON indexes of its catalogue and the DLA FLIS code dictionary.
image: https://dibind.com/images/og-default.jpg
json_schemas:
- name: DutyAnswer
  property_count: 15
  slug: dibind-com-duty-answer
- name: Measure
  property_count: 7
  slug: dibind-com-measure
- name: Status
  property_count: 5
  slug: dibind-com-status
- name: TariffRecord
  property_count: 5
  slug: dibind-com-tariff-record
jsonld:
- class_count: 9
  name: Dibind Com Context
  property_count: 48
  slug: dibind-com-context
layout: provider
mcp_servers:
- description: Official remote MCP server (Streamable HTTP) operated by Dibblee Industries for DAITK-TIC, the Canadian total import cost tool. Advertised in the provider's own llms.txt files. initialize and tools/li
  name: DAITK Total Import Cost MCP Server
  slug: daitk-total-import-cost-mcp-server
modified: '2026-11-05'
name: Dibblee Industries
nav: Providers
network: true
overview: 'Dibblee Industries publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Duty API, Reference API, Status API, and 1 more. Tagged areas include Company, Defence, Supply Chain, Marine Hardware, and NATO.


  The Dibblee Industries catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Dibblee Industries'' developer surface includes authentication, documentation, API reference, support, engineering blog, and 27 more developer resources.'
plans:
- name: Dibind Com Plans Pricing
  plan_count: 2
  slug: dibind-com-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 1
  name: Dibind Com Rate Limits
  slug: dibind-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 83
  extends:
  - spectral:oas
  name: Dibblee Industries API Rules
  rule_count: 42
  severity_counts:
    error: 40
    hint: 0
    info: 1
    warn: 1
  slug: dibind-com-rules
score:
  band: developing
  composite: 45.9
  coverage:
    artifact_dirs: 27
    catalog_earned: 78.8
    catalog_earned_first_party: 16.0
    catalog_gap: 36.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 35.6
    contract_quality: 58.1
    developer_ergonomics: 37.5
    discoverability: 71.7
    operational_transparency: 42.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Dibind Com Authentication
  slug: dibind-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Dibind Com Domain Security
  slug: dibind-com-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 2
skills:
- name: estimate-canadian-import-duty
  slug: dibind-com-estimate-canadian-import-duty
- name: monitor-trade-measure-changes
  slug: dibind-com-monitor-trade-measure-changes
slug: dibind-com
tags:
- Company
- Defence
- Supply Chain
- Marine Hardware
- NATO
- Logistics
- Artificial Intelligence
- MCP
- Canada
website: https://dibind.com/
---
