---
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.7
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 71
  human_in_the_loop: 3
  name: Firma Dev Agentic Access
  operation_count: 115
  slug: firma-dev-agentic-access
  summary_line: 115 operations · 71 acting · 3 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.firma.dev/functions/v1/signing-request-api
  baseurl_source: spec
  description: Company information and settings
  name: Firma.dev Company API
  slug: firma-dev-company-api
- baseURL: https://api.firma.dev/functions/v1/signing-request-api
  baseurl_source: spec
  description: Custom field definition management for workspaces, templates, and signing requests
  name: Firma.dev Custom Fields API
  slug: firma-dev-custom-fields-api
- baseURL: https://api.firma.dev/functions/v1/signing-request-api
  baseurl_source: spec
  description: Email domain setup and verification for sending signing request emails from custom domains
  name: Firma.dev Email Domains API
  slug: firma-dev-email-domains-api
- baseURL: https://api.firma.dev/functions/v1/signing-request-api
  baseurl_source: spec
  description: Email template management for workspace and company-level customization of signing request notifications
  name: Firma.dev Email Templates API
  slug: firma-dev-email-templates-api
- baseURL: https://api.firma.dev/functions/v1/signing-request-api
  baseurl_source: spec
  description: JWT token generation and revocation for embedded templates
  name: Firma.dev JWT Management API
  slug: firma-dev-jwt-management-api
- baseURL: https://api.firma.dev/functions/v1/signing-request-api
  baseurl_source: spec
  description: 'Organization seal management: create, update, revoke, and erase seals applied to signing requests'
  name: Firma.dev Organization Seals API
  slug: firma-dev-organization-seals-api
- baseURL: https://api.firma.dev/functions/v1/signing-request-api
  baseurl_source: spec
  description: Custom signer terms-of-service / consent statements, company-level with per-language workspace overrides
  name: Firma.dev Signer Terms API
  slug: firma-dev-signer-terms-api
- baseURL: https://api.firma.dev/functions/v1/signing-request-api
  baseurl_source: spec
  description: Document signing request operations
  name: Firma.dev Signing Requests API
  slug: firma-dev-signing-requests-api
- baseURL: https://api.firma.dev/functions/v1/signing-request-api
  baseurl_source: spec
  description: Template management operations
  name: Firma.dev Templates API
  slug: firma-dev-templates-api
- baseURL: https://api.firma.dev/functions/v1/signing-request-api
  baseurl_source: spec
  description: Webhook configuration and management
  name: Firma.dev Webhooks API
  slug: firma-dev-webhooks-api
- baseURL: https://api.firma.dev/functions/v1/signing-request-api
  baseurl_source: spec
  description: Workspace configuration and settings
  name: Firma.dev Workspace Settings API
  slug: firma-dev-workspace-settings-api
- baseURL: https://api.firma.dev/functions/v1/signing-request-api
  baseurl_source: spec
  description: Workspace management operations
  name: Firma.dev Workspaces API
  slug: firma-dev-workspaces-api
artifact_total: 78
common:
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/firma-dev/refs/heads/main/mcp/firma-dev-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/firma-dev-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/firma-dev/refs/heads/main/agentic-access/firma-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/firma-dev-agentic-access.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/firma-dev/refs/heads/main/plans/firma-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/firma-dev-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/firma-dev/refs/heads/main/rules/firma-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/firma-dev-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/firma-dev/refs/heads/main/json-ld/firma-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/firma-dev-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/firma-dev/refs/heads/main/vocabulary/firma-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/firma-dev-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/firma-dev/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/firma-dev/refs/heads/main/data-model/firma-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/firma-dev-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://firma.dev/trust
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/firma-dev/refs/heads/main/errors/firma-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/firma-dev-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/firma-dev/refs/heads/main/conformance/firma-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/firma-dev-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/firma-dev/refs/heads/main/llms/firma-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/firma-dev-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/firma-dev/refs/heads/main/a2a/firma-dev-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/firma-dev-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/firma-dev/refs/heads/main/mcp/firma-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/firma-dev-mcp.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/firma-dev/refs/heads/main/hosts/firma-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/firma-dev-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/firma-dev/refs/heads/main/vendors/firma-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/firma-dev-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://firma.dev/legal/terms-conditions
- group: operate
  title: ''
  type: StatusPage
  url: https://status.firma.dev/
