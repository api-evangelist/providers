---
access_model:
  confidence: high
  label: Public read-only content API, no signup, no credential
  onboarding: unknown
  pricing: unknown
  public: true
  source:
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 11.9
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: 3Bar Biologics Agentic Access
  operation_count: 19
  slug: 3bar-biologics-agentic-access
  summary_line: 19 operations
api_count: 1
apis:
- description: 'The public WordPress REST API (wp-json) of the 3Bar Biologics website at www.3barbiologics.com: the route index of the site''s content management system, catalogued as one site surface rather than as s'
  name: 3Bar Biologics Website (WordPress REST)
  slug: 3barbiologics-com-website-wordpress-rest
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.3barbiologics.com/
- group: company
  title: ''
  type: About
  url: https://www.3barbiologics.com/why-3bar/
- group: other
  title: ''
  type: Services
  url: https://www.3barbiologics.com/design-develop-deliver/
- group: other
  title: ''
  type: CaseStudies
  url: https://www.3barbiologics.com/case-studies/
- group: company
  title: ''
  type: Blog
  url: https://www.3barbiologics.com/news-insights/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.3barbiologics.com/feed/
- group: operate
  title: ''
  type: Contact
  url: https://www.3barbiologics.com/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.3barbiologics.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/3bar-biologics-inc-/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/3bar-biologics/refs/heads/main/authentication/3bar-biologics-authentication.yml
  title: ''
  type: Authentication
  url: authentication/3bar-biologics-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/3bar-biologics/refs/heads/main/errors/3bar-biologics-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/3bar-biologics-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/3bar-biologics/refs/heads/main/conventions/3bar-biologics-conventions.yml
  title: ''
  type: Conventions
  url: conventions/3bar-biologics-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/3bar-biologics/refs/heads/main/data-model/3bar-biologics-data-model.yml
  title: ''
  type: DataModel
  url: data-model/3bar-biologics-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/3bar-biologics/refs/heads/main/conformance/3bar-biologics-conformance.yml
  title: ''
  type: Conformance
  url: conformance/3bar-biologics-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/3bar-biologics/refs/heads/main/lifecycle/3bar-biologics-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/3bar-biologics-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/3bar-biologics/refs/heads/main/rate-limits/3bar-biologics-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/3bar-biologics-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/3bar-biologics/refs/heads/main/plans/3bar-biologics-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/3bar-biologics-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/3bar-biologics/refs/heads/main/llms/3bar-biologics-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/3bar-biologics-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/3bar-biologics/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/3bar-biologics/refs/heads/main/examples/3bar-biologics-examples.yml
  title: ''
  type: Examples
  url: examples/3bar-biologics-examples.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/3bar-biologics/refs/heads/main/agentic-access/3bar-biologics-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/3bar-biologics-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/3bar-biologics/refs/heads/main/security/3bar-biologics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/3bar-biologics-domain-security.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/3bar-biologics/refs/heads/main/packages/3bar-biologics-packages.yml
  title: ''
  type: Packages
  url: packages/3bar-biologics-packages.yml
created: '2026-09-05'
description: '3Bar Biologics (3BarBio) is an agricultural biotechnology company in Columbus, Ohio, spun out of research at The Ohio State University and operating as the first contract development and manufacturing organization (CDMO) dedicated to agricultural biologicals. Its business is getting living microbes to the field alive: the patented LiveMicrobe platform, including the Iso-Pak and Re-Pak delivery systems, keeps beneficial bacteria viable through storage and distribution, the problem that has historically limited adoption of microbial crop inputs. The company sells design, development, biomanufacturing and fulfillment services to discovery companies, distributors and bulk suppliers, and previously marketed its own Bio-YIELD inoculant to corn, soybean and wheat growers in the eastern Corn Belt. 3Bar Biologics is a manufacturer and services business, not a software vendor: it publishes no developer program, no developer portal, no API documentation, no SDKs and no pricing for any
  programmatic product. The only machine-readable interface it exposes is the WordPress REST content API behind its corporate website at www.3barbiologics.com, which is captured here for discovery purposes. That surface is anonymously readable, read-only, entirely undocumented by the company, and carries two reproducible defects on its media collection that are recorded in this profile.'
image: https://www.3barbiologics.com/wp-content/uploads/2021/05/3B-Logo-Website-512-x-512.png
layout: provider
modified: '2026-09-05'
name: 3Bar Biologics
nav: Providers
network: true
overview: '3Bar Biologics publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Agriculture, AgTech, Biotechnology, and Agricultural Biologicals.


  3Bar Biologics'' developer surface includes engineering blog, authentication, code examples, and 20 more developer resources.'
plans:
- name: 3Bar Biologics Plans Pricing
  plan_count: 0
  slug: 3bar-biologics-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: 3Bar Biologics Rate Limits
  slug: 3bar-biologics-rate-limits
score:
  band: emerging
  composite: 17.5
  coverage:
    artifact_dirs: 20
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 6.5
    developer_ergonomics: 25.6
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 17.5
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: authentication
  name: 3Bar Biologics Authentication
  slug: 3bar-biologics-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: 3Bar Biologics Domain Security
  slug: 3bar-biologics-domain-security
  summary_line: TLSv1.3 · HSTS
slug: 3bar-biologics
tags:
- Company
- Agriculture
- AgTech
- Biotechnology
- Agricultural Biologicals
- Biomanufacturing
- CDMO
- Microbials
- Crop Inputs
- Sustainability
- Contract Manufacturing
website: https://www.3barbiologics.com/
---
