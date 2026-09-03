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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/levee-medical-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://leveemedical.com/
- group: company
  title: ''
  type: Blog
  url: https://leveemedical.com/feed/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://leveemedical.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://leveemedical.com/terms/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/levee-medical-llms.txt
coverage:
  checked: '2026-08-25'
  detail: Levee Medical manufactures a single investigational bioabsorbable implant (the Voro Urologic Scaffold) and its entire web presence is a five-page WordPress marketing and clinical-trial site — there is no developer subdomain (api./developer./docs./status.leveemedical.com are all NXDOMAIN) and the only machine-readable endpoint on the domain is the default WordPress core REST API at /wp-json/, which is CMS scaffolding rather than a product API.
  evidence:
  - status: 404
    url: https://leveemedical.com/openapi.json
  - status: 404
    url: https://leveemedical.com/.well-known/agent-card.json
  - status: 404
    url: https://leveemedical.com/llms.txt
  - status: 200
    url: https://leveemedical.com/wp-json/
  reason: not-a-software-company
  state: none
created: '2026-08-25'
description: 'Levee Medical, Inc. is a privately held, clinical-stage medical device company headquartered in Durham, North Carolina, developing the Voro Urologic Scaffold — a bioabsorbable implant designed to support and stabilize the bladder neck and urethra following radical prostatectomy, in order to accelerate the return of continence and reduce the risk of chronic post-prostatectomy urinary incontinence. The device is investigational, is not approved for commercial sale, and is being evaluated in the FDA-approved ARID II IDE multicenter randomized pivotal trial. The company was founded in 2018 and has raised Series A and Series B financing. Levee Medical is a physical medical device manufacturer: it publishes no public API, developer portal, SDK, or machine-readable specification, and its only web surface is a WordPress marketing and clinical-trial site.'
image: https://leveemedical.com/wp-content/uploads/2024/09/open-graph-image.png
layout: provider
modified: '2026-08-25'
name: Levee Medical
nav: Providers
network: true
overview: 'Levee Medical is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Healthcare, MedTech, and Urology.


  Levee Medical''s developer surface includes engineering blog and 5 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 10.3
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/levee-medical/refs/heads/main/screenshots/levee-medical-2026-09-02T150243.png
security:
- kind: domain-security
  name: Levee Medical Domain Security
  slug: levee-medical-domain-security
  summary_line: TLSv1.3
slug: levee-medical
tags:
- Company
- Medical Devices
- Healthcare
- MedTech
- Urology
- Prostate Cancer
- Clinical Trials
- Implantable Devices
website: https://leveemedical.com/
---
