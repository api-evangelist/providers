---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
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
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 10.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: SignUp.com provides an API for managing sign‑up sheets, events, and participants. Documentation is not publicly available.
  name: SignUp API
  slug: signup-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/signup-com/plans/signup-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/signup-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/signup-com/well-known/signup-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/signup-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/signup-com/hosts/signup-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/signup-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/signup-com/vendors/signup-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/signup-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://signup.com/Terms
- group: operate
  title: ''
  type: Support
  url: https://support.signup.com/
- group: start
  title: ''
  type: SignUp
  url: https://signup.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://signup.com/Privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://signup.com/Pricing
- group: auth
  href: https://artifacts.apis.io/signup-com/security/signup-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/signup-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://signup.com/
coverage:
  checked: '2026-10-27'
  detail: Documentation pages redirect to 404, no public OpenAPI or other machine‑readable contract is available.
  evidence:
  - status: 404
    url: https://signup.com/developers
  - status: 404
    url: https://signup.com/api-docs
  - status: 404
    url: https://signup.com/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: SignUp.com provides online sign‑up sheets and coordination solutions for schools, churches, teams, nonprofits, and businesses. Their platform enables users to create, share, and manage sign‑up forms, streamline event planning, and collaborate efficiently across various organizations.
image: https://vspot.s3.amazonaws.com/sign-up/Facebook-Images/SignUp-Facebook-Default-Image.jpg
layout: provider
modified: '2026-10-27'
name: SignUp.com
nav: Providers
network: true
overview: 'SignUp.com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Software-as-a-Service, Scheduling, Volunteer, Education, and Non-Profit.


  SignUp.com''s developer surface includes support, signup flow, pricing, and 8 more developer resources.'
plans:
- name: Signup Com Plans Pricing
  plan_count: 5
  slug: signup-com-plans-pricing
random_paper: 18
score:
  band: emerging
  composite: 16.6
  coverage:
    artifact_dirs: 10
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.5
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 22.1
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/signup-com/signup-com-2026-11-03T143208.png
security:
- kind: domain-security
  name: Signup Com Domain Security
  slug: signup-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: signup-com
tags:
- Software-as-a-Service
- Scheduling
- Volunteer
- Education
- Non-Profit
website: https://signup.com/
---
