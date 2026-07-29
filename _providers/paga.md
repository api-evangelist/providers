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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: documented
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 50.7
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 15
  human_in_the_loop: 8
  name: Paga Agentic Access
  operation_count: 23
  slug: paga-agentic-access
  summary_line: 23 operations · 15 acting · 8 human-in-the-loop
api_count: 5
apis:
- description: OAuth-based hosted checkout that lets third parties charge a customer's Paga wallet and read account/merchant details after the customer authorizes access. Documented separately from the hash-authenti
  name: Paga Connect
  slug: paga-connect-api
- description: Disbursements, airtime/data, merchant payments, deposits, onboarding.
  name: Paga Business API
  slug: paga-business-api
- description: NGN collections - payment requests and persistent payment accounts.
  name: Paga Collect API
  slug: paga-collect-api
- description: Bank-account mandate tokenization and recurring debits.
  name: Paga Direct Debit API
  slug: paga-direct-debit-api
- description: Look-up operations - banks, mobile operators, status.
  name: Paga Reference API
  slug: paga-reference-api
artifact_total: 19
asyncapis:
- description: ''
  name: Paga Webhooks
  slug: paga-webhooks
collections:
- collection_type: postman
  name: Paga Developer Business API
  slug: postman-paga-business-api
- collection_type: postman
  name: Paga Developer Business Collect API
  slug: postman-paga-collect-api
- collection_type: postman
  name: Paga Developer Business Direct Debit API
  slug: postman-paga-direct-debit-api
- collection_type: postman
  name: Paga Developer Business Reference API
  slug: postman-paga-reference-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/paga/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/paga-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/paga-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/paga-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/paga-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/paga-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Paga-Developer-Community
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/paga-tech
- group: company
  title: ''
  type: Website
  url: https://www.paga.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer-docs.paga.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/paga-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/paga-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/paga-finops.yml
- group: build
  title: ''
  type: Packages
  url: packages/paga-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/paga-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/paga-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/paga-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/paga-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/paga-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/paga-trust-center.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/paga-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/paga-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.paga.com
- group: start
  title: ''
  type: Sandbox
  url: sandbox/paga-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/paga-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/paga-conventions.yml
- group: design
  title: ''
  type: Components
  url: components/paga-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/paga-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/paga-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer-docs.paga.com/
- group: start
  title: ''
  type: Quickstart
  url: https://developer-docs.paga.com/docs/create-an-account
- group: operate
  title: ''
  type: Support
  url: https://www.paga.com/contact
- group: company
  title: ''
  type: Blog
  url: https://paga.blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.paga.com/terms
created: '2026-07-17'
description: Paga (Pagatech Financial Services Limited) is a Nigerian mobile-money and payments company founded in 2009 and licensed by the Central Bank of Nigeria. Its developer platform exposes REST APIs - the Business API, Collect API, and Direct Debit API - for disbursements, airtime/data and bill payments, bank deposits, and NGN collections via payment requests and persistent (NUBAN) account numbers. Authentication combines a principal/credential key pair with a per-request SHA-512 hash header.
finops:
- name: Paga Finops
  service_category: Payments and Financial Services
  slug: paga-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/paga.png
layout: provider
mcp_servers:
- description: ''
  name: paga-mcp.yml
  slug: paga-mcpyml
modified: '2026-07-17'
name: Paga
nav: Providers
network: true
overview: 'Paga publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Business API, Collect API, Direct Debit API, and 1 more. Tagged areas include Payments, Mobile Money, Fintech, Collections, and Nigeria.


  The Paga catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Paga''s developer surface includes authentication, documentation, sandbox, quickstart, support, engineering blog, and 29 more developer resources.'
plans:
- name: Paga Plans Pricing
  plan_count: 2
  slug: paga-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 2
  name: Paga Rate Limits
  slug: paga-rate-limits
score:
  band: strong
  composite: 58.2
  delta: -2.0
  facets:
    commercial_clarity: 55.3
    contract_quality: 63.6
    developer_ergonomics: 66.8
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 50.0
  previous_composite: 60.2
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
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 62.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Paga Authentication
  slug: paga-authentication
  summary_line: http/apiKey · 4 schemes
- kind: domain-security
  name: Paga Domain Security
  slug: paga-domain-security
  summary_line: no transport/DNS hardening detected
- kind: vulnerability-disclosure
  name: Paga Vulnerability Disclosure
  slug: paga-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Paga Trust Center
  slug: paga-trust-center
  summary_line: PCI DSS, CBN licensed (Mobile Money Operator), NDPR (Nigeria Data Protection Regulation)
slug: paga
tags:
- Payments
- Mobile Money
- Fintech
- Collections
- Nigeria
website: https://www.paga.com/
---
