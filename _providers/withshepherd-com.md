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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/withshepherd-com/hosts/withshepherd-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/withshepherd-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/withshepherd-com/vendors/withshepherd-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/withshepherd-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.shepherdinsurance.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.shepherdinsurance.com/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://app.withshepherd.com/auth/sign-in
- group: company
  title: ''
  type: Blog
  url: https://www.shepherdinsurance.com/blog
- group: auth
  href: https://artifacts.apis.io/withshepherd-com/security/withshepherd-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/withshepherd-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.shepherdinsurance.com
coverage:
  checked: '2026-10-25'
  detail: The website provides no machine‑readable OpenAPI/GraphQL/AsyncAPI specifications and no developer portal was found.
  evidence:
  - status: 200
    url: https://www.shepherdinsurance.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-25'
description: Shepherd provides construction and renewable energy insurance solutions, leveraging data and technology to offer smarter underwriting and financial services for builders and operators. Backed by Costanoa Ventures, the company focuses on risk management, casualty, excess casualty, and builder’s risk products, serving the construction and renewable energy sectors with innovative insurance offerings.
image: https://www.shepherdinsurance.com/og/home
layout: provider
modified: '2026-10-25'
name: Shepherd
nav: Providers
network: true
overview: 'Shepherd is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurance, Construction, Renewable Energy, and Technology.


  Shepherd''s developer surface includes engineering blog and 7 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 11.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 12.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Withshepherd Com Domain Security
  slug: withshepherd-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: withshepherd-com
tags:
- Company
- Insurance
- Construction
- Renewable Energy
- Technology
website: https://www.shepherdinsurance.com
---
