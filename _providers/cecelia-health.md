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
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cecelia-health/refs/heads/main/hosts/cecelia-health-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cecelia-health-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ceceliahealth.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ceceliahealth.com/privacy-policy/
- group: company
  title: ''
  type: Blog
  url: https://www.ceceliahealth.com/blog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cecelia-health/refs/heads/main/security/cecelia-health-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cecelia-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ceceliahealth.com/
coverage:
  checked: '2026-10-07'
  detail: No machine‑readable API contract (OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL) was found on the provider's hosts.
  evidence:
  - status: 200
    url: https://www.ceceliahealth.com/contact-us/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-07'
description: Cecelia Health provides virtual, human-centered care solutions focused on integrated cardiometabolic management, GLP‑1 clinical support, and lifestyle‑driven weight management for employers. Their platform offers patient support services for pharma partners and delivers insights for individuals, combining technology with personalized care to improve health outcomes across populations.
layout: provider
modified: '2026-10-07'
name: Cecelia Health
nav: Providers
network: true
overview: 'Cecelia Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Virtual Care, Cardiometabolic Care, GLP‑1 Support, Employer Solutions, and Pharma Patient Support.


  Cecelia Health''s developer surface includes engineering blog and 5 more developer resources.'
random_paper: 21
score:
  band: minimal
  composite: 9.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cecelia Health Domain Security
  slug: cecelia-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cecelia-health
tags:
- Virtual Care
- Cardiometabolic Care
- GLP‑1 Support
- Employer Solutions
- Pharma Patient Support
website: https://www.ceceliahealth.com/
---
