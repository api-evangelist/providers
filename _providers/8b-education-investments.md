---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 20.4
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: 'An OAuth-protected Model Context Protocol endpoint served from 8B''s own WordPress installation at www.8b.africa. Discovery is standards-conformant: an RFC 8414 authorization-server metadata document a'
  name: 8B Model Context Protocol Server
  slug: 8b-education-investments-mcp
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/8b-education-investments-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.8b.africa/
- group: company
  title: ''
  type: About
  url: https://www.8b.africa/about-8b/
- group: company
  title: ''
  type: Blog
  url: https://www.8b.africa/blogs/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.8b.africa/feed/
- group: operate
  title: ''
  type: Support
  url: https://www.8b.africa/contact-us/
- group: start
  title: ''
  type: Login
  url: https://www.8b.africa/community-login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.8b.africa/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.8b.africa/privacy-policy/
- group: operate
  title: ''
  type: FAQ
  url: https://www.8b.africa/studentloans/financing-faq/
- group: company
  title: ''
  type: Newsroom
  url: https://www.8b.africa/press/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/8b-education-investment-fund
- group: agent
  title: ''
  type: MCPServer
  url: mcp/8b-education-investments-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/8b-education-investments-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/8b-education-investments-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/8b-education-investments-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/8b-education-investments-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/8b-education-investments-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/8b-education-investments-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/8b-education-investments-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/8b-education-investments-plans-pricing.yml
created: '2026-09-05'
description: 8B Education Investments (legally 8B Finance, Inc., trading as 8B) is a New York headquartered education-finance company founded in 2017 by Lydiah Kemunto Bosire that helps African students pay for degrees at universities outside Africa. It operates a student-loan marketplace and eligibility comparison tool, an income-share and guarantee backed lending program originated with partner banks including Nelnet Bank, a University Reserve admissions product, and a free community platform of prospective and current students offering scholarships, courses, forums, events and job listings. 8B publishes no public developer program or API reference; the only machine-readable surfaces it serves are an llms.txt on its marketing site and an OAuth-protected Model Context Protocol endpoint exposed by its WordPress stack.
image: https://www.8b.africa/wp-content/uploads/2022/06/cropped-8b-Icon-192x192.png
layout: provider
mcp_servers:
- description: ''
  name: 8B Model Context Protocol Server
  slug: 8b-model-context-protocol-server
modified: '2026-09-05'
name: 8B Education Investments
nav: Providers
network: true
overview: '8B Education Investments publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, Student Loans, Financial Services, and Lending.


  8B Education Investments'' developer surface includes engineering blog, support, FAQ, authentication, and 17 more developer resources.'
plans:
- name: 8B Education Investments Plans Pricing
  plan_count: 0
  slug: 8b-education-investments-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: 8B Education Investments Rate Limits
  slug: 8b-education-investments-rate-limits
scopes:
- name: 8B Education Investments Scopes
  scope_count: 0
  slug: 8b-education-investments-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 24.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 64.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: authentication
  name: 8B Education Investments Authentication
  slug: 8b-education-investments-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: 8B Education Investments Domain Security
  slug: 8b-education-investments-domain-security
  summary_line: TLSv1.3 · DMARC
slug: 8b-education-investments
tags:
- Company
- Education
- Student Loans
- Financial Services
- Lending
- FinTech
- Africa
- Higher Education
- Study Abroad
- Community
website: https://www.8b.africa/
---
