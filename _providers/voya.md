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
    well_known_catalog: true
  schema_version: 0.2
  score: 2.9
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/voya-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://voya.ai
- group: company
  title: ''
  type: Website
  url: https://www.voya.de/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/voya-llms.txt
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.voya.de/agb
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.voya.de/datenschutz
- group: other
  title: ''
  type: Imprint
  url: https://www.voya.de/impressum
- group: company
  title: ''
  type: Careers
  url: https://www.voya.de/karriere
- group: operate
  title: ''
  type: Contact
  url: https://www.voya.de/kontakt
created: '2026-07-17'
description: Voya GmbH is a software development and consulting company based in Hamburg, Germany, with nearshore TechHubs in Bucharest and Cluj, Romania. Founded in 2015 as an AI-powered chat-based business-travel booking platform backed by 500 Global, it became a wholly-owned Volkswagen Group subsidiary and has been an independent, founder-led company again since November 2024. Today Voya delivers end-to-end software development, applied AI solutions, and engineering team building for automotive, mobility, and travel clients including Volkswagen, Audi, CARIAD, Deutsche Bahn, and Lufthansa City Center. TISAX certified. Voya publishes no public API or developer portal.
image: https://cdn.sanity.io/images/sn6yku2f/production/5dde5c37671f13ee0494bf1e4264e5f7238abb63-1200x630.png
layout: provider
modified: '2026-07-21'
name: Voya
nav: Providers
network: true
overview: Voya is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Software Development, Consulting, Artificial Intelligence, and Automotive.
random_paper: 6
score:
  band: minimal
  composite: 10.0
  coverage:
    artifact_dirs: 4
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
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 10.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/voya/refs/heads/main/screenshots/voya-2026-09-02T170257.png
security:
- kind: domain-security
  name: Voya Domain Security
  slug: voya-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: voya
tags:
- Company
- Software Development
- Consulting
- Artificial Intelligence
- Automotive
- Mobility
- Travel
- Nearshoring
website: https://voya.ai
---
