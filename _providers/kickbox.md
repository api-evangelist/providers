---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.3
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Kickbox Agentic Access
  operation_count: 5
  slug: kickbox-agentic-access
  summary_line: 5 operations · 1 acting
api_count: 5
apis:
- description: REST API for verifying the deliverability of email addresses in real time. Returns a result (deliverable, undeliverable, risky, unknown), a reason code, plus flags for role addresses, disposable domai
  name: Kickbox Email Verification API
  slug: verification-api
- description: Account balance and metadata.
  name: Kickbox Account API
  slug: kickbox-account-api
- description: Bulk CSV email verification.
  name: Kickbox Batch API
  slug: kickbox-batch-api
- description: Free disposable-domain lookup (no auth).
  name: Kickbox Open API
  slug: kickbox-open-api
- description: Real-time email verification.
  name: Kickbox Verification API
  slug: kickbox-verification-api
artifact_total: 19
asyncapis:
- description: ''
  name: Kickbox Batch Webhooks
  slug: kickbox-batch-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Kickbox Email Verification Account API
  slug: open-kickbox-account-api
- collection_type: open
  name: Kickbox Email Verification Account Batch API
  slug: open-kickbox-batch-api
- collection_type: open
  name: Kickbox Email Verification Account Open API
  slug: open-kickbox-open-api
- collection_type: open
  name: Kickbox Email Account Verification API
  slug: open-kickbox-verification-api
- collection_type: open
  name: Kickbox Email Verification API
  slug: open-kickbox
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kickbox-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kickbox-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kickbox-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kickbox
- group: company
  title: ''
  type: Website
  url: https://kickbox.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.kickbox.com
- group: commercial
  title: ''
  type: Pricing
  url: https://kickbox.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.kickbox.com/signup
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kickboxio
- group: operate
  title: ''
  type: Support
  url: https://articles.kickbox.com/en/collections/1840339-kickbox-help-articles
- group: operate
  title: ''
  type: HelpCenter
  url: https://articles.kickbox.com/en/collections/1840339-kickbox-help-articles
- group: operate
  title: ''
  type: Contact
  url: https://kickbox.com/contact/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.kickbox.com/llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kickbox-llms.txt
- group: company
  title: ''
  type: Blog
  url: https://blog.kickbox.com
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.kickbox.com/rss/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://kickbox.com/kickbox-for-developers/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.kickbox.com/docs/single-verification-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.kickbox.com/docs/using-the-api
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.kickbox.com/docs/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.kickbox.com/docs/privacy-policy
- group: build
  title: ''
  type: Packages
  url: packages/kickbox-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/kickbox-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/kickbox-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/kickbox-tool-crosswalk.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/kickbox-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kickbox-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kickbox-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kickbox-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.kickbox.com/
- group: design
  title: ''
  type: DataModel
  url: data-model/kickbox-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kickbox-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.kickbox.com/
- group: auth
  title: ''
  type: Compliance
  url: https://docs.kickbox.com/docs/security-and-compliance
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/kickbox-batch-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/kickbox-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kickbox-rate-limits.yml
created: '2026-05-11'
description: Kickbox is an email verification and list cleaning service that helps senders improve deliverability by detecting invalid, disposable, role-based, and risky email addresses before they enter mailing lists. The platform offers real-time single verification, bulk batch verification, and a deliverability monitoring suite. Kickbox provides a simple HTTPS REST API authenticated by API key returning structured verification results with reason codes.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kickbox.png
layout: provider
mcp_servers:
- description: ''
  name: Kickbox documentation MCP server (auth-gated)
  slug: kickbox-documentation-mcp-server-auth-gated
modified: '2026-08-13'
name: Kickbox
nav: Providers
network: true
overview: 'Kickbox publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Account API, Batch API, Open API, and 1 more. Tagged areas include Email Verification, Email Validation, Deliverability, Data Quality, and Email.


  The Kickbox catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Kickbox''s developer surface includes authentication, documentation, pricing, signup flow, support, engineering blog, API reference, and 31 more developer resources.'
plans:
- name: Kickbox Plans Pricing
  plan_count: 13
  slug: kickbox-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 2
  name: Kickbox Rate Limits
  slug: kickbox-rate-limits
score:
  band: strong
  composite: 59.8
  delta: 1.9
  facets:
    access_clarity: 69.7
    commercial_clarity: 69.7
    contract_governance: 16.7
    contract_quality: 60.5
    developer_ergonomics: 72.0
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 47.4
  previous_composite: 57.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kickbox/refs/heads/main/screenshots/kickbox-2026-06-20T184032.png
security:
- kind: authentication
  name: Kickbox Authentication
  slug: kickbox-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Kickbox Domain Security
  slug: kickbox-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Kickbox Trust Center
  slug: kickbox-trust-center
  summary_line: SOC 2, GDPR, CCPA
slug: kickbox
tags:
- Email Verification
- Email Validation
- Deliverability
- Data Quality
- Email
website: https://kickbox.com
---
