---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
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
    event_surface_described: derived
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Hosted remote MCP server that lets an agent query the Stream Security CloudTwin in natural language - resource metadata, configuration changes, misconfigurations, external exposures, excessive privile
  name: Stream Security MCP Server
  slug: stream-security-mcp-server
- baseURL: https://{app}.streamsec.io/openapi
  baseurl_source: declared
  description: The Attack Paths API from Stream.Security — 3 operation(s) for attack paths.
  name: Stream.Security Attack Paths API
  slug: stream-security-attack-paths-api
- baseURL: https://{app}.streamsec.io/openapi
  baseurl_source: declared
  description: The Canaries API from Stream.Security — 1 operation(s) for canaries.
  name: Stream.Security Canaries API
  slug: stream-security-canaries-api
- baseURL: https://{app}.streamsec.io/openapi
  baseurl_source: declared
  description: The Config Changes API from Stream.Security — 2 operation(s) for config changes.
  name: Stream.Security Config Changes API
  slug: stream-security-config-changes-api
- baseURL: https://{app}.streamsec.io/openapi
  baseurl_source: declared
  description: The Detection Rules API from Stream.Security — 2 operation(s) for detection rules.
  name: Stream.Security Detection Rules API
  slug: stream-security-detection-rules-api
- baseURL: https://{app}.streamsec.io/openapi
  baseurl_source: declared
  description: The Integrations API from Stream.Security — 2 operation(s) for integrations.
  name: Stream.Security Integrations API
  slug: stream-security-integrations-api
- baseURL: https://{app}.streamsec.io/openapi
  baseurl_source: declared
  description: The Inventory API from Stream.Security — 5 operation(s) for inventory.
  name: Stream.Security Inventory API
  slug: stream-security-inventory-api
- baseURL: https://{app}.streamsec.io/openapi
  baseurl_source: declared
  description: The Network & Identity Logs API from Stream.Security — 3 operation(s) for network & identity logs.
  name: Stream.Security Network & Identity Logs API
  slug: stream-security-network-identity-logs-api
- baseURL: https://{app}.streamsec.io/openapi
  baseurl_source: declared
  description: The Notifications API from Stream.Security — 2 operation(s) for notifications.
  name: Stream.Security Notifications API
  slug: stream-security-notifications-api
- baseURL: https://{app}.streamsec.io/openapi
  baseurl_source: declared
  description: The Posture Security API from Stream.Security — 3 operation(s) for posture security.
  name: Stream.Security Posture Security API
  slug: stream-security-posture-security-api
- baseURL: https://{app}.streamsec.io/openapi
  baseurl_source: declared
  description: The Threat Detection API from Stream.Security — 4 operation(s) for threat detection.
  name: Stream.Security Threat Detection API
  slug: stream-security-threat-detection-api
- baseURL: https://{app}.streamsec.io/openapi
  baseurl_source: declared
  description: The Vulnerabilities API from Stream.Security — 3 operation(s) for vulnerabilities.
  name: Stream.Security Vulnerabilities API
  slug: stream-security-vulnerabilities-api
- baseURL: https://{app}.streamsec.io/openapi
  baseurl_source: declared
  description: The Workspaces API from Stream.Security — 1 operation(s) for workspaces.
  name: Stream.Security Workspaces API
  slug: stream-security-workspaces-api
artifact_total: 24
asyncapis:
- description: ''
  name: Stream Security Notifications Webhooks
  slug: stream-security-notifications-webhooks
common:
- group: operate
  href: https://artifacts.apis.io/stream-security/rate-limits/stream-security-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/stream-security-rate-limits.yml
- group: other
  href: https://artifacts.apis.io/stream-security/capabilities/stream-security-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/stream-security-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/stream-security/overlays/stream-security-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/stream-security-api-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/stream-security/security/stream-security-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/stream-security-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.stream.security/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.streamsec.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.streamsec.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.streamsec.io/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.streamsec.io/docs/onboarding
- group: company
  title: ''
  type: Blog
  url: https://www.stream.security/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lightlytics
- group: start
  title: ''
  type: SignUp
  url: https://app.streamsec.io/
- group: operate
  title: ''
  type: Support
  url: https://www.stream.security/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.stream.security/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.stream.security/privacy-policy
- group: agent
  href: https://artifacts.apis.io/stream-security/llms/stream-security-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/stream-security-llms.txt
