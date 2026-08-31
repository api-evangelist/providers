---
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
    dynamic_client_registration: true
    error_semantics: false
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
  score: 15.1
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: The production OpenID Connect / OAuth 2.0 authorization server for the AssistPoint platform, served from Annexus Health's own custom domain. Its discovery document is published anonymously at /.well-k
  name: AssistPoint Identity (OpenID Connect)
  slug: assistpoint-identity
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.annexushealth.com/
- group: company
  title: ''
  type: About
  url: https://www.annexushealth.com/about/
- group: docs
  title: ''
  type: Documentation
  url: https://www.annexushealth.com/assistpoint/
- group: operate
  title: ''
  type: Support
  url: https://www.annexushealth.com/customer-support/
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.annexushealth.com/provider-faqs/
- group: company
  title: ''
  type: Blog
  url: https://www.annexushealth.com/insights/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.annexushealth.com/feed/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.annexushealth.com/privacy-policy/
- group: other
  title: ''
  type: CookiePolicy
  url: https://www.annexushealth.com/cookie-policy/
- group: start
  title: ''
  type: SignUp
  url: https://www.annexushealth.com/contact/
- group: start
  title: ''
  type: Login
  url: https://login.live.annexushealth.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.annexushealth.com/
- group: auth
  title: ''
  type: Compliance
  url: security/annexus-health-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/annexus-health-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/annexus-health-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/annexus-health-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/annexus-health-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/annexus-health-llms.txt
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/annexushealth
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/annexushealth/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCLKjak9CEP1Z9DjIjV2op9g
created: '2026-08-06'
description: 'Annexus Health is a privately held healthcare technology company headquartered in Cranberry Township, Pennsylvania that builds software to reduce the administrative burden of patient financial navigation across the patient access journey. Its flagship platform, AssistPoint, is an enterprise workflow application used by financial counselors and patient advocates at provider organizations to proactively identify, enroll in, and manage copay assistance, charitable foundation grants, and manufacturer patient support programs. A companion integration layer, AP Connect, creates a two-way secure information exchange between life science and foundation patient support programs and AssistPoint, digitally integrating enrollment, e-signature, and real-time award balance updates. Annexus Health also publishes Adparo, a patient financial navigation service offering. The company reports AssistPoint is licensed by 165+ healthcare organizations across 4,200+ sites of care and has processed
  more than $6 billion in patient financial assistance awards since 2018. Its integration and developer surface is partner-only: AP Connect is delivered through direct life science and foundation partnerships rather than a public developer program, and no public API reference or machine-readable specification is published. The publicly reachable machine-readable surface is the AssistPoint identity tier — an OpenID Connect authorization server on the company''s own custom domain — plus a SafeBase-hosted trust center carrying its HITRUST r2 certification.'
image: https://www.annexushealth.com/wp-content/uploads/2019/06/AnnexusHealth_logo_NAV-1.png
layout: provider
modified: '2026-08-06'
name: Annexus Health
nav: Providers
network: true
overview: 'Annexus Health publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Health Technology, Patient Access, and Financial Assistance.


  Annexus Health''s developer surface includes documentation, support, engineering blog, signup flow, YouTube channel, and 16 more developer resources.'
random_paper: 17
scopes:
- name: Annexus Health Scopes
  scope_count: 0
  slug: annexus-health-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 27.9
  coverage:
    artifact_dirs: 10
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 27.9
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 53.8
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/annexus-health/refs/heads/main/screenshots/annexus-health-2026-08-07T161419.png
security:
- kind: authentication
  name: Annexus Health Authentication
  slug: annexus-health-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Annexus Health Domain Security
  slug: annexus-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Annexus Health Trust Center
  slug: annexus-health-trust-center
  summary_line: HITRUST Risk-based, 2-year (r2) Certification
slug: annexus-health
tags:
- Company
- Healthcare
- Health Technology
- Patient Access
- Financial Assistance
- Oncology
- Revenue Cycle
- Copay Assistance
- Identity
- OpenID Connect
- HITRUST
website: https://www.annexushealth.com/
---
