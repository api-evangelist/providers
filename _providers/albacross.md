---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: verified
    event_surface_described: true
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 50.3
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Albacross Agentic Access
  operation_count: 1
  slug: albacross-agentic-access
  summary_line: 1 operation
api_count: 3
apis:
- description: Resolves an IPv4 address to a company profile — company name, country, registration number, description, founded year, postal address, LinkedIn URL, employee-count band, revenue band, NACE code and Li
  name: Albacross Reveal API
  slug: albacross-reveal-api
- description: 'Resolves a website domain to the same firmographic company record the Reveal API returns — name, country, registration number, description, founded year, address, LinkedIn URL, employee band, revenue '
  name: Albacross Enrich API
  slug: albacross-enrich-api
- description: The account-automation surface Albacross's own MIT-licensed n8n community node calls — GET /n8n/me to verify a key, GET /n8n/segments and GET /n8n/buyer_personas to list account objects, and POST/PATC
  name: Albacross n8n Automation API
  slug: albacross-n8n-api
artifact_total: 10
asyncapis:
- description: ''
  name: Albacross Webhooks
  slug: albacross-webhooks
collections:
- collection_type: open
  name: Reveal API docs
  slug: open-albacross-reveal
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/albacross-domain-security.yml
- group: agent
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
  title: ''
  type: LLMsTxt
  url: llms/albacross-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/albacross-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/albacross-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/albacross-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/albacross-rate-limits.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/albacross-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/albacross-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/albacross-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/albacross-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/albacross-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/albacross-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
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
image: https://albacross.com/albacross-logo.png
layout: provider
modified: '2026-08-12'
name: Albacross
nav: Providers
network: true
overview: 'Albacross publishes 1 API on the [APIs.io](https://apis.io/) network: Reveal API. Tagged areas include Company, B2B Data, Lead Generation, Intent Data, and Company Enrichment.


  The Albacross catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Albacross'' developer surface includes documentation, API reference, getting-started guide, authentication, support, pricing, signup flow, and 29 more developer resources.'
plans:
- name: Albacross Plans Pricing
  plan_count: 3
  slug: albacross-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Albacross Rate Limits
  slug: albacross-rate-limits
score:
  band: developing
  composite: 48.6
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 16.7
    contract_quality: 57.3
    developer_ergonomics: 37.5
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 10.5
  previous_composite: 48.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/albacross/refs/heads/main/screenshots/albacross-2026-08-17T080546.png
security:
- kind: authentication
  name: Albacross Authentication
  slug: albacross-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Albacross Domain Security
  slug: albacross-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
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
website: https://albacross.com/
---
