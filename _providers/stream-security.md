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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.2
  scored_at: '2026-09-04'
api_count: 2
apis:
- baseURL: https://{app}.streamsec.io/openapi
  baseurl_source: declared
  description: REST API over the Stream Security CloudTwin. 34 operations across twelve resource groups - inventory, attack paths, config changes, threat detections, detection rules, posture security rules and viola
  name: Stream Security API
  slug: stream-security-api
- description: Hosted remote MCP server that lets an agent query the Stream Security CloudTwin in natural language - resource metadata, configuration changes, misconfigurations, external exposures, excessive privile
  name: Stream Security MCP Server
  slug: stream-security-mcp-server
artifact_total: 8
asyncapis:
- description: ''
  name: Stream Security Notifications Webhooks
  slug: stream-security-notifications-webhooks
common:
- group: auth
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
  title: ''
  type: LLMsTxt
  url: llms/stream-security-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/stream-security-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/stream-security-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/stream-security-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/stream-security-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/stream-security-plans-pricing.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/stream-security-authentication.yml
created: '2026-08-29'
description: Stream.Security (formerly Lightlytics) is a cloud detection and response (CDR) and real-time CNAPP vendor that builds a live model of a customer's cloud - its "CloudTwin" - by continuously ingesting configuration state and activity from AWS, Azure, GCP, Kubernetes, ECS and VMware vSphere, then correlating posture drift against runtime behaviour to expose exploitable attack paths, excessive privilege, external exposure and active threats. The platform combines cloud-native log ingestion (CloudTrail, VPC Flow Logs, Route53 DNS, ELB/ALB, WAF, Entra ID audit) with eBPF runtime agents on Kubernetes, ECS and standalone VMs, adds canary/trap decoy resources and auto-remediation, and exposes it all through a public REST API and an MCP server so security teams and agents can query inventory, detections, vulnerabilities, attack paths and posture violations programmatically.
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
overview: 'Stream.Security publishes 1 API on the [APIs.io](https://apis.io/) network: Stream Security API. Tagged areas include Company, Security, Cloud Security, Cloud Detection and Response, and CNAPP.


  The Stream.Security catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Stream.Security''s developer surface includes documentation, API reference, getting-started guide, engineering blog, signup flow, support, authentication, and 13 more developer resources.'
plans:
- name: Stream Security Plans Pricing
  plan_count: 0
  slug: stream-security-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Stream Security Rate Limits
  slug: stream-security-rate-limits
score:
  band: developing
  composite: 40.0
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 4.5
    contract_quality: 67.1
    developer_ergonomics: 39.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 10.5
  previous_composite: 40.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/stream-security/refs/heads/main/screenshots/stream-security-2026-09-02T161000.png
security:
- kind: authentication
  name: Stream Security Authentication
  slug: stream-security-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Stream Security Domain Security
  slug: stream-security-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
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
