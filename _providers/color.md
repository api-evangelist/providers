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
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 30.0
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: The Eligibility API from Color — 1 operation(s) for eligibility.
  name: Color Eligibility API
  slug: color-eligibility-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/color-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://security.color.com/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/color-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.color.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.color.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://docs.color.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.color.com/docs/getting-started-with-color-apis
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.color.com/changelog
- group: company
  title: ''
  type: Blog
  url: https://color.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/color
- group: start
  title: ''
  type: SignUp
  url: https://home.color.com/sign-in
- group: operate
  title: ''
  type: Support
  url: https://color.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://color.com/policies/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://color.com/policies/privacy
- group: company
  title: ''
  type: Website
  url: https://www.color.com
- group: auth
  title: ''
  type: Authentication
  url: authentication/color-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/color-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/color-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/color-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/color-sandbox.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/color-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/color-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Color Health is an oncologist-led virtual cancer care company that provides screening, early detection, diagnosis, treatment guidance, and survivorship support to employers, health plans, unions, consultants, and public-sector organizations. Originally founded as a genomics testing company (Color Genomics), Color now operates a virtual clinical platform combining at-home testing kits, preventive health programs, and AI-assisted cancer care. For integration partners Color publishes a developer documentation surface at docs.color.com covering an Eligibility List API, Self-Reported Results and Vaccination Status APIs, SAML-based SSO, and SFTP/PGP file transfer for eligibility, claims, and member-event data.
image: https://www.color.com/wp-content/uploads/2021/02/Wordmark_Color_RGB.png
layout: provider
modified: '2026-07-18'
name: Color
nav: Providers
network: true
overview: 'Color publishes 1 API on the [APIs.io](https://apis.io/) network: Eligibility API. Tagged areas include Company, Health, Healthcare, Genomics, and Oncology.


  Color''s developer surface includes documentation, API reference, getting-started guide, changelog, engineering blog, signup flow, support, and 16 more developer resources.'
random_paper: 68
score:
  band: developing
  composite: 47.5
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 63.6
    developer_ergonomics: 60.3
    discoverability: 87.0
    governance: 8.3
    operational_transparency: 21.1
  previous_composite: 47.5
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/color/refs/heads/main/screenshots/color-2026-07-25T210056.png
security:
- kind: authentication
  name: Color Authentication
  slug: color-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Color Domain Security
  slug: color-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Color Trust Center
  slug: color-trust-center
  summary_line: SOC 2, HIPAA, CSA STAR
slug: color
tags:
- Company
- Health
- Healthcare
- Genomics
- Oncology
- Cancer Care
- Preventive Health
- Eligibility
- Virtual Care
website: https://www.color.com
---
