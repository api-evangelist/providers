---
access_model:
  confidence: high
  label: Public
  onboarding: unknown
  pricing: unknown
  public: true
  source:
  - https://www.stackmoxie.com/pricing/
  - https://api.stackmoxie.com/
  trial: true
  try_now: true
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
    error_semantics: verified
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
  score: 26.4
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 23
  human_in_the_loop: 0
  name: Stack Moxie Agentic Access
  operation_count: 43
  slug: stack-moxie-agentic-access
  summary_line: 43 operations · 23 acting
api_count: 2
apis:
- baseURL: https://app.stackmoxie.com/api/
  baseurl_source: declared
  description: Use these calls to provision Organizations (e.g. for your own clients/customers), and automatically grant them (or your own team members) access.
  name: 'Stack Moxie How To: Administer API'
  slug: stack-moxie-how-to-administer-api
- baseURL: https://app.stackmoxie.com/api/
  baseurl_source: declared
  description: Use these calls to Schedule Scenario runs.
  name: 'Stack Moxie How To: Automate API'
  slug: stack-moxie-how-to-automate-api
- baseURL: https://app.stackmoxie.com/api/
  baseurl_source: declared
  description: Use these calls to connect an Organization with Marketing/Sales technologies supported by Stack Moxie.
  name: 'Stack Moxie How To: Integrate API'
  slug: stack-moxie-how-to-integrate-api
- baseURL: https://app.stackmoxie.com/api/
  baseurl_source: declared
  description: Use these calls to organize your test Scenarios into Folders.
  name: 'Stack Moxie How To: Organize API'
  slug: stack-moxie-how-to-organize-api
- baseURL: https://app.stackmoxie.com/api/
  baseurl_source: declared
  description: Use these calls to define test Scenarios, Run them, and retrieve their results.
  name: 'Stack Moxie How To: Test API'
  slug: stack-moxie-how-to-test-api
artifact_total: 12
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/stack-moxie-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/stack-moxie-authentication.yml
- group: docs
  title: ''
  type: APIReference
  url: https://api.stackmoxie.com/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/stack-moxie-rest-api-openapi.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/stack-moxie-rest-api-overlay.yaml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/stack-moxie-problem-types.yml
- group: design
  title: ''
  type: ErrorCodes
  url: errors/stack-moxie-outcome-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/stack-moxie-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/stack-moxie-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/stack-moxie-conformance.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/stack-moxie-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/stack-moxie-plans-pricing.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: SDKs
  url: packages/stack-moxie-packages.yml
- group: company
  title: ''
  type: Website
  url: https://stackmoxie.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://crank.run
- group: docs
  title: ''
  type: Documentation
  url: https://app.stackmoxie.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://crank.run
- group: operate
  title: ''
  type: Support
  url: https://www.stackmoxie.com/support/
- group: company
  title: ''
  type: Blog
  url: https://www.stackmoxie.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.stackmoxie.com/blog/feed/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.stackmoxie.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.stackmoxie.com
- group: start
  title: ''
  type: Login
  url: https://app.stackmoxie.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://app.stackmoxie.com/docs/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.stackmoxie.com/privacypolicy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/run-crank
- group: operate
  title: ''
  type: StatusPage
  url: https://www.stackmoxie.com/app-status/
- group: build
  title: ''
  type: CLI
  url: cli/stack-moxie-cli.yml
- group: other
  title: ''
  type: Protobuf
  url: grpc/stack-moxie-cog.proto
- group: build
  title: ''
  type: Packages
  url: packages/stack-moxie-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/stack-moxie-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/stack-moxie-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/stack-moxie-llms.txt
- group: auth
  title: ''
  type: Compliance
  url: https://www.stackmoxie.com/security/
- group: auth
  title: ''
  type: Security
  url: https://www.stackmoxie.com/security/
- group: auth
  title: ''
  type: TrustCenter
  url: security/stack-moxie-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/stack-moxie-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stack-moxie-domain-security.yml
created: '2026-07-17'
description: 'Stack Moxie is a revenue-observability platform that provides continuous testing and monitoring for AI, marketing, and RevOps technology stacks. It watches integrated SaaS platforms end-to-end, catches outages, broken automations, and email-deliverability issues before they become revenue incidents, and QAs campaign launches so teams ship error-free. It ships two developer surfaces: a hosted REST API (OpenAPI 3.0.1, 43 operations, JWT bearer auth, base https://app.stackmoxie.com/api/) for creating, running, scheduling and monitoring test Scenarios programmatically; and the open-source Crank CLI - a no-code BDD test runner - with its ecosystem of gRPC "Cog" plugins for Salesforce, Marketo, Pardot, Eloqua, HubSpot, Dynamics, OpenAI, web, inbox, DNS and more.'
image: https://stackmoxie.com/favicon.ico
layout: provider
modified: '2026-08-14'
name: Stack Moxie
nav: Providers
network: true
overview: 'Stack Moxie publishes 5 APIs on the [APIs.io](https://apis.io/) network, including How To: Administer API, How To: Automate API, How To: Integrate API, and 2 more. Tagged areas include Company, Revenue Operations, Marketing Operations, Observability, and Monitoring.


  Stack Moxie''s developer surface includes authentication, API reference, documentation, getting-started guide, support, engineering blog, pricing, and 32 more developer resources.'
plans:
- name: Stack Moxie Plans Pricing
  plan_count: 4
  slug: stack-moxie-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Stack Moxie Rate Limits
  slug: stack-moxie-rate-limits
score:
  band: strong
  composite: 59.3
  coverage:
    artifact_dirs: 22
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 4.5
    contract_quality: 52.0
    developer_ergonomics: 73.2
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 44.7
  previous_composite: 59.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/stack-moxie/refs/heads/main/screenshots/stack-moxie-2026-08-17T082056.png
security:
- kind: authentication
  name: Stack Moxie Authentication
  slug: stack-moxie-authentication
  summary_line: http/grpc-metadata/saml · 3 schemes
- kind: domain-security
  name: Stack Moxie Domain Security
  slug: stack-moxie-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Stack Moxie Vulnerability Disclosure
  slug: stack-moxie-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Stack Moxie Trust Center
  slug: stack-moxie-trust-center
  summary_line: SOC 2, ISO 27001
slug: stack-moxie
tags:
- Company
- Revenue Operations
- Marketing Operations
- Observability
- Monitoring
- Testing
- Test Automation
- QA Automation
- Marketing Automation
- Email Deliverability
- Salesforce
- Marketo
- gRPC
- Software-as-a-Service
website: https://stackmoxie.com/
---
