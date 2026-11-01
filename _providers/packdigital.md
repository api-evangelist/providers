---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.8
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: GraphQL API to programmatically manage Shopify Hydrogen storefront content — pages, product pages, collection pages, blogs, articles, sections, templates, site settings, schedules, and revisions — wit
  name: Pack Content Management API
  slug: pack-content-management-api
artifact_total: 7
common:
- group: auth
  href: https://artifacts.apis.io/packdigital/security/packdigital-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/packdigital-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://packdigital.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.packdigital.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.packdigital.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.packdigital.com/api-reference/content-management-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.packdigital.com/getting-started/quickstart
- group: operate
  title: ''
  type: Support
  url: https://docs.packdigital.com/getting-started/faq
- group: company
  title: ''
  type: Blog
  url: https://packdigital.com/blogs/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/packdigital
- group: commercial
  title: ''
  type: Pricing
  url: https://packdigital.com/pages/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.packdigital.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.packdigital.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://packdigital.com/pages/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://packdigital.com/pages/privacy-policy
- group: agent
  href: https://artifacts.apis.io/packdigital/mcp/packdigital-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/packdigital-mcp.yml
- group: agent
  href: https://artifacts.apis.io/packdigital/llms/packdigital-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/packdigital-llms.txt
- group: build
  href: https://artifacts.apis.io/packdigital/packages/packdigital-packages.yml
  title: ''
  type: Packages
  url: packages/packdigital-packages.yml
- group: build
  href: https://artifacts.apis.io/packdigital/packages/packdigital-packages.yml
  title: ''
  type: SDKs
  url: packages/packdigital-packages.yml
- group: auth
  href: https://artifacts.apis.io/packdigital/authentication/packdigital-authentication.yml
  title: ''
  type: Authentication
  url: authentication/packdigital-authentication.yml
- group: design
  href: https://artifacts.apis.io/packdigital/conventions/packdigital-conventions.yml
  title: ''
  type: Conventions
  url: conventions/packdigital-conventions.yml
- group: design
  href: https://artifacts.apis.io/packdigital/data-model/packdigital-data-model.yml
  title: ''
  type: DataModel
  url: data-model/packdigital-data-model.yml
- group: design
  href: https://artifacts.apis.io/packdigital/conformance/packdigital-conformance.yml
  title: ''
  type: Conformance
  url: conformance/packdigital-conformance.yml
- group: design
  href: https://artifacts.apis.io/packdigital/errors/packdigital-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/packdigital-problem-types.yml
- group: design
  href: https://artifacts.apis.io/packdigital/components/packdigital-components.yml
  title: ''
  type: Components
  url: components/packdigital-components.yml
- group: agent
  href: https://artifacts.apis.io/packdigital/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Pack Digital is a digital experience platform purpose-built for Shopify Hydrogen that lets AI agents and human teams collaborate on headless storefronts: agents draft changes, the team reviews them in content releases, and you ship when ready. Pack pairs a visual Customizer, server-side A/B testing, media and localization, and the open-source Blueprint Hydrogen theme with a developer surface — a GraphQL Content Management API, JavaScript SDKs (@pack/client, @pack/react, @pack/hydrogen, @pack/types), and an official hosted MCP server for agent-native content editing, publishing, scheduling, and testing. Backed by Norwest Venture Partners.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/packdigital.png
layout: provider
mcp_servers:
- description: Official remote MCP server that connects AI assistants to Pack to search, edit, preview, publish, schedule, and A/B test Shopify Hydrogen storefront content. Backed by the Pack GraphQL Content Managem
  name: Packdigital MCP Server
  slug: pack
modified: '2026-07-20'
name: Packdigital
nav: Providers
network: true
overview: 'Packdigital is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Content Management, Headless Commerce, Shopify, and CMS.


  Packdigital''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 18 more developer resources.'
random_paper: 21
score:
  band: thin
  composite: 31.3
  coverage:
    artifact_dirs: 16
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 66.1
    discoverability: 65.0
    operational_transparency: 5.3
  previous_composite: 31.3
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/packdigital/packdigital-2026-08-07T191242.png
security:
- kind: authentication
  name: Packdigital Authentication
  slug: packdigital-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Packdigital Domain Security
  slug: packdigital-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: Create, review, and publish a storefront page
  slug: packdigital-publish-a-page
- name: Run and manage an A/B test via the Pack MCP server
  slug: packdigital-run-ab-test
- name: Schedule content to go live
  slug: packdigital-schedule-content
slug: packdigital
tags:
- Company
- Content Management
- Headless Commerce
- Shopify
- CMS
- A/B Testing
- GraphQL
- MCP
- Agents
- Storefront
- Shopify Hydrogen
website: https://packdigital.com
---
