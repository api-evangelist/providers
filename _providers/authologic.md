---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 49.0
  scored_at: '2026-09-23'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Authologic Agentic Access
  operation_count: 14
  slug: authologic-agentic-access
  summary_line: 14 operations · 4 acting
api_count: 1
apis:
- description: The Authologic Identity API enables businesses to initiate identity verification processes and receive results programmatically. Supports document verification, eID, Bank ID, and biometric liveness ch
  name: Authologic Identity API
  slug: authologic-identity-api
- baseURL: https://api.authologic.com
  baseurl_source: declared
  description: The Authologic AML API enables Anti-Money Laundering screening combined with identity verification in a single integrated flow for KYC/AML compliance.
  name: Authologic AML API
  slug: authologic-aml-api
- description: The Authologic Data Verification API enables verification of personal data against authoritative sources including government databases and credit bureaus.
  name: Authologic Data Verification API
  slug: authologic-data-verification-api
- description: The Authologic Enquiry API enables background checks and identity enquiries against national and international data sources for enhanced due diligence.
  name: Authologic Enquiry API
  slug: authologic-enquiry-api
- baseURL: https://api.authologic.com
  baseurl_source: declared
  description: 4. Advanced methods.
  name: Authologic Advanced API
  slug: authologic-advanced-api
- baseURL: https://api.authologic.com
  baseurl_source: declared
  description: '7. Product: Affordability assessment'
  name: Authologic Affordability assessment API
  slug: authologic-affordability-assessment-api
- baseURL: https://api.authologic.com
  baseurl_source: declared
  description: '3. Product: AML'
  name: Authologic AML API
  slug: authologic-aml-api
- baseURL: https://api.authologic.com
  baseurl_source: declared
  description: '2. Product: Bank Transactions'
  name: Authologic Bank API
  slug: authologic-bank-api
- baseURL: https://api.authologic.com
  baseurl_source: declared
  description: 1. Base Methods needed for the verification process.
  name: Authologic Conversation API
  slug: authologic-conversation-api
- baseURL: https://api.authologic.com
  baseurl_source: declared
  description: '8. Product: Database Verification'
  name: Authologic Database Verification API
  slug: authologic-database-verification-api
- baseURL: https://api.authologic.com
  baseurl_source: declared
  description: 6. Enterprise Integration
  name: Authologic Enterprise Integration API
  slug: authologic-enterprise-integration-api
- baseURL: https://api.authologic.com
  baseurl_source: declared
  description: '5. Advanced: Metadata'
  name: Authologic Metadata API
  slug: authologic-metadata-api
artifact_total: 34
asyncapis:
- description: ''
  name: Authologic Callbacks Webhooks
  slug: authologic-callbacks-webhooks
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/authologic/refs/heads/main/overlays/authologic-customer-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/authologic-customer-api-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/authologic/refs/heads/main/agentic-access/authologic-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/authologic-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/authologic/refs/heads/main/security/authologic-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/authologic-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/authologic
- group: company
  title: ''
  type: Website
  url: https://authologic.com/
- group: start
  title: ''
  type: Portal
  url: https://developer.authologic.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.authologic.com/docs/developer-documentation/integration-overview
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.authologic.com/docs/developer-documentation/integration-overview
- group: company
  title: ''
  type: Blog
  url: https://authologic.com/blog/
- group: start
  title: ''
  type: SignUp
  url: https://omnipanel.authologic.com/signup
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://authologic.com/privacy-policy/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/authologic/refs/heads/main/authentication/authologic-authentication.yml
  title: ''
  type: Authentication
  url: authentication/authologic-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/authologic/refs/heads/main/scopes/authologic-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/authologic-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/authologic/refs/heads/main/conventions/authologic-conventions.yml
  title: ''
  type: Conventions
  url: conventions/authologic-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/authologic/refs/heads/main/conventions/authologic-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/authologic-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/authologic/refs/heads/main/errors/authologic-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/authologic-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/authologic/refs/heads/main/errors/authologic-error-codes.yml
  title: ''
  type: ErrorCodes
  url: errors/authologic-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/authologic/refs/heads/main/lifecycle/authologic-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/authologic-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.authologic.com/docs/integration/deprecations
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/authologic/refs/heads/main/conformance/authologic-conformance.yml
  title: ''
  type: Conformance
  url: conformance/authologic-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/authologic/refs/heads/main/conformance/authologic-conformance.yml
  title: ''
  type: Compliance
  url: conformance/authologic-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/authologic/refs/heads/main/security/authologic-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/authologic-trust-center.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/authologic/refs/heads/main/packages/authologic-packages.yml
  title: ''
  type: Packages
  url: packages/authologic-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/authologic/refs/heads/main/packages/authologic-packages.yml
  title: ''
  type: SDKs
  url: packages/authologic-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/authologic/refs/heads/main/components/authologic-components.yml
  title: ''
  type: Components
  url: components/authologic-components.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/authologic/refs/heads/main/sandbox/authologic-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/authologic-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/authologic/refs/heads/main/asyncapi/authologic-callbacks-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/authologic-callbacks-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/authologic/refs/heads/main/well-known/authologic-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/authologic-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/authologic/refs/heads/main/mcp/authologic-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/authologic-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/authologic/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/authologic/refs/heads/main/llms/authologic-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/authologic-llms.txt
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/authologic/refs/heads/main/plans/authologic-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/authologic-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/authologic/refs/heads/main/rate-limits/authologic-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/authologic-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/authologic/refs/heads/main/finops/authologic-finops.yml
  title: ''
  type: FinOps
  url: finops/authologic-finops.yml
