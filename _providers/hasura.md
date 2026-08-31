---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.3
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Hasura Agentic Access
  operation_count: 10
  slug: hasura-agentic-access
  summary_line: 10 operations · 6 acting
api_count: 1
apis:
- description: The Hasura GraphQL Engine v2 provides instant realtime GraphQL APIs on your data with fine-grained access control. Supports GraphQL queries, mutations, and subscriptions at the /v1/graphql endpoint, a
  name: Hasura GraphQL API
  slug: hasura-graphql-api
- description: The Hasura Metadata API allows programmatic management of Hasura GraphQL Engine configuration. All requests are POST requests to the /v1/metadata endpoint, supporting operations for managing data sour
  name: Hasura Metadata API
  slug: hasura-metadata-api
- description: The Hasura Data Delivery Network (DDN) is a metadata-driven API platform that generates instant GraphQL APIs on any data source. It provides queries, mutations, and subscriptions as root-level fields,
  name: Hasura DDN GraphQL API
  slug: hasura-ddn-graphql-api
- description: The Hasura Cloud API provides a GraphQL endpoint at https://data.pro.hasura.io/v1/graphql to programmatically create and manage Hasura Cloud projects, tenants, collaborators, and configurations. Authe
  name: Hasura Cloud API
  slug: hasura-cloud-api
- description: The PromptQL Natural Language API allows interaction with Hasura PromptQL to send natural language messages and receive AI-powered responses with streaming support. It enables accurate AI by continuou
  name: PromptQL Natural Language API
  slug: promptql-natural-language-api
- description: The Graphql API from Hasura — 2 operation(s) for graphql.
  name: Hasura Graphql API
  slug: hasura-graphql-api
- description: The Healthz API from Hasura — 1 operation(s) for healthz.
  name: Hasura Healthz API
  slug: hasura-healthz-api
- description: Hasura metadata management.
  name: Hasura Metadata API
  slug: hasura-metadata-api
- description: The Query API from Hasura — 1 operation(s) for query.
  name: Hasura Query API
  slug: hasura-query-api
- description: The Source Health API from Hasura — 1 operation(s) for source health.
  name: Hasura Source Health API
  slug: hasura-source-health-api
- description: The V1alpha1 API from Hasura — 2 operation(s) for v1alpha1.
  name: Hasura V1alpha1 API
  slug: hasura-v1alpha1-api
- description: The V1beta1 API from Hasura — 1 operation(s) for v1beta1.
  name: Hasura V1beta1 API
  slug: hasura-v1beta1-api
- description: The Version API from Hasura — 1 operation(s) for version.
  name: Hasura Version API
  slug: hasura-version-api
