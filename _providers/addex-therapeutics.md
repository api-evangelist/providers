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
- group: other
  href: https://artifacts.apis.io/addex-therapeutics/hosts/addex-therapeutics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/addex-therapeutics-hosts.yml
- group: start
  title: ''
  type: SignUp
  url: https://www.addextherapeutics.com/en/investors/register-email-news/
- group: company
  title: ''
  type: Newsroom
  url: https://www.addextherapeutics.com/en/media/
- group: auth
  href: https://artifacts.apis.io/addex-therapeutics/security/addex-therapeutics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/addex-therapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.addextherapeutics.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.addextherapeutics.com/en/about-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.addextherapeutics.com/en/about-us/privacy-policy/
- group: company
  title: ''
  type: Careers
  url: https://www.addextherapeutics.com/en/about-us/careers/
coverage:
  checked: '2026-10-26'
  detail: No machine‑readable API contract (OpenAPI/GraphQL/etc.) was found on the provider's documentation site.
  evidence:
  - status: 200
    url: https://www.addextherapeutics.com/en/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-25'
description: Addex Therapeutics is a clinical‑stage biotechnology company focused on developing novel orally available small‑molecule allosteric modulators for neurological and neuropsychiatric disorders. The firm advances a pipeline of candidates targeting conditions such as Parkinson’s disease, schizophrenia, and substance use disorders, leveraging its proprietary allosteric modulation platform to address unmet medical needs.
image: https://www.addextherapeutics.com/themes/application/assets/media/images/fixme_facebook_post_image.jpg
layout: provider
modified: '2026-10-25'
name: Addex Therapeutics
nav: Providers
network: true
overview: 'Addex Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Neurology, and Allosteric-Modulators.


  Addex Therapeutics'' developer surface includes signup flow, documentation, and 6 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 11.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Addex Therapeutics Domain Security
  slug: addex-therapeutics-domain-security
  summary_line: TLSv1.3 · HSTS
slug: addex-therapeutics
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Neurology
- Allosteric-Modulators
- Clinical-Stage
website: https://www.addextherapeutics.com
---
