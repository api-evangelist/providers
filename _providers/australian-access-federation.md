---
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 13.7
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Provides identity federation services for Australian research and education institutions.
  name: Australian Access Federation API
  slug: australian-access-federation-api
artifact_total: 3
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/australian-access-federation/refs/heads/main/plans/australian-access-federation-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/australian-access-federation-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/australian-access-federation/refs/heads/main/well-known/australian-access-federation-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/australian-access-federation-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/australian-access-federation/refs/heads/main/hosts/australian-access-federation-hosts.yml
  title: ''
  type: Hosts
  url: hosts/australian-access-federation-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/australian-access-federation/refs/heads/main/vendors/australian-access-federation-vendors.yml
  title: ''
  type: Vendors
  url: vendors/australian-access-federation-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.aaf.edu.au/
- group: operate
  title: ''
  type: Support
  url: https://aaf.edu.au/support/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.aaf.edu.au/
- group: start
  title: ''
  type: SignUp
  url: https://aaf.edu.au/project/register-now-for-the-aaf-focus-group/
- group: auth
  title: ''
  type: Security
  url: https://aaf.edu.au/support/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aaf.edu.au/wp-content/uploads/Privacy-Collection_v1.2_2025.pdf
- group: commercial
  title: ''
  type: Pricing
  url: https://aaf.edu.au/start/pricing/
- group: company
  title: ''
  type: Newsroom
  url: https://aaf.edu.au/about/news/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/australian-access-federation/refs/heads/main/security/australian-access-federation-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/australian-access-federation-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aaf.edu.au/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/australian-access-federation/refs/heads/main/security/australian-access-federation-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/australian-access-federation-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aaf.edu.au/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://api.edu.au/mcp
  - status: 401
    url: https://support.aaf.edu.au/mcp
  - status: 200
    url: https://aaf.edu.au/
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: The Australian Access Federation (AAF) is the national trust and identity capability for Australia’s research and higher education sector. It enables seamless, secure access to digital resources across institutions with a single identity, supports federated services like EduGAIN, ORCID, and Rapid IdP, and connects thousands of users and services both domestically and internationally. AAF drives collaboration, reduces costs, and fosters innovation across the research ecosystem.
layout: provider
modified: '2026-10-13'
name: Australian Access Federation
nav: Providers
network: true
overview: 'Australian Access Federation is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Identity, Education, Research, and Federation.


  Australian Access Federation''s developer surface includes support, signup flow, pricing, and 13 more developer resources.'
plans:
- name: Australian Access Federation Plans Pricing
  plan_count: 9
  slug: australian-access-federation-plans-pricing
random_paper: 11
score:
  band: emerging
  composite: 25.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 42.0
    catalog_earned_first_party: 12.0
    catalog_gap: 73.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 55.4
    operational_transparency: 26.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 20.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Australian Access Federation Domain Security
  slug: australian-access-federation-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: australian-access-federation
tags:
- Company
- Identity
- Education
- Research
- Federation
website: https://aaf.edu.au/
---
