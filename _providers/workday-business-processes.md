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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
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
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.4
  scored_at: '2026-09-23'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Workday Business Processes Agentic Access
  operation_count: 32
  slug: workday-business-processes-agentic-access
  summary_line: 32 operations · 15 acting
api_count: 2
apis:
- baseURL: https://{tenantHostname}/businessProcess/v1
  baseurl_source: declared
  description: Manage approval steps and approval chains
  name: Workday Business Processes Approvals API
  slug: workday-business-processes-approvals-api
- baseURL: https://{tenantHostname}/businessProcess/v1
  baseurl_source: declared
  description: Retrieve and manage business process type definitions
  name: Workday Business Processes Business Process Definitions API
  slug: workday-business-processes-business-process-definitions-api
- baseURL: https://{tenantHostname}/businessProcess/v1
  baseurl_source: declared
  description: Manage user inbox items requiring action
  name: Workday Business Processes Inbox Items API
  slug: workday-business-processes-inbox-items-api
- baseURL: https://{tenantHostname}/businessProcess/v1
  baseurl_source: declared
  description: Manage running business process instances
  name: Workday Business Processes Process Instances API
  slug: workday-business-processes-process-instances-api
- baseURL: https://api.workday.com/customBusinessProcessConfig/v1
  baseurl_source: declared
  description: Create, read, update and delete custom business process types and their event task definitions.
  name: Workday Custom Business Process Config API
  slug: workday-business-processes-custom-business-process-config-api
- description: 'The Workday Web Services Integrations service, v47.0. Carries the eight SOAP business process operations — Approve, Cancel, Deny, Rescind and Send Back a business process, Reassign a business process '
  name: Workday Integrations SOAP Service (business process operations)
  slug: workday-business-processes-integrations-soap-service
artifact_total: 48
collections:
- collection_type: postman
  name: Workday Business Process Approvals API
  slug: postman-workday-business-processes-approvals-api
- collection_type: postman
  name: Workday Business Process Approvals Business Process Definitions API
  slug: postman-workday-business-processes-business-process-definitions-api
- collection_type: postman
  name: Workday Business Process Approvals Inbox Items API
  slug: postman-workday-business-processes-inbox-items-api
- collection_type: postman
  name: Workday Business Process Approvals Process Instances API
  slug: postman-workday-business-processes-process-instances-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Workday Business Process Approvals API
  slug: open-workday-business-processes-approvals-api
- collection_type: open
  name: Workday Business Process Approvals Business Process Definitions API
  slug: open-workday-business-processes-business-process-definitions-api
- collection_type: open
  name: Workday Business Process Approvals Inbox Items API
  slug: open-workday-business-processes-inbox-items-api
- collection_type: open
  name: Workday Business Process Approvals Process Instances API
  slug: open-workday-business-processes-process-instances-api
- collection_type: open
  name: Workday Business Process API
  slug: open-workday-business-processes
common:
- group: company
  title: ''
  type: Website
  url: https://www.workday.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.workday.com/
- group: start
  title: ''
  type: Portal
  url: https://community.workday.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.workday.com/doc/GUID-e31b535f-7722-4f61-9795-a27ef9d78a86-enHYPHENus.md
- group: docs
  title: ''
  type: APIReference
  url: https://community.workday.com/sites/default/files/file-hosting/restapi/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.workday.com/doc/zwx1518028675482.md
- group: operate
  title: ''
  type: Support
  url: https://community.workday.com
- group: operate
  title: ''
  type: HelpCenter
  url: https://forum.developer.workday.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.workday.com/en-us/homepage.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Workday
