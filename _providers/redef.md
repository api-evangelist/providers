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
  url: security/redef-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://redef.com/
- group: operate
  title: ''
  type: Support
  url: https://redef.com/info/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://redef.com/info/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://redef.com/info/terms
- group: start
  title: ''
  type: SignUp
  url: https://redef.com/signup/join
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/REDEF
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/redef-llms.txt
coverage:
  checked: '2026-08-13'
  detail: REDEF is a hand-curated consumer media site and email newsletter with no developer program at all — redef.com answers every probed API path (/openapi.json, /graphql, /api, /docs, /llms.txt and all /.well-known/*) with the identical 504,882-byte HTML catch-all page it serves for "/", api./developer./docs.redef.com are NXDOMAIN, and the REDEF GitHub org holds one forked EJS build tool from 2015.
  evidence:
  - status: 200
    url: https://redef.com/openapi.json
  - status: 200
    url: https://redef.com/.well-known/agent-card.json
  - status: 200
    url: https://redef.com/api
  - status: 200
    url: https://redef.com/open_search.xml
  - status: 200
    url: https://api.github.com/orgs/REDEF/repos
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: REDEF is a media curation and newsletter company founded and led by Jason Hirschhorn (CEO + Chief Curator) that "DJs the internet" — surfacing daily remixes of the stories, people, and ideas that matter across Media, Fashion, Music, Sports, and Tech. Readers follow curated Mixes, Sets, Originals, Charts, and email Newsletters ("interest remixes for curious minds"), and can build and share their own mixes. ReDEF was surfaced as a portfolio company of bloomberg-beta and added to the API Evangelist network; enrichment found a public consumer content website (redef.com) but no public developer program, API, documentation, or machine-readable surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/redef.png
layout: provider
modified: '2026-08-13'
name: ReDEF
nav: Providers
network: true
overview: 'ReDEF is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Media, Curation, Newsletters, and Content.


  ReDEF''s developer surface includes support, signup flow, and 6 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 13.9
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 13.9
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Redef Domain Security
  slug: redef-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: redef
tags:
- Company
- Media
- Curation
- Newsletters
- Content
- Publishing
- Pop Culture
website: https://redef.com/
---
