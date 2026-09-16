---
agent_readiness:
  band: agent-aware
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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 8.5
  scored_at: '2026-09-15'
api_count: 2
apis:
- description: 'KnowHOW is Publicis Sapient''s open-source (Apache-2.0) engineering measurement platform — a KPI dashboard that pulls from Jira, source control, CI and quality tools and reports delivery health across '
  name: Publicis Sapient KnowHOW
  slug: publicis-groupe-knowhow
- description: Sapient Slingshot is Publicis Sapient's proprietary AI software-engineering platform — an enterprise LLM gateway plus a family of agents for legacy modernization, spec generation and code delivery. Th
  name: Sapient Slingshot
  slug: publicis-groupe-sapient-slingshot
artifact_total: 7
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/publicis-groupe/refs/heads/main/security/publicis-groupe-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/publicis-groupe-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.publicisgroupe.com/en
- group: company
  title: ''
  type: About
  url: https://www.publicisgroupe.com/en/the-groupe/about-publicis-groupe
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.publicisgroupe.com/en/legal-mentions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.publicisgroupe.com/en/cookies
- group: company
  title: ''
  type: Blog
  url: https://www.publicissapient.com/resources/blog
- group: operate
  title: ''
  type: Support
  url: https://www.publicissapient.com/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PublicisSapient
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/publicis-groupe/refs/heads/main/packages/publicis-groupe-packages.yml
  title: ''
  type: Packages
  url: packages/publicis-groupe-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/publicis-groupe/refs/heads/main/packages/publicis-groupe-packages.yml
  title: ''
  type: SDKs
  url: packages/publicis-groupe-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/publicis-groupe/refs/heads/main/cli/publicis-groupe-cli.yml
  title: ''
  type: CLI
  url: cli/publicis-groupe-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/publicis-groupe/refs/heads/main/components/publicis-groupe-components.yml
  title: ''
  type: Components
  url: components/publicis-groupe-components.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/publicis-groupe/refs/heads/main/mcp/publicis-groupe-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/publicis-groupe-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/publicis-groupe/refs/heads/main/llms/publicis-groupe-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/publicis-groupe-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/publicis-groupe/refs/heads/main/authentication/publicis-groupe-authentication.yml
  title: ''
  type: Authentication
  url: authentication/publicis-groupe-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/publicis-groupe/refs/heads/main/conformance/publicis-groupe-conformance.yml
  title: ''
  type: Conformance
  url: conformance/publicis-groupe-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/publicis-groupe/refs/heads/main/conformance/publicis-groupe-conformance.yml
  title: ''
  type: Compliance
  url: conformance/publicis-groupe-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/publicis-groupe/refs/heads/main/lifecycle/publicis-groupe-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/publicis-groupe-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/publicis-groupe/refs/heads/main/changelog/publicis-groupe-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/publicis-groupe-changelog.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/publicis-groupe/refs/heads/main/plans/publicis-groupe-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/publicis-groupe-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/publicis-groupe/refs/heads/main/rate-limits/publicis-groupe-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/publicis-groupe-rate-limits.yml
created: '2026-09-13'
description: Publicis Groupe is the French-headquartered global marketing, communications and business-transformation holding company behind Publicis Sapient, Publicis Media, Epsilon, CJ Affiliate, Leo Burnett, Saatchi & Saatchi, Digitas and Razorfish. The Groupe itself runs no public developer program and publishes no API at publicisgroupe.com; its machine-readable surface is produced by the operating units. The largest publicly readable one is the Publicis Sapient KnowHOW suite — an Apache-2.0 engineering-KPI platform (knowhow-api / knowhow-ui / knowhow-common / knowhow-processors on GitHub, container psknowhow/knowhow-api on Docker Hub) whose Spring Boot service self-documents an OpenAPI at /api/v3/api-docs on whatever host an operator deploys it to, plus knowhow-mcp, a self-hosted MCP server exposing the KnowHOW documentation assistant. Alongside it Publicis Sapient publishes the @psnext npm scope — the sling CLI for the Sapient Slingshot enterprise LLM gateway, the lscg local source-context-graph
  CLI and stdio MCP server, and the Block SDK for building iframe Blocks on Publicis Groupe's CoreAI platform. Epsilon and CJ Affiliate, which do publish hosted API contracts, are profiled in their own API Evangelist repositories.
image: https://www.publicisgroupe.com/themes/custom/publicis/front/src/images/theme/share.jpg
layout: provider
mcp_servers:
- description: ''
  name: Publicis Groupe — Model Context Protocol servers
  slug: publicis-groupe-model-context-protocol-servers
modified: '2026-09-13'
name: Publicis Groupe
nav: Providers
network: true
overview: 'Publicis Groupe publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, Marketing, Media, and Digital Transformation.


  Publicis Groupe''s developer surface includes engineering blog, support, CLI, authentication, changelog, and 16 more developer resources.'
plans:
- name: Publicis Groupe Plans Pricing
  plan_count: 0
  slug: publicis-groupe-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Publicis Groupe Rate Limits
  slug: publicis-groupe-rate-limits
score:
  band: thin
  composite: 28.0
  coverage:
    artifact_dirs: 14
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 54.8
    discoverability: 66.7
    operational_transparency: 18.4
  previous_composite: 28.0
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-15'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Publicis Groupe Authentication
  slug: publicis-groupe-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Publicis Groupe Domain Security
  slug: publicis-groupe-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: publicis-groupe
tags:
- Company
- Advertising
- Marketing
- Media
- Digital Transformation
- Consulting
- Artificial Intelligence
- Developer Tools
- Engineering Metrics
- Open-Source
- MCP
- Agency Holding Company
website: https://www.publicisgroupe.com/en
---
