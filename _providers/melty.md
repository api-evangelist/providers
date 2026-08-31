---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-08-30'
api_count: 2
apis:
- description: Kisee is an open-source HTTP API server published by Melty Group that exchanges valid username/password pairs for JSON Web Tokens, and nothing else. It is self-hosted software, not a Melty-operated pu
  name: Kisee — Identity Provider Server
  slug: melty-kisee
- description: Pasee is an open-source HTTP API server published by Melty Group that layers group and user management over one or more identity providers — one or many Kisee instances plus external providers such as
  name: Pasee — Identity Management Server
  slug: melty-pasee
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/melty-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.melty.fr/
- group: company
  title: ''
  type: Blog
  url: https://www.melty.fr/actu/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.melty.fr/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/meltygroup
- group: operate
  title: ''
  type: Support
  url: https://www.melty.fr/nous-contacter
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.melty.fr/mentions-legales
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.reworldmedia.com/mentions-legales/politique-des-donnees-a-caractere-personnel-et-cookies
- group: build
  title: ''
  type: Packages
  url: packages/melty-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/melty-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/melty-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/melty-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/melty-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/melty-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/melty-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/melty-conventions.yml
coverage:
  checked: '2026-08-17'
  detail: melty.fr is a WordPress consumer media site with no developer portal at all, and the only two documented HTTP APIs the company ever published — the self-hosted Kisee and Pasee identity servers on readthedocs — ship no OpenAPI, AsyncAPI, GraphQL SDL, Postman collection or JSON Schema in any of the 7 meltygroup GitHub repositories.
  evidence:
  - status: 404
    url: https://www.melty.fr/openapi.json
  - status: 404
    url: https://www.melty.fr/.well-known/agent-card.json
  - status: 200
    url: https://kisee.readthedocs.io/en/latest/
  - status: 200
    url: https://api.github.com/repos/meltygroup/kisee/git/trees/HEAD?recursive=1
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-08-17'
description: Melty is a French digital media brand for youth culture — news and entertainment coverage of series, cinema, television, celebrity, gaming and lifestyle aimed at a 15-34 audience. Founded in 2008 in Paris and operated by EEPLE SAS, Melty was a Serena Capital portfolio company before Reworld Media acquired 100% of the business in a distressed M&A process completed in 2021-2022; melty.fr is now published by EEPLE within Groupe Reworld Media and monetised through advertising and native content rather than software licensing. Melty publishes no developer program, no public API product and no machine-readable API contract. Its only public developer surface is the meltygroup GitHub organisation, which carries the identity servers Kisee and Pasee — MIT-licensed, self-hosted Python HTTP API servers written in-house and released to PyPI, last published in 2021.
image: https://www.melty.fr/wp-content/uploads/meltyfr/2023/06/melty-logo.jpg
layout: provider
modified: '2026-08-17'
name: Melty
nav: Providers
network: true
overview: 'Melty publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Media, Publishing, and News.


  Melty''s developer surface includes engineering blog, support, authentication, and 13 more developer resources.'
plans:
- name: Melty Plans Pricing
  plan_count: 0
  slug: melty-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Melty Rate Limits
  slug: melty-rate-limits
score:
  band: emerging
  composite: 17.7
  coverage:
    artifact_dirs: 11
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 17.7
  provenance:
    conformance: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Melty Authentication
  slug: melty-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Melty Domain Security
  slug: melty-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: melty
tags:
- Company
- Consumer
- Media
- Publishing
- News
- Entertainment
- France
- Advertising
- Open-Source
- Identity
website: https://www.melty.fr/
---
