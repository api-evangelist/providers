---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 51.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Trulioo Agentic Access
  operation_count: 54
  slug: trulioo-agentic-access
  summary_line: 54 operations · 20 acting
api_count: 1
apis:
- baseURL: https://api.trulioo.com
  baseurl_source: declared
  description: Normalized KYC / electronic identity verification API. Submit a Verify request with normalized PersonInfo, Communication, Location, NationalIds, and Documents fields and Trulioo's GlobalGateway routes
  name: Trulioo Verifications API
  slug: trulioo-verifications-api
- baseURL: https://api.trulioo.com
  baseurl_source: declared
  description: 'Discovery endpoints for the GlobalGateway. Learn which countries, datasources, fields, document types, consents, and test entities are available for a configured product / package before submitting a '
  name: Trulioo Configuration API
  slug: trulioo-configuration-api
- baseURL: https://api.trulioo.com
  baseurl_source: declared
  description: Health-check and authentication-test endpoints. `sayhello` is an unauthenticated ping; `testauthentication` verifies your credentials before exercising paid endpoints.
  name: Trulioo Connection API
  slug: trulioo-connection-api
- baseURL: https://api.trulioo.com
  baseurl_source: declared
  description: Know Your Business (KYB) API for verifying legal entities, retrieving business registration data from official registries, listing officers and persons of significant control, and downloading business
  name: Trulioo Business Verification API
  slug: trulioo-business-verification-api
- baseURL: https://api.trulioo.com
  baseurl_source: declared
  description: Fraud Intelligence — Person Fraud risk scoring. Submit an identity payload and receive a risk verdict that aggregates third-party fraud signals, velocity checks, device intelligence, and identity-grap
  name: Trulioo Person Fraud API
  slug: trulioo-person-fraud-api
- baseURL: https://api.trulioo.com
  baseurl_source: declared
  description: 'Capture, classify, and verify government-issued identity documents (driver''s license, passport, national ID) paired with optional liveness selfie checks. Used to authenticate documents, extract MRZ / '
  name: Trulioo Identity Document Verification API
  slug: trulioo-document-verification-api
- baseURL: https://api.trulioo.com
  baseurl_source: declared
  description: OAuth2 client-credential token acquisition.
  name: Trulioo Authentication API
  slug: trulioo-authentication-api
- baseURL: https://api.trulioo.com
  baseurl_source: declared
  description: Discover JOIs and registration number requirements.
  name: Trulioo Business Configuration API
  slug: trulioo-business-configuration-api
- baseURL: https://api.trulioo.com
  baseurl_source: declared
  description: Download business reports.
  name: Trulioo Business Reports API
  slug: trulioo-business-reports-api
- baseURL: https://api.trulioo.com
  baseurl_source: declared
  description: Search the Trulioo business registry universe.
  name: Trulioo Business Search API
  slug: trulioo-business-search-api
- baseURL: https://api.trulioo.com
  baseurl_source: declared
  description: Discover document types per country.
  name: Trulioo Document Configuration API
  slug: trulioo-document-configuration-api
- baseURL: https://api.trulioo.com
  baseurl_source: declared
  description: Download evidence documents from completed transactions.
  name: Trulioo Documents API
  slug: trulioo-documents-api
- baseURL: https://api.trulioo.com
  baseurl_source: declared
  description: Profiles, files, and bulk operations on end clients.
  name: Trulioo End Clients API
  slug: trulioo-end-clients-api
- baseURL: https://api.trulioo.com
  baseurl_source: declared
  description: Webhook event dispatch.
  name: Trulioo Events API
  slug: trulioo-events-api
- baseURL: https://api.trulioo.com
  baseurl_source: declared
  description: Initialize and drive a workflow flow.
  name: Trulioo Flows API
  slug: trulioo-flows-api
- baseURL: https://api.trulioo.com
  baseurl_source: declared
  description: Manage Known Faces lists for biometric watchlists.
  name: Trulioo Known Faces API
  slug: trulioo-known-faces-api
- baseURL: https://api.trulioo.com
  baseurl_source: declared
  description: Generate signed URLs for user sessions.
  name: Trulioo Sessions API
  slug: trulioo-sessions-api
- baseURL: https://api.trulioo.com
  baseurl_source: declared
  description: Retrieve verification transactions and status.
  name: Trulioo Transactions API
  slug: trulioo-transactions-api
