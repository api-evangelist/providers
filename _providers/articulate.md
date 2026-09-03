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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.articulate.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://id.articulate.com/.well-known/openid-configuration
- group: docs
  title: ''
  type: Documentation
  url: https://www.articulatesupport.com/
- group: operate
  title: ''
  type: Support
  url: https://www.articulatesupport.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://community.articulate.com/
- group: company
  title: ''
  type: Blog
  url: https://www.articulate.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.articulate.com/360/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.articulate.com/360/trial/
- group: start
  title: ''
  type: Login
  url: https://id.articulate.com/redirect/360
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.articulate.com/360-terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.articulate.com/trust/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://www.articulatestatus.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/articulate-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.articulate.com/trust/
- group: auth
  title: ''
  type: Security
  url: https://www.articulate.com/.well-known/security.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/articulate-authentication.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: https://id.articulate.com/.well-known/openid-configuration
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/articulate-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/articulate-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/articulate-security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/articulate-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/articulate-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/articulate-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/articulate-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/articulate-llms.txt
created: '2026-07-17'
description: Articulate is an AI-powered workplace-training platform for creating, collaborating on, and distributing e-learning at scale. Its Articulate 360 suite pairs Rise (web-based responsive authoring) and Storyline (desktop authoring for custom interactive content) with Review 360 (stakeholder feedback), Reach 360 (an integrated LMS for sharing and tracking training), Content Library 360, an agentic AI Assistant, and localization into 80+ languages. The platform serves 125,000+ organizations across 187 countries and 133 million learners. Articulate does not publish a public developer REST API; its programmatic surface is the id.articulate.com identity provider (OpenID Connect / OAuth 2.0, Okta-hosted) used for single sign-on, plus standards-based content interoperability (SCORM and xAPI) emitted by its authoring tools. Surfaced as a portfolio company of ICONIQ Capital.
image: https://www.articulate.com/apple-touch-icon.png
layout: provider
modified: '2026-07-18'
name: Articulate
nav: Providers
network: true
overview: 'Articulate is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, EdTech, E-Learning, Learning Management, and Training.


  Articulate''s developer surface includes documentation, support, engineering blog, pricing, signup flow, authentication, and 19 more developer resources.'
random_paper: 20
scopes:
- name: Articulate Scopes
  scope_count: 7
  slug: articulate-scopes
  summary_line: 7 scopes · authorizationCode
score:
  band: developing
  composite: 39.7
  coverage:
    artifact_dirs: 9
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 39.7
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: fedramp
    jurisdictions_satisfied: 2
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 85.2
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/articulate/refs/heads/main/screenshots/articulate-2026-07-25T201329.png
security:
- kind: authentication
  name: Articulate Authentication
  slug: articulate-authentication
  summary_line: openIdConnect/oauth2 · 2 schemes
- kind: domain-security
  name: Articulate Domain Security
  slug: articulate-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Articulate Vulnerability Disclosure
  slug: articulate-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
- kind: trust-center
  name: Articulate Trust Center
  slug: articulate-trust-center
  summary_line: SOC 2, ISO 27001, FedRAMP, GDPR, CSA STAR
slug: articulate
tags:
- Company
- EdTech
- E-Learning
- Learning Management
- Training
- Course Authoring
- SSO
- OpenID Connect
website: https://www.articulate.com/
---
