---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.5
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 55
  human_in_the_loop: 2
  name: Unqork Agentic Access
  operation_count: 93
  slug: unqork-agentic-access
  summary_line: 93 operations · 55 acting · 2 human-in-the-loop
api_count: 1
apis:
- description: 'Unqork''s customer-facing REST API, based on open standards, for setting and retrieving module submission data and controlling other aspects of an Unqork environment. 93 operations across Submissions, '
  name: Unqork Customer API
  slug: unqork-customer-api
artifact_total: 9
asyncapis:
- description: ''
  name: Unqork Webhooks
  slug: unqork-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/unqork-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/unqork-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://unqork.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.unqork.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.unqork.io/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.unqork.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.unqork.io/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://community.unqork.com/
- group: company
  title: ''
  type: Blog
  url: https://unqork.com/resource-center/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/unqork-external
- group: start
  title: ''
  type: SignUp
  url: https://community.unqork.com/member/register
- group: commercial
  title: ''
  type: Pricing
  url: https://unqork.com/pricing-meeting-request/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://unqork.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://unqork.com/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.unqork.com/
- group: auth
  title: ''
  type: Security
  url: https://unqork.com/security/
- group: auth
  title: ''
  type: Compliance
  url: https://unqork.com/security-compliance/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.unqork.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.unqork.io/docs/unqork-release-notes
- group: learn
  title: ''
  type: Training
  url: https://academy.unqork.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/unqork-llms.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/unqork-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/unqork-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/unqork-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/unqork-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/unqork-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/unqork-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/unqork-components.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/unqork-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-31'
description: Unqork is an enterprise application development platform — a no-code / "codeless" platform-as-a-service used by banks, insurers, healthcare organizations and government agencies to build and operate complex, regulated business applications without hand-written application code. Creators assemble applications from modules, workflows, components and data models in the Unqork Designer, and the platform exposes a REST Customer API (documented as OpenAPI 3.0.3 at developers.unqork.io) that lets external systems manage submissions, modules, applications, workflows, users, groups, promotions, transforms, global variables and API access credentials in an Unqork environment. The API is served per-tenant at https://{subdomain}.unqork.io/api/1.0, secured with OAuth 2.0 client-credentials and password grants issued through API Access Management, and the platform ships on a quarterly GA release cadence with weekly patch releases.
image: https://developers.unqork.io/unqork-logo.png
layout: provider
modified: '2026-07-31'
name: Unqork
nav: Providers
network: true
overview: 'Unqork publishes 1 API on the [APIs.io](https://apis.io/) network: Customer API. Tagged areas include Company, No-Code, Low-Code, Application Development, and Enterprise Software.


  The Unqork catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Unqork''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, pricing, and 23 more developer resources.'
random_paper: 7
rate_limits:
- limit_count: 2
  name: Unqork Rate Limits
  slug: unqork-rate-limits
scopes:
- name: Unqork Scopes
  scope_count: 1
  slug: unqork-scopes
  summary_line: 1 scope · clientCredentials/password
score:
  band: strong
  composite: 59.4
  facets:
    commercial_clarity: 60.5
    contract_quality: 56.7
    developer_ergonomics: 49.5
    discoverability: 87.0
    governance: 20.8
    operational_transparency: 76.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 71.2
  schema_version: 0.9
  scored_at: '2026-08-03'
security:
- kind: authentication
  name: Unqork Authentication
  slug: unqork-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Unqork Domain Security
  slug: unqork-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Unqork Vulnerability Disclosure
  slug: unqork-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Unqork Trust Center
  slug: unqork-trust-center
  summary_line: SOC 2 Type II, ISO/IEC 27001:2013, HIPAA, FedRAMP, GDPR
slug: unqork
tags:
- Company
- No-Code
- Low-Code
- Application Development
- Enterprise Software
- Platform as a Service
- Workflow
- Financial Services
- Insurance
- Government
- Application Modernization
website: https://unqork.com/
---
