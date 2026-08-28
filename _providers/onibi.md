---
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
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/onibi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.onibi.gg/
- group: other
  title: ''
  type: Product
  url: https://www.tomoendlessblue.com/en/
- group: operate
  title: ''
  type: Contact
  url: https://www.onibi.gg/contact.html
- group: company
  title: ''
  type: Careers
  url: https://www.onibi.gg/career.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tomoendlessblue.com/en/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tomoendlessblue.com/en/privacy-policy/
- group: operate
  title: ''
  type: Community
  url: https://discord.gg/tomoendlessblue
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/onibigg
- group: company
  title: ''
  type: Twitter
  url: https://x.com/onibigg
- group: other
  title: ''
  type: Steam
  url: https://store.steampowered.com/app/3301510/Tomo_Endless_Blue/
- group: other
  title: ''
  type: Kickstarter
  url: https://www.kickstarter.com/projects/1891746870/tomoendlessblue
- group: other
  title: ''
  type: LinkTree
  url: https://linktr.ee/TomoEndlessBlue
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/onibi-llms.txt
coverage:
  checked: '2026-08-17'
  detail: 'Onibi is a pre-release consumer game studio whose entire web presence is three static pages (Studio, Career, Contact) plus a nine-language marketing site for the unreleased Tomo: Endless Blue — the Steam page promises the game will be moddable but no modding API, SDK or developer documentation exists yet, and the only HTTP API on any Onibi host is /api/ on the product site, which its own robots.txt disallows; onibi.gg answers HTTP 200 with the same 43KB homepage for /openapi.json and every other probed path, so its 200s are soft-404s, while tomoendlessblue.com returns real 404s for all of them.'
  evidence:
  - status: 200
    url: https://www.onibi.gg/openapi.json
  - status: 404
    url: https://www.tomoendlessblue.com/.well-known/agent-card.json
  - status: 200
    url: https://www.tomoendlessblue.com/robots.txt
  - status: 404
    url: https://api.github.com/orgs/onibi
  reason: no-developer-program
  state: none
created: '2026-08-17'
description: 'Onibi (Onibi inc.) is a video game studio founded in 2023 by Benjamin Devienne, with a distributed team in San Francisco, London and Bordeaux drawn from Blizzard, Riot, Ubisoft, EA and Rockstar. Its first title is Tomo: Endless Blue, a procedurally generated monster-taming voxel sandbox open world announced for Steam and funded through a Kickstarter campaign plus roughly $6.5M in seed capital from SeaX Ventures, Serena, Octopus Ventures and Pix Capital. Onibi is a consumer game studio, not an API provider: as of August 2026 the game is unreleased and the studio publishes no developer portal, API reference, SDK or machine-readable specification. The Steam page states an intent to keep the game moddable, but no modding API, tooling or documentation has been published yet, so there is nothing machine-readable to catalog.'
image: https://onibi.gg/unfurl/onibi_studio.png
layout: provider
modified: '2026-08-17'
name: Onibi
nav: Providers
network: true
overview: Onibi is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Video Games, Game Development, Game Studio, and Sandbox MMO.
random_paper: 4
score:
  band: minimal
  composite: 10.2
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.2
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: domain-security
  name: Onibi Domain Security
  slug: onibi-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: onibi
tags:
- Company
- Video Games
- Game Development
- Game Studio
- Sandbox MMO
- User Generated Content
- Procedural Generation
- Entertainment
- Consumer Software
website: https://www.onibi.gg/
---
