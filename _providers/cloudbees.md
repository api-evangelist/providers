---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
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
  score: 38.9
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 33
  human_in_the_loop: 0
  name: Cloudbees Agentic Access
  operation_count: 79
  slug: cloudbees-agentic-access
  summary_line: 79 operations · 33 acting
api_count: 3
apis:
- description: CloudBees CI is a hardened, enterprise distribution of Jenkins. The REST API is the Jenkins remote access API exposed at /api on every controller and on individual jobs, runs, queues and nodes. Caller
  name: CloudBees CI REST API
  slug: ci
- description: 'The CloudBees CD/RO (Continuous Delivery / Release Orchestration) REST API exposes resources for pipelines, releases, environments, applications, deployments, projects and resources. Operations cover '
  name: CloudBees CD/RO REST API
  slug: cd-ro
- description: The CloudBees Feature Management REST API (formerly Rollout) provides programmatic access to applications, environments, feature flags, experiments, target groups, audit logs, and users. Authenticatio
  name: CloudBees Feature Management REST API
  slug: feature-management
- baseURL: https://api.cloudbees.io
  baseurl_source: declared
  description: 'CloudBees Unify is the modern, opinionated software delivery platform that unifies CI, CD, feature management, analytics, and security into a single workflow. The CloudBees Unify Public API is served '
  name: CloudBees Unify Platform API
  slug: unify
- description: The CloudBees CD plugin for Jenkins exposes Jenkins pipeline steps that call CloudBees CD/RO REST endpoints — triggering pipelines, running releases, deploying applications, and pulling artifacts from
  name: CloudBees CD/RO Jenkins Plugin Steps
  slug: jenkins-plugin
- baseURL: https://example.cloudbees.com
  baseurl_source: declared
  description: The Computer API from CloudBees — 1 operation(s) for computer.
  name: CloudBees Computer API
  slug: cloudbees-computer-api
- baseURL: https://example.cloudbees.com
  baseurl_source: declared
  description: The CreateItem API from CloudBees — 1 operation(s) for createitem.
  name: CloudBees CreateItem API
  slug: cloudbees-createitem-api
- baseURL: https://example.cloudbees.com
  baseurl_source: declared
  description: The Job API from CloudBees — 7 operation(s) for job.
  name: CloudBees Job API
  slug: cloudbees-job-api
- baseURL: https://example.cloudbees.com
  baseurl_source: declared
  description: The Json API from CloudBees — 1 operation(s) for json.
  name: CloudBees Json API
  slug: cloudbees-json-api
- baseURL: https://example.cloudbees.com
  baseurl_source: declared
  description: The Python API from CloudBees — 1 operation(s) for python.
  name: CloudBees Python API
  slug: cloudbees-python-api
- baseURL: https://example.cloudbees.com
  baseurl_source: declared
  description: The Queue API from CloudBees — 1 operation(s) for queue.
  name: CloudBees Queue API
  slug: cloudbees-queue-api
- baseURL: https://example.cloudbees.com
  baseurl_source: declared
  description: The Xml API from CloudBees — 1 operation(s) for xml.
  name: CloudBees Xml API
  slug: cloudbees-xml-api
artifact_total: 34
asyncapis:
- description: ''
  name: Cloudbees Webhooks
  slug: cloudbees-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CloudBees CI REST API (Jenkins-compatible) Computer API
  slug: open-cloudbees-computer-api
- collection_type: open
  name: CloudBees CI REST API (Jenkins-compatible) Computer CreateItem API
  slug: open-cloudbees-createitem-api
- collection_type: open
  name: CloudBees CI REST API (Jenkins-compatible) Computer Job API
  slug: open-cloudbees-job-api
- collection_type: open
  name: CloudBees CI REST API (Jenkins-compatible) Computer Json API
  slug: open-cloudbees-json-api
- collection_type: open
  name: CloudBees CI REST API (Jenkins-compatible) Computer Python API
  slug: open-cloudbees-python-api
- collection_type: open
  name: CloudBees CI REST API (Jenkins-compatible) Computer Queue API
  slug: open-cloudbees-queue-api
- collection_type: open
  name: CloudBees CI REST API (Jenkins-compatible) Computer Xml API
  slug: open-cloudbees-xml-api
- collection_type: open
  name: CloudBees CI REST API (Jenkins-compatible)
  slug: open-cloudbees
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cloudbees-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/cloudbees-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cloudbees-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cloudbees-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cloudbees-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cloudbees
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cloudbees
- group: company
  title: ''
  type: Website
  url: https://www.cloudbees.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cloudbees.com/
- group: operate
  title: ''
  type: Support
  url: https://support.cloudbees.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cloudbees.com/legal/privacy-policy
