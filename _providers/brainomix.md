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
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/brainomix/refs/heads/main/conformance/brainomix-conformance.yml
  title: ''
  type: Conformance
  url: conformance/brainomix-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/brainomix/refs/heads/main/hosts/brainomix-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brainomix-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/brainomix/refs/heads/main/vendors/brainomix-vendors.yml
  title: ''
  type: Vendors
  url: vendors/brainomix-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.brainomix.com/support/trust-center/faq
- group: operate
  title: ''
  type: Support
  url: https://www.brainomix.com/support/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.brainomix.com/privacy-eu
- group: other
  title: ''
  type: Leadership
  url: https://www.brainomix.com/company/team
- group: docs
  title: ''
  type: Documentation
  url: https://www.brainomix.com/docs
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/brainomix/refs/heads/main/security/brainomix-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brainomix-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.brainomix.com
coverage:
  checked: '2026-10-03'
  detail: The provider's documentation at https://www.brainomix.com/docs is HTML only and contains no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL specifications.
  evidence:
  - status: 200
    url: https://www.brainomix.com/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-03'
description: Brainomix is a UK‑based medical‑technology company that develops AI‑powered imaging software for brain and lung diagnostics. Their flagship product, Brainomix 360, provides automated analysis of CT and MRI scans to assist clinicians in stroke detection, treatment planning, and pulmonary disease assessment. The platform integrates with hospital PACS systems, offers quantitative biomarkers, and supports clinical trials with AI‑derived endpoints. Brainomix serves over 100 hospitals worldwide, processing hundreds of thousands of scans annually, and collaborates with pharmaceutical partners on research studies.
image: https://cdn.prod.website-files.com/69e0a08b3efbcfa15c020ad8/6a5e35990010e55ffb8e94a1_1efca530e9dec9a865ab468a126a6f56_Brainomix%20Graph%20Image.jpg
layout: provider
modified: '2026-10-03'
name: Brainomix
nav: Providers
network: true
overview: 'Brainomix is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Medical Imaging, Healthcare, Diagnostics, and Stroke.


  Brainomix''s developer surface includes support, documentation, and 8 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 14.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 18.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 14.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Brainomix Domain Security
  slug: brainomix-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: brainomix
tags:
- Artificial Intelligence
- Medical Imaging
- Healthcare
- Diagnostics
- Stroke
website: https://www.brainomix.com
---
