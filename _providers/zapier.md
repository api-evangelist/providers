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
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 67.1
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Zapier Agentic Access
  operation_count: 21
  slug: zapier-agentic-access
  summary_line: 21 operations · 8 acting
api_count: 13
apis:
- description: Build and ship AI workflows in minutesno IT bottlenecks, no complexity. Just results.
  name: Zapier
  slug: zapier
- description: 'Zapier AI Actions (formerly Natural Language Actions) provides a universal natural language API optimized for AI and LLM-based experiences. It enables AI platforms and custom integrations to leverage '
  name: Zapier AI Actions API
  slug: ai-actions-api
- description: Zapier MCP (Model Context Protocol) connects AI tools like Claude, ChatGPT, and Cursor to over 8,000 apps using the open Model Context Protocol standard. It provides a server endpoint for connecting a
  name: Zapier MCP
  slug: mcp
- description: Refers to resources interacting with 'Accounts' associated resources
  name: Zapier Accounts API
  slug: zapier-accounts-api
- description: Refers to resources interacting with 'Actions' associated resources
  name: Zapier Actions API
  slug: zapier-actions-api
- description: Refers to resources interacting with 'Apps' associated resources
  name: Zapier Apps API
  slug: zapier-apps-api
- description: Refers to resources interacting with 'Authentications' associated resources
  name: Zapier Authentications API
  slug: zapier-authentications-api
- description: Refers to resources interacting with 'Categories' associated resources
  name: Zapier Categories API
  slug: zapier-categories-api
- description: Refers to resources interacting with 'Experimental' associated resources
  name: Zapier Experimental API
  slug: zapier-experimental-api
- description: Refers to resources interacting with 'Inputs' associated resources
  name: Zapier Inputs API
  slug: zapier-inputs-api
- description: Refers to resources interacting with 'Outputs' associated resources
  name: Zapier Outputs API
  slug: zapier-outputs-api
- description: Refers to resources interacting with 'Zap Templates' associated resources
  name: Zapier Zap Templates API
  slug: zapier-zap-templates-api
- description: Refers to resources interacting with 'Zaps' associated resources
  name: Zapier Zaps API
  slug: zapier-zaps-api
arazzos:
- description: Create an authentication for an app, list its actions, and test an action against the live third-party API.
  name: Zapier Connect and Test an Action
  slug: zapier-connect-and-test-action-workflow
- description: List an app's actions, create a multi-step Zap, and confirm it appears in the user's Zap list.
  name: Zapier Create a Zap from Actions
  slug: zapier-create-zap-from-actions-workflow
- description: Search for an app, list its actions, read the input fields, and resolve the choices for a dropdown field.
  name: Zapier Discover and Configure an Action
  slug: zapier-discover-and-configure-action-workflow
- description: List an app's actions, then fetch both the input and output field schemas for a chosen action.
  name: Zapier Inspect an Action Schema
  slug: zapier-inspect-action-schema-workflow
- description: List the user's Zaps, pull recent runs, and branch when errored runs are present.
  name: Zapier Monitor Zap Runs
  slug: zapier-monitor-zap-runs-workflow
- description: Discover an action on an app, resolve its input fields, run it, and poll for the result.
  name: Zapier Run an AI Action
  slug: zapier-run-ai-action-workflow
artifact_total: 388
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Partner Accounts API
  slug: open-zapier-accounts-api
- collection_type: open
  name: Partner Accounts Actions API
  slug: open-zapier-actions-api
- collection_type: open
  name: Partner Accounts Apps API
  slug: open-zapier-apps-api
- collection_type: open
  name: Partner Accounts Authentications API
  slug: open-zapier-authentications-api
- collection_type: open
  name: Partner Accounts Categories API
  slug: open-zapier-categories-api
- collection_type: open
  name: Partner Accounts Experimental API
  slug: open-zapier-experimental-api
- collection_type: open
  name: Partner Accounts Inputs API
  slug: open-zapier-inputs-api
- collection_type: open
  name: Partner Accounts Outputs API
  slug: open-zapier-outputs-api
- collection_type: open
  name: Partner API
  slug: open-zapier-partner-api
- collection_type: open
  name: Partner Accounts Zap Templates API
  slug: open-zapier-zap-templates-api
- collection_type: open
  name: Partner Accounts Zaps API
  slug: open-zapier-zaps-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zapier-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/zapier-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zapier-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zapier-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/zapier-scopes.yml
- group: build
  title: ''
  type: Packages
  url: packages/zapier-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/zapier-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/zapier-mcp.yml
- group: agent
  title: ''
  type: LlmsText
  url: llms/zapier-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/zapier-partner-api-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/zapier-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/zapier-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/zapier-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/zapier-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/zapier-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/zapier-cli.yml
- group: design
  title: ''
  type: Components
  url: components/zapier-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/zapier-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/zapier-sandbox.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/zapier/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/zapier-connect-and-test-action-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/zapier-create-zap-from-actions-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/zapier-discover-and-configure-action-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/zapier-inspect-action-schema-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/zapier-monitor-zap-runs-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/zapier-run-ai-action-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zapier
- group: company
  title: ''
  type: Website
  url: https://zapier.com/
- group: company
  title: ''
  type: Blog
  url: https://zapier.com/blog/
- group: other
  title: ''
  type: Customers
  url: https://zapier.com/customer-stories
