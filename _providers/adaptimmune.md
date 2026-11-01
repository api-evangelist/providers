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
  href: https://artifacts.apis.io/adaptimmune/hosts/adaptimmune-hosts.yml
  title: ''
  type: Hosts
  url: hosts/adaptimmune-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.adaptimmune.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.adaptimmune.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.adaptimmune.com/investors-and-media/news-center/media
- group: auth
  href: https://artifacts.apis.io/adaptimmune/security/adaptimmune-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adaptimmune-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.adaptimmune.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.adaptimmune.com/
  reason: no-developer-program
  state: none
created: '2026-10-25'
description: Adaptimmune is a clinical-stage biopharmaceutical company focused on the development of novel cancer immunotherapy products for cancer patients. The company leverages its proprietary TCR platform to engineer T cells that can recognize and target a broad range of tumor antigens, aiming to provide transformative treatments across multiple cancer indications. Adaptimmune collaborates with academic, biotech, and pharmaceutical partners to advance its pipeline through preclinical and clinical development, emphasizing safety, efficacy, and innovative manufacturing processes.
image: https://d1io3yog0oux5.cloudfront.net/_a238800713053d6455e191465ff24faf/adaptimmune/db/223/1247/social_image_resized.jpg
layout: provider
modified: '2026-10-25'
name: Adaptimmune
nav: Providers
network: true
overview: Adaptimmune is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biopharma, Immunotherapy, TCR, and Oncology.
random_paper: 21
score:
  band: minimal
  composite: 9.0
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
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Adaptimmune Domain Security
  slug: adaptimmune-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: adaptimmune
tags:
- Company
- Biopharma
- Immunotherapy
- TCR
- Oncology
website: https://www.adaptimmune.com/
---
