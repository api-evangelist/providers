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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 13.7
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: The CentralReach Enhanced API lets partner organizations connect securely to the CentralReach platform and integrate with third-party applications. Authentication is OAuth 2.0 client-credentials again
  name: CentralReach Enhanced API
  slug: centralreach-enhanced-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/centralreach-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://centralreach.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://centralreach.com/resources/api/
- group: docs
  title: ''
  type: Documentation
  url: https://centralreach.com/resources/api/requests/
- group: start
  title: ''
  type: GettingStarted
  url: https://centralreach.com/resources/api/
- group: operate
  title: ''
  type: Support
  url: https://community.centralreach.com/
- group: company
  title: ''
  type: Blog
  url: https://centralreach.com/cr-blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CentralReach
- group: start
  title: ''
  type: SignUp
  url: https://centralreach.com/book-demo/
- group: start
  title: ''
  type: Login
  url: https://login.centralreach.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://centralreach.com/legal/terms-policies/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://centralreach.com/legal/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.centralreach.com/
- group: auth
  title: ''
  type: Compliance
  url: https://centralreach.com/about/security/
- group: auth
  title: ''
  type: Authentication
  url: authentication/centralreach-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/centralreach-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/centralreach-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/centralreach-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/centralreach-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/centralreach-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/centralreach-trust-center.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/centralreach-well-known.yml
created: '2026-07-17'
description: CentralReach is a healthcare software and services platform for organizations that serve children and adults diagnosed with autism and related intellectual and developmental disabilities (IDD). Its integrated practice-management and electronic-medical-record (EMR) system covers clinical data collection, scheduling, note drafting and auditing, claims management and billing, staff training and certification, and caregiver engagement across ABA therapy, multidisciplinary therapy, and special-education providers. CentralReach publishes a gated Enhanced API (OAuth 2.0 client-credentials, JWT) at partners-api.centralreach.com for securely connecting the platform to critical third-party applications, with access provisioned through a dedicated CentralReach representative. Surfaced as a portfolio company of Insight Partners and enriched by the API Evangelist pipeline.
image: https://centralreach.com/wp-content/uploads/2022/05/logo-centralreach-navy-teal-yoast.jpg
layout: provider
modified: '2026-07-18'
name: CentralReach
nav: Providers
network: true
overview: 'CentralReach publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, ABA Therapy, Autism, and IDD.


  CentralReach''s developer surface includes documentation, getting-started guide, support, engineering blog, signup flow, authentication, and 16 more developer resources.'
random_paper: 0
scopes:
- name: Centralreach Scopes
  scope_count: 4
  slug: centralreach-scopes
  summary_line: 4 scopes · clientCredentials
score:
  band: thin
  composite: 39.1
  coverage:
    artifact_dirs: 11
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 54.8
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 39.1
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: CA
      standard: pipeda
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ferpa
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 3
    matched_via: tags
    regime: Health
    regime_id: health
    score: 58.8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/centralreach/refs/heads/main/screenshots/centralreach-2026-07-25T204931.png
security:
- kind: authentication
  name: Centralreach Authentication
  slug: centralreach-authentication
  summary_line: oauth2/apiKey · 2 schemes
- kind: domain-security
  name: Centralreach Domain Security
  slug: centralreach-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Centralreach Trust Center
  slug: centralreach-trust-center
  summary_line: SOC 2, HIPAA, PCI DSS, FERPA, GDPR, UK GDPR, EU-U.S. Data Privacy Framework, Swiss-U.S. Data Privacy Framework, UK Data Privacy Framework, PIPEDA
slug: centralreach
tags:
- Company
- Healthcare
- ABA Therapy
- Autism
- IDD
- EMR
- Practice Management
- Behavioral Health
- Special Education
- Billing
- Authentication
website: https://centralreach.com/
---
