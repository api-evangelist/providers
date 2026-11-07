---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 35.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Theneo Agentic Access
  operation_count: 11
  slug: theneo-agentic-access
  summary_line: 11 operations · 6 acting
api_count: 1
apis:
- baseURL: https://api.theneo.io
  baseurl_source: declared
  description: Import API specifications into projects.
  name: Theneo Import API
  slug: theneo-import-api
- baseURL: https://api.theneo.io
  baseurl_source: declared
  description: Manage API documentation projects.
  name: Theneo Projects API
  slug: theneo-projects-api
- baseURL: https://api.theneo.io
  baseurl_source: declared
  description: Publish and preview documentation.
  name: Theneo Publishing API
  slug: theneo-publishing-api
- baseURL: https://api.theneo.io
  baseurl_source: declared
  description: Manage user access to projects.
  name: Theneo Users API
  slug: theneo-users-api
- baseURL: https://api.theneo.io
  baseurl_source: declared
  description: Manage workspaces.
  name: Theneo Workspaces API
  slug: theneo-workspaces-api
artifact_total: 38
collections:
- collection_type: postman
  name: Theneo Import API
  slug: postman-theneo-import-api
- collection_type: postman
  name: Theneo Import Projects API
  slug: postman-theneo-projects-api
- collection_type: postman
  name: Theneo Import Publishing API
  slug: postman-theneo-publishing-api
- collection_type: postman
  name: Theneo Import Users API
  slug: postman-theneo-users-api
- collection_type: postman
  name: Theneo Import Workspaces API
  slug: postman-theneo-workspaces-api
- collection_type: open
  name: Theneo API
  slug: open-theneo-api
- collection_type: open
  name: Theneo Import API
  slug: open-theneo-import-api
- collection_type: open
  name: Theneo Import Projects API
  slug: open-theneo-projects-api
- collection_type: open
  name: Theneo Import Publishing API
  slug: open-theneo-publishing-api
- collection_type: open
  name: Theneo Import Users API
  slug: open-theneo-users-api
- collection_type: open
  name: Theneo Import Workspaces API
  slug: open-theneo-workspaces-api
common:
- group: auth
  href: https://artifacts.apis.io/theneo/well-known/theneo-calendly-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/theneo-calendly-security.txt
- group: build
  href: https://artifacts.apis.io/theneo/integrations/theneo-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/theneo-integration-edges.yml
- group: commercial
  href: https://artifacts.apis.io/theneo/plans/theneo-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/theneo-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/theneo/rate-limits/theneo-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/theneo-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/theneo/finops/theneo-finops.yml
  title: ''
  type: FinOps
  url: finops/theneo-finops.yml
- group: other
  href: https://artifacts.apis.io/theneo/capabilities/theneo-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/theneo-capability-edges.yml
- group: operate
  href: https://artifacts.apis.io/theneo/changelog/theneo-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/theneo-changelog.yml
- group: design
  href: https://artifacts.apis.io/theneo/rules/theneo-rules.yml
  title: ''
  type: Spectral
  url: rules/theneo-rules.yml
- group: design
  href: https://artifacts.apis.io/theneo/rules/theneo-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/theneo-jsonschema-spectral-rules.yml
- group: agent
  href: https://artifacts.apis.io/theneo/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/theneo/data-model/theneo-data-model.yml
  title: ''
  type: DataModel
  url: data-model/theneo-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.theneo.io/security
- group: design
  href: https://artifacts.apis.io/theneo/errors/theneo-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/theneo-problem-types.yml
- group: design
  href: https://artifacts.apis.io/theneo/conformance/theneo-conformance.yml
  title: ''
  type: Conformance
  url: conformance/theneo-conformance.yml
- group: agent
  href: https://artifacts.apis.io/theneo/llms/theneo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/theneo-llms.txt
- group: agent
  href: https://artifacts.apis.io/theneo/well-known/theneo-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/theneo-well-known.yml
- group: other
  href: https://artifacts.apis.io/theneo/hosts/theneo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/theneo-hosts.yml
- group: other
  href: https://artifacts.apis.io/theneo/vendors/theneo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/theneo-vendors.yml
- group: build
  href: https://artifacts.apis.io/theneo/packages/theneo-packages.yml
  title: ''
  type: Packages
  url: packages/theneo-packages.yml
- group: start
  title: ''
  type: SignUp
  url: https://app.theneo.io/signup
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.theneo.io/privacy-terms
- group: start
  title: ''
  type: GettingStarted
  url: https://app.theneo.io/theneo/quickstart/theneo-quickstart-guide/quickstart
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.theneo.io/developer-portal
- group: docs
  title: ''
  type: APIReference
  url: https://www.theneo.io/api-reference