- group: auth
  title: ''
  type: Security
  url: https://firma.dev/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://firma.dev/legal/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://firma.dev/media
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/firma-dev/refs/heads/main/authentication/firma-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/firma-dev-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/firma-dev/refs/heads/main/security/firma-dev-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/firma-dev-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/firma-dev/refs/heads/main/security/firma-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/firma-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://firma.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.firma.dev/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.firma.dev/api-reference/v01.38.00/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.firma.dev/guides/complete-setup-guide
- group: commercial
  title: ''
  type: Pricing
  url: https://firma.dev/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.firma.dev/signup
- group: operate
  title: ''
  type: Support
  url: https://firma.dev/contact
- group: company
  title: ''
  type: Blog
  url: https://firma.dev/insights
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/firma-dev/workspace
created: '2026-09-25'
description: Firma.dev provides a low‑cost electronic signature API aimed at developers, offering pay‑as‑you‑go pricing starting at €0.049 per envelope with no minimums or contracts. The platform is fully white‑labeled, compliant with ESIGN, UETA, eIDAS, and includes audit trails, SOC 2, GDPR, ISO 27001 certifications. It offers a simple REST API, Swagger/OpenAPI docs, webhook events, and sample apps, targeting quick integration for any language. Firma.dev also supplies a developer portal, pricing page, and extensive documentation for embedding e‑signatures directly into applications.
image: https://framerusercontent.com/assets/6BZ6uZhXFZ37plllWJaDRaNVyoo.png
json_schemas:
- name: AnchorTag
  property_count: 25
  slug: firma-dev-anchor-tag
- name: ApiKeyExpireResponse
  property_count: 4
  slug: firma-dev-api-key-expire-response
- name: ApiKeyRegenerateResponse
  property_count: 4
  slug: firma-dev-api-key-regenerate-response
- name: CompanyEmailTemplateListResponse
  property_count: 1
  slug: firma-dev-company-email-template-list-response
- name: Company
  property_count: 10
  slug: firma-dev-company
- name: CompanySettings
  property_count: 27
  slug: firma-dev-company-settings
- name: ConditionSet
  property_count: 2
  slug: firma-dev-condition-set
- name: CustomFieldListResponse
  property_count: 1
  slug: firma-dev-custom-field-list-response
- name: DomainCreateResponse
  property_count: 2
  slug: firma-dev-domain-create-response
- name: DomainFinalizeResponse
  property_count: 4
  slug: firma-dev-domain-finalize-response
- name: DomainListResponse
  property_count: 2
  slug: firma-dev-domain-list-response
- name: Domain
  property_count: 10
  slug: firma-dev-domain
- name: DomainVerifyDnsResponse
  property_count: 4
  slug: firma-dev-domain-verify-dns-response
- name: DomainVerifyOwnershipResponse
  property_count: 3
  slug: firma-dev-domain-verify-ownership-response
- name: EmailTemplateDefaultsResponse
  property_count: 2
  slug: firma-dev-email-template-defaults-response
- name: EmailTemplateDeleteResponse
  property_count: 2
  slug: firma-dev-email-template-delete-response
- name: EmailTemplatePlaceholdersResponse
  property_count: 1
  slug: firma-dev-email-template-placeholders-response
- name: EmailTemplate
  property_count: 6
  slug: firma-dev-email-template
- name: Field
  property_count: 22
  slug: firma-dev-field
- name: GenerateJWTRequest
  property_count: 1
  slug: firma-dev-generate-jwtrequest
- name: GenerateSigningRequestJWTRequest
  property_count: 1
  slug: firma-dev-generate-signing-request-jwtrequest
- name: GenerateSigningRequestJWTResponse
  property_count: 5
  slug: firma-dev-generate-signing-request-jwtresponse
- name: GenerateTemplateTokenResponse
  property_count: 3
  slug: firma-dev-generate-template-token-response
- name: LogoDeleteResponse
  property_count: 1
  slug: firma-dev-logo-delete-response
- name: LogoUploadResponse
  property_count: 2
  slug: firma-dev-logo-upload-response
- name: MessageResponse
  property_count: 1
  slug: firma-dev-message-response
- name: OrganizationSealCreate
  property_count: 10
  slug: firma-dev-organization-seal-create
- name: OrganizationSeal
  property_count: 19
  slug: firma-dev-organization-seal
- name: Recipient
  property_count: 17
  slug: firma-dev-recipient
- name: Reminder
  property_count: 10
  slug: firma-dev-reminder
