---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 3
common:
- group: design
  title: ''
  type: Conformance
  url: conformance/siepe-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/siepe-conformance.yml
- group: agent
  title: ''
  type: WellKnownProbe
  url: well-known/siepe-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/siepe-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/siepe-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/siepe-rate-limits.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/siepe-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.siepe.com/
- group: company
  title: ''
  type: About
  url: https://www.siepe.com/company/about-us/
- group: operate
  title: ''
  type: Support
  url: https://www.siepe.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://www.siepe.com/category/blog/
- group: other
  title: ''
  type: Insights
  url: https://www.siepe.com/insights/
- group: company
  title: ''
  type: Press
  url: https://www.siepe.com/company/company-press/
- group: other
  title: ''
  type: CaseStudies
  url: https://www.siepe.com/case-studies/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.siepe.com/terms-of-use-2022-1
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.siepe.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Siepe
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/siepe/
coverage:
  checked: '2026-08-27'
  detail: Siepe sells software and managed services to private credit and CLO managers but ships no developer program at all — the word "API" appears nowhere on siepe.com, none of api./docs./developer./developers./portal./connect.siepe.com resolve in DNS, all 654 sitemap URLs were walked with no reference or spec page, and connectivity is delivered as bilateral managed integrations (its Octaura OMS link-up) negotiated through the contact form.
  evidence:
  - status: 200
    url: https://www.siepe.com/sitemap_index.xml
  - status: 404
    url: https://www.siepe.com/openapi.json
  - status: 404
    url: https://www.siepe.com/.well-known/agent-card.json
  - status: 404
    url: https://www.siepe.com/llms.txt
  reason: no-developer-program
  state: none
created: '2026-08-27'
description: 'Siepe is a Dallas, Texas fintech providing cloud-based software and technology-enabled services for private credit, CLO and alternative investment managers. Its front-to-back platform spans portfolio management, operations and accounting, collateral administration, compliance and legal, middle-office services, data extraction and a centralized data-management warehouse that normalizes borrower, lender, agent-bank and investor feeds into one real-time view. Siepe also operates managed technology and public-cloud services for asset managers. The company raised a $30M Series B led by WestCap in 2024 and holds SOC 2 Type II certification. Siepe publishes no public developer program: connectivity is delivered as bilateral, managed integrations (for example its 2026 Order Management System integration with Octaura for syndicated loan and CLO trading) rather than as a self-serve, documented public API.'
image: https://www.siepe.com/wp-content/uploads/2020/08/Siepe-Logo.png
layout: provider
modified: '2026-08-27'
name: Siepe
nav: Providers
network: true
overview: 'Siepe is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial-Services, Private Credit, CLO, and Alternative Investments.


  Siepe''s developer surface includes support, engineering blog, and 16 more developer resources.'
plans:
- name: Siepe Plans Pricing
  plan_count: 0
  slug: siepe-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Siepe Rate Limits
  slug: siepe-rate-limits
score:
  band: emerging
  composite: 13.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 13.3
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/siepe/refs/heads/main/screenshots/siepe-2026-09-02T155413.png
security:
- kind: domain-security
  name: Siepe Domain Security
  slug: siepe-domain-security
  summary_line: TLSv1.3 · DMARC
slug: siepe
tags:
- Company
- Financial-Services
- Private Credit
- CLO
- Alternative Investments
- Portfolio-Management
- Data Management
- Fund Administration
- Middle Office
- Managed Service
- Fintech
website: https://www.siepe.com/
---
