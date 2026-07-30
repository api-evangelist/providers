---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.9
  scored_at: '2026-07-28'
api_count: 4
apis:
- description: Assembly ("hive") membership for the authenticated member.
  name: La Ruche qui dit Oui! Assemblies API
  slug: la-ruche-qui-dit-oui-assemblies-api
- description: OAuth 2 token issuance.
  name: La Ruche qui dit Oui! Authentication API
  slug: la-ruche-qui-dit-oui-authentication-api
- description: Basket, orders and payment.
  name: La Ruche qui dit Oui! Orders API
  slug: la-ruche-qui-dit-oui-orders-api
- description: Products and offers on sale for a distribution.
  name: La Ruche qui dit Oui! Sale API
  slug: la-ruche-qui-dit-oui-sale-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/la-ruche-qui-dit-oui-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/la-ruche-qui-dit-oui-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://laruchequiditoui.fr
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lrqdo
- group: operate
  title: ''
  type: Support
  url: https://support.crowdfarming.com/l/fr
- group: operate
  title: ''
  type: HelpCenter
  url: https://laruchequiditoui.fr/en/open-incident
- group: start
  title: ''
  type: SignUp
  url: https://laruchequiditoui.fr/fr/auth
- group: commercial
  title: ''
  type: TermsOfService
  url: https://laruchequiditoui.fr/fr/tos
- group: company
  title: ''
  type: Blog
  url: https://laruchequiditoui.fr/fr/what-the-field/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/la-ruche-qui-dit-oui-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/la-ruche-qui-dit-oui-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/la-ruche-qui-dit-oui-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/la-ruche-qui-dit-oui-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/la-ruche-qui-dit-oui-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/la-ruche-qui-dit-oui-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/la-ruche-qui-dit-oui-api-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: La Ruche qui dit Oui! is a French direct-from-farmer food marketplace, founded in Paris in 2010 and known in English-speaking markets as The Food Assembly. It connects members with local and European producers through neighbourhood assemblies ("ruches" / hives) and, since a May 2025 merger with CrowdFarming, through direct home delivery of seasonal boxes, subscriptions and harvest "adoptions" in which a member reserves the output of a specific tree, hive or plot for a season. The company operated a public member-facing REST API documented as the Food Assembly API — OAuth 2 token issuance, assembly membership, distribution product and offer listings, and the basket/order payment flow — published as an API Blueprint in the lrqdo/developer repository. That developer documentation has not been updated since 2017, and there is no current developer portal, but the API host remains live behind bearer authentication.
image: https://laruchequiditoui.fr/img/seo/og-image.jpg
layout: provider
modified: '2026-07-19'
name: La Ruche qui dit Oui!
nav: Providers
network: true
overview: 'La Ruche qui dit Oui! publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Assemblies API, Authentication API, Orders API, and 1 more. Tagged areas include Company, Food, Agriculture, Marketplace, and E-Commerce.


  La Ruche qui dit Oui!''s developer surface includes authentication, support, signup flow, engineering blog, and 13 more developer resources.'
random_paper: 23
score:
  band: thin
  composite: 35.9
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 64.1
    developer_ergonomics: 19.0
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 35.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: La Ruche Qui Dit Oui Authentication
  slug: la-ruche-qui-dit-oui-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: La Ruche Qui Dit Oui Domain Security
  slug: la-ruche-qui-dit-oui-domain-security
  summary_line: TLSv1.3 · DMARC
slug: la-ruche-qui-dit-oui
tags:
- Company
- Food
- Agriculture
- Marketplace
- E-Commerce
- Local Food
- Sustainability
- France
website: https://laruchequiditoui.fr
---