- name: RevokeJWTResponse
  property_count: 3
  slug: firma-dev-revoke-jwtresponse
- name: RevokeSigningRequestJWTResponse
  property_count: 3
  slug: firma-dev-revoke-signing-request-jwtresponse
- name: RotateSecretResponse
  property_count: 4
  slug: firma-dev-rotate-secret-response
- name: SealAccessLogEntry
  property_count: 7
  slug: firma-dev-seal-access-log-entry
- name: SealApplication
  property_count: 8
  slug: firma-dev-seal-application
- name: SealImage
  property_count: 3
  slug: firma-dev-seal-image
- name: SealStatement
  property_count: 6
  slug: firma-dev-seal-statement
- name: SecretStatusResponse
  property_count: 4
  slug: firma-dev-secret-status-response
- name: SignerTermsDeleteResponse
  property_count: 2
  slug: firma-dev-signer-terms-delete-response
- name: SignerTermsListResponse
  property_count: 1
  slug: firma-dev-signer-terms-list-response
- name: SignerTermsUpdateResponse
  property_count: 3
  slug: firma-dev-signer-terms-update-response
- name: SigningRequestCustomField
  property_count: 6
  slug: firma-dev-signing-request-custom-field
- name: SigningRequestDetail
  property_count: 26
  slug: firma-dev-signing-request-detail
- name: SigningRequestSettings
  property_count: 15
  slug: firma-dev-signing-request-settings
- name: SigningRequestUpdateResponse
  property_count: 6
  slug: firma-dev-signing-request-update-response
- name: TemplateCopyResponse
  property_count: 4
  slug: firma-dev-template-copy-response
- name: TemplateCustomField
  property_count: 5
  slug: firma-dev-template-custom-field
- name: TemplateDuplicateResponse
  property_count: 6
  slug: firma-dev-template-duplicate-response
- name: TemplatePatchResponse
  property_count: 3
  slug: firma-dev-template-patch-response
- name: Template
  property_count: 13
  slug: firma-dev-template
- name: TestWebhookResponse
  property_count: 5
  slug: firma-dev-test-webhook-response
- name: WebhookListResponse
  property_count: 2
  slug: firma-dev-webhook-list-response
- name: Webhook
  property_count: 9
  slug: firma-dev-webhook
- name: WorkspaceCustomField
  property_count: 7
  slug: firma-dev-workspace-custom-field
- name: WorkspaceEmailTemplateListResponse
  property_count: 2
  slug: firma-dev-workspace-email-template-list-response
- name: WorkspaceListResponse
  property_count: 2
  slug: firma-dev-workspace-list-response
- name: Workspace
  property_count: 13
  slug: firma-dev-workspace
- name: WorkspaceSettings
  property_count: 32
  slug: firma-dev-workspace-settings
jsonld:
- class_count: 108
  name: Firma Dev Context
  property_count: 312
  slug: firma-dev-context
layout: provider
mcp_servers:
- description: ''
  name: Firma.dev MCP Server
  slug: firmadev-mcp-server
modified: '2026-09-25'
name: Firma.dev
nav: Providers
network: true
overview: 'Firma.dev publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Company API, Custom Fields API, Email Domains API, and 9 more. Tagged areas include Company, E-Signature, Developer Tools, LowCost, and White Label.


  The Firma.dev catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Firma.dev''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, signup flow, support, and 26 more developer resources.'
plans:
- name: Firma Dev Plans Pricing
  plan_count: 2
  slug: firma-dev-plans-pricing
random_paper: 11
rules:
- effective_rule_count: 57
  extends:
  - spectral:oas
  name: Firma.dev API Rules
  rule_count: 16
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 3
  slug: firma-dev-rules
score:
  band: strong
  composite: 60.5
  coverage:
    artifact_dirs: 20
    catalog_earned: 60.8
    catalog_earned_first_party: 8.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 81.6
    contract_governance: 22.0
    contract_quality: 69.2
    developer_ergonomics: 54.2
    discoverability: 53.3
    operational_transparency: 26.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: true
    score: 33.3
security:
- kind: authentication
  name: Firma Dev Authentication
  slug: firma-dev-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Firma Dev Domain Security
  slug: firma-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Firma Dev Trust Center
  slug: firma-dev-trust-center
  summary_line: GDPR
slug: firma-dev
tags:
- Company
- E-Signature
- Developer Tools
- LowCost
- White Label
website: https://firma.dev/
---
