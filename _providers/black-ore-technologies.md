---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
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
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 15.1
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://blackore.ai/
- group: other
  title: ''
  type: Company
  url: https://blackore.ai/company
- group: commercial
  title: ''
  type: Pricing
  url: https://blackore.ai/pricing
- group: auth
  title: ''
  type: Security
  url: https://blackore.ai/security
- group: auth
  title: ''
  type: TrustCenter
  url: https://blackore.ai/security
- group: auth
  title: ''
  type: Compliance
  url: https://blackore.ai/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://blackore.ai/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://blackore.ai/terms-of-service
- group: company
  title: ''
  type: Blog
  url: https://blackore.ai/news
- group: start
  title: ''
  type: SignUp
  url: https://auth.blackore.ai/u/login/identifier
- group: start
  title: ''
  type: Login
  url: https://auth.blackore.ai/u/login/identifier
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/black-ore-ai/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/black-ore-technologies-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/black-ore-technologies-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/black-ore-technologies-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/black-ore-technologies-domain-security.yml
created: '2026-07-17'
description: Black Ore Technologies is an Austin, Texas AI company building AI infrastructure for tax and financial services. Founded in 2022 by Eyal Shinar (previously founder of the fintech unicorn Fundbox) and Pavel Kapovski, the company emerged from stealth in November 2023 with $60 million in funding led by Andreessen Horowitz (a16z) and Oak HC/FT. Its flagship product, Tax Autopilot, combines proprietary AI with federal and state tax codes to autonomously execute the full lifecycle of complex tax returns for Certified Public Accountants and accounting firms, spanning document ingestion, intelligent extraction, return preparation, workpaper generation, and tax software integration (UltraTax, Lacerte, ProConnect). The platform covers 1040 individual returns plus 1041, 1065, and Schedule K-1/K-3 automation, and is used by 40% of the top 20 leading firms. Black Ore does not publish a public developer API or OpenAPI at this time; its authentication is handled by an Auth0-hosted OpenID Connect
  tenant at auth.blackore.ai.
image: https://cdn.prod.website-files.com/68ecfebb353873d3847e78ca/68ecfebb353873d3847e7a29_black-ore-logo.svg
layout: provider
modified: '2026-07-18'
name: Black Ore Technologies
nav: Providers
network: true
overview: 'Black Ore Technologies is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Financial-Services, Tax, and Accounting.


  Black Ore Technologies'' developer surface includes pricing, engineering blog, signup flow, authentication, and 12 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 22.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 22.2
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/black-ore-technologies/refs/heads/main/screenshots/black-ore-technologies-2026-07-25T203235.png
security:
- kind: authentication
  name: Black Ore Technologies Authentication
  slug: black-ore-technologies-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Black Ore Technologies Domain Security
  slug: black-ore-technologies-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Black Ore Technologies Trust Center
  slug: black-ore-technologies-trust-center
  summary_line: SOC 2 Type II
slug: black-ore-technologies
tags:
- Company
- Artificial Intelligence
- Financial-Services
- Tax
- Accounting
- Fintech
- Automation
- Tax Preparation
website: https://blackore.ai/
---
