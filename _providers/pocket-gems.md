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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pocket-gems-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.pocketgems.com/
- group: company
  title: ''
  type: About
  url: https://www.pocketgems.com/about/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pocketgems
- group: operate
  title: ''
  type: Support
  url: https://pocketgems-support.helpshift.com/hc/en/
- group: operate
  title: ''
  type: Community
  url: https://discord.com/invite/VAzufMmXgA
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pocketgems.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pocketgems.com/privacy-policy/
- group: company
  title: ''
  type: Careers
  url: https://www.pocketgems.com/jobs/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/pocket-gems_stock/
- group: build
  title: ''
  type: Packages
  url: packages/pocket-gems-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pocket-gems-llms.txt
coverage:
  checked: '2026-08-05'
  detail: Pocket Gems is an active mobile game studio (Episode, Episode XOXO, War Dragons) that ships consumer apps only — no api./developer./docs. host exists except docs.pocketgems.com, which 302s to an Okta/Google Workspace SSO login for internal Google Drive rather than to developer documentation.
  evidence:
  - status: 0
    url: https://api.pocketgems.com/
  - status: 302
    url: http://docs.pocketgems.com/
  - status: 404
    url: https://www.pocketgems.com/openapi.json
  - status: 404
    url: https://www.pocketgems.com/.well-known/agent-card.json
  - status: 404
    url: https://www.episodeinteractive.com/.well-known/agent-card.json
  - status: 200
    url: https://registry.npmjs.org/-/v1/search?text=%40pocketgems
  reason: no-developer-program
  state: none
created: '2026-08-05'
description: 'Pocket Gems is a San Francisco mobile games and interactive entertainment studio founded in 2009, employing over 200 people and backed by Sequoia Capital and Tencent. It builds and operates the Episode interactive-storytelling network, Episode XOXO, and the 3D real-time strategy title War Dragons on its proprietary mobile-first Mantis Engine, with products downloaded more than 325 million times. Pocket Gems ships consumer mobile applications rather than a developer-facing API program: there is no public developer portal, API reference, or machine-readable specification. Its public developer surface is a GitHub organization and four first-party Apache-2.0 Node.js libraries published to npm under the @pocketgems scope (the internal "Todea" service stack), plus an Episode Writer''s Portal used by story authors.'
image: https://www.pocketgems.com/wp-content/themes/pocketgems/assets/images/pocket-gems-logo@2x.png
layout: provider
modified: '2026-08-05'
name: Pocket Gems
nav: Providers
network: true
overview: 'Pocket Gems is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Gaming, Mobile Games, Interactive Fiction, and Entertainment.


  Pocket Gems'' developer surface includes support and 11 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 11.3
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
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 11.3
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Pocket Gems Domain Security
  slug: pocket-gems-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pocket-gems
tags:
- Company
- Gaming
- Mobile Games
- Interactive Fiction
- Entertainment
- Mobile Applications
- Game Development
- Consumer Software
website: https://www.pocketgems.com/
---