artifact_total: 47
asyncapis:
- description: AsyncAPI definition for Hasura GraphQL Engine real-time subscriptions delivered over WebSocket at the `/v1/graphql` endpoint. Hasura supports two WebSocket subprotocols, negotiated via the `Sec-WebSoc
  name: Hasura GraphQL Subscriptions over WebSocket
  slug: hasura-asyncapi
collections:
- collection_type: postman
  name: Hasura Engine HTTP APIs Graphql API
  slug: postman-hasura-graphql-api
- collection_type: postman
  name: Hasura Engine HTTP APIs Graphql Healthz API
  slug: postman-hasura-healthz-api
- collection_type: postman
  name: Hasura Engine HTTP APIs Graphql Metadata API
  slug: postman-hasura-metadata-api
- collection_type: postman
  name: Hasura Engine HTTP APIs Graphql Query API
  slug: postman-hasura-query-api
- collection_type: postman
  name: Hasura Engine HTTP APIs Graphql Source Health API
  slug: postman-hasura-source-health-api
- collection_type: postman
  name: Hasura Engine HTTP APIs Graphql V1alpha1 API
  slug: postman-hasura-v1alpha1-api
- collection_type: postman
  name: Hasura Engine HTTP APIs Graphql V1beta1 API
  slug: postman-hasura-v1beta1-api
- collection_type: postman
  name: Hasura Engine HTTP APIs Graphql Version API
  slug: postman-hasura-version-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Hasura Engine HTTP APIs Graphql API
  slug: open-hasura-graphql-api
- collection_type: open
  name: Hasura Engine HTTP APIs Graphql Healthz API
  slug: open-hasura-healthz-api
- collection_type: open
  name: Hasura Engine HTTP APIs Graphql Metadata API
  slug: open-hasura-metadata-api
- collection_type: open
  name: Hasura Engine HTTP APIs Graphql Query API
  slug: open-hasura-query-api
- collection_type: open
  name: Hasura Engine HTTP APIs Graphql Source Health API
  slug: open-hasura-source-health-api
- collection_type: open
  name: Hasura Engine HTTP APIs Graphql V1alpha1 API
  slug: open-hasura-v1alpha1-api
- collection_type: open
  name: Hasura Engine HTTP APIs Graphql V1beta1 API
  slug: open-hasura-v1beta1-api
- collection_type: open
  name: Hasura Engine HTTP APIs Graphql Version API
  slug: open-hasura-version-api
- collection_type: open
  name: Hasura GraphQL Engine HTTP APIs
  slug: open-hasura
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/hasura/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hasura-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/hasura-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/hasura-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hasura-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hasura-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hasura
- group: company
  title: ''
  type: Website
  url: https://hasura.io/
- group: commercial
  title: ''
  type: Plans
  url: https://hasura.io/pricing
- group: auth
  title: ''
  type: Authentication
  url: https://hasura.io/docs/2.0/auth/overview/
- group: start
  title: ''
  type: GettingStarted
  url: https://hasura.io/docs/2.0/getting-started/overview/
- group: start
  title: ''
  type: GettingStarted
  url: https://hasura.io/docs/2.0/getting-started/overview/
- group: auth
  title: ''
  type: Security
  url: https://hasura.io/docs/2.0/security/overview/
- group: build
  title: ''
  type: CLI
  url: https://hasura.io/docs/2.0/hasura-cli/overview/
- group: other
  title: ''
  type: CI/CD
  url: https://hasura.io/docs/2.0/cloud-ci-cd/index/
- group: operate
  title: ''
  type: Support
  url: https://hasura.io/docs/2.0/get-support/
- group: operate
  title: ''
  type: FAQ
  url: https://hasura.io/docs/2.0/faq/index/
- group: operate
  title: ''
  type: Discord
  url: https://discord.com/invite/hasura
- group: other
  title: ''
  type: Glossary
  url: https://hasura.io/docs/2.0/glossary/index/
- group: company
  title: ''
  type: Blog
  url: https://hasura.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://hasura.io/pricing
- group: other
  title: ''
  type: Customers
  url: https://hasura.io/customers
- group: learn
  title: ''
  type: Webinars
  url: https://hasura.io/events?category=Webinar#wall-section
- group: other
  title: ''
  type: Hub
  url: https://hasura.io/graphql/
- group: other
  title: ''
  type: Events
  url: https://hasura.io/events
- group: other
  title: ''
  type: WhitePapers
  url: https://hasura.io/resources
- group: start
  title: ''
  type: Login
  url: https://cloud.hasura.io/signup
- group: start
  title: ''
  type: Signup
  url: https://cloud.hasura.io/signup/new_user
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hasura.io/legal/hasura-cloud-terms-of-service
- group: learn
  title: ''
  type: Tutorials
  url: https://hasura.io/learn/
- group: operate
  title: ''
  type: FAQ
  url: https://hasura.io/learn/#learn-faq
- group: company
  title: ''
  type: AboutPage
  url: https://hasura.io/about/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.hasura.io/
- group: operate
  title: ''
  type: ChangeLog
  url: https://hasura.io/changelog
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/hasura/graphql-engine
- group: build
  title: ''
  type: GitHubDiscussions
  url: https://github.com/hasura/graphql-engine/discussions
- group: build
  title: ''
  type: GitHubReleases
  url: https://github.com/hasura/graphql-engine/releases
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/hasurahq
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hasura/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCZo1ciR8pZvdD3Wxp9aSNhQ
- group: other
  title: ''
  type: Reddit
  url: https://www.reddit.com/r/Hasura/
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/hasura
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hasura.io/legal/hasura-privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hasura.io/legal/website-terms-of-use
- group: operate
  title: ''
  type: Contact
  url: https://hasura.io/contact-us
- group: operate
  title: ''
  type: Help
  url: https://hasura.io/help/
- group: operate
  title: ''
  type: Community
  url: https://hasura.io/community
- group: other
  title: ''
  type: ProductPage
  url: https://hasura.io/ddn
- group: docs
  title: ''
  type: APIReference
  url: https://hasura.io/docs/2.0/api-reference/overview/
- group: docs
  title: ''
  type: Documentation
  url: https://hasura.io/docs/3.0/index/
- group: other
  title: ''
  type: CaseStudies
  url: https://hasura.io/user-stories/
- group: commercial
  title: ''
  type: Legal
  url: https://hasura.io/legal
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://hasura.io/docs/2.0/enterprise/release-notes/
- group: other
  title: ''
  type: ProductPage
  url: https://hasura.io/learn-more
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/hasura/promptql-mcp
- group: agent
  title: ''
  type: LlmsText
  url: https://hasura.io/docs/llms.txt
created: '2025-06-10T00:00:00.000Z'
description: We've spent years perfecting products that make it effortless to access and use data.PromptQL for AIAccurate AI by continuously learning the unique context of your business.
features:
- name: Use Cases
- name: GraphQL backend
- name: Data Access Layer
- name: API gateway
finops:
- name: Hasura Finops
  service_category: API
  slug: hasura-finops
graphqls:
- description: The Hasura GraphQL Engine v2 provides instant realtime GraphQL APIs on your data with fine-grained access control. Supports GraphQL queries, mutations, and subscriptions at the /v1/graphql endpoint, a
  name: Hasura GraphQL API
  slug: hasura-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hasura.png
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-08-03'
name: Hasura
nav: Providers
network: true
overview: 'Hasura publishes 10 APIs on the [APIs.io](https://apis.io/) network, including GraphQL API, Metadata API, Graphql API, and 7 more. Tagged areas include Data Access and GraphQL.


  The Hasura catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Hasura''s developer surface includes authentication, getting-started guide, CLI, support, FAQ, engineering blog, pricing, and 49 more developer resources.'
plans:
- name: Hasura Plans Pricing
  plan_count: 3
  slug: hasura-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Hasura Rate Limits
  slug: hasura-rate-limits
rules:
- effective_rule_count: 33
  extends:
  - spectral:asyncapi
  name: Hasura API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 5
  slug: hasura-asyncapi-spectral-rules
score:
  band: developing
  composite: 53.3
  coverage:
    artifact_dirs: 15
    catalog_gap: 80.3
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 68.4
    commercial_clarity: 68.4
    contract_governance: 11.4
    contract_quality: 57.5
    developer_ergonomics: 59.5
    discoverability: 48.1
    governance: 11.4
    operational_transparency: 55.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 53.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hasura/refs/heads/main/screenshots/hasura-2026-06-20T182534.png
security:
- kind: authentication
  name: Hasura Authentication
  slug: hasura-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Hasura Domain Security
  slug: hasura-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Hasura Vulnerability Disclosure
  slug: hasura-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Hasura Trust Center
  slug: hasura-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: hasura
tags:
- Data Access
- GraphQL
website: https://hasura.io/
---
