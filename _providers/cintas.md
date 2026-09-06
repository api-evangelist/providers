---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cintas-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cintas
- group: company
  title: ''
  type: Website
  url: https://www.cintas.com/
- group: start
  title: ''
  type: Customer Portal (myCintas)
  url: https://www.mycintas.com/
- group: other
  title: ''
  type: Online Store
  url: https://store.cintas.com/site/
- group: company
  title: ''
  type: Investor Relations
  url: https://www.cintas.com/investors/
- group: company
  title: ''
  type: Careers
  url: https://careers.cintas.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cintas.com/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cintas.com/legal/
- group: operate
  title: ''
  type: Support
  url: https://www.cintas.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://www.cintas.com/about/newsroom/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cintas-llms.txt
coverage:
  checked: '2026-09-05'
  detail: Cintas' own 10,733-URL sitemap contains no developer, API, EDI or integration page at all — the only machine-integration door is X12 EDI trading-partner onboarding (850/855/856/810/997) arranged through a Cintas account team and documented publicly only by third-party VANs, while the myCintas portal is a customer sign-in wall, so the contract is reachable only with a signed Cintas account agreement.
  evidence:
  - status: 200
    url: https://www.cintas.com/sitemap/sitemap.xml
  - status: 200
    url: https://www.mycintas.com/
  - status: 404
    url: https://www.cintas.com/openapi.json
  - status: 404
    url: https://www.cintas.com/.well-known/security.txt
  reason: customer-only-docs
  state: gated
created: '2026-03-21'
description: Cintas Corporation is a Fortune 500 provider of uniform rental, facility services, first aid and safety products, and fire protection services. Cintas does not currently publish a public developer portal; B2B integrations (ordering, EDI, route management, billing) are delivered to enterprise customers through the myCintas portal, the Cintas Partner Connect program, and account-managed EDI relationships.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cintas.png
layout: provider
modified: '2026-09-05'
name: Cintas
nav: Providers
network: true
overview: 'Cintas is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Facility Services, First Aid, Fortune 500, Safety, and Uniforms.


  Cintas'' developer surface includes support, engineering blog, and 10 more developer resources.'
press:
- date: '2026-05-25'
  title: Cintas Builds Generative AI-Powered Internal Knowledge ...
  url: https://www.prnewswire.com/news-releases/cintas-builds-generative-ai-powered-internal-knowledge-center-with-google-cloud-302111348.html
- date: '2026-05-25'
  title: What impact is AI having on media localization? (Prof. Jorge ...
  url: https://www.youtube.com/watch?v=vDcr-QlT3rA
- date: '2026-05-25'
  title: 'From Legacy to Innovation: How Cintas is Transforming ...'
  url: https://lemongrasscloud.com/articles/legacy-to-innovation-how-cintas-is-transforming-with-cloud-data-and-ai/
- date: '2026-05-25'
  title: 'Cintas'' AI Strategy: Analysis of Dominance in Business ...'
  url: https://www.klover.ai/cintas-ai-strategy-analysis-of-dominance-in-business-services-ai/
- date: '2026-05-25'
  title: 2025-form-10-k.pdf
  url: https://www.cintas.com/docs/default-source/investor-relations/annual-reports/2025-form-10-k.pdf
random_paper: 12
score:
  band: minimal
  composite: 10.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 4.6
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cintas/refs/heads/main/screenshots/cintas-2026-06-20T174348.png
security:
- kind: domain-security
  name: Cintas Domain Security
  slug: cintas-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: cintas
tags:
- Facility Services
- First Aid
- Fortune 500
- Safety
- Uniforms
website: https://www.cintas.com/
---
