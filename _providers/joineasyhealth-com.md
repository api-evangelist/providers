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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Public API referenced on the Easyhealth website.
  name: Easyhealth API
  slug: easyhealth-api
artifact_total: 6
common:
- group: other
  href: https://artifacts.apis.io/joineasyhealth-com/hosts/joineasyhealth-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/joineasyhealth-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/joineasyhealth-com/vendors/joineasyhealth-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/joineasyhealth-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.easyhealth.com/terms-of-service
- group: start
  title: ''
  type: SignUp
  url: https://www.easyhealth.com/signup-3/thank-you
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.easyhealth.com/privacy
- group: other
  title: ''
  type: Leadership
  url: https://www.easyhealth.com/team
- group: auth
  href: https://artifacts.apis.io/joineasyhealth-com/security/joineasyhealth-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/joineasyhealth-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.joineasyhealth.com/
coverage:
  checked: '2026-10-29'
  detail: The provider's public website contains human‑readable documentation but no machine‑readable OpenAPI, AsyncAPI, GraphQL, or other spec.
  evidence:
  - status: 200
    url: https://www.easyhealth.com/contact-2-0
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: 'EasyHealth delivers better health outcomes for the 100M+ members on government sponsored insurance. Empowering healthy communities through proactive care in collaboration with health plans and provider groups. Focused on clinical excellence to engage members where they want to receive care: in the home, in the clinic, and through virtual health.'
image: https://cdn.prod.website-files.com/6514a9a971576f72d272d996/6514ad5aa20ba62ec4a8bf8b_61279c03c148106e7fe5f4d9_social%20sharing%20card.jpg
layout: provider
modified: '2026-10-28'
name: Easyhealth
nav: Providers
network: true
overview: 'Easyhealth is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Health, Healthcare, API, SaaS, and Insurance.


  Easyhealth''s developer surface includes signup flow and 7 more developer resources.'
plans:
- name: Joineasyhealth Com Plans Pricing
  plan_count: 0
  slug: joineasyhealth-com-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Joineasyhealth Com Rate Limits
  slug: joineasyhealth-com-rate-limits
scopes:
- name: Joineasyhealth Com Scopes
  scope_count: 0
  slug: joineasyhealth-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 14.5
  coverage:
    artifact_dirs: 20
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 58.9
    operational_transparency: 0.0
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 24.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Joineasyhealth Com Authentication
  slug: joineasyhealth-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Joineasyhealth Com Domain Security
  slug: joineasyhealth-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: joineasyhealth-com
tags:
- Health
- Healthcare
- API
- SaaS
- Insurance
website: https://www.joineasyhealth.com/
---
