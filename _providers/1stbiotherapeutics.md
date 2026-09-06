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
  url: security/1stbiotherapeutics-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/1stbiotherapeutics-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.1stbio.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.1stbio.com/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://www.1stbio.com/contact-us/
coverage:
  checked: '2026-09-05'
  detail: 1ST Biotherapeutics is a clinical-stage drug-discovery company whose entire public web presence is an eight-page WordPress marketing and investor site; no api./developer./docs./ dev./portal. subdomain of 1stbio.com resolves in DNS, every /.well-known/ discovery path 404s, and the only machine-readable endpoint on the domain is the stock WordPress REST API discovery document at /wp-json (namespaces wp/v2, oembed/1.0, yoast/v1, gravityforms/v2) — default CMS infrastructure, not a product API the company designed or supports.
  evidence:
  - status: 200
    url: https://www.1stbio.com/
  - status: 404
    url: https://www.1stbio.com/openapi.json
  - status: 404
    url: https://www.1stbio.com/.well-known/agent-card.json
  - status: 404
    url: https://www.1stbio.com/llms.txt
  - status: 200
    url: https://www.1stbio.com/wp-json
  reason: not-a-software-company
  state: none
created: '2026-09-05'
description: '1ST Biotherapeutics (1STBIO) is a clinical-stage biopharmaceutical company founded in 2016 and headquartered in Gyeonggi-do, South Korea. It discovers and develops novel small-molecule therapeutics for areas of significant unmet medical need, with programs spanning neurodegenerative disease, immuno-oncology, metabolic disease and rare/orphan disease, supported by a genomics-based target discovery capability and an R&D network of academic, hospital, CRO and investor partners. The company sells no software product and operates no developer program: its public web presence is an eight-page corporate and investor site with no API, SDK, developer portal or machine-readable contract of any kind.'
image: https://www.1stbio.com/android-chrome-192x192.png
layout: provider
modified: '2026-09-05'
name: 1ST Biotherapeutics
nav: Providers
network: true
overview: '1ST Biotherapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Drug Discovery, and Life Sciences.


  1ST Biotherapeutics'' developer surface includes support and 4 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 7.9
  coverage:
    artifact_dirs: 3
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
    developer_ergonomics: 4.8
    discoverability: 57.4
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
  name: 1Stbiotherapeutics Domain Security
  slug: 1stbiotherapeutics-domain-security
  summary_line: TLSv1.3
slug: 1stbiotherapeutics
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Drug Discovery
- Life Sciences
- Healthcare
- Oncology
- Neurodegenerative Disease
- Rare Disease
- South Korea
website: https://www.1stbio.com/
---
