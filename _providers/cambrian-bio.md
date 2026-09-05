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
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cambrian-bio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cambrianbio.com/
- group: company
  title: ''
  type: About
  url: https://www.cambrianbio.com/about
- group: company
  title: ''
  type: Blog
  url: https://www.cambrianbio.com/blogs
- group: company
  title: ''
  type: News
  url: https://www.cambrianbio.com/news-and-publications
- group: operate
  title: ''
  type: Support
  url: https://www.cambrianbio.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cambrianbio.com/privacy-policy
- group: company
  title: ''
  type: Careers
  url: https://www.cambrianbio.com/careers-page
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cambrianbio/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/cambrianbio
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cambrian-bio-llms.txt
coverage:
  checked: '2026-08-09'
  detail: Cambrian Bio is a clinical-stage drug developer whose product is therapeutics, not software; its Webflow corporate site has no developer, API, or docs section and every spec and .well-known probe against www.cambrianbio.com returned the site 404 page.
  evidence:
  - status: 404
    url: https://www.cambrianbio.com/openapi.json
  - status: 404
    url: https://www.cambrianbio.com/developers
  - status: 404
    url: https://www.cambrianbio.com/.well-known/agent-card.json
  - status: 404
    url: https://www.cambrianbio.com/llms.txt
  - status: 200
    url: https://www.cambrianbio.com/
  reason: not-a-software-company
  state: none
created: '2026-08-09'
description: 'Cambrian Bio (Cambrian BioPharma, Inc.) is a New York-headquartered clinical-stage drug development company working on the biology of aging. It runs a distributed "PipeCo" model — sourcing promising academic and early-stage science, then capitalizing and staffing each program as a separate subsidiary company under a shared development engine — to advance therapeutics that target the metabolic pathways that decline with age, first as treatments for chronic metabolic disease and ultimately as preventive medicines that extend healthspan. Its lead program, ATX-304, is an AMPK network activator with reported positive human translational data. Cambrian Bio is a therapeutics developer, not a software vendor: it publishes a corporate website, a science and pipeline overview, news and publications, and a blog, but no public API, developer portal, SDK, or machine-readable specification.'
image: https://cdn.prod.website-files.com/600be113c4111047016de64a/600be12d2137ed834d86305c_webclip.png
layout: provider
modified: '2026-08-09'
name: Cambrian Bio
nav: Providers
network: true
overview: 'Cambrian Bio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Drug Development, and Longevity.


  Cambrian Bio''s developer surface includes engineering blog, product news, support, and 8 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 7.6
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cambrian-bio/refs/heads/main/screenshots/cambrian-bio-2026-09-02T145011.png
security:
- kind: domain-security
  name: Cambrian Bio Domain Security
  slug: cambrian-bio-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: cambrian-bio
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Drug Development
- Longevity
- Healthcare
- Life Sciences
- Clinical Stage
- Aging
- Metabolic Disease
website: https://www.cambrianbio.com/
---
