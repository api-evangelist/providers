---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
  - security
  - '{''url'': ''https://educ-up.fr/'', ''status'': 302, ''note'': ''declared website redirects to http://s880385942.onlinehome.fr/ — a different registrable domain (educ-up.fr -> onlinehome.fr), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://educ-up.fr/
- group: other
  title: ''
  type: Subsidiary
  url: https://domissori.fr/
- group: other
  title: ''
  type: Subsidiary
  url: https://www.edacademy.fr/
- group: other
  title: ''
  type: Product
  url: https://formation.edacademy.fr/
- group: company
  title: ''
  type: Blog
  url: https://domissori.fr/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.edacademy.fr/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.edacademy.fr/conditions-utilisation
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://domissori.fr/politique-de-confidentialite/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/educ-up/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/educ-up-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/educ-up-llms.txt
coverage:
  checked: '2026-08-17'
  detail: The only software Educ-up operates is an end-user Moodle LMS at formation.edacademy.fr for enrolled Edacademy learners — its stock Moodle web-service endpoint answers 200 with errorcode "invalidtoken" but is Moodle's contract, token-gated and undocumented by Educ-up — while the corporate domain educ-up.fr now 302s to an IONOS parked page that returns the same 336-byte body for every path including nonsense ones, and the Domissori (WordPress) and Edacademy (Webflow) marketing sites carry no developer portal, no API reference and no spec at any probed location.
  evidence:
  - status: 200
    url: https://educ-up.fr/
  - status: 200
    url: https://educ-up.fr/.well-known/zzz-control-9f3k
  - status: 404
    url: https://domissori.fr/openapi.json
  - status: 404
    url: https://domissori.fr/.well-known/agent-card.json
  - status: 404
    url: https://www.edacademy.fr/llms.txt
  - status: 404
    url: https://www.edacademy.fr/.well-known/agent-card.json
  - status: 404
    url: https://formation.edacademy.fr/openapi.json
  - status: 200
    url: https://formation.edacademy.fr/webservice/rest/server.php?wsfunction=core_webservice_get_site_info
  - status: 404
    url: https://educ-up.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-08-17'
description: 'Educ-up is a French social-impact education group founded in 2016 by Mohamed El Mazzouji, headquartered in Saint-Denis, La Réunion with establishments in metropolitan France including Montreuil (Seine-Saint-Denis). It operates two consumer- and professional-facing brands rather than a software product: Domissori, launched in 2019, which places Montessori-trained educators in family homes for childcare, educational workshops and academic tutoring across Vannes, Chambéry, Lyon, Grenoble, Perpignan, Montpellier, Marseille and Saint-Denis; and Edacademy, a Qualiopi-certified training and apprenticeship centre for early-childhood and personal-care professions (CAP AEPE, Titre Pro ADVF, Bac Pro ASSP, parenting and Montessori support). The group also runs Ed''solidaire, a subsidy scheme that opens paid childcare to low-income families. Investors include Serena, M Capital, Inco Ventures, MakeSense and Racine2. Edacademy delivers its programmes through a self-hosted Moodle learning
  platform at formation.edacademy.fr, but that is an end-user LMS: as of August 2026 Educ-up publishes no developer portal, no API documentation and no machine-readable API contract, and its corporate domain educ-up.fr now redirects to a parked IONOS default site.'
layout: provider
modified: '2026-08-17'
name: Educ-up
nav: Providers
network: true
overview: 'Educ-up is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, EdTech, Education, Childcare, and Training.


  Educ-up''s developer surface includes engineering blog, support, and 9 more developer resources.'
plans:
- name: Educ Up Plans Pricing
  plan_count: 0
  slug: educ-up-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Educ Up Rate Limits
  slug: educ-up-rate-limits
score:
  band: minimal
  composite: 10.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 53.7
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 10.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 25.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/educ-up/refs/heads/main/screenshots/educ-up-2026-09-02T145329.png
security:
- kind: domain-security
  name: Educ Up Domain Security
  slug: educ-up-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: educ-up
tags:
- Company
- EdTech
- Education
- Childcare
- Training
- Montessori
- Vocational Training
- France
- Social Impact
website: https://educ-up.fr/
---
