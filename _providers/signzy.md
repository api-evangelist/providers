---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
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
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
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
  score: 23.6
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Signzy Agentic Access
  operation_count: 6
  slug: signzy-agentic-access
  summary_line: 6 operations · 5 acting
api_count: 1
apis:
- baseURL: https://api.signzy.app
  baseurl_source: declared
  description: The Authentication API from Signzy — 2 operation(s) for authentication.
  name: Signzy Authentication API
  slug: signzy-authentication-api
- baseURL: https://api.signzy.app
  baseurl_source: declared
  description: The Banking API from Signzy — 1 operation(s) for banking.
  name: Signzy Banking API
  slug: signzy-banking-api
- baseURL: https://api.signzy.app
  baseurl_source: declared
  description: The Identity (India) API from Signzy — 2 operation(s) for identity (india).
  name: Signzy Identity (India) API
  slug: signzy-identity-india-api
- baseURL: https://api.signzy.app
  baseurl_source: declared
  description: The Identity (US) API from Signzy — 1 operation(s) for identity (us).
  name: Signzy Identity (US) API
  slug: signzy-identity-us-api
artifact_total: 22
collections:
- collection_type: postman
  name: Signzy Verification Authentication API
  slug: postman-signzy-authentication-api
- collection_type: postman
  name: Signzy Verification Authentication Banking API
  slug: postman-signzy-banking-api
- collection_type: postman
  name: Signzy Verification Authentication Identity (India) API
  slug: postman-signzy-identity-india-api
- collection_type: postman
  name: Signzy Verification Authentication Identity (US) API
  slug: postman-signzy-identity-us-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Signzy Verification Authentication API
  slug: open-signzy-authentication-api
- collection_type: open
  name: Signzy Verification Authentication Banking API
  slug: open-signzy-banking-api
- collection_type: open
  name: Signzy Verification Authentication Identity (India) API
  slug: open-signzy-identity-india-api
- collection_type: open
  name: Signzy Verification Authentication Identity (US) API
  slug: open-signzy-identity-us-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/signzy/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/signzy-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/signzy-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/signzy-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/signzy-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/signzy-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/signzy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/signzy
- group: company
  title: ''
  type: Website
  url: https://www.signzy.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.signzy.com
- group: commercial
  title: ''
  type: Plans
  url: plans/signzy-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/signzy-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/signzy-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.signzy.com/blogs
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/signzy-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/signzy-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/signzy-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/signzy-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/signzy-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/signzy-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/signzy-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/signzy-trust-center.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/signzy-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/signzy-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.signzy.com
- group: design
  title: ''
  type: Conventions
  url: conventions/signzy-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/signzy-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/signzy-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.signzy.com
- group: docs
  title: ''
  type: APIReference
  url: https://www.signzy.com/us/verification-api-marketplace/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.signzy.com/getting-started
- group: operate
  title: ''
  type: Support
  url: https://www.signzy.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.signzy.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.signzy.com/privacy-policy/
- group: start
  title: ''
  type: SignUp
  url: https://www.signzy.com/contact
- group: build
  title: ''
  type: Postman
  url: collections/signzy.postman_collection.json
created: '2026-07-17'
description: Signzy is a global identity verification, KYC, KYB and AML compliance platform founded in Bengaluru, India in 2015. Its API marketplace exposes 240+ bespoke verification building blocks - document OCR, liveness and face match, deepfake detection, Aadhaar/PAN and other India checks, US ID and business verification, AML/sanctions/PEP screening, bank verification, Video KYC and Aadhaar eSign - behind a single token-authenticated REST API across India, the US, the Middle East and APAC.
finops:
- name: Signzy Finops
  service_category: Identity and Compliance
  slug: signzy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/signzy.png
layout: provider
mcp_servers:
- description: ''
  name: Signzy MCP Server
  slug: signzy-mcp-server
modified: '2026-07-17'
name: Signzy
nav: Providers
network: true
overview: 'Signzy publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Banking API, Identity (India) API, and 1 more. Tagged areas include Identity Verification, KYC, KYB, AML, and Onboarding.


  Signzy''s developer surface includes authentication, documentation, engineering blog, sandbox, API reference, getting-started guide, support, and 30 more developer resources.'
plans:
- name: Signzy Plans Pricing
  plan_count: 2
  slug: signzy-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 3
  name: Signzy Rate Limits
  slug: signzy-rate-limits
score:
  band: strong
  composite: 55.3
  coverage:
    artifact_dirs: 23
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 78.9
    commercial_clarity: 78.9
    contract_governance: 4.5
    contract_quality: 54.8
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 34.2
  previous_composite: 55.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/signzy/refs/heads/main/screenshots/signzy-2026-08-17T081859.png
security:
- kind: authentication
  name: Signzy Authentication
  slug: signzy-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Signzy Domain Security
  slug: signzy-domain-security
  summary_line: HSTS
- kind: vulnerability-disclosure
  name: Signzy Vulnerability Disclosure
  slug: signzy-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Signzy Trust Center
  slug: signzy-trust-center
  summary_line: ISO 27001, SOC 2, GDPR, FATF-aligned
slug: signzy
tags:
- Identity Verification
- KYC
- KYB
- AML
- Onboarding
- Compliance
- RegTech
website: https://www.signzy.com/
---
