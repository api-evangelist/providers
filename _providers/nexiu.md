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
- group: company
  title: ''
  type: Website
  url: https://nexiu.ai
- group: commercial
  title: ''
  type: Pricing
  url: https://nexiu.ai/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nexiu.ai/privacy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nexiu-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nexiu-domain-security.yml
created: '2026-07-17'
description: Nexiu (Nexiu AI LLC) is a Latin America-focused recruiting automation platform that uses AI agents to source, contact, screen, and schedule high-volume candidates over the official WhatsApp Business API, integrating with Google Workspace (Gmail, Calendar, Meet) and existing ATS systems and job boards. It offers a fully managed pay-per-hire service (Nexiu Managed) and a self-service SaaS platform (Nexiu Platform) for internal talent-acquisition teams, and is backed by 500 Global (500 Latam) and NVIDIA Inception. As of this pass Nexiu consumes third-party APIs (WhatsApp Business, Google, Anthropic Claude, OpenAI) but does not publish a public developer API of its own.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nexiu.png
layout: provider
modified: '2026-07-20'
name: Nexiu
nav: Providers
network: true
overview: 'Nexiu is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Recruiting, Human Resources, Automation, and Artificial Intelligence.


  Nexiu''s developer surface includes pricing and 4 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 5.7
  coverage:
    artifact_dirs: 3
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
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  previous_composite: 5.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nexiu/refs/heads/main/screenshots/nexiu-2026-08-07T185149.png
security:
- kind: domain-security
  name: Nexiu Domain Security
  slug: nexiu-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nexiu
tags:
- Company
- Recruiting
- Human Resources
- Automation
- Artificial Intelligence
- WhatsApp
- Latin America
website: https://nexiu.ai
---
