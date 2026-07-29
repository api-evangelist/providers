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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 53.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Trulioo Agentic Access
  operation_count: 54
  slug: trulioo-agentic-access
  summary_line: 54 operations · 20 acting
api_count: 19
apis:
- description: Normalized KYC / electronic identity verification API. Submit a Verify request with normalized PersonInfo, Communication, Location, NationalIds, and Documents fields and Trulioo's GlobalGateway routes
  name: Trulioo Verifications API
  slug: trulioo-verifications-api
- description: 'Discovery endpoints for the GlobalGateway. Learn which countries, datasources, fields, document types, consents, and test entities are available for a configured product / package before submitting a '
  name: Trulioo Configuration API
  slug: trulioo-configuration-api
- description: Health-check and authentication-test endpoints. `sayhello` is an unauthenticated ping; `testauthentication` verifies your credentials before exercising paid endpoints.
  name: Trulioo Connection API
  slug: trulioo-connection-api
- description: Know Your Business (KYB) API for verifying legal entities, retrieving business registration data from official registries, listing officers and persons of significant control, and downloading business
  name: Trulioo Business Verification API
  slug: trulioo-business-verification-api
- description: Fraud Intelligence — Person Fraud risk scoring. Submit an identity payload and receive a risk verdict that aggregates third-party fraud signals, velocity checks, device intelligence, and identity-grap
  name: Trulioo Person Fraud API
  slug: trulioo-person-fraud-api
- description: 'Capture, classify, and verify government-issued identity documents (driver''s license, passport, national ID) paired with optional liveness selfie checks. Used to authenticate documents, extract MRZ / '
  name: Trulioo Identity Document Verification API
  slug: trulioo-document-verification-api
- description: OAuth2 client-credential token acquisition.
  name: Trulioo Authentication API
  slug: trulioo-authentication-api
- description: Discover JOIs and registration number requirements.
  name: Trulioo Business Configuration API
  slug: trulioo-business-configuration-api
- description: Download business reports.
  name: Trulioo Business Reports API
  slug: trulioo-business-reports-api
- description: Search the Trulioo business registry universe.
  name: Trulioo Business Search API
  slug: trulioo-business-search-api
- description: Discover document types per country.
  name: Trulioo Document Configuration API
  slug: trulioo-document-configuration-api
- description: Download evidence documents from completed transactions.
  name: Trulioo Documents API
  slug: trulioo-documents-api
- description: Profiles, files, and bulk operations on end clients.
  name: Trulioo End Clients API
  slug: trulioo-end-clients-api
- description: Webhook event dispatch.
  name: Trulioo Events API
  slug: trulioo-events-api
- description: Initialize and drive a workflow flow.
  name: Trulioo Flows API
  slug: trulioo-flows-api
- description: Manage Known Faces lists for biometric watchlists.
  name: Trulioo Known Faces API
  slug: trulioo-known-faces-api
- description: Generate signed URLs for user sessions.
  name: Trulioo Sessions API
  slug: trulioo-sessions-api
- description: Retrieve verification transactions and status.
  name: Trulioo Transactions API
  slug: trulioo-transactions-api
- description: Retrieve workflow definitions.
  name: Trulioo Workflows API
  slug: trulioo-workflows-api
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
artifact_total: 92
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
  name: Trulioo Business Verification API
  slug: open-trulioo-business-verification-api
- collection_type: open
  name: Trulioo Configuration API
  slug: open-trulioo-configuration-api
- collection_type: open
  name: Trulioo Connection API
  slug: open-trulioo-connection-api
- collection_type: open
  name: Trulioo Identity Document Verification API
  slug: open-trulioo-document-verification-api
- collection_type: open
  name: Trulioo Person Fraud API
  slug: open-trulioo-person-fraud-api
- collection_type: open
  name: Trulioo Platform API
  slug: open-trulioo-platform-api
- collection_type: open
  name: Trulioo Verifications API
  slug: open-trulioo-verifications-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/trulioo-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/trulioo-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trulioo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/trulioo-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/trulioo-scopes.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/trulioo/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/trulioo-async-verify-and-poll-status-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/trulioo-business-registration-numbers-and-search-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/trulioo-business-search-and-verify-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/trulioo-business-verify-and-download-report-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/trulioo-configure-and-verify-person-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/trulioo-detailed-consents-and-verify-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/trulioo-discover-package-and-verify-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/trulioo-document-verification-with-liveness-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/trulioo-document-verify-and-download-evidence-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/trulioo-hosted-session-signed-url-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/trulioo-identity-and-fraud-risk-decision-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/trulioo-known-faces-enroll-from-document-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/trulioo-person-fraud-risk-check-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/trulioo-preflight-and-verify-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/trulioo-recommended-fields-verify-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/trulioo-sandbox-test-entity-verify-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/trulioo-subdivisions-and-verify-with-address-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/trulioo-verify-person-and-fetch-record-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/trulioo-workflow-studio-run-flow-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://www.trulioo.com
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
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://developer.trulioo.com/docs/platform-update-67
- group: start
  title: ''
  type: Sandbox
  url: https://developer.trulioo.com/docs/trulidemo
- group: operate
  title: ''
  type: Support
  url: https://support@trulioo.com
- group: start
  title: ''
  type: SupportPortal
  url: https://knowledgehub.trulioo.com
