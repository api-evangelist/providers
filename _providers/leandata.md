---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.6
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Leandata Agentic Access
  operation_count: 16
  slug: leandata-agentic-access
  summary_line: 16 operations · 12 acting
api_count: 9
apis:
- description: <p>The availability endpoints return meeting configuration and open time slots used to render booking pages or refresh availability. Depending on the request context (routing, direct link, or reschedu
  name: LeanData 🗓️ Availability API
  slug: leandata-availability-api
- description: <p>This section outlines the endpoints used to retrieve scheduling data for building a custom calendaring experience. Both endpoints return the same structure of <strong>read-only</strong> information
  name: LeanData Legacy (still supported) API
  slug: leandata-legacy-still-supported-api
- description: The Matching API from LeanData — 1 operation(s) for matching.
  name: LeanData Matching API
  slug: leandata-matching-api
- description: '<p>Use these endpoints to finalize and book meetings after a timeslot has been selected.</p> <p>⚠️ <strong>Important:</strong> You <strong>must</strong> support both <code>POST /v1/meeting</code> and '
  name: LeanData 📆 Meetings > Create API
  slug: leandata-meetings-create-api
- description: The 📆 Meetings > Manage API from LeanData — 1 operation(s) for 📆 meetings > manage.
  name: LeanData 📆 Meetings > Manage API
  slug: leandata-meetings-manage-api
- description: The 📆 Meetings > Retrieve API from LeanData — 2 operation(s) for 📆 meetings > retrieve.
  name: LeanData 📆 Meetings > Retrieve API
  slug: leandata-meetings-retrieve-api
- description: '<p>This section describes the endpoints used to trigger 1x Routing for creating a custom orchestration experience, as well as to retrieve the status of the resulting job. When invoked, the 1x Routing '
  name: LeanData One Time Routing API
  slug: leandata-one-time-routing-api
- description: <p>This section outlines the endpoints used to retrieve Routing Graphs information for building a custom orchestration experience. The endpoint returns information such as trigger node names, the edge
  name: LeanData Retrieve Routing Graphs Information API
  slug: leandata-retrieve-routing-graphs-information-api
- description: The 🧠 Scheduling Inputs API from LeanData — 1 operation(s) for 🧠 scheduling inputs.
  name: LeanData 🧠 Scheduling Inputs API
  slug: leandata-scheduling-inputs-api
artifact_total: 32
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: LeanData BookIt 🗓️ Availability 🗓️ Availability 🗓️ Availability API
  slug: open-leandata-availability-api
- collection_type: open
  name: LeanData BookIt API
  slug: open-leandata-bookit
- collection_type: open
  name: LeanData Graph API
  slug: open-leandata-graph
- collection_type: open
  name: LeanData BookIt 🗓️ Availability 🗓️ Availability Legacy (still supported) API
  slug: open-leandata-legacy-still-supported-api
- collection_type: open
  name: LeanData BookIt 🗓️ Availability 🗓️ Availability Matching API
  slug: open-leandata-matching-api
- collection_type: open
  name: LeanData Matching and Round Robin API
  slug: open-leandata-matching
- collection_type: open
  name: LeanData BookIt 🗓️ Availability 🗓️ Availability 📆 Meetings > Create API
  slug: open-leandata-meetings-create-api
- collection_type: open
  name: LeanData BookIt 🗓️ Availability 🗓️ Availability 📆 Meetings > Manage API
  slug: open-leandata-meetings-manage-api
- collection_type: open
  name: LeanData BookIt 🗓️ Availability 🗓️ Availability 📆 Meetings > Retrieve API
  slug: open-leandata-meetings-retrieve-api
- collection_type: open
  name: LeanData BookIt 🗓️ Availability 🗓️ Availability One Time Routing API
  slug: open-leandata-one-time-routing-api
- collection_type: open
  name: LeanData BookIt 🗓️ Availability 🗓️ Availability Retrieve Routing Graphs Information API
  slug: open-leandata-retrieve-routing-graphs-information-api
- collection_type: open
  name: LeanData BookIt 🗓️ Availability 🗓️ Availability 🧠 Scheduling Inputs API
  slug: open-leandata-scheduling-inputs-api
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/leandata-trust-center.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/leandata-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/leandata-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.leandata.com
- group: start
  title: ''
  type: Portal
  url: https://docs.leandata.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.leandata.com
- group: docs
  title: ''
  type: Documentation
  url: https://api.leandatainc.com
- group: start
  title: ''
  type: SupportPortal
  url: https://leandatahelp.zendesk.com
- group: start
  title: ''
  type: SupportPortal
  url: https://support.leandata.com
- group: operate
  title: ''
  type: ChangeLog
  url: https://leandatahelp.zendesk.com/hc/en-us/sections/360002566353-Release-Notes
- group: commercial
  title: ''
  type: Pricing
  url: https://www.leandata.com/pricing/
- group: commercial
  title: ''
  type: Plans
  url: plans/leandata-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/leandata-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/leandata-finops.yml
- group: other
  title: ''
  type: Product
  url: https://www.leandata.com/platform/
- group: other
  title: ''
  type: Product
  url: https://www.leandata.com/platform/orchestration/
- group: other
  title: ''
  type: Product
  url: https://www.leandata.com/platform/bookit/
- group: other
  title: ''
  type: Product
  url: https://www.leandata.com/platform/buying-groups/
- group: other
  title: ''
  type: Customers
  url: https://www.leandata.com/customers/
- group: learn
  title: ''
  type: Training
  url: https://www.leandata.com/learning-center/
- group: learn
  title: ''
  type: Training
  url: https://www.leandata.com/certification/
- group: other
  title: ''
  type: Resources
  url: https://www.leandata.com/resources/
- group: company
  title: ''
  type: Blog
  url: https://www.leandata.com/blog/
- group: operate
  title: ''
  type: Forums
  url: https://www.opsstars.com/
- group: other
  title: ''
  type: AppExchange
  url: https://appexchange.salesforce.com/listingDetail?listingId=a0N3000000B4HCREA3
- group: other
  title: ''
  type: Company
  url: https://www.leandata.com/company/
- group: company
  title: ''
  type: Careers
  url: https://www.leandata.com/careers/
- group: operate
  title: ''
  type: Contact
  url: https://www.leandata.com/contact/
- group: company
  title: ''
  type: Newsroom
  url: https://www.leandata.com/press/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.leandata.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/leandata-trust-center.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.leandata.com/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.leandata.com/terms-of-service/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/leandatainc/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/leandatainc
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@leandatainc
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/leandata
- group: auth
  title: ''
  type: Authentication
  url: authentication/leandata-authentication.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.leandata.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.leandata.com
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.leandata.com
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/leandata/workspace/leandata-s-public-workspace
- group: operate
  title: ''
  type: Support
  url: https://support.leandata.com
- group: start
  title: ''
  type: Login
  url: https://login.leandata.com
- group: start
  title: ''
  type: SignUp
  url: https://www.leandata.com/demo-request/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/leandata-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/leandata-tool-crosswalk.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/leandata-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/leandata-llms.txt
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/leandata-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/leandata-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/leandata-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/leandata-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/leandata-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.leandata.com
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/leandata-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/leandata-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.leandata.com/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/leandata-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://trust.leandata.com/?itemUid=64c9680b-ef79-4c92-baa0-13b541954bef
- group: build
  title: ''
  type: Packages
  url: packages/leandata-packages.yml
- group: design
  title: ''
  type: Components
  url: components/leandata-components.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/leandata-availability-overlay.yaml
created: '2026-05-25'
description: LeanData is a Sunnyvale, California revenue orchestration platform built on the Salesforce ecosystem. The company is best known for inventing lead-to- account matching and lead routing for B2B revenue teams; its managed package on the Salesforce AppExchange has been deployed by more than 1,000 B2B companies including Uber, Palo Alto Networks, Shopify, Zoom, New Relic, Snowflake, and DocuSign. The current platform spans four product lines — Orchestration (lead/contact/account routing, deduplication, SLAs, signal workflows), BookIt (forms, handoff, and links-based scheduling), Buying Groups (multi-stakeholder pipeline and engagement), and Revenue Insights (reporting and analytics). LeanData exposes four developer APIs that wrap the platform's core capabilities — the Matching API (real-time lead / contact / account identification from external systems), the Round Robin API (advanced weighted distribution, working hours, and vacation-aware assignment), the BookIt API (scheduling
  inputs, availability, and meeting CRUD for custom UIs), and the Graph API (one-time routing and routing-graph metadata for custom orchestration). The Matching and Round Robin APIs are Salesforce-native and dispatched through the managed package's Apex REST endpoint at /services/apexrest/LeanData/LeanDataAPI, authenticated with the customer's own Salesforce OAuth 2.0 Connected App; BookIt and Graph are hosted at api.leandata.com behind AWS API Gateway and authenticated with a server-side API key in an X-Api-Key header. Since the Q2 2026 release LeanData also runs a hosted BookIt MCP server at https://mcp.leandata.com/mcp — currently labelled beta — which exposes BookIt scheduling and operational data to MCP-compatible AI clients under OAuth 2.1 with PKCE and dynamic client registration, with admin, user and partner scopes and tool visibility filtered by the caller's BookIt permission set. Developer documentation is published as a public Postman collection at docs.leandata.com. Commercial
  offerings are tiered across Standard, Advanced, Premium, and Enterprise editions of Orchestration plus BookIt scheduling products and Buying Groups, with implementation services billed separately.