- baseURL: https://api.trulioo.com
  baseurl_source: declared
  description: Retrieve workflow definitions.
  name: Trulioo Workflows API
  slug: trulioo-workflows-api
- description: Hosted Model Context Protocol server (streamable HTTP) at https://mcp.trulioo.com/mcp exposing typed KYC person verification, KYB business search/verification/reporting, AML screening, document verifi
  name: Trulioo MCP Server
  slug: trulioo-mcp-server
arazzos:
- description: Submit an asynchronous verification, poll its status until complete, then read the result.
  name: Trulioo Async Verify And Poll For Completion
  slug: trulioo-async-verify-and-poll-status-workflow
- description: List a country's business registration number types, then search the registry by number.
  name: Trulioo Discover Registration Number Types Then Search Business
  slug: trulioo-business-registration-numbers-and-search-workflow
- description: Resolve a country's jurisdictions of incorporation, search for a business, then verify the best match.
  name: Trulioo Business Search Then Verify (KYB)
  slug: trulioo-business-search-and-verify-workflow
- description: Verify a business by registration number, then download its registry report.
  name: Trulioo Business Verify And Download Report (KYB)
  slug: trulioo-business-verify-and-download-report-workflow
- description: Discover a country's accepted fields and consents, then run a KYC identity verification.
  name: Trulioo Configure And Verify A Person
  slug: trulioo-configure-and-verify-person-workflow
- description: Pull the full consent text to present to the end user, then verify with those consents recorded.
  name: Trulioo Capture Detailed Consents And Verify
  slug: trulioo-detailed-consents-and-verify-workflow
- description: List the customer's configured packages, resolve a package's supported countries, then verify a person.
  name: Trulioo Discover A Package And Verify
  slug: trulioo-discover-package-and-verify-workflow
- description: Resolve supported document types for a country, then verify a captured ID against a liveness selfie.
  name: Trulioo Document Verification With Liveness
  slug: trulioo-document-verification-with-liveness-workflow
- description: Verify an identity document, then download a captured evidence image from the transaction.
  name: Trulioo Document Verify And Download Evidence Image
  slug: trulioo-document-verify-and-download-evidence-workflow
- description: Authenticate, list available workflows, then generate a signed URL for an end-user hosted session.
  name: Trulioo Generate A Hosted Verification Session URL
  slug: trulioo-hosted-session-signed-url-workflow
- description: Run a KYC identity verification and a Person Fraud risk check on the same person for a layered decision.
  name: Trulioo Combined Identity Verify And Fraud Risk Decision
  slug: trulioo-identity-and-fraud-risk-decision-workflow
- description: Create a Known Faces watchlist, verify a document with a selfie, then enroll the transaction into the list.
  name: Trulioo Enroll A Verified Face Into A Known Faces List
  slug: trulioo-known-faces-enroll-from-document-workflow
- description: Resolve the Person Fraud field schema for a country, then run a fraud risk check.
  name: Trulioo Person Fraud Risk Check
  slug: trulioo-person-fraud-risk-check-workflow
- description: Confirm connectivity and credentials before spending a paid Verify call.
  name: Trulioo Preflight Credentials Then Verify
  slug: trulioo-preflight-and-verify-workflow
- description: Fetch the recommended field combination for a country, list its datasources, then verify a person.
  name: Trulioo Use Recommended Fields To Verify
  slug: trulioo-recommended-fields-verify-workflow
- description: Pull a deterministic sandbox test entity for a country and run a Verify against it.
  name: Trulioo Verify A Sandbox Test Entity
  slug: trulioo-sandbox-test-entity-verify-workflow
- description: Look up a country's state/province codes, verify a person with an address, then read the cleansed address.
  name: Trulioo Resolve Subdivisions And Verify With Address
  slug: trulioo-subdivisions-and-verify-with-address-workflow
- description: Run a KYC verification, then pull the complete transaction record including datasource detail.
  name: Trulioo Verify A Person And Fetch The Full Record
  slug: trulioo-verify-person-and-fetch-record-workflow
- description: Authenticate, initialize a user state, fetch the current step, submit step data, then read the profile.
  name: Trulioo Workflow Studio Drive A Flow
  slug: trulioo-workflow-studio-run-flow-workflow
