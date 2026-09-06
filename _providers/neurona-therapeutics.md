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
- group: auth
  title: ''
  type: DomainSecurity
  url: security/neurona-therapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.neuronatherapeutics.com/
- group: company
  title: ''
  type: About
  url: https://www.neuronatherapeutics.com/about/
- group: other
  title: ''
  type: Technology
  url: https://www.neuronatherapeutics.com/technology/
- group: other
  title: ''
  type: Pipeline
  url: https://www.neuronatherapeutics.com/pipeline/
- group: company
  title: ''
  type: News
  url: https://www.neuronatherapeutics.com/news/press-releases/
- group: company
  title: ''
  type: Careers
  url: https://www.neuronatherapeutics.com/careers/
- group: operate
  title: ''
  type: Contact
  url: https://www.neuronatherapeutics.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.neuronatherapeutics.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.neuronatherapeutics.com/privacy-policy/
- group: other
  title: ''
  type: ParentCompany
  url: https://www.ucb.com
- group: other
  title: ''
  type: ParentCompanyProfile
  url: https://github.com/api-evangelist/ucb
- group: other
  title: ''
  type: AcquisitionAnnouncement
  url: https://www.ucb.com/newsroom/press-releases/article/ucb-completes-acquisition-of-neurona-therapeutics-advancing-its-leadership-as-innovator-in-epilepsy-through-regenerative-science
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://forgeglobal.com/neurona-therapeutics_stock/
- group: commercial
  title: ''
  type: Plans
  url: plans/neurona-therapeutics-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/neurona-therapeutics-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/neurona-therapeutics-llms.txt
coverage:
  checked: '2026-08-26'
  detail: Neurona Therapeutics is a clinical-stage cell-therapy biotech whose product is an injected neural cell therapy (NRTX-1001); its corporate site has no developer, API, or data section at all and every contract-discovery path probed on www.neuronatherapeutics.com returned a hard 404.
  evidence:
  - status: 404
    url: https://www.neuronatherapeutics.com/openapi.json
  - status: 404
    url: https://www.neuronatherapeutics.com/.well-known/agent-card.json
  - status: 404
    url: https://www.neuronatherapeutics.com/graphql
  - status: 200
    url: https://www.neuronatherapeutics.com/
  reason: not-a-software-company
  state: none
created: '2026-08-26'
description: Neurona Therapeutics is a clinical-stage biotherapeutics company in South San Francisco, California, developing allogeneic regenerative neural cell therapies that permanently integrate into neural circuits to treat chronic disorders of the nervous system. Founded on nearly two decades of stem cell research from the University of California, San Francisco, its lead candidate NRTX-1001 (rezanecel) is an inhibitory interneuron cell therapy delivered as a single, minimally invasive dose for drug-resistant mesial temporal lobe epilepsy, and is advancing through the NTE001 and NTE002 studies toward the Phase 3 EPIC trial. UCB completed its acquisition of Neurona on June 2, 2026. The company publishes no public API, developer program, SDK, or machine-readable specification; its public surface is corporate and clinical, not developer-facing.
image: https://www.neuronatherapeutics.com/themes/default/images/logo_gray.png
layout: provider
modified: '2026-08-26'
name: Neurona Therapeutics
nav: Providers
network: true
overview: 'Neurona Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Cell Therapy, and Regenerative Medicine.


  Neurona Therapeutics'' developer surface includes product news and 16 more developer resources.'
plans:
- name: Neurona Therapeutics Plans Pricing
  plan_count: 0
  slug: neurona-therapeutics-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Neurona Therapeutics Rate Limits
  slug: neurona-therapeutics-rate-limits
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
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/neurona-therapeutics/refs/heads/main/screenshots/neurona-therapeutics-2026-09-02T150736.png
security:
- kind: domain-security
  name: Neurona Therapeutics Domain Security
  slug: neurona-therapeutics-domain-security
  summary_line: TLSv1.3 · HSTS
slug: neurona-therapeutics
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Cell Therapy
- Regenerative Medicine
- Neurology
- Epilepsy
- Clinical Trials
- Life Sciences
website: https://www.neuronatherapeutics.com/
---
