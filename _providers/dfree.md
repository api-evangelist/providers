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
api_count: 1
apis:
- description: Dfree provides a platform for financial empowerment tools and resources.
  name: Dfree API
  slug: dfree-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/dfree/hosts/dfree-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dfree-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dfree.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dfree.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://dfree.com/media/
- group: auth
  href: https://artifacts.apis.io/dfree/security/dfree-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dfree-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dfree.com
created: '2026-10-23'
description: Dfree is a movement focused on financial empowerment and wealth gap disruption, offering tools, tips, and resources through its website. The organization provides a foundation, community events, and a range of educational materials aimed at helping individuals improve their financial health and access to wealth-building opportunities.
image: https://dfree.com/wp-content/uploads/2026/02/dfree-community-cover-002.webp
layout: provider
modified: '2026-10-23'
name: Dfree
nav: Providers
network: true
overview: Dfree is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Education, Community, and Wealth.
random_paper: 14
score:
  band: minimal
  composite: 9.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 58.9
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dfree Domain Security
  slug: dfree-domain-security
  summary_line: TLSv1.2 · DMARC
slug: dfree
tags:
- Company
- Finance
- Education
- Community
- Wealth
website: https://dfree.com
---
