---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 7.9
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: The League platform API, served from the Kong-fronted gateway at api.league.com. Unauthenticated requests return an RFC-shaped JSON:API error document (content-type application/vnd.api+json) and carry
  name: League Platform API
  slug: league-platform-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/league-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/league-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://league.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://league.com/digital-healthcare-developer-program/
- group: start
  title: ''
  type: SignUp
  url: https://league.com/digital-healthcare-developer-program/join/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://league.com/developer-program-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://league.com/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://help.league.com/ca-en
- group: company
  title: ''
  type: Blog
  url: https://league.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/leagueinc
- group: auth
  title: ''
  type: Compliance
  url: conformance/league-conformance.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/league-conformance.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/league-changelog.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/league-lifecycle.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/league-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/league-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/league-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/league-llms.txt
created: '2026-08-25'
description: 'League is a Toronto-founded (2014) healthcare platform company whose Health OS powers consumer healthcare experiences for payers, providers, consumer health brands and employers, and which now positions itself as a healthcare-grade agentic experience platform shipping pre-built AI Agent Teams for benefits navigation, care navigation and health coaching. Its data platform is built on the HL7 FHIR standard, using FHIR resources such as QuestionnaireResponse and CarePlan to model both integrated healthcare data and member-generated data across a longitudinal health record. League runs a Developer Program that gives contracted customers SDKs, a server-driven UI framework, back-end extensions and data integrations for embedding League into existing applications. The platform API is served from a live Kong-fronted gateway at api.league.com that answers with the JSON:API media type, but neither the API reference nor any machine-readable contract is published publicly: the documentation
  portal sits behind an Auth0 login and developer access is granted through a contact-sales form.'
image: https://e3r429ujnza.exactdn.com/wp-content/uploads/2022/06/league-logo.svg
layout: provider
modified: '2026-08-25'
name: League
nav: Providers
network: true
overview: 'League publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, Digital Health, and Health Benefits.


  League''s developer surface includes signup flow, support, engineering blog, changelog, and 14 more developer resources.'
plans:
- name: League Plans Pricing
  plan_count: 0
  slug: league-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: League Rate Limits
  slug: league-rate-limits
score:
  band: thin
  composite: 34.5
  coverage:
    artifact_dirs: 14
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 47.4
  previous_composite: 34.5
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/league/refs/heads/main/screenshots/league-2026-09-02T150232.png
security:
- kind: authentication
  name: League Authentication
  slug: league-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: League Domain Security
  slug: league-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: League Vulnerability Disclosure
  slug: league-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: League Trust Center
  slug: league-trust-center
  summary_line: SOC 2 Type 2, HITRUST, ISO/IEC 27001, HIPAA, NIST 800-53 Rev. 5, NIST 800-171 Rev. 3, NIST CSF, NIST AI RMF, FIPS 140-2, 21 CFR Part 11, 23 NYCRR 500, CPCSC Level 1, Canada PBMM, WCAG
slug: league
tags:
- Company
- Health
- Healthcare
- Digital Health
- Health Benefits
- Interoperability
- FHIR
- Agents
- Artificial Intelligence
- Patient Engagement
- Insurance
- Software-as-a-Service
website: https://league.com/
---
