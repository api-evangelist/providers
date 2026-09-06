---
access_model:
  confidence: low
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
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
  score: 2.5
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mind-foundry-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.mindfoundry.ai/
- group: company
  title: ''
  type: Blog
  url: https://www.mindfoundry.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://www.mindfoundry.ai/contactus
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MindFoundry
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mindfoundry.ai/privacy-policy
- group: build
  title: ''
  type: Packages
  url: packages/mind-foundry-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mind-foundry-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/mind-foundry-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mind-foundry-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mind-foundry-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/mind-foundry-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mind-foundry-rate-limits.yml
coverage:
  checked: '2026-08-25'
  detail: Mind Foundry's site is a 139-URL HubSpot marketing site for two defence products (SENTRY, NIGHTINGALE) with no developer, docs or API path in its own sitemap; the one public API it ever shipped, OPTaaS, has been silently retired — mindfoundry.ai/optaas 404s, its optaas.mindfoundry.ai and demo.optimize.mindfoundry.ai hosts are NXDOMAIN, and the MindFoundry GitHub organisation now reports 0 public repositories.
  evidence:
  - status: 200
    url: https://www.mindfoundry.ai/sitemap.xml
  - status: 404
    url: https://mindfoundry.ai/optaas
  - status: 200
    url: https://api.github.com/orgs/MindFoundry
  - status: 404
    url: https://www.mindfoundry.ai/.well-known/api-catalog
  - status: 0
    url: https://optaas.mindfoundry.ai/
  reason: no-developer-program
  state: none
created: '2026-08-25'
description: Mind Foundry is an Oxford University spin-out, founded in 2016 and headquartered at Ewert House in Oxford, United Kingdom, that builds applied machine learning for high-stakes, real-world problems across defence, national security, insurance, infrastructure and government. Its current products are SENTRY, a multi-modal sensor-fusion capability that detects, classifies and tracks objects in time and space from raw sensor data, and NIGHTINGALE, AI-enabled acoustic intelligence for anti-submarine warfare that has been integrated with Thales systems. Mind Foundry delivers these as deployed and integrated systems for customers and prime contractors rather than as a public, self-serve developer API, and it publishes no developer portal, API reference or machine-readable specification. The company previously operated OPTaaS (Optimization as a Service), a Bayesian optimisation API with first-party Python and R clients; the OPTaaS service hosts and its GitHub client repositories are
  no longer reachable, and the PyPI client has had no release since January 2024. Mind Foundry publishes ISO 27001, Cyber Essentials Plus and JOSCAR certifications on its own site.
image: https://www.mindfoundry.ai/hubfs/MF%20Logo%20L.png
layout: provider
modified: '2026-08-25'
name: Mind Foundry
nav: Providers
network: true
overview: 'Mind Foundry is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Machine-Learning, Defence, and National Security.


  Mind Foundry''s developer surface includes engineering blog, support, and 11 more developer resources.'
plans:
- name: Mind Foundry Plans Pricing
  plan_count: 0
  slug: mind-foundry-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Mind Foundry Rate Limits
  slug: mind-foundry-rate-limits
score:
  band: emerging
  composite: 12.6
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 12.6
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mind-foundry/refs/heads/main/screenshots/mind-foundry-2026-09-02T150545.png
security:
- kind: domain-security
  name: Mind Foundry Domain Security
  slug: mind-foundry-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mind-foundry
tags:
- Company
- Artificial Intelligence
- Machine-Learning
- Defence
- National Security
- Sensor Fusion
- Responsible AI
- Optimization
- United Kingdom
website: https://www.mindfoundry.ai/
---
