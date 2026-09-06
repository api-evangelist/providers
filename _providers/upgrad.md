---
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
    error_semantics: verified
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
  score: 24.6
  scored_at: '2026-09-05'
api_count: 2
apis:
- baseURL: https://partner.upgrad.com
  baseurl_source: declared
  description: 'Channel-partner operations API for upGrad''s referral and franchise network: partner onboarding and KYC document upload/verification, prospect (lead) capture and status transitions, store and team-memb'
  name: upGrad Partner Service API
  slug: upgrad-partner-service-api
- baseURL: https://learner-analytics-rest.upgrad.com
  baseurl_source: declared
  description: 'Learner-experience analytics service behind upGrad''s learning platform: daily reading-time leaderboards per course and per user, micro-interaction notification records, and administrative cache evicti'
  name: upGrad Learner Experience Analytics API
  slug: upgrad-learner-experience-analytics-api
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://www.upgrad.com/
- group: company
  title: ''
  type: About
  url: https://www.upgrad.com/about/
- group: company
  title: ''
  type: Blog
  url: https://www.upgrad.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.upgrad.com/us/contact/
- group: start
  title: ''
  type: Login
  url: https://learn.upgrad.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.upgrad.com/us/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.upgrad.com/us/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/upgrad
- group: operate
  title: ''
  type: StatusPage
  url: https://status.upgrad.com/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/upgrad-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/upgrad-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/upgrad-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/upgrad-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/upgrad-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/upgrad-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/upgrad-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/upgrad-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/upgrad-packages.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/upgrad-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/upgrad-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/upgrad-rate-limits.yml
created: '2026-09-02'
description: 'upGrad is an online higher-education and workforce-upskilling platform headquartered in Mumbai, India, founded in 2015 by Ronnie Screwvala, Mayank Kumar and Phalgun Kompalli. It delivers degrees, executive certifications, bootcamps and doctoral programmes in partnership with global universities including Liverpool John Moores University, Golden Gate University, O.P. Jindal Global University, IIIT Bangalore, IIM Kozhikode and IIT Kharagpur, alongside a study-abroad advisory business covering the USA, UK, Canada, Australia, Germany and Ireland. Its public API surface is not a marketed developer programme: it is a large internal microservice estate on upgrad.com subdomains, of which two Spring Boot services publish their springdoc OpenAPI 3.0.1 documents anonymously at /api-docs — a Partner Service covering channel-partner onboarding, prospects, stores, team hierarchy, commission rules and partner invoicing/credit notes, and a Learner Experience Analytics service covering reading-time
  leaderboards and micro-interaction notifications.'
image: https://prod-mphs.upgrad.com/hubfs/NF%20upGrad%20Assets/University%20Logos%20and%20Images/upGrad%20Logos/upgrad-logo.svg
layout: provider
modified: '2026-09-02'
name: upGrad
nav: Providers
network: true
overview: 'upGrad publishes 2 APIs on the [APIs.io](https://apis.io/) network: Partner Service API and Learner Experience Analytics API. Tagged areas include Education, EdTech, Online Learning, Higher Education, and Certification.


  upGrad''s developer surface includes engineering blog, support, authentication, and 19 more developer resources.'
plans:
- name: Upgrad Plans Pricing
  plan_count: 0
  slug: upgrad-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Upgrad Rate Limits
  slug: upgrad-rate-limits
score:
  band: thin
  composite: 36.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 51.8
    developer_ergonomics: 20.8
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 18.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 36.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 46.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: authentication
  name: Upgrad Authentication
  slug: upgrad-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Upgrad Domain Security
  slug: upgrad-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Upgrad Vulnerability Disclosure
  slug: upgrad-vulnerability-disclosure
  summary_line: Hackerone · security.txt
slug: upgrad
tags:
- Education
- EdTech
- Online Learning
- Higher Education
- Certification
- Learning Analytics
- Partner Management
- India
website: https://www.upgrad.com/
---
