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
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/hr-cloud/plans/hr-cloud-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hr-cloud-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/hr-cloud/llms/hr-cloud-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hr-cloud-llms.txt
- group: other
  href: https://artifacts.apis.io/hr-cloud/hosts/hr-cloud-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hr-cloud-hosts.yml
- group: other
  href: https://artifacts.apis.io/hr-cloud/vendors/hr-cloud-vendors.yml
  title: ''
  type: Vendors
  url: vendors/hr-cloud-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hrcloud.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hrcloud.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.hrcloud.com/workmates/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.hrcloud.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/HRCloud
- group: auth
  href: https://artifacts.apis.io/hr-cloud/security/hr-cloud-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hr-cloud-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.hrcloud.com/
coverage:
  checked: '2026-10-27'
  detail: HR Cloud documentation pages return HTML shells requiring JavaScript rendering, preventing machine‑readable contract discovery.
  evidence:
  - status: 200
    url: https://www.hrcloud.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-26'
description: HR Cloud provides an AI‑powered enterprise HR platform designed for frontline teams. It unifies onboarding, core HR, employee engagement, time‑off, performance management and payroll in a single cloud solution. The platform offers a mobile‑first experience, integrates with popular tools, and includes features such as Maya AI onboarding assistant, employee recognition, shift planning and robust reporting, aimed at improving workforce productivity and compliance.
image: https://www.hrcloud.com/og-image.jpg
layout: provider
modified: '2026-10-26'
name: HR Cloud
nav: Providers
network: true
overview: 'HR Cloud is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Human Resources, Software-as-a-Service, Frontline, and Artificial Intelligence.


  HR Cloud''s developer surface includes pricing, engineering blog, and 9 more developer resources.'
plans:
- name: Hr Cloud Plans Pricing
  plan_count: 3
  slug: hr-cloud-plans-pricing
random_paper: 6
score:
  band: emerging
  composite: 13.2
  coverage:
    artifact_dirs: 12
    catalog_earned: 34.0
    catalog_earned_first_party: 12.0
    catalog_gap: 81.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.8
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 46.4
    operational_transparency: 2.6
  previous_composite: 19.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/hr-cloud/hr-cloud-2026-11-03T133508.png
security:
- kind: domain-security
  name: Hr Cloud Domain Security
  slug: hr-cloud-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hr-cloud
tags:
- Human Resources
- Software-as-a-Service
- Frontline
- Artificial Intelligence
website: https://www.hrcloud.com/
---