artifact_total: 111
asyncapis:
- description: ''
  name: Trulioo Webhooks
  slug: trulioo-webhooks
collections:
- collection_type: postman
  name: Trulioo Business Verification API
  slug: postman-trulioo-business-verification-api
- collection_type: postman
  name: Trulioo Configuration API
  slug: postman-trulioo-configuration-api
- collection_type: postman
  name: Trulioo Connection API
  slug: postman-trulioo-connection-api
- collection_type: postman
  name: Trulioo Identity Document Verification API
  slug: postman-trulioo-document-verification-api
- collection_type: postman
  name: Trulioo Person Fraud API
  slug: postman-trulioo-person-fraud-api
- collection_type: postman
  name: Trulioo Platform API
  slug: postman-trulioo-platform-api
- collection_type: postman
  name: Trulioo Verifications API
  slug: postman-trulioo-verifications-api
- collection_type: open
  name: Trulioo Business Verification Authentication API
  slug: open-trulioo-authentication-api
- collection_type: open
  name: Trulioo Business Verification Authentication Business Configuration API
  slug: open-trulioo-business-configuration-api
- collection_type: open
  name: Trulioo Business Verification Authentication Business Reports API
  slug: open-trulioo-business-reports-api
- collection_type: open
  name: Trulioo Business Verification Authentication Business Search API
  slug: open-trulioo-business-search-api
- collection_type: open
  name: Trulioo Authentication Business Verification API
  slug: open-trulioo-business-verification-api
- collection_type: open
  name: Trulioo Business Verification Authentication Configuration API
  slug: open-trulioo-configuration-api
- collection_type: open
  name: Trulioo Business Verification Authentication Connection API
  slug: open-trulioo-connection-api
- collection_type: open
  name: Trulioo Business Verification Authentication Document Configuration API
  slug: open-trulioo-document-configuration-api
- collection_type: open
  name: Trulioo Business Verification Authentication Document Verification API
  slug: open-trulioo-document-verification-api
- collection_type: open
  name: Trulioo Business Verification Authentication Documents API
  slug: open-trulioo-documents-api
- collection_type: open
  name: Trulioo Business Verification Authentication End Clients API
  slug: open-trulioo-end-clients-api
- collection_type: open
  name: Trulioo Business Verification Authentication Events API
  slug: open-trulioo-events-api
- collection_type: open
  name: Trulioo Business Verification Authentication Flows API
  slug: open-trulioo-flows-api
- collection_type: open
  name: Trulioo Business Verification Authentication Known Faces API
  slug: open-trulioo-known-faces-api
- collection_type: open
  name: Trulioo Business Verification Authentication Person Fraud API
  slug: open-trulioo-person-fraud-api
- collection_type: open
  name: Trulioo Platform API
  slug: open-trulioo-platform-api
- collection_type: open
  name: Trulioo Business Verification Authentication Sessions API
  slug: open-trulioo-sessions-api
- collection_type: open
  name: Trulioo Business Verification Authentication Transactions API
  slug: open-trulioo-transactions-api
- collection_type: open
  name: Trulioo Business Verification Authentication Verifications API
  slug: open-trulioo-verifications-api
- collection_type: open
  name: Trulioo Business Verification Authentication Workflows API
  slug: open-trulioo-workflows-api
common:
- group: other
  href: https://artifacts.apis.io/trulioo/capabilities/trulioo-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/trulioo-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/trulioo/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/trulioo/asyncapi/trulioo-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/trulioo-webhooks.yml
- group: design
  href: https://artifacts.apis.io/trulioo/components/trulioo-components.yml
  title: ''
  type: Components
  url: components/trulioo-components.yml
- group: operate
  href: https://artifacts.apis.io/trulioo/changelog/trulioo-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/trulioo-changelog.yml
- group: design
  href: https://artifacts.apis.io/trulioo/conventions/trulioo-conventions.yml
  title: ''
  type: Conventions
  url: conventions/trulioo-conventions.yml
- group: start
  href: https://artifacts.apis.io/trulioo/sandbox/trulioo-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/trulioo-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/trulioo/security/trulioo-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/trulioo-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/trulioo/lifecycle/trulioo-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/trulioo-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/trulioo/errors/trulioo-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/trulioo-error-codes.yml
