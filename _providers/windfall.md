---
access_model:
  confidence: high
  label: Contact sales — tokens issued by Windfall
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://api-docs.windfall.com/authentication/
  - https://www.windfall.com/blog/powering-real-time-ai-native-workflows-opening-the-windfall-api-to-all-customers-and-partners
  - plans/windfall-plans-pricing.yml
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.5
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Windfall Agentic Access
  operation_count: 1
  slug: windfall-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- baseURL: https://api.windfalldata.com/v1
  baseurl_source: declared
  description: The Windfall API API from Windfall — 1 operation(s) for windfall api.
  name: Windfall Windfall API API
  slug: windfall-windfall-api-api
artifact_total: 9
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Windfall Windfall API API
  slug: open-windfall-windfall-api-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/windfall-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.windfall.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api-docs.windfall.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.windfall.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.windfall.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://api-docs.windfall.com/quickstart/
- group: company
  title: ''
  type: Blog
  url: https://www.windfall.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.windfall.com/contact
- group: start
  title: ''
  type: Login
  url: https://login.windfalldata.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.windfall.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.windfall.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/windfalldata
- group: auth
  title: ''
  type: Compliance
  url: https://www.windfall.com/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/windfall-trust-center.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/windfall-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/windfall-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/windfall-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/windfall-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/windfall-rate-limits.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/windfall-sandbox.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/windfall-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/windfall-enrich-person-record.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/windfall-sandbox-integration-test.md
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/windfall-llms.txt
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/windfall-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/windfall-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/windfall-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/windfall-plans-pricing.yml
- group: build
  title: ''
  type: CodeExamples
  url: https://api-docs.windfall.com/examples/
- group: company
  title: ''
  type: News
  url: https://www.windfall.com/company/news
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/windfall-data/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/windfalldata
created: '2026-07-17'
description: Windfall is an AI-powered people intelligence platform that helps go-to-market teams personalize workflows with wealth and career data, serving 1,500+ organizations across finance, retail, education, healthcare, and nonprofits. The Windfall API delivers enriched household and career data for a single person record in real time — submit basic PII and receive JSON in one HTTPS request. One operation (enrichRecord) returns up to 32 documented household fields (net worth and its confidence bounds, property, life events, philanthropy, political giving, financial signals) and 26 career fields (job title and level, job-change signals, employer firmographics, LinkedIn URL), with availability set by the customer's plan. US coverage only; the database is rebuilt weekly; rate limited to 5 requests/second; and a non-billed sandbox with 15 deterministic fictitious personas and a header-driven error simulator mirrors production for integration testing. Access is contractual — tokens are issued
  by Windfall and API credits were bundled into existing subscriptions when the API opened to all customers and partners in May 2026.
image: https://api-docs.windfall.com/static/favicon.png
layout: provider
modified: '2026-08-14'
name: Windfall
nav: Providers
network: true
overview: 'Windfall publishes 1 API on the [APIs.io](https://apis.io/) network: Windfall API API. Tagged areas include Company, Fintech, Data Enrichment, Wealth Data, and People Intelligence.


  Windfall''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, sandbox, and 25 more developer resources.'
plans:
- name: Windfall Plans Pricing
  plan_count: 0
  slug: windfall-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 1
  name: Windfall Rate Limits
  slug: windfall-rate-limits
score:
  band: developing
  composite: 49.7
  coverage:
    artifact_dirs: 23
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 59.9
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 23.7
  previous_composite: 49.7
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
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/windfall/refs/heads/main/screenshots/windfall-2026-08-17T082920.png
security:
- kind: authentication
  name: Windfall Authentication
  slug: windfall-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Windfall Domain Security
  slug: windfall-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Windfall Trust Center
  slug: windfall-trust-center
  summary_line: SOC 2 Type 2, CCPA / California registered data broker
slug: windfall
tags:
- Company
- Fintech
- Data Enrichment
- Wealth Data
- People Intelligence
- Career Data
- Identity Resolution
- Sales Intelligence
- Marketing
website: https://www.windfall.com
---
