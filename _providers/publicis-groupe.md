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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 8.5
  scored_at: '2026-10-31'
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
- group: company
  title: ''
  type: BlogRSS
  url: https://www.publicisgroupe.com/fr/rss.xml
- group: auth
  href: https://artifacts.apis.io/publicis-groupe/security/publicis-groupe-domain-security.yml
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
  href: https://artifacts.apis.io/publicis-groupe/packages/publicis-groupe-packages.yml
  title: ''
  type: Packages
  url: packages/publicis-groupe-packages.yml
- group: build
  href: https://artifacts.apis.io/publicis-groupe/packages/publicis-groupe-packages.yml
  title: ''
  type: SDKs
  url: packages/publicis-groupe-packages.yml
- group: build
  href: https://artifacts.apis.io/publicis-groupe/cli/publicis-groupe-cli.yml
  title: ''
  type: CLI
  url: cli/publicis-groupe-cli.yml
- group: design
  href: https://artifacts.apis.io/publicis-groupe/components/publicis-groupe-components.yml
  title: ''
  type: Components
  url: components/publicis-groupe-components.yml
- group: agent
  href: https://artifacts.apis.io/publicis-groupe/mcp/publicis-groupe-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/publicis-groupe-mcp.yml
- group: agent
  href: https://artifacts.apis.io/publicis-groupe/llms/publicis-groupe-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/publicis-groupe-llms.txt
- group: auth
  href: https://artifacts.apis.io/publicis-groupe/authentication/publicis-groupe-authentication.yml
  title: ''
  type: Authentication
  url: authentication/publicis-groupe-authentication.yml
- group: design
  href: https://artifacts.apis.io/publicis-groupe/conformance/publicis-groupe-conformance.yml
  title: ''
  type: Conformance
  url: conformance/publicis-groupe-conformance.yml
- group: auth
  href: https://artifacts.apis.io/publicis-groupe/conformance/publicis-groupe-conformance.yml
  title: ''
  type: Compliance
  url: conformance/publicis-groupe-conformance.yml
- group: design
  href: https://artifacts.apis.io/publicis-groupe/lifecycle/publicis-groupe-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/publicis-groupe-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/publicis-groupe/changelog/publicis-groupe-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/publicis-groupe-changelog.yml
- group: commercial
  href: https://artifacts.apis.io/publicis-groupe/plans/publicis-groupe-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/publicis-groupe-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/publicis-groupe/rate-limits/publicis-groupe-rate-limits.yml
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
modified: '2026-10-06'
name: Publicis Groupe
nav: Providers
network: true
overview: 'Publicis Groupe is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, Marketing, Media, and Digital Transformation.


  Publicis Groupe''s developer surface includes engineering blog, support, CLI, authentication, changelog, and 17 more developer resources.'
plans:
- name: Publicis Groupe Plans Pricing
  plan_count: 0
  slug: publicis-groupe-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Publicis Groupe Rate Limits
  slug: publicis-groupe-rate-limits
score:
  band: thin
  composite: 30.5
  coverage:
    artifact_dirs: 17
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
    discoverability: 56.7
    operational_transparency: 31.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 30.5
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/publicis-groupe/publicis-groupe-2026-10-11T112928.png
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
- Open Source
- MCP
- Agency Holding Company
website: https://www.publicisgroupe.com/en
---