- group: other
  href: https://artifacts.apis.io/trulioo/overlays/trulioo-authentication-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/trulioo-authentication-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/trulioo/llms/trulioo-mcp-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/trulioo-mcp-llms.txt
- group: agent
  href: https://artifacts.apis.io/trulioo/llms/trulioo-mcp-developer-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/trulioo-mcp-developer-llms.txt
- group: build
  href: https://artifacts.apis.io/trulioo/mcp/trulioo-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/trulioo-tool-crosswalk.yml
- group: build
  href: https://artifacts.apis.io/trulioo/packages/trulioo-packages.yml
  title: ''
  type: Packages
  url: packages/trulioo-packages.yml
- group: design
  href: https://artifacts.apis.io/trulioo/rules/trulioo-rules.yml
  title: ''
  type: Spectral
  url: rules/trulioo-rules.yml
- group: design
  href: https://artifacts.apis.io/trulioo/rules/trulioo-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/trulioo-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/trulioo/vocabulary/trulioo-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/trulioo-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/trulioo/data-model/trulioo-data-model.yml
  title: ''
  type: DataModel
  url: data-model/trulioo-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.trulioo.com/compliance
- group: design
  href: https://artifacts.apis.io/trulioo/errors/trulioo-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/trulioo-problem-types.yml
- group: design
  href: https://artifacts.apis.io/trulioo/conformance/trulioo-conformance.yml
  title: ''
  type: Conformance
  url: conformance/trulioo-conformance.yml
- group: agent
  href: https://artifacts.apis.io/trulioo/llms/trulioo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/trulioo-llms.txt
- group: agent
  href: https://artifacts.apis.io/trulioo/well-known/trulioo-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/trulioo-well-known.yml
- group: other
  href: https://artifacts.apis.io/trulioo/hosts/trulioo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/trulioo-hosts.yml
- group: other
  href: https://artifacts.apis.io/trulioo/vendors/trulioo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/trulioo-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.trulioo.com/access/login
- group: company
  title: ''
  type: Website
  url: https://www.trulioo.com/
- group: agent
  href: https://artifacts.apis.io/trulioo/agentic-access/trulioo-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/trulioo-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/trulioo/security/trulioo-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/trulioo-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/trulioo/security/trulioo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/trulioo-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/trulioo/authentication/trulioo-authentication.yml
  title: ''
  type: Authentication
  url: authentication/trulioo-authentication.yml
- group: auth
  href: https://artifacts.apis.io/trulioo/scopes/trulioo-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/trulioo-scopes.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/trulioo/overview
- group: design
  href: https://artifacts.apis.io/trulioo/arazzo/trulioo-async-verify-and-poll-status-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/trulioo-async-verify-and-poll-status-workflow.yml
- group: design
  href: https://artifacts.apis.io/trulioo/arazzo/trulioo-business-registration-numbers-and-search-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/trulioo-business-registration-numbers-and-search-workflow.yml
- group: design
  href: https://artifacts.apis.io/trulioo/arazzo/trulioo-business-search-and-verify-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/trulioo-business-search-and-verify-workflow.yml
- group: design
  href: https://artifacts.apis.io/trulioo/arazzo/trulioo-business-verify-and-download-report-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/trulioo-business-verify-and-download-report-workflow.yml
- group: design
  href: https://artifacts.apis.io/trulioo/arazzo/trulioo-configure-and-verify-person-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/trulioo-configure-and-verify-person-workflow.yml
- group: design
  href: https://artifacts.apis.io/trulioo/arazzo/trulioo-detailed-consents-and-verify-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/trulioo-detailed-consents-and-verify-workflow.yml
- group: design
  href: https://artifacts.apis.io/trulioo/arazzo/trulioo-discover-package-and-verify-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/trulioo-discover-package-and-verify-workflow.yml
- group: design
  href: https://artifacts.apis.io/trulioo/arazzo/trulioo-document-verification-with-liveness-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/trulioo-document-verification-with-liveness-workflow.yml
- group: design
  href: https://artifacts.apis.io/trulioo/arazzo/trulioo-document-verify-and-download-evidence-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/trulioo-document-verify-and-download-evidence-workflow.yml
