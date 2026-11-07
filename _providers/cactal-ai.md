---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 61.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 87
  human_in_the_loop: 2
  name: Cactal Ai Agentic Access
  operation_count: 134
  slug: cactal-ai-agentic-access
  summary_line: 134 operations · 87 acting · 2 human-in-the-loop
api_count: 1
apis:
- description: Public API for Cactal platform
  name: Cactal API
  slug: cactal-api
- baseURL: https://api.cactal.ai/v1
  baseurl_source: declared
  description: Read first-party traffic analytics for a website and export datasets as CSV.
  name: Cactal Analytics API
  slug: cactal-ai-analytics-api
- baseURL: https://api.cactal.ai/v1
  baseurl_source: declared
  description: Create, scope, rotate, and revoke the API keys that authenticate programmatic and agent access.
  name: Cactal API keys API
  slug: cactal-ai-api-keys-api
- baseURL: https://api.cactal.ai/v1
  baseurl_source: declared
  description: Upload and manage website files and images served from the Cactal CDN.
  name: Cactal Assets API
  slug: cactal-ai-assets-api
- baseURL: https://api.cactal.ai/v1
  baseurl_source: declared
  description: Read the immutable record of actions performed in an organization by users and API keys.
  name: Cactal Audit log API
  slug: cactal-ai-audit-log-api
- baseURL: https://api.cactal.ai/v1
  baseurl_source: declared
  description: Read billing state and manage plans, site capacity, and prepaid usage balance. Every billing operation requires the organization owner role, which API keys cannot hold — today these operations are per
  name: Cactal Billing API
  slug: cactal-ai-billing-api
- baseURL: https://api.cactal.ai/v1
  baseurl_source: declared
  description: 'Define the content model: collections of structured content owned by a website.'
  name: Cactal CMS collections API
  slug: cactal-ai-cms-collections-api
- baseURL: https://api.cactal.ai/v1
  baseurl_source: declared
  description: Manage the typed fields that make up a collection schema.
  name: Cactal CMS fields API
  slug: cactal-ai-cms-fields-api
- baseURL: https://api.cactal.ai/v1
  baseurl_source: declared
  description: Create, query, publish, and organize the content entries inside a collection.
  name: Cactal CMS items API
  slug: cactal-ai-cms-items-api
- baseURL: https://api.cactal.ai/v1
  baseurl_source: declared
  description: Search and read the Cactal product documentation for concepts, guides, agent workflows, platform behavior, and API operations.
  name: Cactal Documentation API
  slug: cactal-ai-documentation-api
- baseURL: https://api.cactal.ai/v1
  baseurl_source: declared
  description: Manage platform subdomains and custom domains, including DNS verification and the primary domain.
  name: Cactal Domains API
  slug: cactal-ai-domains-api
- baseURL: https://api.cactal.ai/v1
  baseurl_source: declared
  description: Submit free-form product feedback from users and agents to the Cactal feedback inbox.
  name: Cactal Feedback API
  slug: cactal-ai-feedback-api
- baseURL: https://api.cactal.ai/v1
  baseurl_source: declared
  description: Read and triage website form submissions, manage notification recipients, and configure per-form settings. Visitors submit to `POST /_cactal/forms/{name}` on the website itself.
  name: Cactal Forms API
  slug: cactal-ai-forms-api
- baseURL: https://api.cactal.ai/v1
  baseurl_source: declared
  description: Generate reference-guided website images that are stored as ordinary Cactal CDN assets.
  name: Cactal Media generation API
  slug: cactal-ai-media-generation-api
- baseURL: https://api.cactal.ai/v1
  baseurl_source: declared
  description: Manage organizations, members, and organization-wide invitations.
  name: Cactal Organizations API
  slug: cactal-ai-organizations-api
- baseURL: https://api.cactal.ai/v1
  baseurl_source: declared
  description: Upload private durable reference material that the website agent can search, read, and inspect.
  name: Cactal Project Context API
  slug: cactal-ai-project-context-api
- baseURL: https://api.cactal.ai/v1
  baseurl_source: declared
  description: Validate, build, publish, and roll back website versions.
  name: Cactal Publishing API
  slug: cactal-ai-publishing-api
- baseURL: https://api.cactal.ai/v1
  baseurl_source: declared
  description: Manage a website's write-only secrets, which its server functions read from `env`. Values can be set and deleted but are never returned.
  name: Cactal Secrets API
  slug: cactal-ai-secrets-api
- baseURL: https://api.cactal.ai/v1
  baseurl_source: declared
  description: Inspect a website's server function runs and run its `http` functions on the draft. Visitors call `http` functions with `POST /_framework/server/{name}` on the website itself.
  name: Cactal Server functions API
  slug: cactal-ai-server-functions-api
- baseURL: https://api.cactal.ai/v1
  baseurl_source: declared
  description: Read and edit the framework source files of a website draft. Mutations require an edit lease.
  name: Cactal Source code API
  slug: cactal-ai-source-code-api
