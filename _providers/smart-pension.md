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
    well_known_catalog: true
  schema_version: 0.2
  score: 48.9
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 180
  human_in_the_loop: 0
  name: Smart Pension Agentic Access
  operation_count: 383
  slug: smart-pension-agentic-access
  summary_line: 383 operations · 180 acting
api_count: 1
apis:
- description: The public REST API behind the Keystone platform and the Smart Pension UK master trust. It exposes the same operations Smart's own employer, employee and adviser portals consume — companies, employees
  name: Keystone API
  slug: keystone-api
artifact_total: 8
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/smart-pension-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/smart-pension-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.smartpension.co.uk/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.autoenrolment.co.uk/smart
- group: docs
  title: ''
  type: Documentation
  url: https://developers.autoenrolment.co.uk/smart
- group: docs
  title: ''
  type: APIReference
  url: https://developers.autoenrolment.co.uk/smart
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.autoenrolment.co.uk/smart/7756f9f9959a5-getting-started
- group: operate
  title: ''
  type: Support
  url: https://www.smartpension.co.uk/support/en/
- group: company
  title: ''
  type: Blog
  url: https://www.smartpension.co.uk/news-and-insights
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/smartpension
- group: commercial
  title: ''
  type: Pricing
  url: https://www.smartpension.co.uk/charges
- group: start
  title: ''
  type: SignUp
  url: https://partner.autoenrolment.co.uk/partners/sign-up
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.smartpension.co.uk/legal-compliance-pages/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.smartpension.co.uk/legal-compliance-pages/privacy-notice
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/smart-pension-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/smart-pension-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/smart-pension-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/smart-pension-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/smart-pension-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/smart-pension-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/smart-pension-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/smart-pension-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.smart.co/
- group: auth
  title: ''
  type: TrustCenter
  url: security/smart-pension-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/smart-pension-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.smart.co/footer/responsible-disclosure-program-policy
- group: start
  title: ''
  type: Sandbox
  url: sandbox/smart-pension-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/smart-pension-data-model.yml
- group: build
  title: ''
  type: Examples
  url: examples/smart-pension-keystone-examples.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/smart-pension-keystone-overlay.yaml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/smart-pension-well-known.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/smart-pension-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/smart-pension-packages.yml
created: '2026-08-05'
description: Smart Pension is a UK defined contribution workplace pension master trust operated by Smart Pension Limited (Smart Group), managing pensions for millions of UK savers on behalf of over 90,000 employers. Its API surface is the Keystone API — the same public REST API that powers Smart's own employer, employee and adviser portals — published by Keystone, Smart's proprietary savings administration platform, which also runs retirement solutions for financial institutions and governments outside the UK. The API lets payroll software, HR and employee-benefits platforms, advisers and banking apps create and manage companies (employers), employees (members), contributions, assessment and auto-enrolment data, postponements, opt-ins and opt-outs, valuations, funds and bank details, either as a full integration that provisions schemes end to end or as a light integration that posts PAPDIS contribution files. Authentication is OAuth 2.0 (authorization code for user-context apps, client credentials
  for machine-to-machine partners), with three sandboxed environments and self-serve partner registration.
image: https://cdn.prod.website-files.com/5ce68aba5375cabb8f952335/5d8a243dcd466e77cc8dc3b6_Z-V12-Social-GeneralTile.png
layout: provider
modified: '2026-08-05'
name: Smart Pension
nav: Providers
network: true
overview: 'Smart Pension publishes 1 API on the [APIs.io](https://apis.io/) network: Keystone API. Tagged areas include pensions, retirement, workplace-pension, auto-enrolment, and payroll.


  Smart Pension''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 27 more developer resources.'
random_paper: 4
rate_limits:
- limit_count: 4
  name: Smart Pension Rate Limits
  slug: smart-pension-rate-limits
scopes:
- name: Smart Pension Scopes
  scope_count: 41
  slug: smart-pension-scopes
  summary_line: 41 scopes · authorizationCode/clientCredentials
score:
  band: strong
  composite: 56.5
  delta: 9.1
  facets:
    commercial_clarity: 60.5
    contract_quality: 51.9
    developer_ergonomics: 60.3
    discoverability: 87.0
    governance: 20.8
    operational_transparency: 63.2
  previous_composite: 47.4
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
  trend: rising
security:
- kind: authentication
  name: Smart Pension Authentication
  slug: smart-pension-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Smart Pension Domain Security
  slug: smart-pension-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Smart Pension Vulnerability Disclosure
  slug: smart-pension-vulnerability-disclosure
  summary_line: Intigriti · security.txt · contact published
- kind: trust-center
  name: Smart Pension Trust Center
  slug: smart-pension-trust-center
  summary_line: ISO 27001:2022, SOC 2 Type 2
slug: smart-pension
tags:
- pensions
- retirement
- workplace-pension
- auto-enrolment
- payroll
- fintech
- financial-services
- united-kingdom
- master-trust
- employee-benefits
- contributions
- papdis
website: https://www.smartpension.co.uk/
---
