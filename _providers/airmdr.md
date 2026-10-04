---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 45.8
  scored_at: '2026-10-03'
api_count: 4
apis:
- description: 'Hosted, unauthenticated Streamable-HTTP MCP server on the AirMDR documentation host (Mintlify-operated) exposing three tools: search the AirMDR documentation, run read-only queries against a virtual f'
  name: AirMDR Documentation MCP Server
  slug: airmdr-documentation-mcp-server
- baseURL: https://app.airmdr.com/airmdrapi
  baseurl_source: declared
  description: The AlertCatalog API from AirMDR — 8 operation(s) for alertcatalog.
  name: AirMDR Alert Catalog API
  slug: airmdr-alertcatalog-api
- baseURL: https://app.airmdr.com/airmdrapi
  baseurl_source: declared
  description: The Alerts API from AirMDR — 15 operation(s) for alerts.
  name: AirMDR Alerts API
  slug: airmdr-alerts-api
- baseURL: https://app.airmdr.com/airmdrapi
  baseurl_source: declared
  description: The AlertTypes API from AirMDR — 3 operation(s) for alerttypes.
  name: AirMDR Alert Types API
  slug: airmdr-alerttypes-api
- baseURL: https://app.airmdr.com/airmdrapi
  baseurl_source: declared
  description: The Case Manager API from AirMDR — 32 operation(s) for case manager.
  name: AirMDR Case Manager API
  slug: airmdr-case-manager-api
- baseURL: https://app.airmdr.com/airmdrapi
  baseurl_source: declared
  description: The Case Manager Internal API from AirMDR — 10 operation(s) for case manager internal.
  name: AirMDR Case Manager Internal API
  slug: airmdr-case-manager-internal-api
- baseURL: https://app.airmdr.com/airmdrapi
  baseurl_source: declared
  description: The Case Manager V2 API from AirMDR — 43 operation(s) for case manager v2.
  name: AirMDR Case Manager V2 API
  slug: airmdr-case-manager-v2-api
- baseURL: https://app.airmdr.com/airmdrapi
  baseurl_source: declared
  description: The CaseDecisionAutomation API from AirMDR — 4 operation(s) for casedecisionautomation.
  name: AirMDR Case Decision Automation API
  slug: airmdr-casedecisionautomation-api
- baseURL: https://app.airmdr.com/airmdrapi
  baseurl_source: declared
  description: The Dashboard API from AirMDR — 20 operation(s) for dashboard.
  name: AirMDR Dashboard API
  slug: airmdr-dashboard-api
- baseURL: https://app.airmdr.com/airmdrapi
  baseurl_source: declared
  description: The Internal API from AirMDR — 8 operation(s) for internal.
  name: AirMDR Internal API
  slug: airmdr-internal-api
- baseURL: https://app.airmdr.com/airmdrapi
  baseurl_source: declared
  description: The MitreTactics API from AirMDR — 1 operation(s) for mitretactics.
  name: AirMDR Mitre Tactics API
  slug: airmdr-mitretactics-api
- baseURL: https://app.airmdr.com/airmdrapi
  baseurl_source: declared
  description: Endpoints to manage organizations
  name: AirMDR Organization API
  slug: airmdr-organization-api
- baseURL: https://app.airmdr.com/airmdrapi
  baseurl_source: declared
  description: Endpoints to manage user password
  name: AirMDR Password API
  slug: airmdr-password-api
- baseURL: https://app.airmdr.com/airmdrapi
  baseurl_source: declared
  description: Endpoints to read system permissions
  name: AirMDR Permission API
  slug: airmdr-permission-api
- baseURL: https://app.airmdr.com/airmdrapi
  baseurl_source: declared
  description: The Ping API from AirMDR — 1 operation(s) for ping.
  name: AirMDR Ping API
  slug: airmdr-ping-api
- baseURL: https://app.airmdr.com/airmdrapi
  baseurl_source: declared
  description: The Query DSL API from AirMDR — 3 operation(s) for query dsl.
  name: AirMDR Query DSL API
  slug: airmdr-query-dsl-api
- baseURL: https://app.airmdr.com/airmdrapi
  baseurl_source: declared
  description: The Security Review API from AirMDR — 5 operation(s) for security review.
  name: AirMDR Security Review API
  slug: airmdr-security-review-api
- baseURL: https://app.airmdr.com/airmdrapi
  baseurl_source: declared
  description: Endpoints to manage sessions
  name: AirMDR Session API
  slug: airmdr-session-api
- baseURL: https://app.airmdr.com/airmdrapi
  baseurl_source: declared
  description: Endpoints to manage tokens
  name: AirMDR Token API
  slug: airmdr-token-api
- baseURL: https://app.airmdr.com/airmdrapi
  baseurl_source: declared
  description: The Trial API from AirMDR — 1 operation(s) for trial.
  name: AirMDR Trial API
  slug: airmdr-trial-api
- baseURL: https://app.airmdr.com/airmdrapi
  baseurl_source: declared
  description: Endpoints to manager users
  name: AirMDR User API
  slug: airmdr-user-api
- baseURL: https://app.airmdr.com/airmdrapi
  baseurl_source: declared
  description: Endpoints to manage user groups
  name: AirMDR User Group API
  slug: airmdr-user-group-api
- baseURL: https://app.airmdr.com/airmdrapi
  baseurl_source: declared
  description: The Webhooks API from AirMDR — 3 operation(s) for webhooks.
  name: AirMDR Webhooks API
  slug: airmdr-webhooks-api
