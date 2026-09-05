---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/myra-vision-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.myravision.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.myravision.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/myra-vision
coverage:
  checked: '2026-08-04'
  detail: Myra Vision is a 25-person clinical-stage medical device maker whose product is the Calibreye titratable glaucoma shunt — a nitinol implant adjusted in-office by laser, not software; its entire web presence is a five-page WordPress marketing site (home, sign-up, privacy policy, titratable-outflow, 404) with no developer, docs, or api subdomain resolving in DNS, no GitHub organization, and no package on npm/PyPI, and the origin additionally answers every path with a SiteGround captcha challenge (HTTP 202) so live /.well-known and /openapi.json probes were confirmed against archived crawls instead.
  evidence:
  - status: 202
    url: https://www.myravision.com/
  - status: 202
    url: https://www.myravision.com/openapi.json
  - status: 200
    url: https://web.archive.org/web/20250305100237id_/https://www.myravision.com/page-sitemap.xml
  - status: 404
    url: https://web.archive.org/web/20250306013206/https://www.myravision.com/.well-known/security.txt
  - status: 404
    url: https://api.github.com/orgs/myravision
  reason: not-a-software-company
  state: none
created: '2026-08-04'
description: 'Myra Vision, Inc. is a clinical-stage ophthalmic medical device company headquartered in Campbell, California, and a privately held portfolio company of the Shifamed LLC medical device incubator. It develops the Calibreye Titratable Glaucoma Therapy (TGT) Surgical System, an aqueous shunt for patients with moderate to severe glaucoma whose valve-controlled outflow channels use shape-memory nitinol and can be reversibly opened or closed in-office with a transcorneal laser, letting a clinician titrate intraocular pressure after implantation rather than committing to a fixed flow at the time of surgery. The company completed first-in-human use of the Calibreye System in 2023, received FDA conditional approval of its Investigational Device Exemption in August 2025, and enrolled the first patient in its US ADAPT clinical study in January 2026. As a medical device manufacturer its product is a physical implant and a surgical procedure, not software: Myra Vision publishes no public
  developer API, SDK, developer portal, or machine-readable API specification, and this profile captures its corporate identity and public web properties in the API Evangelist network.'
layout: provider
modified: '2026-08-04'
name: Myra Vision
nav: Providers
network: true
overview: Myra Vision is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Healthcare, Ophthalmology, and Glaucoma.
random_paper: 16
score:
  band: minimal
  composite: 2.9
  coverage:
    artifact_dirs: 2
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 2.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/myra-vision/refs/heads/main/screenshots/myra-vision-2026-08-07T184533.png
security:
- kind: domain-security
  name: Myra Vision Domain Security
  slug: myra-vision-domain-security
  summary_line: TLSv1.3 · DMARC
slug: myra-vision
tags:
- Company
- Medical Devices
- Healthcare
- Ophthalmology
- Glaucoma
- Life Sciences
- Medical Technology
- Clinical Stage
website: https://www.myravision.com/
---