- group: company
  title: ''
  type: Website
  url: https://www.theneo.io/
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/theneo/overview
- group: agent
  href: https://artifacts.apis.io/theneo/agentic-access/theneo-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/theneo-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/theneo/security/theneo-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/theneo-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/theneo/security/theneo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/theneo-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/theneo/authentication/theneo-authentication.yml
  title: ''
  type: Authentication
  url: authentication/theneo-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/theneoinc
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Theneo-Inc
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Theneo-Inc/theneo-tools
- group: build
  title: ''
  type: GitHubAction
  url: https://github.com/Theneo-Inc/api-documentation
- group: other
  title: ''
  type: Repository
  url: https://github.com/Theneo-Inc/Cartlis
- group: docs
  title: ''
  type: Documentation
  url: https://app.theneo.io/theneo/quickstart/theneo-quickstart-guide
- group: operate
  title: ''
  type: FAQ
  url: https://app.theneo.io/theneo/quickstart/faq-2
- group: commercial
  title: ''
  type: Pricing
  url: https://www.theneo.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.theneo.io/blog
- group: auth
  title: ''
  type: Security
  url: https://www.theneo.io/security
- group: start
  title: ''
  type: Signup
  url: https://app.theneo.io/signup
- group: start
  title: ''
  type: Demo
  url: https://calendly.com/theneo/theneo-demo
coverage:
  checked: '2026-10-04'
  detail: Docs at https://docs.theneo.io/openapi.json return HTML instead of a machine‑readable spec.
  evidence:
  - status: 200
    url: https://docs.theneo.io/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2025-01-08'
description: Beautiful, up-to-date docs without the effort. Theneo is an AI-native API documentation and developer portal platform that auto-generates interactive docs from OpenAPI, Swagger, Postman, GraphQL, gRPC, SOAP/WSDL, and AsyncAPI specifications. Its AI Co-pilot can fully generate, enhance, or stay out of the way of human-authored content, while Ask AI Bot, MCP server integration, llms.txt support, smart changelogs, and the Elva API management platform extend the same surface to AI agents. Used by 15,000+ teams including Ticketmaster, Corpay, and SimilarWeb; backed by Y Combinator; SOC 2 Type II, ISO 27001, ISO 9001, and GDPR compliant.
examples:
- key_count: 2
  name: Theneo Add New Project Example
  slug: theneo-add-new-project-example
- key_count: 2
  name: Theneo Get All Projects Example
  slug: theneo-get-all-projects-example
- key_count: 2
  name: Theneo Import Api Specification Example
  slug: theneo-import-api-specification-example
- key_count: 2
  name: Theneo Publish Project Example
  slug: theneo-publish-project-example
finops:
- has_sources: true
  method: derived
  name: Theneo Finops
  primary_unit: workspace
  service_category: ''
  slug: theneo-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/theneo.png
json_schemas:
- name: Theneo Project User
  property_count: 4
  slug: project-user
- name: Theneo Project
  property_count: 8
  slug: project
- name: Theneo Workspace
  property_count: 3
  slug: workspace
json_structures:
- name: Theneo Project Structure
  property_count: 0
  slug: theneo-project-structure
jsonld:
- class_count: 0
  name: Theneo Context
  property_count: 3
  slug: theneo-context
layout: provider
modified: '2026-05-22'
name: Theneo
nav: Providers
network: true
overview: 'Theneo publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Import API, Projects API, Publishing API, and 2 more. Tagged areas include API Documentation, Developer Portal, Developer Tools, Documentation Platform, and Artificial Intelligence.


  The Theneo catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Theneo''s developer surface includes changelog, signup flow, getting-started guide, API reference, authentication, documentation, FAQ, and 35 more developer resources.'
plans:
- name: Theneo Plans Pricing
  plan_count: 6
  slug: theneo-plans-pricing
- name: Theneo Price Estimates
  plan_count: 0
  slug: theneo-price-estimates
random_paper: 19
rate_limits:
- limit_count: 16
  name: Theneo Rate Limits
  slug: theneo-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Theneo — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: theneo-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 10
  extends: []
  name: Theneo API Rules
  rule_count: 10
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 8
  slug: theneo-rules
score:
  band: strong
  composite: 55.5
  coverage:
    artifact_dirs: 36
    catalog_earned: 76.8
    catalog_earned_first_party: 12.0
    catalog_gap: 38.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.6
  facets:
    access_clarity: 73.7
    contract_governance: 28.0
    contract_quality: 61.3
    developer_ergonomics: 48.2
    discoverability: 73.2
    operational_transparency: 39.5
  previous_composite: 62.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/theneo/theneo-2026-06-20T195249.png
security:
- kind: authentication
  name: Theneo Authentication
  slug: theneo-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Theneo Domain Security
  slug: theneo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Theneo Trust Center
  slug: theneo-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
skill_count: 3
skills:
- name: theneo-create-project
  slug: theneo-create-project
- name: projects
  slug: theneo-projects-skill
- name: theneo-publish-and-preview
  slug: theneo-publish-and-preview
slug: theneo
tags:
- API Documentation
- Developer Portal
- Developer Tools
- Documentation Platform
- Artificial Intelligence
- AI Copilot
- MCP
- Platform
website: https://www.theneo.io/
---