artifact_total: 30
asyncapis:
- description: ''
  name: Airmdr Webhooks
  slug: airmdr-webhooks
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/airmdr/refs/heads/main/security/airmdr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/airmdr-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/airmdr/refs/heads/main/authentication/airmdr-authentication.yml
  title: ''
  type: Authentication
  url: authentication/airmdr-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://airmdr.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.airmdr.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.airmdr.com/essentials/Landingpage
- group: docs
  title: ''
  type: APIReference
  url: https://docs.airmdr.com/api-reference/apilandingpage
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.airmdr.com/api-reference/apitoken
- group: company
  title: ''
  type: Blog
  url: https://airmdr.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://airmdr.com/blog/rss.xml
- group: company
  title: ''
  type: Newsroom
  url: https://airmdr.com/newsroom
- group: other
  title: ''
  type: Leadership
  url: https://airmdr.com/about-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AirMDR
- group: commercial
  title: ''
  type: Pricing
  url: https://airmdr.com/pricing
- group: start
  title: ''
  type: Login
  url: https://app.airmdr.com/auth/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://airmdr.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://airmdr.com/contact-us
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.airmdr.com/changelog/changelog
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/airmdr/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/AirMDR_Company
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UC_qHwQAACG8K20-X3JaB-yA
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/airmdr/refs/heads/main/packages/airmdr-packages.yml
  title: ''
  type: Packages
  url: packages/airmdr-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/airmdr/refs/heads/main/well-known/airmdr-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/airmdr-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/airmdr/refs/heads/main/a2a/airmdr-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/airmdr-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/airmdr/refs/heads/main/mcp/airmdr-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/airmdr-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/airmdr/refs/heads/main/mcp/airmdr-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/airmdr-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/airmdr/refs/heads/main/llms/airmdr-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/airmdr-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://docs.airmdr.com/llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/airmdr/refs/heads/main/overlays/airmdr-case-manager-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/airmdr-case-manager-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/airmdr/refs/heads/main/overlays/airmdr-user-management-service-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/airmdr-user-management-service-overlay.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/airmdr/refs/heads/main/conformance/airmdr-conformance.yml
  title: ''
  type: Conformance
  url: conformance/airmdr-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/airmdr/refs/heads/main/errors/airmdr-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/airmdr-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/airmdr/refs/heads/main/lifecycle/airmdr-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/airmdr-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/airmdr/refs/heads/main/conventions/airmdr-conventions.yml
  title: ''
  type: Conventions
  url: conventions/airmdr-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/airmdr/refs/heads/main/data-model/airmdr-data-model.yml
  title: ''
  type: DataModel
  url: data-model/airmdr-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/airmdr/refs/heads/main/changelog/airmdr-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/airmdr-changelog.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/airmdr/refs/heads/main/plans/airmdr-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/airmdr-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/airmdr/refs/heads/main/rate-limits/airmdr-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/airmdr-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/airmdr/refs/heads/main/asyncapi/airmdr-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/airmdr-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/airmdr/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/airmdr/refs/heads/main/regulatory/airmdr-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/airmdr-regulatory-posture.yml
created: '2026-09-19'
description: AirMDR is an AI-native managed detection and response (MDR) provider whose virtual security analyst, Darryl, automates alert triage, investigation and response across endpoint, cloud, SaaS, identity, email and network tools. The platform ingests alerts from 200+ integrations, runs automated or AI-generated investigation playbooks, and produces documented cases; it is sold as a full-service MDR for small security teams, an AI SOC platform for MSSPs and enterprise SOCs, and a free plan with 100 alert investigations. Programmatic access is a REST API on app.airmdr.com (Case Manager and User Management services, documented in Redoc), authenticated with an API token sent as a Session cookie, plus a webhook endpoint for pushing alerts into the platform.
image: https://airmdr.com/hubfs/Favicon.png
layout: provider
mcp_servers:
- description: ''
  name: AirMDR documentation MCP
  slug: airmdr-documentation-mcp
- description: ''
  name: AirMDR MCP Server
  slug: airmdr-mcp-server
modified: '2026-09-19'
name: AirMDR
nav: Providers
network: true
overview: 'AirMDR publishes 23 APIs on the [APIs.io](https://apis.io/) network, including Alert Catalog API, Alerts API, Alert Types API, and 20 more. Tagged areas include Security, Managed Detection and Response, Security Operations, Alert Triage, and Incident Response.


  The AirMDR catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  AirMDR''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, pricing, support, and 33 more developer resources.'
plans:
- name: Airmdr Plans Pricing
  plan_count: 3
  slug: airmdr-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Airmdr Rate Limits
  slug: airmdr-rate-limits
score:
  band: strong
  composite: 55.1
  coverage:
    artifact_dirs: 22
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.2
  facets:
    access_clarity: 59.2
    contract_governance: 4.5
    contract_quality: 52.2
    developer_ergonomics: 59.5
    discoverability: 81.7
    operational_transparency: 26.3
  previous_composite: 54.9
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 22
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: true
    score: 61.1
security:
- kind: authentication
  name: Airmdr Authentication
  slug: airmdr-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Airmdr Domain Security
  slug: airmdr-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: airmdr
tags:
- Security
- Managed Detection and Response
- Security Operations
- Alert Triage
- Incident Response
- AI Agents
- SOC Automation
- Threat Detection
- MCP
- A2A
website: https://airmdr.com/
---
