---
access_model:
  confidence: low
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.0
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 21
  human_in_the_loop: 0
  name: Aristamd Agentic Access
  operation_count: 42
  slug: aristamd-agentic-access
  summary_line: 42 operations · 21 acting
api_count: 1
apis:
- baseURL: https://api.aristamd.com
  baseurl_source: declared
  description: The Comments API from AristaMD — 1 operation(s) for comments.
  name: AristaMD Comments API
  slug: aristamd-comments-api
- baseURL: https://api.aristamd.com
  baseurl_source: declared
  description: The Diagnostic API from AristaMD — 1 operation(s) for diagnostic.
  name: AristaMD Diagnostic API
  slug: aristamd-diagnostic-api
- baseURL: https://api.aristamd.com
  baseurl_source: declared
  description: The EConsults API from AristaMD — 7 operation(s) for econsults.
  name: AristaMD E Consults API
  slug: aristamd-econsults-api
- baseURL: https://api.aristamd.com
  baseurl_source: declared
  description: The Intergy/Patients API from AristaMD — 1 operation(s) for intergy/patients.
  name: AristaMD Intergy/Patients API
  slug: aristamd-intergy-patients-api
- baseURL: https://api.aristamd.com
  baseurl_source: declared
  description: The Panelists API from AristaMD — 2 operation(s) for panelists.
  name: AristaMD Panelists API
  slug: aristamd-panelists-api
- baseURL: https://api.aristamd.com
  baseurl_source: declared
  description: The Patients API from AristaMD — 7 operation(s) for patients.
  name: AristaMD Patients API
  slug: aristamd-patients-api
- baseURL: https://api.aristamd.com
  baseurl_source: declared
  description: The Requests API from AristaMD — 1 operation(s) for requests.
  name: AristaMD Requests API
  slug: aristamd-requests-api
- baseURL: https://api.aristamd.com
  baseurl_source: declared
  description: The Reviews API from AristaMD — 2 operation(s) for reviews.
  name: AristaMD Reviews API
  slug: aristamd-reviews-api
- baseURL: https://api.aristamd.com
  baseurl_source: declared
  description: The Specialties API from AristaMD — 3 operation(s) for specialties.
  name: AristaMD Specialties API
  slug: aristamd-specialties-api
- baseURL: https://api.aristamd.com
  baseurl_source: declared
  description: The Specialty API from AristaMD — 1 operation(s) for specialty.
  name: AristaMD Specialty API
  slug: aristamd-specialty-api
- baseURL: https://api.aristamd.com
  baseurl_source: declared
  description: The Users API from AristaMD — 4 operation(s) for users.
  name: AristaMD Users API
  slug: aristamd-users-api
- baseURL: https://api.aristamd.com
  baseurl_source: declared
  description: The Workup Checklists API from AristaMD — 3 operation(s) for workup checklists.
  name: AristaMD Workup Checklists API
  slug: aristamd-workup-checklists-api
artifact_total: 31
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Arista MD Comments API
  slug: open-aristamd-comments-api
- collection_type: open
  name: Arista MD Diagnostic API
  slug: open-aristamd-diagnostic-api
- collection_type: open
  name: Arista MD E Consults API
  slug: open-aristamd-econsults-api
- collection_type: open
  name: Arista MD Intergy/Patients API
  slug: open-aristamd-intergy-patients-api
- collection_type: open
  name: Arista MD API
  slug: open-aristamd-openapi-original
- collection_type: open
  name: Arista MD Panelists API
  slug: open-aristamd-panelists-api
- collection_type: open
  name: Arista MD Patients API
  slug: open-aristamd-patients-api
- collection_type: open
  name: Arista MD Requests API
  slug: open-aristamd-requests-api
- collection_type: open
  name: Arista MD Specialties API
  slug: open-aristamd-specialties-api
- collection_type: open
  name: Arista MD Specialty API
  slug: open-aristamd-specialty-api
- collection_type: open
  name: Arista MD Users API
  slug: open-aristamd-users-api
- collection_type: open
  name: Arista MD Workup Checklists API
  slug: open-aristamd-workup-checklists-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/aristamd-capability-edges.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/aristamd-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/aristamd-api-overlay.yaml
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
mcp_servers:
- description: A CANDIDATE tool surface derived by API Evangelist from AristaMD's published Swagger 2.0 document. This is NOT an AristaMD product and no such server is running. It exists to show what an MCP server o
  name: AristaMD MCP Server
  slug: aristamd-mcp-server
modified: '2026-08-06'
name: AristaMD
nav: Providers
network: true
overview: 'AristaMD publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Comments API, Diagnostic API, E Consults API, and 9 more. Tagged areas include Company, Healthcare, Digital Health, Telehealth, and eConsult.


  AristaMD''s developer surface includes signup flow, support, engineering blog, authentication, and 22 more developer resources.'
random_paper: 13
score:
  band: developing
  composite: 39.7
  coverage:
    artifact_dirs: 19
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 4.5
    contract_quality: 46.9
    developer_ergonomics: 20.8
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 13.2
  previous_composite: 39.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 45.0
  schema_version: 0.18.0
  scored_at: '2026-09-02'
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
