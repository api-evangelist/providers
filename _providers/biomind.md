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
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/biomind/refs/heads/main/plans/biomind-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/biomind-plans-pricing.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/biomind/refs/heads/main/hosts/biomind-hosts.yml
  title: ''
  type: Hosts
  url: hosts/biomind-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.biomindhealth.com/terms.html
- group: start
  title: ''
  type: SignUp
  url: https://www.biomindhealth.com/auth/signup.php
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.biomindhealth.com/privacy.html
- group: commercial
  title: ''
  type: Pricing
  url: https://www.biomindhealth.com/pricing.html
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/biomind/refs/heads/main/security/biomind-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/biomind-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.biomindhealth.com/
coverage:
  checked: '2026-09-28'
  detail: The BioMind website provides no developer program or API documentation.
  evidence:
  - status: 200
    url: https://www.biomindhealth.com/
  reason: no-developer-program
  state: none
created: '2026-09-28'
description: BioMind Health is an award‑winning artificial intelligence company delivering a Biological Operating System that merges AI, ancient wisdom, and biotechnology to provide educational health intelligence. The platform offers modules on nutrition, emotion, and biology, serving hospitals, clinicians, and individuals worldwide, aiming to make biological literacy accessible and empower personalized health insights.
layout: provider
modified: '2026-09-28'
name: BioMind
nav: Providers
network: true
overview: 'BioMind is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Health, Biotechnology, and Education.


  BioMind''s developer surface includes signup flow, pricing, and 6 more developer resources.'
plans:
- name: Biomind Plans Pricing
  plan_count: 3
  slug: biomind-plans-pricing
random_paper: 12
score:
  band: emerging
  composite: 19.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 37.0
    catalog_earned_first_party: 12.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.3
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Biomind Domain Security
  slug: biomind-domain-security
  summary_line: TLSv1.3 · DMARC
slug: biomind
tags:
- Company
- Artificial Intelligence
- Health
- Biotechnology
- Education
- Platform
website: https://www.biomindhealth.com/
---
