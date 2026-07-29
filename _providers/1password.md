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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 54.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: 1Password Agentic Access
  operation_count: 23
  slug: 1password-agentic-access
  summary_line: 23 operations · 10 acting
api_count: 11
apis:
- description: Operations for managing partner billing accounts for customers, including creating, retrieving, updating, and deleting billing accounts.
  name: 1Password Accounts API
  slug: 1password-accounts-api
- description: Operations for listing API requests made to the Connect server.
  name: 1Password Activity API
  slug: 1password-activity-api
- description: Retrieve information about actions performed by team members within a 1Password account, including when an action was performed and by whom, along with details about the type and object of the action.
  name: 1Password Audit Events API
  slug: 1password-audit-events-api
- description: Operations for listing and retrieving files attached to items.
  name: 1Password Files API
  slug: 1password-files-api
- description: Operations for checking the health and status of the Connect server.
  name: 1Password Health API
  slug: 1password-health-api
- description: Retrieve information about the authentication token being used, including its features and permissions.
  name: 1Password Introspection API
  slug: 1password-introspection-api
- description: Retrieve information about items in shared vaults that have been modified, accessed, or used, including the user who accessed the item, when it was accessed, and the vault where the item is stored.
  name: 1Password Item Usages API
  slug: 1password-item-usages-api
- description: Operations for creating, reading, updating, and deleting items within vaults.
  name: 1Password Items API
  slug: 1password-items-api
- description: Operations for retrieving Prometheus-style metrics from the Connect server.
  name: 1Password Metrics API
  slug: 1password-metrics-api
- description: 'Retrieve information about sign-in attempts to 1Password accounts, including the name and IP address of the user who attempted to sign in, when the attempt was made, and for failed attempts the cause '
  name: 1Password Sign-In Attempts API
  slug: 1password-sign-in-attempts-api
- description: Operations for listing and retrieving vaults available to the Connect server.
  name: 1Password Vaults API
  slug: 1password-vaults-api
arazzos:
- description: Confirm an item exists, then permanently delete it from its vault.
  name: 1Password Decommission an Item
  slug: 1password-decommission-item-workflow
- description: Read an item, list its attached files, select one by name, and download its content.
  name: 1Password Download an Item File
  slug: 1password-download-item-file-workflow
- description: Create a new item in a vault and read it back to confirm it was stored.
  name: 1Password Provision an Item
  slug: 1password-provision-item-workflow
- description: Create a customer partner billing account, read it back, then schedule its end date.
  name: 1Password Provision Partner Billing
  slug: 1password-provision-partner-billing-workflow
- description: Resolve a vault, locate an item by title, and read its full field values.
  name: 1Password Read an Item Secret
  slug: 1password-read-item-secret-workflow
- description: Read an item, then apply a JSON Patch to replace its password field value.
  name: 1Password Rotate an Item Password
  slug: 1password-rotate-item-password-workflow
- description: Validate the Events token, open an audit event feed from a start time, then page with the cursor.
  name: 1Password Stream Audit Events
  slug: 1password-stream-audit-events-workflow
- description: Open an item usage feed from a start time, then continue paging with the cursor while more remain.
  name: 1Password Stream Item Usages
  slug: 1password-stream-item-usages-workflow
artifact_total: 148
collections:
- collection_type: postman
  name: 1Password Connect Server API
  slug: postman-1password-connect
- collection_type: postman
  name: 1Password Events API
  slug: postman-1password-events
- collection_type: postman
  name: 1Password Partnership API
  slug: postman-1password-partnership
- collection_type: open
  name: 1Password Connect Server API
  slug: open-1password-connect
- collection_type: open
  name: 1Password Events API
  slug: open-1password-events
- collection_type: open
  name: 1Password Partnership API
  slug: open-1password-partnership