- group: design
  href: https://artifacts.apis.io/trulioo/arazzo/trulioo-hosted-session-signed-url-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/trulioo-hosted-session-signed-url-workflow.yml
- group: design
  href: https://artifacts.apis.io/trulioo/arazzo/trulioo-identity-and-fraud-risk-decision-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/trulioo-identity-and-fraud-risk-decision-workflow.yml
- group: design
  href: https://artifacts.apis.io/trulioo/arazzo/trulioo-known-faces-enroll-from-document-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/trulioo-known-faces-enroll-from-document-workflow.yml
- group: design
  href: https://artifacts.apis.io/trulioo/arazzo/trulioo-person-fraud-risk-check-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/trulioo-person-fraud-risk-check-workflow.yml
- group: design
  href: https://artifacts.apis.io/trulioo/arazzo/trulioo-preflight-and-verify-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/trulioo-preflight-and-verify-workflow.yml
- group: design
  href: https://artifacts.apis.io/trulioo/arazzo/trulioo-recommended-fields-verify-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/trulioo-recommended-fields-verify-workflow.yml
- group: design
  href: https://artifacts.apis.io/trulioo/arazzo/trulioo-sandbox-test-entity-verify-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/trulioo-sandbox-test-entity-verify-workflow.yml
- group: design
  href: https://artifacts.apis.io/trulioo/arazzo/trulioo-subdivisions-and-verify-with-address-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/trulioo-subdivisions-and-verify-with-address-workflow.yml
- group: design
  href: https://artifacts.apis.io/trulioo/arazzo/trulioo-verify-person-and-fetch-record-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/trulioo-verify-person-and-fetch-record-workflow.yml
- group: design
  href: https://artifacts.apis.io/trulioo/arazzo/trulioo-workflow-studio-run-flow-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/trulioo-workflow-studio-run-flow-workflow.yml
- group: docs
  title: ''
  type: Documentation
  url: https://developer.trulioo.com
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.trulioo.com/reference/getting-started-1
- group: docs
  title: ''
  type: APIReference
  url: https://developer.trulioo.com/reference/api-reference-overview
- group: auth
  title: ''
  type: Authentication
  url: https://developer.trulioo.com/reference/authentication
- group: auth
  title: ''
  type: Authentication
  url: https://developer.trulioo.com/reference/hmac
- group: auth
  title: ''
  type: Authentication
  url: https://developer.trulioo.com/reference/connecting-to-trulioos-api-using-mutual-tls
- group: design
  title: ''
  type: Webhooks
  url: https://developer.trulioo.com/reference/event-dispatcher
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.trulioo.com/docs/release-notes
- group: start
  title: ''
  type: SupportPortal
  url: https://knowledgehub.trulioo.com
- group: operate
  title: ''
  type: Status
  url: https://status.trulioo.com
- group: company
  title: ''
  type: Blog
  url: https://www.trulioo.com/blog
- group: start
  title: ''
  type: Login
  url: https://portal.trulioo.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/trulioo
- group: build
  title: ''
  type: SDKs
  url: https://github.com/trulioo/sdk-csharp-v3
- group: build
  title: ''
  type: SDKs
  url: https://github.com/trulioo/sdk-java-v3
- group: build
  title: ''
  type: SDKs
  url: https://github.com/trulioo/sdk-csharp-v1
- group: build
  title: ''
  type: SDKs
  url: https://github.com/trulioo/sdk-java-v1
- group: build
  title: ''
  type: MobileSDK
  url: https://github.com/trulioo/trulioo-ios
- group: build
  title: ''
  type: MobileSDK
  url: https://github.com/trulioo/kyc-documents-capture
- group: build
  title: ''
  type: MobileSDK
  url: https://github.com/trulioo/docv
- group: build
  title: ''
  type: MobileSDK
  url: https://developer.trulioo.com/reference/android
- group: build
  title: ''
  type: MobileSDK
  url: https://developer.trulioo.com/reference/react-native
- group: build
  title: ''
  type: WebSDK
  url: https://developer.trulioo.com/reference/web
- group: agent
  href: https://artifacts.apis.io/trulioo/mcp/trulioo-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/trulioo-mcp.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/trulioo
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/trulioo
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/trulioo_global
- group: other
  title: ''
  type: Regions
  url: https://developer.trulioo.com/reference/multi-region-hosting
