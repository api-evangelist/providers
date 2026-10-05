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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/brainscopecompany/refs/heads/main/hosts/brainscopecompany-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brainscopecompany-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/brainscopecompany/refs/heads/main/vendors/brainscopecompany-vendors.yml
  title: ''
  type: Vendors
  url: vendors/brainscopecompany-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/brainscopecompany/refs/heads/main/security/brainscopecompany-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brainscopecompany-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.brainscope.com
- group: company
  title: ''
  type: Blog
  url: https://www.brainscope.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.brainscope.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.brainscope.com/termsofuse
- group: operate
  title: ''
  type: Contact
  url: https://www.brainscope.com/new/contactus
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://www.brainscope.com/mcp
  - status: 403
    url: https://info.brainscope.com/mcp
  - status: 403
    url: https://equityzen.com/company/brainscopecompany
  reason: no-developer-program
  state: none
created: '2026-10-03'
description: BrainScope is a leading neurotechnology company with over 15 years of experience advancing brain health by transforming EEG data into objective diagnostic insights. It offers FDA‑cleared AI‑driven platforms for rapid, radiation‑free assessment of head injuries, and is developing novel biomarkers for broader clinical use.
image: https://www.brainscope.com/hubfs/Screenshot%202023-03-09%20at%2010.24.36%20AM.png
layout: provider
modified: '2026-10-03'
name: Brainscopecompany
nav: Providers
network: true
overview: 'Brainscopecompany is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Neurotechnology, Artificial Intelligence, EEG, Medical Devices, and Healthcare.


  Brainscopecompany''s developer surface includes engineering blog and 7 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 9.2
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
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.3
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Brainscopecompany Domain Security
  slug: brainscopecompany-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: brainscopecompany
tags:
- Neurotechnology
- Artificial Intelligence
- EEG
- Medical Devices
- Healthcare
website: https://www.brainscope.com
---
