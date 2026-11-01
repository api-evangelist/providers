---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 32.5
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Cybrary Agentic Access
  operation_count: 3
  slug: cybrary-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- baseURL: https://app.cybrary.it/courses/api
  baseurl_source: declared
  description: Daily completion-event exports as xAPI statements.
  name: Cybrary Completions API
  slug: cybrary-completions-api
artifact_total: 12
collections:
- collection_type: open
  name: Cybrary Export Completions API
  slug: open-cybrary-completions-api
common:
- group: commercial
  href: https://artifacts.apis.io/cybrary/plans/cybrary-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cybrary-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/cybrary/mcp/cybrary-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/cybrary-mcp.yml
- group: company
  title: ''
  type: Website
  url: https://www.cybrary.it/
- group: docs
  title: ''
  type: Documentation
  url: https://help.cybrary.it/hc/en-us
- group: docs
  title: ''
  type: APIReference
  url: https://help.cybrary.it/completions-export-integration
- group: start
  title: ''
  type: GettingStarted
  url: https://help.cybrary.it/cybrary-for-teams
- group: operate
  title: ''
  type: Support
  url: https://help.cybrary.it/hc/en-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.cybrary.it/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.cybrary.it/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Cybrary
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cybrary.it/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.cybrary.it/register
- group: start
  title: ''
  type: Login
  url: https://app.cybrary.it/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cybrary.it/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cybrary.it/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://www.cybrary.it/responsible-disclosure-program
- group: auth
  href: https://artifacts.apis.io/cybrary/security/cybrary-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cybrary-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/cybrary/security/cybrary-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cybrary-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/cybrary/authentication/cybrary-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cybrary-authentication.yml
- group: auth
  href: https://artifacts.apis.io/cybrary/scopes/cybrary-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/cybrary-scopes.yml
- group: design
  href: https://artifacts.apis.io/cybrary/conventions/cybrary-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cybrary-conventions.yml
- group: design
  href: https://artifacts.apis.io/cybrary/conformance/cybrary-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cybrary-conformance.yml
- group: design
  href: https://artifacts.apis.io/cybrary/errors/cybrary-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cybrary-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cybrary/lifecycle/cybrary-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/cybrary-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/cybrary/data-model/cybrary-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cybrary-data-model.yml
- group: agent
  href: https://artifacts.apis.io/cybrary/llms/cybrary-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cybrary-llms.txt
- group: agent
  href: https://artifacts.apis.io/cybrary/well-known/cybrary-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cybrary-well-known.yml
- group: build
  href: https://artifacts.apis.io/cybrary/packages/cybrary-packages.yml
  title: ''
  type: Packages
  url: packages/cybrary-packages.yml
- group: agent
  href: https://artifacts.apis.io/cybrary/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/cybrary/agentic-access/cybrary-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cybrary-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/cybrary/rate-limits/cybrary-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cybrary-rate-limits.yml
- group: other
  href: https://artifacts.apis.io/cybrary/overlays/cybrary-completions-export-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cybrary-completions-export-overlay.yaml
created: '2026-08-04'
description: Cybrary is a cybersecurity and IT skills-development platform used by individuals and enterprise teams for hands-on training, certification preparation and workforce upskilling. The catalog spans certification prep paths (Security+, CISSP, CISA, CISM, CCSP, CCNA, AWS security tracks), role-based career paths (SOC analyst, penetration tester, security engineer, incident handler, network engineer), skill paths, virtual labs, assessments and security awareness training. Cybrary for Teams adds administrative surfaces for enterprise customers — SAML 2.0 single sign-on with Okta, OneLogin and Microsoft Entra ID, SCIM 2.0 automated user provisioning with a per-tenant base URL and bearer token, bulk user upload, goals and custom career paths. Its one publicly documented API is the Completions Export Integration, an OAuth 2.0 client-credentials REST API that returns daily course, lab, assessment and career-path completion events as xAPI (Experience API) statements for ingestion into
  a customer LMS, HRIS or reporting warehouse.
finops:
- has_sources: true
  method: derived
  name: Cybrary Finops
  primary_unit: month billed annually
  service_category: ''
  slug: cybrary-finops
  template: false
image: https://cdn.prod.website-files.com/63eef15e3ff8fd318e9a6888/645ef224f84b330beefae1e7_Cybrary%20Opengraph%20(1).png
layout: provider
modified: '2026-08-04'
name: Cybrary
nav: Providers
network: true
overview: 'Cybrary publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Completions API. Tagged areas include Company, Cybersecurity, Training, Education, and LMS.


  Cybrary''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 25 more developer resources.'
plans:
- name: Cybrary Plans Pricing
  plan_count: 5
  slug: cybrary-plans-pricing
- name: Cybrary Price Estimates
  plan_count: 0
  slug: cybrary-price-estimates
random_paper: 20
rate_limits:
- limit_count: 2
  name: Cybrary Rate Limits
  slug: cybrary-rate-limits
scopes:
- name: Cybrary Scopes
  scope_count: 1
  slug: cybrary-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: developing
  composite: 47.4
  coverage:
    artifact_dirs: 24
    catalog_earned: 60.0
    catalog_earned_first_party: 20.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 7.9
  facets:
    access_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 15.5
    developer_ergonomics: 49.4
    discoverability: 66.1
    operational_transparency: 36.8
  previous_composite: 39.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 40.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/cybrary/cybrary-2026-08-07T164005.png
security:
- kind: authentication
  name: Cybrary Authentication
  slug: cybrary-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Cybrary Domain Security
  slug: cybrary-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Cybrary Vulnerability Disclosure
  slug: cybrary-vulnerability-disclosure
  summary_line: Hackerone · contact published
skill_count: 1
skills:
- name: Export Cybrary completions as xAPI statements
  slug: cybrary-export-completions-to-lms
slug: cybrary
tags:
- Company
- Cybersecurity
- Training
- Education
- LMS
- Certification
- Workforce Development
- xAPI
- SCIM
- Security Awareness
website: https://www.cybrary.it/
---
