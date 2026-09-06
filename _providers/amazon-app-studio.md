---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.3
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Amazon App Studio Agentic Access
  operation_count: 2
  slug: amazon-app-studio-agentic-access
  summary_line: 2 operations
api_count: 1
apis:
- baseURL: https://appstudio.amazonaws.com
  baseurl_source: declared
  description: The Apps API from Amazon App Studio — 2 operation(s) for apps.
  name: Amazon App Studio Apps API
  slug: amazon-app-studio-apps-api
artifact_total: 33
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon App Studio Apps API
  slug: open-amazon-app-studio-apps-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/amazon-app-studio-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-app-studio-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-app-studio-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-app-studio-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-app-studio-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-app-studio-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/app-studio/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/app-studio/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://us-east-1.console.aws.amazon.com/appstudio/
- group: start
  title: ''
  type: SignUp
  url: https://signin.aws.amazon.com/signup?request_type=register
- group: operate
  title: ''
  type: Status
  url: https://health.aws.amazon.com/health/status
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-app-studio-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-app-studio-vocabulary.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/amazon-app-studio-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/amazon-app-studio-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/amazon-app-studio-security.txt
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/amazon-app-studio-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/amazon-app-studio-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/amazon-app-studio-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/amazon-app-studio-lifecycle.yml
created: '2026-03-16'
description: Amazon App Studio is a generative AI-powered low-code application builder that enables business users to create internal applications without requiring extensive coding knowledge. Built on AWS infrastructure, App Studio integrates with AWS data sources and services to enable rapid development of enterprise business tools.
examples:
- key_count: 6
  name: Amazon App Studio App Example
  slug: amazon-app-studio-app-example
- key_count: 4
  name: Amazon App Studio Appsummary Example
  slug: amazon-app-studio-appsummary-example
- key_count: 2
  name: Amazon App Studio Listappsresponse Example
  slug: amazon-app-studio-listappsresponse-example
features:
- description: Use natural language prompts to generate application layouts, data models, and logic with Amazon Q assistance.
  name: Generative AI Application Builder
- description: Build internal business applications using drag-and-drop components without writing code.
  name: No-Code Application Development
- description: Connect applications to AWS DynamoDB, Aurora, S3, and other data sources with built-in connectors.
  name: AWS Data Source Integration
- description: Configure fine-grained access permissions for application users using AWS IAM Identity Center.
  name: Role-Based Access Control
- description: Deploy internal applications with a single click and share with team members using AWS access controls.
  name: One-Click Deployment
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-app-studio.png
integrations:
- description: Connect App Studio applications to DynamoDB for serverless NoSQL data storage and retrieval.
  name: Amazon DynamoDB
- description: Use Aurora as a relational database backend for App Studio applications requiring structured data.
  name: Amazon Aurora
- description: Manage user access to App Studio applications using IAM Identity Center for single sign-on.
  name: AWS IAM Identity Center
- description: Leverage Amazon Q generative AI capabilities within App Studio for AI-assisted application development.
  name: Amazon Q
json_schemas:
- name: App
  property_count: 6
  slug: amazon-app-studio-app
- name: AppSummary
  property_count: 4
  slug: amazon-app-studio-appsummary
- name: ListAppsResponse
  property_count: 2
  slug: amazon-app-studio-listappsresponse
json_structures:
- name: Amazon App Studio App Structure
  property_count: 0
  slug: amazon-app-studio-app-structure
- name: Amazon App Studio Appsummary Structure
  property_count: 0
  slug: amazon-app-studio-appsummary-structure
- name: Amazon App Studio Listappsresponse Structure
  property_count: 0
  slug: amazon-app-studio-listappsresponse-structure
jsonld:
- class_count: 0
  name: Amazon App Studio Context
  property_count: 6
  slug: amazon-app-studio-context
layout: provider
modified: '2026-06-20'
name: Amazon App Studio
nav: Providers
network: true
overview: 'Amazon App Studio publishes 1 API on the [APIs.io](https://apis.io/) network: Apps API. Tagged areas include Generative AI, Internal Tools, Low-Code, and No-Code.


  The Amazon App Studio catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon App Studio''s developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 19 more developer resources.'
random_paper: 20
rules:
- effective_rule_count: 5
  extends: []
  name: Amazon App Studio API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: amazon-app-studio-jsonschema-spectral-rules
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: Amazon App Studio API Rules
  rule_count: 9
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 4
  slug: amazon-app-studio-spectral-rules
score:
  band: developing
  composite: 45.2
  coverage:
    artifact_dirs: 20
    catalog_earned: 56.5
    catalog_earned_first_party: 0.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 33.3
    contract_quality: 66.0
    developer_ergonomics: 35.7
    discoverability: 66.7
    governance: 33.3
    operational_transparency: 2.6
  previous_composite: 45.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-app-studio/refs/heads/main/screenshots/amazon-app-studio-2026-07-25T195916.png
security:
- kind: authentication
  name: Amazon App Studio Authentication
  slug: amazon-app-studio-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Amazon App Studio Domain Security
  slug: amazon-app-studio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon App Studio Vulnerability Disclosure
  slug: amazon-app-studio-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon App Studio Trust Center
  slug: amazon-app-studio-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-app-studio
tags:
- Generative AI
- Internal Tools
- Low-Code
- No-Code
use_cases:
- description: Build inventory management, employee onboarding, and operational dashboards for internal business use.
  name: Internal Business Tools
- description: Create forms and data entry tools connected to existing databases for field operations and back-office teams.
  name: Data Entry Applications
- description: Automate approval workflows, task management, and process tracking with connected business logic.
  name: Workflow Automation
- description: Build IT request portals, asset management tools, and helpdesk applications for internal teams.
  name: IT Self-Service Portals
website: https://aws.amazon.com/app-studio/
---
