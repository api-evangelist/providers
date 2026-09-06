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
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.35pharma.com/
- group: operate
  title: ''
  type: PressReleases
  url: https://www.35pharma.com/news
- group: company
  title: ''
  type: Careers
  url: https://www.35pharma.com/careers
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cdn.prod.website-files.com/679106f289641fbcc75092be/690117401d052d425a9a6c62_35Pharma_PrivacyPolicy_EN_FR.pdf
- group: other
  title: ''
  type: ParentCompany
  url: https://www.gsk.com
- group: auth
  title: ''
  type: DomainSecurity
  url: security/35pharma-domain-security.yml
coverage:
  checked: '2026-09-05'
  detail: 35Pharma is a clinical-stage biopharmaceutical company developing Activin x GDF ligand-trap biologics (lead asset HS235); its entire public site is seven marketing pages — technology, pipeline, about, careers, news, publications — with no developer section, no API, and no machine-readable artifact on any probed path.
  evidence:
  - status: 200
    url: https://www.35pharma.com/sitemap.xml
  - status: 404
    url: https://www.35pharma.com/openapi.json
  - status: 404
    url: https://www.35pharma.com/llms.txt
  - status: 404
    url: https://www.35pharma.com/.well-known/agent-card.json
  - status: 404
    url: https://www.35pharma.com/apis.json
  reason: not-a-software-company
  state: none
created: '2026-09-05'
description: 35Pharma is a Canada-based, private, clinical-stage biopharmaceutical company headquartered in Montreal, Quebec, with a research hub in Boston, Massachusetts. It designs and develops next-generation protein-based therapeutics — multi-specific Activin x GDF ligand traps engineered against the TGF-beta superfamily — for pulmonary hypertension, heart failure, cardiometabolic disease and obesity. Its lead program, HS235, is a precision-engineered activin signalling inhibitor that has completed Phase I healthy-volunteer studies and is entering proof-of-principle trials in PAH and PH-HFpEF; a second program, HS370, targets heart failure and obesity. 35Pharma publishes no developer program, API, or machine-readable API artifacts of any kind — it is a therapeutics developer, not a software or data provider. On 25 February 2026 the company announced an agreement to be acquired by GSK plc.
image: https://cdn.prod.website-files.com/679106f289641fbcc75092be/6920bf64870d13ff322aff0b_Open%20graph%20logo.jpg
layout: provider
modified: '2026-09-05'
name: 35Pharma
nav: Providers
network: true
overview: 35Pharma is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Biopharmaceutical, and Drug Development.
random_paper: 2
score:
  band: minimal
  composite: 6.2
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: domain-security
  name: 35Pharma Domain Security
  slug: 35pharma-domain-security
  summary_line: TLSv1.3 · DMARC
slug: 35pharma
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Biopharmaceutical
- Drug Development
- Clinical Trials
- Life Sciences
- Protein Engineering
- Healthcare
website: https://www.35pharma.com/
---
