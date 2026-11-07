---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
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
  score: 28.6
  scored_at: '2026-11-06'
api_count: 3
apis:
- baseURL: https://striim.stoplight.io
  baseurl_source: declared
  description: The application API from Striim — 4 operation(s) for application.
  name: Striim Application API
  slug: striim-application-api
- baseURL: https://striim.stoplight.io
  baseurl_source: declared
  description: The applicationMetadata API from Striim — 2 operation(s) for applicationmetadata.
  name: Striim Application Metadata API
  slug: striim-applicationmetadata-api
- baseURL: https://striim.stoplight.io
  baseurl_source: declared
  description: The checkpoint API from Striim — 1 operation(s) for checkpoint.
  name: Striim Checkpoint API
  slug: striim-checkpoint-api
- baseURL: https://striim.stoplight.io
  baseurl_source: declared
  description: The monitoring API from Striim — 1 operation(s) for monitoring.
  name: Striim Monitoring API
  slug: striim-monitoring-api
- baseURL: https://striim.stoplight.io
  baseurl_source: declared
  description: The template API from Striim — 3 operation(s) for template.
  name: Striim Template API
  slug: striim-template-api
- baseURL: https://striim.stoplight.io
  baseurl_source: declared
  description: The tqlfiles API from Striim — 2 operation(s) for tqlfiles.
  name: Striim Tqlfiles API
  slug: striim-tqlfiles-api
- baseURL: https://striim.stoplight.io
  baseurl_source: declared
  description: The tungsten API from Striim — 1 operation(s) for tungsten.
  name: Striim Tungsten API
  slug: striim-tungsten-api
artifact_total: 18
common:
- group: other
  href: https://artifacts.apis.io/striim/overlays/striim-tql-files-5-4-0-2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/striim-tql-files-5-4-0-2-overlay.yaml
- group: other
  href: https://artifacts.apis.io/striim/overlays/striim-application-management-3-10-3-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/striim-application-management-3-10-3-overlay.yaml
- group: other
  href: https://artifacts.apis.io/striim/overlays/striim-application-management-3-10-1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/striim-application-management-3-10-1-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.striim.com/
- group: auth
  href: https://artifacts.apis.io/striim/authentication/striim-authentication.yml
  title: ''
  type: Authentication
  url: authentication/striim-authentication.yml
- group: auth
  href: https://artifacts.apis.io/striim/security/striim-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/striim-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.striim.com/feed/
- group: build
  href: https://artifacts.apis.io/striim/packages/striim-packages.yml
  title: ''
  type: Packages
  url: packages/striim-packages.yml
- group: agent
  href: https://artifacts.apis.io/striim/mcp/striim-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/striim-mcp.yml
- group: agent
  href: https://artifacts.apis.io/striim/llms/striim-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/striim-llms.txt
- group: design
  href: https://artifacts.apis.io/striim/lifecycle/striim-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/striim-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/striim/conformance/striim-conformance.yml
  title: ''
  type: Conformance
  url: conformance/striim-conformance.yml
- group: design
  href: https://artifacts.apis.io/striim/errors/striim-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/striim-problem-types.yml
- group: design
  href: https://artifacts.apis.io/striim/conventions/striim-conventions.yml
  title: ''
  type: Conventions
  url: conventions/striim-conventions.yml
- group: operate
  href: https://artifacts.apis.io/striim/changelog/striim-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/striim-changelog.yml
- group: design
  href: https://artifacts.apis.io/striim/data-model/striim-data-model.yml
  title: ''
  type: DataModel
  url: data-model/striim-data-model.yml
- group: commercial
  href: https://artifacts.apis.io/striim/plans/striim-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/striim-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/striim/rate-limits/striim-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/striim-rate-limits.yml
- group: start
  href: https://artifacts.apis.io/striim/sandbox/striim-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/striim-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/striim/security/striim-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/striim-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/striim/security/striim-trust-center.yml
  title: ''
  type: Compliance
  url: security/striim-trust-center.yml
- group: agent
  href: https://artifacts.apis.io/striim/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.striim.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.striim.com/eula/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.striim.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/striim
- group: operate
  title: ''
  type: Support
  url: https://www.striim.com/contact-us/
created: '2026-07-02'
description: Unified data integration and streaming platform offering change data capture (CDC), real-time streaming analytics, and data validation. Exposes a token-authenticated REST API (WActionStore queries, system health, Application Management) consumed against your own Striim instance or Striim Cloud service.
finops:
- has_sources: true
  method: derived
  name: Striim Finops
  primary_unit: ''
  service_category: ''
  slug: striim-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/striim.png
layout: provider
mcp_servers:
- description: Remote MCP server over HTTP.
  name: Striim MCP AgentLink
  slug: striim-mcp-agentlink
modified: '2026-09-03'
name: Striim
nav: Providers
network: true
overview: 'Striim publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Application API, Application Metadata API, Checkpoint API, and 4 more. Tagged areas include Data, Streaming, Change Data Capture, Real-Time, and Data Integration.


  The Striim catalog on APIs.io includes 1 Spectral governance ruleset.


  Striim''s developer surface includes authentication, engineering blog, changelog, sandbox, pricing, support, and 21 more developer resources.'
plans:
- name: Striim Plans Pricing
  plan_count: 4
  slug: striim-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Striim Rate Limits
  slug: striim-rate-limits
rules:
- authorship: generated
  effective_rule_count: 104
  extends:
  - spectral:oas
  name: Striim API Rules
  rule_count: 63
  severity_counts:
    error: 59
    hint: 0
    info: 1
    warn: 3
  slug: striim-rules
score:
  band: developing
  composite: 49.1
  coverage:
    artifact_dirs: 27
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 78.9
    contract_governance: 18.2
    contract_quality: 45.6
    developer_ergonomics: 44.6
    discoverability: 70.0
    operational_transparency: 18.4
  previous_composite: 49.1
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/striim/striim-2026-09-02T161015.png
security:
- kind: authentication
  name: Striim Authentication
  slug: striim-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Striim Domain Security
  slug: striim-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Striim Trust Center
  slug: striim-trust-center
  summary_line: SOC 2 Type II, HIPAA, GDPR, PCI DSS
skill_count: 3
skills:
- name: striim-deploy-and-run-application
  slug: striim-deploy-and-run-application
- name: striim-execute-console-commands
  slug: striim-execute-console-commands
- name: striim-manage-tql-files
  slug: striim-manage-tql-files
slug: striim
tags:
- Data
- Streaming
- Change Data Capture
- Real-Time
- Data Integration
- Streaming Analytics
website: https://www.striim.com/
---
