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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: design
  href: https://artifacts.apis.io/arria-nlg/conformance/arria-nlg-conformance.yml
  title: ''
  type: Conformance
  url: conformance/arria-nlg-conformance.yml
- group: other
  href: https://artifacts.apis.io/arria-nlg/hosts/arria-nlg-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arria-nlg-hosts.yml
- group: other
  href: https://artifacts.apis.io/arria-nlg/vendors/arria-nlg-vendors.yml
  title: ''
  type: Vendors
  url: vendors/arria-nlg-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.arria.com/terms-of-use
- group: auth
  title: ''
  type: Security
  url: https://www.arria.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.arria.com/privacy-policy
- group: other
  title: ''
  type: Leadership
  url: https://www.arria.com/leadership
- group: auth
  href: https://artifacts.apis.io/arria-nlg/security/arria-nlg-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arria-nlg-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.arria.com
- group: company
  title: ''
  type: Blog
  url: https://www.arria.com/blog
- group: operate
  title: ''
  type: Contact
  url: https://www.arria.com/contact
- group: start
  title: ''
  type: GettingStarted
  url: https://www.arria.com/get-started
- group: docs
  title: ''
  type: Documentation
  url: https://www.arria.com/document-library
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 403
    url: https://go.arria.com/mcp
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-26'
description: Arria NLG provides enterprise generative AI solutions, offering a platform that combines deterministic natural language generation with large language model capabilities. Their products include Studio for authoring analytics, Author for hybrid deterministic‑plus‑LLM content creation, and Answers for conversational AI. Arria serves industries such as financial services, pharma, energy, and consumer goods, delivering automated reports, portfolio commentaries, and custom analytics. The company emphasizes compliance, security, and integration with BI tools like PowerBI, Tableau, and Qlik.
image: https://www.arria.com/wp-content/uploads/2026/02/Site-ShareCard-SwirlyColors-1024x536b.webp
layout: provider
modified: '2026-09-26'
name: Arria NLG
nav: Providers
network: true
overview: 'Arria NLG is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Generative AI, Natural Language Generation, Enterprise Software, and Financial Services.


  Arria NLG''s developer surface includes engineering blog, getting-started guide, documentation, and 10 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 11.6
  coverage:
    artifact_dirs: 11
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.8
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 49.1
    operational_transparency: 5.3
  previous_composite: 17.4
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 13.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/arria-nlg/arria-nlg-2026-10-11T100341.png
security:
- kind: domain-security
  name: Arria Nlg Domain Security
  slug: arria-nlg-domain-security
  summary_line: TLSv1.3
slug: arria-nlg
tags:
- Artificial Intelligence
- Generative AI
- Natural Language Generation
- Enterprise Software
- Financial Services
website: https://www.arria.com
---