- group: docs
  title: ''
  type: APIReference
  url: https://developer.authologic.com/api
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.authologic.com/
- group: operate
  title: ''
  type: Support
  url: mailto:tech-support@authologic.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://authologic.com/terms-of-use/
created: '2025-05-02'
description: Authologic is an identity verification platform providing businesses with a single API to aggregate multiple ID verification methods including government-issued digital IDs, Bank IDs, document OCR, liveness checks, and AML screening. It supports seamless KYC/KYB workflow integration for businesses across multiple countries.
features:
- description: One API integration provides access to multiple identity verification methods without separate integrations per provider.
  name: Single API Integration
- description: Native support for government-issued digital IDs and Bank IDs across multiple European countries for high-trust verification.
  name: eID and Bank ID Support
- description: Automated document scanning with OCR and biometric liveness detection to prevent spoofing and fraud.
  name: Document OCR and Liveness
- description: Integrated anti-money laundering screening against sanctions lists, PEP databases, and adverse media sources.
  name: AML Screening
- description: No-integration verification flow using a hosted link for simple verification without technical implementation.
  name: OmniLink
- description: Compose verification workflows from modular steps combining document, biometric, data, and AML checks.
  name: Modular Workflows
finops:
- name: Authologic Finops
  service_category: API
  slug: authologic-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/authologic.png
layout: provider
mcp_servers:
- description: Authologic publishes no MCP server. This is a DERIVED candidate tool list computed from the 14 operations of the published Authologic Customer API (OpenAPI 3.1.0, API version 1.1) — what an MCP server
  name: Authologic MCP Server
  slug: authologic-mcp-server
modified: '2026-09-14'
name: Authologic
nav: Providers
network: true
overview: 'Authologic publishes 9 APIs on the [APIs.io](https://apis.io/) network, including AML API, Advanced API, Affordability assessment API, and 6 more. Tagged areas include AML, Digital Identity, eID, Identity Verification, and KYB.


  The Authologic catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Authologic''s developer surface includes developer portal, documentation, getting-started guide, engineering blog, signup flow, authentication, sandbox, and 31 more developer resources.'
plans:
- name: Authologic Plans Pricing
  plan_count: 0
  slug: authologic-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Authologic Rate Limits
  slug: authologic-rate-limits
scopes:
- name: Authologic Scopes
  scope_count: 0
  slug: authologic-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 51.9
  coverage:
    artifact_dirs: 27
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 68.9
    developer_ergonomics: 73.2
    discoverability: 75.9
    operational_transparency: 15.8
  previous_composite: 51.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/authologic/refs/heads/main/screenshots/authologic-2026-06-20T172610.png
security:
- kind: authentication
  name: Authologic Authentication
  slug: authologic-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Authologic Domain Security
  slug: authologic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Authologic Trust Center
  slug: authologic-trust-center
  summary_line: ISO/IEC 27001, ISO/IEC 22301, eIDAS non-qualified trust service provider (EAA issuance)
slug: authologic
solutions:
- description: Complete KYC solution for banks, fintechs, and payment providers with AML screening and document verification.
  name: Financial Services KYC
- description: Aggregate multiple ID verification methods via single API for flexible identity assurance across user populations.
  name: Digital Identity Verification
tags:
- AML
- Digital Identity
- eID
- Identity Verification
- KYB
- KYC
- Liveness Check
use_cases:
- description: Verify customer identities during registration and onboarding for financial services, fintech, and regulated industries.
  name: Customer Onboarding KYC
- description: Combine identity verification with AML screening to meet financial institution compliance requirements.
  name: AML Compliance
- description: Verify business identities and beneficial owners for B2B onboarding and corporate due diligence.
  name: Business Verification (KYB)
- description: Verify user ages using official ID documents for age-restricted products and services.
  name: Age Verification
website: https://authologic.com/
---
