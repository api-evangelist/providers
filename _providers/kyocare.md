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
- description: The Attain platform API is the backend serving the Kyo Care portal (portal.kyocare.com) and the Kyo Care mobile app. It is an OAuth 2.0 / OpenID Connect protected API fronted by AWS Cognito, publishin
  name: Kyo Attain Platform API
  slug: attain
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://kyocare.com
- group: start
  title: ''
  type: Portal
  url: https://portal.kyocare.com
- group: start
  title: ''
  type: SignUp
  url: https://kyocare.com/aba-therapy-services/enroll-today/
- group: operate
  title: ''
  type: Support
  url: https://kyocare.com/autism-aba-therapy-faqs/
- group: company
  title: ''
  type: Blog
  url: https://kyocare.com/news/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kyocare.com/privacy-policy/
- group: company
  title: ''
  type: Careers
  url: https://kyocare.com/careers/
- group: auth
  title: ''
  type: Authentication
  url: authentication/kyocare-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/kyocare-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kyocare-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kyocare-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kyocare-conventions.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kyocare-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kyocare-llms.txt
created: '2026-07-17'
description: Kyo (kyocare.com) is a US provider of Applied Behavior Analysis (ABA) therapy for autistic children and young adults, delivering in-home, in-school and center-based care across 20+ locations with in-network coverage from major insurers. Kyo runs a client-facing digital surface — the Kyo Care portal and mobile app — for scheduling, session notes, progress tracking and family communication, backed by the internal "Attain" platform API (api.attain.kyocare.com) that publishes live OpenID Connect and RFC 8414 discovery documents over AWS Cognito, plus a private Workato-managed partner gateway at api.kyocare.com. Kyo publishes no public developer program, documentation or SDKs; its API surface is private to its own applications and payer integrations.
image: https://kyocare.com/wp-content/uploads/2022/06/cropped-favicon-192x192-1.png
layout: provider
modified: '2026-07-19'
name: Kyo
nav: Providers
network: true
overview: 'Kyo publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Autism, ABA Therapy, and Behavioral Health.


  Kyo''s developer surface includes developer portal, signup flow, support, engineering blog, authentication, and 9 more developer resources.'
random_paper: 15
scopes:
- name: Kyocare Scopes
  scope_count: 2
  slug: kyocare-scopes
  summary_line: 2 scopes · authorizationCode/clientCredentials
score:
  band: emerging
  composite: 24.6
  coverage:
    artifact_dirs: 9
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 24.6
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 47.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kyocare/refs/heads/main/screenshots/kyocare-2026-07-25T224350.png
security:
- kind: authentication
  name: Kyocare Authentication
  slug: kyocare-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Kyocare Domain Security
  slug: kyocare-domain-security
  summary_line: TLSv1.3 · DMARC
slug: kyocare
tags:
- Company
- Healthcare
- Autism
- ABA Therapy
- Behavioral Health
- Patient Engagement
- Digital Health
- Scheduling
- Private API
website: https://kyocare.com
---
