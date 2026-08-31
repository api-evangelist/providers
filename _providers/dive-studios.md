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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dive-studios-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dive-studios-llms.txt
- group: commercial
  title: ''
  type: TermsOfService
  url: https://divestudios.io/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://divestudios.io/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://divestudios.io/contact
- group: company
  title: ''
  type: Website
  url: https://divestudios.io
coverage:
  checked: '2026-08-12'
  detail: DIVE Studios sells K-entertainment media, advertising and creator campaigns — its sitemap is 40 marketing and case-study pages with no developer, docs or reference route, the word "API" appears nowhere on the site, and no api./developer./docs. subdomain resolves; the only machine-readable thing it publishes is an llms.txt describing those same marketing pages.
  evidence:
  - status: 200
    url: https://divestudios.io/sitemap.xml
  - status: 404
    url: https://divestudios.io/openapi.json
  - status: 404
    url: https://divestudios.io/.well-known/agent-card.json
  - status: 200
    url: https://divestudios.io/llms.txt
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: 'DIVE Studios is a global K-entertainment media platform that produces original shows, podcasts, and short-form social content, reaching over 135M Gen Z and Millennial fans and 5B+ lifetime views. The company operates two commercial arms: DIVE Media, which sells advertising and branded content across its podcast, video, and social network, and DIVE Agency (DIVE X), which builds creator, influencer, and celebrity marketing campaigns for global brands connecting with K-culture audiences. It publishes an llms.txt describing its pages but exposes no public developer API, SDK, or portal. Surfaced as a 500 Global portfolio company and profiled in the API Evangelist network.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dive-studios.png
layout: provider
modified: '2026-08-12'
name: DIVE studios
nav: Providers
network: true
overview: 'DIVE studios is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Media, K-Entertainment, Advertising, and Influencer Marketing.


  DIVE studios'' developer surface includes support and 5 more developer resources.'
random_paper: 9
score:
  band: minimal
  composite: 5.7
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
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
  previous_composite: 5.7
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dive-studios/refs/heads/main/screenshots/dive-studios-2026-07-25T212125.png
security:
- kind: domain-security
  name: Dive Studios Domain Security
  slug: dive-studios-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dive-studios
tags:
- Company
- Media
- K-Entertainment
- Advertising
- Influencer Marketing
- Content
- Entertainment
website: https://divestudios.io
---
