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
api_count: 0
artifact_total: 5
common:
- group: other
  href: https://artifacts.apis.io/youmehealthcare-com/hosts/youmehealthcare-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/youmehealthcare-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/youmehealthcare-com/vendors/youmehealthcare-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/youmehealthcare-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hellobackpack.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hellobackpack.com/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://www.carecompanion.hellobackpack.com/auth/login
- group: other
  title: ''
  type: Leadership
  url: https://www.hellobackpack.com/team
- group: company
  title: ''
  type: Blog
  url: https://www.hellobackpack.com/blog
- group: auth
  href: https://artifacts.apis.io/youmehealthcare-com/security/youmehealthcare-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/youmehealthcare-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.hellobackpack.com/
coverage:
  checked: '2026-10-29'
  detail: The provider offers virtual therapy services and does not expose a public API.
  evidence:
  - status: 200
    url: https://www.hellobackpack.com
  reason: not-a-software-company
  state: none
created: '2026-10-29'
description: Backpack Healthcare provides virtual mental health therapy and psychiatry for individuals ages 4 and up, including children, teens, young adults, and adults. The service is offered online in Georgia, Illinois, Maryland, Michigan, and Virginia and is covered by Medicaid and over 100 commercial insurance plans. It matches patients with licensed clinicians who specialize in pediatric and family mental health and offers same‑week appointments and weekend hours.
layout: provider
modified: '2026-10-29'
name: Backpack Healthcare
nav: Providers
network: true
overview: 'Backpack Healthcare is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Virtual Therapy, Pediatric Mental Health, Insurance Covered, Behavioral Health, and Mental Health Services.


  Backpack Healthcare''s developer surface includes engineering blog and 8 more developer resources.'
plans:
- name: Youmehealthcare Com Plans Pricing
  plan_count: 0
  slug: youmehealthcare-com-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Youmehealthcare Com Rate Limits
  slug: youmehealthcare-com-rate-limits
scopes:
- name: Youmehealthcare Com Scopes
  scope_count: 0
  slug: youmehealthcare-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 13.6
  coverage:
    artifact_dirs: 20
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 46.4
    operational_transparency: 0.0
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 27.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Youmehealthcare Com Authentication
  slug: youmehealthcare-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Youmehealthcare Com Domain Security
  slug: youmehealthcare-com-domain-security
  summary_line: TLSv1.3
slug: youmehealthcare-com
tags:
- Virtual Therapy
- Pediatric Mental Health
- Insurance Covered
- Behavioral Health
- Mental Health Services
website: https://www.hellobackpack.com/
---
