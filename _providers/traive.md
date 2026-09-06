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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/traive-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://traive.com.br/
- group: company
  title: ''
  type: Blog
  url: https://traive.com.br/blog/
- group: start
  title: ''
  type: Login
  url: https://auth.traive-prod.com/realms/traive-prod/protocol/openid-connect/auth
- group: commercial
  title: ''
  type: TermsOfService
  url: https://traive.com.br/termos-e-condicoes-de-uso/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://traive.com.br/politica-de-privacidade/
- group: operate
  title: ''
  type: Contact
  url: https://traive.com.br/contato/
- group: company
  title: ''
  type: Careers
  url: https://traive.com.br/carreiras/
- group: company
  title: ''
  type: Press
  url: https://traive.com.br/imprensa/
- group: other
  title: ''
  type: CaseStudies
  url: https://traive.com.br/cases/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Traive-Finance
- group: agent
  title: ''
  type: WellKnown
  url: well-known/traive-well-known.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/traive-openid-configuration.json
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/traive-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/traive-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/traive-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/traive-llms.txt
created: '2026-07-17'
description: Traive is a Brazilian agri-fintech that connects agribusiness with financial investors, using AI and data analytics to simplify credit access in the agricultural sector. Its Traive Agro product handles agricultural credit commercialization with risk analysis, process automation, and financing access, while Traive Finance provides credit risk analysis and access to qualified agricultural assets with traceability. The platform serves 160K+ registered producers and manages over R$6B in structured recurring credit operations. Traive publishes no public developer API; its platform authenticates via a Keycloak OpenID Connect provider whose public discovery documents reveal an internal service estate (credit, farmers, retailers, ERP integration, GraphQL) captured in this profile.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/traive.png
layout: provider
modified: '2026-07-21'
name: Traive
nav: Providers
network: true
overview: 'Traive is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Agriculture, Fintech, Credit, and Risk Analysis.


  Traive''s developer surface includes engineering blog, authentication, and 15 more developer resources.'
random_paper: 0
scopes:
- name: Traive Scopes
  scope_count: 50
  slug: traive-scopes
  summary_line: 50 scopes · authorizationCode/clientCredentials/deviceCode/ciba
score:
  band: emerging
  composite: 16.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - brazil
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  previous_composite: 16.6
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/traive/refs/heads/main/screenshots/traive-2026-09-02T164117.png
security:
- kind: authentication
  name: Traive Authentication
  slug: traive-authentication
  summary_line: openIdConnect/oauth2 · 1 scheme
- kind: domain-security
  name: Traive Domain Security
  slug: traive-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: traive
tags:
- Company
- Agriculture
- Fintech
- Credit
- Risk Analysis
- Lending
- AgTech
- Brazil
website: https://traive.com.br/
---
