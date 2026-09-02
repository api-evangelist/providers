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
    auth_clarity: bearer
    consent_identity: true
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 7.6
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Lingco Classroom is registered in an LMS as an IMS/1EdTech LTI 1.3 tool. The platform performs an OIDC third-party-initiated login against Lingco's initiation endpoint, launches into the target link U
  name: Lingco Classroom LTI 1.3 Tool
  slug: lingco-language-labs-lti-1-3-tool
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://lingco.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.lingco.io/en/collections/2522345-for-it-administrators
- group: docs
  title: ''
  type: Documentation
  url: https://help.lingco.io/en/collections/2522345-for-it-administrators
- group: operate
  title: ''
  type: Support
  url: https://help.lingco.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lingco.io/terms_of_service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lingco.io/privacy_policy
- group: other
  title: ''
  type: AcceptableUsePolicy
  url: https://lingco.io/acceptable_use_policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.lingco.io/
- group: auth
  title: ''
  type: Compliance
  url: https://lingco.io/terms_of_service
- group: auth
  title: ''
  type: Authentication
  url: authentication/lingco-language-labs-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lingco-language-labs-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lingco-language-labs-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/lingco-language-labs-conventions.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/lingco-language-labs-well-known.yml
- group: other
  title: ''
  type: ContentSignal
  url: well-known/lingco-language-labs-robots.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lingco-language-labs-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lingco-language-labs-llms.txt
created: '2026-07-17'
description: 'Lingco Language Labs, Inc. is a Delaware-incorporated education technology company operating Lingco Classroom, a cloud language-learning platform used by schools and universities. Lingco pairs a library of pre-built, customizable world-language content with an instructor platform for building courses, assigning activities and tracking learner outcomes. Lingco publishes no general-purpose public developer API; its integration surface is standards-based education interoperability: an IMS/1EdTech LTI 1.3 tool (OIDC third-party-initiated login, JWKS, Assignment and Grade Services and Names and Role Provisioning Services) hosted at class.lingco.io, OneRoster v1.1 rostering via REST or SFTP CSV, a Canvas API client integration, and SSO with Google Classroom, Schoology and Clever.'
image: https://www.lingco.io/og-image.png
layout: provider
modified: '2026-07-19'
name: Lingco Language Labs
nav: Providers
network: true
overview: 'Lingco Language Labs publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, EdTech, Language Learning, and Learning Management.


  Lingco Language Labs'' developer surface includes documentation, support, authentication, and 14 more developer resources.'
random_paper: 6
score:
  band: thin
  composite: 26.9
  coverage:
    artifact_dirs: 9
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 26.9
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 55.6
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lingco-language-labs/refs/heads/main/screenshots/lingco-language-labs-2026-07-25T225237.png
security:
- kind: authentication
  name: Lingco Language Labs Authentication
  slug: lingco-language-labs-authentication
  summary_line: openIdConnect/oauth2 · 7 schemes
- kind: domain-security
  name: Lingco Language Labs Domain Security
  slug: lingco-language-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lingco-language-labs
tags:
- Company
- Education
- EdTech
- Language Learning
- Learning Management
- LTI
- OneRoster
- Rostering
- Single Sign-On
- Interoperability
website: https://lingco.io/
---
