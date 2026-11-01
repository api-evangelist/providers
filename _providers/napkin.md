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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.8
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Napkin Agentic Access
  operation_count: 3
  slug: napkin-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 1
apis:
- baseURL: https://api.napkin.ai
  baseurl_source: declared
  description: Create, poll, and download programmatic visual generations.
  name: Napkin Visuals API
  slug: napkin-visuals-api
artifact_total: 10
collections:
- collection_type: open
  name: Napkin Visuals API
  slug: open-napkin-visuals-api
common:
- group: commercial
  href: https://artifacts.apis.io/napkin/plans/napkin-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/napkin-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/napkin/overlays/napkin-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/napkin-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/napkin/agentic-access/napkin-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/napkin-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://www.napkin.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.napkin.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://api.napkin.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://api.napkin.ai/api/create-visual-request
- group: start
  title: ''
  type: GettingStarted
  url: https://api.napkin.ai/
- group: operate
  title: ''
  type: ChangeLog
  url: https://api.napkin.ai/docs/changelog
- group: operate
  title: ''
  type: Support
  url: https://help.napkin.ai/en/
- group: company
  title: ''
  type: Blog
  url: https://www.napkin.ai/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.napkin.ai/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.napkin.ai/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.napkin.ai/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.napkin.ai/privacy-policy/
- group: auth
  href: https://artifacts.apis.io/napkin/authentication/napkin-authentication.yml
  title: ''
  type: Authentication
  url: authentication/napkin-authentication.yml
- group: auth
  href: https://artifacts.apis.io/napkin/scopes/napkin-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/napkin-scopes.yml
- group: design
  href: https://artifacts.apis.io/napkin/lifecycle/napkin-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/napkin-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://api.napkin.ai/docs/changelog
- group: design
  href: https://artifacts.apis.io/napkin/conventions/napkin-conventions.yml
  title: ''
  type: Conventions
  url: conventions/napkin-conventions.yml
- group: design
  href: https://artifacts.apis.io/napkin/errors/napkin-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/napkin-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/napkin/llms/napkin-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/napkin-llms.txt
- group: agent
  href: https://artifacts.apis.io/napkin/well-known/napkin-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/napkin-well-known.yml
- group: auth
  href: https://artifacts.apis.io/napkin/well-known/napkin-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/napkin-security.txt
- group: auth
  href: https://artifacts.apis.io/napkin/security/napkin-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/napkin-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://vdp.napkin.ai
- group: auth
  href: https://artifacts.apis.io/napkin/security/napkin-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/napkin-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/napkin/mcp/napkin-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/napkin-mcp.yml
- group: agent
  href: https://artifacts.apis.io/napkin/skills/napkin-generate-visual.md
  title: ''
  type: AgentSkill
  url: skills/napkin-generate-visual.md
- group: design
  href: https://artifacts.apis.io/napkin/data-model/napkin-data-model.yml
  title: ''
  type: DataModel
  url: data-model/napkin-data-model.yml
- group: design
  href: https://artifacts.apis.io/napkin/conformance/napkin-conformance.yml
  title: ''
  type: Conformance
  url: conformance/napkin-conformance.yml
created: '2026-07-17'
description: 'Napkin AI turns typed or pasted text into editable visuals — diagrams, charts, icons, and infographics — and into full presentation decks, with no prompting or design skill required. Two products share one text-to-visual engine: Napkin Visuals (standalone diagrams and graphics) and Napkin Slides (beta AI presentation agent). Napkin also ships a developer API (currently a developer preview) for generating visuals programmatically: submit text, poll the asynchronous request, and download the results as SVG, PNG, or PPT. The API authenticates with account bearer tokens or an OAuth 2.0 authorization-code flow. Napkin is an AI company backed by CRV.'
finops:
- has_sources: true
  method: derived
  name: Napkin Finops
  primary_unit: person
  service_category: ''
  slug: napkin-finops
  template: false
image: https://www.napkin.ai/favicon.ico
layout: provider
modified: '2026-07-20'
name: Napkin
nav: Providers
network: true
overview: 'Napkin publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Visuals API. Tagged areas include Company, Artificial Intelligence, Visualization, Diagramming, and Infographics.


  Napkin''s developer surface includes documentation, API reference, getting-started guide, changelog, support, engineering blog, pricing, and 24 more developer resources.'
plans:
- name: Napkin Plans Pricing
  plan_count: 4
  slug: napkin-plans-pricing
random_paper: 17
scopes:
- name: Napkin Scopes
  scope_count: 2
  slug: napkin-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: strong
  composite: 56.5
  coverage:
    artifact_dirs: 22
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.5
  facets:
    access_clarity: 84.2
    contract_governance: 4.5
    contract_quality: 52.0
    developer_ergonomics: 58.9
    discoverability: 66.1
    operational_transparency: 34.2
  previous_composite: 55.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 37.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/napkin/napkin-2026-08-07T184622.png
security:
- kind: authentication
  name: Napkin Authentication
  slug: napkin-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Napkin Domain Security
  slug: napkin-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Napkin Vulnerability Disclosure
  slug: napkin-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: Generate a visual from text (Napkin API)
  slug: napkin-generate-visual
slug: napkin
tags:
- Company
- Artificial Intelligence
- Visualization
- Diagramming
- Infographics
- Presentations
- Content Generation
- Developer API
- Design
website: https://www.napkin.ai/
---
