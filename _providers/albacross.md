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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.8
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Albacross Agentic Access
  operation_count: 1
  slug: albacross-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: 'Resolves a website domain to the same firmographic company record the Reveal API returns — name, country, registration number, description, founded year, address, LinkedIn URL, employee band, revenue '
  name: Albacross Enrich API
  slug: albacross-enrich-api
- description: The account-automation surface Albacross's own MIT-licensed n8n community node calls — GET /n8n/me to verify a key, GET /n8n/segments and GET /n8n/buyer_personas to list account objects, and POST/PATC
  name: Albacross n8n Automation API
  slug: albacross-n8n-api
- baseURL: https://api.albacross.com/reveal
  baseurl_source: declared
  description: The Company API from Albacross — 1 operation(s) for company.
  name: Albacross Company API
  slug: albacross-company-api
artifact_total: 15
asyncapis:
- description: ''
  name: Albacross Webhooks
  slug: albacross-webhooks
collections:
- collection_type: open
  name: Reveal API docs
  slug: open-albacross-reveal
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/albacross/n8n-nodes-albacross/blob/main/LICENSE
- group: other
  href: https://artifacts.apis.io/albacross/overlays/albacross-reveal-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/albacross-reveal-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/albacross/security/albacross-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/albacross-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/albacross/agentic-access/albacross-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/albacross-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://albacross.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.albacross.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.albacross.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.albacross.com/reveal
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.albacross.com/authentication
- group: auth
  href: https://artifacts.apis.io/albacross/authentication/albacross-authentication.yml
  title: ''
  type: Authentication
  url: authentication/albacross-authentication.yml
- group: operate
  title: ''
  type: Support
  url: https://help.albacross.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.albacross.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/albacross
- group: commercial
  title: ''
  type: Pricing
  url: https://www.albacross.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.albacross.com/register
- group: start
  title: ''
  type: Login
  url: https://app.albacross.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.albacross.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.albacross.com/privacy-policy
- group: other
  title: ''
  type: CookiePolicy
  url: https://www.albacross.com/cookie-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.albacross.com/newsroom
- group: build
  title: ''
  type: Postman
  url: https://reveal.api.albacross.com/public/postman_collection.json
- group: agent
  href: https://artifacts.apis.io/albacross/llms/albacross-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/albacross-llms.txt
- group: build
  href: https://artifacts.apis.io/albacross/packages/albacross-packages.yml
  title: ''
  type: Packages
  url: packages/albacross-packages.yml
- group: build
  href: https://artifacts.apis.io/albacross/packages/albacross-packages.yml
  title: ''
  type: SDKs
  url: packages/albacross-packages.yml
- group: commercial
  href: https://artifacts.apis.io/albacross/plans/albacross-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/albacross-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/albacross/rate-limits/albacross-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/albacross-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/albacross/conventions/albacross-conventions.yml
  title: ''
  type: Conventions
  url: conventions/albacross-conventions.yml
- group: design
  href: https://artifacts.apis.io/albacross/errors/albacross-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/albacross-problem-types.yml
- group: design
  href: https://artifacts.apis.io/albacross/lifecycle/albacross-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/albacross-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/albacross/data-model/albacross-data-model.yml
  title: ''
  type: DataModel
  url: data-model/albacross-data-model.yml
- group: design
  href: https://artifacts.apis.io/albacross/conformance/albacross-conformance.yml
  title: ''
  type: Conformance
  url: conformance/albacross-conformance.yml
- group: design
  href: https://artifacts.apis.io/albacross/asyncapi/albacross-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/albacross-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/albacross/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/albacross/components/albacross-components.yml
  title: ''
  type: Components
  url: components/albacross-components.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/albacross
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/albacrossnordic
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/albacross
- group: company
  title: ''
  type: Careers
  url: https://career.albacross.com/
created: '2026-08-12'
description: Albacross is a Stockholm-founded B2B intent data and lead generation platform that identifies anonymous website visitors by IP, enriches them with firmographic data, segments them by buying intent using AI, and auto-engages high-intent prospects through email and LinkedIn sequences. For developers it exposes a small, key-authenticated HTTP surface on api.albacross.com — a Reveal API that resolves an IPv4 address to a company profile, an Enrich API that resolves a website domain to the same firmographic record (name, country, registration number, address, LinkedIn URL, employee band, revenue band, NACE and LinkedIn industry codes), and an n8n automation API for registering lead webhooks. Outbound webhooks push identified-company leads into workflows in real time. The company publishes an OpenAPI 3.0.3 document for the Reveal API and an llms.txt at its website root.
finops:
- has_sources: true
  method: derived
  name: Albacross Finops
  primary_unit: subscription
  service_category: ''
  slug: albacross-finops
  template: false
image: https://albacross.com/albacross-logo.png
layout: provider
modified: '2026-08-12'
name: Albacross
nav: Providers
network: true
overview: 'Albacross publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network, including Company API, and 2 more. Tagged areas include Company, B2B Data, Lead Generation, Intent Data, and Company Enrichment.


  The Albacross catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Albacross'' developer surface includes documentation, API reference, getting-started guide, authentication, support, pricing, signup flow, and 31 more developer resources.'
plans:
- name: Albacross Plans Pricing
  plan_count: 5
  slug: albacross-plans-pricing
- name: Albacross Price Estimates
  plan_count: 0
  slug: albacross-price-estimates
random_paper: 18
rate_limits:
- limit_count: 0
  name: Albacross Rate Limits
  slug: albacross-rate-limits
score:
  band: developing
  composite: 51.9
  coverage:
    artifact_dirs: 24
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.0
  facets:
    access_clarity: 84.2
    contract_governance: 4.5
    contract_quality: 43.7
    developer_ergonomics: 68.5
    discoverability: 67.9
    operational_transparency: 13.2
  previous_composite: 50.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 25.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/albacross/albacross-2026-08-17T080546.png
security:
- kind: authentication
  name: Albacross Authentication
  slug: albacross-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Albacross Domain Security
  slug: albacross-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: Enrich a company from a website domain
  slug: albacross-enrich-domain-to-company
- name: Register a lead webhook and receive identified companies
  slug: albacross-register-lead-webhook
- name: Reveal a company from an IPv4 address
  slug: albacross-reveal-ip-to-company
slug: albacross
tags:
- Company
- B2B Data
- Lead Generation
- Intent Data
- Company Enrichment
- IP Intelligence
- Firmographics
- Marketing
- Sales Intelligence
- Account Based Marketing
- Website Visitor Identification
- Webhook
- Data Enrichment
website: https://albacross.com/
---
