---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.2
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Wallarm Agentic Access
  operation_count: 17
  slug: wallarm-agentic-access
  summary_line: 17 operations · 16 acting
api_count: 9
apis:
- description: Application and scope management
  name: Wallarm Applications API
  slug: wallarm-applications-api
- description: Attack and incident data management
  name: Wallarm Attacks API
  slug: wallarm-attacks-api
- description: Third-party integrations (SIEM, notifications, etc.)
  name: Wallarm Integrations API
  slug: wallarm-integrations-api
- description: IP allowlist, denylist, and graylist management
  name: Wallarm IP Lists API
  slug: wallarm-ip-lists-api
- description: Wallarm filter node management
  name: Wallarm Nodes API
  slug: wallarm-nodes-api
- description: Security rules and virtual patch management
  name: Wallarm Rules API
  slug: wallarm-rules-api
- description: Automated trigger and alert management
  name: Wallarm Triggers API
  slug: wallarm-triggers-api
- description: User account and authentication management
  name: Wallarm User API
  slug: wallarm-user-api
- description: Vulnerability detection and management
  name: Wallarm Vulnerabilities API
  slug: wallarm-vulnerabilities-api
artifact_total: 25
collections:
- collection_type: open
  name: Wallarm API
  slug: open-wallarm
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wallarm-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wallarm-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wallarm-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wallarm
- group: company
  title: ''
  type: Website
  url: https://www.wallarm.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.wallarm.com/
- group: docs
  title: ''
  type: Reference
  url: https://docs.wallarm.com/api/overview/
- group: build
  title: ''
  type: Examples
  url: https://docs.wallarm.com/api/request-examples/
- group: start
  title: ''
  type: Console
  url: https://apiconsole.us1.wallarm.com/
- group: start
  title: ''
  type: Console
  url: https://apiconsole.eu1.wallarm.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wallarm
- group: other
  title: ''
  type: OpenSource
  url: https://github.com/wallarm/api-firewall
- group: company
  title: ''
  type: Blog
  url: https://lab.wallarm.com/feed/
- group: build
  title: ''
  type: SDKs
  url: https://github.com/wallarm/wallarm-go
- group: other
  title: ''
  type: TerraformProvider
  url: https://github.com/wallarm/terraform-provider-wallarm
- group: other
  title: ''
  type: TerraformModule
  url: https://github.com/wallarm/terraform-aws-wallarm
- group: build
  title: ''
  type: SDKs
  url: https://github.com/wallarm/ingress
- group: other
  title: ''
  type: HelmChart
  url: https://github.com/wallarm/helm-charts
- group: build
  title: ''
  type: Tools
  url: https://github.com/wallarm/gotestwaf
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.wallarm.com/llms.txt
created: '2025-01-08'
description: Wallarm provides advanced API security and protection solutions for APIs, web applications, and microservices. The platform includes API discovery, real-time attack protection, vulnerability testing, and an open-source API Firewall that enforces OpenAPI specifications as a positive security model. Wallarm supports deployment on Kubernetes, cloud environments, and as an NGINX-based proxy.
examples:
- key_count: 2
  name: Wallarm Addiprule Example
  slug: wallarm-addIpRule-example
- key_count: 2
  name: Wallarm Listattacks Example
  slug: wallarm-listAttacks-example
- key_count: 2
  name: Wallarm Listvulnerabilities Example
  slug: wallarm-listVulnerabilities-example
finops:
- name: Wallarm Finops
  service_category: API
  slug: wallarm-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wallarm.png
json_schemas:
- name: Wallarm Attack
  property_count: 10
  slug: wallarm-attack
- name: Wallarm Vulnerability
  property_count: 11
  slug: wallarm-vulnerability
json_structures:
- name: Wallarm Attack Structure
  property_count: 0
  slug: wallarm-attack-structure
jsonld:
- class_count: 9
  name: Wallarm Context
  property_count: 14
  slug: wallarm-context
layout: provider
modified: '2026-05-19'
name: Wallarm
nav: Providers
network: true
overview: 'Wallarm publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Applications API, Attacks API, Integrations API, and 6 more. Tagged areas include API Security, Security Testing, WAF, and Cybersecurity.


  The Wallarm catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Wallarm''s developer surface includes authentication, documentation, code examples, developer console, engineering blog, tooling, and 14 more developer resources.'
plans:
- name: Wallarm Plans Pricing
  plan_count: 3
  slug: wallarm-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 5
  name: Wallarm Rate Limits
  slug: wallarm-rate-limits
rules:
- name: Wallarm API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: wallarm-jsonschema-spectral-rules
- name: Wallarm API Rules
  rule_count: 12
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 7
  slug: wallarm-rules
score:
  band: developing
  composite: 53.9
  delta: -4.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 78.0
    developer_ergonomics: 41.3
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 57.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wallarm/refs/heads/main/screenshots/wallarm-2026-06-20T201213.png
security:
- kind: authentication
  name: Wallarm Authentication
  slug: wallarm-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Wallarm Domain Security
  slug: wallarm-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wallarm
tags:
- API Security
- Security Testing
- WAF
- Cybersecurity
website: https://www.wallarm.com/
---