- group: operate
  title: ''
  type: Status
  url: https://status.trulioo.com
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.trulioo.com/trust
- group: auth
  title: ''
  type: Security
  url: https://www.trulioo.com/trust/security
- group: auth
  title: ''
  type: Compliance
  url: https://www.trulioo.com/trust/compliance
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.trulioo.com/legal/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.trulioo.com/legal/terms-of-service
- group: company
  title: ''
  type: Blog
  url: https://www.trulioo.com/blog
- group: other
  title: ''
  type: Customers
  url: https://www.trulioo.com/customers
- group: other
  title: ''
  type: CaseStudies
  url: https://www.trulioo.com/resource-library?type=case-studies
- group: build
  title: ''
  type: ResourceLibrary
  url: https://www.trulioo.com/resource-library
- group: commercial
  title: ''
  type: Pricing
  url: https://www.trulioo.com/contact
- group: start
  title: ''
  type: Login
  url: https://portal.trulioo.com
- group: start
  title: ''
  type: Signup
  url: https://www.trulioo.com/contact-sales
- group: operate
  title: ''
  type: ContactSales
  url: https://www.trulioo.com/contact-sales
- group: company
  title: ''
  type: Careers
  url: https://www.trulioo.com/about-us/careers
- group: company
  title: ''
  type: AboutUs
  url: https://www.trulioo.com/about-us
- group: other
  title: ''
  type: Leadership
  url: https://www.trulioo.com/about-us/leadership
- group: company
  title: ''
  type: News
  url: https://www.trulioo.com/news-and-events
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
  title: ''
  type: MCPServer
  url: https://github.com/trulioo/mcp-server
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
  title: ''
  type: Plans
  url: plans/trulioo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/trulioo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/trulioo-finops.yml
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
features:
- GlobalGateway — single API into 450+ data sources across 195+ countries
- Normalized KYC verification (Verifications API) with watchlist and PEP screening
- KYB business verification with official registry data, officers, and persons of significant control
- Identity Document Verification (DocV) with MRZ / barcode extraction and liveness checks
- Biometric face match plus Known Faces biometric watchlists
- Fraud Intelligence — Person Fraud risk scoring with third-party signal aggregation
- Watchlist screening (sanctions, PEPs, adverse media) and ongoing AML monitoring
- Address validation, cleansing, and standardization
- Workflow Studio — low-code orchestrator for verification flows
- Workflow Studio (API) — programmatic flow control with hand-offs and signed-URL sessions
- Reusable end-client profiles and bulk client management
- Multi-region data residency (AMER, EMEA, APAC) for sovereign deployments
- Webhook event delivery via the Event Dispatcher
- Authentication via Basic, OAuth2 client-credential, HMAC, and Mutual TLS
- Sandbox (Trulidemo) with deterministic test entities per country
- Mobile SDKs (iOS, Android, React Native) and Web Capture SDK
- Backend SDKs in C# (v3) and Java (v3) plus legacy v1 SDKs
- MCP Server for agentic KYB integrations
- Customer consent capture per datasource with retrievable consent text
- Configuration API for runtime form generation and field discovery
finops:
- name: Trulioo Finops
  service_category: ''
  slug: trulioo-finops
graphqls:
- description: Trulioo is a global identity verification platform. The API covers identity document verification, biometric matching, business verification (KYB), watchlist screening, address verification, and globa
  name: Trulioo GraphQL API
  slug: trulioo-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/trulioo.png
json_schemas:
- name: Trulioo Business Record
  property_count: 9
  slug: trulioo-business-record
- name: Trulioo Verify Request
  property_count: 8
  slug: trulioo-verify-request
- name: Trulioo Verify Result
  property_count: 6
  slug: trulioo-verify-result
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
- description: ''
  name: Trulioo MCP Server (KYB)
  slug: trulioo-mcp-server-kyb
modified: '2026-05-25'
name: Trulioo
nav: Providers
network: true
overview: 'Trulioo publishes 19 APIs on the [APIs.io](https://apis.io/) network, including Verifications API, Configuration API, Connection API, and 16 more. Tagged areas include Identity Verification, KYC, KYB, AML, and Watchlist Screening.


  The Trulioo catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Trulioo''s developer surface includes authentication, developer portal, documentation, getting-started guide, API reference, changelog, release notes, and 71 more developer resources.'
plans:
- name: Trulioo Plans Pricing
  plan_count: 6
  slug: trulioo-plans-pricing
random_paper: 62
rate_limits:
- limit_count: 3
  name: Trulioo Rate Limits
  slug: trulioo-rate-limits
rules:
- name: Trulioo API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: trulioo-jsonschema-spectral-rules
- name: Trulioo API Rules
  rule_count: 8
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 4
  slug: trulioo-rules
scopes:
- name: Trulioo Scopes
  scope_count: 3
  slug: trulioo-scopes
  summary_line: 3 scopes · clientCredentials
score:
  band: exemplar
  composite: 81.1
  delta: -3.4
  facets:
    commercial_clarity: 100.0
    contract_quality: 80.2
    developer_ergonomics: 87.0
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 71.1
  previous_composite: 84.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/trulioo/refs/heads/main/screenshots/trulioo-2026-06-20T195758.png
security:
- kind: authentication
  name: Trulioo Authentication
  slug: trulioo-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Trulioo Domain Security
  slug: trulioo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Trulioo Trust Center
  slug: trulioo-trust-center
  summary_line: SOC 2, ISO 27001
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
website: https://www.trulioo.com
---