finops:
- name: Leandata Finops
  service_category: Sales and Marketing Software
  slug: leandata-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/leandata.png
layout: provider
mcp_servers:
- description: ''
  name: LeanData BookIt MCP (remote, https://mcp.leandata.com/mcp)
  slug: leandata-bookit-mcp-remote-httpsmcpleandatacommcp
modified: '2026-08-13'
name: LeanData
nav: Providers
network: true
overview: 'LeanData publishes 9 APIs on the [APIs.io](https://apis.io/) network, including 🗓️ Availability API, Legacy (still supported) API, Matching API, and 6 more. Tagged areas include Revenue Operations, Lead Routing, Lead to Account Matching, Salesforce, and Sales Engagement.


  LeanData''s developer surface includes developer portal, documentation, changelog, pricing, training material, engineering blog, YouTube channel, and 57 more developer resources.'
plans:
- name: Leandata Plans Pricing
  plan_count: 8
  slug: leandata-plans-pricing
random_paper: 81
rate_limits:
- limit_count: 1
  name: Leandata Rate Limits
  slug: leandata-rate-limits
scopes:
- name: Leandata Scopes
  scope_count: 4
  slug: leandata-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: strong
  composite: 61.0
  delta: -6.2
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 16.7
    contract_quality: 45.9
    developer_ergonomics: 58.9
    discoverability: 92.6
    governance: 16.7
    operational_transparency: 50.0
  previous_composite: 67.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/leandata/refs/heads/main/screenshots/leandata-2026-06-20T184358.png
security:
- kind: authentication
  name: Leandata Authentication
  slug: leandata-authentication
  summary_line: apiKey/oauth2 · 4 schemes
- kind: domain-security
  name: Leandata Domain Security
  slug: leandata-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Leandata Vulnerability Disclosure
  slug: leandata-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Leandata Trust Center
  slug: leandata-trust-center
  summary_line: SOC 2 Type 2, GDPR, CCPA
slug: leandata
tags:
- Revenue Operations
- Lead Routing
- Lead to Account Matching
- Salesforce
- Sales Engagement
- Sales Productivity
- Marketing Operations
- Scheduling
- Meeting Booking
- Account Based Marketing
- Buying Groups
- Signal Orchestration
- Go to Market
- RevOps
- GTM
- CRM
- AppExchange
website: https://www.leandata.com
---
