---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 34.6
  scored_at: '2026-09-08'
api_count: 15
apis:
- baseURL: https://apis.accela.com
  baseurl_source: declared
  description: The public REST API to the Accela Civic Platform. 417 operations across fifteen published Swagger 2.0 documents cover transactional records, inspections and checklists, contacts and licensed professio
  name: Accela Construct API (V4)
  slug: accela-construct-api-v4
- baseURL: https://auth.accela.com
  baseurl_source: declared
  description: The Construct authorization server. Three operations — POST /oauth2/authorize (authorization code), POST /oauth2/token (authorization code, implicit and password-credential grants) and GET /oauth2/tok
  name: Accela Authentication API (OAuth 2.0)
  slug: accela-authentication-api-oauth-20
- description: 'CivicData.com is Accela''s free open-data platform for government agencies, described on its own site as "a free open data platform built by Accela" and "Built on open source using CKAN". It exposes a '
  name: CivicData Open Data API (CKAN) — END OF LIFE
  slug: civicdata-open-data-api-ckan-end-of-life
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/accela-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.accela.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.accela.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.accela.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.accela.com/docs/api_reference/api-index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.accela.com/docs/construct-gettingStarted.html
- group: operate
  title: ''
  type: Support
  url: https://www.accela.com/services/technical-support/
- group: operate
  title: ''
  type: HelpCenter
  url: https://success.accela.com/s/
- group: company
  title: ''
  type: Blog
  url: https://www.accela.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.accela.com/blog/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Accela-Inc
- group: start
  title: ''
  type: SignUp
  url: https://developer.accela.com/Register/Register
- group: start
  title: ''
  type: Login
  url: https://developer.accela.com/Login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.accela.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.accela.com/privacy-policy/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.accela.com/docs/construct_api_v4_rel_notes.html
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/accela-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.accela.com/civic-platform/security/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/accela-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/accela-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/accela-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/accela-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/accela-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/accela-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/accela-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/accela-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/accela-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/accela-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/accela-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/accela-sandbox.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/accela-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/accela-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Components
  url: components/accela-components.yml
created: '2026-09-06'
description: Accela is a San Ramon, California govtech company whose cloud Civic Platform runs permitting, planning, licensing, code enforcement, inspections, asset management and citizen service requests for state and local government agencies worldwide. Its public developer surface is the Accela Construct API (V4) — a 417-operation REST API served from apis.accela.com and documented as fifteen Swagger 2.0 documents on the Accela Developer Portal, covering records, inspections, contacts and professionals, addresses/parcels/owners, assets and assessments, documents, payments and shopping carts, reports, search, citizens, CivicID and platform settings. Access is OAuth 2.0 against auth.accela.com with agency- and environment-scoped tokens, and every request is bound to a specific government tenant through the x-accela-agency and x-accela-environment headers.
image: https://www.accela.com/wp-content/uploads/2026/07/AccelaLogo-website.webp
layout: provider
modified: '2026-09-06'
name: Accela
nav: Providers
network: true
overview: 'Accela publishes 2 APIs on the [APIs.io](https://apis.io/) network: Construct API (V4) and Authentication API (OAuth 2.0). Tagged areas include GovTech, Government, Permitting, Licensing, and Code Enforcement.


  Accela''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, changelog, and 27 more developer resources.'
plans:
- name: Accela Plans Pricing
  plan_count: 0
  slug: accela-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Accela Rate Limits
  slug: accela-rate-limits
scopes:
- name: Accela Scopes
  scope_count: 0
  slug: accela-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 57.4
  coverage:
    artifact_dirs: 21
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 48.9
    developer_ergonomics: 73.2
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 57.4
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 15
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: ccpa
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 88.9
  schema_version: 0.20.0
  scored_at: '2026-09-08'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Accela Authentication
  slug: accela-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Accela Domain Security
  slug: accela-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: accela
tags:
- GovTech
- Government
- Permitting
- Licensing
- Code Enforcement
- Inspections
- Asset Management
- Citizen Engagement
- Land Management
- Civic Platform
- Public Sector
- SaaS
website: https://www.accela.com/
---
