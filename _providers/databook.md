---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Databook Agentic Access
  operation_count: 8
  slug: databook-agentic-access
  summary_line: 8 operations · 3 acting
api_count: 1
apis:
- baseURL: https://api.databook.com
  baseurl_source: declared
  description: The batch - create API from Databook — 3 operation(s) for batch - create.
  name: Databook batch - create API
  slug: databook-batch-create-api
- baseURL: https://api.databook.com
  baseurl_source: declared
  description: The batch - query API from Databook — 3 operation(s) for batch - query.
  name: Databook batch - query API
  slug: databook-batch-query-api
- baseURL: https://api.databook.com
  baseurl_source: declared
  description: The chat API from Databook — 1 operation(s) for chat.
  name: Databook Chat API
  slug: databook-chat-api
- baseURL: https://api.databook.com
  baseurl_source: declared
  description: The reasoning API from Databook — 1 operation(s) for reasoning.
  name: Databook Reasoning API
  slug: databook-reasoning-api
- baseURL: https://api.databook.com
  baseurl_source: declared
  description: The asset_studio API from Databook — 6 operation(s) for asset_studio.
  name: Databook Asset Studio API
  slug: databook-asset-studio-api
artifact_total: 15
common:
- group: company
  title: ''
  type: Website
  url: https://databook.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.databook.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.databook.com/redoc
- group: docs
  title: ''
  type: APIReference
  url: https://api.databook.com/redoc
- group: start
  title: ''
  type: GettingStarted
  url: https://api.databook.com/redoc#section/Getting-started
- group: company
  title: ''
  type: Blog
  url: https://databook.com/resources
- group: operate
  title: ''
  type: Support
  url: https://databook.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://databook.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://databook.com/privacy
- group: start
  title: ''
  type: Login
  url: https://chat.databook.com
- group: auth
  title: ''
  type: Security
  url: https://databook.com/security
- group: auth
  title: ''
  type: Compliance
  url: https://databook.com/security
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.databook.com/
- group: auth
  href: https://artifacts.apis.io/databook/security/databook-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/databook-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/databook/security/databook-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/databook-domain-security.yml
- group: design
  href: https://artifacts.apis.io/databook/conformance/databook-conformance.yml
  title: ''
  type: Conformance
  url: conformance/databook-conformance.yml
- group: auth
  href: https://artifacts.apis.io/databook/authentication/databook-authentication.yml
  title: ''
  type: Authentication
  url: authentication/databook-authentication.yml
- group: design
  href: https://artifacts.apis.io/databook/conventions/databook-conventions.yml
  title: ''
  type: Conventions
  url: conventions/databook-conventions.yml
- group: design
  href: https://artifacts.apis.io/databook/errors/databook-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/databook-problem-types.yml
- group: design
  href: https://artifacts.apis.io/databook/data-model/databook-data-model.yml
  title: ''
  type: DataModel
  url: data-model/databook-data-model.yml
- group: operate
  href: https://artifacts.apis.io/databook/rate-limits/databook-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/databook-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/databook/plans/databook-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/databook-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/databook/lifecycle/databook-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/databook-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/databook/agentic-access/databook-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/databook-agentic-access.yml
- group: agent
  href: https://artifacts.apis.io/databook/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/databook/llms/databook-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/databook-llms.txt
- group: other
  href: https://artifacts.apis.io/databook/overlays/databook-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/databook-openapi-overlay.yaml
- group: company
  title: ''
  type: Blog
  url: https://trydatabook.com/blog/
created: '2026-07-17'
description: 'Databook is an AI-powered decision system for enterprise sales teams, combining verified market intelligence with structured reasoning to give sellers visibility into their largest deals. The platform pairs an "Outside-In Radar" of signals beyond the CRM with an advanced reasoning engine, a dynamic Customer Context Graph modeling every buying group, guided sales agents tuned to specific KPIs, a CRO dashboard for leadership, and a Value Coach for executive narratives. It serves enterprise revenue organizations across cloud, cybersecurity, managed services, and software. Databook is a portfolio company of Bessemer Venture Partners and Threshold Ventures. It publishes a machine-readable REST API — the DatabookAI REST API, OpenAPI 3.1.0 at https://api.databook.com/openapi.json — exposing a catalog of 66 account-research insights, asynchronous CSV batch jobs that run those insights across many target accounts, a threaded chat endpoint, and a deep-reasoning endpoint that returns
  cited, structured analysis. Access is not self-serve: bearer tokens are provisioned by Databook support.'
image: https://storage.googleapis.com/gpt-engineer-file-uploads/rfjG12z2plW0k4X3iSgJgycEVfj1/social-images/social-1779217719891-Databook_Preview_Home.webp
layout: provider
modified: '2026-08-13'
name: Databook
nav: Providers
network: true
overview: 'Databook publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including batch - create API, batch - query API, Chat API, and 2 more. Tagged areas include Company, Vertical Software, Sales Intelligence, Account Intelligence, and Sales Enablement.


  The Databook catalog on APIs.io includes 1 Spectral governance ruleset.


  Databook''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, and 22 more developer resources.'
plans:
- name: Databook Plans Pricing
  plan_count: 0
  slug: databook-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 0
  name: Databook Rate Limits
  slug: databook-rate-limits
rules:
- authorship: generated
  effective_rule_count: 97
  extends:
  - spectral:oas
  name: Databook API Rules
  rule_count: 56
  severity_counts:
    error: 51
    hint: 0
    info: 1
    warn: 4
  slug: databook-rules
score:
  band: developing
  composite: 48.0
  coverage:
    artifact_dirs: 23
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 10.4
  facets:
    access_clarity: 43.4
    contract_governance: 31.8
    contract_quality: 52.4
    developer_ergonomics: 58.9
    discoverability: 73.2
    operational_transparency: 10.5
  previous_composite: 37.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 55.6
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/databook/databook-2026-07-25T211258.png
security:
- kind: authentication
  name: Databook Authentication
  slug: databook-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Databook Domain Security
  slug: databook-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Databook Vulnerability Disclosure
  slug: databook-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Databook Trust Center
  slug: databook-trust-center
  summary_line: SOC 2 Type 2, NIST 800-171, GDPR, CCPA
skill_count: 2
skills:
- name: Research an account with Databook chat and deep reasoning
  slug: databook-account-research-chat
- name: Run a Databook batch insight job
  slug: databook-batch-insight-run
slug: databook
tags:
- Company
- Vertical Software
- Sales Intelligence
- Account Intelligence
- Sales Enablement
- Enterprise Sales
- Artificial Intelligence
- Revenue Operations
- REST API
- OpenAPI
- Batch Processing
- Agents
- Reasoning
- Company Data
- Data Platform
- Business Intelligence
website: https://databook.com/
---
