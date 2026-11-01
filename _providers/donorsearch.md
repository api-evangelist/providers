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
- group: design
  href: https://artifacts.apis.io/donorsearch/conformance/donorsearch-conformance.yml
  title: ''
  type: Conformance
  url: conformance/donorsearch-conformance.yml
- group: other
  href: https://artifacts.apis.io/donorsearch/hosts/donorsearch-hosts.yml
  title: ''
  type: Hosts
  url: hosts/donorsearch-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.donorsearch.net/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.donorsearch.net/privacy-policy/
- group: other
  title: ''
  type: Leadership
  url: https://www.donorsearch.net/team/jay-frost/
- group: auth
  href: https://artifacts.apis.io/donorsearch/security/donorsearch-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/donorsearch-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://donorsearch.net/
- group: docs
  title: ''
  type: APIReference
  url: https://www.donorsearch.net/api-integrations/
- group: docs
  title: ''
  type: Documentation
  url: https://www.donorsearch.net/api-integrations/
- group: company
  title: ''
  type: Blog
  url: https://www.donorsearch.net/type/blog/
created: '2026-10-27'
description: DonorSearch provides a cloud‑based platform for donor prospect research, wealth screening, and fundraising intelligence. Leveraging AI and extensive donor data, it helps nonprofit organizations identify high‑value prospects, personalize outreach, and optimize campaign performance. The service includes API access for programmatic integration, enabling partners to embed donor insights directly into their applications and workflows.
image: https://www.donorsearch.net/wp-content/uploads/2021/06/cropped-DonorSearch-D-01-01-e1622565752180.png
layout: provider
modified: '2026-10-27'
name: DonorSearch
nav: Providers
network: true
overview: 'DonorSearch is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Nonprofit, Fundraising, DonorResearch, and API.


  DonorSearch''s developer surface includes API reference, documentation, engineering blog, and 7 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 15.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Donorsearch Domain Security
  slug: donorsearch-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: donorsearch
tags:
- Company
- Nonprofit
- Fundraising
- DonorResearch
- API
website: https://donorsearch.net/
---
