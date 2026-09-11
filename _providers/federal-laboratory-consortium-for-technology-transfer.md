---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.8
  scored_at: '2026-09-10'
api_count: 1
apis:
- baseURL: https://api.federallabs.org
  baseurl_source: declared
  description: 'Public API behind the FLC Green Book mobile app. One published operation performs retrieval-augmented search over the sections of the Green Book (Federal Technology Transfer Legislation and Policy): s'
  name: FLC Greenbook API
  slug: flc-greenbook-api
artifact_total: 5
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
  title: ''
  type: Authentication
  url: authentication/federal-laboratory-consortium-for-technology-transfer-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/federal-laboratory-consortium-for-technology-transfer-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/federal-laboratory-consortium-for-technology-transfer-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/federal-laboratory-consortium-for-technology-transfer-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/federal-laboratory-consortium-for-technology-transfer-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/federal-laboratory-consortium-for-technology-transfer-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/federal-laboratory-consortium-for-technology-transfer-plans-pricing.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/federal-laboratory-consortium-for-technology-transfer-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/federal-laboratory-consortium-for-technology-transfer-packages.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/federal-laboratory-consortium-for-technology-transfer-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/federal-laboratory-consortium-for-technology-transfer-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/federal-laboratory-consortium-for-technology-transfer-greenbook-overlay.yaml
- group: auth
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
overview: 'Federal Laboratory Consortium for Technology Transfer publishes 1 API on the [APIs.io](https://apis.io/) network: FLC Greenbook API. Tagged areas include Federal-Government, Technology-Transfer, Research, Laboratories, and Government.


  Federal Laboratory Consortium for Technology Transfer''s developer surface includes documentation, API reference, support, engineering blog, signup flow, authentication, and 16 more developer resources.'
plans:
- name: Federal Laboratory Consortium For Technology Transfer Plans Pricing
  plan_count: 0
  slug: federal-laboratory-consortium-for-technology-transfer-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 1
  name: Federal Laboratory Consortium For Technology Transfer Rate Limits
  slug: federal-laboratory-consortium-for-technology-transfer-rate-limits
score:
  band: thin
  composite: 37.5
  coverage:
    artifact_dirs: 17
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 35.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 4.5
    contract_quality: 50.3
    developer_ergonomics: 37.5
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 21.1
  previous_composite: 2.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 38.9
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://raw.githubusercontent.com/api-evangelist/federal-laboratory-consortium-for-technology-transfer/refs/heads/main/screenshots/federal-laboratory-consortium-for-technology-transfer-2026-06-20T181119.png
security:
- kind: authentication
  name: Federal Laboratory Consortium For Technology Transfer Authentication
  slug: federal-laboratory-consortium-for-technology-transfer-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Federal Laboratory Consortium For Technology Transfer Domain Security
  slug: federal-laboratory-consortium-for-technology-transfer-domain-security
  summary_line: TLSv1.3 · DMARC
slug: federal-laboratory-consortium-for-technology-transfer
tags:
- Federal-Government
- Technology-Transfer
- Research
- Laboratories
- Government
- Innovation
- Search
website: https://www.federallabs.org/
---
