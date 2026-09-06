---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.9
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://api-v2.7signal.com
  baseurl_source: declared
  description: The 7SIGNAL public REST API gateway. 215 operations across 32 tags covering authentication, users, roles, groups and organizations, API keys, Eyes (agents and sensors), locations, service areas, netwo
  name: 7SIGNAL Platform API (Gateway v2)
  slug: 7signal-platform-api-gateway-v2
- description: Remote, OAuth-protected Model Context Protocol server that lets Claude, ChatGPT, Microsoft Copilot and other agents query 7SIGNAL Wi-Fi telemetry and Eyeris AI analysis in natural language. The endpoi
  name: 7SIGNAL MCP Server
  slug: 7signal-mcp-server
artifact_total: 10
asyncapis:
- description: ''
  name: 7Signalsolutions Webhooks
  slug: 7signalsolutions-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/7signalsolutions-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://7signal.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api-v2.7signal.com/swagger-ui/index.html
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/7Signal/API-Examples/blob/develop/docs/README.md
- group: docs
  title: ''
  type: APIReference
  url: https://api-v2.7signal.com/swagger-ui/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/7Signal/API-Examples/blob/develop/docs/01-authentication.md
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/7Signal
- group: operate
  title: ''
  type: Support
  url: https://7signal.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://7signal.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://7signal.com/mobile-eye/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://7signal.com/schedule-a-demo/
- group: start
  title: ''
  type: Login
  url: https://start.7signal.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://7signal.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://7signal.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://7signal.com/status/
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/7signalsolutions-lifecycle.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/7signalsolutions-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/7signalsolutions-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/7signalsolutions-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/7signalsolutions-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/7signalsolutions-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/7signalsolutions-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/7signalsolutions-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/7signalsolutions-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/7signalsolutions-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-09-05'
description: 7SIGNAL is an enterprise wireless and wired network experience monitoring platform, headquartered in Independence, Ohio, that measures Wi-Fi and network performance from the client's point of view using vendor-agnostic Sapphire Eye hardware sensors and Mobile Eye software agents installed on endpoints. The 7SIGNAL Platform exposes a public REST API gateway at api-v2.7signal.com covering agents and sensors, locations, service areas, networks and access points, time-series KPIs, on-demand tests (ping, traceroute, iPerf3, speedtest, MOS, packet capture), RF scans, impact and experience scores, alert rules and incidents with email/webhook/ServiceNow delivery, and Eyeris AI analysis over Server-Sent Events. It also publishes a remote, OAuth-protected MCP server so Claude, ChatGPT and Copilot agents can query live Wi-Fi telemetry in natural language.
image: https://7signal.com/images/brand-assets/7signal-share.png
layout: provider
mcp_servers:
- description: ''
  name: 7SIGNAL MCP Server
  slug: 7signal-mcp-server
- description: ''
  name: 7SIGNAL MCP Server
  slug: 7signal-mcp-server-2
modified: '2026-09-05'
name: 7SIGNAL
nav: Providers
network: true
overview: '7SIGNAL publishes 1 API on the [APIs.io](https://apis.io/) network: Platform API (Gateway v2). Tagged areas include Wireless Network Monitoring, Wi-Fi Experience Monitoring, Digital Experience Monitoring, Network Performance Monitoring, and Network Observability.


  The 7SIGNAL catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  7SIGNAL''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 19 more developer resources.'
plans:
- name: 7Signalsolutions Plans Pricing
  plan_count: 0
  slug: 7signalsolutions-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: 7Signalsolutions Rate Limits
  slug: 7signalsolutions-rate-limits
scopes:
- name: 7Signalsolutions Scopes
  scope_count: 10
  slug: 7signalsolutions-scopes
  summary_line: 10 scopes · clientCredentials/authorization_code
score:
  band: strong
  composite: 54.8
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 65.1
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 50.0
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
  scored_at: '2026-09-05'
security:
- kind: authentication
  name: 7Signalsolutions Authentication
  slug: 7signalsolutions-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: 7Signalsolutions Domain Security
  slug: 7signalsolutions-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: 7signalsolutions
tags:
- Wireless Network Monitoring
- Wi-Fi Experience Monitoring
- Digital Experience Monitoring
- Network Performance Monitoring
- Network Observability
- AIOps
- IT Operations
- Endpoint Monitoring
- Time Series
- MCP
- agent-native
- Company
website: https://7signal.com/
---
