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
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zurex-pharma-domain-security.yml
coverage:
  checked: '2026-09-05'
  detail: 'Zurex Pharma sells regulated physical antiseptics (ZuraPrep, ZuraGard, ZurAsept, ZuraLac), not software, and it has no readable web surface either: its own domain zurexpharma.com is pointed at Wix with no site connected, so the origin answers the "ConnectYourDomain Error | Wix.com" HTML page with HTTP 404 for every path including the root, /openapi.json, /llms.txt and every /.well-known/ path, while its LinkedIn company page at /company/zurex-pharma also 404s.'
  evidence:
  - status: 404
    url: https://www.zurexpharma.com/
  - status: 404
    url: https://www.zurexpharma.com/openapi.json
  - status: 404
    url: https://www.zurexpharma.com/llms.txt
  - status: 404
    url: https://zurexpharma.com/.well-known/agent-card.json
  - status: 404
    url: https://www.linkedin.com/company/zurex-pharma
  reason: not-a-software-company
  state: none
created: '2026-09-05'
description: 'Zurex Pharma, Inc. is a privately held specialty pharmaceutical and medical technology company founded in 2008 and headquartered in Middleton, Wisconsin, developing a portfolio of patented antimicrobial formulations intended to prevent healthcare-acquired infections. Its products are physical, regulated goods rather than software: ZuraPrep, a single-use pre-surgical skin antiseptic submitted to the FDA as NDA 210872 in June 2018; ZuraGard for peri-operative and catheter exit-site antisepsis; ZurAsept, a catheter lock solution; and ZuraLac, a teat sanitizer for dairy cattle. Backed by Baird Venture Partners, the State of Wisconsin Investment Board, Peak Ridge Capital and Wisconsin Investment Partners. The company publishes no developer program, no API and no machine-readable API artifacts of any kind, and as of this pass its own domain serves no website.'
layout: provider
modified: '2026-09-05'
name: Zurex Pharma
nav: Providers
network: true
overview: Zurex Pharma is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Pharmaceuticals, Medical Devices, Healthcare, and Antimicrobials.
random_paper: 13
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
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: domain-security
  name: Zurex Pharma Domain Security
  slug: zurex-pharma-domain-security
  summary_line: TLSv1.3 · DMARC
slug: zurex-pharma
tags:
- Company
- Pharmaceuticals
- Medical Devices
- Healthcare
- Antimicrobials
- Infection Prevention
- Life Sciences
- Wisconsin
---
