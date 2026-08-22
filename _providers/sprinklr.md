---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 45.6
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: RESTful APIs for integrating with the Sprinklr Unified-CXM platform, covering social listening, publishing, reporting, user provisioning, digital asset management, and webhook subscriptions across 30+
  name: Sprinklr API
  slug: sprinklr-api
artifact_total: 10
asyncapis:
- description: ''
  name: Sprinklr Webhooks
  slug: sprinklr-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/sprinklr-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sprinklr-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sprinklr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sprinklr.com
- group: docs
  title: ''
  type: Documentation
  url: https://dev.sprinklr.com/api-overview
- group: start
  title: ''
  type: GettingStarted
  url: https://dev.sprinklr.com/getting-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sprinklr-inc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sprinklr
- group: company
  title: ''
  type: Blog
  url: https://www.sprinklr.com/blog/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sprinklr.com/
- group: other
  title: ''
  type: X
  url: https://x.com/sprinklr
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.sprinklr.com/
- group: docs
  title: ''
  type: APIReference
  url: https://dev.sprinklr.com/api2-0
- group: start
  title: ''
  type: SignUp
  url: https://dev.sprinklr.com/login
- group: operate
  title: ''
  type: Support
  url: https://www.sprinklr.com/help/
- group: operate
  title: ''
  type: Community
  url: https://community.sprinklr.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sprinklr.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sprinklr.com/privacy/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/sprinklr-api/sprinklr-public-api-collections/overview
- group: auth
  title: ''
  type: Security
  url: https://www.sprinklr.com/responsible-disclosure/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.sprinklr.com/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sprinklr-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/sprinklr-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sprinklr-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/sprinklr-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/sprinklr-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/sprinklr-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sprinklr-mcp.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/sprinklr-changelog.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sprinklr-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sprinklr-conventions.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sprinklr-authentication.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sprinklr-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sprinklr-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/sprinklr-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/sprinklr-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/sprinklr-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sprinklr-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/sprinklr/refs/heads/main/plans/sprinklr-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/sprinklr/refs/heads/main/rate-limits/sprinklr-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/sprinklr/refs/heads/main/finops/sprinklr-finops.yml
created: '2026-06-13'
description: Sprinklr is a unified customer experience management (Unified-CXM) platform offering REST APIs for social media management, customer service, marketing, and advertising across 30+ digital channels. APIs support listening, publishing, reporting, user provisioning, digital asset management, and webhook integrations, all secured via OAuth 2.0 and accessible to enterprise license holders.
finops:
- name: Sprinklr Finops
  service_category: ''
  slug: sprinklr-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sprinklr.png
layout: provider
mcp_servers:
- description: ''
  name: sprinklr-mcp.yml
  slug: sprinklr-mcpyml
modified: '2026-08-12'
name: Sprinklr
nav: Providers
network: true
overview: 'Sprinklr publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Social Media Management, Customer Experience, Customer Service, Marketing, and Advertising.


  The Sprinklr catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Sprinklr''s developer surface includes documentation, getting-started guide, engineering blog, API reference, signup flow, support, CLI, and 34 more developer resources.'
plans:
- name: Sprinklr Plans Pricing
  plan_count: 5
  slug: sprinklr-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 2
  name: Sprinklr Rate Limits
  slug: sprinklr-rate-limits
score:
  band: developing
  composite: 49.2
  delta: -18.7
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 45.1
    developer_ergonomics: 26.2
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 50.0
  previous_composite: 67.9
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/sprinklr/refs/heads/main/screenshots/sprinklr-2026-06-20T194419.png
security:
- kind: authentication
  name: Sprinklr Authentication
  slug: sprinklr-authentication
  summary_line: oauth2/apiKey/mutualTLS · 5 schemes
- kind: domain-security
  name: Sprinklr Domain Security
  slug: sprinklr-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Sprinklr Vulnerability Disclosure
  slug: sprinklr-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Sprinklr Trust Center
  slug: sprinklr-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, FedRAMP, GDPR
slug: sprinklr
tags:
- Social Media Management
- Customer Experience
- Customer Service
- Marketing
- Advertising
- Listening
- Publishing
- Reporting
- Unified CXM
website: https://www.sprinklr.com
---