- group: design
  title: ''
  type: Webhooks
  url: https://zapier.com/blog/what-are-webhooks/
- group: docs
  title: ''
  type: Guide
  url: https://zapier.com/resources/guides
- group: learn
  title: ''
  type: Webinars
  url: https://zapier.com/resources/events
- group: operate
  title: ''
  type: Support
  url: https://help.zapier.com/hc/en-us
- group: company
  title: ''
  type: Partners
  url: https://zapier.com/experts
- group: operate
  title: ''
  type: Support
  url: https://zapier.com/l/support
- group: operate
  title: ''
  type: Support
  url: https://zapier.com/l/support-services
- group: docs
  title: ''
  type: Documentation
  url: https://docs.zapier.com/platform/home
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.zapier.com/platform/quickstart/build-integration
- group: other
  title: ''
  type: Glossary
  url: https://docs.zapier.com/platform/quickstart/glossary
- group: build
  title: ''
  type: CLI
  url: https://docs.zapier.com/platform/build-cli/overview
- group: start
  title: ''
  type: Login
  url: https://zapier.com/app/login?next=%2Fapp%2Fdeveloper%2F
- group: start
  title: ''
  type: Signup
  url: https://zapier.com/sign-up?next=%2Fapp%2Fdeveloper%2F
- group: commercial
  title: ''
  type: Pricing
  url: https://zapier.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.zapier.com
- group: operate
  title: ''
  type: Forums
  url: https://community.zapier.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://zapier.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://zapier.com/legal/data-privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://zapier.com/developer-platform/tos
- group: start
  title: ''
  type: DeveloperPortal
  url: https://zapier.com/developer-platform
- group: company
  title: ''
  type: PartnerProgram
  url: https://zapier.com/developer-platform/partner-program
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/zapier/zapier-platform
- group: docs
  title: ''
  type: Schema
  url: https://zapier.github.io/zapier-platform-schema/build/schema.html
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/zapier/refs/heads/main/rules/zapier-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/zapier/refs/heads/main/vocabulary/zapier-vocabulary.yml
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/zapier/refs/heads/main/json-schema/zapier-platform-schema.json
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.zapier.com/llms.txt
- group: other
  title: ''
  type: AICatalog
  url: ai-catalog/zapier-ai-catalog.yml
created: '2025-06-06T00:00:00.000Z'
description: Zapier is an automation platform that connects different apps and services to automate workflows without requiring coding knowledge. It acts as a bridge between thousands of popular applications like Gmail, Slack, Salesforce, Google Sheets, Trello, and many others.
examples:
- key_count: 5
  name: Partner Api  Action Run Response Error Example
  slug: partner-api--action-run-response-error-example
- key_count: 4
  name: Partner Api  Action Run Response Example
  slug: partner-api--action-run-response-example
- key_count: 4
  name: Partner Api  Action Test Request Example
  slug: partner-api--action-test-request-example
- key_count: 3
  name: Partner Api  Authentication Create Request Example
  slug: partner-api--authentication-create-request-example
- key_count: 2
  name: Partner Api  List Input Fields Request Example
  slug: partner-api--list-input-fields-request-example
- key_count: 3
  name: Partner Api  List Output Fields Request Example
  slug: partner-api--list-output-fields-request-example
- key_count: 3
  name: Partner Api  Run Action Request Example
  slug: partner-api--run-action-request-example
- key_count: 2
  name: Partner Api  Run Action Response Example
  slug: partner-api--run-action-response-example
- key_count: 8
  name: Partner Api Action Example
  slug: partner-api-action-example
- key_count: 1
  name: Partner Api Action Run Response Example
  slug: partner-api-action-run-response-example
- key_count: 1
  name: Partner Api Action Test Request Example
  slug: partner-api-action-test-request-example
- key_count: 3
  name: Partner Api Action Test Response Example
  slug: partner-api-action-test-response-example
- key_count: 3
  name: Partner Api Actions Response Example
  slug: partner-api-actions-response-example
- key_count: 8
  name: Partner Api App Category Example
  slug: partner-api-app-category-example
- key_count: 10
  name: Partner Api App Example
  slug: partner-api-app-example
- key_count: 10
  name: Partner Api Apps Example
  slug: partner-api-apps-example
- key_count: 4
  name: Partner Api Apps Images Example
  slug: partner-api-apps-images-example
- key_count: 7
  name: Partner Api Apps Response Example
  slug: partner-api-apps-response-example
- key_count: 1
  name: Partner Api Authentication Create Request Example
  slug: partner-api-authentication-create-request-example
- key_count: 5
  name: Partner Api Authentication Example
  slug: partner-api-authentication-example
- key_count: 3
  name: Partner Api Authentication Response Example
  slug: partner-api-authentication-response-example
- key_count: 3
  name: Partner Api Base Meta Example
  slug: partner-api-base-meta-example
- key_count: 4
  name: Partner Api Categories Response Example
  slug: partner-api-categories-response-example
- key_count: 1
  name: Partner Api Category Example
  slug: partner-api-category-example
- key_count: 4
  name: Partner Api Choice Example
  slug: partner-api-choice-example
- key_count: 2
  name: Partner Api Choice Params Example
  slug: partner-api-choice-params-example
- key_count: 1
  name: Partner Api Choice Request Example
  slug: partner-api-choice-request-example
- key_count: 3
  name: Partner Api Choice Response Example
  slug: partner-api-choice-response-example
