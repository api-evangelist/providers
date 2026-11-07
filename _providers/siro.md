---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
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
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 110
  human_in_the_loop: 1
  name: Siro Agentic Access
  operation_count: 213
  slug: siro-agentic-access
  summary_line: 213 operations · 110 acting · 1 human-in-the-loop
api_count: 5
apis:
- baseURL: https://functions.siro.ai/api-externalApi
  baseurl_source: declared
  description: The Audit API from Siro — 1 operation(s) for audit.
  name: Siro Audit API
  slug: siro-audit-api
- baseURL: https://functions.siro.ai/api-externalApi
  baseurl_source: declared
  description: The Core API from Siro — 23 operation(s) for core.
  name: Siro Core API
  slug: siro-core-api
- baseURL: https://functions.siro.ai/api-externalApi
  baseurl_source: declared
  description: The Folders API from Siro — 2 operation(s) for folders.
  name: Siro Folders API
  slug: siro-folders-api
- baseURL: https://functions.siro.ai/api-externalApi
  baseurl_source: declared
  description: The Integrations API from Siro — 21 operation(s) for integrations.
  name: Siro Integrations API
  slug: siro-integrations-api
- baseURL: https://functions.siro.ai/api-externalApi
  baseurl_source: declared
  description: The Agents API from Siro — 3 operation(s) for agents.
  name: Siro Agents API
  slug: siro-agents-api
- baseURL: https://functions.siro.ai/api-externalApi
  baseurl_source: declared
  description: The Billing Graph API from Siro — 10 operation(s) for billing graph.
  name: Siro Billing Graph API
  slug: siro-billing-graph-api
- baseURL: https://functions.siro.ai/api-externalApi
  baseurl_source: declared
  description: The Docs API from Siro — 1 operation(s) for docs.
  name: Siro Docs API
  slug: siro-docs-api
- baseURL: https://functions.siro.ai/api-externalApi
  baseurl_source: declared
  description: The Halftime API from Siro — 1 operation(s) for halftime.
  name: Siro Halftime API
  slug: siro-halftime-api
- baseURL: https://functions.siro.ai/api-externalApi
  baseurl_source: declared
  description: The Intercom API from Siro — 1 operation(s) for intercom.
  name: Siro Intercom API
  slug: siro-intercom-api
- baseURL: https://functions.siro.ai/api-externalApi
  baseurl_source: declared
  description: The Invoices API from Siro — 1 operation(s) for invoices.
  name: Siro Invoices API
  slug: siro-invoices-api
- baseURL: https://functions.siro.ai/api-externalApi
  baseurl_source: declared
  description: The Jobs API from Siro — 3 operation(s) for jobs.
  name: Siro Jobs API
  slug: siro-jobs-api
- baseURL: https://functions.siro.ai/api-externalApi
  baseurl_source: declared
  description: The Licenses API from Siro — 1 operation(s) for licenses.
  name: Siro Licenses API
  slug: siro-licenses-api
- baseURL: https://functions.siro.ai/api-externalApi
  baseurl_source: declared
  description: The Portal API from Siro — 1 operation(s) for portal.
  name: Siro Portal API
  slug: siro-portal-api
- baseURL: https://functions.siro.ai/api-externalApi
  baseurl_source: declared
  description: The Sessions API from Siro — 4 operation(s) for sessions.
  name: Siro Sessions API
  slug: siro-sessions-api
- baseURL: https://functions.siro.ai/api-externalApi
  baseurl_source: declared
  description: The Subscription API from Siro — 1 operation(s) for subscription.
  name: Siro Subscription API
  slug: siro-subscription-api
- baseURL: https://functions.siro.ai/api-externalApi
  baseurl_source: declared
  description: The Suggested Questions API from Siro — 1 operation(s) for suggested questions.
  name: Siro Suggested Questions API
  slug: siro-suggested-questions-api
artifact_total: 31
collections:
- collection_type: open
  name: Swagger Audit API
  slug: open-siro-audit-api
- collection_type: open
  name: Swagger Audit Core API
  slug: open-siro-core-api
- collection_type: open
  name: Swagger Audit Folders API
  slug: open-siro-folders-api
- collection_type: open
  name: Swagger Audit Integrations API
  slug: open-siro-integrations-api
common:
- group: other
  href: https://artifacts.apis.io/siro/capabilities/siro-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/siro-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/siro/overlays/siro-platform-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/siro-platform-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/siro/agentic-access/siro-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/siro-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/siro/security/siro-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/siro-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://siro.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.siro.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.siro.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.siro.ai/api-references/get-recordings
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.siro.ai/getting-started
- group: start
  title: ''
  type: Quickstart
  url: https://docs.siro.ai/phones-integration-getting-started
- group: operate
  title: ''
  type: Support
  url: https://docs.siro.ai/support
- group: company
  title: ''
  type: Blog
  url: https://www.siro.ai/insights
- group: start
  title: ''
  type: Login
  url: https://app.siro.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.siro.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.siro.ai/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.siro.ai/
- group: agent
  href: https://artifacts.apis.io/siro/llms/siro-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/siro-llms.txt
- group: auth
  href: https://artifacts.apis.io/siro/authentication/siro-authentication.yml
  title: ''
  type: Authentication
  url: authentication/siro-authentication.yml