common:
- group: build
  title: ''
  type: Packages
  url: packages/1password-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/1password-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/1password-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/1password-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/1password-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/1password-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/1password-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/1password-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/1password-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/1password-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/1password-cli.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/1password-data-model.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/1password-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/1password-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/1password-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/1password-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/1password-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/1password/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/1password-decommission-item-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/1password-download-item-file-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/1password-provision-item-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/1password-provision-partner-billing-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/1password-read-item-secret-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/1password-rotate-item-password-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/1password-stream-audit-events-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/1password-stream-item-usages-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/1password
- group: company
  title: ''
  type: Website
  url: https://1password.com/
- group: start
  title: ''
  type: Portal
  url: https://developer.1password.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.1password.com/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.1password.com/docs/get-started/
- group: auth
  title: ''
  type: Authentication
  url: https://developer.1password.com/docs/connect/connect-api-reference/#authentication
- group: build
  title: Official SDKs
  type: SDKs
  url: https://developer.1password.com/docs/sdks/
- group: build
  title: Python SDK
  type: SDKs
  url: https://pypi.org/project/onepassword-sdk/
- group: build
  title: JavaScript SDK
  type: SDKs
  url: https://www.npmjs.com/package/@1password/sdk
- group: build
  title: Go SDK
  type: SDKs
  url: https://pkg.go.dev/github.com/1Password/onepassword-sdk-go
- group: build
  title: Connect Python SDK
  type: SDKs
  url: https://pypi.org/project/onepassword-connect-sdk/
- group: build
  title: Connect Node.js SDK
  type: SDKs
  url: https://www.npmjs.com/package/@1password/connect
- group: build
  title: Connect Go SDK
  type: SDKs
  url: https://pkg.go.dev/github.com/1Password/connect-sdk-go
- group: build
  title: 1Password CLI
  type: CLI
  url: https://developer.1password.com/docs/cli/
- group: company
  title: ''
  type: Blog
  url: https://blog.1password.com/
- group: operate
  title: ''
  type: Support
  url: https://support.1password.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://1password.com/legal/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://1password.com/legal/terms-of-service/
- group: start
  title: ''
  type: Signup
  url: https://start.1password.com/sign-up/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.1password.com/docs/events-api/changelog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/1Password
- group: design
  title: ''
  type: SpectralRules
  url: rules/1password-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/1password-vocabulary.yaml
created: '2025-02-08'
description: 1Password is a password manager that helps individuals and businesses securely store and manage passwords, credentials, and sensitive information. The platform provides a Connect Server API for programmatic secrets management, an Events API for security monitoring and audit logging, and a Partnership API for managing partner billing accounts.
examples:
- key_count: 6
  name: 1Password Connect Api Request Example
  slug: 1password-connect-api-request-example
- key_count: 9
  name: 1Password Connect Field Example
  slug: 1password-connect-field-example
- key_count: 6
  name: 1Password Connect File Example
  slug: 1password-connect-file-example
- key_count: 0
  name: 1Password Connect Full Item Example
  slug: 1password-connect-full-item-example
- key_count: 3
  name: 1Password Connect Generator Recipe Example
  slug: 1password-connect-generator-recipe-example
- key_count: 12
  name: 1Password Connect Item Example
  slug: 1password-connect-item-example
- key_count: 0
  name: 1Password Connect Json Patch Example
  slug: 1password-connect-json-patch-example
- key_count: 2
  name: 1Password Connect Section Example
  slug: 1password-connect-section-example
- key_count: 1
  name: 1Password Connect Section Ref Example
  slug: 1password-connect-section-ref-example
- key_count: 3
  name: 1Password Connect Server Health Example
  slug: 1password-connect-server-health-example
- key_count: 2
  name: 1Password Connect Url Example
  slug: 1password-connect-url-example
- key_count: 9
  name: 1Password Connect Vault Example
  slug: 1password-connect-vault-example
- key_count: 1
  name: 1Password Connect Vault Ref Example
  slug: 1password-connect-vault-ref-example
