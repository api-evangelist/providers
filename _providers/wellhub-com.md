---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.3
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Wellhub Com Agentic Access
  operation_count: 10
  slug: wellhub-com-agentic-access
  summary_line: 10 operations · 4 acting
api_count: 1
apis:
- description: 'Client-facing REST API for Wellhub''s corporate customers. Syncs employee eligibility from an HR system into Wellhub using batch eligibility jobs (create, add items, submit, poll status, list errors), '
  name: Wellhub Integrations API
  slug: wellhub-integrations-api
artifact_total: 7
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wellhub-com-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wellhub-com-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wellhub-com-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://wellhub.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer-hub.wellhub.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer-hub.wellhub.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developer-hub.wellhub.com/docs/integrations/api/eligibility
- group: start
  title: ''
  type: GettingStarted
  url: https://developer-hub.wellhub.com/docs/integrations/api/getting-started
- group: operate
  title: ''
  type: Support
  url: https://helpcenter.gympass.com/en-us
- group: company
  title: ''
  type: Blog
  url: https://wellhub.com/en-us/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gympass
- group: commercial
  title: ''
  type: Pricing
  url: https://wellhub.com/en-us/companies/plans-pricing
- group: start
  title: ''
  type: Login
  url: https://clients.gympass.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://wellhub.com/en-us/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://wellhub.com/en-us/privacy/
- group: auth
  title: ''
  type: TrustCenter
  url: https://security.wellhub.com/
- group: auth
  title: ''
  type: Compliance
  url: https://security.wellhub.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wellhub-com-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/wellhub-com-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/wellhub-com-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/wellhub-com-problem-types.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/wellhub-com-job-error-codes.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/wellhub-com-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/wellhub-com-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/wellhub-com-conformance.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/wellhub-com-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/wellhub-com-data-model.yml
- group: build
  title: ''
  type: Examples
  url: examples/wellhub-com-examples.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/wellhub-com-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/wellhub-com-trust-center.yml
created: '2026-08-04'
description: Wellhub (formerly Gympass) is a corporate wellbeing platform that gives employees a single subscription covering gyms, studios, classes, personal trainers, and fitness, mindfulness, nutrition, therapy and sleep apps across the Americas and Europe. For the companies that buy the benefit, Wellhub publishes a client-facing Integrations API — an OAuth 2.0 client-credentials REST API on api.clients.wellhub.com that syncs employee eligibility from an HR system into Wellhub so people gain access on hire and lose it on termination. Eligibility is modelled as batch jobs (create a job, add up to 500 items per request, submit, poll status, list errors), alongside cursor-paginated endpoints for listing entity companies and employees. Wellhub also offers an SFTP file-exchange integration for eligibility, payroll deduction and reporting files, and an SSO integration. A published OpenAPI 3.0.3 contract, a documented sandbox environment, and per-endpoint rate limits back the REST surface.
image: https://assets-cdn.wellhub.com/images/mep-cms/EN_UK_IT_meta_d8c2bf8ba9.png
layout: provider
modified: '2026-08-04'
name: Wellhub
nav: Providers
network: true
overview: 'Wellhub publishes 1 API on the [APIs.io](https://apis.io/) network: Integrations API. Tagged areas include Company, corporate-wellness, employee-benefits, human-resources, and hr-tech.


  Wellhub''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 24 more developer resources.'
random_paper: 102
rate_limits:
- limit_count: 10
  name: Wellhub Com Rate Limits
  slug: wellhub-com-rate-limits
score:
  band: strong
  composite: 57.2
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 60.2
    developer_ergonomics: 60.3
    discoverability: 87.0
    governance: 20.8
    operational_transparency: 52.6
  previous_composite: 57.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Wellhub Com Authentication
  slug: wellhub-com-authentication
  summary_line: http/oauth2 · 1 scheme
- kind: domain-security
  name: Wellhub Com Domain Security
  slug: wellhub-com-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Wellhub Com Vulnerability Disclosure
  slug: wellhub-com-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Wellhub Com Trust Center
  slug: wellhub-com-trust-center
  summary_line: ISO/IEC 27001, PCI DSS, GDPR, CCPA, LGPD
slug: wellhub-com
tags:
- Company
- corporate-wellness
- employee-benefits
- human-resources
- hr-tech
- eligibility
- workforce
- fitness
- wellbeing
- payroll
- sftp
- hris-integration
website: https://wellhub.com/
---
