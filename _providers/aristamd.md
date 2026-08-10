---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
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
  score: 32.2
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 21
  human_in_the_loop: 0
  name: Aristamd Agentic Access
  operation_count: 42
  slug: aristamd-agentic-access
  summary_line: 42 operations · 21 acting
api_count: 12
apis:
- description: The Comments API from AristaMD — 1 operation(s) for comments.
  name: AristaMD Comments API
  slug: aristamd-comments-api
- description: The Diagnostic API from AristaMD — 1 operation(s) for diagnostic.
  name: AristaMD Diagnostic API
  slug: aristamd-diagnostic-api
- description: The EConsults API from AristaMD — 7 operation(s) for econsults.
  name: AristaMD E Consults API
  slug: aristamd-econsults-api
- description: The Intergy/Patients API from AristaMD — 1 operation(s) for intergy/patients.
  name: AristaMD Intergy/Patients API
  slug: aristamd-intergy-patients-api
- description: The Panelists API from AristaMD — 2 operation(s) for panelists.
  name: AristaMD Panelists API
  slug: aristamd-panelists-api
- description: The Patients API from AristaMD — 7 operation(s) for patients.
  name: AristaMD Patients API
  slug: aristamd-patients-api
- description: The Requests API from AristaMD — 1 operation(s) for requests.
  name: AristaMD Requests API
  slug: aristamd-requests-api
- description: The Reviews API from AristaMD — 2 operation(s) for reviews.
  name: AristaMD Reviews API
  slug: aristamd-reviews-api
- description: The Specialties API from AristaMD — 3 operation(s) for specialties.
  name: AristaMD Specialties API
  slug: aristamd-specialties-api
- description: The Specialty API from AristaMD — 1 operation(s) for specialty.
  name: AristaMD Specialty API
  slug: aristamd-specialty-api
- description: The Users API from AristaMD — 4 operation(s) for users.
  name: AristaMD Users API
  slug: aristamd-users-api
- description: The Workup Checklists API from AristaMD — 3 operation(s) for workup checklists.
  name: AristaMD Workup Checklists API
  slug: aristamd-workup-checklists-api
artifact_total: 17
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
overview: 'AristaMD publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Comments API, Diagnostic API, E Consults API, and 9 more. Tagged areas include Company, Healthcare, Digital Health, Telehealth, and eConsult.


  AristaMD''s developer surface includes signup flow, support, engineering blog, authentication, and 19 more developer resources.'
random_paper: 41
score:
  band: thin
  composite: 38.9
  delta: 3.2
  facets:
    commercial_clarity: 50.0
    contract_quality: 45.2
    developer_ergonomics: 19.0
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 15.8
  previous_composite: 35.7
  provenance:
    agentic_access: derived
    conformance: derived
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
    regime: Health
    regime_id: health
    score: 45.0
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aristamd/refs/heads/main/screenshots/aristamd-2026-08-07T161715.png
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
