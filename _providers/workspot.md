---
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
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.4
  scored_at: '2026-09-04'
api_count: 2
apis:
- baseURL: https://api.workspot.com
  baseurl_source: declared
  description: REST API for Workspot Control, the SaaS management plane for Workspot Cloud PCs. 105 operations across 85 paths for IT Service Management (ITSM), automation and scripting tools — provisioning and life
  name: Workspot Control REST API
  slug: control
- description: HMAC-SHA256 authenticated REST API for fetching Workspot Control event data — end-user and administrator actions — into Splunk or any other SIEM. Uses a submit/poll/fetch flow with checkpoint-based in
  name: Workspot SIEM (Splunk) Events API
  slug: siem
artifact_total: 10
asyncapis:
- description: ''
  name: Workspot Siem Events
  slug: workspot-siem-events
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/workspot-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://www.workspot.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.workspot.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api.workspot.com/swagger-ui.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.workspot.com/docs/using-the-workspot-control-api
- group: operate
  title: ''
  type: Support
  url: https://www.workspot.com/support/
- group: company
  title: ''
  type: Blog
  url: https://www.workspot.com/blog/
- group: start
  title: ''
  type: SignUp
  url: https://www.workspot.com/company/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.workspot.com/legal/workspot-enterprise-subscription-agreement/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.workspot.com/legal/privacy-policy/
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.workspot.com/resources/trust-center/
- group: auth
  title: ''
  type: Compliance
  url: https://www.workspot.com/resources/trust-center/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.workspot.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/workspot-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/workspot-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/workspot-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/workspot-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/workspot-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/workspot-plans-pricing.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/workspot-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/workspot-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/workspot-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/workspot-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/workspot-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/workspot-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/workspot-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/workspot-packages.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://go.workspot.com/231025-Request-Product-Pricing
- group: other
  title: ''
  type: Events
  url: asyncapi/workspot-siem-events.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/workspot-control-overlay.yaml
- group: docs
  title: ''
  type: Swagger
  url: openapi/workspot-control-openapi-original.json
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/workspot-control-openapi.json
- group: commercial
  title: ''
  type: ServiceLevelAgreement
  url: https://www.workspot.com/legal/cloudslac/
created: '2026-09-04'
description: Workspot is a cloud-native virtual desktop infrastructure (VDI) and Cloud PC provider delivering Desktop-as-a-Service through its Workspot Control SaaS plane and the Workspot Desktop Control Fabric, a globally distributed architecture that provisions and manages Windows desktops and published applications across Microsoft Azure, Google Cloud and Amazon WorkSpaces Core. Workspot publishes a Workspot Control REST API for IT service management, automation and scripting tools — 105 operations covering desktop pools, desktops, users, groups, templates, application bundles, cloud app server pools, RD gateway clusters, licenses and usage reporting — plus a separate HMAC-authenticated SIEM/Splunk events API for streaming admin and end-user event data into security tooling. It serves regulated and design-heavy industries including finance, legal, healthcare, manufacturing, life sciences, construction, retail and education.
image: https://www.workspot.com/app/uploads/2024/10/cropped-workspot-secondary-logo-blue-192x192.png
layout: provider
mcp_servers:
- description: ''
  name: Workspot MCP Server
  slug: workspot-mcp-server
modified: '2026-09-04'
name: Workspot
nav: Providers
network: true
overview: 'Workspot publishes 1 API on the [APIs.io](https://apis.io/) network: Control REST API. Tagged areas include Virtual Desktop Infrastructure, Desktop as a Service, Cloud PC, End User Computing, and Cloud Infrastructure.


  The Workspot catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Workspot''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, changelog, and 27 more developer resources.'
plans:
- name: Workspot Plans Pricing
  plan_count: 0
  slug: workspot-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 2
  name: Workspot Rate Limits
  slug: workspot-rate-limits
score:
  band: developing
  composite: 49.9
  coverage:
    artifact_dirs: 20
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 48.1
    developer_ergonomics: 49.4
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 52.6
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
security:
- kind: authentication
  name: Workspot Authentication
  slug: workspot-authentication
  summary_line: oauth2/http/hmac · 3 schemes
- kind: domain-security
  name: Workspot Domain Security
  slug: workspot-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Workspot Vulnerability Disclosure
  slug: workspot-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Workspot Trust Center
  slug: workspot-trust-center
  summary_line: SOC 2 Type 2, GDPR
slug: workspot
tags:
- Virtual Desktop Infrastructure
- Desktop as a Service
- Cloud PC
- End User Computing
- Cloud Infrastructure
- Enterprise IT
- Workspace Management
- SaaS
website: https://www.workspot.com/
---
