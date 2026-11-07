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
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 55.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://app.syftdata.com/api
  baseurl_source: declared
  description: The Export API from Syft Data — 1 operation(s) for export.
  name: Syft Data Export API
  slug: syft-data-export-api
- baseURL: https://app.syftdata.com/api
  baseurl_source: declared
  description: The Lookup API from Syft Data — 1 operation(s) for lookup.
  name: Syft Data Lookup API
  slug: syft-data-lookup-api
- baseURL: https://e2.sy-d.io
  baseurl_source: declared
  description: The ingest endpoint the Syft browser tracking tag, SDK and server-side callers post behavioural and custom events to. Documented only inside the developer guide — no reference page, no published paylo
  name: Syft Data Event Collection API
  slug: syft-data-events-api
artifact_total: 20
asyncapis:
- description: ''
  name: Syft Data Webhooks
  slug: syft-data-webhooks
collections:
- collection_type: open
  name: Syft Data Event Collection API
  slug: open-syft-data-events-api
- collection_type: open
  name: Syft Data Lookup & Export API
  slug: open-syft-data-export-api
- collection_type: open
  name: Syft Data & Export Lookup API
  slug: open-syft-data-lookup-api
common:
- group: other
  href: https://artifacts.apis.io/syft-data/capabilities/syft-data-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/syft-data-capability-edges.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.syftdata.com/feed
- group: other
  href: https://artifacts.apis.io/syft-data/overlays/syft-data-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/syft-data-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.syftdata.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.syftdata.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.syftdata.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.syftdata.com/implementation/lookup-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.syftdata.com/tutorial-basics/installation
- group: operate
  title: ''
  type: Support
  url: https://www.syftdata.com/support
- group: company
  title: ''
  type: Blog
  url: https://blog.syftdata.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/syftdata
- group: commercial
  title: ''
  type: Pricing
  url: https://www.syftdata.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.syftdata.com/auth/syft-signup
- group: start
  title: ''
  type: Login
  url: https://app.syftdata.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.syftdata.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.syftdata.com/privacy.html
- group: build
  href: https://artifacts.apis.io/syft-data/packages/syft-data-packages.yml
  title: ''
  type: SDKs
  url: packages/syft-data-packages.yml
- group: build
  href: https://artifacts.apis.io/syft-data/packages/syft-data-packages.yml
  title: ''
  type: Packages
  url: packages/syft-data-packages.yml
- group: build
  href: https://artifacts.apis.io/syft-data/cli/syft-data-cli.yml
  title: ''
  type: CLI
  url: cli/syft-data-cli.yml
- group: agent
  href: https://artifacts.apis.io/syft-data/mcp/syft-data-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/syft-data-mcp.yml
- group: agent
  href: https://artifacts.apis.io/syft-data/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/syft-data/well-known/syft-data-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/syft-data-well-known.yml
- group: design
  href: https://artifacts.apis.io/syft-data/asyncapi/syft-data-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/syft-data-webhooks.yml
- group: design
  href: https://artifacts.apis.io/syft-data/lifecycle/syft-data-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/syft-data-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/syft-data/security/syft-data-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/syft-data-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/syft-data/llms/syft-data-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/syft-data-llms.txt
- group: build
  href: https://artifacts.apis.io/syft-data/mcp/syft-data-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/syft-data-tool-crosswalk.yml
- group: commercial
  href: https://artifacts.apis.io/syft-data/plans/syft-data-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/syft-data-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/syft-data/rate-limits/syft-data-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/syft-data-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/syft-data/components/syft-data-components.yml
  title: ''
  type: Components
  url: components/syft-data-components.yml
- group: auth
  href: https://artifacts.apis.io/syft-data/security/syft-data-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/syft-data-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/syft-data/security/syft-data-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/syft-data-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/syft-data/security/syft-data-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/syft-data-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/syft-data/security/syft-data-trust-center.yml
  title: ''
  type: Compliance
  url: security/syft-data-trust-center.yml