- key_count: 0
  name: 1Password Event Example
  slug: 1password-event-example
- key_count: 14
  name: 1Password Events Audit Event Example
  slug: 1password-events-audit-event-example
- key_count: 3
  name: 1Password Events Audit Event Response Example
  slug: 1password-events-audit-event-response-example
- key_count: 7
  name: 1Password Events Event Client Example
  slug: 1password-events-event-client-example
- key_count: 5
  name: 1Password Events Event Location Example
  slug: 1password-events-event-location-example
- key_count: 3
  name: 1Password Events Event Request Example
  slug: 1password-events-event-request-example
- key_count: 3
  name: 1Password Events Event User Example
  slug: 1password-events-event-user-example
- key_count: 9
  name: 1Password Events Item Usage Example
  slug: 1password-events-item-usage-example
- key_count: 3
  name: 1Password Events Item Usage Response Example
  slug: 1password-events-item-usage-response-example
- key_count: 8
  name: 1Password Events Sign In Attempt Example
  slug: 1password-events-sign-in-attempt-example
- key_count: 3
  name: 1Password Events Sign In Attempt Response Example
  slug: 1password-events-sign-in-attempt-response-example
- key_count: 2
  name: 1Password Events Token Introspection Example
  slug: 1password-events-token-introspection-example
- key_count: 14
  name: 1Password Item Example
  slug: 1password-item-example
- key_count: 7
  name: 1Password Partnership Account Example
  slug: 1password-partnership-account-example
- key_count: 4
  name: 1Password Partnership Create Account Request Example
  slug: 1password-partnership-create-account-request-example
- key_count: 1
  name: 1Password Partnership Update Account Request Example
  slug: 1password-partnership-update-account-request-example
features:
- description: Programmatic access to 1Password vaults and items via Connect Server API
  name: Secrets Management
- description: Real-time audit log streaming of sign-in events, item usage, and audit trails
  name: Security Monitoring
- description: Provision and deprovision 1Password accounts for partner customers
  name: Partner Billing Management
- description: Official SDKs for Python, JavaScript/TypeScript, Go, and Connect-specific clients
  name: SDKs
- description: 1Password CLI for command-line secrets management and automation
  name: CLI
- description: Kubernetes operator and secrets injector for cloud-native deployments
  name: Kubernetes Integration
- description: Terraform provider to manage 1Password vault items as infrastructure
  name: Terraform Provider
- description: Load secrets from 1Password directly into GitHub Actions CI/CD pipelines
  name: GitHub Actions
finops:
- name: 1Password Finops
  service_category: Identity
  slug: 1password-finops
image: /assets/icons/1password.png
integrations:
- description: Native integration via operator and secrets injector for Kubernetes deployments
  name: Kubernetes
- description: Terraform provider for managing 1Password items as infrastructure resources
  name: Terraform
- description: Ansible collection for 1Password Connect integration
  name: Ansible
- description: GitHub Actions to load and install 1Password secrets in CI/CD workflows
  name: GitHub Actions
- description: Events API Splunk integration for security event streaming
  name: Splunk
- description: Vault plugin for 1Password Connect secrets retrieval
  name: HashiCorp Vault
- description: Official Helm charts for deploying 1Password Connect on Kubernetes
  name: Helm Charts
json_schemas:
- name: APIRequest
  property_count: 6
  slug: 1password-connect-api-request
- name: Field
  property_count: 9
  slug: 1password-connect-field
- name: File
  property_count: 6
  slug: 1password-connect-file
- name: FullItem
  property_count: 0
  slug: 1password-connect-full-item
- name: GeneratorRecipe
  property_count: 3
  slug: 1password-connect-generator-recipe
- name: Item
  property_count: 12
  slug: 1password-connect-item
- name: JsonPatch
  property_count: 0
  slug: 1password-connect-json-patch
- name: SectionRef
  property_count: 1
  slug: 1password-connect-section-ref
