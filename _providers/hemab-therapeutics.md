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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hemab-therapeutics-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hemab-therapeutics-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.hemab.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hemab.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hemab.com/terms-conditions
- group: operate
  title: ''
  type: Support
  url: https://www.hemab.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.hemab.com/news-media-hub
- group: company
  title: ''
  type: About
  url: https://www.hemab.com/about-us
- group: company
  title: ''
  type: InvestorRelations
  url: https://ir.hemab.com
- group: company
  title: ''
  type: Careers
  url: https://career.hitalento.com/hemab/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hemabaps/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/hemab_tx
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://forgeglobal.com/hemab-therapeutics_stock/
coverage:
  checked: '2026-08-22'
  detail: Hemab Therapeutics is a clinical-stage antibody biopharma whose only web properties are a Webflow marketing site and a third-party investor-relations host; www.hemab.com returns 404 for every OpenAPI, GraphQL and /.well-known/ path probed, and api./developer./docs.hemab.com do not resolve in DNS, so there is no API surface to profile.
  evidence:
  - status: 404
    url: https://www.hemab.com/openapi.json
  - status: 404
    url: https://www.hemab.com/.well-known/api-catalog
  - status: 404
    url: https://www.hemab.com/.well-known/agent-card.json
  - status: 404
    url: https://www.hemab.com/llms.txt
  - status: 200
    url: https://www.hemab.com/
  reason: not-a-software-company
  state: none
created: '2026-08-22'
description: 'Hemab Therapeutics is a clinical-stage biopharmaceutical company headquartered in Copenhagen, Denmark with a US presence in Cambridge, Massachusetts, developing prophylactic antibody-based therapeutics for serious, underserved bleeding and thrombotic disorders. Its modality-agnostic approach uses monoclonal and bispecific antibodies to stabilize coagulation proteins, prevent their premature breakdown, and direct them to sites of injury. The clinical pipeline targets Glanzmann Thrombasthenia (sutacimig, HMB-001), von Willebrand Disease (HMB-002), Factor VII deficiency and heavy menstrual bleeding. Hemab publishes a corporate marketing site, an investor relations site, and audience-specific sections for patients, caregivers and healthcare providers. It operates no public developer program: there is no developer portal, API reference, machine-readable specification, SDK, or webhook surface on any host it controls.'
image: https://cdn.prod.website-files.com/683e244b9c2c9828c10be2ed/68505c0989a11b7e82490360_Webclip.png
layout: provider
modified: '2026-08-22'
name: Hemab Therapeutics
nav: Providers
network: true
overview: 'Hemab Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Life Sciences, and Clinical Trials.


  Hemab Therapeutics'' developer surface includes support, engineering blog, and 11 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 10.5
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
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hemab-therapeutics/refs/heads/main/screenshots/hemab-therapeutics-2026-09-02T145721.png
security:
- kind: domain-security
  name: Hemab Therapeutics Domain Security
  slug: hemab-therapeutics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hemab-therapeutics
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Life Sciences
- Clinical Trials
- Healthcare
- Rare Disease
- Hematology
- Denmark
website: https://www.hemab.com/
---