- group: design
  href: https://artifacts.apis.io/syft-data/conformance/syft-data-conformance.yml
  title: ''
  type: Conformance
  url: conformance/syft-data-conformance.yml
- group: commercial
  title: ''
  type: DataProcessingAgreement
  url: https://www.syftdata.com/dpa
created: '2026-07-17'
description: Syft Data, Inc. is a B2B lead-intelligence platform that identifies and qualifies high-intent prospects from inbound website traffic and LinkedIn engagement. Its tracking pixel reveals anonymous visitors, enriches contacts, scores them against an Ideal Customer Profile, and triggers multi-channel outreach ("motions") into CRM, email, LinkedIn, and ad platforms. For developers Syft ships a schema-driven analytics SDK and CLI (npm @syftdata/*), a server-side Lookup and Export REST API secured with sk_live_ keys, outbound webhooks, and an official hosted MCP server so AI agents can query visitor data and build automations from chat.
finops:
- has_sources: true
  method: derived
  name: Syft Data Finops
  primary_unit: subscription
  service_category: ''
  slug: syft-data-finops
  template: false
image: https://www.syftdata.com/logo_180.png
layout: provider
mcp_servers:
- description: Official hosted MCP (Model Context Protocol) server that lets AI assistants query Syft visitor data, enqueue leads into motions, and build GTM automations from chat. Available on Pro plans.
  name: Syft MCP Server
  slug: syft-mcp-server
modified: '2026-10-06'
name: Syft Data
nav: Providers
network: true
overview: 'Syft Data publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Export API, Lookup API, and Event Collection API. Tagged areas include Company, Lead Intelligence, Intent Data, Website Visitor Identification, and Sales Intelligence.


  The Syft Data catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Syft Data''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 29 more developer resources.'
plans:
- name: Syft Data Plans Pricing
  plan_count: 3
  slug: syft-data-plans-pricing
- name: Syft Data Price Estimates
  plan_count: 0
  slug: syft-data-price-estimates
random_paper: 21
rate_limits:
- limit_count: 0
  name: Syft Data Rate Limits
  slug: syft-data-rate-limits
rules:
- authorship: generated
  effective_rule_count: 97
  extends:
  - spectral:oas
  name: Syft Data API Rules
  rule_count: 56
  severity_counts:
    error: 54
    hint: 0
    info: 1
    warn: 1
  slug: syft-data-rules
scopes:
- name: Syft Data Scopes
  scope_count: 4
  slug: syft-data-scopes
  summary_line: 4 scopes
score:
  band: strong
  composite: 65.3
  coverage:
    artifact_dirs: 33
    catalog_earned: 65.5
    catalog_earned_first_party: 12.0
    catalog_gap: 49.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 64.4
    developer_ergonomics: 64.9
    discoverability: 75.0
    operational_transparency: 21.1
  previous_composite: 65.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
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
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/syft-data/syft-data-2026-08-17T082227.png
security:
- kind: authentication
  name: Syft Data Authentication
  slug: syft-data-authentication
  summary_line: 5 schemes
- kind: domain-security
  name: Syft Data Domain Security
  slug: syft-data-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Syft Data Vulnerability Disclosure
  slug: syft-data-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Syft Data Trust Center
  slug: syft-data-trust-center
  summary_line: SOC 2 Type I, SOC 2 Type II, Penetration Testing, ISO 27001
skill_count: 2
skills:
- name: syft-data-export-motion-results
  slug: syft-data-export-motion-results
- name: syft-data-lookup-visitor-intelligence
  slug: syft-data-lookup-visitor-intelligence
slug: syft-data
tags:
- Company
- Lead Intelligence
- Intent Data
- Website Visitor Identification
- Sales Intelligence
- Go-To-Market
- Analytics
- MCP
website: https://www.syftdata.com/
---
