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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/coursestorm/plans/coursestorm-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/coursestorm-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/coursestorm/conformance/coursestorm-conformance.yml
  title: ''
  type: Conformance
  url: conformance/coursestorm-conformance.yml
- group: other
  href: https://artifacts.apis.io/coursestorm/hosts/coursestorm-hosts.yml
  title: ''
  type: Hosts
  url: hosts/coursestorm-hosts.yml
- group: other
  href: https://artifacts.apis.io/coursestorm/vendors/coursestorm-vendors.yml
  title: ''
  type: Vendors
  url: vendors/coursestorm-vendors.yml
- group: auth
  href: https://artifacts.apis.io/coursestorm/security/coursestorm-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coursestorm-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.coursestorm.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.coursestorm.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.coursestorm.com/get-a-free-demo
- group: operate
  title: ''
  type: Support
  url: https://www.coursestorm.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.coursestorm.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.coursestorm.com/pricing
coverage:
  checked: '2026-10-27'
  detail: The provider's documentation pages are HTML without any published OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specifications.
  evidence:
  - status: 200
    url: https://www.coursestorm.com/guides
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: CourseStorm provides cloud‑based class registration and management software for arts, community, and continuing education programs. It streamlines enrollment, payments, scheduling, reporting, and communications, helping organizations save time and grow their education offerings. The platform offers features such as class management, integrated payments, growth analytics, and customizable registration forms, targeting schools, nonprofits, and community groups across the United States.
image: https://cdn.prod.website-files.com/67bf68dcd823c76088e867ed/67d42b45c77645f4d16a3ec6_CourseStorm%20Preview%20Image.png
layout: provider
modified: '2026-10-27'
name: CourseStorm
nav: Providers
network: true
overview: 'CourseStorm is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Education, SaaS, Registration, Community, and Arts.


  CourseStorm''s developer surface includes getting-started guide, support, engineering blog, pricing, and 7 more developer resources.'
plans:
- name: Coursestorm Plans Pricing
  plan_count: 8
  slug: coursestorm-plans-pricing
random_paper: 22
score:
  band: emerging
  composite: 20.0
  coverage:
    artifact_dirs: 10
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 10.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Coursestorm Domain Security
  slug: coursestorm-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: coursestorm
tags:
- Education
- SaaS
- Registration
- Community
- Arts
website: https://www.coursestorm.com/
---
