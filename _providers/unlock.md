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
    openapi_examples: documented
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 10.1
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: 'The public WordPress REST API (wp-json) of the Unlock website at www.unlock.com: the route index of the site''s content management system, catalogued as one site surface rather than as separate APIs.'
  name: Unlock Website (WordPress REST)
  slug: unlock-com-website-wordpress-rest
artifact_total: 10
common:
- group: company
  title: ''
  type: Website
  url: https://www.unlock.com/
- group: company
  title: ''
  type: About
  url: https://www.unlock.com/about/
- group: company
  title: ''
  type: Blog
  url: https://www.unlock.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://support.unlock.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.unlock.com/resources/faqs/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.unlock.com/what-it-costs/
- group: start
  title: ''
  type: SignUp
  url: https://app.unlock.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.unlock.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.unlock.com/legal/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.unlock.com/legal/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/unlock-com
- group: company
  title: ''
  type: Careers
  url: https://www.unlock.com/careers/
- group: auth
  href: https://artifacts.apis.io/unlock/authentication/unlock-authentication.yml
  title: ''
  type: Authentication
  url: authentication/unlock-authentication.yml
- group: design
  href: https://artifacts.apis.io/unlock/conventions/unlock-conventions.yml
  title: ''
  type: Conventions
  url: conventions/unlock-conventions.yml
- group: design
  href: https://artifacts.apis.io/unlock/errors/unlock-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/unlock-problem-types.yml
- group: design
  href: https://artifacts.apis.io/unlock/data-model/unlock-data-model.yml
  title: ''
  type: DataModel
  url: data-model/unlock-data-model.yml
- group: design
  href: https://artifacts.apis.io/unlock/lifecycle/unlock-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/unlock-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/unlock/conformance/unlock-conformance.yml
  title: ''
  type: Conformance
  url: conformance/unlock-conformance.yml
- group: operate
  href: https://artifacts.apis.io/unlock/rate-limits/unlock-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/unlock-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/unlock/plans/unlock-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/unlock-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/unlock/security/unlock-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/unlock-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/unlock/llms/unlock-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/unlock-llms.txt
- group: build
  href: https://artifacts.apis.io/unlock/packages/unlock-packages.yml
  title: ''
  type: Packages
  url: packages/unlock-packages.yml
- group: agent
  href: https://artifacts.apis.io/unlock/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/unlock/mcp/unlock-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/unlock-tool-crosswalk.yml
- group: build
  href: https://artifacts.apis.io/unlock/examples/unlock-active-states.json
  title: ''
  type: Examples
  url: examples/unlock-active-states.json
- group: build
  href: https://artifacts.apis.io/unlock/examples/unlock-company.json
  title: ''
  type: Examples
  url: examples/unlock-company.json
- group: build
  href: https://artifacts.apis.io/unlock/examples/unlock-social.json
  title: ''
  type: Examples
  url: examples/unlock-social.json
created: '2026-09-02'
description: 'Unlock Technologies, Inc. is a Tempe, Arizona fintech founded in 2020 by Jim Riccitelli, Dan Foster and Ryan Craft, with a branch office in Troy, Michigan. Its flagship product is the home equity agreement (HEA) — a homeowner receives a lump sum today, from $15,000 up to $500,000, in exchange for a share of the home''s future value, with no monthly payments and no interest, settled when the home is sold or refinanced or at the end of the ten-year term. Unlock charges an origination fee of up to 4.9% of the amount advanced, takes a share of the property capped at 49.9%, and caps its own return at 19.9% per year. The company is licensed in 26 US states and has raised roughly $52.6M in equity; its Series B included a $30M equity investment from D2 Asset Management, with Saluda Grade, Second Century Ventures and REACH also participating. Unlock sells to homeowners, not to developers: it publishes no developer program, no API reference, no SDKs, no key issuance and no partner API.
  The only machine-readable interfaces it exposes are the first-party WordPress REST namespaces behind www.unlock.com — `unlock/v1`, `unlock/v2` and `unlk/v1`, custom endpoints written for Unlock rather than WordPress core routes — plus the core `wp/v2` editorial content API. Both are captured here for discovery, are anonymously readable, and are read-only without credentials.'
examples:
- key_count: 2
  name: Unlock Active States
  slug: unlock-active-states
- key_count: 2
  name: Unlock Company
  slug: unlock-company
- key_count: 6
  name: Unlock Social
  slug: unlock-social
image: https://www.unlock.com/app/uploads/logo-footer-1.svg
layout: provider
modified: '2026-09-02'
name: Unlock
nav: Providers
network: true
overview: 'Unlock publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial Services, Fintech, Home Equity, and Mortgage.


  Unlock''s developer surface includes engineering blog, support, pricing, signup flow, authentication, code examples, and 22 more developer resources.'
plans:
- name: Unlock Plans Pricing
  plan_count: 0
  slug: unlock-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Unlock Rate Limits
  slug: unlock-rate-limits
score:
  band: emerging
  composite: 22.4
  coverage:
    artifact_dirs: 20
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 38.2
    contract_governance: 4.5
    contract_quality: 6.5
    developer_ergonomics: 25.6
    discoverability: 57.1
    operational_transparency: 2.6
  previous_composite: 23.3
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/unlock/unlock-2026-10-11T131454.png
security:
- kind: authentication
  name: Unlock Authentication
  slug: unlock-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Unlock Domain Security
  slug: unlock-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: unlock-content-research
  slug: unlock-content-research
- name: unlock-hea-eligibility-lookup
  slug: unlock-hea-eligibility-lookup
slug: unlock
tags:
- Company
- Financial Services
- Fintech
- Home Equity
- Mortgage
- Real Estate
- Consumer Lending
- Home Equity Agreement
- Personal Finance
- Content
website: https://www.unlock.com/
---
