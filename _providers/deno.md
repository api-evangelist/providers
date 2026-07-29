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
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 30
  human_in_the_loop: 1
  name: Deno Agentic Access
  operation_count: 61
  slug: deno-agentic-access
  summary_line: 61 operations · 30 acting · 1 human-in-the-loop
api_count: 11
apis:
- description: The Deno Runtime API is the built-in namespace of globals and modules available to all programs running on the Deno JavaScript and TypeScript runtime. It provides access to filesystem operations, netw
  name: Deno Runtime API
  slug: runtime-api
- description: Deno KV is a key-value database built directly into the Deno runtime and available as a globally distributed store on Deno Deploy. It is accessed via the Deno.Kv namespace and supports get, set, delet
  name: Deno KV API
  slug: kv-api
- description: The Deno Standard Library is a collection of audited TypeScript modules maintained by the Deno core team and published on JSR under the @std scope. It provides common utilities including HTTP server h
  name: Deno Standard Library
  slug: standard-library
- description: Create, list, retrieve, update, and delete applications. Apps are the top-level containers for deployable code on Deno Deploy v2.
  name: Deno Apps API
  slug: deno-apps-api
- description: Create, list, retrieve, redeploy, and delete deployments; access build and app logs
  name: Deno Deployments API
  slug: deno-deployments-api
- description: Register and manage custom domains with TLS certificate support
  name: Deno Domains API
  slug: deno-domains-api
- description: Create and manage Deno KV databases and backups
  name: Deno KV Databases API
  slug: deno-kv-databases-api
- description: Query or stream runtime application logs for apps
  name: Deno Logs API
  slug: deno-logs-api
- description: Retrieve organization details and analytics
  name: Deno Organizations API
  slug: deno-organizations-api
- description: Create, list, update, and delete Deploy projects
  name: Deno Projects API
  slug: deno-projects-api
- description: Deploy new revisions, track build progress, cancel builds, and delete revisions. Revisions are immutable snapshots of deployed code.
  name: Deno Revisions API
  slug: deno-revisions-api
artifact_total: 26
collections:
- collection_type: open
  name: Deno Deploy REST API
  slug: open-deno-deploy-rest-api
- collection_type: open
  name: Deno Deploy API v2
  slug: open-deno-deploy-v2-api
- collection_type: open
  name: Deno Subhosting API
  slug: open-deno-subhosting-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/deno-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/deno-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/deno-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/deno-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/deno
- group: company
  title: ''
  type: Website
  url: https://deno.com
- group: start
  title: ''
  type: Portal
  url: https://dash.deno.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.deno.com
- group: company
  title: ''
  type: Blog
  url: https://deno.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/denoland
- group: start
  title: ''
  type: Login
  url: https://dash.deno.com/signin
- group: design
  title: ''
  type: JSONLD
  url: json-ld/deno-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/deno-deployment-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/deno-kv-database-schema.json
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/deno-vocabulary.yml
- group: other
  title: ''
  type: Capabilities
  url: capabilities/deno-capabilities.yml
- group: design
  title: ''
  type: Rules
  url: rules/deno-rules.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.deno.com/llms.txt
created: '2026-03-21'
description: Deno is a modern JavaScript and TypeScript runtime built on V8 that emphasizes security, simplicity, and developer productivity. It provides a comprehensive developer platform including the Deno Deploy serverless edge network, a built-in key-value store, and a standard library of audited modules, all designed to run TypeScript natively without additional tooling.
finops:
- name: Deno Finops
  service_category: Edge Compute / Serverless Runtime
  slug: deno-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/deno.png
json_schemas:
- name: Deno Deployment
  property_count: 11
  slug: deno-deployment
- name: Deno KV Database
  property_count: 6
  slug: deno-kv-database
jsonld:
- class_count: 0
  name: Deno Context
  property_count: 9
  slug: deno-context
layout: provider
modified: '2026-05-19'
name: Deno
nav: Providers
network: true
overview: 'Deno publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Apps API, Deployments API, Domains API, and 5 more. Tagged areas include Deployment, Edge, JavaScript, Runtime, and Serverless.


  The Deno catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Deno''s developer surface includes authentication, developer portal, documentation, engineering blog, and 14 more developer resources.'
plans:
- name: Deno Plans Pricing
  plan_count: 4
  slug: deno-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 8
  name: Deno Rate Limits
  slug: deno-rate-limits
rules:
- name: Deno API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: deno-jsonschema-spectral-rules
- name: Deno API Rules
  rule_count: 5
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 3
  slug: deno-rules
score:
  band: developing
  composite: 54.9
  delta: -4.4
  facets:
    commercial_clarity: 52.6
    contract_quality: 71.2
    developer_ergonomics: 30.4
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 59.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/deno/refs/heads/main/screenshots/deno-2026-06-20T175911.png
security:
- kind: authentication
  name: Deno Authentication
  slug: deno-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Deno Domain Security
  slug: deno-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Deno Vulnerability Disclosure
  slug: deno-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: deno
tags:
- Deployment
- Edge
- JavaScript
- Runtime
- Serverless
- TypeScript
website: https://deno.com
---