- group: start
  title: ''
  type: SignUp
  url: https://developer.workday.com/login
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/workday-business-processes/overview
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.workday.com/en-us/legal/site-terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.workday.com/en-us/privacy.html
- group: auth
  title: ''
  type: Compliance
  url: https://www.workday.com/en-us/why-workday/trust/compliance.html
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/workday-business-processes/refs/heads/main/security/workday-business-processes-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/workday-business-processes-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/workday-business-processes/refs/heads/main/security/workday-business-processes-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/workday-business-processes-domain-security.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.workday.com
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/workday-business-processes/refs/heads/main/changelog/workday-business-processes-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/workday-business-processes-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/workday-business-processes/refs/heads/main/lifecycle/workday-business-processes-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/workday-business-processes-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/workday-business-processes/refs/heads/main/authentication/workday-business-processes-authentication.yml
  title: ''
  type: Authentication
  url: authentication/workday-business-processes-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/workday-business-processes/refs/heads/main/scopes/workday-business-processes-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/workday-business-processes-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/workday-business-processes/refs/heads/main/conventions/workday-business-processes-conventions.yml
  title: ''
  type: Conventions
  url: conventions/workday-business-processes-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/workday-business-processes/refs/heads/main/errors/workday-business-processes-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/workday-business-processes-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/workday-business-processes/refs/heads/main/conformance/workday-business-processes-conformance.yml
  title: ''
  type: Conformance
  url: conformance/workday-business-processes-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/workday-business-processes/refs/heads/main/data-model/workday-business-processes-data-model.yml
  title: ''
  type: DataModel
  url: data-model/workday-business-processes-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/workday-business-processes/refs/heads/main/rate-limits/workday-business-processes-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/workday-business-processes-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/workday-business-processes/refs/heads/main/plans/workday-business-processes-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/workday-business-processes-plans-pricing.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/workday-business-processes/refs/heads/main/packages/workday-business-processes-packages.yml
  title: ''
  type: Packages
  url: packages/workday-business-processes-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/workday-business-processes/refs/heads/main/packages/workday-business-processes-packages.yml
  title: ''
  type: SDKs
  url: packages/workday-business-processes-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/workday-business-processes/refs/heads/main/cli/workday-business-processes-cli.yml
  title: ''
  type: CLI
  url: cli/workday-business-processes-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/workday-business-processes/refs/heads/main/components/workday-business-processes-components.yml
  title: ''
  type: Components
  url: components/workday-business-processes-components.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/workday-business-processes/refs/heads/main/sandbox/workday-business-processes-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/workday-business-processes-sandbox.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/workday-business-processes/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/workday-business-processes/refs/heads/main/mcp/workday-business-processes-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/workday-business-processes-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/workday-business-processes/refs/heads/main/agentic-access/workday-business-processes-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/workday-business-processes-agentic-access.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/workday-business-processes/refs/heads/main/llms/workday-business-processes-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/workday-business-processes-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/workday-business-processes/refs/heads/main/wsdl/workday-business-processes-integrations-v47.0.wsdl
  title: ''
  type: WSDL
  url: wsdl/workday-business-processes-integrations-v47.0.wsdl
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/workday-business-processes/refs/heads/main/overlays/workday-business-processes-business-process-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/workday-business-processes-business-process-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/workday-business-processes/refs/heads/main/overlays/workday-business-processes-custom-business-process-config-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/workday-business-processes-custom-business-process-config-overlay.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/workday-business-processes/refs/heads/main/json-ld/workday-business-processes-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/workday-business-processes-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/workday-business-processes/refs/heads/main/rules/workday-business-processes-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/workday-business-processes-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/workday-business-processes/refs/heads/main/vocabulary/workday-business-processes-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/workday-business-processes-vocabulary.yml
created: '2024-01-01'
description: 'Workday Business Processes is the workflow engine at the centre of Workday HCM and Financial Management: every hire, job change, expense report, requisition and payment runs as a business process event routed through configured approval, to-do and questionnaire steps. Workday exposes it as a first-party REST service, businessProcess v1, which reads business process types, events and event steps and performs the real actions on them — approve, deny, send back, reassign, cancel and rescind — alongside a Custom Business Process Config v1 service for authoring custom process types and event task definitions, business-process operations inside the Integrations SOAP service, and business process query fields in the Workday Graph API.'
examples:
- key_count: 2
  name: Workday Business Processes Approval Request Example
  slug: workday-business-processes-approval-request-example
- key_count: 7
  name: Workday Business Processes Business Process Definition Example
  slug: workday-business-processes-business-process-definition-example
- key_count: 2
  name: Workday Business Processes Denial Request Example
  slug: workday-business-processes-denial-request-example
- key_count: 8
  name: Workday Business Processes Inbox Item Example
  slug: workday-business-processes-inbox-item-example
- key_count: 4
  name: Workday Business Processes Initiate Process Request Example
  slug: workday-business-processes-initiate-process-request-example
- key_count: 9
  name: Workday Business Processes Process Instance Example
  slug: workday-business-processes-process-instance-example
