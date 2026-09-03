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
  url: security/triveni-bio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://triveni.bio/
- group: company
  title: ''
  type: About
  url: https://triveni.bio/about/
- group: company
  title: ''
  type: Blog
  url: https://triveni.bio/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://triveni.bio/feed/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://triveni.bio/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://triveni.bio/terms-and-conditions/
- group: company
  title: ''
  type: Careers
  url: https://triveni.bio/about#careers
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/triveni-bio
- group: operate
  title: ''
  type: Contact
  url: https://triveni.bio/contact/
- group: other
  title: ''
  type: Email
  url: mailto:info@triveni.bio
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/triveni-bio_stock/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/triveni-bio-llms.txt
coverage:
  checked: '2026-08-05'
  detail: Triveni Bio is a clinical-stage antibody therapeutics developer whose entire public site is seven WordPress pages (home, about, science, pipeline, news, contact, legal) with no developer, technology, or partner-integration section at all; every API-host, docs-host and /.well-known/ probe 404'd and no api./developer./docs. subdomain resolves.
  evidence:
  - status: 200
    url: https://triveni.bio/page-sitemap.xml
  - status: 404
    url: https://triveni.bio/developers
  - status: 404
    url: https://triveni.bio/openapi.json
  - status: 404
    url: https://triveni.bio/.well-known/agent-card.json
  - status: 404
    url: https://triveni.bio/llms.txt
  reason: not-a-software-company
  state: none
created: '2026-08-05'
description: 'Triveni Bio is a clinical-stage biotechnology company developing first-in-class antibody therapeutics for immunological and inflammatory (I&I) disorders, built on a genetics-informed approach to target discovery combined with advanced antibody engineering. Its lead program TRIV-509 is a dual-specific monoclonal antibody against kallikreins 5 and 7 (KLK5/7) for moderate-to-severe atopic dermatitis, addressing barrier dysfunction, inflammation and itch; TRIV-573 is a half-life-extended, second-generation bispecific that pairs the KLK5/7 mechanism with anti-interleukin-13 (IL-13) and entered Phase 1 in 2026. The pipeline also includes an antibody inhibitor of trypsin 1 and 2 for hereditary pancreatitis driven by PRSS1 mutations. The company launched with a $92M Series A, raised a $115M Series B, and closed a $65M Series C in June 2026, and was named a Fierce 15 biotech of 2025. Triveni Bio is a therapeutics developer, not a software vendor: it publishes no public API, developer
  portal, SDK or machine-readable specification.'
image: https://triveni.bio/wp-content/uploads/2025/09/cropped-triveni-icon-1-192x192.png
layout: provider
modified: '2026-08-05'
name: Triveni Bio
nav: Providers
network: true
overview: 'Triveni Bio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Life Sciences, Pharmaceuticals, and Therapeutics.


  Triveni Bio''s developer surface includes engineering blog and 12 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 4
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
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/triveni-bio/refs/heads/main/screenshots/triveni-bio-2026-09-02T164307.png
security:
- kind: domain-security
  name: Triveni Bio Domain Security
  slug: triveni-bio-domain-security
  summary_line: TLSv1.3
slug: triveni-bio
tags:
- Company
- Biotechnology
- Life Sciences
- Pharmaceuticals
- Therapeutics
- Antibodies
- Immunology
- Drug Development
- Clinical Trials
- Healthcare
website: https://triveni.bio/
---