- key_count: 2
  name: Partner Api Create Zap Request Example
  slug: partner-api-create-zap-request-example
- key_count: 4
  name: Partner Api Create Zap Request Step Example
  slug: partner-api-create-zap-request-step-example
- key_count: 3
  name: Partner Api Error Source Example
  slug: partner-api-error-source-example
- key_count: 3
  name: Partner Api Expanded Apps Response Example
  slug: partner-api-expanded-apps-response-example
- key_count: 8
  name: Partner Api Expanded Zap Example
  slug: partner-api-expanded-zap-example
- key_count: 4
  name: Partner Api Expanded Zap Step Example
  slug: partner-api-expanded-zap-step-example
- key_count: 3
  name: Partner Api Expanded Zaps Response Example
  slug: partner-api-expanded-zaps-response-example
- key_count: 4
  name: Partner Api Fieldset Example
  slug: partner-api-fieldset-example
- key_count: 3
  name: Partner Api Info Field Example
  slug: partner-api-info-field-example
- key_count: 12
  name: Partner Api Input Field Example
  slug: partner-api-input-field-example
- key_count: 3
  name: Partner Api Input Fields Response Example
  slug: partner-api-input-fields-response-example
- key_count: 1
  name: Partner Api Invalid Zap Guesser Response Example
  slug: partner-api-invalid-zap-guesser-response-example
- key_count: 2
  name: Partner Api Links Example
  slug: partner-api-links-example
- key_count: 1
  name: Partner Api List Input Fields Request Example
  slug: partner-api-list-input-fields-request-example
- key_count: 1
  name: Partner Api List Output Fields Request Example
  slug: partner-api-list-output-fields-request-example
- key_count: 1
  name: Partner Api Meta Example
  slug: partner-api-meta-example
- key_count: 4
  name: Partner Api Output Field Example
  slug: partner-api-output-field-example
- key_count: 3
  name: Partner Api Output Fields Response Example
  slug: partner-api-output-fields-response-example
- key_count: 7
  name: Partner Api Profile Example
  slug: partner-api-profile-example
- key_count: 1
  name: Partner Api Run Action Request Example
  slug: partner-api-run-action-request-example
- key_count: 1
  name: Partner Api Run Action Response Example
  slug: partner-api-run-action-response-example
- key_count: 8
  name: Partner Api Whitelabel App Example
  slug: partner-api-whitelabel-app-example
- key_count: 2
  name: Partner Api Whitelabel App Links Example
  slug: partner-api-whitelabel-app-links-example
- key_count: 3
  name: Partner Api Whitelabel Apps Response Example
  slug: partner-api-whitelabel-apps-response-example
- key_count: 6
  name: Partner Api Zap Example
  slug: partner-api-zap-example
- key_count: 3
  name: Partner Api Zap Guesser Raw Step Example
  slug: partner-api-zap-guesser-raw-step-example
- key_count: 1
  name: Partner Api Zap Guesser Request Example
  slug: partner-api-zap-guesser-request-example
- key_count: 4
  name: Partner Api Zap Guesser Response Example
  slug: partner-api-zap-guesser-response-example
- key_count: 2
  name: Partner Api Zap Guesser Step Example
  slug: partner-api-zap-guesser-step-example
- key_count: 1
  name: Partner Api Zap Request Example
  slug: partner-api-zap-request-example
- key_count: 9
  name: Partner Api Zap Run Example
  slug: partner-api-zap-run-example
- key_count: 2
  name: Partner Api Zap Run Step Example
  slug: partner-api-zap-run-step-example
- key_count: 3
  name: Partner Api Zap Runs Response Example
  slug: partner-api-zap-runs-response-example
- key_count: 10
  name: Partner Api Zap Step App Example
  slug: partner-api-zap-step-app-example
- key_count: 3
  name: Partner Api Zap Step Example
  slug: partner-api-zap-step-example
- key_count: 11
  name: Partner Api Zap Template Example
  slug: partner-api-zap-template-example
- key_count: 11
  name: Partner Api Zap Template Step Example
  slug: partner-api-zap-template-step-example
- key_count: 4
  name: Partner Api Zap Template Step Images Example
  slug: partner-api-zap-template-step-images-example
- key_count: 4
  name: Partner Api Zaps Response Example
  slug: partner-api-zaps-response-example
- key_count: 6
  name: Zapier Create Action Run Example
  slug: zapier-create-action-run-example
- key_count: 6
  name: Zapier Create Authentication Example
  slug: zapier-create-authentication-example
- key_count: 6
  name: Zapier Create Zap Guess Example
  slug: zapier-create-zap-guess-example
- key_count: 6
  name: Zapier Get Actions Example
  slug: zapier-get-actions-example
- key_count: 6
  name: Zapier Get Authentications Example
  slug: zapier-get-authentications-example
- key_count: 6
  name: Zapier Get Choices Example
  slug: zapier-get-choices-example
- key_count: 6
  name: Zapier Get Fields Inputs Example
  slug: zapier-get-fields-inputs-example
- key_count: 6
  name: Zapier Get Fields Outputs Example
  slug: zapier-get-fields-outputs-example
- key_count: 6
  name: Zapier Get V2 Apps Example
  slug: zapier-get-v2-apps-example
- key_count: 6
  name: Zapier Get V2 Zaps Example
  slug: zapier-get-v2-zaps-example