- key_count: 7
  name: Workday Business Processes Process Step Example
  slug: workday-business-processes-process-step-example
finops:
- name: Workday Business Processes Finops
  service_category: API
  slug: workday-business-processes-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/workday-business-processes.png
json_schemas:
- name: Approval Request
  property_count: 2
  slug: workday-business-processes-approval-request
- name: Business Process Definition
  property_count: 6
  slug: workday-business-processes-business-process-definition
- name: Denial Request
  property_count: 2
  slug: workday-business-processes-denial-request
- name: Inbox Item
  property_count: 10
  slug: workday-business-processes-inbox-item
- name: Initiate Process Request
  property_count: 4
  slug: workday-business-processes-initiate-process-request
- name: Process Instance
  property_count: 11
  slug: workday-business-processes-process-instance
- name: Process Step
  property_count: 8
  slug: workday-business-processes-process-step
json_structures:
- name: Workday Business Processes Approval Request Structure
  property_count: 2
  slug: workday-business-processes-approval-request-structure
- name: Workday Business Processes Business Process Definition Structure
  property_count: 6
  slug: workday-business-processes-business-process-definition-structure
- name: Workday Business Processes Denial Request Structure
  property_count: 2
  slug: workday-business-processes-denial-request-structure
- name: Workday Business Processes Inbox Item Structure
  property_count: 10
  slug: workday-business-processes-inbox-item-structure
- name: Workday Business Processes Initiate Process Request Structure
  property_count: 4
  slug: workday-business-processes-initiate-process-request-structure
- name: Workday Business Processes Process Instance Structure
  property_count: 11
  slug: workday-business-processes-process-instance-structure
- name: Workday Business Processes Process Step Structure
  property_count: 8
  slug: workday-business-processes-process-step-structure
jsonld:
- class_count: 31
  name: Workday Business Processes Context
  property_count: 11
  slug: workday-business-processes-context
layout: provider
modified: '2026-09-17'
name: Workday Business Processes
nav: Providers
network: true
overview: 'Workday Business Processes publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Approvals API, Business Process Definitions API, Inbox Items API, and 2 more. Tagged areas include Business Processes, Workflows, Approvals, Human Resources, and Enterprise.


  The Workday Business Processes catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Workday Business Processes'' developer surface includes developer portal, documentation, API reference, getting-started guide, support, engineering blog, signup flow, and 36 more developer resources.'
plans:
- name: Workday Business Processes Plans Pricing
  plan_count: 0
  slug: workday-business-processes-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 7
  name: Workday Business Processes Rate Limits
  slug: workday-business-processes-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Workday Business Processes API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: workday-business-processes-jsonschema-spectral-rules
- effective_rule_count: 85
  extends:
  - spectral:oas
  name: Workday Business Processes API Rules
  rule_count: 44
  severity_counts:
    error: 8
    hint: 0
    info: 9
    warn: 27
  slug: workday-business-processes-spectral-rules
scopes:
- name: Workday Business Processes Scopes
  scope_count: 2
  slug: workday-business-processes-scopes
  summary_line: 2 scopes · implicit
score:
  band: developing
  composite: 51.9
  coverage:
    artifact_dirs: 35
    catalog_earned: 73.5
    catalog_earned_first_party: 0.0
    catalog_gap: 41.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 3.1
  facets:
    access_clarity: 57.9
    contract_governance: 47.0
    contract_quality: 26.1
    developer_ergonomics: 81.0
    discoverability: 68.5
    operational_transparency: 44.7
  previous_composite: 48.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/workday-business-processes/refs/heads/main/screenshots/workday-business-processes-2026-06-20T201558.png
security:
- kind: authentication
  name: Workday Business Processes Authentication
  slug: workday-business-processes-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Workday Business Processes Domain Security
  slug: workday-business-processes-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Workday Business Processes Trust Center
  slug: workday-business-processes-trust-center
  summary_line: SOC 1, SOC 2, ISO 27001, ISO 22301, CSA STAR, FedRAMP, IRAP, HITRUST, HIPAA, GDPR, C5
slug: workday-business-processes
tags:
- Business Processes
- Workflows
- Approvals
- Human Resources
- Enterprise
- Software-as-a-Service
- HCM
- Financial Management
- Process Automation
- Event Steps
- SOAP
- GraphQL
website: https://www.workday.com/
---
