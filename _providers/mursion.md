---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mursion-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.mursion.com/
- group: docs
  title: ''
  type: Documentation
  url: https://support.mursion.com/knowledge
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.mursion.com/knowledge
- group: operate
  title: ''
  type: Support
  url: https://support.mursion.com/knowledge/kb-tickets/new
- group: company
  title: ''
  type: Blog
  url: https://www.mursion.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MursionInc
- group: start
  title: ''
  type: Login
  url: https://www.mursion.com/log-in/
- group: start
  title: ''
  type: SignUp
  url: https://www.mursion.com/request-demo/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mursion.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mursion.com/privacynotice/
- group: operate
  title: ''
  type: FAQ
  url: https://www.mursion.com/faq/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.mursion.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://support.mursion.com/knowledge/mursion-release-notes
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://forgeglobal.com/mursion_stock/
- group: auth
  title: ''
  type: Authentication
  url: authentication/mursion-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mursion-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mursion-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/mursion-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mursion-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/mursion-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mursion-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/mursion-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mursion-llms.txt
- group: auth
  title: ''
  type: TrustCenter
  url: security/mursion-trust-center.yml
coverage:
  checked: '2026-08-26'
  detail: 'Mursion ships only an end-user product — the browser-based Mursion Portal — and runs no developer program of any kind: no developer subdomain resolves, no API reference or spec is served on any Mursion host, and the AWS API Gateway behind the portal (apiaws.mursion.com) answers 403 "Missing Authentication Token" on every path including /openapi.json; the only integration Mursion documents publicly is SAML 2.0 / OpenID Connect single sign-on for customer IT teams.'
  evidence:
  - status: 403
    url: https://apiaws.mursion.com/openapi.json
  - status: 404
    url: https://www.mursion.com/openapi.json
  - status: 404
    url: https://www.mursion.com/llms.txt
  - status: 404
    url: https://www.mursion.com/.well-known/agent-card.json
  - status: 200
    url: https://support.mursion.com/knowledge/configuring-saml-2.0
  reason: no-developer-program
  state: none
created: '2026-08-26'
description: Mursion is an AI-powered immersive upskilling platform that trains workforce soft skills — leadership, customer service, sales, healthcare communication and difficult conversations — through simulated conversations with virtual avatars. Simulations run either human-powered (Mursion Live, where a certified Simulation Specialist puppets the avatar in real time) or AI-powered (Mursion On-Demand), and are delivered and administered through the Mursion Portal, a browser-based web application for scheduling, cohorts, pathways, session reports and learner analytics. Mursion publishes no public developer program, API reference or machine-readable contract; its documented integration surface is enterprise identity — SAML 2.0 and OpenID Connect single sign-on with just-in-time provisioning and team assignment via an IdP claim — documented in the customer-facing knowledge base for IT teams.
image: https://www.mursion.com/wp-content/uploads/2022/10/Mursion-Logo.svg
layout: provider
modified: '2026-08-26'
name: Mursion
nav: Providers
network: true
overview: 'Mursion is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Learning and Development, Corporate Training, Simulation, and Immersive Learning.


  Mursion''s developer surface includes documentation, support, engineering blog, signup flow, FAQ, changelog, authentication, and 18 more developer resources.'
plans:
- name: Mursion Plans Pricing
  plan_count: 0
  slug: mursion-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Mursion Rate Limits
  slug: mursion-rate-limits
score:
  band: emerging
  composite: 24.9
  coverage:
    artifact_dirs: 13
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 24.9
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 46.3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Mursion Authentication
  slug: mursion-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Mursion Domain Security
  slug: mursion-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Mursion Trust Center
  slug: mursion-trust-center
  summary_line: trust center published
slug: mursion
tags:
- Company
- Learning and Development
- Corporate Training
- Simulation
- Immersive Learning
- Artificial Intelligence
- Virtual Reality
- Education
- Human Resources
- Enterprise Software
website: https://www.mursion.com/
---
