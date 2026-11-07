---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 8.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: 1Clickwebsite Ai Agentic Access
  operation_count: 22
  slug: 1clickwebsite-ai-agentic-access
  summary_line: 22 operations · 11 acting
api_count: 1
apis:
- description: Create complete V2 websites, generate Lead Gen mini-sites, manage white-label agency requests, and edit completed WordPress sites.
  name: 1ClickWebsite API
  slug: 1clickwebsite-api
artifact_total: 18
common:
- group: design
  href: https://artifacts.apis.io/1clickwebsite-ai/conformance/1clickwebsite-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/1clickwebsite-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/1clickwebsite-ai/well-known/1clickwebsite-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/1clickwebsite-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/1clickwebsite-ai/hosts/1clickwebsite-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/1clickwebsite-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/1clickwebsite-ai/vendors/1clickwebsite-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/1clickwebsite-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.1clickwebsite.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.1clickwebsite.ai/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.1clickwebsite.ai/docs/plans
- group: start
  title: ''
  type: Login
  url: https://www.1clickwebsite.ai/login
- group: docs
  title: ''
  type: Documentation
  url: https://www.1clickwebsite.ai/docs
- group: company
  title: ''
  type: Blog
  url: https://www.1clickwebsite.ai/blog
- group: docs
  title: ''
  type: APIReference
  url: https://www.1clickwebsite.ai/docs/api
- group: auth
  href: https://artifacts.apis.io/1clickwebsite-ai/security/1clickwebsite-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/1clickwebsite-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://1clickwebsite.ai/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://1clickwebsite.ai/openapi.json
  - status: null
    url: https://www.1clickwebsite.ai/openapi.json
  - status: 401
    url: https://www.1clickwebsite.ai/api/mcp
  - status: 200
    url: https://1clickwebsite.ai/
  reason: partner-login
  state: gated
created: '2026-10-31'
description: 1ClickWebsite.ai provides a platform that launches SEO‑optimized WordPress sites in minutes. Users fill a brief intake form and the service automatically designs, builds, and deploys a professional site with built‑in SEO, content, and branding. It targets agencies and freelancers who need to deliver client‑ready websites quickly, offering plans starting at $49/month and handling over 5,000 sites generated. The platform includes features like lead‑generation tools, white‑label agency options, and AI‑assisted site editing, aiming to streamline the web‑development workflow and reduce time‑to‑launch for WordPress sites.
image: https://1clickwebsite.ai/brand/og-image.png
json_schemas:
- name: LeadGenBatchCreateRequest
  property_count: 12
  slug: 1clickwebsite-ai-lead-gen-batch-create-request
- name: LeadGenBatchUpdateRequest
  property_count: 6
  slug: 1clickwebsite-ai-lead-gen-batch-update-request
- name: LeadGenBatchUpdateResponse
  property_count: 12
  slug: 1clickwebsite-ai-lead-gen-batch-update-response
- name: SiteCreateRequest
  property_count: 35
  slug: 1clickwebsite-ai-site-create-request
- name: SiteStatus
  property_count: 12
  slug: 1clickwebsite-ai-site-status
- name: SiteTemplate
  property_count: 10
  slug: 1clickwebsite-ai-site-template
jsonld:
- class_count: 19
  name: 1Clickwebsite Ai Context
  property_count: 100
  slug: 1clickwebsite-ai-context
layout: provider
modified: '2026-10-31'
name: 1ClickWebsite.ai
nav: Providers
network: true
overview: '1ClickWebsite.ai publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, SEO, WordPress, Agency, and Automation.


  The 1ClickWebsite.ai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  1ClickWebsite.ai''s developer surface includes pricing, documentation, engineering blog, API reference, and 9 more developer resources.'
plans:
- name: 1Clickwebsite Ai Plans Pricing
  plan_count: 3
  slug: 1clickwebsite-ai-plans-pricing
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: 1ClickWebsite.ai API Rules
  rule_count: 16
  severity_counts:
    error: 11
    hint: 0
    info: 2
    warn: 3
  slug: 1clickwebsite-ai-rules
scopes:
- name: 1Clickwebsite Ai Scopes
  scope_count: 0
  slug: 1clickwebsite-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 28.1
  coverage:
    artifact_dirs: 23
    catalog_earned: 64.5
    catalog_earned_first_party: 12.0
    catalog_gap: 50.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.9
  facets:
    access_clarity: 53.9
    contract_governance: 18.2
    contract_quality: 20.7
    developer_ergonomics: 9.5
    discoverability: 66.1
    operational_transparency: 0.0
  previous_composite: 35.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: 1Clickwebsite Ai Authentication
  slug: 1clickwebsite-ai-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: 1Clickwebsite Ai Domain Security
  slug: 1clickwebsite-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 4
skills:
- name: lead-gen
  slug: 1clickwebsite-ai-lead-gen
- name: site-creation
  slug: 1clickwebsite-ai-site-creation
- name: site-editing-ocf
  slug: 1clickwebsite-ai-site-editing-ocf
- name: white-label-agency
  slug: 1clickwebsite-ai-white-label-agency
slug: 1clickwebsite-ai
tags:
- Company
- SEO
- WordPress
- Agency
- Automation
website: https://1clickwebsite.ai/
---
