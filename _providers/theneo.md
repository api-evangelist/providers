---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.5
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Theneo Agentic Access
  operation_count: 11
  slug: theneo-agentic-access
  summary_line: 11 operations · 6 acting
api_count: 1
apis:
- description: Import API specifications into projects.
  name: Theneo Import API
  slug: theneo-import-api
- description: Manage API documentation projects.
  name: Theneo Projects API
  slug: theneo-projects-api
- description: Publish and preview documentation.
  name: Theneo Publishing API
  slug: theneo-publishing-api
- description: Manage user access to projects.
  name: Theneo Users API
  slug: theneo-users-api
- description: Manage workspaces.
  name: Theneo Workspaces API
  slug: theneo-workspaces-api
artifact_total: 36
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
  name: API Collection
  slug: open-.refine-report
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
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/theneo/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/theneo-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/theneo-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/theneo-domain-security.yml
- group: auth
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
- name: Theneo Finops
  service_category: API
  slug: theneo-finops
graphqls:
- description: ''
  name: Theneo GraphQL API
  slug: theneo-graphql
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
overview: 'Theneo publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Import API, Projects API, Publishing API, and 2 more. Tagged areas include API Documentation, Developer Portal, Developer Tools, Documentation Platform, and Artificial Intelligence.


  The Theneo catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Theneo''s developer surface includes authentication, documentation, FAQ, pricing, engineering blog, signup flow, and 11 more developer resources.'
plans:
- name: Theneo Plans Pricing
  plan_count: 4
  slug: theneo-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 16
  name: Theneo Rate Limits
  slug: theneo-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Theneo API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: theneo-jsonschema-spectral-rules
- effective_rule_count: 10
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
  band: developing
  composite: 46.5
  coverage:
    artifact_dirs: 18
    catalog_gap: 45.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 25.0
    contract_quality: 67.8
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 25.0
    operational_transparency: 23.7
  previous_composite: 47.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/theneo/refs/heads/main/screenshots/theneo-2026-06-20T195249.png
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
slug: theneo
tags:
- API Documentation
- Developer Portal
- Developer Tools
- Documentation Platform
- Artificial Intelligence
- AI Co-Pilot
- MCP
- Platform
---
