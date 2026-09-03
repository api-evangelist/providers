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
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.1
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 14
  human_in_the_loop: 5
  name: Prometeo Agentic Access
  operation_count: 26
  slug: prometeo-agentic-access
  summary_line: 26 operations · 14 acting · 5 human-in-the-loop
api_count: 1
apis:
- description: Government / fiscal data access - Colombia DIAN, Mexico SAT and CEP (payment receipt), and Uruguay BCU (central bank) filings and statements. Sandbox host fiscal.sandbox.prometeoapi.com.
  name: Prometeo Fiscal API
  slug: prometeo-fiscal-api
- baseURL: https://banking.prometeoapi.net
  baseurl_source: declared
  description: Real-time bank account verification / ownership checks.
  name: Prometeo Account Validation API
  slug: prometeo-account-validation-api
- baseURL: https://banking.prometeoapi.net
  baseurl_source: declared
  description: Bank account access, movements, transfers, credit cards, providers.
  name: Prometeo Banking API
  slug: prometeo-banking-api
- baseURL: https://banking.prometeoapi.net
  baseurl_source: declared
  description: Pay-in intents, payouts over local rails, and FX exchange.
  name: Prometeo Cross-Border API
  slug: prometeo-cross-border-api
- baseURL: https://banking.prometeoapi.net
  baseurl_source: declared
  description: Mexico CURP query and reverse query.
  name: Prometeo Identity API
  slug: prometeo-identity-api
- baseURL: https://banking.prometeoapi.net
  baseurl_source: declared
  description: Account-to-account (open banking initiated) payment intents.
  name: Prometeo Payment API
  slug: prometeo-payment-api
artifact_total: 27
asyncapis:
- description: ''
  name: Prometeo Webhooks
  slug: prometeo-webhooks
collections:
- collection_type: postman
  name: Prometeo Account Validation API
  slug: postman-prometeo-account-validation-api
- collection_type: postman
  name: Prometeo Account Validation Banking API
  slug: postman-prometeo-banking-api
- collection_type: postman
  name: Prometeo Account Validation Cross-Border API
  slug: postman-prometeo-cross-border-api
- collection_type: postman
  name: Prometeo Account Validation Identity API
  slug: postman-prometeo-identity-api
- collection_type: postman
  name: Prometeo Account Validation Payment API
  slug: postman-prometeo-payment-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Prometeo Account Validation API
  slug: open-prometeo-account-validation-api
- collection_type: open
  name: Prometeo Account Validation Banking API
  slug: open-prometeo-banking-api
- collection_type: open
  name: Prometeo Account Validation Cross-Border API
  slug: open-prometeo-cross-border-api
- collection_type: open
  name: Prometeo Account Validation Identity API
  slug: open-prometeo-identity-api
- collection_type: open
  name: Prometeo Account Validation Payment API
  slug: open-prometeo-payment-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/prometeo-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/prometeo/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/prometeo-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/prometeo-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/prometeo-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/prometeo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/prometeo-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/prometeoapi
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/prometeoapi
- group: company
  title: ''
  type: Website
  url: https://prometeoapi.com/en
- group: docs
  title: ''
  type: Documentation
  url: https://docs.prometeoapi.com
- group: commercial
  title: ''
  type: Plans
  url: plans/prometeo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/prometeo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/prometeo-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://prometeoapi.com/en/blog
- group: build
  title: ''
  type: Packages
  url: packages/prometeo-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/prometeo-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/prometeo-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/prometeo-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/prometeo-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/prometeo-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/prometeo-trust-center.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/prometeo-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/prometeo-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/prometeo-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/prometeo-conventions.yml
- group: design
  title: ''
  type: Components
  url: components/prometeo-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/prometeo-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/prometeo-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: security/prometeo-vulnerability-disclosure.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.prometeoapi.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.prometeoapi.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.prometeoapi.com/docs/gu%C3%ADa-r%C3%A1pida
- group: operate
  title: ''
  type: Support
  url: mailto:support@prometeoapi.com
- group: commercial
  title: ''
  type: Pricing
  url: https://prometeoapi.com/en/pricing
- group: start
  title: ''
  type: SignUp
  url: https://prometeoapi.com/accounts/create/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://prometeoapi.com/en/legal/msa
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://prometeoapi.com/en/legal/privacy-policy
- group: build
  title: ''
  type: Postman
  url: collections/prometeo.postman_collection.json
created: '2026-07-17'
description: Prometeo is a LatAm-founded (Uruguay) fintech infrastructure company offering a single financial API over 7,500+ banking connections across the Americas. Products span banking data access, real-time account validation, cross-border pay-in / payout / FX, account-to-account payments, Mexican CURP identity, and fiscal data (DIAN / SAT / CEP / BCU). All products authenticate with an X-API-Key header and offer a mock-data sandbox.
finops:
- name: Prometeo Finops
  service_category: Financial Services
  slug: prometeo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/prometeo.png
layout: provider
mcp_servers:
- description: ''
  name: Prometeo MCP Server
  slug: prometeo-mcp-server
modified: '2026-07-17'
name: Prometeo
nav: Providers
network: true
overview: 'Prometeo publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Account Validation API, Banking API, Cross-Border API, and 2 more. Tagged areas include Open Banking, Payments, Fintech, LatAm, and Financial Data.


  The Prometeo catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Prometeo''s developer surface includes authentication, documentation, engineering blog, sandbox, API reference, getting-started guide, support, and 33 more developer resources.'
plans:
- name: Prometeo Plans Pricing
  plan_count: 2
  slug: prometeo-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 2
  name: Prometeo Rate Limits
  slug: prometeo-rate-limits
score:
  band: strong
  composite: 55.6
  coverage:
    artifact_dirs: 26
    catalog_gap: 59.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 55.3
    commercial_clarity: 55.3
    contract_governance: 18.2
    contract_quality: 56.8
    developer_ergonomics: 68.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 42.1
  previous_composite: 55.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 40.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/prometeo/refs/heads/main/screenshots/prometeo-2026-08-17T081352.png
security:
- kind: authentication
  name: Prometeo Authentication
  slug: prometeo-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Prometeo Domain Security
  slug: prometeo-domain-security
  summary_line: no transport/DNS hardening detected
- kind: vulnerability-disclosure
  name: Prometeo Vulnerability Disclosure
  slug: prometeo-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Prometeo Trust Center
  slug: prometeo-trust-center
  summary_line: ISO 27001, SOC 2, GDPR
slug: prometeo
tags:
- Open Banking
- Payments
- Fintech
- LatAm
- Financial Data
- Account Validation
- Cross-Border
website: https://prometeoapi.com/en
---
