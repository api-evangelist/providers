---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.0
  scored_at: '2026-09-05'
api_count: 2
apis:
- baseURL: https://www.unlock.com/wp-json
  baseurl_source: declared
  description: The first-party REST namespaces Unlock registers on www.unlock.com — `unlock/v1`, `unlock/v2` and `unlk/v1`. These are custom endpoints written for Unlock, not WordPress core routes, and they serve th
  name: Unlock Site Content API
  slug: unlock-site-content-api
- baseURL: https://www.unlock.com/wp-json
  baseurl_source: declared
  description: Anonymous read access to the Unlock editorial archive through the WordPress core `wp/v2` namespace — 251 blog posts, 24 pages, 778 media items, 9 Learn articles, 13 homeowner stories, 6 education topi
  name: Unlock Editorial API
  slug: unlock-editorial-api
artifact_total: 14
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
  title: ''
  type: Authentication
  url: authentication/unlock-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/unlock-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/unlock-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/unlock-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/unlock-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/unlock-conformance.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/unlock-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/unlock-plans-pricing.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/unlock-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/unlock-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/unlock-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/unlock-tool-crosswalk.yml
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
- key_count: 3
  name: Unlock Logos
  slug: unlock-logos
- key_count: 3
  name: Unlock Menus Primary
  slug: unlock-menus-primary
- key_count: 6
  name: Unlock Social
  slug: unlock-social
- key_count: 2
  name: Unlock Statuses
  slug: unlock-statuses
- key_count: 6
  name: Unlock Taxonomies
  slug: unlock-taxonomies
- key_count: 18
  name: Unlock Types
  slug: unlock-types
image: https://www.unlock.com/app/uploads/logo-footer-1.svg
layout: provider
modified: '2026-09-02'
name: Unlock
nav: Providers
network: true
overview: 'Unlock publishes 2 APIs on the [APIs.io](https://apis.io/) network: Site Content API and Editorial API. Tagged areas include Company, Financial Services, FinTech, Home Equity, and Mortgage.


  Unlock''s developer surface includes engineering blog, support, pricing, signup flow, authentication, and 20 more developer resources.'
plans:
- name: Unlock Plans Pricing
  plan_count: 0
  slug: unlock-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Unlock Rate Limits
  slug: unlock-rate-limits
score:
  band: emerging
  composite: 23.7
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.7
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 4.5
    contract_quality: 16.7
    developer_ergonomics: 20.8
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 25.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: authentication
  name: Unlock Authentication
  slug: unlock-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Unlock Domain Security
  slug: unlock-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: unlock
tags:
- Company
- Financial Services
- FinTech
- Home Equity
- Mortgage
- Real Estate
- Consumer Lending
- Home Equity Agreement
- Personal Finance
- Content
website: https://www.unlock.com/
---
