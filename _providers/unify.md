---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
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
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 60.0
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 38
  human_in_the_loop: 0
  name: Unify Agentic Access
  operation_count: 68
  slug: unify-agentic-access
  summary_line: 68 operations · 38 acting
api_count: 4
apis:
- baseURL: https://api.unifyintent.com/analytics/v1
  baseurl_source: declared
  description: Server-side event collection for the Unify Analytics API - identify, page and track events posted from a website or product with a public write key over HTTP Basic. 3 operation(s).
  name: Unify Analytics Events API
  slug: unify-events-api
- baseURL: https://api.unifygtm.com/data/v1
  baseurl_source: declared
  description: 'Asynchronous Bulk API export of collected analytics events: create a query job, poll its status, page the results, or cancel it. 5 operation(s).'
  name: Unify Event Query Jobs API
  slug: unify-event-query-jobs-api
- baseURL: https://api.unifygtm.com/data/v1
  baseurl_source: declared
  description: Create, read, update and delete the objects (tables) of the Unify data platform, covering both the standard company/person/user objects and custom objects. 5 operation(s).
  name: Unify Objects API
  slug: unify-objects-api
- baseURL: https://api.unifygtm.com/data/v1
  baseurl_source: declared
  description: Manage the attributes (fields) defined on a Unify object, including type, uniqueness and lifecycle. 5 operation(s).
  name: Unify Object Attributes API
  slug: unify-object-attributes-api
- baseURL: https://api.unifygtm.com/data/v1
  baseurl_source: declared
  description: Manage the allowed option values on select-style Unify object attributes. 5 operation(s).
  name: Unify Object Attribute Options API
  slug: unify-object-attribute-options-api
- baseURL: https://api.unifygtm.com/data/v1
  baseurl_source: declared
  description: Create, read, update, delete, upsert and find-unique the records of any Unify object, with a validation_mode dry-run for writes. 6 operation(s).
  name: Unify Object Records API
  slug: unify-object-records-api
- baseURL: https://api.unifygtm.com/data/v1
  baseurl_source: declared
  description: 'Asynchronous Bulk API export of object records: create a query job with structured filters, poll it, page the results, or cancel it. 5 operation(s).'
  name: Unify Object Record Query Jobs API
  slug: unify-object-record-query-jobs-api
- baseURL: https://api.unifygtm.com/sequences/v1
  baseurl_source: declared
  description: List, retrieve, pause, resume and delete Unify outbound sequences and read their ordered steps. 7 operation(s).
  name: Unify Sequences API
  slug: unify-sequences-api
- baseURL: https://api.unifygtm.com/sequences/v1
  baseurl_source: declared
  description: Enroll people in sequences and pause, resume, cancel, list and bulk-export those enrollments. 11 operation(s).
  name: Unify Sequence Enrollments API
  slug: unify-sequence-enrollments-api
- baseURL: https://api.unifygtm.com/sequences/v1
  baseurl_source: declared
  description: Asynchronous Bulk API export of executed sequence enrollment steps. 5 operation(s).
  name: Unify Sequence Enrollment Steps API
  slug: unify-sequence-enrollment-steps-api
- baseURL: https://api.unifygtm.com/tasks/v1
  baseurl_source: declared
  description: Create, read, update, complete, delete, list and bulk-export the outreach tasks - emails, calls, LinkedIn touches and manual action items - assigned to Unify users against a person. 11 operation(s).
  name: Unify Tasks API
  slug: unify-tasks-api
artifact_total: 32
asyncapis:
- description: ''
  name: Unify Webhooks
  slug: unify-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Unify Data Event Query Jobs API
  slug: open-unify-event-query-jobs-api
- collection_type: open
  name: Unify Analytics Events API
  slug: open-unify-events-api
- collection_type: open
  name: Unify Data Object Attribute Options API
  slug: open-unify-object-attribute-options-api
- collection_type: open
  name: Unify Data Object Attributes API
  slug: open-unify-object-attributes-api
- collection_type: open
  name: Unify Data Object Record Query Jobs API
  slug: open-unify-object-record-query-jobs-api
- collection_type: open
  name: Unify Data Object Records API
  slug: open-unify-object-records-api
- collection_type: open
  name: Unify Data Objects API
  slug: open-unify-objects-api
