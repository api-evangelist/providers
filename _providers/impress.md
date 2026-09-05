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
  url: security/impress-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://smile2impress.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://smile2impress.com/us/prices
- group: company
  title: ''
  type: Blog
  url: https://smile2impress.com/us/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://static.smile2impress.com/website/v2/live/media/policy/terms-and-conditions_us.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://smile2impress-5970216.hs-sites.com/us/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/smile2impress
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/impress-llms.txt
coverage:
  checked: '2026-08-23'
  detail: Impress sells orthodontic treatment through 110+ owned clinics and ships software only as two end-user mobile apps; its single API host api.smile2impress.com is the private backend for those apps and answers 403 {"message":"Forbidden"} to every anonymous request, including every OpenAPI, GraphQL and .well-known path, and no developer portal, reference or spec exists on any other host.
  evidence:
  - status: 403
    url: https://api.smile2impress.com/openapi.json
  - status: 404
    url: https://smile2impress.com/openapi.json
  - status: 404
    url: https://smile2impress.com/.well-known/agent-card.json
  - status: 404
    url: https://smile2impress.com/llms.txt
  - status: 200
    url: https://smile2impress.com/
  reason: no-developer-program
  state: none
created: '2026-08-23'
description: 'Impress (legal entity Smile2Impress SL) is a Barcelona-founded chain of clear-aligner orthodontic clinics, launched in 2019 by Vladimir Lupenko, Diliara Lupenko and Dr. Khaled Kasem, and today Europe''s largest invisible-orthodontics clinic network. It runs 110+ doctor-led clinics across ten countries — Spain, Italy, Portugal, France, the United Kingdom, Germany, the Netherlands, Sweden, Ukraine and the United States — has treated more than 500,000 patients, and pairs in-clinic 3D intraoral scanning and patented diagnostics with AI-assisted treatment planning and remote monitoring through its patient mobile app. Impress publishes no developer portal, API reference, SDK, CLI, status page, changelog or machine-readable specification of any kind: contract discovery found no OpenAPI, Swagger, GraphQL SDL, AsyncAPI, MCP server, A2A agent card or .well-known document on any host it operates. Its one API host, api.smile2impress.com, is the private backend for the Impress patient app
  and the Impress Clinics practitioner app; it resolves and is live but answers HTTP 403 to every anonymous request, including every spec and .well-known path probed. Its GitHub organization, github.com/smile2impress, is real but carries only internal engineering tooling — five forks of Node.js/TypeScript infrastructure libraries and one first-party static-analysis tool, fe-explorer — and no client library for any Impress service. Products sold are orthodontic treatment, retainers and teeth whitening, priced and booked through the consumer site.'
image: https://static.smile2impress.com/website/v2/live/media/images/fav/og-image.jpg
layout: provider
modified: '2026-08-23'
name: Impress
nav: Providers
network: true
overview: 'Impress is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Dental, Orthodontics, and Clear Aligners.


  Impress'' developer surface includes pricing, engineering blog, and 6 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 12.7
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 12.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/impress/refs/heads/main/screenshots/impress-2026-09-02T145849.png
security:
- kind: domain-security
  name: Impress Domain Security
  slug: impress-domain-security
  summary_line: TLSv1.3 · DMARC
slug: impress
tags:
- Company
- Healthcare
- Dental
- Orthodontics
- Clear Aligners
- Clinics
- Consumer Health
- Telehealth
- Artificial Intelligence
- Mobile Apps
- Spain
website: https://smile2impress.com/
---
