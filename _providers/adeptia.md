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
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/adeptia/plans/adeptia-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/adeptia-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://security.adeptia.com/
- group: agent
  href: https://artifacts.apis.io/adeptia/llms/adeptia-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/adeptia-llms.txt
- group: other
  href: https://artifacts.apis.io/adeptia/hosts/adeptia-hosts.yml
  title: ''
  type: Hosts
  url: hosts/adeptia-hosts.yml
- group: other
  href: https://artifacts.apis.io/adeptia/vendors/adeptia-vendors.yml
  title: ''
  type: Vendors
  url: vendors/adeptia-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.adeptia.com/news
- group: other
  title: ''
  type: Leadership
  url: https://www.adeptia.com/about/team/charles-nardi
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/adeptia
- group: auth
  href: https://artifacts.apis.io/adeptia/security/adeptia-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/adeptia-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/adeptia/security/adeptia-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adeptia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://adeptia.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.adeptia.com/home/en-us/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.adeptia.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.adeptia.com/home/en-us/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.adeptia.com/request-demo
- group: operate
  title: ''
  type: Support
  url: https://www.adeptia.com/about/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.adeptia.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.adeptia.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.adeptia.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.adeptia.com/privacy-policy
coverage:
  checked: '2026-10-19'
  detail: Documentation is available at https://docs.adeptia.com/home/en-us/ but provides no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL specifications.
  evidence:
  - status: 200
    url: https://docs.adeptia.com/home/en-us/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-19'
description: Adeptia provides intelligent ETL and enterprise data automation solutions, enabling organizations to map, transform, and orchestrate data across on-premises and cloud environments. Their platform leverages AI-powered data mapping, configurable business rules, and self‑service partner onboarding to streamline complex data integration tasks for industries such as insurance, financial services, manufacturing, and healthcare. Adeptia’s offerings include data integration, API management, and automation tools designed to meet compliance demands and accelerate digital transformation initiatives.
layout: provider
modified: '2026-10-19'
name: Adeptia
nav: Providers
network: true
overview: 'Adeptia is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Integration, ETL, Automation, and Artificial Intelligence.


  Adeptia''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, and 14 more developer resources.'
plans:
- name: Adeptia Plans Pricing
  plan_count: 3
  slug: adeptia-plans-pricing
random_paper: 8
score:
  band: emerging
  composite: 21.5
  coverage:
    artifact_dirs: 10
    catalog_earned: 37.0
    catalog_earned_first_party: 12.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.9
  facets:
    access_clarity: 59.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 22.6
    discoverability: 53.6
    operational_transparency: 2.6
  previous_composite: 31.4
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/adeptia/adeptia-2026-11-03T120248.png
security:
- kind: domain-security
  name: Adeptia Domain Security
  slug: adeptia-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Adeptia Trust Center
  slug: adeptia-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: adeptia
tags:
- Company
- Data Integration
- ETL
- Automation
- Artificial Intelligence
website: https://adeptia.com/
---
