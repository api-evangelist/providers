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
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bluenote.ai/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bluenote.ai/privacy-policy
- group: other
  href: https://artifacts.apis.io/bluenotehealth-com/hosts/bluenotehealth-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bluenotehealth-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/bluenotehealth-com/vendors/bluenotehealth-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bluenotehealth-com-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.bluenote.ai
- group: company
  title: ''
  type: Newsroom
  url: https://bluenote.ai/news
- group: auth
  href: https://artifacts.apis.io/bluenotehealth-com/security/bluenotehealth-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bluenotehealth-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bluenote.ai/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.bluenotehealth.com/
  reason: no-developer-program
  state: none
created: '2026-10-25'
description: Bluenote Health provides an AI‑driven platform that accelerates clinical development and regulatory submissions for life‑science companies. Leveraging advanced machine learning, the service streamlines data collection, trial management, and compliance reporting, helping pharma, biotech, and CROs bring therapies to patients faster. The company partners with major industry players and offers a cloud‑based solution with robust security and integration capabilities.
image: https://www.bluenote.ai/og.jpg
layout: provider
modified: '2026-10-25'
name: Bluenote
nav: Providers
network: true
overview: Bluenote is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Life Sciences, Clinical Development, and Regulatory.
random_paper: 8
score:
  band: emerging
  composite: 11.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 14.0
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bluenotehealth Com Domain Security
  slug: bluenotehealth-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: bluenotehealth-com
tags:
- Company
- AI
- Life Sciences
- Clinical Development
- Regulatory
- Healthcare
website: https://bluenote.ai/
---