- group: build
  href: https://artifacts.apis.io/stream-security/packages/stream-security-packages.yml
  title: ''
  type: Packages
  url: packages/stream-security-packages.yml
- group: design
  href: https://artifacts.apis.io/stream-security/conformance/stream-security-conformance.yml
  title: ''
  type: Conformance
  url: conformance/stream-security-conformance.yml
- group: auth
  href: https://artifacts.apis.io/stream-security/conformance/stream-security-conformance.yml
  title: ''
  type: Compliance
  url: conformance/stream-security-conformance.yml
- group: design
  href: https://artifacts.apis.io/stream-security/lifecycle/stream-security-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/stream-security-lifecycle.yml
- group: commercial
  href: https://artifacts.apis.io/stream-security/plans/stream-security-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/stream-security-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/stream-security/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/stream-security/authentication/stream-security-authentication.yml
  title: ''
  type: Authentication
  url: authentication/stream-security-authentication.yml
created: '2026-08-29'
description: Stream.Security (formerly Lightlytics) is a cloud detection and response (CDR) and real-time CNAPP vendor that builds a live model of a customer's cloud - its "CloudTwin" - by continuously ingesting configuration state and activity from AWS, Azure, GCP, Kubernetes, ECS and VMware vSphere, then correlating posture drift against runtime behaviour to expose exploitable attack paths, excessive privilege, external exposure and active threats. The platform combines cloud-native log ingestion (CloudTrail, VPC Flow Logs, Route53 DNS, ELB/ALB, WAF, Entra ID audit) with eBPF runtime agents on Kubernetes, ECS and standalone VMs, adds canary/trap decoy resources and auto-remediation, and exposes it all through a public REST API and an MCP server so security teams and agents can query inventory, detections, vulnerabilities, attack paths and posture violations programmatically.
finops:
- has_sources: true
  method: derived
  name: Stream Security Finops
  primary_unit: ''
  service_category: ''
  slug: stream-security-finops
  template: true
image: https://cdn.prod.website-files.com/5f05d585ae7f3b0c47bc77a4/67166fa0d1d0600f5c5d67e8_page-preview.png
layout: provider
mcp_servers:
- description: Lets an agent interact with Stream Security data in natural language - retrieving resource metadata, configuration changes, misconfigurations, external exposures, excessive privileges and access to cr
  name: Stream Security MCP Server
  slug: stream-security-mcp-server
modified: '2026-08-29'
name: Stream.Security
nav: Providers
network: true
overview: 'Stream.Security publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including Attack Paths API, Canaries API, Config Changes API, and 10 more. Tagged areas include Company, Security, Cloud Security, Cloud Detection and Response, and CNAPP.


  The Stream.Security catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Stream.Security''s developer surface includes documentation, API reference, getting-started guide, engineering blog, signup flow, support, authentication, and 16 more developer resources.'
plans:
- name: Stream Security Plans Pricing
  plan_count: 0
  slug: stream-security-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Stream Security Rate Limits
  slug: stream-security-rate-limits
rules:
- authorship: generated
  effective_rule_count: 102
  extends:
  - spectral:oas
  name: Stream.Security API Rules
  rule_count: 61
  severity_counts:
    error: 54
    hint: 0
    info: 1
    warn: 6
  slug: stream-security-rules
score:
  band: developing
  composite: 46.4
  coverage:
    artifact_dirs: 26
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 5.2
  facets:
    access_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 66.8
    developer_ergonomics: 58.9
    discoverability: 75.0
    operational_transparency: 10.5
  previous_composite: 41.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 12
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/stream-security/stream-security-2026-09-02T161000.png
security:
- kind: authentication
  name: Stream Security Authentication
  slug: stream-security-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Stream Security Domain Security
  slug: stream-security-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: stream-security-manage-notification-rules
  slug: stream-security-manage-notification-rules
- name: stream-security-prioritize-vulnerabilities
  slug: stream-security-prioritize-vulnerabilities
- name: stream-security-triage-detection
  slug: stream-security-triage-detection
slug: stream-security
tags:
- Company
- Security
- Cloud Security
- Cloud Detection and Response
- CNAPP
- Threat Detection
- Vulnerability Management
- Kubernetes
- Observability
- DevSecOps
- Artificial Intelligence
website: https://www.stream.security/
---
