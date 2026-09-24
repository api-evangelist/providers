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
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-09-24'
api_count: 0
artifact_total: 16
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/auto-owners-insurance/refs/heads/main/security/auto-owners-insurance-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/auto-owners-insurance-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/auto-owners-insurance
- group: company
  title: ''
  type: Website
  url: https://www.auto-owners.com
- group: start
  title: ''
  type: CustomerPortal
  url: https://customercenter.auto-owners.com/cp/sign-in
- group: start
  title: ''
  type: PartnerPortal
  url: https://www.auto-owners.com/agent-login
- group: operate
  title: ''
  type: Support
  url: https://www.auto-owners.com/about/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.auto-owners.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.auto-owners.com/privacy
- group: company
  title: ''
  type: Careers
  url: https://www.auto-owners.com/about/career-opportunities
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/auto-owners
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/auto-owners-insurance/refs/heads/main/llms/auto-owners-insurance-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/auto-owners-insurance-llms.txt
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/auto-owners-insurance/refs/heads/main/plans/auto-owners-insurance-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/auto-owners-insurance-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/auto-owners-insurance/refs/heads/main/rate-limits/auto-owners-insurance-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/auto-owners-insurance-rate-limits.yml
coverage:
  checked: '2026-09-18'
  detail: 'Auto-Owners sells policies only through independent agents and ships no developer program: www.auto-owners.com/developers and /api return 404, the apex host redirects every path to the home page, the agent portal www.aoins.com answers every unauthenticated request with a 302 to its F5 /my.policy login, and the company''s own GitHub organization has no public repositories.'
  evidence:
  - status: 404
    url: https://www.auto-owners.com/developers
  - status: 404
    url: https://www.auto-owners.com/api
  - status: 400
    url: https://www.auto-owners.com/openapi.json
  - status: 302
    url: https://www.aoins.com/api
  - status: 404
    url: https://customercenter.auto-owners.com/.well-known/agent-card.json
  - status: 200
    url: https://github.com/auto-owners
  reason: no-developer-program
  state: none
created: '2025-01-01'
description: Auto-Owners Insurance is a mutual insurance company headquartered in Lansing, Michigan, offering auto, home, life, business, and farm insurance products through a network of independent agents. Founded in 1916, the company is consistently rated among the top mutual insurance companies in the United States. Auto-Owners provides online account management, claims filing, and agent portal services but does not currently offer a public developer API.
features:
- description: Comprehensive personal lines coverage including auto, home, condo, renters, life, and specialty policies such as pet, flood, umbrella, and farm insurance.
  name: Personal Insurance
- description: Commercial insurance products including commercial auto, workers compensation, bonds, commercial umbrella, and loss control services for businesses of all sizes.
  name: Business Insurance
- description: Access to a nationwide network of independent insurance agents who provide local, personalized expertise and policy management services.
  name: Independent Agent Network
- description: Digital claims submission and tracking for auto, property, and other covered losses through the policyholder online portal.
  name: Online Claims Filing
- description: Policyholder self-service portal for managing policies, making payments, viewing documents, and tracking claim status.
  name: Online Account Management
- description: Roadside assistance services for auto policyholders covering towing, battery jump, flat tire, fuel delivery, and lockout assistance.
  name: Road Trouble Assistance
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/auto-owners-insurance.png
integrations:
- description: Integration with agency management systems used by independent agents to manage policies, quotes, and client relationships.
  name: Independent Agent Systems
- description: Adherence to ACORD data standards used in the insurance industry for data exchange between carriers, agencies, and industry partners.
  name: ACORD Standards
layout: provider
modified: '2026-09-18'
name: Auto-Owners Insurance
nav: Providers
network: true
overview: 'Auto-Owners Insurance is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Auto Insurance, Home Insurance, Life Insurance, and Business Insurance.


  Auto-Owners Insurance''s developer surface includes support and 12 more developer resources.'
plans:
- name: Auto Owners Insurance Plans Pricing
  plan_count: 0
  slug: auto-owners-insurance-plans-pricing
press:
- date: ''
  title: A-O Blog
  url: https://www.auto-owners.com/ao-blog
- date: ''
  title: Auto-Owners Insurance Signs Agreement to Acquire ...
  url: https://www.prnewswire.com/news-releases/auto-owners-insurance-signs-agreement-to-acquire-capital-insurance-group-300798151.html
- date: ''
  title: 2024 U.S. Auto Insurance Study
  url: https://www.jdpower.com/business/press-releases/2024-us-auto-insurance-study
- date: ''
  title: Eric Coombs - Auto-Owners Insurance
  url: https://www.linkedin.com/in/eric-coombs-52a5462b3
- date: ''
  title: 'AI Cyberattacks Are Growing: What Businesses Can Do'
  url: https://www.auto-owners.com/ao-blog/-/blogs/ai-cyberattacks-are-growing-what-businesses-can-do
random_paper: 13
rate_limits:
- limit_count: 0
  name: Auto Owners Insurance Rate Limits
  slug: auto-owners-insurance-rate-limits
score:
  band: minimal
  composite: 9.6
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 9.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 21.2
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/auto-owners-insurance/refs/heads/main/screenshots/auto-owners-insurance-2026-06-20T172622.png
security:
- kind: domain-security
  name: Auto Owners Insurance Domain Security
  slug: auto-owners-insurance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: auto-owners-insurance
tags:
- Insurance
- Auto Insurance
- Home Insurance
- Life Insurance
- Business Insurance
- Mutual Insurance
- Independent Agents
use_cases:
- description: Protecting personal vehicles with liability, collision, comprehensive, uninsured motorist, and medical payment coverages.
  name: Personal Auto Coverage
- description: Insuring primary residences against damage, theft, liability, and additional living expenses with customizable coverage options.
  name: Homeowners Protection
- description: Providing commercial insurance packages for small to mid-size businesses covering property, liability, workers compensation, and commercial auto.
  name: Small Business Insurance
- description: Offering term, universal, and whole life insurance products to help individuals and families plan for long-term financial security.
  name: Life Insurance Planning
- description: Specialized farm insurance covering farmland, equipment, livestock, and agricultural operations for rural property owners.
  name: Farm and Agricultural Insurance
website: https://www.auto-owners.com
---
