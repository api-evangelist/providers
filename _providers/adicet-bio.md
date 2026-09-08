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
  scored_at: '2026-09-07'
api_count: 0
artifact_total: 1
common:
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/adicet-bio-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adicet-bio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.adicetbio.com/
- group: company
  title: ''
  type: About
  url: https://www.adicetbio.com/about/
- group: operate
  title: ''
  type: Support
  url: https://www.adicetbio.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.adicetbio.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.adicetbio.com/privacy/
- group: company
  title: ''
  type: Careers
  url: https://www.adicetbio.com/careers/openings/
coverage:
  checked: '2026-09-07'
  detail: Adicet Bio is a clinical-stage cell-therapy biotech — its products are investigational gamma delta CAR T cell therapies, not software — and its entire public surface is a nine-page corporate marketing site plus a vendor-hosted investor relations portal; every OpenAPI, Swagger, GraphQL, MCP, agent-card and /.well-known/ path probed on adicetbio.com, www.adicetbio.com and investor.adicetbio.com returned 404, 301 or 403, and the site contains no developer, API, docs or integrations link anywhere in its navigation.
  evidence:
  - status: 404
    url: https://www.adicetbio.com/openapi.json
  - status: 404
    url: https://www.adicetbio.com/.well-known/agent-card.json
  - status: 404
    url: https://www.adicetbio.com/llms.txt
  - status: 404
    url: https://www.adicetbio.com/graphql
  - status: 200
    url: https://www.adicetbio.com/
  reason: not-a-software-company
  state: none
created: '2026-09-07'
description: 'Adicet Bio, Inc. (Nasdaq: ACET) is a clinical-stage biotechnology company with offices in Redwood City, California and Boston, Massachusetts, discovering and developing allogeneic "off-the-shelf" gamma delta T cell therapies engineered with chimeric antigen receptors (CARs) for autoimmune disease and cancer. Its lead candidate, prulacabtagene leucel (prula-cel), is an anti-CD20 gamma delta CAR T cell therapy in development for B cell-mediated autoimmune diseases, alongside ADI-212 for metastatic castration-resistant prostate cancer. Adicet publishes a corporate website covering its science platform, clinical pipeline, leadership and careers, plus a vendor-hosted investor relations portal. It operates no public developer program, API, SDK, or machine-readable interface of any kind; this profile records that absence rather than an API surface.'
image: https://www.adicetbio.com/themes/default/images/logo.svg
layout: provider
modified: '2026-09-07'
name: Adicet Bio
nav: Providers
network: true
overview: 'Adicet Bio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Life Sciences, Cell Therapy, and Immunotherapy.


  Adicet Bio''s developer surface includes support and 7 more developer resources.'
random_paper: 11
score:
  band: minimal
  composite: 10.7
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
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
    score: 17.5
  schema_version: 0.20.0
  scored_at: '2026-09-07'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Adicet Bio Domain Security
  slug: adicet-bio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: adicet-bio
tags:
- Company
- Biotechnology
- Life Sciences
- Cell Therapy
- Immunotherapy
- Oncology
- Autoimmune
- Clinical Trials
- Pharmaceuticals
website: https://www.adicetbio.com/
---
