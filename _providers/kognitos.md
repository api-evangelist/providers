---
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
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.8
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 30
  human_in_the_loop: 1
  name: Kognitos Agentic Access
  operation_count: 102
  slug: kognitos-agentic-access
  summary_line: 102 operations · 30 acting · 1 human-in-the-loop
api_count: 2
apis:
- description: 'The Kognitos MCP Server lets AI assistants (Claude Desktop, Claude Code, Claude.ai and other Model Context Protocol clients) list automations, start runs, inspect exceptions and manage schedules in a '
  name: Kognitos MCP Server
  slug: kognitos-mcp-server
- baseURL: https://app.us-1.kognitos.com/api/v1
  baseurl_source: declared
  description: Query dashboards, automation estimates, insights, and metrics.
  name: Kognitos Analytics API
  slug: kognitos-analytics-api
- baseURL: https://app.us-1.kognitos.com/api/v1
  baseurl_source: declared
  description: Create and configure automations, revisions, schedules, triggers, and connections.
  name: Kognitos Automations API
  slug: kognitos-automations-api
- baseURL: https://app.us-1.kognitos.com/api/v1
  baseurl_source: declared
  description: Browse and search books, concepts, procedures, connections, and triggers.
  name: Kognitos Books API
  slug: kognitos-books-api
- baseURL: https://app.us-1.kognitos.com/api/v1
  baseurl_source: declared
  description: Track exceptions, view analytics, manage agent events, and access troubleshooting guides.
  name: Kognitos Exceptions API
  slug: kognitos-exceptions-api
- baseURL: https://app.us-1.kognitos.com/api/v1
  baseurl_source: declared
  description: Upload, download, and manage files.
  name: Kognitos Files API
  slug: kognitos-files-api
- baseURL: https://app.us-1.kognitos.com/api/v1
  baseurl_source: declared
  description: Manage organizations, users, roles, invitations, and preferences.
  name: Kognitos Organizations API
  slug: kognitos-organizations-api
- baseURL: https://app.us-1.kognitos.com/api/v1
  baseurl_source: declared
  description: Execute automations and manage run lifecycle — start, pause, continue, and view events.
  name: Kognitos Runs API
  slug: kognitos-runs-api
- baseURL: https://app.us-1.kognitos.com/api/v1
  baseurl_source: declared
  description: Manage workspaces, members, roles, invitations, and preferences.
  name: Kognitos Workspaces API
  slug: kognitos-workspaces-api
artifact_total: 25
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/kognitos/refs/heads/main/agentic-access/kognitos-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/kognitos-agentic-access.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/kognitos/refs/heads/main/plans/kognitos-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/kognitos-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kognitos/refs/heads/main/rules/kognitos-rules.yml
  title: ''
  type: Spectral
  url: rules/kognitos-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kognitos/refs/heads/main/rules/kognitos-openapi-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/kognitos-openapi-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kognitos/refs/heads/main/json-ld/kognitos-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/kognitos-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kognitos/refs/heads/main/vocabulary/kognitos-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/kognitos-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/kognitos/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kognitos/refs/heads/main/data-model/kognitos-data-model.yml
  title: ''
  type: DataModel
  url: data-model/kognitos-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kognitos/refs/heads/main/conventions/kognitos-conventions.yml
  title: ''
  type: Conventions
  url: conventions/kognitos-conventions.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/kognitos/refs/heads/main/sandbox/kognitos-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/kognitos-sandbox.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.kognitos.com/
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/kognitos/refs/heads/main/lifecycle/kognitos-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/kognitos-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kognitos/refs/heads/main/lifecycle/kognitos-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/kognitos-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kognitos/refs/heads/main/errors/kognitos-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/kognitos-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kognitos/refs/heads/main/conformance/kognitos-conformance.yml
  title: ''
  type: Conformance
  url: conformance/kognitos-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/kognitos/refs/heads/main/overlays/kognitos-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/kognitos-openapi-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/kognitos/refs/heads/main/llms/kognitos-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/kognitos-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/kognitos/refs/heads/main/mcp/kognitos-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/kognitos-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/kognitos/refs/heads/main/mcp/kognitos-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/kognitos-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/kognitos/refs/heads/main/well-known/kognitos-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/kognitos-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/kognitos/refs/heads/main/hosts/kognitos-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kognitos-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/kognitos/refs/heads/main/vendors/kognitos-vendors.yml
  title: ''
  type: Vendors
  url: vendors/kognitos-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/kognitos/refs/heads/main/packages/kognitos-packages.yml
  title: ''
  type: SDKs
  url: packages/kognitos-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/kognitos/refs/heads/main/packages/kognitos-packages.yml
  title: ''
  type: Packages
  url: packages/kognitos-packages.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.kognitos.com/news/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/kognitos/refs/heads/main/authentication/kognitos-authentication.yml
  title: ''
  type: Authentication
  url: authentication/kognitos-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/kognitos/refs/heads/main/security/kognitos-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/kognitos-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/kognitos/refs/heads/main/security/kognitos-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kognitos-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.kognitos.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.kognitos.com/developer/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.kognitos.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.kognitos.com/guides/api-reference/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.kognitos.com/guides/getting-started/quick-start