- group: design
  title: ''
  type: ErrorCodes
  url: https://developer.trulioo.com/reference/errors
- group: design
  title: ''
  type: Versioning
  url: https://developer.trulioo.com/reference/api-reference-overview
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.trulioo.com/llms.txt
- group: commercial
  href: https://artifacts.apis.io/trulioo/plans/trulioo-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/trulioo-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/trulioo/rate-limits/trulioo-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/trulioo-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/trulioo/finops/trulioo-finops.yml
  title: ''
  type: FinOps
  url: finops/trulioo-finops.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.trulioo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.trulioo.com/docs
- group: operate
  title: ''
  type: Support
  url: https://www.trulioo.com/company/contact-us
- group: operate
  title: ''
  type: ContactSales
  url: https://www.trulioo.com/lp/contact/book-a-demo
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.trulioo.com/privacy
- group: other
  title: ''
  type: CookiePolicy
  url: https://www.trulioo.com/cookie-policy
- group: commercial
  title: ''
  type: Legal
  url: https://www.trulioo.com/legal
- group: commercial
  title: ''
  type: DataProcessingAgreement
  url: https://www.trulioo.com/legal/dpa
- group: auth
  title: ''
  type: Security
  url: https://www.trulioo.com/company/security-compliance
- group: company
  title: ''
  type: AboutUs
  url: https://www.trulioo.com/company/about-us
- group: company
  title: ''
  type: Careers
  url: https://www.trulioo.com/company/careers
- group: other
  title: ''
  type: Leadership
  url: https://www.trulioo.com/company/leadership
- group: company
  title: ''
  type: Newsroom
  url: https://www.trulioo.com/company/newsroom
- group: company
  title: ''
  type: Partners
  url: https://www.trulioo.com/company/partners
- group: build
  title: ''
  type: ResourceLibrary
  url: https://www.trulioo.com/resources
- group: other
  title: ''
  type: CaseStudies
  url: https://www.trulioo.com/resources/case-studies
- group: docs
  title: ''
  type: Documentation
  url: https://mcp.trulioo.com/developer/
- group: agent
  title: ''
  type: LlmsText
  url: https://mcp.trulioo.com/llms.txt
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/Trulioo/trulioo-mcp
- group: other
  title: ''
  type: DataResidency
  url: https://developer.trulioo.com/reference/multi-region-hosting
- group: operate
  title: ''
  type: IncidentNotification
  url: https://www.trulioo.com/legal/dpa
- group: operate
  title: ''
  type: SupportLifetime
  url: https://github.com/Trulioo/trulioo-mcp/blob/main/SECURITY.md
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.trulioo.com/reference/deprecated
created: '2026-05-25'
description: Trulioo is a Vancouver-based global identity verification platform that operates GlobalGateway, a single-API gateway into 450+ data sources across 195+ countries for person verification (KYC), business verification (KYB), watchlist and PEP screening, identity document verification (DocV), biometric face match, and fraud-intelligence risk scoring. The Trulioo Platform layers Workflow Studio (hosted and low-code), reusable end-client profiles, event-driven webhooks, native mobile and web capture SDKs, and an MCP server on top of the underlying Verifications and Business APIs.
examples:
- key_count: 2
  name: Trulioo Business Search Example
  slug: trulioo-business-search-example
- key_count: 2
  name: Trulioo Document Verify Example
  slug: trulioo-document-verify-example
- key_count: 2
  name: Trulioo Verify Person Example
  slug: trulioo-verify-person-example
finops:
- has_sources: true
  method: derived
  name: Trulioo Finops
  primary_unit: ''
  service_category: ''
  slug: trulioo-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/trulioo.png
json_schemas:
- name: AccessToken
  property_count: 3
  slug: trulioo-access-token
- name: Trulioo Business Record
  property_count: 9
  slug: trulioo-business-record
- name: BusinessRegistrationNumber
  property_count: 4
  slug: trulioo-business-registration-number
- name: BusinessSearchRequest
  property_count: 5
  slug: trulioo-business-search-request
- name: BusinessSearchResponse
  property_count: 2
  slug: trulioo-business-search-response
- name: Consent
  property_count: 3
  slug: trulioo-consent
- name: CountrySubdivision
  property_count: 2
  slug: trulioo-country-subdivision