- collection_type: open
  name: Unify Sequences Sequence Enrollment Steps API
  slug: open-unify-sequence-enrollment-steps-api
- collection_type: open
  name: Unify Sequences Sequence Enrollments API
  slug: open-unify-sequence-enrollments-api
- collection_type: open
  name: Unify Sequences API
  slug: open-unify-sequences-api
- collection_type: open
  name: Unify Tasks API
  slug: open-unify-tasks-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/unify-analytics-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/unify-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/unify-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/unify-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/unify-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.unifygtm.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.unifygtm.com/developers/introduction
- group: docs
  title: ''
  type: Documentation
  url: https://docs.unifygtm.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.unifygtm.com/developers/api/data/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.unifygtm.com/getting-started/setup-guide
- group: company
  title: ''
  type: Blog
  url: https://www.unifygtm.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/unifygtm
- group: commercial
  title: ''
  type: Pricing
  url: https://www.unifygtm.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.unifygtm.com/?screen_hint=signup
- group: start
  title: ''
  type: Login
  url: https://auth.unifygtm.com/u/login/identifier
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.unifygtm.com/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.unifygtm.com/legal/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://trust.unifygtm.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/unify-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/unify-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/unify-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/unify-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/unify-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/unify-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/unify-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/unify-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/unify-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/unify-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/unify-webhooks.yml
- group: company
  title: ''
  type: XTwitter
  url: https://twitter.com/unifygtm
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/unifygtm/
- group: other
  title: ''
  type: AgentCard
  url: a2a/unify-a2a.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/unify-well-known.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/unify-scopes.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/unify-tool-crosswalk.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/unify-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/unify-rate-limits.yml
- group: design
  title: ''
  type: Components
  url: components/unify-components.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/unify-data-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/unify-sequences-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/unify-tasks-overlay.yaml
- group: operate
  title: ''
  type: Support
  url: mailto:support@unifygtm.com
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.unifygtm.com/changelog
created: '2026-07-17'
description: Unify is a B2B outbound and go-to-market platform that pairs AI agents with reps to find buyers already in market and reach them with the right message, combining 40+ data sources, 1.1B+ contacts and 65M+ companies with intent signals, automated Plays and multi-channel sequences. Founded in 2023 and backed by $52M+ from the OpenAI Startup Fund, Thrive Capital, Battery Ventures and Emergence Capital, Unify publishes four anonymous OpenAPI 3.0 documents covering 68 operations across Data, Sequences, Tasks and Analytics, official Python and TypeScript SDKs, browser intent clients, a hosted OAuth-protected MCP server exposing 71 tools, provider-published agent skills, and an A2A agent card.
image: https://raw.githubusercontent.com/unifygtm/agent-plugins/main/unify/assets/unify-logo-light.svg
layout: provider
mcp_servers:
- description: ''
  name: Unify MCP Server
  slug: unify-mcp-server
modified: '2026-08-13'
name: Unify
nav: Providers
network: true
overview: 'Unify publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Analytics Events API, Event Query Jobs API, Objects API, and 8 more. Tagged areas include Sales, Marketing, Go-To-Market, Outbound, and Intent Data.


  The Unify catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Unify''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, and 37 more developer resources.'
plans:
- name: Unify Plans Pricing
  plan_count: 4
  slug: unify-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 7
  name: Unify Rate Limits
  slug: unify-rate-limits
scopes:
- name: Unify Scopes
  scope_count: 14
  slug: unify-scopes
  summary_line: 14 scopes
score:
  band: strong
  composite: 64.3
  coverage:
    artifact_dirs: 25
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 85.5
    commercial_clarity: 85.5
    contract_governance: 18.2
    contract_quality: 60.1
    developer_ergonomics: 71.4
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 57.9
  previous_composite: 64.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: first-party
    skills: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/unify/refs/heads/main/screenshots/unify-2026-08-17T080432.png
security:
- kind: authentication
  name: Unify Authentication
  slug: unify-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Unify Domain Security
  slug: unify-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Unify Trust Center
  slug: unify-trust-center
  summary_line: SOC 2
slug: unify
tags:
- Sales
- Marketing
- Go-To-Market
- Outbound
- Intent Data
- AI Agents
- B2B
- Data Enrichment
- Sequences
- Analytics
- Task
- Bulk API
- MCP
- Agent Skills
- Webhook
website: https://www.unifygtm.com
---