- name: Section
  property_count: 2
  slug: 1password-connect-section
- name: ServerHealth
  property_count: 3
  slug: 1password-connect-server-health
- name: Url
  property_count: 2
  slug: 1password-connect-url
- name: VaultRef
  property_count: 1
  slug: 1password-connect-vault-ref
- name: Vault
  property_count: 9
  slug: 1password-connect-vault
- name: 1Password Event
  property_count: 0
  slug: 1password-event
- name: AuditEventResponse
  property_count: 3
  slug: 1password-events-audit-event-response
- name: AuditEvent
  property_count: 14
  slug: 1password-events-audit-event
- name: EventClient
  property_count: 7
  slug: 1password-events-event-client
- name: EventLocation
  property_count: 5
  slug: 1password-events-event-location
- name: EventRequest
  property_count: 3
  slug: 1password-events-event-request
- name: EventUser
  property_count: 3
  slug: 1password-events-event-user
- name: ItemUsageResponse
  property_count: 3
  slug: 1password-events-item-usage-response
- name: ItemUsage
  property_count: 9
  slug: 1password-events-item-usage
- name: SignInAttemptResponse
  property_count: 3
  slug: 1password-events-sign-in-attempt-response
- name: SignInAttempt
  property_count: 8
  slug: 1password-events-sign-in-attempt
- name: TokenIntrospection
  property_count: 2
  slug: 1password-events-token-introspection
- name: 1Password Item
  property_count: 14
  slug: 1password-item
- name: Account
  property_count: 7
  slug: 1password-partnership-account
- name: CreateAccountRequest
  property_count: 4
  slug: 1password-partnership-create-account-request
- name: UpdateAccountRequest
  property_count: 1
  slug: 1password-partnership-update-account-request
json_structures:
- name: 1Password Connect Api Request Structure
  property_count: 6
  slug: 1password-connect-api-request-structure
- name: 1Password Connect Field Structure
  property_count: 9
  slug: 1password-connect-field-structure
- name: 1Password Connect File Structure
  property_count: 6
  slug: 1password-connect-file-structure
- name: 1Password Connect Full Item Structure
  property_count: 0
  slug: 1password-connect-full-item-structure
- name: 1Password Connect Generator Recipe Structure
  property_count: 3
  slug: 1password-connect-generator-recipe-structure
- name: 1Password Connect Item Structure
  property_count: 12
  slug: 1password-connect-item-structure
- name: 1Password Connect Json Patch Structure
  property_count: 0
  slug: 1password-connect-json-patch-structure
- name: 1Password Connect Section Ref Structure
  property_count: 1
  slug: 1password-connect-section-ref-structure
- name: 1Password Connect Section Structure
  property_count: 2
  slug: 1password-connect-section-structure
- name: 1Password Connect Server Health Structure
  property_count: 3
  slug: 1password-connect-server-health-structure
- name: 1Password Connect Url Structure
  property_count: 2
  slug: 1password-connect-url-structure
- name: 1Password Connect Vault Ref Structure
  property_count: 1
  slug: 1password-connect-vault-ref-structure
- name: 1Password Connect Vault Structure
  property_count: 9
  slug: 1password-connect-vault-structure
- name: 1Password Event Structure
  property_count: 0
  slug: 1password-event-structure
- name: 1Password Events Audit Event Response Structure
  property_count: 3
  slug: 1password-events-audit-event-response-structure
- name: 1Password Events Audit Event Structure
  property_count: 14
  slug: 1password-events-audit-event-structure
- name: 1Password Events Event Client Structure
  property_count: 7
  slug: 1password-events-event-client-structure
- name: 1Password Events Event Location Structure
  property_count: 5
  slug: 1password-events-event-location-structure
- name: 1Password Events Event Request Structure
  property_count: 3
  slug: 1password-events-event-request-structure
- name: 1Password Events Event User Structure
  property_count: 3
  slug: 1password-events-event-user-structure
