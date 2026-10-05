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
  href: https://raw.githubusercontent.com/api-evangelist/beijingaccbbiotechltd/refs/heads/main/hosts/beijingaccbbiotechltd-hosts.yml
  title: ''
  type: Hosts
  url: hosts/beijingaccbbiotechltd-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/beijingaccbbiotechltd/refs/heads/main/vendors/beijingaccbbiotechltd-vendors.yml
  title: ''
  type: Vendors
  url: vendors/beijingaccbbiotechltd-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://accbiotech.com/tc/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://accbiotech.com/tc/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://accbiotech.com/tc/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/beijingaccbbiotechltd/refs/heads/main/security/beijingaccbbiotechltd-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/beijingaccbbiotechltd-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://accbiotech.com
coverage:
  checked: '2026-09-27'
  detail: The company website provides no developer documentation or API reference.
  evidence:
  - status: 200
    url: https://accbiotech.com
  reason: no-developer-program
  state: none
created: '2026-09-27'
description: ACC Biotech Limited (北京雅康博生物科技有限公司) is a Hong‑Kong based professional health‑supplement OEM/ODM manufacturer. It offers end‑to‑end services from formulation design, global ingredient sourcing, production, packaging and regulatory compliance, serving clients worldwide. The company also provides patented ingredient development and a range of supplement dosage forms.
image: https://accbiotech.com/site/assets/images/og-image.png
layout: provider
modified: '2026-09-27'
name: Beijingaccbbiotechltd
nav: Providers
network: true
overview: 'Beijingaccbbiotechltd is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Health Supplements, OEM, and ODM.


  Beijingaccbbiotechltd''s developer surface includes engineering blog and 6 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 9.3
  coverage:
    artifact_dirs: 6
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
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.9
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Beijingaccbbiotechltd Domain Security
  slug: beijingaccbbiotechltd-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: beijingaccbbiotechltd
tags:
- Company
- Biotechnology
- Health Supplements
- OEM
- ODM
- Hong Kong
website: https://accbiotech.com
---