- key_count: 6
  name: Zapier Get Zap Runs Example
  slug: zapier-get-zap-runs-example
- key_count: 6
  name: Zapier Post Zaps Example
  slug: zapier-post-zaps-example
- key_count: 6
  name: Zapier Retrieve Action Run Example
  slug: zapier-retrieve-action-run-example
- key_count: 6
  name: Zapier Test Action Example
  slug: zapier-test-action-example
- key_count: 6
  name: Zapier V1 Apps List Example
  slug: zapier-v1-apps-list-example
- key_count: 6
  name: Zapier V1 Categories List Example
  slug: zapier-v1-categories-list-example
- key_count: 6
  name: Zapier V1 Profiles Me List Example
  slug: zapier-v1-profiles-me-list-example
- key_count: 6
  name: Zapier V1 Zap Templates List Example
  slug: zapier-v1-zap-templates-list-example
- key_count: 6
  name: Zapier V1 Zaps List Example
  slug: zapier-v1-zaps-list-example
- key_count: 6
  name: Zapier V2 Authorize List Example
  slug: zapier-v2-authorize-list-example
- key_count: 6
  name: Zapier V2 Whitelabel Apps List Example
  slug: zapier-v2-whitelabel-apps-list-example
features:
- 'Free: 100 tasks/mo, two-step Zaps, Copilot (daily limit)'
- 'Professional at $19.99/mo: multi-step Zaps, premium apps, webhooks'
- 'Team at $69/mo: 25 users, SAML SSO, shared Zaps'
- 'Enterprise custom: unlimited users, advanced admin, TAM'
- 8,000+ app integrations
- 'Polling intervals: 15min Free, 2min Pro, 1min Team/Enterprise'
- Task = one successful action in a Zap
- Webhooks (Pro+)
- Tables for data storage
- Forms for data capture
- Interfaces for app building (separate)
- Chatbots and AI assistants (separate)
- Zapier Copilot AI assistant
- Custom integrations via Developer Platform (Zapier CLI)
- Error handling, paths, filters, formatters
- Webhook payload size 10 MB
finops:
- name: Zapier Finops
  service_category: Workflow Automation
  slug: zapier-finops
graphqls:
- description: 'Zapier is an integration automation platform connecting 8,000+ apps through a workflow engine built around Zaps — automated workflows that watch for triggers in one app and execute actions in others. '
  name: Zapier GraphQL Schema
  slug: zapier-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zapier.png
json_schemas:
- name: _ActionRunResponseError
  property_count: 5
  slug: partner-api--action-run-response-error
- name: _ActionRunResponse
  property_count: 4
  slug: partner-api--action-run-response
- name: _ActionRunResponseStatusEnum
  property_count: 0
  slug: partner-api--action-run-response-status-enum
- name: _ActionTestRequest
  property_count: 4
  slug: partner-api--action-test-request
- name: _AuthenticationCreateRequest
  property_count: 3
  slug: partner-api--authentication-create-request
- name: _ListInputFieldsRequest
  property_count: 2
  slug: partner-api--list-input-fields-request
- name: _ListOutputFieldsRequest
  property_count: 3
  slug: partner-api--list-output-fields-request
- name: _RunActionRequest
  property_count: 3
  slug: partner-api--run-action-request
- name: _RunActionResponse
  property_count: 2
  slug: partner-api--run-action-response
- name: ActionRunResponse
  property_count: 1
  slug: partner-api-action-run-response
- name: Action
  property_count: 8
  slug: partner-api-action
- name: ActionTestRequest
  property_count: 1
  slug: partner-api-action-test-request
- name: ActionTestResponse
  property_count: 3
  slug: partner-api-action-test-response
- name: ActionTypeEnum
  property_count: 0
  slug: partner-api-action-type-enum
- name: ActionsResponse
  property_count: 3
  slug: partner-api-actions-response
- name: AppCategory
  property_count: 8
  slug: partner-api-app-category
- name: App
  property_count: 10
  slug: partner-api-app
- name: AppsImages
  property_count: 4
  slug: partner-api-apps-images
- name: AppsResponse
  property_count: 7
  slug: partner-api-apps-response
- name: Apps
  property_count: 10
  slug: partner-api-apps
- name: AuthenticationCreateRequest
  property_count: 1
  slug: partner-api-authentication-create-request
- name: AuthenticationResponse
  property_count: 3
  slug: partner-api-authentication-response
- name: Authentication
  property_count: 5
  slug: partner-api-authentication
- name: AuthenticationTypeEnum
  property_count: 0
  slug: partner-api-authentication-type-enum
- name: BaseMeta
  property_count: 3
  slug: partner-api-base-meta
- name: CategoriesResponse
  property_count: 4
  slug: partner-api-categories-response
- name: Category
  property_count: 1
  slug: partner-api-category
- name: ChoiceParams
  property_count: 2
  slug: partner-api-choice-params
- name: ChoiceRequest
  property_count: 1
  slug: partner-api-choice-request
- name: ChoiceResponse
  property_count: 3
  slug: partner-api-choice-response
- name: Choice
  property_count: 4
  slug: partner-api-choice
- name: CodeEnum
  property_count: 0
  slug: partner-api-code-enum
- name: CreateZapRequest
  property_count: 2
  slug: partner-api-create-zap-request
- name: CreateZapRequestStep
  property_count: 4
  slug: partner-api-create-zap-request-step
