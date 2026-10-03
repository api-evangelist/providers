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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: Arrive Health provides healthcare navigation and payment solutions.
  name: Arrive Health API
  slug: arrive-health-api
artifact_total: 3
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/arrive-health/refs/heads/main/well-known/arrive-health-clarity-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/arrive-health-clarity-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/arrive-health/refs/heads/main/well-known/arrive-health-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/arrive-health-well-known.yml
- group: auth
  title: ''
  type: Security
  url: https://clarity.com/vdp
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/arrive-health/refs/heads/main/hosts/arrive-health-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arrive-health-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/arrive-health/refs/heads/main/vendors/arrive-health-vendors.yml
  title: ''
  type: Vendors
  url: vendors/arrive-health-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://arrivehealth.com/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://arrivehealth.com/price-transparency-patients-providers-need/
- group: company
  title: ''
  type: Newsroom
  url: https://arrivehealth.com/press/global-excellence-awards-2025/
- group: other
  title: ''
  type: Leadership
  url: https://arrivehealth.com/about/leadership/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/arrive-health/refs/heads/main/security/arrive-health-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/arrive-health-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/arrive-health/refs/heads/main/security/arrive-health-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arrive-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arrivehealth.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.hiive.com/securities/arrive-health-stock
  reason: no-developer-program
  state: none
created: '2026-09-26'
description: Arrive Health works to improve health care decisions for patients and providers by increasing affordability, access, and outcomes while reducing administrative burden. The company, now part of Interra Health, partners with health systems, providers, health plans, PBMs, EHRs, and technology vendors to deliver solutions for providers, care teams, and patients. Their platform offers tools for care navigation, cost transparency, and patient engagement, aiming to clear barriers to care and support better health outcomes across the United States.
image: https://arrivehealth.com/wp-content/uploads/2022/06/Arrive_AllPurpose_1600x900.png
layout: provider
modified: '2026-09-26'
name: Arrive Health
nav: Providers
network: true
overview: 'Arrive Health publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Patient Engagement, Health Tech, and InterraHealth.


  Arrive Health''s developer surface includes pricing and 11 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 11.7
  coverage:
    artifact_dirs: 5
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
    discoverability: 60.7
    operational_transparency: 10.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Arrive Health Domain Security
  slug: arrive-health-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Arrive Health Vulnerability Disclosure
  slug: arrive-health-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: arrive-health
tags:
- Company
- Healthcare
- Patient Engagement
- Health Tech
- InterraHealth
website: https://arrivehealth.com
---
