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
    agent_skills: derived
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.8
  scored_at: '2026-11-06'
api_count: 2
apis:
- baseURL: https://api.federallabs.org
  baseurl_source: declared
  description: The Sections API from Federal Laboratory Consortium for Technology Transfer — 1 operation(s) for sections.
  name: Federal Laboratory Consortium for Technology Transfer Sections API
  slug: federal-laboratory-consortium-for-technology-transfer-sections-api
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://www.federallabs.org/
- group: docs
  title: ''
  type: Documentation
  url: https://api.federallabs.org/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.federallabs.org/docs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://federallabs.org/website-user-agreement
- group: operate
  title: ''
  type: Support
  url: https://federallabs.org/contact
- group: company
  title: ''
  type: Blog
  url: https://federallabs.org/communications/federal-lab-news
- group: start
  title: ''
  type: SignUp
  url: https://portal.federallabs.org/account/login.aspx
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/federallabs
- group: auth
  href: https://artifacts.apis.io/federal-laboratory-consortium-for-technology-transfer/authentication/federal-laboratory-consortium-for-technology-transfer-authentication.yml
  title: ''
  type: Authentication
  url: authentication/federal-laboratory-consortium-for-technology-transfer-authentication.yml
- group: design
  href: https://artifacts.apis.io/federal-laboratory-consortium-for-technology-transfer/conventions/federal-laboratory-consortium-for-technology-transfer-conventions.yml
  title: ''
  type: Conventions
  url: conventions/federal-laboratory-consortium-for-technology-transfer-conventions.yml
- group: design
  href: https://artifacts.apis.io/federal-laboratory-consortium-for-technology-transfer/conformance/federal-laboratory-consortium-for-technology-transfer-conformance.yml
  title: ''
  type: Conformance
  url: conformance/federal-laboratory-consortium-for-technology-transfer-conformance.yml
- group: design
  href: https://artifacts.apis.io/federal-laboratory-consortium-for-technology-transfer/errors/federal-laboratory-consortium-for-technology-transfer-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/federal-laboratory-consortium-for-technology-transfer-problem-types.yml
- group: design
  href: https://artifacts.apis.io/federal-laboratory-consortium-for-technology-transfer/lifecycle/federal-laboratory-consortium-for-technology-transfer-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/federal-laboratory-consortium-for-technology-transfer-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/federal-laboratory-consortium-for-technology-transfer/rate-limits/federal-laboratory-consortium-for-technology-transfer-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/federal-laboratory-consortium-for-technology-transfer-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/federal-laboratory-consortium-for-technology-transfer/plans/federal-laboratory-consortium-for-technology-transfer-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/federal-laboratory-consortium-for-technology-transfer-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/federal-laboratory-consortium-for-technology-transfer/data-model/federal-laboratory-consortium-for-technology-transfer-data-model.yml
  title: ''
  type: DataModel
  url: data-model/federal-laboratory-consortium-for-technology-transfer-data-model.yml
- group: build
  href: https://artifacts.apis.io/federal-laboratory-consortium-for-technology-transfer/packages/federal-laboratory-consortium-for-technology-transfer-packages.yml
  title: ''
  type: Packages
  url: packages/federal-laboratory-consortium-for-technology-transfer-packages.yml
- group: agent
  href: https://artifacts.apis.io/federal-laboratory-consortium-for-technology-transfer/mcp/federal-laboratory-consortium-for-technology-transfer-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/federal-laboratory-consortium-for-technology-transfer-mcp.yml
- group: agent
  href: https://artifacts.apis.io/federal-laboratory-consortium-for-technology-transfer/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/federal-laboratory-consortium-for-technology-transfer/llms/federal-laboratory-consortium-for-technology-transfer-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/federal-laboratory-consortium-for-technology-transfer-llms.txt
- group: other
  href: https://artifacts.apis.io/federal-laboratory-consortium-for-technology-transfer/overlays/federal-laboratory-consortium-for-technology-transfer-greenbook-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/federal-laboratory-consortium-for-technology-transfer-greenbook-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/federal-laboratory-consortium-for-technology-transfer/security/federal-laboratory-consortium-for-technology-transfer-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/federal-laboratory-consortium-for-technology-transfer-domain-security.yml
created: '2024-12-03'
description: The Federal Laboratory Consortium for Technology Transfer (FLC) is the nationwide network of more than 300 federal laboratories, agencies and research centers chartered by the Federal Technology Transfer Act of 1986 to move federally funded research into the wider economy. The FLC runs the FLC Business search over federal lab technologies and facilities, the interactive lab directory, the T2 Toolkit and Learning Center, and publishes the Green Book (Federal Technology Transfer Legislation and Policy). Its one machine-readable API surface is the public Greenbook API on api.federallabs.org, which backs the FLC Green Book mobile app with retrieval-augmented search over federal tech transfer legislation and policy.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/federal-laboratory-consortium-for-technology-transfer.png
layout: provider
modified: '2026-09-09'
name: Federal Laboratory Consortium for Technology Transfer
nav: Providers
network: true
overview: 'Federal Laboratory Consortium for Technology Transfer publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Sections API. Tagged areas include Federal Government, Technology-Transfer, Research, Laboratories, and Government.


  The Federal Laboratory Consortium for Technology Transfer catalog on APIs.io includes 1 Spectral governance ruleset.


  Federal Laboratory Consortium for Technology Transfer''s developer surface includes documentation, API reference, support, engineering blog, signup flow, authentication, and 16 more developer resources.'
plans:
- name: Federal Laboratory Consortium For Technology Transfer Plans Pricing
  plan_count: 0
  slug: federal-laboratory-consortium-for-technology-transfer-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 1
  name: Federal Laboratory Consortium For Technology Transfer Rate Limits
  slug: federal-laboratory-consortium-for-technology-transfer-rate-limits
rules:
- authorship: generated
  effective_rule_count: 89
  extends:
  - spectral:oas
  name: Federal Laboratory Consortium for Technology Transfer API Rules
  rule_count: 48
  severity_counts:
    error: 46
    hint: 0
    info: 1
    warn: 1
  slug: federal-laboratory-consortium-for-technology-transfer-rules
score:
  band: thin
  composite: 35.0
  coverage:
    artifact_dirs: 22
    catalog_earned: 49.5
    catalog_earned_first_party: 8.0
    catalog_gap: 65.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    contract_governance: 18.2
    contract_quality: 40.4
    developer_ergonomics: 37.5
    discoverability: 66.1
    operational_transparency: 21.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 35.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/federal-laboratory-consortium-for-technology-transfer/federal-laboratory-consortium-for-technology-transfer-2026-06-20T181119.png
security:
- kind: authentication
  name: Federal Laboratory Consortium For Technology Transfer Authentication
  slug: federal-laboratory-consortium-for-technology-transfer-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Federal Laboratory Consortium For Technology Transfer Domain Security
  slug: federal-laboratory-consortium-for-technology-transfer-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: flc-greenbook-search
  slug: federal-laboratory-consortium-for-technology-transfer-greenbook-search
slug: federal-laboratory-consortium-for-technology-transfer
tags:
- Federal Government
- Technology-Transfer
- Research
- Laboratories
- Government
- Innovation
- Search
website: https://www.federallabs.org/
---
