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
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.1
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Cooperators Agentic Access
  operation_count: 10
  slug: cooperators-agentic-access
  summary_line: 10 operations · 9 acting
api_count: 1
apis:
- description: Partner-gated embedded insurance API from Duuo, the digital insurance brand of The Co-operators. Duuo's own published documentation describes APIs for account, quote and policy, risk rating and paymen
  name: Duuo Platform API
  slug: duuo-platform-api
arazzos:
- description: ''
  name: _Index
  slug: _index
- description: 'The full Duuo event insurance partner flow in Duuo''s mandatory order: create the entity, price the event, retrieve the quote for display, then generate the Duuo-hosted payment redirect. With bindOnPay'
  name: Duuo event insurance — quote and bind
  slug: cooperators-event-insurance-quote-and-bind
- description: 'The full Duuo tenant (renters) insurance partner flow in Duuo''s mandatory order: check eligibility with consent, add the risk detail and price it into four options, record the selection and any additi'
  name: Duuo tenant insurance — quote and bind
  slug: cooperators-tenant-insurance-quote-and-bind
artifact_total: 8
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cooperators-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cooperators-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cooperators-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cooperators.ca/
- group: company
  title: ''
  type: About
  url: https://www.cooperators.ca/en/about-us/corporate-overview
- group: other
  title: ''
  type: SignIn
  url: https://www.cooperators.ca/en/advisors/sign-in
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.cooperators.ca/en/about-us/corporate-overview/investor-relations
- group: auth
  title: ''
  type: SecurityAndPrivacy
  url: https://www.cooperators.ca/en/security-privacy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/co-operators
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cooperators.ca/en/security-privacy/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cooperators.ca/en/security-privacy/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.cooperators.ca/en/contact-us
- group: company
  title: ''
  type: News
  url: https://www.cooperators.ca/en/about-us/newsroom
- group: company
  title: ''
  type: Blog
  url: https://duuo.ca/blog/
- group: company
  title: ''
  type: Careers
  url: https://www.cooperators.ca/en/about-us/careers
- group: other
  title: ''
  type: Sustainability
  url: https://www.cooperators.ca/en/about-us/sustainability
- group: build
  title: ''
  type: CodeOfConduct
  url: https://www.cooperators.ca/en/about-us/code-of-ethics-business-conduct
- group: other
  title: ''
  type: Accessibility
  url: https://www.cooperators.ca/en/client-resources/accessibility-plan-details
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cooperators-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/cooperators-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cooperators-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cooperators-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cooperators-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cooperators-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/cooperators-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-25'
description: The Co-operators is a Canadian insurance and financial services co-operative, formed in 1978 from the amalgamation of the Saskatchewan and Ontario co-operative insurers whose roots run back to the Co-operative Life Insurance Company founded in Regina in 1945. It is owned by Canadian co-operatives, credit union centrals and farm organizations rather than public shareholders, and writes multi-line property and casualty, home, auto, farm, travel and life insurance alongside group benefits, group retirement and savings, wealth management and institutional asset management, reporting more than $62 billion in assets under administration, nearly 7,000 employees and more than 2,800 licensed insurance representatives across Canada. Its API posture is partner-gated. There is no first-party developer portal on cooperators.ca — developer, developers, docs, api and partners subdomains do not resolve in DNS, and /developers, /developer, /api, /partners and /integrations all return HTTP 404
  — while the advisor and broker channel is a set of sign-in walls (lifeportal.cooperators.ca, benefitsnowlogon.cooperators.ca, basis.cooperators.ca, illustration.cumis.com). The only public API surface in the group belongs to its embedded-insurance brand Duuo, whose Duuo Platform partner APIs cover account, quote, payment and policy issuance for tenant and event insurance behind a signed partnership agreement and issued OAuth 2.0 client credentials; the developer portal Duuo advertises at developer.duuo.ca is a Postman-hosted documentation domain that returns HTTP 404 as of 2026-07-25. No ACORD, AL3 or CSIO reference was found anywhere in the company's public materials.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: Duuo Platform MCP tool surface (CANDIDATE — derived from the OpenAPI, NOT published or hosted by the provider)
  slug: duuo-platform-mcp-tool-surface-candidate-derived-from-the-openapi-not-published-or-hosted-by-the-provider
modified: '2026-07-25'
name: The Co-operators
nav: Providers
network: true
overview: 'The Co-operators publishes 1 API on the [APIs.io](https://apis.io/) network: Duuo Platform API. Tagged areas include Insurance, Canada, Property and Casualty, Life Insurance, and Group Benefits.


  The Co-operators'' developer surface includes authentication, support, product news, engineering blog, sandbox, and 21 more developer resources.'
random_paper: 71
score:
  band: emerging
  composite: 26.2
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 15.3
    developer_ergonomics: 25.5
    discoverability: 77.8
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 26.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 48.5
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cooperators/refs/heads/main/screenshots/cooperators-2026-07-25T210405.png
security:
- kind: authentication
  name: Cooperators Authentication
  slug: cooperators-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Cooperators Domain Security
  slug: cooperators-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cooperators
tags:
- Insurance
- Canada
- Property and Casualty
- Life Insurance
- Group Benefits
- Embedded Insurance
- Co-operative
- Wealth Management
- Partner API
website: https://www.cooperators.ca/
---
