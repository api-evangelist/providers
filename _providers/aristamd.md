---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.3
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 21
  human_in_the_loop: 0
  name: Aristamd Agentic Access
  operation_count: 42
  slug: aristamd-agentic-access
  summary_line: 42 operations · 21 acting
api_count: 1
apis:
- description: 'The AristaMD API is the business logic core that serves all AristaMD sites, tools and integrations. It exposes eConsult lifecycle operations (create, retrieve, update, assign, search by status, event '
  name: AristaMD API
  slug: api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.aristamd.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.aristamd.com/request-demo/
- group: start
  title: ''
  type: Login
  url: https://app.aristamd.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aristamd.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aristamd.com/privacy-policy/
- group: auth
  title: ''
  type: Security
  url: https://www.aristamd.com/security/
- group: auth
  title: ''
  type: Compliance
  url: https://www.aristamd.com/security/
- group: auth
  title: ''
  type: TrustCenter
  url: security/aristamd-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/aristamd-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aristamd-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aristamd
- group: operate
  title: ''
  type: Support
  url: https://www.aristamd.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://www.aristamd.com/thought-leadership/
- group: auth
  title: ''
  type: Authentication
  url: authentication/aristamd-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/aristamd-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/aristamd-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/aristamd-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/aristamd-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/aristamd-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/aristamd-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aristamd-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/aristamd-agentic-access.yml
created: '2026-08-06'
description: AristaMD is a San Diego based specialty care company whose eConsult platform connects primary care providers to a panel of board-certified specialists across more than 70 specialties and subspecialties, delivering asynchronous, documented specialist recommendations that reduce unnecessary face-to-face referrals, emergency department visits and hospitalizations. The platform is sold to health plans, Medicaid programs, federally qualified health centers and provider groups, and is delivered through EHR-embedded referral workflows, HL7 messaging and a REST API. AristaMD publishes a live Swagger 2.0 definition for its core business-logic API at api.aristamd.com/api-docs covering eConsults, patients, panelists, specialties, reviews and workup checklists, and operates an OAuth 2.0 authorization server plus a SAML 2.0 service-provider endpoint for federated single sign-on.
image: https://www.aristamd.com/wp-content/uploads/AristaMD-SM.jpg
layout: provider
modified: '2026-08-06'
name: AristaMD
nav: Providers
network: true
overview: 'AristaMD publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Digital Health, Telehealth, and eConsult.


  AristaMD''s developer surface includes signup flow, support, engineering blog, authentication, and 19 more developer resources.'
random_paper: 62
score:
  band: thin
  composite: 37.4
  facets:
    commercial_clarity: 50.0
    contract_quality: 32.3
    developer_ergonomics: 23.9
    discoverability: 87.0
    governance: 20.8
    operational_transparency: 15.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 45.0
  schema_version: 0.9.1
  scored_at: '2026-08-06'
security:
- kind: authentication
  name: Aristamd Authentication
  slug: aristamd-authentication
  summary_line: oauth2/saml2 · 2 schemes
- kind: domain-security
  name: Aristamd Domain Security
  slug: aristamd-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aristamd Vulnerability Disclosure
  slug: aristamd-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Aristamd Trust Center
  slug: aristamd-trust-center
  summary_line: SOC 2
slug: aristamd
tags:
- Company
- Healthcare
- Digital Health
- Telehealth
- eConsult
- Specialty Care
- Referrals
- Care Coordination
- Health Plans
- Medicaid
- HL7
- Electronic Health Records
website: https://www.aristamd.com/
---