- group: design
  href: https://artifacts.apis.io/siro/asyncapi/siro-webhooks.json
  title: ''
  type: Webhooks
  url: asyncapi/siro-webhooks.json
- group: operate
  href: https://artifacts.apis.io/siro/rate-limits/siro-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/siro-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/siro/errors/siro-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/siro-problem-types.yml
- group: design
  href: https://artifacts.apis.io/siro/conventions/siro-conventions.yml
  title: ''
  type: Conventions
  url: conventions/siro-conventions.yml
- group: design
  href: https://artifacts.apis.io/siro/lifecycle/siro-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/siro-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/siro/data-model/siro-data-model.yml
  title: ''
  type: DataModel
  url: data-model/siro-data-model.yml
- group: design
  href: https://artifacts.apis.io/siro/conformance/siro-conformance.yml
  title: ''
  type: Conformance
  url: conformance/siro-conformance.yml
- group: agent
  href: https://artifacts.apis.io/siro/mcp/siro-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/siro-mcp.yml
- group: agent
  href: https://artifacts.apis.io/siro/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/siro/overlays/siro-external-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/siro-external-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/siro/well-known/siro-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/siro-well-known.yml
- group: other
  href: https://artifacts.apis.io/siro/a2a/siro-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/siro-a2a.yml
- group: build
  href: https://artifacts.apis.io/siro/mcp/siro-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/siro-tool-crosswalk.yml
- group: build
  href: https://artifacts.apis.io/siro/packages/siro-packages.yml
  title: ''
  type: Packages
  url: packages/siro-packages.yml
- group: build
  href: https://artifacts.apis.io/siro/packages/siro-packages.yml
  title: ''
  type: SDKs
  url: packages/siro-packages.yml
- group: commercial
  href: https://artifacts.apis.io/siro/plans/siro-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/siro-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.siro.ai/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/siro-ai
- group: operate
  title: ''
  type: Contact
  url: mailto:support@siro.ai
created: '2026-07-17'
description: 'Siro is an AI sales coaching platform for in-person and field sales teams. Reps record their live sales conversations from the Siro mobile app, and Siro transcribes each conversation, surfaces coaching insights, generates scorecards and summaries, and extracts structured fields (budget, objections, decision makers, timelines) that are pushed back into the team''s CRM. Siro publishes a documented REST API and webhook surface that enables fully bidirectional, custom CRM integrations: syncing appointments/engagements, opportunities and accounts into Siro, matching recordings to CRM entities, and pulling recording details, summaries, entity extractions and coaching scorecards back out. The platform ships prebuilt integrations for Salesforce, HubSpot, Microsoft Dynamics, Pipedrive, Zoho, SalesRabbit, Leap SalesPro, Hatch, CompanyCam and a range of dealership DMS and home-services tools. Siro is backed by CRV and Index Ventures.'
finops:
- has_sources: true
  method: derived
  name: Siro Finops
  primary_unit: ''
  service_category: ''
  slug: siro-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/siro.png
layout: provider
modified: '2026-08-13'
name: Siro
nav: Providers
network: true
overview: 'Siro publishes 16 API contracts indexed on the [APIs.io](https://apis.io/) network, including Audit API, Core API, Folders API, and 13 more. Tagged areas include Company, Sales, Sales Coaching, Conversation Intelligence, and Field Sales.


  The Siro catalog on APIs.io includes 1 Spectral governance ruleset.


  Siro''s developer surface includes documentation, API reference, getting-started guide, quickstart, support, engineering blog, authentication, and 30 more developer resources.'
plans:
- name: Siro Plans Pricing
  plan_count: 0
  slug: siro-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 1
  name: Siro Rate Limits
  slug: siro-rate-limits
rules:
- authorship: generated
  effective_rule_count: 102
  extends:
  - spectral:oas
  name: Siro API Rules
  rule_count: 61
  severity_counts:
    error: 48
    hint: 0
    info: 5
    warn: 8
  slug: siro-rules
score:
  band: strong
  composite: 58.5
  coverage:
    artifact_dirs: 29
    catalog_earned: 52.5
    catalog_earned_first_party: 8.0
    catalog_gap: 62.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.2
  facets:
    access_clarity: 43.4
    contract_governance: 31.8
    contract_quality: 49.9
    developer_ergonomics: 71.4
    discoverability: 78.6
    operational_transparency: 31.6
  previous_composite: 58.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 12.5
      total: 16
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 61.1
screenshot: https://apis.io/screenshots/siro/siro-2026-08-17T081908.png
security:
- kind: authentication
  name: Siro Authentication
  slug: siro-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Siro Domain Security
  slug: siro-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Siro Trust Center
  slug: siro-trust-center
  summary_line: SOC 2 Type 1, SOC 2 Type 2
skill_count: 3
skills:
- name: Pull recording summaries and AI entity extractions
  slug: siro-pull-conversation-insights
- name: Siro
  slug: siro-siro-skill
- name: Sync CRM engagements and link Siro recordings
  slug: siro-sync-crm-and-link-recordings
slug: siro
tags:
- Company
- Sales
- Sales Coaching
- Conversation Intelligence
- Field Sales
- CRM
- Artificial Intelligence
- Speech-to-Text
- Webhook
- Integration
- A2A
website: https://siro.ai/
---
