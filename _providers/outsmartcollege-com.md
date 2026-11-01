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
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/outsmartcollege-com/hosts/outsmartcollege-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/outsmartcollege-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/outsmartcollege-com/vendors/outsmartcollege-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/outsmartcollege-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/outsmartcollege-com/security/outsmartcollege-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/outsmartcollege-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://outsmartcollege.com/
- group: operate
  title: ''
  type: Support
  url: https://joinoutsmart.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://joinoutsmart.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://joinoutsmart.com/privacy-policy
coverage:
  checked: '2026-10-24'
  detail: No public developer documentation or API reference was found on the provider's website.
  evidence:
  - status: 200
    url: https://joinoutsmart.com
  reason: no-developer-program
  state: none
created: '2026-10-24'
description: Outsmart College provides a platform that helps higher education institutions reimagine student engagement, recruitment, and enrollment processes through data-driven tools and personalized experiences. The service offers marketing automation, lead management, and analytics to improve college outreach and student conversion, aiming to modernize the higher education landscape.
image: https://joinoutsmart.com/outsmart-logo-orange.svg
layout: provider
modified: '2026-10-24'
name: Outsmart College
nav: Providers
network: true
overview: 'Outsmart College is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Marketing, SaaS, HigherEducation, and Recruitment.


  Outsmart College''s developer surface includes support and 6 more developer resources.'
random_paper: 22
score:
  band: minimal
  composite: 9.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
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
  name: Outsmartcollege Com Domain Security
  slug: outsmartcollege-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: outsmartcollege-com
tags:
- Education
- Marketing
- SaaS
- HigherEducation
- Recruitment
website: https://outsmartcollege.com/
---