- name: 1Password Events Item Usage Response Structure
  property_count: 3
  slug: 1password-events-item-usage-response-structure
- name: 1Password Events Item Usage Structure
  property_count: 9
  slug: 1password-events-item-usage-structure
- name: 1Password Events Sign In Attempt Response Structure
  property_count: 3
  slug: 1password-events-sign-in-attempt-response-structure
- name: 1Password Events Sign In Attempt Structure
  property_count: 8
  slug: 1password-events-sign-in-attempt-structure
- name: 1Password Events Token Introspection Structure
  property_count: 2
  slug: 1password-events-token-introspection-structure
- name: 1Password Item Structure
  property_count: 14
  slug: 1password-item-structure
- name: 1Password Partnership Account Structure
  property_count: 7
  slug: 1password-partnership-account-structure
- name: 1Password Partnership Create Account Request Structure
  property_count: 4
  slug: 1password-partnership-create-account-request-structure
- name: 1Password Partnership Update Account Request Structure
  property_count: 1
  slug: 1password-partnership-update-account-request-structure
jsonld:
- class_count: 15
  name: 1Password Connect Context
  property_count: 46
  slug: 1password-connect-context
- class_count: 0
  name: 1Password Context
  property_count: 8
  slug: 1password-context
- class_count: 13
  name: 1Password Events Context
  property_count: 43
  slug: 1password-events-context
- class_count: 4
  name: 1Password Partnership Context
  property_count: 6
  slug: 1password-partnership-context
layout: provider
mcp_servers:
- description: ''
  name: 1password-mcp.yml
  slug: 1password-mcpyml
modified: '2026-06-20'
name: 1Password
nav: Providers
network: true
overview: '1Password publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Activity API, Audit Events API, and 8 more. Tagged areas include Password Manager, Passwords, Security, and Secrets.


  The 1Password catalog on APIs.io includes 4 JSON-LD contexts and 2 Spectral governance rulesets.


  1Password''s developer surface includes changelog, CLI, authentication, developer portal, documentation, getting-started guide, engineering blog, and 42 more developer resources.'
plans:
- name: 1Password Plans Pricing
  plan_count: 5
  slug: 1password-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 4
  name: 1Password Rate Limits
  slug: 1password-rate-limits
rules:
- name: 1Password API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: 1password-jsonschema-spectral-rules
- name: 1Password API Rules
  rule_count: 30
  severity_counts:
    error: 13
    hint: 0
    info: 6
    warn: 11
  slug: 1password-spectral-rules
score:
  band: exemplar
  composite: 71.7
  delta: -1.8
  facets:
    commercial_clarity: 68.4
    contract_quality: 72.4
    developer_ergonomics: 80.4
    discoverability: 74.1
    governance: 80.2
    operational_transparency: 52.6
  previous_composite: 73.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/1password/refs/heads/main/screenshots/1password-2026-06-20T162519.png
security:
- kind: authentication
  name: 1Password Authentication
  slug: 1password-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: 1Password Domain Security
  slug: 1password-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: 1Password Vulnerability Disclosure
  slug: 1password-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: 1Password Trust Center
  slug: 1password-trust-center
  summary_line: SOC 2
slug: 1password
tags:
- Password Manager
- Passwords
- Security
- Secrets
use_cases:
- description: Inject secrets from 1Password into applications and containers at runtime
  name: Secrets Injection
- description: Stream and analyze sign-in events and item usage for security incident response
  name: Security Audit
- description: Export audit trails for SOC2, GDPR, and other compliance frameworks
  name: Compliance Reporting
- description: Securely provide secrets to CI/CD pipelines without hardcoding credentials
  name: CI/CD Secrets
- description: Manage secrets as part of Terraform or Ansible automation workflows
  name: Infrastructure as Code
- description: Automate provisioning of 1Password accounts for partner customer bases
  name: Partner Account Provisioning
website: https://1password.com/
---