- name: ErrorSource
  property_count: 3
  slug: partner-api-error-source
- name: ExpandedAppsResponse
  property_count: 3
  slug: partner-api-expanded-apps-response
- name: ExpandedZap
  property_count: 8
  slug: partner-api-expanded-zap
- name: ExpandedZapStep
  property_count: 4
  slug: partner-api-expanded-zap-step
- name: ExpandedZapsResponse
  property_count: 3
  slug: partner-api-expanded-zaps-response
- name: FieldsetFieldsField
  property_count: 0
  slug: partner-api-fieldset-fields-field
- name: Fieldset
  property_count: 4
  slug: partner-api-fieldset
- name: FormatEnum
  property_count: 0
  slug: partner-api-format-enum
- name: InfoField
  property_count: 3
  slug: partner-api-info-field
- name: InputField
  property_count: 12
  slug: partner-api-input-field
- name: InputFieldsResponse
  property_count: 3
  slug: partner-api-input-fields-response
- name: InvalidZapGuesserResponse
  property_count: 1
  slug: partner-api-invalid-zap-guesser-response
- name: Links
  property_count: 2
  slug: partner-api-links
- name: ListInputFieldsRequest
  property_count: 1
  slug: partner-api-list-input-fields-request
- name: ListOutputFieldsRequest
  property_count: 1
  slug: partner-api-list-output-fields-request
- name: Meta
  property_count: 1
  slug: partner-api-meta
- name: OutputField
  property_count: 4
  slug: partner-api-output-field
- name: OutputFieldsResponse
  property_count: 3
  slug: partner-api-output-fields-response
- name: Profile
  property_count: 7
  slug: partner-api-profile
- name: RootFieldset
  property_count: 0
  slug: partner-api-root-fieldset
- name: RunActionRequest
  property_count: 1
  slug: partner-api-run-action-request
- name: RunActionResponse
  property_count: 1
  slug: partner-api-run-action-response
- name: RunTypeEnum
  property_count: 0
  slug: partner-api-run-type-enum
- name: TypeOfEnum
  property_count: 0
  slug: partner-api-type-of-enum
- name: ValueTypeEnum
  property_count: 0
  slug: partner-api-value-type-enum
- name: WhitelabelAppLinks
  property_count: 2
  slug: partner-api-whitelabel-app-links
- name: WhitelabelApp
  property_count: 8
  slug: partner-api-whitelabel-app
- name: WhitelabelAppsResponse
  property_count: 3
  slug: partner-api-whitelabel-apps-response
- name: ZapGuesserRawStep
  property_count: 3
  slug: partner-api-zap-guesser-raw-step
- name: ZapGuesserRequest
  property_count: 1
  slug: partner-api-zap-guesser-request
- name: ZapGuesserResponse
  property_count: 4
  slug: partner-api-zap-guesser-response
- name: ZapGuesserStep
  property_count: 2
  slug: partner-api-zap-guesser-step
- name: ZapRequest
  property_count: 1
  slug: partner-api-zap-request
- name: ZapRun
  property_count: 9
  slug: partner-api-zap-run
- name: ZapRunStep
  property_count: 2
  slug: partner-api-zap-run-step
- name: ZapRunsResponse
  property_count: 3
  slug: partner-api-zap-runs-response
- name: Zap
  property_count: 6
  slug: partner-api-zap
- name: ZapStepApp
  property_count: 10
  slug: partner-api-zap-step-app
- name: ZapStep
  property_count: 3
  slug: partner-api-zap-step
- name: ZapTemplate
  property_count: 11
  slug: partner-api-zap-template
- name: ZapTemplateStatusEnum
  property_count: 0
  slug: partner-api-zap-template-status-enum
- name: ZapTemplateStepImages
  property_count: 4
  slug: partner-api-zap-template-step-images
- name: ZapTemplateStep
  property_count: 11
  slug: partner-api-zap-template-step
- name: ZapsResponse
  property_count: 4
  slug: partner-api-zaps-response
- name: Action
  property_count: 8
  slug: zapier-action
- name: ActionRunResponse
  property_count: 1
  slug: zapier-actionrunresponse
- name: _ActionRunResponseError
  property_count: 5
  slug: zapier-actionrunresponseerror
- name: _ActionRunResponseStatusEnum
  property_count: 0
  slug: zapier-actionrunresponsestatusenum
- name: ActionsResponse
  property_count: 3
  slug: zapier-actionsresponse
- name: ActionTestRequest
  property_count: 1
  slug: zapier-actiontestrequest
- name: ActionTestResponse
  property_count: 3
  slug: zapier-actiontestresponse
- name: ActionTypeEnum
  property_count: 0
  slug: zapier-actiontypeenum
- name: App
  property_count: 10
  slug: zapier-app
- name: AppCategory
  property_count: 8
  slug: zapier-appcategory
- name: Apps
  property_count: 10
  slug: zapier-apps
- name: AppsImages
  property_count: 4
  slug: zapier-appsimages
- name: AppsResponse
  property_count: 7
  slug: zapier-appsresponse
- name: Authentication
  property_count: 5
  slug: zapier-authentication
- name: AuthenticationCreateRequest
  property_count: 1
  slug: zapier-authenticationcreaterequest
- name: AuthenticationResponse
  property_count: 3
  slug: zapier-authenticationresponse
- name: AuthenticationTypeEnum
  property_count: 0
  slug: zapier-authenticationtypeenum
