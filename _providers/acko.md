---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 44.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Acko Agentic Access
  operation_count: 3
  slug: acko-agentic-access
  summary_line: 3 operations · 3 acting
api_count: 1
apis:
- description: The APIs API from Acko — 3 operation(s) for apis.
  name: Acko APIs API
  slug: acko-apis-api
artifact_total: 5
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/acko-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/acko-authentication.yml
- group: auth
  title: ''
  type: API Keys
  url: authentication/acko-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/acko-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/acko-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/acko-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/acko-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/acko-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/acko-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/acko-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/acko-well-known.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/acko-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.acko.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.acko.com/enterprise/documentation/enterprise.html
- group: docs
  title: ''
  type: APIReference
  url: https://www.acko.com/enterprise/documentation/enterprise.html
- group: company
  title: ''
  type: Blog
  url: https://www.acko.com/articles/
- group: operate
  title: ''
  type: Support
  url: https://www.acko.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.acko.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.acko.com/privacy-policy/
- group: company
  title: ''
  type: About
  url: https://www.acko.com/about-us/
created: '2026-07-17'
description: Acko (ACKO Technology & Services Private Limited) is an Indian digital-first general insurance company founded in 2016 and headquartered in Bengaluru, Karnataka. Acko sells car, bike, health, term life and travel insurance entirely online, along with group health and personal-accident cover and embedded insurance for partners. It is a portfolio company of Accel. Acko exposes insurance policy certificates to citizens through India's government API Setu / DigiLocker platform (car, health and two-wheeler certificate fetch), and operates a separate enterprise/partner issuance API covering token generation, Loan-Shield, Trip, GIG, Health, House, Credit Life, Fire, Cyber and Electronics products plus policy and claims management.
image: https://www.acko.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: acko-mcp.yml
  slug: acko-mcpyml
modified: '2026-07-18'
name: Acko
nav: Providers
network: true
overview: 'Acko publishes 1 API on the [APIs.io](https://apis.io/) network: APIs API. Tagged areas include Company, Consumer, Insurance, InsurTech, and Financial Services.


  Acko''s developer surface includes authentication, documentation, API reference, engineering blog, support, and 16 more developer resources.'
random_paper: 19
score:
  band: thin
  composite: 38.4
  delta: -1.7
  facets:
    commercial_clarity: 21.1
    contract_quality: 60.2
    developer_ergonomics: 36.4
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 40.1
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
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 48.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/acko/refs/heads/main/screenshots/acko-2026-07-25T181503.png
security:
- kind: authentication
  name: Acko Authentication
  slug: acko-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Acko Domain Security
  slug: acko-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: acko
tags:
- Company
- Consumer
- Insurance
- InsurTech
- Financial Services
- Digital Insurance
- India
- Embedded Insurance
website: http://www.acko.com
---
