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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.0
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Wallarm Agentic Access
  operation_count: 17
  slug: wallarm-agentic-access
  summary_line: 17 operations · 16 acting
api_count: 1
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
artifact_total: 35
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Wallarm Applications API
  slug: open-wallarm-applications-api
- collection_type: open
  name: Wallarm Applications Attacks API
  slug: open-wallarm-attacks-api
- collection_type: open
  name: Wallarm Applications Integrations API
  slug: open-wallarm-integrations-api
- collection_type: open
  name: Wallarm Applications IP Lists API
  slug: open-wallarm-ip-lists-api
- collection_type: open
  name: Wallarm Applications Nodes API
  slug: open-wallarm-nodes-api
- collection_type: open
  name: Wallarm Applications Rules API
  slug: open-wallarm-rules-api
- collection_type: open
  name: Wallarm Applications Triggers API
  slug: open-wallarm-triggers-api
- collection_type: open
  name: Wallarm Applications User API
  slug: open-wallarm-user-api
- collection_type: open
  name: Wallarm Applications Vulnerabilities API
  slug: open-wallarm-vulnerabilities-api
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
random_paper: 17
rate_limits:
- limit_count: 5
  name: Wallarm Rate Limits
  slug: wallarm-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Wallarm API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: wallarm-jsonschema-spectral-rules
- effective_rule_count: 53
  extends:
  - spectral:oas
  name: Wallarm API Rules
  rule_count: 12
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 7
  slug: wallarm-rules
score:
  band: developing
  composite: 42.7
  coverage:
    artifact_dirs: 17
    catalog_gap: 43.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 28.8
    contract_quality: 74.6
    developer_ergonomics: 45.2
    discoverability: 66.7
    governance: 28.8
    operational_transparency: 13.2
  previous_composite: 43.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.17.2
  scored_at: '2026-08-30'
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
