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
  url: https://www.conxtech.com/
- group: company
  title: ''
  type: Blog
  url: https://www.conxtech.com/status/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.conxtech.com/feed/
- group: other
  title: ''
  type: Documents
  url: https://www.conxtech.com/docs/
- group: company
  title: ''
  type: About
  url: https://www.conxtech.com/who-we-are/
- group: operate
  title: ''
  type: ContactForm
  url: https://www.conxtech.com/contact/
- group: company
  title: ''
  type: Careers
  url: https://www.conxtech.com/careers/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/conxtech
- group: company
  title: ''
  type: Twitter
  url: https://x.com/conxtech
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/conxtech
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/ConXtech/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/conxtech-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/conxtech-llms.txt
coverage:
  checked: '2026-08-09'
  detail: ConXtech sells prefabricated structural steel frames, not software — www.conxtech.com is a WordPress marketing site whose only machine-readable endpoint is the stock /wp-json/ CMS discovery document, and every developer-shaped subdomain (api., developer., docs., portal., app.) resolves to an unconfigured-host 404.
  evidence:
  - status: 404
    url: https://www.conxtech.com/openapi.json
  - status: 404
    url: https://www.conxtech.com/llms.txt
  - status: 404
    url: https://www.conxtech.com/.well-known/agent-card.json
  - status: 404
    url: http://developer.conxtech.com/
  - status: 200
    url: https://www.conxtech.com/wp-json/
  reason: not-a-software-company
  state: none
created: '2026-08-09'
description: ConXtech is a Pleasanton, California structural steel subcontractor that designs, fabricates, delivers and erects prefabricated steel building frames for commercial construction. Its ConX Systems product line — the XL-400 and XR-200 chassis — uses patented collar-and-column connection technology and AISC 358 seismic prequalification to erect frames the company reports are three to five times faster than traditional steel erection, across healthcare, data center, retail, office, education, high-density residential, hospitality, industrial and government projects totalling more than 20 million square feet. ConXtech is a private company; its equity trades on secondary markets. It sells a physical building system, not software, and publishes no public developer program, API or machine-readable contract.
image: https://www.conxtech.com/wp-content/uploads/2022/02/Conxtech800x400.jpg
layout: provider
modified: '2026-08-09'
name: ConXtech
nav: Providers
network: true
overview: 'ConXtech is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Construction, Structural Steel, Prefabrication, and Modular Construction.


  ConXtech''s developer surface includes engineering blog, YouTube channel, and 11 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 6.2
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/conxtech/refs/heads/main/screenshots/conxtech-2026-09-02T145140.png
security:
- kind: domain-security
  name: Conxtech Domain Security
  slug: conxtech-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: conxtech
tags:
- Company
- Construction
- Structural Steel
- Prefabrication
- Modular Construction
- Building Systems
- Manufacturing
- Industrial
website: https://www.conxtech.com/
---