- name: BaseMeta
  property_count: 3
  slug: zapier-basemeta
- name: CategoriesResponse
  property_count: 4
  slug: zapier-categoriesresponse
- name: Category
  property_count: 1
  slug: zapier-category
- name: Choice
  property_count: 4
  slug: zapier-choice
- name: ChoiceParams
  property_count: 2
  slug: zapier-choiceparams
- name: ChoiceRequest
  property_count: 1
  slug: zapier-choicerequest
- name: ChoiceResponse
  property_count: 3
  slug: zapier-choiceresponse
- name: CodeEnum
  property_count: 0
  slug: zapier-codeenum
- name: CreateZapRequest
  property_count: 2
  slug: zapier-createzaprequest
- name: CreateZapRequestStep
  property_count: 4
  slug: zapier-createzaprequeststep
- name: Error
  property_count: 6
  slug: zapier-error
- name: ErrorResponse
  property_count: 1
  slug: zapier-errorresponse
- name: ErrorSource
  property_count: 3
  slug: zapier-errorsource
- name: ExpandedAppsResponse
  property_count: 3
  slug: zapier-expandedappsresponse
- name: ExpandedZap
  property_count: 8
  slug: zapier-expandedzap
- name: ExpandedZapsResponse
  property_count: 3
  slug: zapier-expandedzapsresponse
- name: ExpandedZapStep
  property_count: 4
  slug: zapier-expandedzapstep
- name: Fieldset
  property_count: 4
  slug: zapier-fieldset
- name: FieldsetFieldsField
  property_count: 0
  slug: zapier-fieldsetfieldsfield
- name: FormatEnum
  property_count: 0
  slug: zapier-formatenum
- name: InfoField
  property_count: 3
  slug: zapier-infofield
- name: InputField
  property_count: 12
  slug: zapier-inputfield
- name: InputFieldsResponse
  property_count: 3
  slug: zapier-inputfieldsresponse
- name: InvalidZapGuesserResponse
  property_count: 1
  slug: zapier-invalidzapguesserresponse
- name: Links
  property_count: 2
  slug: zapier-links
- name: ListInputFieldsRequest
  property_count: 1
  slug: zapier-listinputfieldsrequest
- name: ListOutputFieldsRequest
  property_count: 1
  slug: zapier-listoutputfieldsrequest
- name: Meta
  property_count: 1
  slug: zapier-meta
- name: OutputField
  property_count: 4
  slug: zapier-outputfield
- name: OutputFieldsResponse
  property_count: 3
  slug: zapier-outputfieldsresponse
- name: Zapier Platform
  property_count: 0
  slug: zapier-platform
- name: Profile
  property_count: 7
  slug: zapier-profile
- name: RootFieldset
  property_count: 0
  slug: zapier-rootfieldset
- name: RunActionRequest
  property_count: 1
  slug: zapier-runactionrequest
- name: RunActionResponse
  property_count: 1
  slug: zapier-runactionresponse
- name: RunTypeEnum
  property_count: 0
  slug: zapier-runtypeenum
- name: TypeOfEnum
  property_count: 0
  slug: zapier-typeofenum
- name: ValueTypeEnum
  property_count: 0
  slug: zapier-valuetypeenum
- name: WhitelabelApp
  property_count: 8
  slug: zapier-whitelabelapp
- name: WhitelabelAppLinks
  property_count: 2
  slug: zapier-whitelabelapplinks
- name: WhitelabelAppsResponse
  property_count: 3
  slug: zapier-whitelabelappsresponse
- name: Zap
  property_count: 6
  slug: zapier-zap
- name: ZapGuesserRawStep
  property_count: 3
  slug: zapier-zapguesserrawstep
- name: ZapGuesserRequest
  property_count: 1
  slug: zapier-zapguesserrequest
- name: ZapGuesserResponse
  property_count: 4
  slug: zapier-zapguesserresponse
- name: ZapGuesserStep
  property_count: 2
  slug: zapier-zapguesserstep
- name: ZapRequest
  property_count: 1
  slug: zapier-zaprequest
- name: ZapRun
  property_count: 9
  slug: zapier-zaprun
- name: ZapRunsResponse
  property_count: 3
  slug: zapier-zaprunsresponse
- name: ZapRunStep
  property_count: 2
  slug: zapier-zaprunstep
- name: ZapsResponse
  property_count: 4
  slug: zapier-zapsresponse
- name: ZapStep
  property_count: 3
  slug: zapier-zapstep
- name: ZapStepApp
  property_count: 10
  slug: zapier-zapstepapp
- name: ZapTemplate
  property_count: 11
  slug: zapier-zaptemplate
- name: ZapTemplateStatusEnum
  property_count: 0
  slug: zapier-zaptemplatestatusenum
- name: ZapTemplateStep
  property_count: 11
  slug: zapier-zaptemplatestep
- name: ZapTemplateStepImages
  property_count: 4
  slug: zapier-zaptemplatestepimages
json_structures:
- name: Partner Api  Action Run Response Error Structure
  property_count: 5
  slug: partner-api--action-run-response-error-structure
- name: Partner Api  Action Run Response Status Enum Structure
  property_count: 0
  slug: partner-api--action-run-response-status-enum-structure
- name: Partner Api  Action Run Response Structure
  property_count: 4
  slug: partner-api--action-run-response-structure
