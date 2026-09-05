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
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.1
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Appsmith Agentic Access
  operation_count: 5
  slug: appsmith-agentic-access
  summary_line: 5 operations · 1 acting
api_count: 1
apis:
- baseURL: https://app.appsmith.com/api/v1
  baseurl_source: declared
  description: Low-code application management
  name: Appsmith Applications API
  slug: appsmith-applications-api
- baseURL: https://app.appsmith.com/api/v1
  baseurl_source: declared
  description: Connected datasource management
  name: Appsmith Datasources API
  slug: appsmith-datasources-api
- baseURL: https://app.appsmith.com/api/v1
  baseurl_source: declared
  description: Workspace organization and management
  name: Appsmith Workspaces API
  slug: appsmith-workspaces-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Appsmith Applications API
  slug: open-appsmith-applications-api
- collection_type: open
  name: Appsmith Applications Datasources API
  slug: open-appsmith-datasources-api
- collection_type: open
  name: Appsmith Applications Workspaces API
  slug: open-appsmith-workspaces-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/appsmithorg/appsmith/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/appsmithorg/appsmith/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/appsmithorg/appsmith/blob/release/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/appsmithorg/appsmith/blob/release/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/appsmithorg/appsmith/blob/release/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/appsmithorg/appsmith/blob/release/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/appsmith-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/appsmith-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/appsmith-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/appsmith-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/appsmith
- group: company
  title: ''
  type: Website
  url: https://www.appsmith.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.appsmith.com
- group: agent
  title: ''
  type: MCPServer
  url: mcp/appsmith-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/appsmith-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/appsmith-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/appsmith-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/appsmith-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/appsmith-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://security.appsmith.com/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/appsmith-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/appsmith-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.appsmith.com
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/appsmith-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/appsmith-cli.yml
- group: design
  title: ''
  type: Components
  url: components/appsmith-components.yml
- group: build
  title: ''
  type: Packages
  url: packages/appsmith-packages.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/appsmith-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/appsmith-plans-pricing.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/appsmith-finops.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/appsmith-llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/appsmithorg
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.appsmith.com/getting-started
- group: operate
  title: ''
  type: Support
  url: https://community.appsmith.com
- group: company
  title: ''
  type: Blog
  url: https://www.appsmith.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.appsmith.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.appsmith.com/user/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.appsmith.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.appsmith.com/privacy-policy
created: 2026-03-27
description: 'Appsmith is an open source (Apache-2.0) low-code platform for building internal tools, admin panels and workflow applications on top of 25+ databases and any REST or GraphQL API. It runs self-hosted via Docker, Kubernetes or Helm, or as Appsmith Cloud. Its agent surface is a first-party Model Context Protocol server bundled into the Appsmith image and fronted at /mcp, exposing 61 tools that build and edit applications under the calling user''s own permissions; it ships disabled by default and requires a per-user mcp_ token. Appsmith publishes no public REST API reference: the platform API at /api/v1 is undocumented editor traffic and its springdoc OpenAPI surface is disabled by default and authenticated when enabled.'
examples:
- key_count: 8
  name: Application Example
  slug: application-example
finops:
- name: Appsmith Finops
  service_category: API
  slug: appsmith-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/appsmith.png
json_schemas:
- name: Application
  property_count: 8
  slug: application
json_structures:
- name: Application Structure
  property_count: 0
  slug: application-structure
jsonld:
- class_count: 10
  name: Appsmith Context
  property_count: 0
  slug: appsmith-context
layout: provider
mcp_servers:
- description: ''
  name: Appsmith MCP server
  slug: appsmith-mcp-server
modified: '2026-09-04'
name: Appsmith
nav: Providers
network: true
overview: 'Appsmith publishes 3 APIs on the [APIs.io](https://apis.io/) network: Applications API, Datasources API, and Workspaces API. Tagged areas include Low-Code, Open-Source, Internal Tools, Workflow-Automation, and Developer Tools.


  The Appsmith catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Appsmith''s developer surface includes authentication, documentation, changelog, CLI, getting-started guide, support, engineering blog, and 33 more developer resources.'
plans:
- name: Appsmith Plans Pricing
  plan_count: 3
  slug: appsmith-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 6
  name: Appsmith Rate Limits
  slug: appsmith-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Appsmith API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: appsmith-jsonschema-spectral-rules
- effective_rule_count: 64
  extends:
  - spectral:oas
  name: Appsmith API Rules
  rule_count: 23
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 14
  slug: appsmith-spectral-rules
score:
  band: exemplar
  composite: 71.3
  coverage:
    artifact_dirs: 29
    catalog_earned: 87.5
    catalog_earned_first_party: 24.0
    catalog_gap: 27.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 25.0
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 28.8
    contract_quality: 70.7
    developer_ergonomics: 49.4
    discoverability: 68.5
    governance: 28.8
    operational_transparency: 78.9
  open_source:
    applies: true
    score: 100.0
  previous_composite: 46.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/appsmith/refs/heads/main/screenshots/appsmith-2026-06-20T172348.png
security:
- kind: authentication
  name: Appsmith Authentication
  slug: appsmith-authentication
  summary_line: cookie/http-bearer/apiKey · 3 schemes
- kind: domain-security
  name: Appsmith Domain Security
  slug: appsmith-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Appsmith Vulnerability Disclosure
  slug: appsmith-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Appsmith Trust Center
  slug: appsmith-trust-center
  summary_line: SOC 2
slug: appsmith
tags:
- Low-Code
- Open-Source
- Internal Tools
- Workflow-Automation
- Developer Tools
website: https://www.appsmith.com
---