- group: build
  title: ''
  type: Plugins
  url: https://docs.cloudbees.com/plugins/ci
- group: design
  title: ''
  type: JSONLD
  url: json-ld/cloudbees-context.jsonld
- group: design
  title: ''
  type: Spectral
  url: rules/cloudbees-rules.yml
- group: company
  title: ''
  type: Blog
  url: https://www.cloudbees.com/blog/rss.xml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cloudbees-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/cloudbees-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cloudbees-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cloudbees-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/cloudbees-security.txt
- group: build
  title: ''
  type: Packages
  url: packages/cloudbees-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/cloudbees-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://www.cloudbees.com/legal/security-policy
- group: auth
  title: ''
  type: Compliance
  url: https://www.cloudbees.com/company/trust-center
- group: design
  title: ''
  type: Conformance
  url: conformance/cloudbees-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cloudbees-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cloudbees-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloudbees.io/
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.cloudbees.com/docs/cloudbees-common/latest/maintenance-lifecycle
- group: design
  title: ''
  type: Conventions
  url: conventions/cloudbees-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/cloudbees-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.cloudbees.com/docs/cloudbees-unify-changelog/latest/
- group: build
  title: ''
  type: CLI
  url: cli/cloudbees-cli.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/cloudbees-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cloudbees-data-model.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cloudbees-scopes.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/cloudbees-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cloudbees-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/cloudbees-finops.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.cloudbees.com/docs/cloudbees-unify/latest/
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.cloudbees.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.cloudbees.com/docs/cloudbees-unify/latest/getting-started/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cloudbees.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cloudbees.com/company/terms-of-service
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/cloudbees/cloudbees-feature-management
created: '2025-01-08'
description: CloudBees provides software delivery automation across continuous integration, continuous deployment, release orchestration, and feature management. Their developer surface includes the CloudBees CI REST API (an extension of the Jenkins REST API), the CloudBees CD/RO REST API for release orchestration, the CloudBees Feature Management REST API (formerly Rollout) for feature flags and environments, and the CloudBees Unify Platform API for the modern unified delivery platform. APIs are generally JSON, token-authenticated, and follow REST conventions.
finops:
- name: Cloudbees Finops
  service_category: API
  slug: cloudbees-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cloudbees.png
jsonld:
- class_count: 0
  name: Cloudbees Context
  property_count: 11
  slug: cloudbees-context
layout: provider
mcp_servers:
- description: ''
  name: CloudBees Unify MCP Server
  slug: cloudbees-unify-mcp-server
modified: '2026-09-05'
name: CloudBees
nav: Providers
network: true
overview: 'CloudBees publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Unify Platform API, Computer API, CreateItem API, and 5 more. Tagged areas include CI/CD, Continuous Delivery, Continuous Integration, DevOps, and Feature Flags.


  The CloudBees catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  CloudBees'' developer surface includes authentication, documentation, support, engineering blog, changelog, CLI, API reference, and 39 more developer resources.'
plans:
- name: Cloudbees Plans Pricing
  plan_count: 0
  slug: cloudbees-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 1
  name: Cloudbees Rate Limits
  slug: cloudbees-rate-limits
rules:
- effective_rule_count: 53
  extends:
  - spectral:oas
  name: CloudBees API Rules
  rule_count: 12
  severity_counts:
    error: 4
    hint: 0
    info: 2
    warn: 6
  slug: cloudbees-rules
scopes:
- name: Cloudbees Scopes
  scope_count: 4
  slug: cloudbees-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: exemplar
  composite: 67.3
  coverage:
    artifact_dirs: 27
    catalog_earned: 72.0
    catalog_earned_first_party: 8.0
    catalog_gap: 43.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 27.7
  facets:
    access_clarity: 55.3
    commercial_clarity: 55.3
    contract_governance: 72.7
    contract_quality: 58.1
    developer_ergonomics: 75.6
    discoverability: 72.2
    governance: 72.7
    operational_transparency: 81.6
  previous_composite: 39.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 22.2
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/cloudbees/refs/heads/main/screenshots/cloudbees-2026-06-20T174542.png
security:
- kind: authentication
  name: Cloudbees Authentication
  slug: cloudbees-authentication
  summary_line: apiKey/http/oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Cloudbees Domain Security
  slug: cloudbees-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cloudbees Vulnerability Disclosure
  slug: cloudbees-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Cloudbees Trust Center
  slug: cloudbees-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, HIPAA, FedRAMP, GDPR
slug: cloudbees
tags:
- CI/CD
- Continuous Delivery
- Continuous Integration
- DevOps
- Feature Flags
- Feature Management
- Jenkins
- Release Orchestration
- Software Delivery
website: https://www.cloudbees.com/
---
