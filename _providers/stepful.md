---
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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.stepful.com/
- group: company
  title: ''
  type: Blog
  url: https://www.stepful.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.stepful.com/faq
- group: start
  title: ''
  type: Login
  url: https://classroom.stepful.com/users/sign_in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.stepful.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.stepful.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/stepful
- group: auth
  title: ''
  type: Compliance
  url: https://www.stepful.com/regulatory-information
- group: design
  title: ''
  type: Conformance
  url: conformance/stepful-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/stepful-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stepful-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/stepful-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/stepful-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/stepful-rate-limits.yml
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/stepful_stock/
coverage:
  checked: '2026-08-29'
  detail: Stepful ships an AI-assisted healthcare-training platform only as an end-user product — its student classroom and staff admin apps are Rails/Devise logins with no API, and full contract discovery across six stepful.com hosts found no OpenAPI, GraphQL, MCP, agent card or webhook surface; the only APIs answering on a stepful.com hostname are vendor CNAMEs (c.stepful.com is Converge, issuer app.runconverge.com; k.stepful.com is a PostHog proxy) and are not Stepful's.
  evidence:
  - status: 404
    url: https://www.stepful.com/openapi.json
  - status: 404
    url: https://www.stepful.com/.well-known/agent-card.json
  - status: 404
    url: https://classroom.stepful.com/api/v1/openapi.json
  - status: 404
    url: https://admin.stepful.com/api-docs
  - status: 200
    url: https://c.stepful.com/.well-known/openid-configuration
  reason: no-developer-program
  state: none
created: '2026-08-29'
description: 'Stepful is a New York-based healthcare workforce education company that trains people with a high-school education for entry-level allied-health roles in as little as four months. It runs live, cohort-based online programs — Medical Assistant, Pharmacy Technician, Patient Care Technician, Medical Administrative Assistant, Surgical Technologist, Dental Assistant, Phlebotomy Technician, Sterile Processing and Practical Nursing — pairing virtual instructor-led classes and 1:1 coaching with at-home clinical skills kits, employer-site clinical rotations and an AI-assisted practice platform, then places graduates into hospital and clinic jobs. Its "School-as-a-Service" employer product lets health systems stand up in-house training and upskilling pipelines. Stepful is backed by Y Combinator, Oak HC/FT and Reach Capital, has raised a $31.5M Series B and a $55M Series C, and reports having served more than 30,000 students. It is a Delaware corporation approved to operate by state career-school
  boards in Alabama, California, Indiana, Kentucky, Michigan, Ohio, Pennsylvania, Texas and Utah. Stepful publishes no public developer API: its student classroom and staff admin applications are both authenticated-only, and no OpenAPI, GraphQL, MCP or webhook contract is served from any host it controls.'
image: https://cdn.prod.website-files.com/60fae2951956f7e83dd6018b/6894edaeb10999d0cfd0257e_logo.svg
layout: provider
modified: '2026-08-29'
name: Stepful
nav: Providers
network: true
overview: 'Stepful is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, Healthcare, Workforce Development, and Online Learning.


  Stepful''s developer surface includes engineering blog, support, and 13 more developer resources.'
plans:
- name: Stepful Plans Pricing
  plan_count: 0
  slug: stepful-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Stepful Rate Limits
  slug: stepful-rate-limits
score:
  band: emerging
  composite: 17.1
  coverage:
    artifact_dirs: 8
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 17.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 44.4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Stepful Domain Security
  slug: stepful-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: stepful
tags:
- Company
- Education
- Healthcare
- Workforce Development
- Online Learning
- Certification
- Allied Health
- Career Training
- Staffing
- EdTech
website: https://www.stepful.com/
---