- group: agent
  title: ''
  type: LLMsTxt
  url: https://docs.kognitos.com/llms.txt
- group: start
  title: ''
  type: Login
  url: https://app.us-1.kognitos.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.kognitos.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.kognitos.com/
- group: company
  title: ''
  type: Blog
  url: https://www.kognitos.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.kognitos.com/contact-us/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kognitos
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kognitos.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kognitos.com/privacy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kognitos/
- group: other
  title: ''
  type: X
  url: https://x.com/kognitos_inc
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@KognitosAutomation
- group: other
  title: ''
  type: EquityZen
  url: https://equityzen.com/company/kognitos
- group: design
  title: ''
  type: SpectralRules
  url: https://github.com/kognitos/openapi/blob/edf6b8b8988fd6aff8938039aaa1e96c2ec88b6b/.spectral.yaml
created: '2026-10-09'
description: Kognitos is a neurosymbolic agentic AI platform that automates finance, accounts payable, healthcare, and IT workflows in plain English ("English as code"), positioned as deterministic agentic AI for the enterprise with zero hallucinations and full audit compliance. The platform runs on AWS, offers integrations with SAP, Oracle Cloud ERP, Microsoft Dynamics 365 and Workday, and exposes a REST API (base https://app.us-1.kognitos.com/api/v1, Bearer personal access tokens) for managing organizations, workspaces, automations, runs, books, files, exceptions and analytics.
image: https://www.kognitos.com/img/kognitos-og.png?v=cee38495
json_schemas:
- name: apiHttpBody
  property_count: 3
  slug: kognitos-api-http-body
- name: v1Automation
  property_count: 25
  slug: kognitos-v1-automation
- name: v1Exception
  property_count: 16
  slug: kognitos-v1-exception
- name: A troubleshooting guide entry for an automation
  property_count: 15
  slug: kognitos-v1-guide-entry
- name: v1ListRunEventsResponse
  property_count: 2
  slug: kognitos-v1-list-run-events-response
- name: v1Run
  property_count: 10
  slug: kognitos-v1-run
jsonld:
- class_count: 120
  name: Kognitos Context
  property_count: 211
  slug: kognitos-context
layout: provider
mcp_servers:
- description: Official hosted Kognitos MCP server. Lets MCP clients (Claude Desktop, Claude Code, Claude.ai, ChatGPT and others) list automations, start runs, inspect exceptions and manage schedules in a Kognitos w
  name: Kognitos MCP Server
  slug: kognitos-mcp-server
modified: '2026-10-09'
name: Kognitos
nav: Providers
network: true
overview: 'Kognitos publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Analytics API, Automations API, Books API, and 6 more. Tagged areas include Company, AI Agents, Automation, Workflow Automation, and Finance Automation.


  The Kognitos catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Kognitos'' developer surface includes sandbox, authentication, documentation, API reference, getting-started guide, engineering blog, support, and 40 more developer resources.'
plans:
- name: Kognitos Plans Pricing
  plan_count: 2
  slug: kognitos-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Kognitos Rate Limits
  slug: kognitos-rate-limits
rules:
- authorship: provider
  effective_rule_count: 41
  extends:
  - spectral:oas
  name: Kognitos — openapi rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: kognitos-openapi-spectral-rules
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Kognitos API Rules
  rule_count: 14
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 3
  slug: kognitos-rules
score:
  band: strong
  composite: 61.0
  coverage:
    artifact_dirs: 29
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.2
  facets:
    access_clarity: 71.1
    contract_governance: 35.6
    contract_quality: 60.0
    developer_ergonomics: 73.2
    discoverability: 76.7
    operational_transparency: 28.9
  previous_composite: 66.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/kognitos/refs/heads/main/screenshots/kognitos-2026-10-11T190428.png
security:
- kind: authentication
  name: Kognitos Authentication
  slug: kognitos-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Kognitos Domain Security
  slug: kognitos-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Kognitos Trust Center
  slug: kognitos-trust-center
  summary_line: SOC 2, ISO 27001
slug: kognitos
tags:
- Company
- AI Agents
- Automation
- Workflow Automation
- Finance Automation
- Accounts Payable
- Neuro-Symbolic AI
- Enterprise
website: https://www.kognitos.com
---