- baseURL: https://api.cactal.ai/v1
  baseurl_source: declared
  description: 'Look at the public web for a website''s work: screenshots and measurements of external pages, a business''s own pages read into profiles, and many images at once on numbered contact sheets.'
  name: Cactal Web research API
  slug: cactal-ai-web-research-api
- baseURL: https://api.cactal.ai/v1
  baseurl_source: declared
  description: Grant, list, and revoke website-scoped editor access, and invite collaborators to a single website by email.
  name: Cactal Website editors API
  slug: cactal-ai-website-editors-api
- baseURL: https://api.cactal.ai/v1
  baseurl_source: declared
  description: Create and manage websites — the top-level resource that owns source code, content, assets, domains, and analytics.
  name: Cactal Websites API
  slug: cactal-ai-websites-api
artifact_total: 34
common:
- group: agent
  href: https://artifacts.apis.io/cactal-ai/agentic-access/cactal-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cactal-ai-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/cactal-ai/plans/cactal-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cactal-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/cactal-ai/rules/cactal-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/cactal-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/cactal-ai/json-ld/cactal-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cactal-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/cactal-ai/vocabulary/cactal-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cactal-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/cactal-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/cactal-ai/data-model/cactal-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cactal-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/cactal-ai/conventions/cactal-ai-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/cactal-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/cactal-ai/conventions/cactal-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cactal-ai-conventions.yml
- group: auth
  href: https://artifacts.apis.io/cactal-ai/authentication/cactal-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cactal-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/cactal-ai/errors/cactal-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cactal-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cactal-ai/conformance/cactal-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cactal-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cactal-ai/llms/cactal-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cactal-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/cactal-ai/a2a/cactal-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/cactal-ai-a2a.yml
- group: agent
  href: https://artifacts.apis.io/cactal-ai/well-known/cactal-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cactal-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/cactal-ai/hosts/cactal-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cactal-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/cactal-ai/vendors/cactal-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cactal-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cactal.ai/legal/terms
- group: auth
  title: ''
  type: Security
  url: https://cactal.ai/templates/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cactal.ai/legal/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://cactal.ai/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://cactal.ai/templates/news
- group: start
  title: ''
  type: Login
  url: https://cactal.ai/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://cactal.ai/developers
- group: company
  title: ''
  type: Blog
  url: https://cactal.ai/templates/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://cactal.ai/docs/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cactal.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://cactal.ai/llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cactal
- group: auth
  href: https://artifacts.apis.io/cactal-ai/security/cactal-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cactal-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cactal.ai/
created: '2026-11-03'
description: Cactal is the agent‑native website platform for building, publishing, hosting, and operating production websites. It offers AI‑driven site creation, a CMS, forms, SEO, analytics, and free starter plans, with paid options for custom domains and advanced features. The company is based in Austin, Texas, and focuses on empowering agencies and developers to deliver high‑quality web experiences quickly.
image: https://cdn.cactal.app/website-assets/-wwVLhayoYvbr-MwKOQRt.jpg
jsonld:
- class_count: 1
  name: Cactal Ai Context
  property_count: 4
  slug: cactal-ai-context
layout: provider
modified: '2026-11-03'
name: Cactal
nav: Providers
network: true
overview: 'Cactal publishes 23 API contracts indexed on the [APIs.io](https://apis.io/) network, including Analytics API, API keys API, Assets API, and 20 more. Tagged areas include Artificial Intelligence, Website Builder, CMS, SEO, and Analytics.


  The Cactal catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Cactal''s developer surface includes authentication, pricing, engineering blog, getting-started guide, documentation, API reference, and 25 more developer resources.'
plans:
- name: Cactal Ai Plans Pricing
  plan_count: 3
  slug: cactal-ai-plans-pricing
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 101
  extends:
  - spectral:oas
  name: Cactal API Rules
  rule_count: 60
  severity_counts:
    error: 52
    hint: 0
    info: 1
    warn: 7
  slug: cactal-ai-rules
score:
  band: developing
  composite: 41.7
  coverage:
    artifact_dirs: 23
    catalog_earned: 59.8
    catalog_earned_first_party: 12.0
    catalog_gap: 55.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 52.7
    developer_ergonomics: 33.9
    discoverability: 67.0
    operational_transparency: 7.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 22
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Cactal Ai Authentication
  slug: cactal-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Cactal Ai Domain Security
  slug: cactal-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 5
skills:
- name: cactal-ai-billing-change-plan
  slug: cactal-ai-billing-change-plan
- name: cactal-ai-invoke-and-monitor-function
  slug: cactal-ai-invoke-and-monitor-function
- name: cactal-ai-list-organizations
  slug: cactal-ai-list-organizations
- name: cactal-ai-project-context-list-and-get
  slug: cactal-ai-project-context-list-and-get
- name: cactal-ai-upload-asset
  slug: cactal-ai-upload-asset
slug: cactal-ai
tags:
- Artificial Intelligence
- Website Builder
- CMS
- SEO
- Analytics
website: https://cactal.ai/
---
