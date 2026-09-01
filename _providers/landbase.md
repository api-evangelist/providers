---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 18.7
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The Landbase cloud gateway that landbase-cli calls in platform mode. It backs natural-language audience search and agent runs, dataset upload/lineage/download, record match, synchronous person/company
  name: Landbase Platform API
  slug: landbase-platform-api
artifact_total: 29
common:
- group: company
  title: ''
  type: Website
  url: https://www.landbase.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.landbase.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.landbase.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.landbase.com/docs/reference/search
- group: start
  title: ''
  type: GettingStarted
  url: https://www.landbase.com/docs/quickstart
- group: company
  title: ''
  type: Blog
  url: https://www.landbase.com/blog
- group: operate
  title: ''
  type: Support
  url: https://support.landbase.com/landbase/directories
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/landbaseapp
- group: commercial
  title: ''
  type: Pricing
  url: https://www.landbase.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://accounts.landbase.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://accounts.landbase.com/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.landbase.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.landbase.com/legal/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: security/landbase-trust-center.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/landbase-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: CLI
  url: cli/landbase-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/landbase-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/landbase-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/landbase-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/landbase-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/landbase-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/landbase-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/landbase-error-codes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/landbase-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/landbase-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/landbase-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/landbase-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/landbase-rate-limits.yml
created: '2026-08-23'
description: 'Landbase is a Palo Alto, California go-to-market (GTM) data and agentic-AI company whose platform builds, qualifies, enriches and activates B2B audiences from natural-language requests. Its GTM-1/GTM-2 Omni models sit behind a B2B database of 300M+ contacts with 1,500+ enrichment fields, an agentic search surface, lookalike expansion, AI lead qualification, and email/LinkedIn outbound campaign execution. Landbase''s programmable surface is deliberately agent-first rather than REST-first: the documented client is `landbase-cli`, a self-updating binary distributed from cli.landbase.com that talks to the cloud gateway at api.landbase.com, returns JSON on stdout and stable error codes on stderr, and ships a library of provider-authored Agent Skills for Claude Code and Codex. No OpenAPI description of the gateway is published; the gateway itself sits behind a Cloudflare bot challenge on every path except /.well-known/.'
image: https://cdn.prod.website-files.com/663db35157fcd223250841ff/665df6511f919f2ee06412ee_webclip-landbase.png
layout: provider
modified: '2026-08-23'
name: Landbase
nav: Providers
network: true
overview: 'Landbase publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Go-To-Market, Sales, Marketing, and B2B Data.


  Landbase''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 22 more developer resources.'
plans:
- name: Landbase Plans Pricing
  plan_count: 4
  slug: landbase-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 4
  name: Landbase Rate Limits
  slug: landbase-rate-limits
score:
  band: developing
  composite: 44.3
  coverage:
    artifact_dirs: 16
    catalog_gap: 54.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 66.7
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 50.0
  previous_composite: 44.3
  provenance:
    conformance: first-party
    mcp: derived
    skills: first-party
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Landbase Authentication
  slug: landbase-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Landbase Domain Security
  slug: landbase-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Landbase Trust Center
  slug: landbase-trust-center
  summary_line: trust center published
skill_count: 23
skills:
- name: contact-enrich
  slug: contact-enrich
- name: contacts-import
  slug: contacts-import
- name: dataset-management
  slug: dataset-management
- name: dataset-pipeline
  slug: dataset-pipeline
- name: dedupe-leads
  slug: dedupe-leads
- name: icp-capture
  slug: icp-capture
- name: landbase-email-campaigns
  slug: landbase-email-campaigns
- name: landbase-feedback
  slug: landbase-feedback
- name: landbase-linkedin-campaigns
  slug: landbase-linkedin-campaigns
- name: landbase-quickstart
  slug: landbase-quickstart
- name: landbase-search
  slug: landbase-search
- name: list-similarity-check
  slug: list-similarity-check
- name: lookalike-expansion
  slug: lookalike-expansion
- name: match-lookup
  slug: match-lookup
- name: presentation
  slug: presentation
- name: prospect-builder
  slug: prospect-builder
- name: qualify-leads
  slug: qualify-leads
- name: query-assist
  slug: query-assist
- name: tam-mapping
  slug: tam-mapping
- name: transcript-synthesis
  slug: transcript-synthesis
- name: workflow-enrich
  slug: workflow-enrich
- name: workflow-monitor
  slug: workflow-monitor
- name: workflow-transform
  slug: workflow-transform
slug: landbase
tags:
- Company
- Go-To-Market
- Sales
- Marketing
- B2B Data
- Data Enrichment
- Artificial Intelligence
- Agents
- Command Line Interface
- Lead Generation
website: https://www.landbase.com/
---
