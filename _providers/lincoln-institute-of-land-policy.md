---
agent_readiness:
  band: agent-aware
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/lincoln-institute-of-land-policy/hosts/lincoln-institute-of-land-policy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lincoln-institute-of-land-policy-hosts.yml
- group: other
  href: https://artifacts.apis.io/lincoln-institute-of-land-policy/vendors/lincoln-institute-of-land-policy-vendors.yml
  title: ''
  type: Vendors
  url: vendors/lincoln-institute-of-land-policy-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lincolninst.edu/terms-service/
- group: start
  title: ''
  type: SignUp
  url: https://go.lincolninst.edu/sign-up-for-land-lines
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lincolninst.edu/privacy/
- group: auth
  href: https://artifacts.apis.io/lincoln-institute-of-land-policy/security/lincoln-institute-of-land-policy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lincoln-institute-of-land-policy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.lincolninst.edu
coverage:
  checked: '2026-10-26'
  detail: The Lincoln Institute of Land Policy website provides no developer program or API documentation.
  evidence:
  - status: 200
    url: https://www.lincolninst.edu
  reason: no-developer-program
  state: none
created: '2026-10-26'
description: The Lincoln Institute of Land Policy is a nonprofit research organization dedicated to improving the use, taxation, and stewardship of land. It conducts interdisciplinary research, provides policy analysis, and offers educational resources on land economics, land use, and fiscal systems. The institute engages scholars, policymakers, and practitioners worldwide to develop data-driven solutions for sustainable land management and equitable land taxation.
layout: provider
modified: '2026-10-26'
name: Lincoln Institute of Land Policy
nav: Providers
network: true
overview: 'Lincoln Institute of Land Policy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Research, LandPolicy, Nonprofit, and Education.


  Lincoln Institute of Land Policy''s developer surface includes signup flow and 6 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 10.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
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
  name: Lincoln Institute Of Land Policy Domain Security
  slug: lincoln-institute-of-land-policy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lincoln-institute-of-land-policy
tags:
- Company
- Research
- LandPolicy
- Nonprofit
- Education
website: https://www.lincolninst.edu
---
