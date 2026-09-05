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
- group: company
  title: ''
  type: Website
  url: https://syntis.bio/
- group: company
  title: ''
  type: About
  url: https://syntis.bio/about/
- group: company
  title: ''
  type: Blog
  url: https://syntis.bio/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://syntis.bio/feed/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://syntis.bio/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://syntis.bio/terms-of-use/
- group: company
  title: ''
  type: Careers
  url: https://syntis.bio/careers/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/syntis-bio/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/syntisbio
- group: auth
  title: ''
  type: DomainSecurity
  url: security/syntis-bio-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/syntis-bio-llms.txt
coverage:
  checked: '2026-08-29'
  detail: Syntis Bio is a clinical-stage biopharmaceutical company whose product is an oral drug-delivery polymer (SYNT / SYNT-101), not software; syntis.bio is a single WordPress marketing site with no api./developer./docs. subdomain resolving, no GitHub organization, and a 404 on every OpenAPI, GraphQL and /.well-known/ path probed.
  evidence:
  - status: 404
    url: https://syntis.bio/openapi.json
  - status: 404
    url: https://syntis.bio/.well-known/api-catalog
  - status: 404
    url: https://syntis.bio/.well-known/agent-card.json
  - status: 404
    url: https://syntis.bio/graphql
  - status: 200
    url: https://syntis.bio/
  reason: not-a-software-company
  state: none
created: '2026-08-29'
description: Syntis Bio is a clinical-stage biopharmaceutical company in Boston, Massachusetts developing oral therapies that use the small intestine as a delivery site. Its SYNT platform (Synthetic Tissue-lining) applies a mussel-inspired polydopamine polymer coating transiently to specific tissues in the GI tract, sustaining therapeutic activity for up to 24 hours before being naturally cleared. The platform is being applied to nutrient exclusion for obesity, gut-restricted enzyme replacement for rare metabolic disorders such as homocystinuria and maple syrup urine disease, and oral bioavailability enhancement for peptides and biologics. Lead candidate SYNT-101 is a once-daily oral pill intended to mimic aspects of gastric bypass by transiently blocking nutrient absorption in the duodenum. The company was co-founded in 2022 by MIT's Robert Langer and Giovanni Traverso with CEO Rahul Dhanda. Syntis Bio is a therapeutics developer and publishes no public API, developer program, SDK, or machine-readable
  specification.
image: https://syntis.bio/wp-content/uploads/2024/06/logo-header.svg
layout: provider
modified: '2026-08-29'
name: Syntis Bio
nav: Providers
network: true
overview: 'Syntis Bio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Life Sciences, and Drug Delivery.


  Syntis Bio''s developer surface includes engineering blog and 10 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 10.3
  coverage:
    artifact_dirs: 5
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
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/syntis-bio/refs/heads/main/screenshots/syntis-bio-2026-09-02T161638.png
security:
- kind: domain-security
  name: Syntis Bio Domain Security
  slug: syntis-bio-domain-security
  summary_line: TLSv1.3
slug: syntis-bio
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Life Sciences
- Drug Delivery
- Clinical Stage
- Obesity
- Rare Disease
- Health
website: https://syntis.bio/
---
