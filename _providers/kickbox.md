---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
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
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Kickbox Agentic Access
  operation_count: 5
  slug: kickbox-agentic-access
  summary_line: 5 operations · 1 acting
api_count: 2
apis:
- description: REST API for verifying the deliverability of email addresses in real time. Returns a result (deliverable, undeliverable, risky, unknown), a reason code, plus flags for role addresses, disposable domai
  name: Kickbox Email Verification API
  slug: verification-api
- baseURL: https://api.kickbox.com/v2
  baseurl_source: declared
  description: Account balance and metadata.
  name: Kickbox Account API
  slug: kickbox-account-api
- baseURL: https://api.kickbox.com/v2
  baseurl_source: declared
  description: Bulk CSV email verification.
  name: Kickbox Batch API
  slug: kickbox-batch-api
- baseURL: https://open.kickbox.com/v1
  baseurl_source: declared
  description: Free disposable-domain lookup (no auth).
  name: Kickbox Open API
  slug: kickbox-open-api
- baseURL: https://api.kickbox.com/v2
  baseurl_source: declared
  description: Real-time email verification.
  name: Kickbox Verification API
  slug: kickbox-verification-api
- baseURL: https://api.kickbox.com/v2
  baseurl_source: declared
  description: The Disposable API from Kickbox — 1 operation(s) for disposable.
  name: Kickbox Disposable API
  slug: kickbox-disposable-api
artifact_total: 24
asyncapis:
- description: ''
  name: Kickbox Batch Webhooks
  slug: kickbox-batch-webhooks
collections:
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
- group: other
  href: https://artifacts.apis.io/kickbox/capabilities/kickbox-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/kickbox-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/kickbox/agentic-access/kickbox-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/kickbox-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/kickbox/security/kickbox-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kickbox-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/kickbox/authentication/kickbox-authentication.yml
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
  href: https://artifacts.apis.io/kickbox/llms/kickbox-llms.txt
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
  href: https://artifacts.apis.io/kickbox/packages/kickbox-packages.yml
  title: ''
  type: Packages
  url: packages/kickbox-packages.yml
- group: build
  href: https://artifacts.apis.io/kickbox/packages/kickbox-packages.yml
  title: ''
  type: SDKs
  url: packages/kickbox-packages.yml
- group: agent
  href: https://artifacts.apis.io/kickbox/mcp/kickbox-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/kickbox-mcp.yml
- group: build
  href: https://artifacts.apis.io/kickbox/mcp/kickbox-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/kickbox-tool-crosswalk.yml
- group: start
  href: https://artifacts.apis.io/kickbox/sandbox/kickbox-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/kickbox-sandbox.yml
- group: design
  href: https://artifacts.apis.io/kickbox/conventions/kickbox-conventions.yml
  title: ''
  type: Conventions
  url: conventions/kickbox-conventions.yml
- group: design
  href: https://artifacts.apis.io/kickbox/errors/kickbox-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/kickbox-problem-types.yml
- group: design
  href: https://artifacts.apis.io/kickbox/lifecycle/kickbox-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/kickbox-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.kickbox.com/
- group: design
  href: https://artifacts.apis.io/kickbox/data-model/kickbox-data-model.yml
  title: ''
  type: DataModel
  url: data-model/kickbox-data-model.yml
- group: design
  href: https://artifacts.apis.io/kickbox/conformance/kickbox-conformance.yml
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
  href: https://artifacts.apis.io/kickbox/asyncapi/kickbox-batch-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/kickbox-batch-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/kickbox/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://artifacts.apis.io/kickbox/plans/kickbox-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/kickbox-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/kickbox/rate-limits/kickbox-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/kickbox-rate-limits.yml
created: '2026-05-11'
description: Kickbox is an email verification and list cleaning service that helps senders improve deliverability by detecting invalid, disposable, role-based, and risky email addresses before they enter mailing lists. The platform offers real-time single verification, bulk batch verification, and a deliverability monitoring suite. Kickbox provides a simple HTTPS REST API authenticated by API key returning structured verification results with reason codes.
finops:
- has_sources: true
  method: derived
  name: Kickbox Finops
  primary_unit: 500 verifications
  service_category: ''
  slug: kickbox-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kickbox.png
layout: provider
mcp_servers:
- description: Remote MCP server at docs.kickbox.com over HTTP.
  name: Kickbox documentation MCP server (auth-gated)
  slug: kickbox-docs
modified: '2026-08-13'
name: Kickbox
nav: Providers
network: true
overview: 'Kickbox publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Batch API, Open API, and 3 more. Tagged areas include Email Verification, Deliverability, Data Quality, and Email.


  The Kickbox catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Kickbox''s developer surface includes authentication, documentation, pricing, signup flow, support, engineering blog, API reference, and 32 more developer resources.'
plans:
- name: Kickbox Plans Pricing
  plan_count: 14
  slug: kickbox-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 2
  name: Kickbox Rate Limits
  slug: kickbox-rate-limits
rules:
- authorship: generated
  effective_rule_count: 102
  extends:
  - spectral:oas
  name: Kickbox API Rules
  rule_count: 61
  severity_counts:
    error: 51
    hint: 0
    info: 9
    warn: 1
  slug: kickbox-rules
score:
  band: strong
  composite: 62.6
  coverage:
    artifact_dirs: 30
    catalog_earned: 59.5
    catalog_earned_first_party: 20.0
    catalog_gap: 55.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 3.7
  facets:
    access_clarity: 86.8
    contract_governance: 18.2
    contract_quality: 53.8
    developer_ergonomics: 78.0
    discoverability: 66.7
    operational_transparency: 47.4
  previous_composite: 58.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 80.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/kickbox/kickbox-2026-06-20T184032.png
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
skill_count: 3
skills:
- name: Screen a signup form with Kickbox
  slug: kickbox-screen-signup-form
- name: Verify an email list with the Kickbox batch API
  slug: kickbox-verify-list-in-batch
- name: Verify a single email address with Kickbox
  slug: kickbox-verify-single-address
slug: kickbox
tags:
- Email Verification
- Deliverability
- Data Quality
- Email
website: https://kickbox.com
---
