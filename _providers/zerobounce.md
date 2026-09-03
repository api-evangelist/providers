---
access_model:
  confidence: high
  label: Freemium self-service
  onboarding: unknown
  pricing: freemium
  public: true
  source:
  - https://www.zerobounce.net/pricing
  - https://www.zerobounce.net/members/createaccount
  - https://www.zerobounce.net/free-email-verifier
  trial: true
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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.3
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Zerobounce Agentic Access
  operation_count: 2
  slug: zerobounce-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 1
apis:
- description: Real-time and batch email validation API including credit balance, API usage, file submission and retrieval, email finder, domain search, activity data and AI scoring endpoints. Authenticated via api_
  name: ZeroBounce Email Validation API
  slug: email-validation-api
- description: 'US-region endpoint of the ZeroBounce v2 email validation API. Introduced October 2025 alongside the EU host so that, per ZeroBounce''s own documentation, "validations and other interactions only occur '
  name: ZeroBounce Email Validation API (US)
  slug: email-validation-api-us
- description: EU-region endpoint of the ZeroBounce v2 email validation API for customers requiring European data residency, where validations and interactions occur only within the European Union.
  name: ZeroBounce Email Validation API (EU)
  slug: email-validation-api-eu
- description: Asynchronous file-job surface for bulk email validation, bulk AI scoring, bulk email finder, bulk domain search, List Evaluator and Amazon S3 file operations. Runs on a separate, non-region-split host
  name: ZeroBounce Bulk API
  slug: bulk-api
- baseURL: https://members-api.zerobounce.net
  baseurl_source: declared
  description: The ZeroBounce ChatGPT-plugin validation surface — 2 operations for single and batch email validation, served from members-api.zerobounce.net. The single-validation operation accepts up to 3 unauthent
  name: ZeroBounce Validation API
  slug: zerobounce-validation-api
- description: Official ZeroBounce Model Context Protocol server, published by ZeroBounce under Apache-2.0 and distributed on npm as @zerobounce/mcp. Exposes 16 tools covering validation, AI scoring, email finder, d
  name: ZeroBounce MCP Server
  slug: mcp
artifact_total: 18
asyncapis:
- description: ''
  name: Zerobounce Webhooks
  slug: zerobounce-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ZeroBounce Validate Email plugin Validation API
  slug: open-zerobounce-validation-api
- collection_type: open
  name: ZeroBounce Validate Email plugin
  slug: open-zerobounce
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zerobounce-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/zerobounce-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/zerobounce-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/zerobounce-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zerobounce-domain-security.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/zerobounce-conformance.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/zerobounce-conformance.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zerobounce-net
- group: company
  title: ''
  type: Website
  url: https://www.zerobounce.net
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.zerobounce.net/apis
- group: docs
  title: ''
  type: Documentation
  url: https://www.zerobounce.net/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.zerobounce.net/docs/api-dashboard/api-endpoints
- group: start
  title: ''
  type: GettingStarted
  url: https://www.zerobounce.net/docs/email-validation-api-quickstart/v2-validate-emails
- group: operate
  title: ''
  type: Support
  url: https://www.zerobounce.net/contact-us
- group: commercial
  title: ''
  type: Pricing
  url: https://www.zerobounce.net/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/zerobounce-plans-pricing.yml
- group: start
  title: ''
  type: SignUp
  url: https://www.zerobounce.net/members/createaccount
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.zerobounce.net/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.zerobounce.net/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zerobounce
- group: build
  title: ''
  type: GitHub
  url: https://github.com/zerobounce
- group: company
  title: ''
  type: Blog
  url: https://www.zerobounce.net/blog/feed
- group: operate
  title: ''
  type: StatusPage
  url: https://status.zerobounce.net
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/zerobounce-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/zerobounce-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/zerobounce-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/zerobounce-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/zerobounce-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/zerobounce-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zerobounce-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/zerobounce-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/zerobounce-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/zerobounce-error-codes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/zerobounce-rate-limits.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/zerobounce-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/zerobounce-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/zerobounce-webhooks.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/zerobounce-validation-api-overlay.yaml
- group: build
  title: ''
  type: Postman
  url: collections/zerobounce-api-v2-official.postman_collection.json
created: '2026-05-11'
description: ZeroBounce is an email validation and deliverability platform that verifies email addresses, detects spam traps and abuse accounts, scores leads, and helps senders reduce bounce rates and protect sender reputation. The platform provides real-time and batch email validation, credit balance checks, file-based validation jobs, email finder, domain search, activity data, list evaluation and AI scoring through a versioned REST API. The ZeroBounce v2 API uses a per-request api_key parameter with no OAuth or scopes, and is served from region-split hosts for US and EU data residency plus a separate bulk host for asynchronous file jobs. ZeroBounce also ships an official MCP server and first-party SDKs across nine languages.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zerobounce.png
layout: provider
mcp_servers:
- description: Official ZeroBounce Model Context Protocol server. Exposes ZeroBounce email validation, AI scoring, email finder, domain search, activity data, credit and bulk-file operations as MCP tools for AI codi
  name: ZeroBounce MCP Server
  slug: zerobounce-mcp-server
modified: '2026-08-13'
name: ZeroBounce
nav: Providers
network: true
overview: 'ZeroBounce publishes 1 API on the [APIs.io](https://apis.io/) network: Validation API. Tagged areas include Email Validation, Email Deliverability, Email Verification, Marketing, and Lead Scoring.


  The ZeroBounce catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ZeroBounce''s developer surface includes documentation, API reference, getting-started guide, support, pricing, signup flow, GitHub presence, and 33 more developer resources.'
plans:
- name: Zerobounce Plans Pricing
  plan_count: 4
  slug: zerobounce-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 6
  name: Zerobounce Rate Limits
  slug: zerobounce-rate-limits
score:
  band: exemplar
  composite: 67.0
  coverage:
    artifact_dirs: 23
    catalog_gap: 54.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 49.0
    developer_ergonomics: 78.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 84.2
  previous_composite: 67.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zerobounce/refs/heads/main/screenshots/zerobounce-2026-08-17T083321.png
security:
- kind: authentication
  name: Zerobounce Authentication
  slug: zerobounce-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Zerobounce Domain Security
  slug: zerobounce-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Zerobounce Vulnerability Disclosure
  slug: zerobounce-vulnerability-disclosure
  summary_line: Intigriti
- kind: trust-center
  name: Zerobounce Trust Center
  slug: zerobounce-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR
slug: zerobounce
tags:
- Email Validation
- Email Deliverability
- Email Verification
- Marketing
- Lead Scoring
- Anti-Spam
- Data Quality
- Email Finder
- Deliverability Monitoring
- DMARC
website: https://www.zerobounce.net
---