- name: Partner Api  Action Test Request Structure
  property_count: 4
  slug: partner-api--action-test-request-structure
- name: Partner Api  Authentication Create Request Structure
  property_count: 3
  slug: partner-api--authentication-create-request-structure
- name: Partner Api  List Input Fields Request Structure
  property_count: 2
  slug: partner-api--list-input-fields-request-structure
- name: Partner Api  List Output Fields Request Structure
  property_count: 3
  slug: partner-api--list-output-fields-request-structure
- name: Partner Api  Run Action Request Structure
  property_count: 3
  slug: partner-api--run-action-request-structure
- name: Partner Api  Run Action Response Structure
  property_count: 2
  slug: partner-api--run-action-response-structure
- name: Partner Api Action Run Response Structure
  property_count: 1
  slug: partner-api-action-run-response-structure
- name: Partner Api Action Structure
  property_count: 8
  slug: partner-api-action-structure
- name: Partner Api Action Test Request Structure
  property_count: 1
  slug: partner-api-action-test-request-structure
- name: Partner Api Action Test Response Structure
  property_count: 3
  slug: partner-api-action-test-response-structure
- name: Partner Api Action Type Enum Structure
  property_count: 0
  slug: partner-api-action-type-enum-structure
- name: Partner Api Actions Response Structure
  property_count: 3
  slug: partner-api-actions-response-structure
- name: Partner Api App Category Structure
  property_count: 8
  slug: partner-api-app-category-structure
- name: Partner Api App Structure
  property_count: 10
  slug: partner-api-app-structure
- name: Partner Api Apps Images Structure
  property_count: 4
  slug: partner-api-apps-images-structure
- name: Partner Api Apps Response Structure
  property_count: 7
  slug: partner-api-apps-response-structure
- name: Partner Api Apps Structure
  property_count: 10
  slug: partner-api-apps-structure
- name: Partner Api Authentication Create Request Structure
  property_count: 1
  slug: partner-api-authentication-create-request-structure
- name: Partner Api Authentication Response Structure
  property_count: 3
  slug: partner-api-authentication-response-structure
- name: Partner Api Authentication Structure
  property_count: 5
  slug: partner-api-authentication-structure
- name: Partner Api Authentication Type Enum Structure
  property_count: 0
  slug: partner-api-authentication-type-enum-structure
- name: Partner Api Base Meta Structure
  property_count: 3
  slug: partner-api-base-meta-structure
- name: Partner Api Categories Response Structure
  property_count: 4
  slug: partner-api-categories-response-structure
- name: Partner Api Category Structure
  property_count: 1
  slug: partner-api-category-structure
- name: Partner Api Choice Params Structure
  property_count: 2
  slug: partner-api-choice-params-structure
- name: Partner Api Choice Request Structure
  property_count: 1
  slug: partner-api-choice-request-structure
- name: Partner Api Choice Response Structure
  property_count: 3
  slug: partner-api-choice-response-structure
- name: Partner Api Choice Structure
  property_count: 4
  slug: partner-api-choice-structure
- name: Partner Api Code Enum Structure
  property_count: 0
  slug: partner-api-code-enum-structure
- name: Partner Api Create Zap Request Step Structure
  property_count: 4
  slug: partner-api-create-zap-request-step-structure
- name: Partner Api Create Zap Request Structure
  property_count: 2
  slug: partner-api-create-zap-request-structure
- name: Partner Api Error Source Structure
  property_count: 3
  slug: partner-api-error-source-structure
- name: Partner Api Expanded Apps Response Structure
  property_count: 3
  slug: partner-api-expanded-apps-response-structure
- name: Partner Api Expanded Zap Step Structure
  property_count: 4
  slug: partner-api-expanded-zap-step-structure
- name: Partner Api Expanded Zap Structure
  property_count: 8
  slug: partner-api-expanded-zap-structure
- name: Partner Api Expanded Zaps Response Structure
  property_count: 3
  slug: partner-api-expanded-zaps-response-structure
- name: Partner Api Fieldset Fields Field Structure
  property_count: 0
  slug: partner-api-fieldset-fields-field-structure
- name: Partner Api Fieldset Structure
  property_count: 4
  slug: partner-api-fieldset-structure
- name: Partner Api Format Enum Structure
  property_count: 0
  slug: partner-api-format-enum-structure
- name: Partner Api Info Field Structure
  property_count: 3
  slug: partner-api-info-field-structure
- name: Partner Api Input Field Structure
  property_count: 12
  slug: partner-api-input-field-structure
- name: Partner Api Input Fields Response Structure
  property_count: 3
  slug: partner-api-input-fields-response-structure
- name: Partner Api Invalid Zap Guesser Response Structure
  property_count: 1
  slug: partner-api-invalid-zap-guesser-response-structure
- name: Partner Api Links Structure
  property_count: 2
  slug: partner-api-links-structure
- name: Partner Api List Input Fields Request Structure
  property_count: 1
  slug: partner-api-list-input-fields-request-structure
- name: Partner Api List Output Fields Request Structure
  property_count: 1
  slug: partner-api-list-output-fields-request-structure
- name: Partner Api Meta Structure
  property_count: 1
  slug: partner-api-meta-structure
- name: Partner Api Output Field Structure
  property_count: 4
  slug: partner-api-output-field-structure
- name: Partner Api Output Fields Response Structure
  property_count: 3
  slug: partner-api-output-fields-response-structure
