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
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.1
  scored_at: '2026-09-16'
api_count: 2
apis:
- description: HMAC-SHA256 authenticated REST API for fetching Workspot Control event data — end-user and administrator actions — into Splunk or any other SIEM. Uses a submit/poll/fetch flow with checkpoint-based in
  name: Workspot SIEM (Splunk) Events API
  slug: siem
- baseURL: https://api.workspot.com
  baseurl_source: declared
  description: Workspot Control REST interface for administrators. See the descriptions below and <a href="https://docs.workspot.com/v1/docs/using-the-workspot-control-api">Using the Workspot Control API </a>for add
  name: Workspot AP Is API
  slug: workspot-apis-api
artifact_total: 10
asyncapis:
- description: ''
  name: Workspot Siem Events
  slug: workspot-siem-events
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/workspot/refs/heads/main/security/workspot-trust-center.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/workspot/refs/heads/main/changelog/workspot-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/workspot-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/workspot/refs/heads/main/lifecycle/workspot-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/workspot-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/workspot/refs/heads/main/authentication/workspot-authentication.yml
  title: ''
  type: Authentication
  url: authentication/workspot-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/workspot/refs/heads/main/conventions/workspot-conventions.yml
  title: ''
  type: Conventions
  url: conventions/workspot-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/workspot/refs/heads/main/rate-limits/workspot-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/workspot-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/workspot/refs/heads/main/plans/workspot-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/workspot-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/workspot/refs/heads/main/conformance/workspot-conformance.yml
  title: ''
  type: Conformance
  url: conformance/workspot-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/workspot/refs/heads/main/errors/workspot-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/workspot-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/workspot/refs/heads/main/data-model/workspot-data-model.yml
  title: ''
  type: DataModel
  url: data-model/workspot-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/workspot/refs/heads/main/well-known/workspot-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/workspot-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/workspot/refs/heads/main/mcp/workspot-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/workspot-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/workspot/refs/heads/main/llms/workspot-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/workspot-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/workspot/refs/heads/main/security/workspot-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/workspot-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/workspot/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/workspot/refs/heads/main/packages/workspot-packages.yml
  title: ''
  type: Packages
  url: packages/workspot-packages.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://go.workspot.com/231025-Request-Product-Pricing
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/workspot/refs/heads/main/asyncapi/workspot-siem-events.yml
  title: ''
  type: Events
  url: asyncapi/workspot-siem-events.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/workspot/refs/heads/main/overlays/workspot-control-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/workspot-control-overlay.yaml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/workspot/refs/heads/main/openapi/workspot-control-openapi-original.json
  title: ''
  type: Swagger
  url: openapi/workspot-control-openapi-original.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/workspot/refs/heads/main/openapi/_original/workspot-control-openapi.json
  title: ''
  type: OpenAPI
  url: openapi/_original/workspot-control-openapi.json
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
modified: '2026-09-16'
name: Workspot
nav: Providers
network: true
overview: 'Workspot publishes 1 API on the [APIs.io](https://apis.io/) network: AP Is API. Tagged areas include Virtual Desktop Infrastructure, Desktop as a Service, Cloud PC, End User Computing, and Cloud Infrastructure.


  The Workspot catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Workspot''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, changelog, and 27 more developer resources.'
plans:
- name: Workspot Plans Pricing
  plan_count: 0
  slug: workspot-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 2
  name: Workspot Rate Limits
  slug: workspot-rate-limits
score:
  band: developing
  composite: 53.3
  coverage:
    artifact_dirs: 21
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.8
  facets:
    access_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 61.7
    developer_ergonomics: 49.4
    discoverability: 75.9
    operational_transparency: 52.6
  previous_composite: 51.5
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
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
- Software-as-a-Service
website: https://www.workspot.com/
---
