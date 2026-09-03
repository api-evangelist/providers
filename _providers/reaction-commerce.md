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
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: The Mailchimp Open Commerce (Reaction Commerce) GraphQL API — a modular, plugin-based headless commerce API covering carts, orders, catalogs, shops, accounts, surcharges and more. Self-hosted; a local
  name: Open Commerce GraphQL API
  slug: open-commerce-graphql-api
artifact_total: 2
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/reactioncommerce/reaction/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/reactioncommerce/reaction/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/reactioncommerce/reaction/blob/trunk/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/reactioncommerce/reaction/blob/trunk/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/reactioncommerce/reaction/blob/trunk/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/reactioncommerce/reaction/blob/trunk/LICENSE
- group: company
  title: ''
  type: Website
  url: https://mailchimp.com/developer/open-commerce/
- group: docs
  title: ''
  type: Documentation
  url: https://mailchimp.com/developer/open-commerce/docs/fundamentals/
- group: docs
  title: ''
  type: APIReference
  url: https://mailchimp.com/developer/open-commerce/api/graphql/
- group: start
  title: ''
  type: GettingStarted
  url: https://mailchimp.com/developer/open-commerce/guides/quick-start/
- group: start
  title: ''
  type: Sandbox
  url: https://mailchimp.com/developer/open-commerce/playground/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/reactioncommerce
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/reactioncommerce/reaction
- group: build
  title: ''
  type: Packages
  url: packages/reaction-commerce-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/reaction-commerce-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/reaction-commerce-cli.yml
- group: design
  title: ''
  type: Components
  url: components/reaction-commerce-components.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/reaction-commerce-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/reaction-commerce-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/reaction-commerce-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://mailchimp.com/about/security/#Responsible_Disclosure
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/reaction-commerce-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/reaction-commerce-llms.txt
created: '2026-07-17'
description: Reaction Commerce is an open-source, API-first, headless commerce platform built with Node.js, React and GraphQL and deployed via Docker and Kubernetes. Acquired by Mailchimp in 2020, it was rebranded as Mailchimp Open Commerce and offered a modular, plugin-based GraphQL API stack aimed at technical, growth-minded retailers. The core `reaction` platform is now discontinued, but its developer documentation, GraphQL API reference, CLI and npm packages remain published under the @reactioncommerce scope. The API is GraphQL and self-hosted; a default local instance exposes its endpoint at http://localhost:3000/graphql, and an interactive GraphQL Playground is provided in the developer docs.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/reaction-commerce.png
layout: provider
modified: '2026-07-20'
name: Reaction Commerce
nav: Providers
network: true
overview: 'Reaction Commerce publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise, Commerce, E-Commerce, and Headless Commerce.


  Reaction Commerce''s developer surface includes documentation, API reference, getting-started guide, sandbox, CLI, and 18 more developer resources.'
random_paper: 19
score:
  band: thin
  composite: 29.2
  coverage:
    artifact_dirs: 8
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 28.9
  open_source:
    applies: true
    score: 100.0
  previous_composite: 29.2
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/reaction-commerce/refs/heads/main/screenshots/reaction-commerce-2026-09-02T152945.png
security:
- kind: vulnerability-disclosure
  name: Reaction Commerce Vulnerability Disclosure
  slug: reaction-commerce-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: reaction-commerce
tags:
- Company
- Enterprise
- Commerce
- E-Commerce
- Headless Commerce
- Open-Source
- GraphQL
- Storefront
- Retail
website: https://mailchimp.com/developer/open-commerce/
---