- name: DatasourceGroup
  property_count: 3
  slug: trulioo-datasource-group
- name: DocumentVerifyRequest
  property_count: 6
  slug: trulioo-document-verify-request
- name: DocumentVerifyResult
  property_count: 7
  slug: trulioo-document-verify-result
- name: DownloadDocument
  property_count: 2
  slug: trulioo-download-document
- name: FlowStep
  property_count: 5
  slug: trulioo-flow-step
- name: KnownFacesList
  property_count: 3
  slug: trulioo-known-faces-list
- name: Package
  property_count: 2
  slug: trulioo-package
- name: Profile
  property_count: 5
  slug: trulioo-profile
- name: RiskVerifyRequest
  property_count: 5
  slug: trulioo-risk-verify-request
- name: RiskVerifyResult
  property_count: 5
  slug: trulioo-risk-verify-result
- name: TestEntity
  property_count: 3
  slug: trulioo-test-entity
- name: TransactionRecordResult
  property_count: 5
  slug: trulioo-transaction-record-result
- name: TransactionStatus
  property_count: 3
  slug: trulioo-transaction-status
- name: Trulioo Verify Request
  property_count: 8
  slug: trulioo-verify-request
- name: Trulioo Verify Result
  property_count: 6
  slug: trulioo-verify-result
- name: Workflow
  property_count: 5
  slug: trulioo-workflow
json_structures:
- name: Trulioo Verification Structure
  property_count: 8
  slug: trulioo-verification-structure
jsonld:
- class_count: 28
  name: Trulioo Context
  property_count: 17
  slug: trulioo-context
layout: provider
mcp_servers:
- description: Trulioo hosts a streamable-HTTP MCP server at https://mcp.trulioo.com/mcp exposing typed KYC, KYB, AML, document verification, age assurance, business monitoring, account analytics and Know Your Agent
  name: Trulioo MCP Server (KYB)
  slug: trulioo-mcp
modified: '2026-10-08'
name: Trulioo
nav: Providers
network: true
overview: 'Trulioo publishes 20 API contracts indexed on the [APIs.io](https://apis.io/) network, including Verifications API, Configuration API, Connection API, and 17 more. Tagged areas include Identity Verification, KYC, KYB, AML, and Watchlist Screening.


  The Trulioo catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Trulioo''s developer surface includes changelog, sandbox, authentication, documentation, getting-started guide, API reference, status page, and 103 more developer resources.'
plans:
- name: Trulioo Plans Pricing
  plan_count: 0
  slug: trulioo-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Trulioo Rate Limits
  slug: trulioo-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Trulioo — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: trulioo-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: Trulioo API Rules
  rule_count: 8
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 4
  slug: trulioo-rules
scopes:
- name: Trulioo Scopes
  scope_count: 12
  slug: trulioo-scopes
  summary_line: 12 scopes · clientCredentials
score:
  band: strong
  composite: 64.1
  coverage:
    artifact_dirs: 42
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 8.5
  facets:
    access_clarity: 23.7
    contract_governance: 22.0
    contract_quality: 68.2
    developer_ergonomics: 82.1
    discoverability: 76.7
    operational_transparency: 75.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - canada
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 55.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 46.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/trulioo/trulioo-2026-06-20T195758.png
security:
- kind: authentication
  name: Trulioo Authentication
  slug: trulioo-authentication
  summary_line: oauth2/http/mutualTLS · 4 schemes
- kind: domain-security
  name: Trulioo Domain Security
  slug: trulioo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Trulioo Vulnerability Disclosure
  slug: trulioo-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Trulioo Trust Center
  slug: trulioo-trust-center
  summary_line: SOC 2, ISO 27001
skill_count: 4
skills:
- name: trulioo-business-search-and-verify-rest
  slug: trulioo-business-search-and-verify-rest
- name: trulioo-document-verification-rest
  slug: trulioo-document-verification-rest
- name: trulioo-person-fraud-check-rest
  slug: trulioo-person-fraud-check-rest
- name: trulioo-verify-person-rest
  slug: trulioo-verify-person-rest
slug: trulioo
tags:
- Identity Verification
- KYC
- KYB
- AML
- Watchlist Screening
- Biometrics
- Document Verification
- Fraud Prevention
- Compliance
- Global Identity
website: https://www.trulioo.com/
---