- name: Partner Api Profile Structure
  property_count: 7
  slug: partner-api-profile-structure
- name: Partner Api Root Fieldset Structure
  property_count: 0
  slug: partner-api-root-fieldset-structure
- name: Partner Api Run Action Request Structure
  property_count: 1
  slug: partner-api-run-action-request-structure
- name: Partner Api Run Action Response Structure
  property_count: 1
  slug: partner-api-run-action-response-structure
- name: Partner Api Run Type Enum Structure
  property_count: 0
  slug: partner-api-run-type-enum-structure
- name: Partner Api Type Of Enum Structure
  property_count: 0
  slug: partner-api-type-of-enum-structure
- name: Partner Api Value Type Enum Structure
  property_count: 0
  slug: partner-api-value-type-enum-structure
- name: Partner Api Whitelabel App Links Structure
  property_count: 2
  slug: partner-api-whitelabel-app-links-structure
- name: Partner Api Whitelabel App Structure
  property_count: 8
  slug: partner-api-whitelabel-app-structure
- name: Partner Api Whitelabel Apps Response Structure
  property_count: 3
  slug: partner-api-whitelabel-apps-response-structure
- name: Partner Api Zap Guesser Raw Step Structure
  property_count: 3
  slug: partner-api-zap-guesser-raw-step-structure
- name: Partner Api Zap Guesser Request Structure
  property_count: 1
  slug: partner-api-zap-guesser-request-structure
- name: Partner Api Zap Guesser Response Structure
  property_count: 4
  slug: partner-api-zap-guesser-response-structure
- name: Partner Api Zap Guesser Step Structure
  property_count: 2
  slug: partner-api-zap-guesser-step-structure
- name: Partner Api Zap Request Structure
  property_count: 1
  slug: partner-api-zap-request-structure
- name: Partner Api Zap Run Step Structure
  property_count: 2
  slug: partner-api-zap-run-step-structure
- name: Partner Api Zap Run Structure
  property_count: 9
  slug: partner-api-zap-run-structure
- name: Partner Api Zap Runs Response Structure
  property_count: 3
  slug: partner-api-zap-runs-response-structure
- name: Partner Api Zap Step App Structure
  property_count: 10
  slug: partner-api-zap-step-app-structure
- name: Partner Api Zap Step Structure
  property_count: 3
  slug: partner-api-zap-step-structure
- name: Partner Api Zap Structure
  property_count: 6
  slug: partner-api-zap-structure
- name: Partner Api Zap Template Status Enum Structure
  property_count: 0
  slug: partner-api-zap-template-status-enum-structure
- name: Partner Api Zap Template Step Images Structure
  property_count: 4
  slug: partner-api-zap-template-step-images-structure
- name: Partner Api Zap Template Step Structure
  property_count: 11
  slug: partner-api-zap-template-step-structure
- name: Partner Api Zap Template Structure
  property_count: 11
  slug: partner-api-zap-template-structure
- name: Partner Api Zaps Response Structure
  property_count: 4
  slug: partner-api-zaps-response-structure
- name: Zapier Platform Structure
  property_count: 0
  slug: zapier-platform-structure
- name: Zapier Structure
  property_count: 0
  slug: zapier-structure
jsonld:
- class_count: 72
  name: Zapier Partner Api Context
  property_count: 95
  slug: zapier-partner-api-context
- class_count: 0
  name: Zapier Zapier Context
  property_count: 0
  slug: zapier-zapier-context
layout: provider
mcp_servers:
- description: ''
  name: zapier-mcp.yml
  slug: zapier-mcpyml
modified: '2026-06-20'
name: Zapier
nav: Providers
network: true
overview: 'Zapier publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Actions API, Apps API, and 7 more. Tagged areas include Integrations and iPaaS.


  The Zapier catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  Zapier''s developer surface includes authentication, changelog, CLI, sandbox, engineering blog, support, documentation, and 51 more developer resources.'
plans:
- name: Zapier Plans Pricing
  plan_count: 4
  slug: zapier-plans-pricing
random_paper: 55
rate_limits:
- limit_count: 5
  name: Zapier Rate Limits
  slug: zapier-rate-limits
rules:
- name: Zapier API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: zapier-jsonschema-spectral-rules
- name: Zapier API Rules
  rule_count: 18
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 13
  slug: zapier-rules
scopes:
- name: Zapier Scopes
  scope_count: 10
  slug: zapier-scopes
  summary_line: 10 scopes · authorizationCode/implicit
score:
  band: exemplar
  composite: 70.9
  delta: 0.0
  facets:
    commercial_clarity: 68.4
    contract_quality: 75.9
    developer_ergonomics: 71.7
    discoverability: 74.1
    governance: 80.2
    operational_transparency: 52.6
  previous_composite: 70.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zapier/refs/heads/main/screenshots/zapier-2026-06-20T201801.png
security:
- kind: authentication
  name: Zapier Authentication
  slug: zapier-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Zapier Domain Security
  slug: zapier-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Zapier Trust Center
  slug: zapier-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, HIPAA, FedRAMP, GDPR, CSA STAR
slug: zapier
tags:
- Integrations
- iPaaS
use_cases:
- name: Customer support
- name: Data management
- name: Lead management
- name: Marketing campaigns
- name: Project management
- name: Sales pipeline
- name: Tickets and incidents
website: https://zapier.com/
---
