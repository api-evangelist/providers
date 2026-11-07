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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/neostella/plans/neostella-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/neostella-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/neostella/llms/neostella-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/neostella-llms.txt
- group: other
  href: https://artifacts.apis.io/neostella/hosts/neostella-hosts.yml
  title: ''
  type: Hosts
  url: hosts/neostella-hosts.yml
- group: other
  href: https://artifacts.apis.io/neostella/vendors/neostella-vendors.yml
  title: ''
  type: Vendors
  url: vendors/neostella-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.neostella.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.neostella.com/
- group: start
  title: ''
  type: SignUp
  url: https://neostella.com/neosummit/register/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.neostella.com/privacy/
- group: company
  title: ''
  type: Newsroom
  url: https://neostella.com/resources/news/
- group: docs
  title: ''
  type: Documentation
  url: https://help.neostella.com/
- group: auth
  href: https://artifacts.apis.io/neostella/security/neostella-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/neostella-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://neostella.com/
- group: operate
  title: ''
  type: Support
  url: https://neostella.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://neostella.com/blogs/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://neostella.com/legal-docs/terms-of-service/
- group: commercial
  title: ''
  type: Pricing
  url: https://neostella.com/pricing/
- group: operate
  title: ''
  type: Support
  url: https://neostella.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://neostella.com/blogs/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://neostella.com/legal-docs/terms-of-service/
coverage:
  checked: '2026-10-28'
  detail: No public developer program or API documentation was found on the provider's website.
  evidence:
  - status: 200
    url: https://neostella.com
  reason: no-developer-program
  state: none
created: '2026-10-28'
description: Neostella provides enterprise legal case management software, offering a comprehensive platform that includes case management, document management, analytics, reporting, time tracking, document generation, intake CRM, AI solutions, workflow automation, and integrations. Designed for law firms and in‑house legal teams, the SaaS solution helps streamline legal processes, improve efficiency, and support practice areas such as personal injury, mass tort, veterans affairs, social security, immigration, and family law.
image: https://neostella.com/wp-content/uploads/2026/05/Hero-Banner-Screens-Cropped.webp
layout: provider
modified: '2026-10-28'
name: Neostella
nav: Providers
network: true
overview: 'Neostella is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Legal Tech, Software-as-a-Service, Case Management, and Enterprise.


  Neostella''s developer surface includes signup flow, documentation, support, engineering blog, pricing, and 14 more developer resources.'
plans:
- name: Neostella Plans Pricing
  plan_count: 1
  slug: neostella-plans-pricing
random_paper: 7
score:
  band: emerging
  composite: 17.4
  coverage:
    artifact_dirs: 11
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.0
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 56.3
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 26.4
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/neostella/neostella-2026-11-03T140104.png
security:
- kind: domain-security
  name: Neostella Domain Security
  slug: neostella-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: neostella
tags:
- Company
- Legal Tech
- Software-as-a-Service
- Case Management
- Enterprise
website: https://neostella.com/
---
